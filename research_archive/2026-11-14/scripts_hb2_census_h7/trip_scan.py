"""List Pythagorean triples with leg X = 6272 q', odd Y, L <= Hmax; classify Y mod 28."""
import math, sys
from collections import Counter
Hmax = int(sys.argv[1]); S = 6272
cnt = Counter(); first = {}
for qq in range(1, Hmax // S + 1):
    X = S * qq; v = (X // 2) ** 2
    for a in range(1, math.isqrt(v) + 1):
        if v % a == 0:
            b = v // a
            if a + b <= Hmax - 1 and (b - a) % 2:
                Y, L = b - a, a + b
                r = min(Y % 28, (-Y) % 28)
                cnt[r] += 1
                if r not in first or L < first[r][2]:
                    first[r] = (X, Y, L)
print("Hmax", Hmax, "triples by min(Y mod 28, -Y mod 28):", dict(sorted(cnt.items())))
print("smallest L per class:", dict(sorted(first.items())))
