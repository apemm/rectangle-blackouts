"""Exact values of the rank-distance bound used in Lemmas SS, BI, J (S = 32).
F(U) = floor(2U(U+1)/(SM) + (M-1)/M) bounds the rank distance d of a constraint on
diagonal U; locality forces (|U| - t)_+^2 < 16 d <= 16 F(U) for an endpoint with |T| <= t;
a leg X = 32q with odd Y = |2U+1| needs Y >= 31 (proved by the parametrisation).
Dmax(t) = max F(U) over admissible U.  Also checks the minimal odd leg Y with 32 | X.
"""
from fractions import Fraction as Fr
from math import isqrt

S = 32
# minimal odd Y with a Pythagorean partner X = 32 q (brute force over Y < 200)
ymin = None
for Y in range(1, 200, 2):
    for u in range(1, Y, 2):
        if (Y * Y) % u == 0:
            w = Y * Y // u
            X = (w - u) // 2
            if X > 0 and X % S == 0:
                ymin = Y; break
    if ymin: break
print("minimal odd Y with 32 | X:", ymin)


def F(U, M):
    return (Fr(2 * U * (U + 1), S * M) + Fr(M - 1, M)).__floor__()


def dmax(t, M):
    best = 0; U_hi = 0
    for U in range(-(10 * t + 100), 10 * t + 101):
        if abs(2 * U + 1) < ymin:
            continue
        f = F(U, M)
        e = max(abs(U) - t, 0)
        if f >= 1 and e * e < 16 * f:
            best = max(best, f); U_hi = max(U_hi, abs(U))
    return best, U_hi


for M in (3, 4):
    print(f"M={M}: largest t with no admissible constraint:",
          max(t for t in range(0, 40) if dmax(t, M)[0] == 0))
    for k in range(1, 13):
        t = 2 ** k - 1
        dm, uh = dmax(t, M)
        crude = 0.116627 * (t + 4.5) ** 2 + 1
        print(f"  k={k:2d} t={t:5d}: Dmax={dm:8d} (|U|<={uh}), crude {crude:10.1f}, "
              f"BI needs <= 4^(k-1)={4**(k-1):8d}: {dm <= 4**(k-1)}; "
              f"J needs Dmax(2m-1)<=m^2 with m=2^(k-1): {dm <= 4**(k-1)}")
