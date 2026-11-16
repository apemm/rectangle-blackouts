# SAT colourability tests with a hard wall-clock limit per call (interrupt). usage: T B n k1,k2,... seconds_per_call
import sys, time, threading
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

def colorable(n, D, k, secs, clique=None):
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
    if clique:
        for idx, v in enumerate(clique): s.add_clause([var(v, idx)])
    else:
        s.add_clause([var(0, 0)])
    timer = threading.Timer(secs, lambda: s.interrupt())
    timer.start()
    r = s.solve_limited(expect_interrupt=True)
    timer.cancel()
    s.delete()
    return r

if __name__ == "__main__":
    T = int(sys.argv[1]); B = int(sys.argv[2]); n = int(sys.argv[3])
    ks = [int(x) for x in sys.argv[4].split(',')]; secs = float(sys.argv[5])
    D = [d for d in dist(T, B) if d < n]
    print("T", T, "n", n, "|D|", len(D), D)
    t0 = time.time()
    for k in ks:
        r = colorable(n, D, k, secs)
        print("  k", k, "->", r, "t=%.1f" % (time.time() - t0), flush=True)
