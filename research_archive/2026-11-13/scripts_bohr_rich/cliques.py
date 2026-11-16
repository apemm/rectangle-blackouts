# clique number of the diagonal graphs G_T(h): 1 + max clique of H on D_T, a~b iff |a-b| in D_T
import sys
from common import all_D

def maxclique(V, adj):
    best = [0]
    def bk(R, P):
        if not P:
            best[0] = max(best[0], R); return
        if R + len(P) <= best[0]: return
        for v in sorted(P):
            if R + len(P) <= best[0]: return
            bk(R + 1, P & adj[v]); P = P - {v}
    bk(0, set(V)); return best[0]

h = int(sys.argv[1])
D = all_D(h)
hist = {}; ex = {}
for T, d in D.items():
    s = set(d)
    adj = {a: {b for b in d if b != a and abs(a - b) in s} for a in d}
    w = 1 + maxclique(d, adj) if d else 1
    hist[w] = hist.get(w, 0) + 1
    if w >= 4 and w not in ex: ex[w] = (T, d[:30])
print("h", h, "clique-number histogram", sorted(hist.items()))
for w, e in sorted(ex.items()): print(w, e)
