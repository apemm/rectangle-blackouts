# Sanity checks for the moment lemma.
# (1) discriminants of C(x,1)=4x^3-16x^2+13x+4 and V(x,1)=x^3-4x^2-3x+4.
# (2) multiplicities R(n) = #shapes with back-modulus n (p_lambda for R_IV, |U'| for R_FF), vs tau(n).
# (3) empirical factorial moments E[C(b,k)] of the back-degree b(x) = #{shapes: m_s | x} over odd x <= X,
#     and the tail P(b >= D).
from math import gcd, comb
from collections import Counter

def disc3(a, b, c, d):
    return 18*a*b*c*d - 4*b**3*d + b*b*c*c - 4*a*c**3 - 27*a*a*d*d
print("disc C(x,1) =", disc3(4, -16, 13, 4), " disc V(x,1) =", disc3(1, -4, -3, 4))

def v2(x):
    k = 0
    while x % 2 == 0: x //= 2; k += 1
    return k

X = 4_000_000
# R_IV^(4) back-moduli p_lambda
piv = []
be = 3
while be**3 // 5 <= X:
    for al in range(1, be, 2):
        if gcd(al, be) != 1 or v2(be - al) < 2: continue
        F = 4*(al - 2*be)**2 + be*be; g = gcd(F, be - al)
        p = (al*F + 4*(be - al)*be*be)//g
        if p <= X: piv.append(p)
    be += 2
# R_FF back-moduli |U'| over all coprime (a,b), b>0, 2b<a<4b (the d<0 range at stride 4), any parity
pff = []
b = 1
while 2*b**3 <= 40*X:
    for a in range(2*b+1, 4*b):
        if gcd(a, b) != 1: continue
        U = (a - 4*b)*(a*a + b*b); V = a**3 - 4*a*a*b - 3*a*b*b + 4*b**3
        g = gcd(U, V); U1 = abs(U//g)
        if U1 <= X: pff.append(U1)
    b += 1

def tau(n):
    t = 1; d = 2
    while d*d <= n:
        e = 0
        while n % d == 0: n //= d; e += 1
        t *= e + 1; d += 1
    if n > 1: t *= 2
    return t

for name, mods in (("R_IV p", piv), ("R_FF |U'|", pff)):
    R = Counter(mods)
    worst = max(R.items(), key=lambda kv: kv[1] / tau(kv[0])**2)
    print(name, ": moduli", len(mods), " distinct", len(R), " max R(n)", max(R.values()),
          " max R/tau^2 =", round(worst[1] / tau(worst[0])**2, 3), "at n =", worst[0])
    # back-degree over all integers x <= X (superset of any AP); count via sieve
    deg = bytearray(X + 1)
    for m in mods:
        for x in range(m, X + 1, m):
            if deg[x] < 255: deg[x] += 1
    cnt = Counter(deg[1:])
    tot = X
    mom = [sum(c * comb(dv, k) for dv, c in cnt.items()) / tot for k in (1, 2, 3, 4)]
    print("   E[C(b,k)], k=1..4:", [f"{v:.3g}" for v in mom])
    tail = {D: sum(c for dv, c in cnt.items() if dv >= D) / tot for D in (1, 2, 3, 4, 5, 6, 8)}
    print("   P(b >= D):", {D: f"{v:.3g}" for D, v in tail.items()}, " max b:", max(cnt))
