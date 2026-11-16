"""Local test of core stability at the next scale (no full build of the larger system).
Usage: py -B next_junction.py g attach W
  g in {id, swap}: orientation of the diagonal block E of side 1024 whose tail is extended.
  attach = O4: E is the third child of F (side 2048, orientation g), attached block O4(F).
  attach = O2: E is the first child of P (side 2048, orientation g o swap), attached block O2(P).
  W: rank window on each side of the junction (must be >= the proved bound Dmax(1023)).
Computes the crossing constraints at the junction (window kernel on the 2048 curve), the
interface set Z (old endpoints, in E-local ranks), then on A = Tail(E) (from the 1024 build):
the certified 3-core K_A, the Z-anchored certified core K_A^Z, and the stability criterion
 (i) K_A and Z disjoint, (ii) no constraint of A between K_A and K_A^Z minus K_A.
"""
import sys, time
import numpy as np
import numba as nb
from blk import hilbert_array, legs, build, weighted_core

g, attach, W = sys.argv[1], sys.argv[2], int(sys.argv[3])
M, S, N = 3, 32, 1024
t0 = time.time()
h = g if attach == "O4" else ("swap" if g == "id" else "id")
xy = hilbert_array(2 * N)
if h == "swap":
    xy = xy[:, ::-1].copy()
J = 3 * N * N if attach == "O4" else N * N
off = 2 * N * N if attach == "O4" else 0          # E-local rank = global rank - off
odd = (2 * xy[:, 0] + 1).astype(np.int64); even = (2 * xy[:, 1] + 2).astype(np.int64)
# sanity: E's cells as placed equal the 1024 block of orientation g, translated
xyE = hilbert_array(N)
if g == "swap":
    xyE = xyE[:, ::-1]
shift = N if attach == "O4" else 0
assert (xy[off:off + N * N] == xyE + shift).all(), "child embedding mismatch"
P = legs(4 * N - 1, S)
qs, offs, Ys, Ls = [], [0], [], []
for q in sorted(P):
    qs.append(q)
    for Y, L in P[q]:
        Ys.append(Y); Ls.append(L)
    offs.append(len(Ys))


@nb.njit(cache=True)
def kern(odd, even, M, J, W, qs, offs, Ys, Ls, out, Ymax):
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
            if d < 1 or d > 2 * W:
                continue
            rlo = max(J - W, J - d); rhi = J          # r < J <= r + d, both within the window
            for r in range(rlo, rhi):
                if r + d >= J + W or r + d >= odd.shape[0]:
                    continue
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
                        out[cnt, 0] = r; out[cnt, 1] = r + d; out[cnt, 2] = delta; out[cnt, 3] = q
                    cnt += 1
        for k in range(offs[t], offs[t + 1]):
            look[Ys[k]] = 0
    return cnt


out = np.zeros((2_000_000, 4), dtype=np.int64)
cnt = kern(odd, even, M, J, W, np.array(qs), np.array(offs), np.array(Ys), np.array(Ls), out, 4 * N)
X = np.unique(out[:cnt], axis=0)
T = xy[:, 1] - xy[:, 0]
print(f"g={g} attach={attach} (2048 orientation {h}) J={J} W={W}: crossing triples {len(X)}  ({time.time()-t0:.1f}s)")
print(f"  max depth J-r {int((J - X[:,0]).max())}, max u-J {int((X[:,1]-J).max())}, gaps {len(np.unique(X[:,3]))} in [{X[:,3].min()},{X[:,3].max()}]")
print(f"  old endpoint T in [{T[X[:,0]].min()},{T[X[:,0]].max()}], new endpoint T in [{T[X[:,1]].min()},{T[X[:,1]].max()}]")
Z = np.unique(X[:, 0]) - off
# A = Tail(E): terminal segment of the 1024 block of orientation g
xy1, E1 = build(N, S, M, g, "cand")
lo = N * N - (N * N - 1) // 3 - 1
A = E1[E1[:, 0] >= lo]
n = N * N
assert Z.min() >= lo
KA = weighted_core(n, A, M, mod=M)
KAl = np.unique(KA[:, :2])
# Z-anchored certified core: Z labels never peeled
key = np.stack([A[:, 0], A[:, 1], A[:, 2] % M], axis=1)
_, first = np.unique(key, axis=0, return_index=True)
Ac = A[np.sort(first)]
anchor = np.zeros(n, dtype=bool); anchor[Z] = True
alive = np.ones(len(Ac), dtype=bool)
while True:
    deg = np.bincount(Ac[alive, 0], minlength=n) + np.bincount(Ac[alive, 1], minlength=n)
    bad = (deg < M) & ~anchor
    kill = alive & (bad[Ac[:, 0]] | bad[Ac[:, 1]])
    if not kill.any():
        break
    alive &= ~kill
KZ = Ac[alive]
KZl = np.unique(KZ[:, :2]) if len(KZ) else np.array([], dtype=np.int64)
inKA = np.zeros(n, dtype=bool); inKA[KAl] = True
inKZ = np.zeros(n, dtype=bool); inKZ[KZl] = True
extra = inKZ & ~inKA
c1 = int(inKA[Z].sum())
bridge = (inKA[A[:, 0]] & extra[A[:, 1]]) | (inKA[A[:, 1]] & extra[A[:, 0]])
print(f"  interface Z: {len(Z)} labels of Tail(E); K_A: {len(KAl)} labels; K_A^Z: {len(KZl)} labels ({int(extra.sum())} outside K_A)")
print(f"  (i) |K_A cap Z| = {c1};  (ii) constraints of A between K_A and K_A^Z minus K_A: {int(bridge.sum())}")
print(f"  rank gap between K_A and the junction: {N*N - 1 - int(KAl.max())} (deepest Z label at depth {N*N - int(Z.min())})")
print(f"  STABLE: {c1 == 0 and int(bridge.sum()) == 0}   ({time.time()-t0:.1f}s)")
# DEC criterion: no component of the graph induced on K_A^Z holds both a label before
# J_9 (the start of the last block W_9 of Tail(E)) and a label of Z.
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
J9 = N * N - (N // 2) ** 2
a = np.searchsorted(KZl, KZ[:, 0]); b = np.searchsorted(KZl, KZ[:, 1])
nc, lab = connected_components(coo_matrix((np.ones(len(KZ)), (a, b)), shape=(len(KZl),) * 2), directed=False)
isZ = np.isin(KZl, Z)
viol = [c for c in range(nc) if ((lab == c) & (KZl < J9)).any() and ((lab == c) & isZ).any()]
print(f"  K_A^Z components {nc}; components holding a label before J_9 and a Z label: {len(viol)}"
      f"  -> DEC at this junction {'PROVED' if not viol else 'not proved'}")
for c in viol:
    L = KZl[lab == c]
    print(f"    comp {c}: {len(L)} labels, before J_9 {int((L < J9).sum())}, Z labels {int(isZ[lab == c].sum())}")
