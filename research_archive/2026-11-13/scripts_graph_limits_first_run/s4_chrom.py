# Chromatic number of Cay(Z, D_T) restricted to [0,n) with distances <= B, by SAT. Under 60 s.
import sys, time
from math import isqrt
from pysat.solvers import Cadical153

def sols(T, dmax):
    out = set()
    for d in range(-dmax, dmax + 1):
        if d == 0: continue
        q = 20*d*d + 4*T*d + T*T
        L = isqrt(q)
        if L*L == q: out.add(abs(d))
    return out

def colorable(n, D, k, clique=None, tlimit=20):
    s = Cadical153()
    var = lambda v, c: v*k + c + 1
    for v in range(n):
        s.add_clause([var(v, c) for c in range(k)])
    Dl = sorted(d for d in D if d < n)
    for v in range(n):
        for d in Dl:
            w = v + d
            if w >= n: break
            for c in range(k):
                s.add_clause([-var(v, c), -var(w, c)])
    if clique:
        for idx, v in enumerate(clique):
            if idx < k: s.add_clause([var(v, idx)])
    r = s.solve()
    s.delete()
    return r

T = int(sys.argv[1]); B = int(sys.argv[2]); ns = [int(x) for x in sys.argv[3].split(',')]
ks = [int(x) for x in sys.argv[4].split(',')]
D = sols(T, B)
print("T", T, "B", B, "|D|", len(D), sorted(D)[:40])
t0 = time.time()
for n in ns:
    for k in ks:
        r = colorable(n, D, k)
        print("n", n, "k", k, "colorable", r, "t=%.1f" % (time.time() - t0), flush=True)
        if time.time() - t0 > 45: sys.exit()
