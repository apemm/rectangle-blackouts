"""Exact check of the two-label/one-filler right-angle obstruction (family F)
in the period-seven profile with Hilbert slots x = S(M r + xi).

Sea (filled_mod7_profile_cover.md (3)): column x = 0 mod 7 holds the filler F
unless it is an occupied label column; label columns are multiples of S.
A support here: vertex V (label point), leg to opposite-parity label point Q
(horizontal distance X = S q, vertical Y odd), leg to the filler E = V + (u, F - y_V).
Fatal when E is black and the fourth corner W = Q + E - V is white in a column whose
only black point has parity different from row(W)."""
import math, sys
from math import gcd

def v(p, n):
    if n == 0: return 99
    n = abs(n); c = 0
    while n % p == 0:
        n //= p; c += 1
    return c

def crt(r1, m1, r2, m2):
    # solve x = r1 mod m1, x = r2 mod m2 (moduli need not be coprime)
    g = gcd(m1, m2)
    assert (r2 - r1) % g == 0
    l = m1 // g * m2
    t = ((r2 - r1) // g) * pow(m1 // g, -1, m2 // g) % (m2 // g)
    return (r1 + m1 * t) % l, l

def profile(h, L, g):
    # H in [h-195,h] with H-L = g mod 7, H != L mod 2 ; F in [1000,3743], F-L = 3g, F = L mod 2
    H = next(x for x in range(h, h - 196, -1) if (x - L) % 7 == g % 7 and (x - L) % 2 == 1)
    F = next(x for x in range(1000, 3744) if (x - L) % 7 == (3 * g) % 7 and (x - L) % 2 == 0)
    return F, H

def sea_row(x, S, F, occupied):
    # only the period-zero logic is needed here
    assert x % 7 == 0
    return None if (x % S == 0 and occupied(x)) else F

def check_case(S, M, h, L, g, mode):
    F, H = profile(h, L, g)
    Wn = list(range(1, 2 * M))            # window of slot gaps at rank distance 1
    lcm = 1
    for q in Wn: lcm = lcm * q // gcd(lcm, q)
    A2 = max(v(2, q) for q in Wn); A7 = max(v(7, q) for q in Wn)
    s2, s7 = v(2, S), v(7, S)
    odd_part = lcm
    while odd_part % 2 == 0: odd_part //= 2
    while odd_part % 7 == 0: odd_part //= 7
    S_other = S // (2 ** s2) // (7 ** s7)
    # vertex row y_V: y_V = F mod 2^(s2+A2)*odd_part*S_other, and y_V in label class 0 (= L mod 7)
    a0 = L % 7  # class 0 residue mod 7
    mod1 = 2 ** (s2 + A2) * odd_part * S_other
    r, m = crt(F % mod1, mod1, a0, 7)
    # want v2(F - y_V) exactly s2 + A2: shift by m/2-type adjustment if needed
    y0 = r + m * (10 ** 6 // m + 1)
    while v(2, F - y0) != s2 + A2:
        y0 += m
    # vertical gap Y odd, v7(Y) = s7 + 1 + A7 exactly, other primes free
    e7 = s7 + 1 + A7
    if mode == "lower":
        Y = 7 ** e7
        yV, yQ = y0, y0 + Y      # vertex is the lower point, row F below
    else:
        Y = 7 ** e7               # upper vertex: needs Y < F
        if Y >= F: return None
        yV, yQ = y0, y0 - Y      # vertex is the upper point
    assert (yV - yQ) % 2 == 1
    assert yQ % 7 == a0 and yV % 7 == a0      # both rows in label class 0 (a = b mod 7 block)
    assert 1 <= min(yV, yQ) and max(yV, yQ) <= h
    ok_all = True
    results = []
    for q in Wn:
        for sgn in (1, -1):
            X = sgn * S * q                   # x_Q - x_V, x_V = 0
            num = -(yQ - yV) * (F - yV)
            if num % X != 0:
                ok_all = False; results.append((q, sgn, "nonintegral")); continue
            u = num // X
            assert X * u + (yQ - yV) * (F - yV) == 0
            E = (u, F); W = (X + u, yQ + F - yV)
            # E black: period-zero, not a multiple of S (so not a slot) -> filler F
            okE = (u % 7 == 0) and (u % S != 0)
            okW_col = ((X + u) % 7 == 0) and ((X + u) % S != 0)
            okW_row = 1 <= W[1] <= h and W[1] != F and (W[1] - F) % 2 == 1
            tilted = X != 0 and u != 0 and (yQ - yV) != 0 and (F - yV) != 0
            ok = okE and okW_col and okW_row and tilted
            ok_all &= ok
            results.append((q, sgn, ok))
    return ok_all, dict(F=F, H=H, yV=yV, yQ=yQ, Y=yQ - yV, v2=v(2, F - yV), v7Y=v(7, yQ - yV)), results

if __name__ == "__main__":
    h = 10 ** 40
    for S in (1568, 2940, 1575, 2520, 1792):
        for mode in ("lower", "upper"):
            good = []
            for M in range(1, 40):
                L = 1 if mode == "lower" else 2   # parity of vertex row = parity of F
                res = check_case(S, M, h, L, 1, mode)
                if res is None: continue
                if res[0]: good.append(M)
            print(S, mode, "all q fatal for M in", good)
    ok, info, res = check_case(1568, 3, h, 1, 1, "lower")
    print(ok, info)
