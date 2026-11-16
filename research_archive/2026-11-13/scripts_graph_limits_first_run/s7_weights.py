# Optimal ratio-bound weights for T = 5, 55, 1045 with signed solutions listed. Sanity check only. Under 60 s.
import sys, time
import numpy as np
from math import isqrt
from scipy.optimize import linprog

def signed(T, dmax):
    out = []
    for d in range(-dmax, dmax + 1):
        if d == 0: continue
        q = 20*d*d + 4*T*d + T*T
        L = isqrt(q)
        if L*L == q: out.append((d, L))
    return out

for T, B in [(5, 600), (55, 1200), (1045, 3000)]:
    S = signed(T, B)
    D = sorted(set(abs(d) for d, L in S))
    Dn = np.array(D, dtype=float)
    grid = 8*B + 1
    th = np.linspace(0, 0.5, grid)
    A = np.cos(2*np.pi*np.outer(th, Dn))
    res = linprog(c=-np.ones(len(D)), A_ub=-A, b_ub=np.ones(len(th)), bounds=[(0, None)]*len(D), method='highs')
    w = res.x
    print("T", T, "theta bound", round(1 + w.sum(), 4))
    t = T // 5
    sg = {}
    for d, L in S: sg.setdefault(abs(d), []).append((d, L))
    for d, x in zip(D, w):
        if x > 1e-4:
            print("   d=%5d w=%.3f signed/L=%s  d/t=%.4f" % (d, x, sg[d], d/t))
    # where is the minimum attained?
    vals = A @ w
    idx = np.where(vals < -1 + 1e-6)[0]
    print("   tight theta (as fractions of 1):", [round(float(th[i]), 5) for i in idx[:30]])
