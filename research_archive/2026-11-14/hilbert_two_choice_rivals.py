"""Exact two-choice CSP for opposite-parity Hilbert rival candidates.

Each label r chooses x_r=S*(2*r+b_r), b_r in {0,1}. Same-parity
integral distances stay excluded for S>=32. This script tests only the
remaining opposite-parity pairs with integral length below h.
"""
import argparse
import json
import math
from pathlib import Path
import numpy as np
from check_hilbert_placement import hilbert


def pythagorean_rows(X, h):
    value = (X // 2) ** 2
    result = {}
    for a in range(1, math.isqrt(value) + 1):
        if value % a:
            continue
        b = value // a
        if a + b < h and (b - a) % 2:
            result[b - a] = a + b
            result[a - b] = a + b
    return result


def solve(h, S=32, inside=True):
    A, K = (h + 1) // 2, h // 2
    q = 1 << (max(A, K) - 1).bit_length()
    xy = np.array(hilbert(q), dtype=np.int64)
    active = (xy[:, 0] < A) & (xy[:, 1] < K)
    odd, even = 2 * xy[:, 0] + 1, 2 * xy[:, 1] + 2
    constraints = set()
    for d in range(1, ((h - 1) // S + 1) // 2 + 1):
        for delta in (-1, 0, 1):
            X = S * (2 * d + delta)
            if X >= h:
                continue
            ys = pythagorean_rows(X, h)
            if not ys:
                continue
            mask = active[:-d] & active[d:]
            hyp = np.zeros(2 * q + 2, dtype=np.int64)
            for y, L in ys.items():
                if abs(y) < len(hyp):
                    hyp[abs(y)] = L
            hit = np.zeros(len(mask), dtype=bool)
            for row1, row2 in ((odd[:-d], even[d:]), (even[:-d], odd[d:])):
                L = hyp[np.abs(row2 - row1)]
                one = L > 0
                if inside:
                    row_sum = row1 + row2
                    one &= (row_sum - L >= 2) & (row_sum + L <= 2 * h)
                hit |= one
            hit &= mask
            for r in np.nonzero(hit)[0]:
                constraints.add((int(r), int(r) + d, delta))
    used = sorted({r for p in constraints for r in p[:2]})
    ids = {r: i for i, r in enumerate(used)}
    n = 2 * len(used)
    graph, rev = [[] for _ in range(n)], [[] for _ in range(n)]
    clauses = 0
    for r, s, delta in constraints:
        for a in (0, 1):
            b = a + delta
            if b not in (0, 1):
                continue
            clauses += 1
            u, v = 2 * ids[r] + a, 2 * ids[s] + b
            graph[u].append(v ^ 1)
            rev[v ^ 1].append(u)
            graph[v].append(u ^ 1)
            rev[u ^ 1].append(v)
    seen = bytearray(n)
    finish = []
    for root in range(n):
        if seen[root]:
            continue
        seen[root] = 1
        stack = [(root, 0)]
        while stack:
            v, j = stack[-1]
            if j == len(graph[v]):
                finish.append(v)
                stack.pop()
                continue
            w = graph[v][j]
            stack[-1] = (v, j + 1)
            if not seen[w]:
                seen[w] = 1
                stack.append((w, 0))
    component = [-1] * n
    nc = 0
    for root in reversed(finish):
        if component[root] >= 0:
            continue
        component[root] = nc
        stack = [root]
        while stack:
            v = stack.pop()
            for w in rev[v]:
                if component[w] < 0:
                    component[w] = nc
                    stack.append(w)
        nc += 1
    bad = [r for r in used if component[2 * ids[r]] == component[2 * ids[r] + 1]]
    result = {"h": h, "S": S, "require_completion_in_strip": inside,
              "labels": int(active.sum()),
              "constrained_labels": len(used), "difference_constraints": len(constraints),
              "clauses": clauses, "components": nc, "satisfiable": not bad}
    if bad:
        c = component[2 * ids[bad[0]]]
        core = {used[v // 2] for v in range(n) if component[v] == c}
        result["contradictory_ranks"] = bad[:20]
        result["contradictory_component_labels"] = len(core)
        result["contradictory_component_constraints"] = [p for p in sorted(constraints)
                                                         if p[0] in core and p[1] in core]
        result["contradictory_component_coordinates"] = {r: xy[r].tolist() for r in sorted(core)}
    else:
        assignment = {r: int(component[2 * ids[r] + 1] > component[2 * ids[r]]) for r in used}
        assert all(assignment[s] - assignment[r] != delta for r, s, delta in constraints)
        result["ones"] = sum(assignment.values())
        result["assignment_ones"] = [r for r in used if assignment[r]]
        result["verified_constraints"] = len(constraints)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("heights", nargs="+", type=int)
    parser.add_argument("--stride", type=int, default=32)
    parser.add_argument("--allow-outside", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    results = []
    for h in args.heights:
        result = solve(h, args.stride, not args.allow_outside)
        results.append(result)
        print(json.dumps({k: v for k, v in result.items()
                          if k not in ("assignment_ones", "contradictory_component_constraints",
                                       "contradictory_component_coordinates")}), flush=True)
    args.out.write_text(json.dumps(results, indent=2) + "\n")


if __name__ == "__main__":
    main()
