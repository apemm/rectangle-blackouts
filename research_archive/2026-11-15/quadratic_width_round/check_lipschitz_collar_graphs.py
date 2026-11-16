"""Independent finite check by enumerating all lattice rectangles.

No support classification from the proof is used to enumerate collisions.
"""

from collections import defaultdict
from itertools import combinations
from math import isqrt
import json
from pathlib import Path


def rectangles(width, height):
    groups = defaultdict(list)
    points = [(x, y) for x in range(width) for y in range(1, height + 1)]
    for p, q in combinations(points, 2):
        key = (p[0] + q[0], p[1] + q[1],
               (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)
        groups[key].append((p, q))
    out = set()
    for diagonals in groups.values():
        for first, second in combinations(diagonals, 2):
            vertices = frozenset(first + second)
            if len(vertices) == 4:
                out.add(vertices)
    return sorted(out, key=lambda r: sorted(r))


def walks(width, height):
    def extend(prefix):
        if len(prefix) == width:
            yield tuple(prefix)
            return
        choices = range(1, height + 1) if not prefix else range(
            max(1, prefix[-1] - 1), min(height, prefix[-1] + 1) + 1)
        for y in choices:
            yield from extend(prefix + [y])
    yield from extend([])


def check_board(rows, all_rectangles):
    black = {(x, y) for x, y in enumerate(rows)}
    presentations = {}
    parked = 0
    for rect in all_rectangles:
        white = rect - black
        assert white, ("fully black rectangle", rows, sorted(rect))
        assert white not in presentations, (
            "equal white parts", rows, sorted(white),
            sorted(rect), sorted(presentations.get(white, ())))
        presentations[white] = rect
        if len(white) == 1:
            x, y = next(iter(white))
            assert (y - rows[x]) % 2 == 0, ("unparked", rows, (x, y))
            parked += 1
    return parked


def actual_p(rows, height):
    for x, z in combinations(range(len(rows)), 2):
        if (z - x) % 2 or (rows[z] - rows[x]) % 2 == 0:
            continue
        norm = (z - x) ** 2 + (rows[z] - rows[x]) ** 2
        length = isqrt(norm)
        if length * length != norm:
            continue
        lo = (rows[x] + rows[z] - length) // 2
        hi = (rows[x] + rows[z] + length) // 2
        if 1 <= lo <= hi <= height:
            return (x, z, lo, hi)
    return None


def main():
    cases = []
    for width, height in [(5, 5), (7, 6), (9, 4)]:
        rects = rectangles(width, height)
        count = parked = checkerboard = adjacent = 0
        ordinary_p_example = None
        for rows in walks(width, height):
            count += 1
            parked += check_board(rows, rects)
            is_checkerboard = len({(x + y) % 2 for x, y in enumerate(rows)}) == 1
            is_adjacent = max(rows) - min(rows) <= 1
            witness = actual_p(rows, height)
            if is_checkerboard or is_adjacent:
                assert witness is None, ("P in special background", rows, witness)
            elif witness and ordinary_p_example is None:
                ordinary_p_example = {"rows": rows, "witness": witness}
            checkerboard += is_checkerboard
            adjacent += is_adjacent
        cases.append({
            "width": width, "height": height, "rectangles": len(rects),
            "graphs": count, "parked_one_white_presentations": parked,
            "checkerboard_graphs": checkerboard, "adjacent_row_graphs": adjacent,
            "ordinary_lipschitz_p_example": ordinary_p_example,
        })
    result = {"status": "PASS", "scope": "Finite graph-background checks only", "cases": cases}
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
