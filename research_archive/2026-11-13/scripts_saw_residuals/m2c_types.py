"""M2c with B an odd label point and D a SAW filler (block_sea Theorem 2 equation), recording the filler offset a,
v2(k) with k = e u2 / n1, and v2(Delta). Prediction (2-adic lemma): only holes, (a = 2, v2 k = 1, v2 Delta = 3)
or (a = 0, k odd, v2 Delta = 4). Usage: py m2c_types.py h1,h2,..."""
import sys
from math import isqrt
from collections import Counter
OFF = (-3, -2, -1, 0)
def v2(x):
    x = abs(x); c = 0
    while x % 2 == 0: x //= 2; c += 1
    return c
def divisors(n):
    n = abs(n); out = []; d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n: out.append(n // d)
        d += 1
    return out
for h in [int(a) for a in sys.argv[1].split(',')]:
    typ = Counter(); bad = Counter()
    for iota in (1, 3, 5, 9):
        r1 = (2 * iota + 1) % 16
        T = max(y for y in range(1, h + 1) if y % 16 == r1)
        rows = [T + 8 * o for o in OFF]
        for i in range(1, (h + 1) // 2):
            if i % 16 != iota: continue
            yB = 2 * i + 1
            if yB >= min(rows) - 80: continue
            u2 = yB - 1; hit = False
            for a, yD in enumerate(rows):
                e = (yD - yB) // 2
                N = e * u2
                for dd in divisors(N):
                    for n1 in (dd, -dd):
                        k = N // n1; z = -k
                        if z % 4 == 0 or (2 * n1 - z) % 4 == 0: continue
                        A_ = n1; B_ = -(2 * n1 * n1 + N); C_ = n1 ** 3 + n1 * e * e + 2 * N * n1
                        disc = B_ * B_ - 4 * A_ * C_
                        if disc < 0: continue
                        s = isqrt(disc)
                        if s * s != disc: continue
                        for sg in (1, -1):
                            num = -B_ + sg * s
                            if num % (2 * A_): continue
                            Dl = num // (2 * A_)
                            if Dl % 4 or (Dl // 4) % 4 != a: continue
                            typ[(a, v2(k), v2(Dl), v2(e))] += 1; hit = True
            if hit: bad[iota] += 1
    print('h', h, 'types (offset a, v2 k, v2 Delta, v2 e):', dict(typ), 'bad odd rows per iota:', dict(bad))
