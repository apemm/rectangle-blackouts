# Sanity check of Proposition 3 on a case where mixed relations exist: T = p prime, h = 10^8,
# p ~ h/20 > (5 r^2 h^2)^(1/3) with r = 13.  S_p(h) is generated from the orbits in Z[phi].
import sys, itertools
from math import isqrt

def mul(x, y):
    a, b = x; c, d = y
    return (a * c + b * d, a * d + b * c + b * d)
def conj(x): return (x[0] + x[1], -x[1])
def norm(x): return x[0] * x[0] + x[0] * x[1] - x[1] * x[1]
def tr(x): return 2 * x[0] + x[1]

def is_prime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

def find_pi(p):
    for b in range(0, 3 * isqrt(p) + 3):
        for sgn in (1, -1):
            D = 5 * b * b + 4 * sgn * p
            if D < 0: continue
            s = isqrt(D)
            if s * s == D and (s - b) % 2 == 0:
                a = (s - b) // 2
                if abs(norm((a, b))) == p: return (a, b)
    return None

def S_of_prime(p, h):
    pi = find_pi(p)
    phi = (0, 1); phinv = (-1, 1)          # 1/phi = phi - 1
    out = set()
    for base in (mul(pi, pi), mul(conj(pi), conj(pi)), (p, 0)):
        for unit in (phi, phinv):
            x = base
            for _ in range(200):
                for sg in (1, -1):
                    y = (sg * x[0], sg * x[1])
                    if norm(y) == -p * p and (tr(y) - p) % 10 == 0:
                        d = (tr(y) - p) // 10
                        L2 = 20 * d * d + 4 * p * d + p * p
                        L = isqrt(L2)
                        if L * L == L2 and 0 < L < h and d != 0:
                            out.add(d)
                x = mul(x, unit)
                if abs(x[0]) > 10 ** 40: break
    return sorted(out)

def main():
    h = 10 ** 8; r = 13
    lo = int((5 * r * r * h * h) ** (1 / 3)) + 1
    found = 0; tested = 0; mixed = 0; bad = 0; examples = []
    p = h // 20
    while tested < 40:
        p += 1
        if p % 5 not in (1, 4) or not is_prime(p): continue
        assert p ** 3 > 5 * r * r * h * h
        ds = S_of_prime(p, h)
        tested += 1
        X = {d: 10 * d + p for d in ds}
        for size in (2, 3, 4):
            for sub in itertools.combinations(ds, size):
                rng = range(-8, 9)
                for cs in itertools.product(rng, repeat=size - 1):
                    if 0 in cs: continue
                    part = sum(c * d for c, d in zip(cs, sub))
                    last = sub[-1]
                    if part % last != 0: continue
                    c_last = -part // last
                    if c_last == 0: continue
                    full = cs + (c_last,)
                    if sum(abs(c) for c in full) > r: continue
                    found += 1
                    prim = [(c, d) for c, d in zip(full, sub) if d % p != 0]
                    if 0 < len(prim) < size:
                        mixed += 1
                        if len(examples) < 3: examples.append((p, sub, full))
                    if sum(c * X[d] for c, d in prim) != 0: bad += 1
    print(f"h={h}, r={r}, primes tested={tested} (first above h/20, all > {lo});")
    print(f"relations with support <= 4 and sum|c| <= {r}: {found}; mixed (some p|d, some not): {mixed}; "
          f"violations of Proposition 3(a): {bad}")
    for e in examples: print("  example:", e)

main()
