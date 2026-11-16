# Sanity checks for the linearization r = L(beta - 1), L(a + b phi) = (a + 3b)/10.
# Elements of K = Q(sqrt5) are pairs (a, b) = a + b*phi, phi^2 = phi + 1.
from fractions import Fraction as F
from math import isqrt, gcd

def mul(x, y):
    a, b = x; c, d = y
    return (a*c + b*d, a*d + b*c + b*d)
def conj(x):
    a, b = x
    return (a + b, -b)
def norm(x):
    a, b = x
    return a*a + a*b - b*b
def inv(x):
    n = norm(x); c = conj(x)
    return (c[0]/n, c[1]/n)
def pw(x, n):
    r = (F(1), F(0))
    base = x if n >= 0 else inv(x)
    for _ in range(abs(n)):
        r = mul(r, base)
    return r
def L(x):
    return (x[0] + 3*x[1]) / 10
def r_of(beta):
    return L((beta[0] - 1, beta[1]))
def is_sq(q):
    if q < 0: return False
    n, d = q.numerator, q.denominator
    return isqrt(n)**2 == n and isqrt(d)**2 == d
def odd_den(q):
    return q.denominator % 2 == 1
def mod2_ok(beta):
    # beta = 1 or phi mod 2 (beta is a 2-adic unit, a, b in Z_(2))
    a, b = beta
    def m2(q):  # residue mod 2 of q in Z_(2)
        assert q.denominator % 2 == 1
        return (q.numerator * q.denominator) % 2
    return (m2(a), m2(b)) in [(1, 0), (0, 1)]

eps = (F(-1), F(-1))
omg = (F(10, 11), F(7, 11))
assert norm(eps) == 1 and norm(omg) == 1

# (1) every beta = +-eps^n omg^k gives r with 20r^2+4r+1 a square; odd denominator iff mod-2 condition
bad = 0; cnt = 0; rset = set()
for s in (1, -1):
    for n in range(-10, 11):
        for k in range(-3, 4):
            beta = mul((F(s), F(0)), mul(pw(eps, n), pw(omg, k)))
            r = r_of(beta)
            if r == 0:
                continue
            cnt += 1
            if not is_sq(20*r*r + 4*r + 1): bad += 1
            if odd_den(r) != mod2_ok(beta): bad += 1
            # denominator only 2,5,11
            d = r.denominator
            for p in (2, 5, 11):
                while d % p == 0: d //= p
            if d != 1: bad += 1
            rset.add(r)
print("check1: elements", cnt, "failures", bad)

# (2) compare with brute force D_T for T = 5*11^k: d with Q(T,d) square, |d| < B
for T in (5, 55, 605, 6655):
    B = 4000
    brute = set()
    for d in range(-B, B + 1):
        if d == 0: continue
        q = 20*d*d + 4*T*d + T*T
        if isqrt(q)**2 == q: brute.add(F(d, T))
    # from beta enumeration: r = d/T with T*r integer, |T r| <= B, odd den
    lin = set()
    for s in (1, -1):
        for n in range(-25, 26):
            for k in range(-4, 5):
                beta = mul((F(s), F(0)), mul(pw(eps, n), pw(omg, k)))
                r = r_of(beta)
                if r != 0 and (r * T).denominator == 1 and abs(r * T) <= B:
                    lin.add(r)
    print("T", T, "brute", len(brute), "lin", len(lin), "equal", brute == lin)
