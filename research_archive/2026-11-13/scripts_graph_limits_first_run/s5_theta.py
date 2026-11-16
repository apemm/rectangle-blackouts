# Ratio (Lovasz-type) bound for Cay(Z, D_T): maximize sum w_d subject to sum_d w_d cos(2 pi theta d) >= -1 for all theta.
# Then chi >= 1 + sum w. Numerical LP on a grid (sanity check only). Under 60 s.
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
    D = np.array(D, dtype=float)
    th = np.linspace(0, 0.5, grid)
    A = np.cos(2*np.pi*np.outer(th, D))      # grid x m
    # constraints: -A w <= 1
    res = linprog(c=-np.ones(len(D)), A_ub=-A, b_ub=np.ones(len(th)), bounds=[(0, None)]*len(D), method='highs')
    w = res.x
    # refine check on a finer grid
    th2 = np.linspace(0, 0.5, 4*grid + 1)
    mn = np.min(np.cos(2*np.pi*np.outer(th2, D)) @ w)
    return w.sum(), mn, w

t0 = time.time()
for T, B in [(1, 2000), (5, 2000), (11, 2000), (55, 2000), (209, 2500), (1045, 1500), (1045, 3000), (1045, 6000)]:
    D = sols(T, B)
    grid = min(40000, 8*B + 1)
    s, mn, w = theta_bound(D, grid)
    # normalized bound: 1 + s/|mn|
    print("T", T, "B", B, "|D|", len(D), "sum w", round(s, 4), "min on fine grid", round(mn, 4), "chi >= ", round(1 + s/abs(mn), 4), "t=%.1f" % (time.time() - t0), flush=True)
    if time.time() - t0 > 40: break
