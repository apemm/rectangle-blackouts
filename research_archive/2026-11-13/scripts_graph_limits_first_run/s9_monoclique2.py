# Structure of maximum cliques of H for moderate h. Sanity check. Under 60 s.
import sys, time
from math import isqrt
import networkx as nx

def build(h):
    A = (h + 1)//2; K = h//2
    labels = [(i, j) for i in range(A) for j in range(K)]
    def V(i, j, ip):
        q = 16*(i - ip)**2 + (2*(j - ip) + 1)**2
        L = isqrt(q)
        return L*L == q and L % 2 == 1 and 0 < L < h
    G = nx.Graph()
    G.add_nodes_from(labels)
    n = len(labels)
    for a in range(n):
        i, j = labels[a]
        for b in range(a + 1, n):
            ip, jp = labels[b]
            if i == ip or j > jp or V(i, j, ip) or V(ip, jp, i):
                G.add_edge(labels[a], labels[b])
    return G, A, K

t0 = time.time()
hs = [int(x) for x in sys.argv[1].split(',')]
for h in hs:
    G, A, K = build(h)
    cl, wt = nx.max_weight_clique(G, weight=None)
    print("h", h, "A", A, "K", K, "omega", wt, "ratio", round(wt/h, 4), "t=%.1f" % (time.time() - t0), flush=True)
    bycol = {}
    for (i, j) in sorted(cl): bycol.setdefault(i, []).append(j)
    print("   by slot:", {i: (js if len(js) < 6 else "%d..%d (%d)" % (min(js), max(js), len(js))) for i, js in bycol.items()})
    if time.time() - t0 > 45: break
