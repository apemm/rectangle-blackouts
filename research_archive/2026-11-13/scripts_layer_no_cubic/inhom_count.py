"""Integer points of the two-filler Fo/Fo surface with filler rows differing by e (Y units):
   4 d u (p - 2D) = (p - 4d)(p^2 + D^2),  D = d + e,  u = depth of L1, v = u - D = depth of L2.
Count (p, d) with 0 < |p|, |d| <= X, p != 2D, u integer in (0, X], v in (0, X]; split off the
polynomial branch p = 2d. No slot or class congruences (an upper-bound style census).
Usage: py inhom_count.py e X"""
import sys
import numpy as np
from numba import njit

@njit(cache=True)
def run(e, X):
    tot = 0; poly = 0; dneg = 0
    ex = np.zeros((12, 4), dtype=np.int64); nex = 0
    for d in range(-X, X + 1):
        if d == 0: continue
        D = d + e
        for p in range(-X, X + 1):
            if p == 0 or p == 2 * D: continue
            num = (p - 4 * d) * (p * p + D * D)
            den = 4 * d * (p - 2 * D)
            if num % den: continue
            u = num // den
            v = u - D
            if u <= 0 or v <= 0 or u > X or v > X: continue
            tot += 1
            if p == 2 * d: poly += 1
            elif nex < 12:
                ex[nex, 0] = p; ex[nex, 1] = d; ex[nex, 2] = u; ex[nex, 3] = v; nex += 1
            if d < 0: dneg += 1
    return tot, poly, dneg, ex[:nex]

e = int(sys.argv[1]); X = int(sys.argv[2])
tot, poly, dneg, ex = run(e, X)
print('e', e, 'X', X, 'solutions', tot, 'on branch p=2d', poly, 'with d<0', dneg)
for r in ex: print('   p, d, u, v =', list(r))
