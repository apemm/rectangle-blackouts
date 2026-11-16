"""Structure of tau=0 integral triangles at vertex 0: primitive count and sample families."""
import sys, math
from collections import Counter
import numpy as np
from tri_count import pyth_set

def triangles(h):
    P = pyth_set(h)
    Xmax = int(P[:, 0].max()) + 1
    keys = np.sort((P[:, 0] + 2 * Xmax) * (4 * h) + (P[:, 1] + 2 * h))
    out = []
    for (X1, y1) in P:
        if X1 <= 0:
            continue
        X3 = P[:, 0] - X1; y3 = P[:, 1] - y1
        ok = (X3 != 0) & (y3 != 0) & (np.abs(y3) < h) & ((X1 * P[:, 1] - P[:, 0] * y1) != 0)
        idx = np.nonzero(ok)[0]
        k3 = (X3[idx] + 2 * Xmax) * (4 * h) + (y3[idx] + 2 * h)
        pos = np.minimum(np.searchsorted(keys, k3), keys.size - 1)
        for i in idx[keys[pos] == k3]:
            out.append((int(X1), int(y1), int(P[i, 0]), int(P[i, 1])))
    return out

if __name__ == "__main__":
    for h in [int(s) for s in sys.argv[1:]]:
        T = triangles(h)
        prim = [t for t in T if math.gcd(math.gcd(t[0], t[1]), math.gcd(t[2], t[3])) == 1]
        print(f"h={h} total(X1>0)={len(T)} primitive={len(prim)}")
        # isosceles / special shapes
        def L(x, y): return math.isqrt(x * x + y * y)
        shapes = Counter()
        for (a, b, c, d) in prim:
            l1, l2, l3 = L(a, b), L(c, d), L(c - a, d - b)
            s = sorted([l1, l2, l3])
            iso = (l1 == l2) or (l1 == l3) or (l2 == l3)
            right = s[0] ** 2 + s[1] ** 2 == s[2] ** 2
            shapes[(iso, right)] += 1
        print("  (isosceles, right) among primitive:", dict(shapes))
        # vertical extent of primitive
        E = Counter()
        for (a, b, c, d) in prim:
            e = max(abs(b), abs(d), abs(d - b)); E[int(math.log2(e))] += 1
        print("  primitive by log2(vertical extent):", dict(sorted(E.items())))
        for t in prim[:8]:
            print("   sample", t)
