"""Check the 2-adic classification of homogeneous Fo/Fo hits against the census solver (copy of fofo_cubic).
Prediction (hole branch, classes i mod 2^k, k>=5): fillers at offset 0, v2(x1)=v2(x2)=j>=2, v2(d)=2j+1,
v2(p)=j+2, and m=p/d=alpha/beta with alpha odd, v2(beta)=j-1. Base branch only if v2(d)=3.
Usage: py classify.py h LM rule(saw|star) iota1,iota2,..."""
import sys
from math import gcd
from fractions import Fraction
from fofo_cubic_copy import census

def v2(n):
    n = abs(n); c = 0
    if n == 0: return 99
    while n % 2 == 0: n //= 2; c += 1
    return c

h = int(sys.argv[1]); LM = int(sys.argv[2]); rule = 0 if sys.argv[3] == 'saw' else 1
iotas = [int(x) for x in sys.argv[4].split(',')]
tot = 0; bad = 0; seen = {}
for iota in iotas:
    nl, nt, hom, ex = census(h, iota, LM, rule, False, h // 2)
    for e in ex:
        s, i1, i2, g1, g2, yF1, yF2, R0 = [int(x) for x in e]
        tot += 1
        d = (i2 - i1) // 2            # (n,Y) units: L2-L1 = (2d, d)
        p = g1 - g2
        u = (yF1 - (2 * i1 + 1)) // 4; v = (yF2 - (2 * i2 + 1)) // 4
        same = (yF1 == yF2)
        m = Fraction(p, d); al, be = m.numerator, m.denominator
        j = v2(g1)
        ok = same and (d > 0 or (al % 2 == 1 and be % 2 == 0 and v2(be) == j - 1 and v2(g2) == j
                                   and v2(d) == 2 * j + 1 and v2(p) == j + 2 and g1 % 4 == 0 and 2 < m < 4))
        if d > 0: ok = ok and same
        if not ok: bad += 1
        key = (al, be, d > 0)
        seen[key] = seen.get(key, 0) + 1
        if not ok and bad <= 10:
            print('  MISMATCH', dict(s=s, i1=i1, i2=i2, g1=g1, g2=g2, yF1=yF1, yF2=yF2, d=d, p=p, u=u, v=v, m=str(m)))
print('h', h, 'LM', LM, sys.argv[3], 'hits', tot, 'mismatches', bad)
for k in sorted(seen, key=lambda t: (t[2], t[1], t[0])):
    print('   alpha/beta = %d/%d  %s  hits %d' % (k[0], k[1], 'd>0' if k[2] else 'd<0', seen[k]))
