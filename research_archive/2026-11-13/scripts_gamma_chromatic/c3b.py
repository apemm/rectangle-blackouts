# Weighted ratio (Hoffman/Delsarte LP) lower bound for chi(Cay(Z, E)), E = D_T^inf cap [1,B],
# T = 5*11^k.  Bound: chi >= 1 + W/lam, lam = -min_theta sum w_d cos(2 pi d theta), sum w = W.
# Cutting-plane LP over theta; final min checked on a fine grid (numerical, not certified).
import numpy as np, time
from fractions import Fraction as F
from scipy.optimize import linprog
exec(open('c1_lib.py').read())
def fpw(x, n):
    base = x if n >= 0 else inv(x); n = abs(n); r = (F(1), F(0))
    while n:
        if n & 1: r = mul(r, base)
        base = mul(base, base); n >>= 1
    return r
def Eset(T, B):
    out = set()
    for s in (1, -1):
        for n in range(-30, 31):
            for k in range(-6, 7):
                beta = mul((F(s), F(0)), mul(fpw(eps, n), fpw(omg, k)))
                r = r_of(beta)
                if r != 0 and (r*T).denominator == 1 and abs(r*T) <= B:
                    out.add(abs(int(r*T)))
    return sorted(out)
def lp_bound(E, iters=60):
    E = np.array(E, dtype=float)
    th = list(np.linspace(0, 0.5, 2001))
    fine = np.linspace(0, 0.5, 3000001)
    for it in range(iters):
        C = np.cos(2*np.pi*np.outer(th, E))
        res = linprog(-np.ones(len(E)), A_ub=-C, b_ub=np.ones(len(th)), bounds=[(0, None)]*len(E), method='highs')
        w = res.x
        P = np.zeros_like(fine)
        for d, wd in zip(E, w):
            if wd > 1e-12: P += wd*np.cos(2*np.pi*d*fine)
        j = np.argmin(P)
        lam = -P[j]
        if lam <= 1 + 1e-6: break
        # add local minima below -1
        idx = np.where((P[1:-1] < P[:-2]) & (P[1:-1] < P[2:]) & (P[1:-1] < -1))[0] + 1
        th += list(fine[idx[:200]])
    W = w.sum()
    return 1 + W/lam, len(E)
t0 = time.time()
for T in (605, 6655, 73205):
    E = Eset(T, 8*T)
    b, n = lp_bound(E)
    print("T", T, "|E|", n, "ratio bound", round(b, 3), "time", round(time.time()-t0, 1), flush=True)
