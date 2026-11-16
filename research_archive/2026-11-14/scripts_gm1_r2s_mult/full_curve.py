"""For curves (m, delta) found by the (X, Y) generator, enumerate ALL R2s solutions of the curve
from the signed factorizations g1 g2 = N (complete by Theorem A), with S | X and the F-sea tests,
and report how many distinct X each curve carries (at any distance).
usage: py full_curve.py nmax dmax maxcurves
"""
import sys
from collections import defaultdict, Counter
from sympy import factorint

nmax, dmax, maxc = map(int, sys.argv[1:4])
S = 6272

def divisors(fd):
    ds = [1]
    for p, c in fd.items():
        ds = [d * p ** k for d in ds for k in range(c + 1)]
    return ds

def role_of(m):
    if m % 28 == 10: return 'odd'
    if m % 2 == 1 and m % 7 in (3, 5): return 'even'
    return None

curves = set()
for n in range(1, nmax + 1):
    X = S * n
    for k in range(-(dmax // 196), dmax // 196 + 1):
        delta = 196 * k
        if delta == 0 or delta * delta >= 2 * X or delta < -3998: continue
        for Ya in divisors(factorint(X * X + delta * delta)):
            for Y in (Ya, -Ya):
                num = -(X - Y) * ((X + Y) ** 2 + delta * delta); den = 4 * delta * Y
                if num % den: continue
                m = num // den
                if m > -100000 or role_of(m) is None: continue
                T = X - Y
                if T == 0 or T % 2 or (m * delta) % T: continue
                U = -(m * delta) // T; V = U + T - 2 * X
                if U == 0 or V == 0 or U % 7 or V % 7: continue
                if U - X == 0 or U - X + T == 0: continue
                curves.add((m, delta))
import random; random.seed(1); curves = sorted(curves); print("total curves", len(curves), "m range", curves[0][0], curves[-1][0]); curves = random.sample(curves, min(maxc, len(curves)))

def all_solutions(m, delta):
    N = delta * (2 * m - delta)
    fd = factorint(abs(delta));
    for p, c in factorint(abs(2 * m - delta)).items(): fd[p] = fd.get(p, 0) + c
    out = set()
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
            if X == 0 or X % S: continue
            if 2 * abs(X) <= delta * delta: continue
            if U % 7 or V % 7: continue
            if U - X == 0 or U - X + T == 0: continue
            out.add(X // S)
    return out

hist = Counter(); multi = []
for (m, delta) in curves:
    xs = all_solutions(m, delta)
    pos = sorted(x for x in xs if x > 0)
    hist[len(pos)] += 1
    if len(pos) >= 2: multi.append((m, delta, pos))
print('curves', len(curves), 'histogram of #positive X/S per curve:', sorted(hist.items()))
multi.sort(key=lambda t: min(b - a for a, b in zip(t[2], t[2][1:])))
for t in multi[:15]:
    print(t)
