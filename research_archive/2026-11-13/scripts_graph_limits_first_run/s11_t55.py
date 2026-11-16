# Check chi of Cay([0,n), D) for D = distances of T=55 with L<256. Two solvers, no symmetry breaking. Under 60 s.
import sys, time
from pysat.solvers import Glucose4, Cadical153, Minisat22

def colorable(n, D, k, Solver):
    s = Solver()
    var = lambda v, c: v*k + c + 1
    for v in range(n):
        s.add_clause([var(v, c) for c in range(k)])
    for v in range(n):
        for d in D:
            w = v + d
            if w < n:
                for c in range(k):
                    s.add_clause([-var(v, c), -var(w, c)])
    r = s.solve()
    model = s.get_model() if r else None
    s.delete()
    return r, model

D = [4, 10, 11, 15, 21, 25, 36, 39, 50]
t0 = time.time()
for n in [60, 70, 80, 90, 100, 101]:
    for k in [4, 5]:
        r1, _ = colorable(n, D, k, Glucose4)
        r2, _ = colorable(n, D, k, Cadical153)
        r3, _ = colorable(n, D, k, Minisat22)
        print("n", n, "k", k, "colorable:", r1, r2, r3, "t=%.1f" % (time.time() - t0), flush=True)
# minimal n with chi >= 6 and >= 5
def first_n(k):
    lo = 1
    for n in range(2, 140):
        r, _ = colorable(n, D, k, Cadical153)
        if not r: return n
    return None
print("least n not 4-colorable:", first_n(4), " least n not 5-colorable:", first_n(5), "t=%.1f" % (time.time() - t0))
r, m = colorable(101, D, 6, Cadical153)
print("101 vertices 6-colorable:", r)
