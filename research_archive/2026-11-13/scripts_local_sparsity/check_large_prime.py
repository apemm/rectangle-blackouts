# Sanity check of Proposition 3 (splitting at a large prime) for relations with sum |c_d| <= r.
# For T with a prime p | T, p^3 > 5 r^2 h^2, every relation sum c_d d = 0 (sum|c_d| <= r) must satisfy
#   sum_{p !| d} c_d X_d = 0   with X_d = 10 d + T.
import sys, itertools
from math import gcd
from collections import defaultdict

def build(h):
    S = defaultdict(set)
    u = 2
    while u * u + 1 < h:
        for v in range(1, u):
            if (u - v) % 2 == 0 or gcd(u, v) != 1: continue
            L0 = u * u + v * v
            if L0 >= h: break
            d0 = u * v // 2; b0 = u * u - v * v
            g = 1
            while g * L0 < h:
                for sd in (g * d0, -g * d0):
                    for sb in (g * b0, -g * b0):
                        S[sb - 2 * sd].add(sd)
                g += 2
        u += 1
    return S

def largest_prime(n):
    n = abs(n); p = 2; best = 1
    while p * p <= n:
        while n % p == 0:
            best = p; n //= p
        p += 1
    return max(best, n) if n > 1 else best

def main(h, r):
    S = build(h)
    nT = 0; nrel = 0; nmixed = 0; bad = 0
    for T, s in S.items():
        if abs(T) >= h: continue
        p = largest_prime(T)
        if p ** 3 <= 5 * r * r * h * h: continue
        nT += 1
        ds = sorted(s)
        # all coefficient vectors with sum |c| <= r, supported on at most r elements
        for size in range(1, r + 1):
            for sub in itertools.combinations(ds, size):
                for cs in itertools.product(range(-r, r + 1), repeat=size):
                    if 0 in cs or sum(abs(c) for c in cs) > r: continue
                    if cs[0] < 0: continue
                    if sum(c * d for c, d in zip(cs, sub)) != 0: continue
                    nrel += 1
                    part = [(c, d) for c, d in zip(cs, sub) if d % p != 0]
                    if part and len(part) < size: nmixed += 1
                    if sum(c * (10 * d + T) for c, d in part) != 0:
                        bad += 1
    print(f"h={h} r={r}: offsets with a prime p^3 > 5 r^2 h^2: {nT}; relations found: {nrel}; "
          f"relations mixing p|d and p!|d: {nmixed}; violations of Proposition 3: {bad}")

main(int(sys.argv[1]), int(sys.argv[2]))
