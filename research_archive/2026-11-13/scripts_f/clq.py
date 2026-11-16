import numpy as np, sys, time, networkx as nx
t0 = time.time()
def Dinf(T, X):
    out = set(); CH = 10**6
    for a in range(-X, X + 1, CH):
        d = np.arange(a, min(a + CH, X + 1), dtype=np.int64)
        Q = 20*d*d + 4*T*d + T*T
        L = np.floor(np.sqrt(Q.astype(np.float64))).astype(np.int64)
        ok = np.zeros(len(d), bool)
        for c in (-1, 0, 1):
            LL = L + c; ok |= (LL*LL == Q)
        ok &= (d != 0)
        out.update(abs(int(x)) for x in d[ok])
    return sorted(out)
def maxclique(D):
    S = set(D); V = sorted(set(D) | set(-x for x in D))
    G = nx.Graph(); G.add_nodes_from(V)
    for i, x in enumerate(V):
        for y in V[i+1:]:
            if (y - x) in S: G.add_edge(x, y)
    best = []
    for c in nx.find_cliques(G):
        if len(c) > len(best): best = c
    return len(best) + 1, sorted(best)   # +1 for vertex 0
X = int(sys.argv[1]);
for T in map(int, sys.argv[2:]):
    D = Dinf(T, X)
    w, c = maxclique(D)
    D32 = [d for d in D if d % 32 == 0]
    w32, c32 = maxclique(D32) if D32 else (1, [])
    D2 = [d for d in D if d % 2 == 0]
    w2, c2 = maxclique(D2) if D2 else (1, [])
    print(f"T={T} |D cap [1,{X}]|={len(D)} omega={w} clique={[0]+c}  |D2|={len(D2)} omega_even={w2}  |D32|={len(D32)} omega_32={w32}  t={time.time()-t0:.1f}", flush=True)
