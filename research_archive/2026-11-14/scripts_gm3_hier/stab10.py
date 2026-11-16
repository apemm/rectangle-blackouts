"""Exact test of core stability at the 1024 -> 2048 junction, by monotonicity of cores.
Usage: py -B stab10.py g attach w0
Builds the cand system induced on ranks [J - |Tail_1024| - 1, J + w0) of the 2048 curve
(orientation as in next_junction.py), takes its certified 3-core K_win, and reports the
components of K_win that contain both labels of K_A (the certified core of the old tail
alone) and labels of W.  Since K_win lies inside the certified core of the whole segment,
one such component proves that K_A is not a union of components of the larger core.
"""
import sys, time
import numpy as np
import numba as nb
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
from blk import hilbert_array, legs, weighted_core

g, attach, w0 = sys.argv[1], sys.argv[2], int(sys.argv[3])
M, S, N = 3, 32, 1024
t0 = time.time()
h = g if attach == "O4" else ("swap" if g == "id" else "id")
xy = hilbert_array(2 * N)
if h == "swap":
    xy = xy[:, ::-1].copy()
J = 3 * N * N if attach == "O4" else N * N
lo = J - (N * N - 1) // 3 - 1
hi = J + w0
odd = (2 * xy[:, 0] + 1).astype(np.int64); even = (2 * xy[:, 1] + 2).astype(np.int64)
P = legs(4 * N - 1, S)
qs, offs, Ys, Ls = [], [0], [], []
for q in sorted(P):
    qs.append(q)
    for Y, L in P[q]:
        Ys.append(Y); Ls.append(L)
    offs.append(len(Ys))


@nb.njit(cache=True)
def kern(odd, even, M, lo, hi, qs, offs, Ys, Ls, out, Ymax):
    look = np.zeros(Ymax + 8, dtype=np.int64)
    cnt = 0
    for t in range(qs.shape[0]):
        q = qs[t]
        for k in range(offs[t], offs[t + 1]):
            look[Ys[k]] = Ls[k]
        for dd in range(2):
            d = q // M if dd == 0 else (q + M - 1) // M
            if dd == 1 and d == q // M:
                continue
            delta = q - M * d
            if d < 1 or d >= hi - lo:
                continue
            for r in range(lo, hi - d):
                for role in range(2):
                    if role == 0:
                        a = odd[r]; b = even[r + d]
                    else:
                        a = odd[r + d]; b = even[r]
                    y = b - a
                    if y < 0:
                        y = -y
                    if look[y] == 0:
                        continue
                    if cnt < out.shape[0]:
                        out[cnt, 0] = r; out[cnt, 1] = r + d; out[cnt, 2] = delta
                    cnt += 1
        for k in range(offs[t], offs[t + 1]):
            look[Ys[k]] = 0
    return cnt


out = np.zeros((6_000_000, 3), dtype=np.int64)
cnt = kern(odd, even, M, lo, hi, np.array(qs), np.array(offs), np.array(Ys), np.array(Ls), out, 4 * N)
assert cnt <= len(out)
E = np.unique(out[:cnt], axis=0)
print(f"g={g} attach={attach}: window [{lo},{hi}) junction {J}: triples {len(E)}  ({time.time()-t0:.1f}s)")
n = 4 * N * N
EA = E[E[:, 1] < J]
KA = weighted_core(n, EA, M, mod=M)
KAl = np.unique(KA[:, :2])
Kw = weighted_core(n, E, M, mod=M)
labs = np.unique(Kw[:, :2])
a = np.searchsorted(labs, Kw[:, 0]); b = np.searchsorted(labs, Kw[:, 1])
nc, lab = connected_components(coo_matrix((np.ones(len(Kw)), (a, b)), shape=(len(labs),) * 2), directed=False)
inKA = np.isin(labs, KAl)
print(f"  K_A (old tail alone): {len(KAl)} labels; K_win: {len(labs)} labels, {nc} components")
bad = 0
for c in range(nc):
    sel = lab == c
    nk, nw, no = int((sel & inKA).sum()), int((sel & (labs >= J)).sum()), int((sel & ~inKA & (labs < J)).sum())
    if nk and nw:
        bad += 1
        print(f"    component {c}: {nk} labels of K_A, {no} other old labels, {nw} labels of W -> K_A merges with W")
# DEC check: does a component of K_win span both J_9 (start of W_9) and J (start of W_10)?
J9 = J - (N // 2) ** 2
for c in range(nc):
    L = labs[lab == c]
    a8, a9, a10 = int((L < J9).sum()), int(((L >= J9) & (L < J)).sum()), int((L >= J).sum())
    print(f"    comp {c}: {len(L)} labels: before J9 {a8}, in W_9 {a9}, in W_10 {a10}"
          + ("   <-- spans J9 and J10" if a8 and a10 else ""))
# certificate of one merging path: a core triple joining a K_A label to a non-K_A label
cross = Kw[(Kw[:, 0] < J) & (Kw[:, 1] >= J)]
print(f"  core triples across the junction in K_win: {len(cross)}; of them with the old end in K_A: {int(np.isin(cross[:,0], KAl).sum())}")
print(f"  STABILITY REFUTED: {bad > 0}  ({time.time()-t0:.1f}s)")
