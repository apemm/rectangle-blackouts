"""V3 between SLF-Pc triples inside one class of a LAD region (row-1 type, r0 = 1).
Label (i, *): odd point (4X, 2i+1) with slot X = i - iota (rel; class slots X = 0 mod 64), i = iota mod 64.
SLF-Pc: vertex V = odd label point, shallow end E = V + (a, -(y_V - 1)), hole end G = V + (4 gam, g), g = y_G - y_V > 0,
2 a gam = u g with u = (y_V - 1)/2, a != 0 mod 4; W = (x_V + 4 gam + a, 1 + g).  Checked from the definitions:
right angle at V, E shallow (column != 0 mod 4), G a LAD hole in that row, W in the grid.
Usage: py slf_v3.py h iota Tstar Ep"""
import sys
from collections import defaultdict
from lad import eta_array
h, iota, Ts, Ep = map(int, sys.argv[1:5]); E, P = eta_array(Ep)
row = lambda X: Ts - 8 * int(E[X % P])
def divisors(n):
    out = []; d = 1
    while d * d <= n:
        if n % d == 0: out += [d, n // d]
        d += 1
    return set(out)
Dwin = 8 * max(E.tolist()) + 24
Wmap = defaultdict(list); ntri = 0
for i in range(iota, (h - 1) // 2 + 1, 64):
    yV = 2 * i + 1
    if yV >= Ts - Dwin - 128: continue           # near-band labels excluded
    XV = i - iota; xV = 4 * XV; u = (yV - 1) // 2
    hole_rows = sorted({row(X) for X in range(P) if X % 2 == 0 and X % 64 != 0})
    for yG in hole_rows:
        g = yG - yV
        if g <= 0 or 1 + g > h: continue
        if (u * g) % 2: continue
        for d in divisors(u * g // 2):
            for gam in (d, -d):
                a = u * g // (2 * gam)
                if a % 4 == 0: continue
                XG = XV + gam
                if XG % 64 == 0 or row(XG) != yG: continue
                # definition check: right angle at V between E - V = (a, -(yV-1)) and G - V = (4 gam, g)
                assert a * 4 * gam - (yV - 1) * g == 0
                xW = xV + 4 * gam + a; yW = 1 + g
                Wmap[(xW, yW)].append((i, gam, yG)); ntri += 1
coll = {k: v for k, v in Wmap.items() if len({t[0] for t in v}) > 1 or len(v) > 1}
print('h=%d iota=%d T*=%d: SLF-Pc triples %d, W with >=2 triples %d' % (h, iota, Ts, ntri, len(coll)))
for k, v in list(coll.items())[:5]: print('  W', k, v)
