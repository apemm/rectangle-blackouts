"""Check the identity (g^2-f^2)(z^2-f^2) = (2fY)^2 for common legs of Sq and S(q+delta),
g = S delta, z = 2Sq + g, f = L1 - L2; and count close-q common legs (all Y) vs h."""
import sys, math
from collections import defaultdict
from pair_corr import vectors
S = int(sys.argv[1]); D = int(sys.argv[2])
for lg in map(int, sys.argv[3:]):
    h = 2 ** lg
    legs = defaultdict(set)
    for q, Y in vectors(S, h):
        legs[Y].add(q)
    cnt = 0; bad = 0; sq_case = 0
    for Y, qs in legs.items():
        for q in qs:
            for d in range(1, D + 1):
                if q + d in qs:
                    cnt += 1
                    L1 = math.isqrt((S*(q+d))**2 + Y*Y); L2 = math.isqrt((S*q)**2 + Y*Y)
                    f = L1 - L2; g = S * d; z = 2 * S * q + g
                    if (g*g - f*f) * (z*z - f*f) != (2*f*Y)**2 or not (0 < f < g) or f % 2: bad += 1
                    r = math.isqrt(g*g - f*f)
                    if r * r == g*g - f*f: sq_case += 1
    print(f"S={S} D={D} h=2^{lg}: close-q common legs (all Y) = {cnt}, identity failures = {bad}, square-D' cases = {sq_case}")
