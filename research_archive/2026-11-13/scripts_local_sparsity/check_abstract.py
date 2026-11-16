# Sanity check of Proposition 4.8 in the abstract setting: count ALL primitive configurations
#   (T; beta_1, beta_2, beta_3; e),  N(beta_j) = -T^2,  sum e_j Tr(beta_j) = e_0 T,  e_j Tr(beta_j) != e_0 T,
# with T odd, 0 < T <= x (T > 0 only; T < 0 is symmetric), |beta_j|, |beta_j'| <= sqrt(5) x.
# Also checks Lemma 4.3 (5 does not divide T; every prime p || T splits; at most one zero pattern).
import sys
from math import isqrt, gcd
from collections import defaultdict

SQ5 = 5 ** 0.5

def norm(x): return x[0] * x[0] + x[0] * x[1] - x[1] * x[1]
def conj(x): return (x[0] + x[1], -x[1])
def mul(x, y):
    a, b = x; c, d = y
    return (a * c + b * d, a * d + b * c + b * d)
def divides(y, x):
    n = norm(y); z = mul(x, conj(y))
    return z[0] % n == 0 and z[1] % n == 0
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
def vals(pi, x):
    v = 0
    while divides(pi, x):
        n = norm(pi); z = mul(x, conj(pi)); x = (z[0] // n, z[1] // n); v += 1
    return v
def factor(n):
    f = {}; p = 2
    while p * p <= n:
        while n % p == 0: f[p] = f.get(p, 0) + 1; n //= p
        p += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def main(x):
    Y = SQ5 * x
    signs = [(1, 1, -1), (1, -1, 1), (-1, 1, 1), (1, 1, 1)]
    prim_by_T = defaultdict(int); total = 0; lemma_checks = 0
    for T in range(1, x + 1, 2):
        # all beta = (X + L sqrt5)/2 with X^2 - 5 L^2 = -4 T^2, both conjugates bounded by Y
        B = []
        for L in range(1, 2 * x + 1):
            X2 = 5 * L * L - 4 * T * T
            if X2 < 0: continue
            X = isqrt(X2)
            if X * X != X2: continue
            for sx in ((X, -X) if X else (0,)):
                for sl in (L, -L):
                    if abs(sx + sl * SQ5) / 2 <= Y and abs(sx - sl * SQ5) / 2 <= Y:
                        B.append(((sx - sl) // 2, sl))        # a + b phi with b = sl, a = (X - L)/2
        byX = defaultdict(list)
        for b in B:
            assert norm(b) == -T * T
            byX[2 * b[0] + b[1]].append(b)
        for e in signs:
            e0 = sum(e)
            for b1 in B:
                x1 = 2 * b1[0] + b1[1]
                if e[0] * x1 == e0 * T: continue
                for b2 in B:
                    x2 = 2 * b2[0] + b2[1]
                    if e[1] * x2 == e0 * T: continue
                    x3 = (e0 * T - e[0] * x1 - e[1] * x2) * e[2]
                    if e[2] * x3 == e0 * T: continue
                    for b3 in byX.get(x3, ()):
                        total += 1
                        g = 0
                        for b in (b1, b2, b3): g = gcd(g, gcd(b[0], b[1]))
                        if g != 1: continue
                        prim_by_T[T] += 1
                        assert T % 5 != 0
                        for p, a in factor(T).items():
                            if a != 1: continue
                            assert p % 5 in (1, 4)
                            pi = find_pi(p)
                            sig = [vals(pi, b) - 1 for b in (b1, b2, b3)]
                            sigc = [vals(conj(pi), b) - 1 for b in (b1, b2, b3)]
                            assert all(s + sc == 0 for s, sc in zip(sig, sigc))
                            assert sig.count(0) <= 1
                            lemma_checks += 1
    xs = [x // 8, x // 4, x // 2, x]
    print(f"x={x}: configurations (T>0, 4 sign classes, sizes <= sqrt5*x): {total}; primitive: {sum(prim_by_T.values())}; "
          f"prime checks of Lemma 4.3: {lemma_checks}")
    print("  primitive configurations with T <= y (same size bound sqrt5*x):",
          {y: sum(v for t, v in prim_by_T.items() if t <= y) for y in xs})

main(int(sys.argv[1]))
