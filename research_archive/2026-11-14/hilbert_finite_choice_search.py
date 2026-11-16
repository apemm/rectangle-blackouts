"""Search bounded local choices for in-strip Hilbert vertical rivals.

Success is a certificate checked against every reconstructed constraint.
Failure is not an unsatisfiability claim.
"""
import argparse
import heapq
import json
from pathlib import Path
import random
import numpy as np
from check_hilbert_placement import hilbert
from hilbert_two_choice_rivals import pythagorean_rows


def hilbert_array(q):
    """The same four recursive maps, without a large Python tuple list."""
    xy = np.zeros((1, 2), dtype=np.int64)
    n = 1
    while n < q:
        block = n * n
        nxt = np.empty((4 * block, 2), dtype=np.int64)
        nxt[:block] = xy[:, ::-1]
        nxt[block:2 * block] = xy + (0, n)
        nxt[2 * block:3 * block] = xy + (n, n)
        nxt[3 * block:, 0] = 2 * n - 1 - xy[:, 1]
        nxt[3 * block:, 1] = n - 1 - xy[:, 0]
        xy = nxt
        n *= 2
    return xy


def search(h, M, S=32, max_steps=1000000, seed=14):
    A, K = (h + 1) // 2, h // 2
    q = 1 << (max(A, K) - 1).bit_length()
    xy = hilbert_array(q)
    active = (xy[:, 0] < A) & (xy[:, 1] < K)
    odd, even = 2 * xy[:, 0] + 1, 2 * xy[:, 1] + 2
    constraints = set()
    for d in range(1, ((h - 1) // S + M - 1) // M + 1):
        for delta in range(1 - M, M):
            X = S * (M * d + delta)
            if X >= h:
                continue
            ys = pythagorean_rows(X, h)
            if not ys:
                continue
            hyp = np.zeros(2 * q + 2, dtype=np.int64)
            for y, L in ys.items():
                if abs(y) < len(hyp):
                    hyp[abs(y)] = L
            hit = np.zeros(q * q - d, dtype=bool)
            for row1, row2 in ((odd[:-d], even[d:]), (even[:-d], odd[d:])):
                L = hyp[np.abs(row2 - row1)]
                row_sum = row1 + row2
                hit |= (L > 0) & (row_sum - L >= 2) & (row_sum + L <= 2 * h)
            hit &= active[:-d] & active[d:]
            for r in np.nonzero(hit)[0]:
                constraints.add((int(r), int(r) + d, delta))
    edges = sorted(constraints)
    adjacency = {}
    for k, (r, s, delta) in enumerate(edges):
        adjacency.setdefault(r, []).append((s, delta, k))
        adjacency.setdefault(s, []).append((r, -delta, k))
    degrees = {r: len(links) for r, links in adjacency.items()}
    heap = [(degree, r) for r, degree in degrees.items()]
    heapq.heapify(heap)
    remaining = set(adjacency)
    peel = []
    weighted_degeneracy = 0
    while heap:
        degree, r = heapq.heappop(heap)
        if r not in remaining or degree != degrees[r]:
            continue
        weighted_degeneracy = max(weighted_degeneracy, degree)
        peel.append(r)
        remaining.remove(r)
        for s, _, _ in adjacency[r]:
            if s in remaining:
                degrees[s] -= 1
                heapq.heappush(heap, (degrees[s], s))
    choice = {r: 0 for r in adjacency}
    rng = random.Random(seed)
    # Directed greedy first. At r, a constraint from an earlier s excludes
    # choice[s]-delta, because choice[s]-choice[r]=delta in adjacency[r].
    greedy_failures = 0
    processed = set()
    for r in reversed(peel):
        costs = [0] * M
        for s, delta, _ in adjacency[r]:
            if s not in processed:
                continue
            forbidden = choice[s] - delta
            if 0 <= forbidden < M:
                costs[forbidden] += 1
        minimum = min(costs)
        if minimum:
            greedy_failures += 1
        choice[r] = rng.choice([i for i, cost in enumerate(costs) if cost == minimum])
        processed.add(r)
    if weighted_degeneracy < M:
        assert greedy_failures == 0
    def violated(k):
        r, s, delta = edges[k]
        return choice[s] - choice[r] == delta
    bad = {k for k in range(len(edges)) if violated(k)}
    steps = 0
    while bad and steps < max_steps:
        k = next(iter(bad)) if steps % 97 else rng.choice(tuple(bad))
        r, s, _ = edges[k]
        vertex = rng.choice((r, s))
        costs = [0] * M
        for neighbor, delta, _ in adjacency[vertex]:
            forbidden = choice[neighbor] - delta
            if 0 <= forbidden < M:
                costs[forbidden] += 1
        minimum = min(costs)
        values = [i for i, cost in enumerate(costs) if cost == minimum]
        if steps % 101 == 100:
            choice[vertex] = rng.randrange(M)
        else:
            choice[vertex] = rng.choice(values)
        for _, _, affected in adjacency[vertex]:
            if violated(affected):
                bad.add(affected)
            else:
                bad.discard(affected)
        steps += 1
    remaining = sum(violated(k) for k in range(len(edges)))
    assert remaining == len(bad)
    return {"h": h, "S": S, "choices": M, "labels": int(active.sum()),
            "constraints": len(edges), "constrained_labels": len(adjacency),
            "maximum_constraint_incidence": max(map(len, adjacency.values()), default=0),
            "weighted_degeneracy": weighted_degeneracy,
            "greedy_failures": greedy_failures, "repair_steps": steps,
            "remaining_violations": remaining, "success": remaining == 0,
            "nonzero_choices": {r: a for r, a in choice.items() if a}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("h", type=int)
    parser.add_argument("choices", type=int)
    parser.add_argument("--stride", type=int, default=32)
    parser.add_argument("--max-steps", type=int, default=1000000)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    result = search(args.h, args.choices, args.stride, args.max_steps)
    args.out.write_text(json.dumps(result) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "nonzero_choices"}))


if __name__ == "__main__":
    main()
