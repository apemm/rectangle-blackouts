# Scaling family: T = q T', H = q (h'+2).  Check (i) q*D_{T'}(h') subset of D_T(H) and (ii) k_T(H) bounded in q,
# and compare with the bound K = |S_{T'}(h'+2)| + 4 tau(T')^2 (1 + log(3.618 (h'+2)/|T'|)/log phi).
import sys
from math import isqrt, gcd, log, sqrt
from common import nT

def divisors(n):
    n = abs(n); small = [g for g in range(1, isqrt(n) + 1) if n % g == 0]
    return sorted(set(small + [n // g for g in small]))

def S_single(T, h):
    out = set()
    for g in divisors(T):
        N = T // g; R = (h - 1) // g  # g(x^2+y^2) < h  <=> x^2+y^2 <= R
        X = isqrt(R)
        for x in range(-X, X + 1):
            if x == 0: continue
            disc = 5 * x * x + 4 * N
            if disc < 0: continue
            z = isqrt(disc)
            if z * z != disc: continue
            for zz in (z, -z):
                if (x + zz) % 2: continue
                y = (x + zz) // 2
                if y < 1 or gcd(abs(x), y) != 1 or x * x + y * y > R or (g * x * y) % 2: continue
                out.add(g * x * y // 2)
    return out

def is_prime(n):
    return n > 1 and all(n % p for p in range(2, isqrt(n) + 1))

phi = (1 + sqrt(5)) / 2
for (Tp, hp) in [(1045, 2000), (-1045, 2000), (6061, 20000), (11, 40)]:
    Dp = {abs(d) for d in S_single(Tp, hp) if abs(d) < nT(hp, Tp)}
    S2 = S_single(Tp, hp + 2)
    tau = len(divisors(Tp))
    K = len(S2) + 4 * tau**2 * (1 + log(3.618 * (hp + 2) / abs(Tp)) / log(phi))
    row = []
    for q in [3, 7, 101, 1009, 10007, 100003]:
        if not is_prime(q): continue
        T = q * Tp; H = q * (hp + 2)
        DT = {abs(d) for d in S_single(T, H) if abs(d) < nT(H, T)}
        ok = all(q * a in DT for a in Dp)
        row.append((q, len(DT), ok))
    print("T'", Tp, "h'", hp, "k'", len(Dp), "bound K %.0f" % K, row)
