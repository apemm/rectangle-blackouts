"""Hole-independent version: two cross pairs of a vertically adjacent Hilbert pair
(same odd row alpha) in an a = b (mod 7) block, type (0,0), with L of the parity of alpha.
Only binary sea columns (residues != 0 mod 7) are used, so hole choices F/H are irrelevant.
Also checks the Hilbert line-adjacency residue property used for existence."""
from math import gcd
import itertools

def chi(x):
    x %= 7
    return 0 if x == 0 else (1 if x in (1, 2, 4) else -1)

def sea(x, L, F, H):
    # profile (3) with g = 1 (normalisation divisor 1 is a residue): actual = normalised
    r = x % 7
    if r == 0: return ('hole', None)
    return ('bin', L if chi(r) == -1 else H)

def v(p, n):
    n = abs(n); c = 0
    while n and n % p == 0: n //= p; c += 1
    return c

def hilbert(q):
    pts = [(0, 0)]; s = 1
    while s < q:
        pts = ([(y, x) for (x, y) in pts] + [(x, y + s) for (x, y) in pts] +
               [(x + s, y + s) for (x, y) in pts] + [(2*s-1-y, s-1-x) for (x, y) in pts])
        s *= 2
    return pts

def line_property(k):
    """For every column i of H_{2^k}: the lower endpoints j of vertical curve
    adjacencies {(i,j),(i,j+1)} cover all residues mod 7. Same for rows/horizontal."""
    q = 2 ** k; H = hilbert(q)
    colres = {i: set() for i in range(q)}; rowres = {j: set() for j in range(q)}
    for a, b in zip(H, H[1:]):
        if a[0] == b[0]: colres[a[0]].add(min(a[1], b[1]) % 7)
        else: rowres[a[1]].add(min(a[0], b[0]) % 7)
    return (min(len(s) for s in colres.values()), min(len(s) for s in rowres.values()))

def check(S, M, h):
    L = 1; g = 1
    H = next(x for x in range(h, h - 196, -1) if (x - L) % 7 == g and (x - L) % 2 == 1)
    F = next(x for x in range(1000, 3744) if (x - L) % 7 == 3 * g % 7 and (x - L) % 2 == 0)
    Wn = range(1, 2 * M)
    lcm = 1
    for q in Wn: lcm = lcm * q // gcd(lcm, q)
    A2 = max(v(2, q) for q in Wn)
    assert max(v(7, q) for q in Wn) == 0, "window must avoid multiples of 7"
    mod = 2 ** (v(2, S) + A2) * 7
    for p in (3, 5, 11, 13):
        while lcm % p == 0 and mod % (p ** (v(p, lcm))) != 0: mod *= p
    # alpha = L mod mod, v7(alpha - L) = 1, alpha = 1 mod 14 (odd, class 0)
    alpha = L + mod * 1000
    while v(7, alpha - L) != 1 or alpha % 14 != 1: alpha += mod
    allok = True
    for t in (2, 3):
        for step in (+1, -1):
            # lower-j cell has (b - alpha)/7 = t ; upper-j cell t+2. e = left cell.
            kk = 1000 + ((1 + t) % 2)          # parity fix: b must be even
            b_low = alpha + 7 * t + 49 * kk
            assert b_low % 14 == 8 and ((b_low - alpha) // 7) % 7 == t and v(7, b_low - alpha) == 1
            b_up = b_low + 14
            be, bf = (b_low, b_up) if step == 1 else (b_up, b_low)
            for q in Wn:
                fired = []
                X = S * q    # x_e = 0, x_f = X
                # option 1: vertex (0, alpha) [odd point of e], leg to (X, bf), E row L
                Y1 = bf - alpha
                num = -Y1 * (L - alpha)
                if num % X == 0:
                    u = num // X; kind, row = sea(u, L, F, H)
                    W = (X + u, bf + L - alpha)
                    k2, r2 = sea(W[0], L, F, H)
                    if kind == 'bin' and row == L and 1 <= W[1] <= h and k2 == 'bin' and (r2 - W[1]) % 2 == 1:
                        fired.append(1)
                # option 4: vertex (X, alpha) [odd point of f], leg to (0, be), E row L
                Y2 = be - alpha
                num = Y2 * (L - alpha)      # (-X) u + Y2 (L - alpha) = 0
                if num % X == 0:
                    u = num // X; kind, row = sea(X + u, L, F, H)
                    W = (u, be + L - alpha)
                    k2, r2 = sea(W[0], L, F, H)
                    assert (-X) * u + Y2 * (L - alpha) == 0
                    if kind == 'bin' and row == L and 1 <= W[1] <= h and k2 == 'bin' and (r2 - W[1]) % 2 == 1:
                        fired.append(4)
                if not fired:
                    allok = False
    return allok

if __name__ == "__main__":
    for k in range(3, 9):
        print("line property k=%d: min residues per column/row" % k, line_property(k))
    for M in (1, 2, 3):
        print("S=1568 M=%d binary obstruction holds:" % M, check(1568, M, 10 ** 30))
