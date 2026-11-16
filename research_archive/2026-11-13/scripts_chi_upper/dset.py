"""D_T^inf ∩ [1,X] (stride 4) via Theorem A: d = g x y / 2, g (y^2 - x y - x^2) = T,
gcd(x,y)=1, g x y even, y>=1, x != 0.  Also a brute-force check against the definition."""
from math import gcd, isqrt
import sys

def divisors(n):
    n = abs(n); ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i * i != n: ds.append(n // i)
        i += 1
    return sorted(ds)

def dset(T, X):
    """set of |d| in D_T^inf with |d| <= X; also returns L-values dict"""
    out = {}
    for g in divisors(T):
        N = T // g  # signed: y^2 - xy - x^2 = N
        xmax = 2 * X // g + 1
        for x in range(-xmax, xmax + 1):
            if x == 0: continue
            disc = 5 * x * x + 4 * N
            if disc < 0: continue
            s = isqrt(disc)
            if s * s != disc: continue
            for sg in (1, -1):
                num = x + sg * s
                if num % 2: continue
                y = num // 2
                if y < 1: continue
                if gcd(abs(x), y) != 1: continue
                if (g * x * y) % 2: continue
                d = g * x * y // 2
                if d == 0 or abs(d) > X: continue
                L = g * (x * x + y * y)
                a = abs(d)
                out[a] = min(out.get(a, 10**30), L)
    return out

def brute(T, X):
    s = {}
    for d in range(-X, X + 1):
        if d == 0: continue
        q = 20 * d * d + 4 * T * d + T * T
        r = isqrt(q)
        if r * r == q:
            s[abs(d)] = min(s.get(abs(d), 10**30), r)
    return s

if __name__ == "__main__":
    for T in [1, 5, 11, -11, 55, 209, 1045, 605, -1045]:
        a = dset(T, 3000); b = brute(T, 3000)
        print(T, len(a), set(a) == set(b))
