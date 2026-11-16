# Independent check of an odd multiplicative relation prod rho_l^{n_l} = 1, sum n_l odd.
# Recomputes q, p from (al, be) and factors by plain trial division (no sympy).
import json, sys
from math import gcd, isqrt
from collections import defaultdict
c = json.load(open(sys.argv[1]))
def fac(n):
    f = defaultdict(int); d = 3
    assert n % 2 == 1
    while d * d <= n:
        while n % d == 0: f[d] += 1; n //= d
        d += 2
    if n > 1: f[n] += 1
    return f
tot = defaultdict(int)
for (al, be, q0, p0), n in zip(c['lams'], c['n']):
    assert al % 2 == 1 and be % 2 == 1 and 0 < al < be and gcd(al, be) == 1
    F = 4 * (al - 2 * be) ** 2 + be * be; g = gcd(F, be - al)
    q = al * F // g; p = (al * F + 4 * (be - al) * be * be) // g
    assert (q, p) == (q0, p0) and gcd(p, q) == 1
    for r, e in fac(p).items(): tot[r] += n * e
    for r, e in fac(q).items(): tot[r] -= n * e
print('lambdas', len(c['n']), 'sum n', sum(c['n']), 'parity', sum(c['n']) % 2, 'max be', max(l[1] for l in c['lams']))
print('all exponents cancel:', all(v == 0 for v in tot.values()), 'primes involved', len(tot))
