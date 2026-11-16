"""The corner segment Gamma_11^g = post(W_10) + pre(W_11) on the 4096 curve (cand, S=32, M=3).
F = side-4096 diagonal block of orientation g, E = C3(F), W_10 = O4(E), W_11 = O4(F).
Builds the window [p10 - pad, p11 + pad), p_i = rank of the corner cell of W_i, checks that no
triple crosses p10 or p11 (corner-cut theorem), and reports the certified 3-core of Gamma_11
and its components.  Usage: py -B gamma11.py g pad"""
import sys, time
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
from common import hilbert_array, legs, window_triples, certified_classes, core

g, pad = sys.argv[1], int(sys.argv[2])
N = 2048
R = lambda m: (m * m - 1) // 3
J11 = 3 * N * N; J10 = J11 - (N // 2) ** 2
p10, p11 = J10 + R(N // 2), J11 + R(N)
lo, hi = p10 - pad, p11 + pad
t0 = time.time()
xy = hilbert_array(2 * N)
if g == "swap":
    xy = xy[:, ::-1].copy()
xw = xy[lo:hi].astype(np.int64); del xy
T = xw[:, 1] - xw[:, 0]
assert abs(T[p10 - lo]) == 1 and abs(T[p11 - lo]) == 1
E = window_triples(2 * xw[:, 0] + 1, 2 * xw[:, 1] + 2, 0, hi - lo, legs(4 * N - 1))
a, b = p10 - lo, p11 - lo
for name, p in (("p10", a), ("p11", b)):
    print(f"{name}: crossing triples {int(((E[:, 0] < p) & (E[:, 1] > p)).sum())}, incident {int(((E[:, 0] == p) | (E[:, 1] == p)).sum())}")
G = E[(E[:, 0] >= a) & (E[:, 1] < b)]
print(f"Gamma_11^{g}: {b - a} labels, {len(G)} triples  ({time.time()-t0:.1f}s)", flush=True)
K = core(hi - lo, certified_classes(G))
labs = np.unique(K[:, :2])
jl = J11 - lo
print(f"certified 3-core: {len(labs)} labels ({int((labs < jl).sum())} in post(W_10), {int((labs >= jl).sum())} in pre(W_11)), {len(K)} classes  ({time.time()-t0:.1f}s)", flush=True)
ia = np.searchsorted(labs, K[:, 0]); ib = np.searchsorted(labs, K[:, 1])
nc, lab = connected_components(coo_matrix((np.ones(len(K)), (ia, ib)), shape=(len(labs),) * 2), directed=False)
sz = np.bincount(lab); old = np.bincount(lab, weights=labs < jl)
o = np.argsort(-sz)
print(f"components {nc}: " + ", ".join(f"{sz[c]} ({int(old[c])}/{sz[c]-int(old[c])})" for c in o[:12]))
print(f"|T| range of core labels: [{int(np.abs(T[labs]).min())}, {int(np.abs(T[labs]).max())}]  ({time.time()-t0:.1f}s)")
