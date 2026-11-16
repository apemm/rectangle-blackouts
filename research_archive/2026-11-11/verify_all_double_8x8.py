"""Independent finite check of the parity-pair 8 by 8 all-double witness."""
from collections import Counter
from pathlib import Path
import json
import verify_all_double_7x7 as geometry

geometry.H = geometry.W = 8
geometry.WORD = ((1, 4), (1, 6), (4, 7), (2, 7),
                 (6, 7), (1, 2), (7, 8), (1, 8))
geometry.POINTS = {(x, y) for x in range(1, 9) for y in range(1, 9)}
geometry.BLACK = {(x, y) for x, rows in enumerate(geometry.WORD, 1) for y in rows}
first = geometry.equal_diagonals()
second = geometry.perpendicular_sides()
third, shapes = geometry.positive_side_parameters()
assert first == second and len(first) == 1192
assert third == {r for r in first if not geometry.axis(r)}
presentations = [frozenset(r - geometry.BLACK) for r in first]
assert all(presentations) and len(set(presentations)) == len(first)
assert all((a - b) % 2 for a, b in geometry.WORD)
assert {frozenset(pair) for pair in geometry.WORD} == {
    frozenset((a, b)) for a in (1, 7) for b in (2, 4, 6, 8)}
result = dict(status='PASS', height=8, width=8, word=geometry.WORD,
              rectangles=len(first), axis=sum(map(geometry.axis, first)),
              tilted=len(third), shape_count=len(shapes),
              white_count_histogram=dict(sorted(Counter(map(len, presentations)).items())),
              row_graph='K_{2,4}: {1,7} versus {2,4,6,8}')
Path(__file__).with_name('all_double_8x8_independent_check.json').write_text(
    json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result))
