"""Monotone P-free partition by arc classes on constant-offset diagonals.

For each offset index s (T = 2s + 1) the labels (i, i + s) are split into M
classes  {i : floor(M * ((a * i) mod q) / q) = c},  c = 0..M-1.  Two slots of
one class differ by an x with ((a x) mod q) in (-q/M, q/M).  The class is
P-free when every blocked difference d of the offset has
min(r, q - r) * M >= q,  r = (a d) mod q   (exact integer test).

Usage:  py arc_partition.py h out.json
"""
import json
import math
import sys
import numpy as np


def blocked_differences(h, s, n):
    T = 2 * s + 1
    d = np.arange(1 - n, n, dtype=np.int64)
    d = d[d != 0]
    v = 20 * d * d + 4 * T * d + T * T
    r = np.sqrt(v.astype(np.float64)).round().astype(np.int64)
    return np.unique(np.abs(d[(r * r == v) & (r < h)]))


def candidates(qmax=307, extra=20000, big=1000003, seed=7):
    out = []
    for q in range(2, qmax + 1):
        for a in range(1, q // 2 + 1):
            if math.gcd(a, q) == 1:
                out.append((a, q))
    rng = np.random.default_rng(seed)
    for a in rng.integers(1, big // 2, size=extra):
        out.append((int(a), big))
    return out


def main():
    h = int(sys.argv[1])
    A, K = (h + 1) // 2, h // 2
    cands = candidates()
    ca = np.array([c[0] for c in cands], dtype=np.int64)
    cq = np.array([c[1] for c in cands], dtype=np.int64)
    classes = []
    total = 0
    hist = {}
    for s in range(-(A - 1), K):
        lo, hi = max(0, -s), min(A, K - s)
        n = hi - lo
        if n <= 0:
            continue
        ds = blocked_differences(h, s, n) if n > 1 else np.zeros(0, dtype=np.int64)
        if len(ds) == 0:
            a, q, M = 0, 1, 1
        else:
            r = (ca[:, None] * ds[None, :]) % cq[:, None]
            m = np.minimum(r, cq[:, None] - r).min(axis=1)          # min_d of q*||a d / q||
            # least M with m * M >= q, i.e. M = ceil(q / m)
            with np.errstate(divide="ignore"):
                Ms = np.where(m > 0, -(-cq // np.maximum(m, 1)), 10 ** 9)
            k = int(Ms.argmin())
            a, q, M = int(ca[k]), int(cq[k]), int(Ms[k])
            if M > len(ds) + 1:                                   # fall back to a greedy proper coloring
                a, q, M = -1, 0, len(ds) + 1
        classes.append({"s": s, "a": a, "q": q, "M": M, "blocked": [int(x) for x in ds]})
        total += M
        hist[M] = hist.get(M, 0) + 1
    json.dump({"h": h, "classes": classes, "total": total}, open(sys.argv[2], "w"))
    print("h=%d  total classes=%d  = %.3f h   histogram=%s" % (h, total, total / h, dict(sorted(hist.items()))))


if __name__ == "__main__":
    main()
