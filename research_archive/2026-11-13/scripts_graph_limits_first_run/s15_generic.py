# Chromatic number of generic "cylinder unions" Cay(Z, {t} U {u_i, u_i+t}) with random parameters. Experiment. Under 60 s.
import sys, time, random, threading
from pysat.solvers import Glucose4

def colorable(n, D, k, secs):
    s = Glucose4()
    var = lambda v, c: v*k + c + 1
    for v in range(n):
        s.add_clause([var(v, c) for c in range(k)])
    D = sorted(D)
    for v in range(n):
        for d in D:
            w = v + d
            if w >= n: break
            for c in range(k):
                s.add_clause([-var(v, c), -var(w, c)])
    s.add_clause([var(0, 0)])
    timer = threading.Timer(secs, lambda: s.interrupt())
    timer.start()
    r = s.solve_limited(expect_interrupt=True)
    timer.cancel(); s.delete()
    return r

random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
t0 = time.time()
for trial in range(4):
    t = random.choice([53, 71, 97, 101, 131])
    us = []
    for m in range(1, 7):
        while True:
            u = random.randint(1, 4*t)
            if u % t != 0 and u not in us and (u + t) not in us and (u - t) not in us: break
        us.append(u)
        D = {t} | set(us) | set(u + t for u in us)
        n = 12*t
        res = []
        chi_lb = None
        for k in range(3, 9):
            r = colorable(n, D, k, 4)
            res.append((k, r))
            if r is True or r is None: break
        print("t", t, "m", m, "us", us, "->", res, "t=%.1f" % (time.time() - t0), flush=True)
        if time.time() - t0 > 50: sys.exit()
