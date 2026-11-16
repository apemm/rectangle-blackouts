import math, sys, time
from math import gcd, isqrt
t0 = time.time()
B = int(sys.argv[1]); v2min = int(sys.argv[2])
def v2(n):
    n = abs(n); c = 0
    while n % 2 == 0: n //= 2; c += 1
    return c
R = set()
for p in range(-B, B + 1):
    for q in range(1, B + 1):
        if p == 0 or gcd(p, q) != 1 or (p*q) % 2: continue
        if v2(p*q) - 1 < v2min: continue
        N = p*p - p*q - q*q
        a, b = p*q, 2*N
        g = gcd(a, b); a //= g; b //= g
        if b < 0: a, b = -a, -b
        R.add((a, b)); R.add((-a, b))
R = sorted(R, key=lambda t: abs(t[0]/t[1]))
def issq(n):
    return n >= 0 and isqrt(n)**2 == n
def inR(a, b):   # a/b in +-R_odd  (b>0, b odd required)
    if b % 2 == 0 or a == 0: return False
    return issq(20*a*a + 4*a*b + b*b) or issq(20*a*a - 4*a*b + b*b)
L = list(R); found = 0; ex = []
for i in range(len(L)):
    a1, b1 = L[i]
    for j in range(i + 1, len(L)):
        a2, b2 = L[j]
        a = a1*b2 - a2*b1; b = b1*b2
        g = gcd(a, b);
        if g == 0: continue
        a //= g; b //= g
        if inR(a, b):
            found += 1
            if len(ex) < 5: ex.append(((a1, b1), (a2, b2), (a, b)))
    if time.time() - t0 > 50: print("time cut at i =", i); break
print(f"B={B} v2min={v2min} |R box|={len(L)} triangles(0,r1,r2) found={found} examples={ex} t={time.time()-t0:.1f}")
