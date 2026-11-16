"""Independent verification of fixed Hilbert local-choice certificates.

This does not import the search or its factorization code. It reconstructs
Hilbert coordinates by the standard low-bit rotation algorithm, enumerates
integer right triangles by Euclid's primitive parametrization, and checks
the final assignment directly at every potentially relevant rank gap.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import numpy as np


def coordinates(q):
    n = q * q
    t = np.arange(n, dtype=np.int64)
    x = np.zeros(n, dtype=np.int64)
    y = np.zeros(n, dtype=np.int64)
    s = 1
    while s < q:
        rx = (t // 2) & 1
        ry = (t ^ rx) & 1
        reflect = (ry == 0) & (rx == 1)
        x[reflect] = s - 1 - x[reflect]
        y[reflect] = s - 1 - y[reflect]
        swap = ry == 0
        saved = x[swap].copy()
        x[swap] = y[swap]
        y[swap] = saved
        x += s * rx
        y += s * ry
        t //= 4
        s *= 2
    return x, y


def verify(path):
    raw = path.read_bytes()
    data = json.loads(raw)
    h, S, M = data["h"], data["S"], data["choices"]
    A, K = (h + 1) // 2, h // 2
    q = 1 << (max(A, K) - 1).bit_length()
    n = q * q
    xi = np.zeros(n, dtype=np.int64)
    for r, value in data["nonzero_choices"].items():
        r = int(r)
        assert 0 <= r < n and 0 <= value < M
        xi[r] = value
    x, y = coordinates(q)
    active = (x < A) & (y < K)
    assert int(active.sum()) == data["labels"]
    odd, even = 2 * x + 1, 2 * y + 2
    max_gap = ((h - 1) // S + M - 1) // M
    table = np.zeros((M * max_gap + M + 1, 2 * q + 2), dtype=np.int64)
    triples = 0
    # A primitive integer right triangle with odd vertical leg has even
    # horizontal leg 2ab, odd vertical leg a^2-b^2, and odd hypotenuse.
    # Its scaling factor is odd. Euclid's conditions make this exhaustive.
    for a in range(2, math.isqrt(h - 1) + 1):
        for b in range(1, a):
            L0 = a * a + b * b
            if L0 >= h or (a - b) % 2 == 0 or math.gcd(a, b) != 1:
                continue
            X0, Y0 = 2 * a * b, a * a - b * b
            for t in range(1, (h - 1) // L0 + 1, 2):
                X, Y, L = t * X0, t * Y0, t * L0
                if X % S == 0:
                    table[X // S, Y] = L
                    triples += 1
    checked = 0
    failures = []
    for d in range(1, max_gap + 1):
        slot_gap = M * d + xi[d:] - xi[:-d]
        assert int(slot_gap.min()) >= d
        present = active[:-d] & active[d:]
        checked += 2 * int(present.sum())
        for rows1, rows2 in ((odd[:-d], even[d:]), (even[:-d], odd[d:])):
            L = table[slot_gap, np.abs(rows1 - rows2)]
            total = rows1 + rows2
            bad = present & (L > 0) & (total - L >= 2) & (total + L <= 2 * h)
            if np.any(bad):
                r = int(np.nonzero(bad)[0][0])
                failures.append({"r": r, "s": r + d,
                                 "X": int(S * slot_gap[r]),
                                 "rows": [int(rows1[r]), int(rows2[r])],
                                 "L": int(L[r])})
    assert not failures, failures
    return {"certificate": path.name, "sha256": hashlib.sha256(raw).hexdigest(),
            "h": h, "S": S, "M": M, "status": "PASS",
            "euclid_triples": triples, "tested_opposite_parity_pairs": checked,
            "maximum_rank_gap": max_gap}


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("certificates", nargs="+", type=Path)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    results = []
    for path in args.certificates:
        result = verify(path)
        results.append(result)
        print(json.dumps(result), flush=True)
    args.out.write_text(json.dumps(results, indent=2) + "\n")
