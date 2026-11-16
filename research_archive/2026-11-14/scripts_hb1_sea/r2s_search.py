"""Search R2-same solutions from the parametrization
   A=(0,y), B=(u,s), C=(X,y+delta), D=(X+v,s), P=u-v,
   N=delta(2m-delta), m=s-y, u=(P^2-N)/(2P), t=-m delta/u, X=(P+t)/2,
and check them against the defining equations and sea-type rules
(columns: label columns = 0 mod 28, so X = 0 mod 28; sea type by chi_7).
Toy rows as in toy_roles.py (mixed block): odd label rows 17 mod 28,
even label rows 8 mod 28, L=3, F=55, H=410, h=420.
"""
import math
h = 420; L, F, H = 3, 55, 410
QR = {1, 2, 4}
def sea(x):
    r = x % 7
    return F if r == 0 else (H if r in QR else L)
def divisors(n):
    n = abs(n); out = []
    for d in range(1, math.isqrt(n) + 1):
        if n % d == 0:
            out += [d, n // d]
    return set(out)
sols = []
for par, res in (('O', 17), ('E', 8)):
    rows = [y for y in range(60, 400) if y % 28 == res]
    for y in rows:
        for s in (L, F, H):
            m = s - y
            for y2 in rows:
                delta = y2 - y
                if delta == 0: continue
                N = delta * (2 * m - delta)
                for P0 in divisors(N):
                    for P in (P0, -P0):
                        if (P * P - N) % (2 * P): continue
                        u = (P * P - N) // (2 * P)
                        if u == 0 or (m * delta) % u: continue
                        t = -(m * delta) // u
                        if (P + t) % 2: continue
                        X = (P + t) // 2
                        if X == 0 or X % 28: continue
                        v = u - P
                        A = (0, y); B = (u, s); C = (X, y2); D = (X + v, s)
                        U = (u, m); V = (v, s - y2)
                        assert U[0]**2 + U[1]**2 == V[0]**2 + V[1]**2
                        Tx2, Ty2 = C[0]+D[0]-A[0]-B[0], C[1]+D[1]-A[1]-B[1]
                        assert U[0]*Tx2 + U[1]*Ty2 == 0
                        if Tx2 % 2 or Ty2 % 2: continue
                        p = (A[0]+Tx2//2, A[1]+Ty2//2); q = (B[0]+Tx2//2, B[1]+Ty2//2)
                        if not (1 <= p[1] <= h and 1 <= q[1] <= h): continue
                        if V == U or V == (-U[0], -U[1]): continue
                        ok_sea = (u % 28 != 0 and sea(u) == s and (X + v) % 28 != 0 and sea(X + v) == s)
                        sols.append((par, s, y, y2, X, u, v, ok_sea))
print('total algebraic solutions with X=0 mod 28 in strip:', len(sols))
good = [z for z in sols if z[-1]]
print('with both sea points of the right type:', len(good))
for z in good[:15]:
    print(z)
from collections import Counter
print(Counter((z[0], z[1]) for z in good))
print('max |X|', max((abs(z[4]) for z in good), default=None))
