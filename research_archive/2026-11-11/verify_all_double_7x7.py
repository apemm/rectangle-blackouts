"""Two independent rectangle generators and a finite all-double certificate.

No SAT package is imported. Coordinates in the output are one-based (column,row).
"""

from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
H = W = 7
WORD = ((1, 7), (6, 7), (1, 5), (3, 5), (3, 6), (2, 3), (1, 2))
POINTS = {(x, y) for x in range(1, W + 1) for y in range(1, H + 1)}
BLACK = {(x, y) for x, rows in enumerate(WORD, 1) for y in rows}


def equal_diagonals():
    groups = defaultdict(list)
    for a, b in combinations(sorted(POINTS), 2):
        key = (a[0] + b[0], a[1] + b[1],
               (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
        groups[key].append((a, b))
    rectangles = set()
    for diagonals in groups.values():
        for first, second in combinations(diagonals, 2):
            corners = frozenset(first + second)
            if len(corners) == 4:
                rectangles.add(corners)
    return rectangles


def perpendicular_sides():
    rectangles = set()
    for root in POINTS:
        for a, b in combinations(POINTS - {root}, 2):
            dot = sum((a[i] - root[i]) * (b[i] - root[i]) for i in (0, 1))
            if dot:
                continue
            fourth = tuple(a[i] + b[i] - root[i] for i in (0, 1))
            if fourth in POINTS:
                rectangles.add(frozenset((root, a, b, fourth)))
    return rectangles


def axis(rectangle):
    return all(len({point[i] for point in rectangle}) == 2 for i in (0, 1))


def positive_side_parameters():
    tilted = set()
    shapes = []
    for a in range(1, W - 1):
        for c in range(1, W - a):
            for b in range(1, H - 1):
                for d in range(1, H - b):
                    if a * c != b * d:
                        continue
                    shapes.append((a, b, c, d))
                    for x in range(1, W - a - c + 1):
                        for y in range(1, H - b - d + 1):
                            tilted.add(frozenset(((x + c, y), (x + c + a, y + b),
                                                 (x, y + d), (x + a, y + b + d))))
    return tilted, shapes


def axis_rival(white):
    """Independent closed-form test, valid for the actual row-pair family."""
    family = {frozenset(rows) for rows in WORD}
    if len(white) == 1:
        (x, r), = white
        return any(frozenset((r, s)) in family for s in WORD[x - 1])
    (x, r), (z, s) = sorted(white)
    if x == z:
        return frozenset((r, s)) in family
    if r == s:
        return bool(set(WORD[x - 1]) & set(WORD[z - 1]))
    return s in WORD[x - 1] and r in WORD[z - 1]


def fmt(points):
    return ', '.join(f'({x},{y})' for x, y in points)


def main():
    first, second = equal_diagonals(), perpendicular_sides()
    assert first == second
    assert len(first) == 640
    parameter_rectangles, shapes = positive_side_parameters()
    assert parameter_rectangles == {r for r in first if not axis(r)}
    assert len(shapes) == 31
    assert len(BLACK) == 14
    assert all(sum(x == col for x, y in BLACK) == 2 for col in range(1, W + 1))
    presentations = {}
    rows = []
    for rectangle in sorted(first, key=lambda r: tuple(sorted(r))):
        white = frozenset(rectangle - BLACK)
        assert white and white not in presentations
        presentations[white] = rectangle
        if len(white) <= 2:
            rows.append(dict(kind='axis' if axis(rectangle) else 'tilted',
                             white=sorted(white), black=sorted(rectangle & BLACK)))
            if not axis(rectangle):
                assert not axis_rival(white)
    assert len(set(map(frozenset, WORD))) == 7
    row_edges = {frozenset(e) for e in WORD}
    assert not any(all(frozenset(e) in row_edges for e in combinations(triple, 2))
                   for triple in combinations(range(1, H + 1), 3))
    histogram = dict(sorted(Counter(len(p) for p in presentations).items()))
    counts = Counter((row['kind'], len(row['white'])) for row in rows)
    result = dict(status='PASS', height=H, width=W, word=WORD,
                  rectangle_count=len(first), axis_count=sum(map(axis, first)),
                  tilted_count=sum(not axis(r) for r in first),
                  positive_side_parameter_shapes=shapes,
                  white_count_histogram=histogram,
                  weak_counts={f'{kind}_{size}': count
                               for (kind, size), count in sorted(counts.items())},
                  weak_rectangles=sorted(rows, key=lambda r: (r['kind'], r['white'])))
    (HERE / 'all_double_7x7_certificate.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')

    text = [
        '# Finite presentation certificate for the all-double 7 by 7 board', '',
        'Coordinates are (column,row), both starting at one. The black row pairs',
        'are 17, 67, 15, 35, 36, 23, 12. Two independent enumerators find',
        '441 axis rectangles and 199 tilted rectangles.', '',
        'No rectangle is hidden. There are 25 one-white presentations and 159',
        'two-white presentations. All are distinct. Presentations with at least',
        'three white corners identify a rectangle automatically.', '',
        'The following tables list every rectangle with at most two white',
        'corners. Each row supplies its full rectangle by joining the two cells',
        'or three cells in the black column to the white column. Distinct rows',
        'have distinct white sets, including across the two tables.', '',
    ]
    for kind in ('tilted', 'axis'):
        text.extend([f'## {kind.capitalize()} rectangles', '',
                     '| White corners | Black corners |', '|---|---|'])
        for row in sorted((r for r in rows if r['kind'] == kind),
                          key=lambda r: r['white']):
            text.append(f"| {fmt(row['white'])} | {fmt(row['black'])} |")
        text.append('')
    text.extend(['Generated and checked by [verify_all_double_7x7.py](verify_all_double_7x7.py).', ''])
    (HERE / 'all_double_7x7_weak_rectangles.md').write_text('\n'.join(text), encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'weak_rectangles'}))


if __name__ == '__main__':
    main()
