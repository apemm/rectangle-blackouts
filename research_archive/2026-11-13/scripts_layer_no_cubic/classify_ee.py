"""Check the 2-adic classification of homogeneous Fe/Fe hits (even label points) against the census solver.
Prediction: t = i2 - i1 has v2(t) = tau odd, v2(P) = (tau+3)/2 (P = X1 - X2 in columns), filler slot offsets
v2(x1) = v2(x2) = (tau-5)/2 relative to the label column, gap between the filler slots of 2-adic order (tau-1)/2.
Usage: py classify_ee.py h LM rule(saw|star) iota1,iota2,... [sstep]"""
import sys
from fofo_cubic_copy import census

def v2(n):
    n = abs(n); c = 0
    if n == 0: return 99
    while n % 2 == 0: n //= 2; c += 1
    return c

h = int(sys.argv[1]); LM = int(sys.argv[2]); rule = 0 if sys.argv[3] == 'saw' else 1
iotas = [int(x) for x in sys.argv[4].split(',')]
sstep = int(sys.argv[5]) if len(sys.argv) > 5 else 7
tot = 0; bad = 0; hist = {}
for iota in iotas:
    nl, nt, hom, ex = census(h, iota, LM, rule, True, sstep)
    for e in ex:
        s, i1, i2, g1, g2, yF1, yF2, R0 = [int(x) for x in e]
        tot += 1
        t = i2 - i1; tau = v2(t); P = 4 * (g1 - g2)
        gap = t + g2 - g1
        ok = (yF1 == yF2 and tau % 2 == 1 and v2(P) == (tau + 3) // 2 and v2(g1) == (tau - 5) // 2
              and v2(g2) == (tau - 5) // 2 and v2(gap) == (tau - 1) // 2)
        if t > 0 and not ok: pass
        if not ok:
            bad += 1
            if bad <= 6: print('  MISMATCH', dict(s=s, i1=i1, i2=i2, g1=g1, g2=g2, yF1=yF1, yF2=yF2, tau=tau))
        hist[(tau, (g1 % 4))] = hist.get((tau, g1 % 4), 0) + 1
print('h', h, 'LM', LM, sys.argv[3], 'ee hits', tot, 'mismatches', bad)
for k in sorted(hist): print('   v2(t)=%d  filler offset %d : %d' % (k[0], k[1], hist[k]))
