"""Exact certified-3 test of one two-block system Pi = W_9 + W_10 at the 1024 -> 2048 junction.
Usage: py -B solve_pi.py g attach [limit] [seeds]
  (g, attach) as in next_junction.py.  Builds the cand system induced on
  [J - 512^2, J + 1024^2) of the 2048 curve, takes the certified 3-core, solves each
  component in certified mode, extends by reverse peeling, verifies every triple, and
  saves pi_<g>_<attach>_sol.npy (int8 per rank of Pi) on success.
"""
import sys, time, random
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
import stab10_kern as sk
from blk import hilbert_array, legs, weighted_core
from listsolve import solve

g, attach = sys.argv[1], sys.argv[2]
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 3_000_000
nseeds = int(sys.argv[4]) if len(sys.argv) > 4 else 3
M, S, N = 3, 32, 1024
t0 = time.time()
h = g if attach == "O4" else ("swap" if g == "id" else "id")
xy = hilbert_array(2 * N)
if h == "swap":
    xy = xy[:, ::-1].copy()
J = 3 * N * N if attach == "O4" else N * N
lo, hi = J - (N // 2) ** 2, J + N * N
odd = (2 * xy[:, 0] + 1).astype(np.int64); even = (2 * xy[:, 1] + 2).astype(np.int64)
P = legs(4 * N - 1, S)
qs, offs, Ys, Ls = [], [0], [], []
for q in sorted(P):
    qs.append(q)
    for Y, L in P[q]:
        Ys.append(Y); Ls.append(L)
    offs.append(len(Ys))
out = np.zeros((9_000_000, 3), dtype=np.int64)
cnt = sk.kern(odd, even, M, lo, hi, np.array(qs), np.array(offs), np.array(Ys), np.array(Ls), out, 4 * N)
assert cnt <= len(out)
E = np.unique(out[:cnt], axis=0)
print(f"Pi({g},{attach}): ranks [{lo},{hi}), triples {len(E)}  ({time.time()-t0:.1f}s)", flush=True)
n = 4 * N * N
K = weighted_core(n, E, M, mod=M)
labs = np.unique(K[:, :2])
a = np.searchsorted(labs, K[:, 0]); b = np.searchsorted(labs, K[:, 1])
nc, lab = connected_components(coo_matrix((np.ones(len(K)), (a, b)), shape=(len(labs),) * 2), directed=False)
print(f"  certified 3-core: {len(labs)} labels, {len(K)} classes, {nc} components  ({time.time()-t0:.1f}s)", flush=True)
val = -np.ones(n, dtype=np.int64)
ok = True
for c in range(nc):
    V = labs[lab == c]
    Ek = K[lab[a] == c]
    res = None
    for sd in range(nseeds):
        Vl = V.tolist()
        if sd:
            random.Random(sd).shuffle(Vl)
        res, s, nodes = solve(Vl, Ek.tolist(), M, {}, limit)
        if res != "LIMIT":
            break
    print(f"    comp {c}: {len(V)} labels (W_9 {int((V < J).sum())}, W_10 {int((V >= J).sum())}): {res}, nodes {nodes}  ({time.time()-t0:.1f}s)", flush=True)
    if res == "SAT":
        for v, x in s.items():
            val[v] = x
    else:
        ok = False
if ok:
    # reverse peeling on certified classes over all labels of Pi
    key = np.stack([E[:, 0], E[:, 1], E[:, 2] % M], axis=1)
    _, first = np.unique(key, axis=0, return_index=True)
    Ec = E[np.sort(first)]
    m = len(Ec)
    ends = np.concatenate([Ec[:, 0], Ec[:, 1]]) - lo
    eid = np.concatenate([np.arange(m), np.arange(m)])
    order = np.argsort(ends, kind="stable"); ends_s, eid_s = ends[order], eid[order]
    npi = hi - lo
    ptr = np.searchsorted(ends_s, np.arange(npi + 1)).tolist(); eidl = eid_s.tolist()
    r_, u_, d_ = (Ec[:, 0] - lo).tolist(), (Ec[:, 1] - lo).tolist(), Ec[:, 2].tolist()
    incore = np.zeros(npi, dtype=bool); incore[labs - lo] = True
    degl = np.diff(np.array(ptr)).tolist()
    removed = [False] * npi; dead = [False] * m; dorder = []
    stack = [v for v in range(npi) if not incore[v] and degl[v] < M]
    while stack:
        v = stack.pop()
        if removed[v]: continue
        removed[v] = True; dorder.append(v)
        for k in range(ptr[v], ptr[v + 1]):
            e = eidl[k]
            if dead[e]: continue
            dead[e] = True
            w = u_[e] if r_[e] == v else r_[e]
            degl[w] -= 1
            if not removed[w] and not incore[w] and degl[w] < M: stack.append(w)
    assert len(dorder) + int(incore.sum()) == npi
    vl = val[lo:hi].tolist()
    for v in reversed(dorder):
        f = 0
        for k in range(ptr[v], ptr[v + 1]):
            e = eidl[k]
            if r_[e] == v:
                w = u_[e]
                if vl[w] >= 0: f |= 1 << ((vl[w] - d_[e]) % M)
            else:
                w = r_[e]
                if vl[w] >= 0: f |= 1 << ((vl[w] + d_[e]) % M)
        x = 0
        while f >> x & 1: x += 1
        assert x < M
        vl[v] = x
    y = np.array(vl, dtype=np.int64)
    assert (y >= 0).all()
    bad = int(((y[E[:, 1] - lo] - y[E[:, 0] - lo] - E[:, 2]) % M == 0).sum())
    print(f"  full certified assignment of Pi: certified violations {bad}  ({time.time()-t0:.1f}s)")
    if bad == 0:
        np.save(f"pi_{g}_{attach}_sol.npy", y.astype(np.int8))
