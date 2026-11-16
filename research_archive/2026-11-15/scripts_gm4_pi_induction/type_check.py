"""Sanity checks of the block-type recursion (no census; fixed small systems).
(1) every aligned block of the side-2^K curve has local curve in {H, aH, tH, rH}
    (a = anti-transpose, t = transpose, r = rotation by 180), and the children rule
    id: (2k,swap),(2k+1,id),(2k,id),(2k-1,id); swap: (2k,id),(2k-1,swap),(2k,swap),(2k+1,swap).
(2) cand systems: H and aH placed at the same offset give identical triple sets; H and tH differ.
(3) the second child of W_j = O4(P_{j+1}) (id P) has the same cand system as W_{j-1} = O4(P_j).
Uses the archive kernel (blk.py, read-only import)."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # local copy of the archive blk.py
import numpy as np
from blk import hilbert_array, legs, kernel

t0 = time.time()
K = 8
N = 2 ** K
xy = hilbert_array(N)
rank = np.empty((N, N), dtype=np.int64)
rank[xy[:, 0], xy[:, 1]] = np.arange(N * N)


def forms(s):
    H = hilbert_array(s)
    a = np.stack([s - 1 - H[:, 1], s - 1 - H[:, 0]], 1)
    t = H[:, ::-1]
    r = s - 1 - H
    return {"H": H, "aH": a, "tH": t, "rH": r}


CLS = {"H": "id", "aH": "id", "tH": "swap", "rH": "swap"}
bad = 0; checked = 0
for lev in range(2, K):
    s = 2 ** lev; q = s // 2
    F = forms(s); Fq = forms(q)
    for X0 in range(0, N, s):
        for Y0 in range(0, N, s):
            r0 = rank[X0:X0 + s, Y0:Y0 + s].min()
            loc = xy[r0:r0 + s * s] - (X0, Y0)
            name = [n for n, f in F.items() if (f == loc).all()]
            assert len(name) == 1, (lev, X0, Y0)
            o = CLS[name[0]]
            k = (Y0 - X0) // s
            # children in rank order
            ch = []
            for i in range(4):
                c = loc[i * q * q]
                cx, cy = (c[0] // q) * q, (c[1] // q) * q
                cl = xy[r0 + i * q * q: r0 + (i + 1) * q * q] - (X0 + cx, Y0 + cy)
                nm = [n for n, f in Fq.items() if (f == cl).all()]
                ch.append(((Y0 + cy - X0 - cx) // q, CLS[nm[0]]))
            exp = ([(2 * k, "swap"), (2 * k + 1, "id"), (2 * k, "id"), (2 * k - 1, "id")] if o == "id"
                   else [(2 * k, "id"), (2 * k - 1, "swap"), (2 * k, "swap"), (2 * k + 1, "swap")])
            checked += 1
            bad += (ch != exp)
    if lev >= 6:
        break
print("children rule: blocks checked", checked, "mismatches", bad, round(time.time() - t0, 1), "s")

M, S = 3, 32


def cand(cells, Ymax):
    odd = np.ascontiguousarray(2 * cells[:, 0] + 1).astype(np.int64)
    even = np.ascontiguousarray(2 * cells[:, 1] + 2).astype(np.int64)
    P = legs(Ymax, S)
    qs, offs, Ys, Ls = [], [0], [], []
    for qq in sorted(P):
        qs.append(qq)
        for Y, L in P[qq]:
            Ys.append(Y); Ls.append(L)
        offs.append(len(Ys))
    out = np.zeros((4_000_000, 4), dtype=np.int64)
    cnt = kernel(odd, even, (Ymax + 8) // 4 + 1, M, False, np.array(qs, dtype=np.int64),
                 np.array(offs, dtype=np.int64), np.array(Ys, dtype=np.int64),
                 np.array(Ls, dtype=np.int64), out)
    assert cnt <= len(out)
    return np.unique(out[:cnt], axis=0)


s = 256
F = forms(s)
for c in (s, 2 * s, -s, -3 * s):
    X0, Y0 = 4096, 4096 + c
    sysA = cand(F["H"] + (X0, Y0), 2 * (abs(c) + s) + 3)
    sysB = cand(F["aH"] + (X0, Y0), 2 * (abs(c) + s) + 3)
    sysC = cand(F["tH"] + (X0, Y0), 2 * (abs(c) + s) + 3)
    print(f"offset {c}: |H|={len(sysA)} |aH|={len(sysB)} equal={np.array_equal(sysA, sysB)} |tH|={len(sysC)} equal={np.array_equal(sysA, sysC)}")

# (3) corner child of W_j versus W_{j-1}, inside the id block of side 2^K
for j in (7, 8):
    m = 2 ** j                        # W_j = O4(P_{j+1}) of the id block [0, 2m)^2: ranks [3m^2, 4m^2)
    big = hilbert_array(2 * m)
    Wj = big[3 * m * m: 4 * m * m]
    small = hilbert_array(m)
    Wjm1 = small[3 * (m // 2) ** 2:]  # W_{j-1} = O4 of the id block [0, m)^2
    child2 = Wj[(m // 2) ** 2: 2 * (m // 2) ** 2]
    shift = child2[0] - Wjm1[0]
    same_cells = (child2 - shift == Wjm1).all()
    A = cand(child2, 4 * m + 3); B = cand(Wjm1, 4 * m + 3)
    print(f"j={j}: second child = W_(j-1) translated by {tuple(shift)} (diagonal: {shift[0] == shift[1]}): {same_cells}; "
          f"cand systems equal: {np.array_equal(A, B)} ({len(A)} triples)")
print("total", round(time.time() - t0, 1), "s")
