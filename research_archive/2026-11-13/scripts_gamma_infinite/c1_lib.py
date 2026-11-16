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
