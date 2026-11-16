"""Junction test: SAW gap (row-1 sea) on columns < X0, Sea(1,g) (deep row g) on columns >= X0. No labels."""
import sys, time
import numpy as np
from driver import analyse
from board import shapes
h = int(sys.argv[1]); g = int(sys.argv[2]); ph = int(sys.argv[3]); iota8 = int(sys.argv[4]) if len(sys.argv) > 4 else 1; r0 = int(sys.argv[5]) if len(sys.argv) > 5 else 1
off = [-3, -2, -1, 0]
r1 = (2 * iota8 + 1) % 16
R0 = max(y for y in range(2, h + 1) if y % 16 == r1)
W = h * h // 4 + 1
Wd = 2 * W + 64
X0 = 4 * ((Wd // 2) // 4)
kind = np.zeros((Wd, h + 2), dtype=np.int64)
for x in range(Wd):
    if x % 4: kind[x, r0] = 1
    else:
        n = x // 4
        kind[x, (R0 + 8 * off[(n - ph) % 4]) if x < X0 else g] = 2
res, ex = analyse(h, kind, shapes(h), only_filler=False)
print('h', h, 'g', g, 'phase', ph, dict(res))
for k in res: print('   ', k, ex[k][0])
