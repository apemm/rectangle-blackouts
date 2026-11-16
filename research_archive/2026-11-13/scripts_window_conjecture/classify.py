"""List all N-windows of width K = h (all A-sets, one per reflection orbit) and describe each:
best cover by two adjacent lattice lines of a non-axis direction (c,d), |c|,|d| <= 3,
and the points left over.  Usage: py classify.py h lo hi"""
import sys, time
from math import gcd
from wk3 import build, count, parts_list

def two_line_cover(pts):
    best = (0, None)
    for c in range(1, 4):
        for d in range(-3, 4):
            if d == 0 or gcd(c, abs(d)) != 1: continue
            # det((c,d),(x,y)) = c*y - d*x
            vals = {}
            for (x, y) in pts:
                v = c * y - d * x
                vals[v] = vals.get(v, 0) + 1
            for v in vals:
                n = vals[v] + vals.get(v + 1, 0)
                if n > best[0]:
                    best = (n, (c, d, v))
    return best

h, lo, hi = map(int, sys.argv[1:4]); K = h
parts = parts_list(h, True)
cells, M = build(h, K)
t0 = time.time()
for A in parts[lo:hi]:
    W = []
    n = count(h, K, A, cells, M, W)
    for w in W:
        pts = [(x + 1, r) for x, e in enumerate(w) for r in e]
        nb, line = two_line_cover(pts)
        c, d, v = line
        rest = [p for p in pts if c * p[1] - d * p[0] not in (v, v + 1)]
        print('A', A, ' '.join(f'{a}-{b}' for a, b in w), '| two-line cover', nb, 'of', 2 * K,
              'dir', (c, d), 'rest', rest, flush=True)
print('sec', round(time.time() - t0, 1))
