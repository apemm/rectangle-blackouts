"""Check arc certificates by exact, complete Pythagorean enumeration.

This checker uses Python integers, gcd, and isqrt. It does not use NumPy,
floating-point square roots, or the producer's stored forbidden-gap lists.
The optional stored gap lists are checked against independently rebuilt sets.

Usage: python check_arc_certificates_integer.py cert1.json ... --out results.json
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import time


def blocked_sets(h):
    """Return all absolute gaps for every actual nonempty label diagonal."""
    A, K = (h + 1) // 2, h // 2
    gaps = {s: set() for s in range(1 - A, K)}
    triangles = 0
    incidences = 0
    for p in range(2, math.isqrt(h - 1) + 1):
        for q in range(1, p):
            hyp = p * p + q * q
            if hyp >= h:
                break
            if (p - q) % 2 == 0 or math.gcd(p, q) != 1:
                continue
            for t in range(1, (h - 1) // hyp + 1, 2):
                triangles += 1
                gap = t * p * q // 2
                vertical = t * (p * p - q * q)
                for sd in (-1, 1):
                    d = sd * gap
                    for sv in (-1, 1):
                        T = sv * vertical - 2 * d
                        s = (T - 1) // 2
                        if s not in gaps:
                            continue
                        n = min(A, K - s) - max(0, -s)
                        if gap < n:
                            gaps[s].add(gap)
                            incidences += 1
    return gaps, {"odd_hypotenuse_triangles": triangles,
                  "admissible_signed_gap_incidences": incidences}


def direct_sets(h):
    """Slow, definition-based reference for small enumeration self-checks."""
    A, K = (h + 1) // 2, h // 2
    result = {}
    for s in range(1 - A, K):
        T = 2 * s + 1
        n = min(A, K - s) - max(0, -s)
        result[s] = set()
        for d in range(1 - n, n):
            if d == 0:
                continue
            value = 20 * d * d + 4 * T * d + T * T
            L = math.isqrt(value)
            if L * L == value and L < h:
                result[s].add(abs(d))
    return result


def check_certificate(path):
    start = time.perf_counter()
    raw = Path(path).read_bytes()
    cert = json.loads(raw)
    h = cert["h"]
    assert isinstance(h, int) and h >= 2
    gaps, stats = blocked_sets(h)
    rows = cert["classes"]
    by_s = {}
    total = 0
    slots = 0
    nonempty_classes = 0
    A, K = (h + 1) // 2, h // 2
    min_numerator = None
    for row in rows:
        s, a, q, M = (row[k] for k in ("s", "a", "q", "M"))
        assert all(isinstance(x, int) for x in (s, a, q, M))
        assert s in gaps and s not in by_s, (h, "duplicate/invalid diagonal", s)
        assert q > 0 and M > 0 and 0 <= a < q, (h, "non-arc certificate", s)
        by_s[s] = row
        if "blocked" in row:
            assert row["blocked"] == sorted(gaps[s]), (h, "stored gaps differ", s)
        for d in gaps[s]:
            r = a * d % q
            numerator = min(r, q - r) * M - q
            assert numerator >= 0, (h, "arc-separation failure", s, d, a, q, M)
            min_numerator = numerator if min_numerator is None else min(min_numerator, numerator)
        lo, hi = max(0, -s), min(A, K - s)
        slots += hi - lo
        # Count actual colors without storing labels or comparing pairs.
        nonempty_classes += len({((a * i) % q) * M // q for i in range(lo, hi)})
        total += M
    assert set(by_s) == set(gaps), (h, "missing diagonals")
    assert total == cert["total"], (h, "incorrect total")
    assert slots == A * K
    return {"certificate": str(Path(path).resolve()), "sha256": hashlib.sha256(raw).hexdigest(),
            "h": h, "status": "PASS", "declared_classes": total,
            "nonempty_classes": nonempty_classes, "labels": slots,
            "diagonals": len(gaps), "distinct_absolute_gaps": sum(map(len, gaps.values())),
            "smallest_arc_inequality_slack": min_numerator,
            "elapsed_seconds": round(time.perf_counter() - start, 3), **stats}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificates", nargs="+")
    parser.add_argument("--out", type=Path)
    parser.add_argument("--self-check-through", type=int, default=128)
    args = parser.parse_args()
    for h in range(2, args.self_check_through + 1):
        assert blocked_sets(h)[0] == direct_sets(h), ("enumeration self-check", h)
    results = []
    for path in args.certificates:
        result = check_certificate(path)
        results.append(result)
        print(json.dumps(result), flush=True)
    if args.out:
        args.out.write_text(json.dumps({"self_check_through": args.self_check_through,
                                        "results": results}, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
