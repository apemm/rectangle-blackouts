"""Exact finite checks for the hole-free rectangle and triangle recursions."""
from fractions import Fraction
import json
from pathlib import Path
import random


def rectangle_point(a, b, r):
    assert a >= 1 and b >= 1 and 0 <= r < a * b
    if a == 1:
        return 0, r
    if b == 1:
        return r, 0
    al, ar, bl, br = a // 2, (a + 1) // 2, b // 2, (b + 1) // 2
    if r < al * bl:
        u, v = rectangle_point(bl, al, r)
        return v, u
    r -= al * bl
    if r < al * br:
        u, v = rectangle_point(al, br, r)
        return u, v + bl
    r -= al * br
    if r < ar * br:
        u, v = rectangle_point(ar, br, r)
        return u + al, v + bl
    r -= ar * br
    u, v = rectangle_point(bl, ar, r)
    return a - 1 - v, bl - 1 - u


def triangular_size(n):
    return n * (n + 1) // 2


def triangle_point(n, r):
    assert n >= 1 and 0 <= r < triangular_size(n)
    if n == 1:
        return 0, 0
    a, k = (n + 1) // 2, n // 2
    if r < triangular_size(a):
        u, v = triangle_point(a, r)
        return v, u
    r -= triangular_size(a)
    if r < triangular_size(k):
        u, v = triangle_point(k, r)
        return u, v + a
    r -= triangular_size(k)
    if r < triangular_size(a - 1):
        u, v = triangle_point(a - 1, r)
        return a - 1 - v, a - 1 - u
    r -= triangular_size(a - 1)
    u, v = triangle_point(k, r)
    return u + a, v


def linf(p, q):
    return max(abs(p[0] - q[0]), abs(p[1] - q[1]))


def hexdist(p, q):
    u, v = p[0] - q[0], p[1] - q[1]
    return max(abs(u), abs(v), abs(u + v))


def all_pairs(points, metric, bound):
    worst = Fraction(0)
    count = 0
    for s, q in enumerate(points):
        for r in range(s):
            distance2 = metric(points[r], q) ** 2
            assert distance2 <= bound * (s - r)
            worst = max(worst, Fraction(distance2, s - r))
            count += 1
    return worst, count


def main():
    rect_cases = rect_pairs = tri_pairs = 0
    rect_max = tri_max = Fraction(0)
    for a in range(1, 17):
        for b in range(1, 17):
            if max(a, b) > 2 * min(a, b) + 2:
                continue
            pts = [rectangle_point(a, b, r) for r in range(a * b)]
            assert set(pts) == {(i, j) for i in range(a) for j in range(b)}
            for r, p in enumerate(pts):
                assert linf(p, (0, 0)) ** 2 <= 16 * (r + 1)
                assert linf(p, (a - 1, 0)) ** 2 <= 16 * (a * b - r)
            assert linf(pts[-1], (a - 1, 0)) <= 3
            bound = 32 if abs(a - b) <= 1 else 81
            worst, count = all_pairs(pts, linf, bound)
            rect_max, rect_pairs = max(rect_max, worst), rect_pairs + count
            rect_cases += 1
    for n in range(1, 33):
        pts = [triangle_point(n, r) for r in range(triangular_size(n))]
        assert set(pts) == {(u, v) for u in range(n) for v in range(n - u)}
        assert pts[0] == (0, 0) and pts[-1] == (n - 1, 0)
        assert all(hexdist(p, q) == 1 for p, q in zip(pts, pts[1:]))
        for r, p in enumerate(pts):
            assert hexdist(p, (0, 0)) ** 2 <= 9 * (r + 1)
            assert hexdist(p, (n - 1, 0)) ** 2 <= 9 * (len(pts) - r)
        worst, count = all_pairs(pts, hexdist, 49)
        tri_max, tri_pairs = max(tri_max, worst), tri_pairs + count
    rng = random.Random(20261115)
    random_checks = 0
    for a, b in [(999, 1000), (1000, 1999), (65535, 65536), (1000001, 1999999)]:
        for _ in range(5000):
            r, s = sorted(rng.sample(range(a * b), 2))
            p, q = rectangle_point(a, b, r), rectangle_point(a, b, s)
            assert linf(p, q) ** 2 <= 81 * (s - r)
            random_checks += 1
    for n in (1023, 1024, 1025, 1000001):
        for _ in range(5000):
            r, s = sorted(rng.sample(range(triangular_size(n)), 2))
            assert hexdist(triangle_point(n, r), triangle_point(n, s)) ** 2 <= 49 * (s - r)
            random_checks += 1
    result = {
        "status": "PASS", "rectangle_cases": rect_cases,
        "rectangle_pair_checks": rect_pairs, "rectangle_max_observed_ratio": str(rect_max),
        "triangle_cases": 32, "triangle_pair_checks": tri_pairs,
        "triangle_max_observed_ratio": str(tri_max),
        "large_random_pair_checks": random_checks,
        "scope": "Finite checks supplement the uniform analytical proof."
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
