"""Type (0,5) block (odd rows = L mod 7, even rows = L+5g mod 7), L odd: single vertical
Hilbert adjacency forces a fatal binary-column right angle for M <= 3.  Also the
design rule check: if L is even (class-0 endpoint parity != L parity), scan all
small configurations for any F1 support (none expected)."""
from math import gcd
import sys
sys.path.insert(0, '.')
from check_binary_angle import chi, sea, v

def run(S, M, h, L, g):
    H = next(x for x in range(h, h - 196, -1) if (x - L) % 7 == g % 7 and (x - L) % 2 == 1)
    F = next(x for x in range(1000, 3744) if (x - L) % 7 == 3 * g % 7 and (x - L) % 2 == 0)
    Wn = range(1, 2 * M)
    lcm = 1
    for q in Wn: lcm = lcm * q // gcd(lcm, q)
    A2 = max(v(2, q) for q in Wn)
    mod = 2 ** (v(2, S) + A2) * 49 * (lcm // (2 ** v(2, lcm)))
    alpha = L + mod * 1001
    while v(7, alpha - L) != 2 or alpha % 2 != 1: alpha += mod
    ok = True
    for be in (alpha + 5 * g + 7 * k for k in range(1, 60) if (alpha + 5 * g + 7 * k) % 2 == 0):
        for step in (14, -14):
            bf = be + step
            for q in Wn:
                X = S * q; fired = False
                Y1 = bf - alpha; num = -Y1 * (L - alpha)
                if num % X == 0:
                    u = num // X; k1, r1 = sea(u, L, F, H); Wc = X + u; k2, r2 = sea(Wc, L, F, H)
                    Wr = bf + L - alpha
                    fired |= (k1 == 'bin' and r1 == L and k2 == 'bin' and (r2 - Wr) % 2 == 1 and 1 <= Wr <= h)
                Y2 = be - alpha; num = Y2 * (L - alpha)
                if num % X == 0:
                    u = num // X; k1, r1 = sea(X + u, L, F, H); k2, r2 = sea(u, L, F, H)
                    Wr = be + L - alpha
                    fired |= (k1 == 'bin' and r1 == L and k2 == 'bin' and (r2 - Wr) % 2 == 1 and 1 <= Wr <= h)
                ok &= fired
    return ok

for M in (1, 2, 3):
    print("type (0,5), L odd, M=%d: every q fatal for all tested b_e:" % M, run(1568, M, 10**30, 1, 1))
