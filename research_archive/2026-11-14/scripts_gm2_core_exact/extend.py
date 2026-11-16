"""Extend a core assignment to every label of the block system (L9).

Usage: py -B extend.py B S M orient version [core_solution.npy]
Peels labels with fewer than M distinct incident triples (queue order), then
assigns peeled labels in reverse deletion order with the smallest value that
violates no triple to an already assigned label.  Labels of the core take the
given core solution.  Writes full_<orient>_<version>_B<B>_M<M>.npy (int8, one
value per local rank) and asserts every constraint of the system holds.
"""
import sys, time
import numpy as np
from build_core import build

B, S, M, orient, version = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5]
modmode = len(sys.argv) > 7 and sys.argv[7] == "mod"   # extend a mod-M certified core solution certifiably
t0 = time.time()
n, E = build(B, S, M, orient, version)
m = len(E)
# CSR adjacency over triples
ends = np.concatenate([E[:, 0], E[:, 1]])
eid = np.concatenate([np.arange(m), np.arange(m)])
order = np.argsort(ends, kind="stable")
ends_s, eid_s = ends[order], eid[order]
ptr = np.searchsorted(ends_s, np.arange(n + 1))
deg = np.diff(ptr).astype(np.int64)
r_, u_, d_ = E[:, 0].tolist(), E[:, 1].tolist(), E[:, 2].tolist()
ptrl, eidl = ptr.tolist(), eid_s.tolist()
degl = deg.tolist()
removed = [False] * n
edge_dead = [False] * m
stack = [v for v in range(n) if degl[v] < M]
delorder = []
while stack:
    v = stack.pop()
    if removed[v]:
        continue
    removed[v] = True
    delorder.append(v)
    for k in range(ptrl[v], ptrl[v + 1]):
        e = eidl[k]
        if edge_dead[e]:
            continue
        edge_dead[e] = True
        w = u_[e] if r_[e] == v else r_[e]
        degl[w] -= 1
        if not removed[w] and degl[w] < M:
            stack.append(w)
core = [v for v in range(n) if not removed[v]]
print(f"B={B} M={M} {orient} {version}: constraints {m}, core labels {len(core)}")
val = [-1] * n
if core:
    sol = np.load(sys.argv[6])
    sd = dict(zip(sol[:, 0].tolist(), sol[:, 1].tolist()))
    assert set(sd) == set(core), "core solution does not cover exactly the core"
    for v in core:
        val[v] = sd[v]
for v in reversed(delorder):
    forb = 0
    for k in range(ptrl[v], ptrl[v + 1]):
        e = eidl[k]
        if r_[e] == v:
            w = u_[e]
            if val[w] >= 0:
                y = val[w] - d_[e]      # xi_w - xi_v = delta forbidden -> xi_v != xi_w - delta
                if modmode: y %= M
                if 0 <= y < M: forb |= 1 << y
        else:
            w = r_[e]
            if val[w] >= 0:
                y = val[w] + d_[e]
                if modmode: y %= M
                if 0 <= y < M: forb |= 1 << y
    x = 0
    while forb >> x & 1:
        x += 1
    assert x < M, "peeling extension failed"
    val[v] = x
full = np.array(val, dtype=np.int64)
assert (full >= 0).all() and (full < M).all()
bad = int((full[E[:, 1]] - full[E[:, 0]] == E[:, 2]).sum())
print(f"  violated constraints of the system: {bad}   ({time.time()-t0:.1f}s)")
assert bad == 0
tag = "_cert" if modmode else ""
if modmode:
    badm = int(((full[E[:, 1]] - full[E[:, 0]] - E[:, 2]) % M == 0).sum())
    print(f"  mod-{M} certified violations: {badm}")
    assert badm == 0
np.save(f"full_{orient}_{version}_B{B}_M{M}{tag}.npy", full.astype(np.int8))
