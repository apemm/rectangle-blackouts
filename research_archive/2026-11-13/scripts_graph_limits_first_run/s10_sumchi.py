# Exact sum over all diagonals T of chi(G_T) at height h (definitions of the setting: L < h, |d| < n_T). Sanity/evidence. Under 60 s.
import sys, time
from math import isqrt
from pysat.solvers import Glucose4

def diag_data(h):
    A = (h + 1)//2; K = h//2
    out = []
    for s in range(-(A - 1), K):
        T = 2*s + 1
        lo = max(0, -s); hi = min(A, K - s)
        n = hi - lo
        D = set()
        for d in range(-(n - 1), n):
            if d == 0: continue
            q = 20*d*d + 4*T*d + T*T
            L = isqrt(q)
            if L*L == q and L < h:
                D.add(abs(d))
        out.append((T, n, sorted(D)))
    return out

def chi(n, D, kmax=12):
    if not D: return 1
    # bipartite test quickly via SAT anyway
    for k in range(2, kmax + 1):
        s = Glucose4()
        var = lambda v, c: v*k + c + 1
        for v in range(n):
            s.add_clause([var(v, c) for c in range(k)])
        for v in range(n):
            for d in D:
                w = v + d
                if w >= n: break
                for c in range(k):
                    s.add_clause([-var(v, c), -var(w, c)])
        # symmetry breaking: vertex 0 gets color 0; its first neighbour color 1
        s.add_clause([var(0, 0)])
        if D[0] < n: s.add_clause([var(D[0], 1)])
        r = s.solve()
        s.delete()
        if r: return k
    return kmax + 1

t0 = time.time()
h = int(sys.argv[1])
data = diag_data(h)
tot = 0; hist = {}; worst = []
for T, n, D in data:
    c = chi(n, D)
    tot += c; hist[c] = hist.get(c, 0) + 1
    if c >= 5: worst.append((T, n, len(D), c))
    if time.time() - t0 > 50:
        print("TIME LIMIT; partial"); break
print("h", h, "diagonals", len(data), "sum chi", tot, "ratio", round(tot/h, 4), "hist", dict(sorted(hist.items())), "t=%.1f" % (time.time() - t0))
print("chi>=5:", worst[:40])
