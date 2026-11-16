"""Sanity checks for the heavy-term note (stride 4).
D_T = { |d| : 16 d^2 + (2d+T)^2 = L^2, 0 < L < h, d != 0, |d| < n_T }.
(1) kappa_T >= g(T) - 1 for odd T, 5 not | T, 0 < |T| < 0.124 h.
(2) 2-adic distribution of D_T on the richest diagonals.
"""
import sys
from math import gcd, isqrt

h = int(sys.argv[1]) if len(sys.argv) > 1 else 6000
A = (h + 1) // 2
K = h // 2

def nT(T):
    s = (T - 1) // 2
    lo = max(0, -s)
    hi = min(A, K - s)
    return max(0, hi - lo)

# enumerate Pythagorean triples x^2 + y^2 = L^2, x = 4d (d>0), y odd, L < h
D = {}
m = 2
while m * m < h:
    for n in range(1, m):
        if (m - n) % 2 == 0 or gcd(m, n) != 1:
            continue
        x0, y0, L0 = 2 * m * n, m * m - n * n, m * m + n * n
        if L0 >= h:
            continue
        # make x0 the even leg; scale g odd so that 4 | g x0 needs 4 | x0
        if x0 % 4 != 0:
            continue
        g = 1
        while g * L0 < h:
            x, y = g * x0, g * y0
            d = x // 4
            for dd in (d, -d):
                for yy in (y, -y):
                    T = yy - 2 * dd
                    if T == 0 or abs(T) >= h:
                        continue
                    if abs(dd) < nT(T):
                        D.setdefault(T, set()).add(abs(dd))
            g += 2
    m += 1

def gsplit(T):
    T = abs(T)
    r = 1
    p = 2
    while p * p <= T:
        if T % p == 0:
            e = 0
            while T % p == 0:
                T //= p
                e += 1
            if p % 5 in (1, 4):
                r *= 2 * e + 1
        p += 1
    if T > 1 and T % 5 in (1, 4):
        r *= 3
    return r

# (1) lower bound kappa_T >= g(T) - 1
bad = 0
tested = 0
for T in range(-h + 1, h, 2):
    if T % 5 == 0 or abs(T) >= 0.124 * h:
        continue
    k = len(D.get(T, ()))
    g = gsplit(T)
    tested += 1
    if k < g - 1:
        bad += 1
        if bad <= 5:
            print("violation", T, k, g)
print("h", h, "tested", tested, "violations of kappa >= g-1:", bad)
ratios = [len(D.get(T, ())) / gsplit(T) for T in range(1, int(0.124 * h), 2) if T % 5 and gsplit(T) >= 9]
print("min kappa/g over g>=9, small T:", min(ratios) if ratios else None)

# (2) 2-adic distribution on the richest diagonals
rich = sorted(D, key=lambda T: -len(D[T]))[:12]
for T in rich:
    S = D[T]
    k = len(S)
    row = [sum(1 for d in S if d % (2 ** a) == 0) for a in range(1, 7)]
    print("T", T, "kappa", k, "|D cap 2^a Z| a=1..6:", row,
          "expected", [round(k / 2 ** a, 1) for a in range(1, 7)])
tot = sum(len(S) for S in D.values())
tot_a = [sum(1 for S in D.values() for d in S if d % (2 ** a) == 0) for a in range(1, 7)]
print("sum kappa / h", round(tot / h, 3), "fractions divisible by 2^a:", [round(t / tot, 4) for t in tot_a])
