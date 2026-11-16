# Clique number of the constraint graph H (non-monotone or P-conflict) for small h. Sanity check. Under 60 s.
import sys, time
from math import isqrt
import networkx as nx

def build(h):
    A = (h + 1)//2; K = h//2
    labels = [(i, j) for i in range(A) for j in range(K)]
    def V(i, j, ip):   # even point of (i,j) sees odd point of slot ip
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
            if i == ip: G.add_edge(labels[a], labels[b]); continue
            # i < ip always here since labels sorted by i
            if j > jp or V(i, j, ip) or V(ip, jp, i):
                G.add_edge(labels[a], labels[b])
    return G, A, K

t0 = time.time()
for h in [8, 12, 16, 20, 24, 28, 32]:
    G, A, K = build(h)
    cl, wt = nx.max_weight_clique(G, weight=None)
    print("h", h, "A", A, "K", K, "omega", wt, "2h/3 =", round(2*h/3, 2), "K+K/3=", round(4*K/3, 2), "t=%.1f" % (time.time() - t0), flush=True)
    if time.time() - t0 > 40: break
