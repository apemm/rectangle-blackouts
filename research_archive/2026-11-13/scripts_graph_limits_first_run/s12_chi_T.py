# Lower bounds for chi(Cay([0,n), D_T^{<=B})) by SAT with a conflict budget. usage: T B n kmin kmax. Under 60 s.
import sys, time
from math import isqrt
from pysat.solvers import Glucose4

def dist(T, B):
    out = set()
    for d in range(-B, B + 1):
        if d == 0: continue
        q = 20*d*d + 4*T*d + T*T
        L = isqrt(q)
        if L*L == q: out.add(abs(d))
    return sorted(out)

def colorable(n, D, k, budget):
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
    s.add_clause([var(0, 0)])
    s.conf_budget(budget)
    r = s.solve_limited()
    s.delete()
    return r   # True / False / None (unknown)

T = int(sys.argv[1]); B = int(sys.argv[2]); n = int(sys.argv[3]); kmin = int(sys.argv[4]); kmax = int(sys.argv[5])
budget = int(sys.argv[6]) if len(sys.argv) > 6 else 200000
D = [d for d in dist(T, B) if d < n]
print("T", T, "n", n, "|D|", len(D), D)
t0 = time.time()
for k in range(kmin, kmax + 1):
    r = colorable(n, D, k, budget)
    print("  k", k, "->", r, "t=%.1f" % (time.time() - t0), flush=True)
    if r or time.time() - t0 > 40: break
