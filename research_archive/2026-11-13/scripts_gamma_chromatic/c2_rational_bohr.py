# Theorem 2 example: beta in <eps^A, omg^Bk> with beta = 1 mod 10M, sigma1(beta) near 1,
# r = L(beta - 1) in R, M | r, |r| tiny.
import sys
sys.setrecursionlimit(10000)
from fractions import Fraction as F
from math import log, sqrt, isqrt
exec(open(__file__.replace('c2_rational_bohr.py', 'c1_lib.py')).read())

M = 21
mod = 10 * M
def red(x):  # reduce a + b phi in Z[1/11] modulo mod
    a, b = x
    def rq(q):
        assert all(q.denominator % p for p in (2, 3, 5, 7))
        return (q.numerator * pow(q.denominator, -1, mod)) % mod
    return (rq(a), rq(b))
def order(x):
    y = x; n = 1
    while red(y) != (1, 0):
        y = mul(y, x); n += 1
    return n
phi = (1 + sqrt(5)) / 2
s1 = lambda x: float(x[0]) + float(x[1]) * phi
oa = order(eps); ob = order(omg)
A = oa if oa % 2 == 0 else 2 * oa       # even power of eps: sigma1 > 0
print("orders mod", mod, ":", oa, ob)
e1 = pw(eps, A); w1 = pw(omg, ob)
l1, l2 = log(abs(s1(e1))), log(abs(s1(w1)))
print("sigma1 signs", s1(e1) > 0, s1(w1) > 0, "logs", l1, l2)
best = None
for y in range(1, 40):
    for x in range(-200, 201):
        t = x * l1 + y * l2
        if best is None or abs(t) < abs(best[0]):
            best = (t, x, y)
t, x, y = best
print("x, y, t =", x, y, t)
beta = mul(pw(e1, x), pw(w1, y))
if s1(beta) < 0:
    beta = (-beta[0], -beta[1])
r = r_of(beta)
q = 20 * r * r + 4 * r + 1
print("norm 1:", norm(beta) == 1, "square:", is_sq(q), "odd den:", r.denominator % 2 == 1)
print("M | r:", (r / M).denominator % 2 == 1 and all((r / M).denominator % p for p in (3, 7)))
print("r approx", float(r), "den = 5^a 11^b:", r.denominator)
