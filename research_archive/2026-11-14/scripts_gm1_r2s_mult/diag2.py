import sys, random
from sympy import factorint
exec(open('full_curve.py').read().split('def all_solutions')[0].replace('nmax, dmax, maxc = map(int, sys.argv[1:4])','nmax, dmax, maxc = 200, 6000, 12'))
for (m, delta) in curves:
    N = delta * (2 * m - delta); K = 2*m*delta
    fd = factorint(abs(delta))
    for p, c in factorint(abs(2 * m - delta)).items(): fd[p] = fd.get(p, 0) + c
    sols = []
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
            if X > 0: sols.append((X, X % 6272 == 0, g1, g2, U, V, T))
    print('m', m, 'delta', delta, 'N', N, 'K', K)
    for s in sols: print('    X', s[0], 'S|X', s[1], 'g1', s[2], 'g2', s[3], 'U', s[4], 'V', s[5], 'T', s[6])
