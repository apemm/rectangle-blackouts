"""Build the main-diagonal block system G_B^o (Corollary A1 of
hilbert_p_height_independent_cores.md) and peel it to its weighted M-core.

Usage: py -B build_core.py B S M orient(id|swap) version(gen|cand) [outprefix]
  gen  = owner of the completion rows outside the block (G_B^o, genuine rivals)
  cand = no owner test (candidate version, a superset)
Writes <outprefix>_core.npy (int32 rows r, u, delta of the weighted M-core) if given.
Independent reimplementation (numba); only the Hilbert recursion is copied from
the archive definition (H_2n quadrants Q1 transposed, Q2, Q3 translated, Q4 reflected).
"""
import sys, os, time
import numpy as np
import numba as nb


def hilbert_array(q):
    xy = np.zeros((1, 2), dtype=np.int64); n = 1
    while n < q:
        b = n * n
        nxt = np.empty((4 * b, 2), dtype=np.int64)
        nxt[:b] = xy[:, ::-1]
        nxt[b:2 * b] = xy + (0, n)
        nxt[2 * b:3 * b] = xy + (n, n)
        nxt[3 * b:, 0] = 2 * n - 1 - xy[:, 1]
        nxt[3 * b:, 1] = n - 1 - xy[:, 0]
        xy = nxt; n *= 2
    return xy


def pyth_by_q(Ymax, S):
    """q -> list of (Y, L) with Y odd <= Ymax, X = S q, X^2 + Y^2 = L^2."""
    out = {}
    for Y in range(1, Ymax + 1, 2):
        Y2 = Y * Y
        u = 1
        while u < Y:
            if Y2 % u == 0:
                w = Y2 // u
                X = (w - u) // 2
                assert X * X + Y2 == ((w + u) // 2) ** 2
                if X > 0 and X % S == 0:
                    out.setdefault(X // S, []).append((Y, (w + u) // 2))
            u += 2
    return out


@nb.njit(cache=True)
def kernel(odd, even, B, M, owner_test, qs, offs, Ys, Ls, out):
    n = odd.shape[0]
    look = np.zeros(4 * B + 8, dtype=np.int64)
    cnt = 0
    for t in range(qs.shape[0]):
        q = qs[t]
        for k in range(offs[t], offs[t + 1]):
            look[Ys[k]] = Ls[k]
        d1 = q // M
        d2 = (q + M - 1) // M
        for dd in range(2):
            d = d1 if dd == 0 else d2
            if dd == 1 and d2 == d1:
                continue
            delta = q - M * d
            if d < 1 or d >= n or delta > M - 1 or delta < -(M - 1):
                continue
            for r in range(n - d):
                for role in range(2):
                    if role == 0:
                        a = odd[r]; b = even[r + d]
                    else:
                        a = odd[r + d]; b = even[r]
                    y = b - a
                    if y < 0:
                        y = -y
                    L = look[y]
                    if L == 0:
                        continue
                    s = a + b
                    lo = (s - L) // 2
                    hi = (s + L) // 2
                    if lo % 2 == 1:
                        oo = lo; ee = hi
                    else:
                        oo = hi; ee = lo
                    oi = (oo - 1) // 2
                    oj = (ee - 2) // 2
                    if owner_test and oi >= 0 and oi < B and oj >= 0 and oj < B:
                        continue
                    if cnt < out.shape[0]:
                        out[cnt, 0] = r
                        out[cnt, 1] = r + d
                        out[cnt, 2] = delta
                    cnt += 1
        for k in range(offs[t], offs[t + 1]):
            look[Ys[k]] = 0
    return cnt


def build(B, S, M, orient, version):
    xy = hilbert_array(B)
    if orient == "swap":
        xy = xy[:, ::-1]
    odd = np.ascontiguousarray(2 * xy[:, 0] + 1).astype(np.int64)
    even = np.ascontiguousarray(2 * xy[:, 1] + 2).astype(np.int64)
    P = pyth_by_q(2 * B - 1, S)
    qs, offs, Ys, Ls = [], [0], [], []
    for q in sorted(P):
        qs.append(q)
        for Y, L in P[q]:
            Ys.append(Y); Ls.append(L)
        offs.append(len(Ys))
    out = np.zeros((8_000_000, 3), dtype=np.int64)
    cnt = kernel(odd, even, B, M, version == "gen", np.array(qs, dtype=np.int64),
                 np.array(offs, dtype=np.int64), np.array(Ys, dtype=np.int64),
                 np.array(Ls, dtype=np.int64), out)
    assert cnt <= out.shape[0]
    E = np.unique(out[:cnt], axis=0)          # distinct triples (r, u, delta)
    return B * B, E


def weighted_core(n, E, k):
    alive = np.ones(len(E), dtype=bool)
    while True:
        deg = np.bincount(E[alive, 0], minlength=n) + np.bincount(E[alive, 1], minlength=n)
        bad = deg < k
        kill = alive & (bad[E[:, 0]] | bad[E[:, 1]])
        if not kill.any():
            return E[alive]
        alive &= ~kill


if __name__ == "__main__":
    B, S, M = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    orient, version = sys.argv[4], sys.argv[5]
    t0 = time.time()
    n, E = build(B, S, M, orient, version)
    C = weighted_core(n, E, M)
    nv = len(np.unique(C[:, :2])) if len(C) else 0
    print(f"B={B} S={S} M={M} {orient} {version}: constraints {len(E)}, "
          f"weighted {M}-core labels {nv}, constraints {len(C)}  ({time.time()-t0:.1f}s)")
    if len(sys.argv) > 6:
        np.save(sys.argv[6] + "_core.npy", C.astype(np.int32))
