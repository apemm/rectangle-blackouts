"""Exact finite check of the recursive Hilbert cross-comparison order.

The rank matrix is built by the iterative distance-to-cell algorithm.
The proposed comparison order uses a separate quadrant recursion.
This checks finite instances, not the induction for every side length.
"""
from pathlib import Path
import json


def cell_from_rank(n, rank):
    x = y = 0
    scale = 1
    while scale < n:
        rx = (rank // 2) & 1
        ry = (rank ^ rx) & 1
        if ry == 0:
            if rx:
                x = scale - 1 - x
                y = scale - 1 - y
            x, y = y, x
        x += scale * rx
        y += scale * ry
        rank //= 4
        scale *= 2
    return x, y


def comparison_order(n):
    if n == 1:
        return [(0, 0)]
    m = n // 2
    previous = comparison_order(m)
    return (
        [(x, y + m) for x, y in previous]
        + [(y, x) for x, y in reversed(previous)]
        + [(2 * m - 1 - y, m - 1 - x)
           for x, y in reversed(previous)]
        + [(x + m, y + m) for x, y in previous]
    )


def check(n):
    ranks = [[None] * n for _ in range(n)]
    for r in range(n * n):
        x, y = cell_from_rank(n, r)
        assert ranks[x][y] is None
        ranks[x][y] = r
    order = comparison_order(n)
    assert len(order) == n * n and len(set(order)) == n * n
    comparisons = 0
    minimum_margin = n * n
    for p, (a, b) in enumerate(order):
        for c, d in order[p + 1:]:
            margin = ranks[c][b] - ranks[a][d]
            assert margin > 0, (n, (a, b), (c, d), margin)
            minimum_margin = min(minimum_margin, margin)
            comparisons += 1
    return dict(side=n, comparisons=comparisons,
                minimum_rank_margin=minimum_margin)


def main():
    results = [check(n) for n in (2, 4, 8, 16, 32)]
    output = dict(status="PASS", scope="finite exact comparison checks",
                  cases=results,
                  comparisons=sum(r["comparisons"] for r in results))
    Path(__file__).with_suffix(".json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output))


if __name__ == "__main__":
    main()
