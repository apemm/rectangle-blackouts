"""Diagnostic: on sampled curves, count all R2s arithmetic solutions without S | X,
and the distribution of v2(X), v7(X), to see whether S | X is a rare independent event."""
import sys, random
from collections import Counter
from sympy import factorint
exec(open('full_curve.py').read().split('def all_solutions')[0].replace('nmax, dmax, maxc = map(int, sys.argv[1:4])','nmax, dmax, maxc = 300, 6000, 1500'))
def v(p, x):
    if x == 0: return 99
    c = 0
    while x % p == 0: x //= p; c += 1
    return c
tot = Counter(); vv = Counter(); cnt = 0
for (m, delta) in curves:
    N = delta * (2 * m - delta)
    fd = factorint(abs(delta))
    for p, c in factorint(abs(2 * m - delta)).items(): fd[p] = fd.get(p, 0) + c
    n_all = 0
    for g in divisors(fd):
        for g1 in (g, -g):
            g2 = N // g1
            if (g1 - g2) % 2: continue
            U = (g2 - g1) // 2; V = (g1 + g2) // 2
            if U == 0 or V == 0 or (m * delta) % U: continue
            T = -(m * delta) // U
            if T % 2: continue
            x2 = U + T - V
            if x2 % 2: continue
            X = x2 // 2
            if X == 0 or U % 7 or V % 7: continue
            n_all += 1
            vv[(min(v(2, X), 9), min(v(7, X), 4))] += 1
    tot[n_all] += 1
print('curves', len(curves))
print('all solutions (F-type tests, no S|X, no Hil) per curve:', sorted(tot.items())[:40])
print('(v2 X, v7 X) distribution:', sorted(vv.items()))
