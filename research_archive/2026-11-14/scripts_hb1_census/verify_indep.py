"""Low-memory adaptation of the archive's verify_hilbert_choice_certificate.py:
Euclid enumeration of integer right triangles (not divisor enumeration),
full scan of every rank pair at every relevant rank gap, final choices
applied directly.  Chunked int32 arithmetic."""
import math
import sys
import time
import numpy as np
from pgraph import d2xy


def verify(path, dlo=1, dhi=10**9):
    z = np.load(path)
    h, S, M = map(int, z["meta"])
    xi = z["xi"].astype(np.int32)
    A, K = (h + 1) // 2, h // 2
    q = 1 << (max(A, K) - 1).bit_length()
    n = q * q
    odd = np.empty(n, np.int32); even = np.empty(n, np.int32)
    for c0 in range(0, n, 1 << 21):
        t = np.arange(c0, min(n, c0 + (1 << 21)), dtype=np.int64)
        x, y = d2xy(q, t)
        assert (x < A).all() and (y < K).all()  # h a power of two: no padding
        odd[t] = 2 * x + 1; even[t] = 2 * y + 2
    max_gap = ((h - 1) // S + M - 1) // M
    rows = M * max_gap + M + 1
    width = 2 * q + 2
    table = np.zeros(rows * width, np.int32)
    triples = 0
    for a in range(2, math.isqrt(h - 1) + 1):
        for b in range(1, a):
            L0 = a * a + b * b
            if L0 >= h or (a - b) % 2 == 0 or math.gcd(a, b) != 1:
                continue
            X0, Y0 = 2 * a * b, a * a - b * b
            for t in range(1, (h - 1) // L0 + 1, 2):
                X, Y, L = t * X0, t * Y0, t * L0
                if X % S == 0 and X // S < rows:
                    table[(X // S) * width + Y] = L
                    triples += 1
    live = np.zeros(rows, bool)
    live[np.nonzero(table.reshape(rows, width).any(axis=1))[0]] = True
    checked = 0
    for d in range(max(1, dlo), min(max_gap, dhi) + 1):
        if not live[max(0, M * (d - 1) + 1):min(rows, M * (d + 1))].any():
            continue
        for c0 in range(0, n - d, 1 << 22):
            c1 = min(n - d, c0 + (1 << 22))
            g = M * d + xi[c0 + d:c1 + d] - xi[c0:c1]
            assert int(g.min()) >= d
            for r1, r2 in ((odd[c0:c1], even[c0 + d:c1 + d]), (even[c0:c1], odd[c0 + d:c1 + d])):
                L = table[g * width + np.abs(r1 - r2)]
                tot = r1 + r2
                bad = (L > 0) & (tot - L >= 2) & (tot + L <= 2 * h)
                assert not bad.any(), (d, c0 + int(np.nonzero(bad)[0][0]))
            checked += 2 * (c1 - c0)
    return {"h": h, "S": S, "M": M, "d_range": [dlo, min(max_gap, dhi)], "max_gap": max_gap, "status": "PASS", "euclid_triples": triples,
            "pairs_checked_all_gaps_scanned_with_live_rows": checked}


if __name__ == "__main__":
    t = time.time()
    print(verify(sys.argv[1], *map(int, sys.argv[2:4])), "sec", round(time.time() - t, 1))
