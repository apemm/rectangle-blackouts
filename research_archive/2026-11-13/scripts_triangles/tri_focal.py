"""For a few focal vectors w in P, list z with z, z - w in P (|y|<h), and classify."""
import sys, math
from collections import Counter
import numpy as np
from tri_count import pyth_set

h = int(sys.argv[1])
P = pyth_set(h)
S = set(map(tuple, P.tolist()))
rng = np.random.default_rng(1)
cnt = []
for trial in range(12):
    X1, y1 = P[rng.integers(len(P))]
    X1, y1 = int(X1), int(y1)
    d = math.isqrt(X1 * X1 + y1 * y1)
    sols = []
    for (X, y) in P.tolist():
        X3, y3 = X - X1, y - y1
        if X3 == 0 or y3 == 0 or abs(y3) >= h or X1 * y - X * y1 == 0:
            continue
        if (X3, y3) in S:
            sols.append((X, y))
    ks = Counter()
    par = 0
    for (X, y) in sols:
        r = math.isqrt(X * X + y * y); s = math.isqrt((X - X1) ** 2 + (y - y1) ** 2)
        ks[r - s] += 1
    g = math.gcd(X1, y1)
    print(f"w=({X1},{y1}) |w|={d} gcd={g} #sols={len(sols)} distinct k={len(ks)} top k={ks.most_common(4)}")
    cnt.append(len(sols))
print("mean", np.mean(cnt), "h/Lambda^2", h / math.log(h) ** 2)
