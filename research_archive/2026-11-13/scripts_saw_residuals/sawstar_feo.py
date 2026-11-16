"""Feo census (all three vertex choices) for one class line with all slots i = iota mod LM occupied,
SAW heights by slot offset (T*-24, T*-16, T*-8, T*), T* chosen by rule:
  'saw'  : T* = max{y <= h : y = 2*iota+1 mod 16}                       (deep_layer_sawtooth.md)
  'star' : T* = max{y <= h : y = yP + 32 (T = 3 mod 4) or yP + 48 (T = 1 mod 4) mod 64}, LM = 32.
Brute force: V vertex over all g with |4g| <= h^2/2; P vertex and Q vertex over all Q in the class line.
Usage: py sawstar_feo.py h iota rule LM [sstep]"""
import sys
import numpy as np
from numba import njit

@njit(cache=True)
def census(h, iota, rule, LM, sstep):
    A = (h + 1) // 2; K = h // 2
    OFF = np.array([-3, -2, -1, 0])
    G = h * h // 8
    nV = 0; nP = 0; nQ = 0; nl = 0
    for s in range(-(h // 2), h // 2, sstep):
        T = 2 * s + 1
        yP0 = (2 * iota + 1) % 64
        if rule == 0:
            res, mod = (2 * iota + 1) % 16, 16
        else:
            res, mod = ((yP0 + (32 if T % 4 == 3 else 48)) % 64), 64
        R0 = 0
        for y in range(2, h + 1):
            if y % mod == res: R0 = y
        occ = np.zeros(A + 1, dtype=np.bool_)
        for i in range(1, A):
            if i % LM == iota and 0 <= i + s < K: occ[i] = True
        for iP in range(1, A):
            if not occ[iP]: continue
            yP = 2 * iP + 1
            if yP > R0 - 24 - 80: continue
            nl += 1
            xP = 4 * iP
            # V vertex
            for g in range(-G, G + 1):
                if g == 0: continue
                n = iP + g
                if 0 < n < A and occ[n]: continue
                yV = R0 + 8 * OFF[(n - iota) % 4]
                f = yV - yP; kap = yV - (2 * (iP + s) + 2)
                num = 16 * g * g + f * kap; den = 16 * g + 2 * f
                if den == 0 or num % den != 0: continue
                t = num // den
                iQ = iP + t
                if iQ < 1 or iQ >= A or not occ[iQ]: continue
                yQ = 2 * (iQ + s) + 2
                if yQ > R0 - 104: continue
                wy = yP + yQ - yV
                if 1 <= wy <= h: nV += 1
            # P vertex and Q vertex
            for iQ in range(1, A):
                if not occ[iQ] or iQ == iP: continue
                t = iQ - iP; yQ = 2 * (iQ + s) + 2
                if yQ > R0 - 104: continue
                for a in range(4):
                    yV = R0 + 8 * OFF[a]
                    f = yV - yP
                    num = -f * (yQ - yP)
                    if num % (16 * t) == 0:
                        g = num // (16 * t)
                        if g != 0 and (g - a) % 4 == 0:
                            n = iP + g
                            if not (0 < n < A and occ[n]):
                                wy = yV + yQ - yP
                                if 1 <= wy <= h: nP += 1
                    # Q vertex: 16 (nV - nQ)(nP - nQ) + (yV - yQ)(yP - yQ) = 0
                    rhs = -(yV - yQ) * (yP - yQ)
                    if rhs % (16 * (-t)) == 0:
                        d = rhs // (16 * (-t))
                        n = iQ + d
                        if d != 0 and (n - iota - a) % 4 == 0 and not (0 < n < A and occ[n]):
                            wy = yV + yP - yQ
                            if 1 <= wy <= h: nQ += 1
    return nl, nV, nP, nQ

h = int(sys.argv[1]); iota = int(sys.argv[2]); rule = 0 if sys.argv[3] == 'saw' else 1
LM = int(sys.argv[4]); sstep = int(sys.argv[5]) if len(sys.argv) > 5 else 1
nl, nV, nP, nQ = census(h, iota, rule, LM, sstep)
print('h', h, 'iota', iota, sys.argv[3], 'LM', LM, 'labels', nl, 'Feo V-vertex', nV, 'P-vertex', nP, 'Q-vertex', nQ)
