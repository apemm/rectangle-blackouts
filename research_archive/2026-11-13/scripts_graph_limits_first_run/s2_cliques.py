# Clique numbers of the distance graphs Cay(Z, D_T) for many T (no height cap other than dmax). Under 60 s.
import math, sys, time
from math import gcd, isqrt

def sols(T, dmax):
    """all d != 0, |d| <= dmax, with 20d^2+4Td+T^2 a square, via the parametrization (complete: verified in s1)."""
    out = set()
    # brute force is O(dmax); fine for dmax up to ~2e5
    for d in range(-dmax, dmax + 1):
        if d == 0: continue
        q = 20*d*d + 4*T*d + T*T
        L = isqrt(q)
        if L*L == q:
            out.add(d)
    return out

def max_clique(D):
    """largest k such that there are 0=a0<a1<...<ak-1 with all pairwise differences in D (D set of positive ints)."""
    Ds = sorted(D)
    best = [1, [0]]
    def ext(cl, cands):
        if len(cl) > best[0]:
            best[0] = len(cl); best[1] = cl[:]
        if len(cl) + len(cands) <= best[0]: return
        for idx, v in enumerate(cands):
            if len(cl) + len(cands) - idx <= best[0]: return
            newc = [u for u in cands[idx+1:] if (u - v) in D]
            ext(cl + [v], newc)
    ext([0], Ds)
    return best

t0 = time.time()
primes_split = [11, 19, 29, 31, 41, 59, 61, 71, 79, 89]
cands = set()
base = [1, 5, 11, 19, 29, 31, 41, 55, 95, 145, 155, 209, 319, 341, 451, 551, 589, 1045, 1595, 1705, 2255, 2945, 3135, 4785, 5225, 6061, 6479, 11495, 30305, 33055]
res = []
for T in base:
    dmax = min(60000, 40*T + 2000)
    S = sols(T, dmax)
    D = set(abs(d) for d in S)
    k, cl = max_clique(D)
    res.append((T, len(D), k, cl))
    print(T, "|D|=", len(D), "clique", k, cl, flush=True)
    if time.time() - t0 > 45: break
print("time", time.time() - t0)
