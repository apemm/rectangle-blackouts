"""Hilbert-free census of per-curve R2s multiplicity for every sea type of design H7.
Step 1: generate every curve (role, m, delta) that has an R2s solution with X = S n,
        1 <= n <= nmax, |delta| <= dmax, from the (X, Y) form 4 delta m Y = -(X-Y)((X+Y)^2+delta^2).
Step 2: for up to maxc of these curves (random sample), enumerate ALL solutions of the curve
        from the factorizations g1 g2 = N (Theorem A), with the tests S | X, weak Hil, the sea
        types of B and D, e1 != 0, e2 != 0, and count distinct X (both signs), distinct U, and
        +-V doubles (same U, both S | X).
Classes (normalized residues of H7; mixed and zero-residue blocks both admitted):
  F odd : m = 2 mod 4, m = 3 mod 7, m < 0      F even: m odd, m = 3,5 mod 7, m < 0
  L odd : m = 2 mod 4, m = 0 mod 7, m < 0      L even: m odd, m = 0,2 mod 7, m < 0
  H odd : m odd, m = 1 mod 7, m > 0            H even: m = 2 mod 4, m = 1,3 mod 7, m > 0
usage: py census_seas.py sea nmax dmax maxc seed
"""
import sys, random
from collections import Counter
from sympy import factorint

sea = sys.argv[1]
nmax, dmax, maxc, seed = map(int, sys.argv[2:6])
S = 6272
QR = {1, 2, 4}

def stype(x):
    r = x % 7
    return 'F' if r == 0 else ('H' if r in QR else 'L')

def role_of(m):
    if sea == 'F':
        if m >= 0: return None
        if m % 4 == 2 and m % 7 == 3: return 'odd'
        if m % 2 == 1 and m % 7 in (3, 5): return 'even'
    if sea == 'L':
        if m >= 0: return None
        if m % 4 == 2 and m % 7 == 0: return 'odd'
        if m % 2 == 1 and m % 7 in (0, 2): return 'even'
    if sea == 'H':
        if m <= 0: return None
        if m % 2 == 1 and m % 7 == 1: return 'odd'
        if m % 4 == 2 and m % 7 in (1, 3): return 'even'
    return None

def divisors(fd):
    ds = [1]
    for p, c in fd.items():
        ds = [d * p ** k for d in ds for k in range(c + 1)]
    return ds

def tests(m, delta, U, V, T, X):
    if U == 0 or V == 0 or X == 0: return False
    if stype(U) != sea or stype(V) != sea: return False
    if U - X == 0 or U - X + T == 0: return False
    if 2 * abs(X) <= delta * delta: return False
    return True

curves = set()
for n in range(1, nmax + 1):
    for X in (S * n, -S * n):
        for k in range(-(dmax // 28), dmax // 28 + 1):
            delta = 28 * k
            if delta == 0 or delta * delta >= 2 * abs(X): continue
            for Ya in divisors(factorint(X * X + delta * delta)):
                for Y in (Ya, -Ya):
                    num = -(X - Y) * ((X + Y) ** 2 + delta * delta); den = 4 * delta * Y
                    if num % den: continue
                    m = num // den
                    if abs(m) < 100000 or role_of(m) is None: continue
                    T = X - Y
                    if T == 0 or T % 2 or (m * delta) % T: continue
                    U = -(m * delta) // T; V = U + T - 2 * X
                    if tests(m, delta, U, V, T, X):
                        curves.add((m, delta))
curves = sorted(curves)
random.seed(seed)
sample = random.sample(curves, min(maxc, len(curves)))

hX = Counter(); hU = Counter(); doubles = 0; multi = []
for (m, delta) in sample:
    N = delta * (2 * m - delta)
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
            if X % S: continue
            if tests(m, delta, U, V, T, X):
                sols.append((X // S, U, V))
    xs = set(x for x, _, _ in sols); us = Counter(u for _, u, _ in sols)
    hX[len(xs)] += 1; hU[len(us)] += 1
    doubles += sum(1 for u, c in us.items() if c > 1)
    pos = sorted(x for x in xs if x > 0)
    if len(pos) >= 2: multi.append((m, delta, pos))
print('sea', sea, 'nmax', nmax, 'dmax', dmax, 'curves found', len(curves), 'sampled', len(sample))
print('  distinct X per curve (both signs):', sorted(hX.items()))
print('  distinct U per curve:', sorted(hU.items()), ' +-V doubles:', doubles)
print('  curves with >= 2 positive X/S:', len(multi), multi[:8])
