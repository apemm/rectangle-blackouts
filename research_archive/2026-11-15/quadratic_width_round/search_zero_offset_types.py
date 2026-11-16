"""Exact small-block, all-offset search for zero-offset P cliques.

No archive code is imported. Original local Hilbert ranks are retained.
Only delta=0 is tested. Output is a targeted arithmetic type search, not
an actual-height graph census.
"""

import argparse
import json
import time
from collections import defaultdict
from pathlib import Path


def curve(n):
    if n == 1:
        return [(0, 0)]
    m = n // 2
    a = curve(m)
    return (
        [(y, x) for x, y in a]
        + [(x, y + m) for x, y in a]
        + [(x + m, y + m) for x, y in a]
        + [(2 * m - 1 - y, m - 1 - x) for x, y in a]
    )


def divisors_of_square(n):
    fs = []
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            fs.append((p, 2 * e))
        p = 3 if p == 2 else p + 2
    if n > 1:
        fs.append((n, 2))
    ds = [1]
    for p, e in fs:
        old = ds
        ds = [d * p**j for d in old for j in range(e + 1)]
    return ds


def odd_vertical_legs(x):
    assert x % 2 == 0
    n = (x // 2) ** 2
    return sorted(
        {n // a - a for a in divisors_of_square(x // 2)
         if a * a < n and (n // a - a) % 2 == 1}
    )


def grouped_events(side, stride, choices, orient):
    pts = curve(side)
    if orient == "swap":
        pts = [(y, x) for x, y in pts]
    count = len(pts)
    for d in range(1, count):
        by_u = defaultdict(set)
        for r in range(count - d):
            x, y = pts[r]
            xx, yy = pts[r + d]
            by_u[yy - x].add(r)
            by_u[y - xx].add(r)
        for vertical in odd_vertical_legs(stride * choices * d):
            for sign in (-1, 1):
                total_u = (sign * vertical - 1) // 2
                residue = total_u % side
                for local_u in (residue, residue - side):
                    ranks = by_u.get(local_u)
                    if ranks:
                        offset = (total_u - local_u) // side
                        yield offset, d, ranks


def find_clique4(adj):
    for u, ns in adj.items():
        for v in ns:
            if v <= u:
                continue
            common = sorted(w for w in ns & adj[v] if w > v)
            for j, w in enumerate(common):
                for z in common[j + 1:]:
                    if z in adj[w]:
                        return [u, v, w, z]
    return None


def run(side, stride, choices, orient):
    started = time.monotonic()
    gap_masks = {}
    grouped = 0
    for k, d, _ in grouped_events(side, stride, choices, orient):
        gap_masks[k] = gap_masks.get(k, 0) | (1 << d)
        grouped += 1
    eligible = {k for k, mask in gap_masks.items() if mask.bit_count() >= 3}
    graphs = {k: defaultdict(set) for k in eligible}
    for k, d, ranks in grouped_events(side, stride, choices, orient):
        if k not in graphs:
            continue
        adj = graphs[k]
        for r in ranks:
            adj[r].add(r + d)
            adj[r + d].add(r)
    witnesses = []
    max_edges = 0
    max_degree = 0
    for k, adj in graphs.items():
        max_edges = max(max_edges, sum(map(len, adj.values())) // 2)
        max_degree = max(max_degree, max(map(len, adj.values()), default=0))
        clique = find_clique4(adj)
        if clique:
            pts = curve(side)
            if orient == "swap":
                pts = [(y, x) for x, y in pts]
            witnesses.append({
                "offset": k, "ranks": clique,
                "local_cells": [pts[r] for r in clique],
            })
    return {
        "side": side, "stride": stride, "choices": choices,
        "orientation": orient, "offset_types_with_edges": len(gap_masks),
        "types_with_at_least_three_rank_gaps": len(eligible),
        "grouped_arithmetic_events": grouped,
        "max_edges_in_eligible_type": max_edges,
        "max_degree_in_eligible_type": max_degree,
        "clique4_witnesses": witnesses,
        "seconds": time.monotonic() - started,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sides", nargs="+", type=int, default=[8, 16])
    ap.add_argument("--stride", type=int, default=32)
    ap.add_argument("--choices", type=int, default=3)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    results = []
    for side in args.sides:
        assert side > 0 and side & (side - 1) == 0
        for orient in ("id", "swap"):
            result = run(side, args.stride, args.choices, orient)
            results.append(result)
            print(json.dumps(result), flush=True)
    if args.output:
        args.output.write_text(json.dumps(results, indent=2) + "\n")


if __name__ == "__main__":
    main()
