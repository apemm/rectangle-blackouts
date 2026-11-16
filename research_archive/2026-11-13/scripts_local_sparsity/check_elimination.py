# Sanity check of the algebra behind Theorem A (local analysis at primes p || T and the
# elimination identity).  Elements of Z[phi] are pairs (a, b) = a + b*phi.
import sys, math
from math import gcd, isqrt
from collections import defaultdict

def mul(x, y):
    a, b = x; c, d = y
    return (a * c + b * d, a * d + b * c + b * d)
def conj(x):
    a, b = x
    return (a + b, -b)
def norm(x):
    a, b = x
    return a * a + a * b - b * b
def tr(x):
    a, b = x
    return 2 * a + b
def add(x, y): return (x[0] + y[0], x[1] + y[1])
def smul(c, x): return (c * x[0], c * x[1])
def divides(y, x):
    # is x / y in Z[phi] ?  returns quotient or None
    n = norm(y)
    z = mul(x, conj(y))
    if z[0] % n == 0 and z[1] % n == 0:
        return (z[0] // n, z[1] // n)
    return None
def val(pi, x):
    v = 0
    while True:
        q = divides(pi, x)
        if q is None: return v
        x = q; v += 1
def real(x):
    PHI = (1 + 5 ** 0.5) / 2
    return x[0] + x[1] * PHI

def find_pi(p):
    B = isqrt(p) + 2
    for a in range(0, 2 * B + 1):
        for b in range(-2 * B, 2 * B + 1):
            if abs(norm((a, b))) == p:
                return (a, b)
    return None

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

def beta(T, d):
    X = 10 * d + T
    L = isqrt(20 * d * d + 4 * T * d + T * T)
    assert L * L == 20 * d * d + 4 * T * d + T * T
    b = (X - L) // 2, L
    assert norm(b) == -T * T and tr(b) == X
    return b

def factor(n):
    f = {}; n = abs(n); p = 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1; n //= p
        p += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def main(h):
    S = build(h)
    nconf = nprim = 0
    prim_by_T = defaultdict(int)
    checked_elim = 0; maxtypes = 0
    signs = [(1, 1, -1), (1, -1, 1), (-1, 1, 1), (1, 1, 1)]   # up to global sign
    for T, s in S.items():
        if abs(T) >= h: continue
        sl = sorted(s)
        for e in signs:
            e0 = sum(e)
            for d1 in sl:
                for d2 in sl:
                    d3 = -(e[0] * d1 + e[1] * d2) * e[2]
                    if d3 not in s: continue
                    ds = (d1, d2, d3)
                    bs = [beta(T, d) for d in ds]
                    assert sum(e[j] * tr(bs[j]) for j in range(3)) == e0 * T
                    # reflection?
                    refl = any(e[j] * tr(bs[j]) == e0 * T for j in range(3))
                    if refl:
                        # must be minority sign element equal to -T/5
                        j0 = [j for j in range(3) if e[j] * tr(bs[j]) == e0 * T][0]
                        assert e0 in (1, -1) and e[j0] == -e0 and 5 * ds[j0] == -T
                        continue
                    nconf += 1
                    G = 0
                    for b in bs: G = gcd(G, gcd(b[0], b[1]))
                    if G != 1: continue
                    nprim += 1
                    prim_by_T[abs(T)] += 1
                    assert T % 5 != 0
                    f = factor(T)
                    types = defaultdict(list)
                    for p, a in f.items():
                        if a != 1: continue
                        assert p % 5 in (1, 4), (T, p)
                        pi = find_pi(p)
                        sig = tuple(val(pi, b) - 1 for b in bs)
                        sigc = tuple(val(conj(pi), b) - 1 for b in bs)
                        assert all(sig[j] == -sigc[j] and sig[j] in (-1, 0, 1) for j in range(3))
                        assert sum(1 for x in sig if x == 0) <= 1, (T, ds, p, sig)
                        if sig < sigc: sig, pi = sigc, conj(pi)   # representative = larger tuple
                        types[sig].append((p, pi))
                    maxtypes = max(maxtypes, len(types))
                    for sig, lst in types.items():
                        kappa = (1, 0); P = 1
                        for p, pi in lst:
                            kappa = mul(kappa, pi); P *= p
                        eta = 1 if norm(kappa) > 0 else -1
                        assert abs(norm(kappa)) == P
                        k2 = mul(kappa, kappa); k2c = conj(k2)
                        nus = []
                        for j in range(3):
                            if sig[j] == 1: q = divides(k2, bs[j])
                            elif sig[j] == -1: q = divides(k2c, bs[j])
                            else: q = divides((P, 0), bs[j])
                            assert q is not None
                            assert norm(q) == -(T // P) ** 2
                            nus.append(q)
                        m = abs(T) // P; sT = 1 if T > 0 else -1
                        Om = (0, 0); c = sT * e0 * m
                        for j in range(3):
                            if sig[j] == 1: Om = add(Om, smul(e[j], nus[j]))
                            elif sig[j] == -1: Om = add(Om, smul(e[j], conj(nus[j])))
                            else: c -= e[j] * tr(nus[j])
                        assert c != 0 and Om != (0, 0)
                        lhs = add(mul(Om, k2), mul(conj(Om), k2c))
                        rhs = smul(c * eta, mul(kappa, conj(kappa)))
                        assert lhs == rhs, (T, ds, e, sig)
                        assert tr(mul(k2, Om)) == c * P
                        checked_elim += 1
    # growth of primitive configurations
    xs = [h // 8, h // 4, h // 2, h]
    cum = {x: sum(v for t, v in prim_by_T.items() if t <= x) for x in xs}
    print(f"h={h}: nonreflection relations (4 sign classes)={nconf}, primitive={nprim}, "
          f"elimination identities checked={checked_elim}, max number of types in one configuration={maxtypes}")
    print("  primitive configurations with |T| <= x (L < h):", cum)

main(int(sys.argv[1]))
