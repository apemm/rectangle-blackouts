"""Exact finite checks of the paired-gap injection; not the asymptotic proof."""
import json
import math
from collections import Counter, defaultdict
from pathlib import Path


def check(h):
    H = h // 100
    A, K = (h + 1) // 2, h // 2
    edges = defaultdict(set)
    triangles = set()
    for u in range(2, math.isqrt(H) + 1):
        for v in range(1, u):
            base = u * u + v * v
            if base > H or math.gcd(u, v) != 1 or (u + v) % 2 == 0:
                continue
            for q in range(1, H // base + 1, 2):
                a = q * u * v // 2
                b = q * (u * u - v * v)
                L0 = q * base
                triangle = (a, b, L0)
                assert triangle not in triangles
                triangles.add(triangle)
                assert (4 * a) ** 2 + b * b == L0 * L0 and L0 % 2
                T, d, e = 5 * (b - 2 * a), 5 * a, 3 * a + b
                s = (T - 1) // 2
                n = min(A, K - s) - max(0, -s)
                assert T != 0 and T % 2 and T % 5 == 0
                assert 0 < d < n and 0 < e < n and d != e
                assert 20 * d * d + 4 * T * d + T * T == (5 * L0) ** 2
                assert 20 * e * e - 4 * T * e + T * T == (5 * L0) ** 2
                assert 5 * L0 < h and d - e == -T // 5
                edge = tuple(sorted((d, e)))
                assert edge not in edges[T]
                edges[T].add(edge)
    maximum_degree = 0
    for T, pairs in edges.items():
        degrees = Counter(x for pair in pairs for x in pair)
        assert all(abs(d-e) == abs(T)//5 for d, e in pairs)
        maximum_degree = max(maximum_degree, max(degrees.values()))
        assert max(degrees.values()) <= 2
    assert sum(map(len, edges.values())) == len(triangles)
    return dict(h=h, base_hypotenuse_cap=H, triangles=len(triangles),
                edges=sum(map(len, edges.values())), offsets=len(edges),
                maximum_degree=maximum_degree, status="PASS")


if __name__ == "__main__":
    results = [check(h) for h in (1000, 5000, 20000, 100000, 1000000)]
    output = dict(scope="integer sanity checks; proof is in the audit note",
                  results=results)
    Path(__file__).with_suffix(".json").write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(output, indent=2))
