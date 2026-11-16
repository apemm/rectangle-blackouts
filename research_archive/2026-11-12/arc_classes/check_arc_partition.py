"""Independent check of an arc-class certificate.

It rebuilds every class from (s, a, q, M) only, ignores the stored blocked
differences, and tests from the definition:
  1. every label (i, j), 0 <= i < A, 0 <= j < K, lies in exactly one class,
  2. in each class i is distinct and j is nondecreasing in i with j' - j <= i' - i,
  3. no two labels (i, j), (i', j') of a class have
     16 (i - i')^2 + (2 (j - i') + 1)^2 = L^2 with 0 < L < h, in either order.

Usage:  py check_arc_partition.py cert.json
"""
import json
import sys
import numpy as np


def is_square_below(v, h):
    r = np.sqrt(v.astype(np.float64)).round().astype(np.int64)
    return (r * r == v) & (r > 0) & (r < h)


def main():
    cert = json.load(open(sys.argv[1]))
    h = cert["h"]
    A, K = (h + 1) // 2, h // 2
    seen = np.zeros((A, K), dtype=np.int32)
    nclasses = 0
    pairs = 0
    bad = 0
    for row in cert["classes"]:
        s, a, q, M = row["s"], row["a"], row["q"], row["M"]
        lo, hi = max(0, -s), min(A, K - s)
        slots = np.arange(lo, hi, dtype=np.int64)
        if a == -1:
            raise SystemExit("greedy fallback class present: not supported by this checker")
        arc = ((a * slots) % q) * M // q if q > 1 else np.zeros(len(slots), dtype=np.int64)
        for c in range(M):
            I = slots[arc == c]
            nclasses += 1
            if len(I) == 0:
                continue
            J = I + s
            seen[I, J] += 1
            if len(I) > 1:
                di = np.diff(I)
                dj = np.diff(J)
                if not (np.all(di > 0) and np.all(dj >= 0) and np.all(dj <= di)):
                    bad += 1
                # P test in both orders: odd point of slot i' against even point of (i, j)
                dI = I[:, None] - I[None, :]                 # i - i'
                e = 2 * (J[:, None] - I[None, :]) + 1         # 2 (j - i') + 1
                v = 16 * dI * dI + e * e
                hit = is_square_below(v, h)
                np.fill_diagonal(hit, False)
                pairs += len(I) * (len(I) - 1)
                bad += int(hit.sum())
    cover_ok = bool(np.all(seen == 1))
    print("h=%d classes=%d ordered pairs tested=%d  coverage exact=%s  violations=%d"
          % (h, nclasses, pairs, cover_ok, bad))
    if not cover_ok or bad:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
