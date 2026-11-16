# Sanity check of Lemma K (congruence) and the (T,a) <-> solution map.
# For delta != 0, T != 0, a*b = T^2 + delta^2, U = T + (a+b)/2 integer,
# m = -T*U/delta integer: check delta1(delta/gcd(T,delta)) divides a+T and b+T,
# where delta1(n) = prod p^ceil(e/2); and check (E1)-(E3) of Theorem A.
import math, random, sys

def factor(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1 if d == 2 else 2
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def delta1(n):
    r = 1
    for p, e in factor(n).items(): r *= p ** ((e + 1) // 2)
    return r

def divisors(n):
    ds = [1]
    for p, e in factor(n).items():
        ds = [d * p**k for d in ds for k in range(e + 1)]
    return ds

random.seed(1)
checked = 0; fails = 0; sols = 0
for delta in list(range(2, 400, 2)) + [196, 392, 784, 1568, 2744, 5488]:
    for _ in range(60):
        T = 2 * random.randint(1, 3000) * random.choice([1, -1])
        n = T * T + delta * delta
        for d in divisors(n):
            for a in (d, -d):
                b = n // a
                if (a + b) % 2: continue
                U = T + (a + b) // 2
                if U == 0 or (T * U) % delta: continue
                m = -(T * U) // delta
                sols += 1
                g = math.gcd(T, delta); d1 = delta1(delta // g)
                ok = (a + T) % d1 == 0 and (b + T) % d1 == 0
                ok &= (a + T) * (b + T) == delta * delta + 2 * T * U
                X2 = 2 * T + a                      # 2X = 2T + a
                V = U + T - X2                      # V = U + T - 2X
                N = delta * (2 * m - delta)
                ok &= V * V - U * U == N and T * U == -m * delta and X2 == U + T - V
                checked += 1; fails += (not ok)
print("solutions checked:", checked, "failures:", fails)
