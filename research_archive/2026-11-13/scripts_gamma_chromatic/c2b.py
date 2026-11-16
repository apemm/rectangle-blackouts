from fractions import Fraction as F
from math import log, sqrt
exec(open('c1_lib.py').read())
def fpw(x, n):
    base = x if n >= 0 else inv(x); n = abs(n); r = (F(1), F(0))
    while n:
        if n & 1: r = mul(r, base)
        base = mul(base, base); n >>= 1
    return r
phi = (1 + sqrt(5)) / 2
A, Bw = 120, 60      # orders mod 210 from c2_rational_bohr.py (120 even)
l1 = A * 4 * log(phi) / 2   # log sigma1(eps^A) = A*log(phi^2)
l2 = Bw * log((3 + phi) / (4 - phi))
best = min(((x * l1 + y * l2, x, y) for y in range(1, 300) for x in range(-1000, 1001)), key=lambda z: abs(z[0]))
t, x, y = best
print("x y t", x, y, t)
beta = mul(fpw(eps, A * x), fpw(omg, Bw * y))
r = r_of(beta)
print("norm1", norm(beta) == 1, "square", is_sq(20*r*r + 4*r + 1))
rm = r / 21
print("21 | r (den of r/21 coprime to 3,7, odd):", all(rm.denominator % p for p in (2, 3, 7)))
d = r.denominator
for p in (5, 11):
    while d % p == 0: d //= p
print("den only 5,11:", d == 1, " r ~", float(r), " predicted sqrt5*t/10 =", sqrt(5) * t / 10)
