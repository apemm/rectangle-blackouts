from math import gcd, isqrt
from collections import defaultdict

def nT(h, T):
    A = (h + 1) // 2; K = h // 2; s = (T - 1) // 2
    return min(A, K - s) - max(0, -s)

def all_D(h):
    """D_T(h) for all odd |T| < h, via the (g,x,y) parametrization."""
    S = defaultdict(set)
    r0 = isqrt(h) + 2
    for y in range(1, r0):
        for x in range(-r0, r0):
            if x == 0 or gcd(abs(x), y) != 1: continue
            r = x * x + y * y
            if r >= h: continue
            N = y * y - x * y - x * x
            for g in range(1, (h - 1) // r + 1):
                if (g * x * y) % 2: continue
                T = g * N
                if T % 2 == 0 or abs(T) >= h: continue
                S[T].add(g * x * y // 2)
    D = {}
    for T in range(-(h - 1), h):
        if T % 2 == 0: continue
        n = nT(h, T)
        if n < 1: continue
        D[T] = sorted({abs(d) for d in S.get(T, ()) if abs(d) < n})
    return D
