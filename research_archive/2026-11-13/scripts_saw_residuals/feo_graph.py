"""Feo graph F_T on the slots i = iota mod 16 of diagonal T = 2s+1 (closed form of feo_closed.py):
edge iP -- iQ when some base V makes (V; P odd, Q even) a fatal right angle. Reports, over all s,
max degree, max degeneracy and the number of diagonals whose graph is not bipartite.
Usage: py feo_graph.py h iota"""
import sys
from collections import defaultdict
from feo_closed import run

def degeneracy(adj):
    deg = {v: len(adj[v]) for v in adj}; alive = set(adj); k = 0
    while alive:
        v = min(alive, key=lambda x: deg[x]); k = max(k, deg[v]); alive.remove(v)
        for w in adj[v]:
            if w in alive: deg[w] -= 1
    return k

def bipartite(adj):
    col = {}
    for v0 in adj:
        if v0 in col: continue
        col[v0] = 0; st = [v0]
        while st:
            v = st.pop()
            for w in adj[v]:
                if w not in col: col[w] = 1 - col[v]; st.append(w)
                elif col[w] == col[v]: return False
    return True

h = int(sys.argv[1]); iota = int(sys.argv[2])
maxdeg = 0; maxdgn = 0; nonbip = 0; E = 0; nd = 0
for s in range(-(h // 2), h // 2):
    n, H = run(h, iota, s, 0)
    adj = defaultdict(set)
    for (iP, g, t, yV) in H:
        adj[iP].add(iP + t); adj[iP + t].add(iP)
    if not adj: continue
    nd += 1; E += sum(len(v) for v in adj.values()) // 2
    maxdeg = max(maxdeg, max(len(v) for v in adj.values()))
    maxdgn = max(maxdgn, degeneracy(adj))
    nonbip += (not bipartite(adj))
print('h', h, 'diagonals with edges', nd, 'edges', E, 'max degree', maxdeg, 'max degeneracy', maxdgn, 'non-bipartite diagonals', nonbip)
