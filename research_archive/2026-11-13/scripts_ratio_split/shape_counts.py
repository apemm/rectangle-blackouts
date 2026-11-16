# Sanity check for the truncated additive split.
# N_IV(H) = #{lambda : q_lambda <= H}, N_FF(H) = #{shapes (a,b) : |U'| <= H},
# and the tails kappa_IV(>H) = sum_{q > H} (1/q + 1/p), kappa_FF(>H) = sum_{|U'| > H} 1/|U'|
# (tails truncated at the enumeration cutoff, so they are lower bounds of the true tails).
from math import gcd, sqrt, log
import sys

def riv(Hmax, kmin):
    out = []  # (q, p)
    bemax = int(sqrt(5 * Hmax)) + 2
    for be in range(3, bemax + 1, 2):
        for al in range(1, be, 2):
            if gcd(al, be) != 1:
                continue
            d = be - al
            if (d & -d).bit_length() - 1 < kmin - 2:
                continue
            F = 4 * (al - 2 * be) ** 2 + be ** 2
            g = gcd(F, d)
            q = al * F // g
            p = (al * F + 4 * d * be * be) // g
            assert g in (1, 5) and p > q
            out.append((q, p))
    return out

def rff(Hmax):
    out = []  # |U'|
    R = int(sqrt(40 * Hmax)) + 2
    for b in range(1, R + 1):
        for a in range(-R, R + 1):
            if gcd(a, b) != 1:
                continue
            U = (a - 4 * b) * (a * a + b * b)
            if U == 0:
                continue
            V = a ** 3 - 4 * a * a * b - 3 * a * b * b + 4 * b ** 3
            gg = gcd(U, V)
            assert 40 % gg == 0
            out.append(abs(U) // gg)
    return out

Hcut = 30000
iv = riv(Hcut, 5)
iv4 = riv(Hcut, 4)
ff = rff(Hcut)
print("Hcut", Hcut, "lambdas(k=5) with q<=Hcut:", sum(1 for q, p in iv if q <= Hcut),
      "shapes |U'|<=Hcut:", sum(1 for u in ff if u <= Hcut))
for H in [100, 300, 1000, 3000, 10000, 30000]:
    n5 = sum(1 for q, p in iv if q <= H)
    n4 = sum(1 for q, p in iv4 if q <= H)
    nf = sum(1 for u in ff if u <= H)
    tail_ff = sum(1.0 / u for u in ff if H < u <= Hcut)
    tail_iv = sum(1.0 / q + 1.0 / p for q, p in iv4 if H < q <= Hcut)
    print(f"H={H:6d} N_IV5={n5:4d} N_IV4={n4:4d} N_FF={nf:6d} N_FF/H^(2/3)={nf / H ** (2 / 3):.3f}"
          f"  tailFF(H,Hcut]={tail_ff:.4f} x H^(1/3)={tail_ff * H ** (1 / 3):.3f}  tailIV4={tail_iv:.2e}")
