"""All odd Y with (32 q)^2 + Y^2 a square, for given q (exact divisor enumeration)."""
import sys
from math import isqrt
def ys(q):
    X = 32 * q; h = X // 2; N = h * h; out = []
    s = 1
    while s * s < N:
        if N % s == 0:
            t = N // s
            if (t - s) % 2 == 1:
                Y = t - s
                L2 = X * X + Y * Y; L = isqrt(L2); assert L * L == L2
                out.append(Y)
        s += 1
    return sorted(out)
for q in map(int, sys.argv[1:]):
    v = ys(q)
    print(q, len(v), [y for y in v if 8000 <= y <= 9000], v[:30])
