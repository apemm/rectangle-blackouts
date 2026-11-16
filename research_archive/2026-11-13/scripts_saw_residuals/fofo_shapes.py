"""List the depth ratios (u : v) and sign of d for the Fo/Fo hits of fofo_cubic.census on the s = 0 diagonal.
Usage: py fofo_shapes.py h iota LM"""
import sys
from math import gcd
from fofo_cubic import census
h = int(sys.argv[1]); iota = int(sys.argv[2]); LM = int(sys.argv[3])
nl, tot, hom, ex = census(h, iota, LM, 0, False, h // 2)
print('h', h, 'LM', LM, 'labels', nl, 'hits', tot)
for e in ex:
    s, i1, i2, g1, g2, yF1, yF2, R0 = [int(x) for x in e]
    if s != 0: continue
    u = (yF1 - (2 * i1 + 1)) // 4; v = (yF2 - (2 * i2 + 1)) // 4; g = gcd(u, v)
    print('  i1 %d i2 %d  depths u=%d v=%d ratio %d:%d  d=%d  fillers row %d (T*-%d)' % (i1, i2, u, v, u // g, v // g, (i2 - i1) // 2, yF1, R0 - yF1))
