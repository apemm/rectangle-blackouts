# Sanity check of the parametrization of S_T and basic data. Under 60 s.
import math, sys
from math import gcd, isqrt
from fractions import Fraction

def S_T(T, h):
    """All d != 0 with 20 d^2 + 4 T d + T^2 = L^2, 0 < L < h (brute force)."""
    out = []
    dmax = int(h / math.sqrt(20)) + 2 + abs(T)
    for d in range(-dmax, dmax + 1):
        if d == 0: continue
        q = 20*d*d + 4*T*d + T*T
        L = isqrt(q)
        if L*L == q and 0 < L < h:
            out.append(d)
    return out

def param_points(T, h):
    """d from r = y(x+y)/(x^2-5y^2) scaled: (d, T, L) = g (y(x+y), x^2-5y^2, x^2+2xy+5y^2)/c."""
    out = set()
    B = int(math.sqrt(h)) * 3 + 10
    for x in range(-B, B + 1):
        for y in range(1, B + 1):
            if gcd(x, y) != 1: continue
            n = x*x - 5*y*y
            m = y*(x + y)
            L = x*x + 2*x*y + 5*y*y
            c = gcd(gcd(abs(n), abs(m)), L)
            n //= c; m //= c; L //= c
            if n == 0: continue
            if T % n != 0: continue
            g = T // n
            d = g*m; LL = abs(g)*L
            if d != 0 and LL < h:
                out.add(d)
    return sorted(out)

ok = True
for T in [1, 3, 5, 7, 11, 15, 19, 29, 55, 95, 209, 1045, -11, -55]:
    h = 3000
    a = sorted(S_T(T, h)); b = param_points(T, h)
    if a != b:
        ok = False
        print("MISMATCH", T, sorted(set(a) - set(b))[:10], sorted(set(b) - set(a))[:10])
    print(T, len(a), a[:14])
print("parametrization agrees:", ok)
