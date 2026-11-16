"""Hilbert-free exploration of R2s multiplicity on one curve (m, delta).
Generate every R2s arithmetic solution with X = +-S*n, 1 <= n <= nmax, from the
(X, Y) parametrization  4 delta m Y = -(X - Y)((X + Y)^2 + delta^2),  Y | X^2 + delta^2,
apply the archive's accept() tests for sea row F (U, V divisible by 7), then bucket by
(role, m, delta) and report curves with two or more solutions whose X/S lie in one
window of 2M-1 consecutive integers.
usage: py explore_xy.py nmax dmax
"""
import sys, math
from collections import defaultdict
from sympy import factorint

nmax, dmax = int(sys.argv[1]), int(sys.argv[2])
S = 6272

def divisors(fd):
    ds = [1]
    for p, c in fd.items():
        ds = [d * p ** k for d in ds for k in range(c + 1)]
    return ds

def role_of(m):
    # odd role, s = F: m = 10 mod 28; even role, s = F: m odd, m = 3 or 5 mod 7
    if m % 28 == 10:
        return 'odd'
    if m % 2 == 1 and m % 7 in (3, 5):
        return 'even'
    return None

buckets = defaultdict(set)
nsol = 0
for n in range(1, nmax + 1):
    for sgnX in (1, -1):
        X = sgnX * S * n
        for k in range(-(dmax // 196), dmax // 196 + 1):
            delta = 196 * k
            if delta == 0 or delta * delta >= 2 * abs(X):
                continue
            if delta < -3998:   # strip: F + delta/2 >= 1 for every admissible F >= 2000
                continue
            R = X * X + delta * delta
            for Ya in divisors(factorint(R)):
                for Y in (Ya, -Ya):
                    num = -(X - Y) * ((X + Y) ** 2 + delta * delta)
                    den = 4 * delta * Y
                    if num % den:
                        continue
                    m = num // den
                    if m > -100000:      # s = F lies below the bulk: m <= F - 1e5 < 0
                        continue
                    rl = role_of(m)
                    if rl is None:
                        continue
                    T = X - Y
                    if T == 0 or T % 2 or (m * delta) % T:
                        continue
                    U = -(m * delta) // T
                    V = U + T - 2 * X
                    N = delta * (2 * m - delta)
                    assert V * V - U * U == N
                    if U == 0 or V == 0 or U % 7 or V % 7:
                        continue
                    e1 = U - X
                    if e1 == 0 or e1 + T == 0:
                        continue
                    buckets[(rl, m, delta)].add((X // S, U, V))
                    nsol += 1

print('nmax', nmax, 'dmax', dmax, 'solutions', nsol, 'curves', len(buckets))
from collections import Counter
print('solutions per curve:', sorted(Counter(len(v) for v in buckets.values()).items()))
for M in (2, 3, 4, 5):
    best = []
    for key, sols in buckets.items():
        xs = sorted(set(x for x, _, _ in sols))
        for i in range(len(xs)):
            j = i
            while j + 1 < len(xs) and xs[j + 1] - xs[i] <= 2 * (M - 1):
                j += 1
            if j > i:
                best.append((j - i + 1, key, xs[i:j + 1]))
    best.sort(reverse=True)
    print('M', M, 'curves with >=2 in one window:', len(best), 'max', best[0][0] if best else 0)
    for b in best[:6]:
        print('   ', b, sorted(buckets[b[1]]))
