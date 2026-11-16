# More ratio-bound data and the optimal weights. Sanity check only. Under 60 s.
import sys, time
import numpy as np
from math import isqrt
from scipy.optimize import linprog

def sols(T, dmax):
    out = set()
    for d in range(-dmax, dmax + 1):
        if d == 0: continue
        q = 20*d*d + 4*T*d + T*T
        L = isqrt(q)
        if L*L == q: out.add(abs(d))
    return sorted(out)

def theta_bound(D, grid):
    Dn = np.array(D, dtype=float)
    th = np.linspace(0, 0.5, grid)
    A = np.cos(2*np.pi*np.outer(th, Dn))
    res = linprog(c=-np.ones(len(D)), A_ub=-A, b_ub=np.ones(len(th)), bounds=[(0, None)]*len(D), method='highs')
    w = res.x
    th2 = np.linspace(0, 0.5, 4*grid + 1)
    mn = np.min(np.cos(2*np.pi*np.outer(th2, Dn)) @ w)
    return w.sum(), mn, w

t0 = time.time()
show = len(sys.argv) > 1
for T, B in [(19, 2000), (29, 2000), (31, 2000), (95, 2500), (145, 2500), (155, 2500), (6061, 9000), (30305, 9000)]:
    D = sols(T, B)
    grid = min(30000, 8*B + 1)
    s, mn, w = theta_bound(D, grid)
    print("T", T, "B", B, "|D|", len(D), "sum w", round(s, 4), "min", round(mn, 4), "chi >=", round(1 + s/abs(mn), 3), "t=%.1f" % (time.time() - t0), flush=True)
    if show:
        print("   weights:", [(d, round(x, 3)) for d, x in zip(D, w) if x > 1e-6])
    if time.time() - t0 > 40: break
