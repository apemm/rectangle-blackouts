# Integral distances between same-parity label points of different classes (rigid layouts),
# numpy version so that h is large enough for blocks to interact (stride*p < h^2).
import numpy as np, sys
from dichotomy_check import layout
h = int(sys.argv[1])
for stride in (4, 8, 12):
    pts, p = layout(h, stride, 1, 0, h - 2)
    out = {}
    for par in (0, 1):
        P = np.array([(q[0], q[1], q[3]) for q in pts if q[4] == par], dtype=np.int64)
        x, y, c = P[:, 0], P[:, 1], P[:, 2]
        hits = 0
        for k in range(len(P)):
            X = x[k + 1:] - x[k]; D = y[k + 1:] - y[k]
            m = (np.abs(X) <= h * h) & (D != 0) & (c[k + 1:] != c[k])
            if not m.any(): continue
            n = X[m] ** 2 + D[m] ** 2
            r = np.round(np.sqrt(n.astype(np.float64))).astype(np.int64)
            hits += int(((r * r == n) | ((r + 1) ** 2 == n) | ((r - 1) ** 2 == n)).sum())
        out["EE" if par == 0 else "OO"] = hits
    print(f"h={h} stride={stride} p={p} cross-class same-parity integral-distance pairs: {out}")
