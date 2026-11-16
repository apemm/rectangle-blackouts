from riv import lambdas
from math import gcd
L = lambdas(10**7, 3)
print(len(L))
def leg(a, l):
    a %= l
    if a == 0: return 0
    return 1 if pow(a, (l-1)//2, l) == 1 else -1
def factor(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
res = {}
for l in [3,5,7,11,13,17,19,23,29,31,37,41,43,47]:
    vals = set()
    for (a,b,q,p) in L:
        vals.add(leg(p*q, l))
    res[l] = vals
print('Legendre (pq/l) value sets:', res)
# Liouville
vals = set()
for (a,b,q,p) in L[:400]:
    vals.add((sum(factor(p).values()) + sum(factor(q).values())) % 2)
print('Omega(p)+Omega(q) parities:', vals)
# p - q, p/q mod small
print(sorted(L, key=lambda t: t[3])[:10])
