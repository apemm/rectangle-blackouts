"""Exact 2-SAT test of the two-point choice set {0, M-1} on the candidate P multigraph.
Only constraints with delta in {0, +-(M-1)} can bind.  A satisfying assignment is
verified against every constraint."""
import sys, time
from core_probe import edges

def scc_2sat(nv, clauses):
    # literal 2v = x_v true, 2v+1 = x_v false; clause (a or b): ~a->b, ~b->a
    N = 2 * nv
    g = [[] for _ in range(N)]; gr = [[] for _ in range(N)]
    for a, b in clauses:
        g[a ^ 1].append(b); g[b ^ 1].append(a)
        gr[b].append(a ^ 1); gr[a].append(b ^ 1)
    seen = bytearray(N); order = []
    for s in range(N):
        if seen[s]: continue
        stack = [(s, 0)]; seen[s] = 1
        while stack:
            v, i = stack[-1]
            if i < len(g[v]):
                stack[-1] = (v, i + 1); w = g[v][i]
                if not seen[w]: seen[w] = 1; stack.append((w, 0))
            else:
                stack.pop(); order.append(v)
    comp = [-1] * N; c = 0
    for s in reversed(order):
        if comp[s] >= 0: continue
        stack = [s]; comp[s] = c
        while stack:
            v = stack.pop()
            for w in gr[v]:
                if comp[w] < 0: comp[w] = c; stack.append(w)
        c += 1
    val = []
    for v in range(nv):
        if comp[2 * v] == comp[2 * v + 1]: return None
        val.append(comp[2 * v] > comp[2 * v + 1])  # Kosaraju: later comp = topologically later
    return val

h, S, M = map(int, sys.argv[1:4])
t0 = time.time()
E = edges(h, S, M)
verts = sorted({x for r, s, _ in E for x in (r, s)}); idx = {x: i for i, x in enumerate(verts)}
T = lambda v: 2 * idx[v]; F = lambda v: 2 * idx[v] + 1
cl = []
for r, s, dl in E:
    if dl == 0: cl += [(T(r), T(s)), (F(r), F(s))]
    elif dl == M - 1: cl.append((T(r), F(s)))
    elif dl == -(M - 1): cl.append((F(r), T(s)))
val = scc_2sat(len(verts), cl)
if val is None:
    print(f"h={h} S={S} M={M} edges={len(E)} clauses={len(cl)} 2-SAT UNSAT t={time.time()-t0:.1f}s")
else:
    ch = {v: (M - 1 if val[idx[v]] else 0) for v in verts}
    bad = sum(1 for r, s, dl in E if ch[s] - ch[r] == dl)
    print(f"h={h} S={S} M={M} edges={len(E)} clauses={len(cl)} 2-SAT SAT, violations={bad} t={time.time()-t0:.1f}s")
