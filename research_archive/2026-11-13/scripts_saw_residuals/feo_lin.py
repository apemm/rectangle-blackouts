"""Numba version of feo_closed.py (same closed form, all diagonals s, all slots i = iota mod 16 occupied).
Usage: py feo_fast.py h iota excl_band"""
import sys
import numpy as np
from numba import njit

@njit(cache=True)
def count(h, iota, eb):
    A = (h + 1) // 2; K = h // 2
    r1 = (2 * iota + 1) % 16
    R0 = 0
    for y in range(2, h + 1):
        if y % 16 == r1: R0 = y
    OFF = np.array([-3, -2, -1, 0])
    nl = 0; tot = 0; mult = 0; lin = 0
    for s in range(-(h // 2), h // 2):
        T = 2 * s + 1
        for iP in range(1, A):
            if iP % 16 != iota or not (0 <= iP + s < K): continue
            nl += 1
            yP = 2 * iP + 1
            if yP > R0 - 24 - eb: continue
            cnt = 0
            for a in (1, 3):
                yV = R0 + 8 * OFF[a]
                f = yV - yP
                if f % 32 != 16: continue
                fp = f // 16
                N = fp * (20 * fp - T)
                if N == 0: continue
                aN = abs(N)
                d = 1
                while d * d <= aN:
                    if aN % d == 0:
                        for D0 in (d, aN // d):
                            if D0 == d and d * d == aN and D0 != d: continue
                            for sg in (1, -1):
                                D = sg * D0
                                if d * d == aN and D0 == aN // d and D0 == d and False: continue
                                g = D - 2 * fp
                                if (g - a) % 4 != 0: continue
                                t = D + N // D - 4 * fp
                                iQ = iP + t
                                if iQ % 16 != iota or not (1 <= iQ < A and 0 <= iQ + s < K): continue
                                yQ = 2 * (iQ + s) + 2
                                if eb > 0 and yQ > R0 - 24 - eb: continue
                                wy = yP + yQ - yV
                                if 1 <= wy <= h:
                                    cnt += 1
                                    if D == fp or D == -fp or D == 20 * fp - T or D == -(20 * fp - T): lin += 1
                            if d * d == aN: break
                    d += 1
            tot += cnt
            if cnt > 1: mult += 1
    return nl, tot, lin

h = int(sys.argv[1]); iota = int(sys.argv[2]); eb = int(sys.argv[3])
nl, tot, mult = count(h, iota, eb)
print('h', h, 'iota', iota, 'labels', nl, 'Feo', tot, 'per label %.4f' % (tot / nl), 'linear-branch hits:', mult)
