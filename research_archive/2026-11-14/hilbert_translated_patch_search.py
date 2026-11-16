"""Exhaustive P-constraint cores on a translated finite Hilbert patch.

The odd/even row offset D is unbounded. All possible integer diagonal
lengths are enumerated from divisors of (X/2)^2. D == 1 mod 2R is
necessary for an aligned identity-oriented R-square. These are candidate
constraints; no global embedding or owner geometry is inferred.
"""
import argparse
from collections import Counter, defaultdict
import heapq
import json
from pathlib import Path

from check_hilbert_placement import hilbert


def positive_pyth_rows(X):
    n = X // 2
    factors = []
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            factors.append((p, 2 * e))
        p += 1
    if n > 1:
        factors.append((n, 2))
    divisors = [1]
    for p, e in factors:
        divisors = [d * p ** j for d in divisors for j in range(e + 1)]
    N = (X // 2) ** 2
    return sorted({N // a - a for a in divisors
                   if a * a < N and (N // a - a) % 2})


def degeneracy(edges):
    adjacency = defaultdict(list)
    for r, s, delta in edges:
        adjacency[r].append(s)
        adjacency[s].append(r)
    degree = {r: len(a) for r, a in adjacency.items()}
    heap = [(d, r) for r, d in degree.items()]
    heapq.heapify(heap)
    remain = set(adjacency)
    result, core = 0, []
    while heap:
        d, r = heapq.heappop(heap)
        if r not in remain or degree[r] != d:
            continue
        if d > result:
            result, core = d, sorted(remain)
        remain.remove(r)
        for s in adjacency[r]:
            if s in remain:
                degree[s] -= 1
                heapq.heappush(heap, (degree[s], s))
    return result, core


def search(R, M, S=32):
    xy = hilbert(R)
    groups = defaultdict(set)
    for d in range(1, R * R):
        for delta in range(1 - M, M):
            X = S * (M * d + delta)
            ys = positive_pyth_rows(X)
            for r in range(R * R - d):
                s = r + d
                i, j = xy[r]
                k, ell = xy[s]
                for y in ys:
                    for D in (y - 2 * ell + 2 * i, -y - 2 * ell + 2 * i,
                              2 * k - 2 * j + y, 2 * k - 2 * j - y):
                        if D % (2 * R) == 1:
                            groups[D].add((r, s, delta))
    histogram = Counter()
    best = []
    max_d = -1
    for D, edges in groups.items():
        deg, core = degeneracy(edges)
        histogram[deg] += 1
        if deg > max_d:
            max_d, best = deg, []
        if deg == max_d and len(best) < 5:
            vertices = set(core)
            best.append({"D": D, "edges": len(edges), "core_vertices": core,
                         "core_edges": sorted(e for e in edges
                                              if e[0] in vertices and e[1] in vertices)})
    return {"R": R, "M": M, "S": S, "offset_groups": len(groups),
            "degeneracy_histogram": dict(histogram), "maximum_degeneracy": max_d,
            "examples": best}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("R", type=int)
    parser.add_argument("M", type=int)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    result = search(args.R, args.M)
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "examples"}))


if __name__ == "__main__":
    main()
