"""Independent geometric verification of saved SAT witnesses; no SAT imports."""
from collections import Counter
from pathlib import Path
from hashlib import sha256
import json
import sys
import verify_all_double_7x7 as geometry

here = Path(__file__).resolve().parent
for name in sys.argv[1:]:
    source = here / name
    raw = source.read_bytes()
    data = json.loads(raw)
    assert data['solve_status'] == 'SAT'
    h, w = data['height'], data['width']
    word = data['word']
    assert len(word) == w
    assert all(len(set(rows)) == len(rows) == 2 for rows in word)
    assert all(1 <= row <= h for rows in word for row in rows)
    geometry.H, geometry.W, geometry.WORD = h, w, word
    geometry.POINTS = {(x, y) for x in range(1, w + 1) for y in range(1, h + 1)}
    geometry.BLACK = {(x, y) for x, rows in enumerate(word, 1) for y in rows}
    diagonal = geometry.equal_diagonals()
    perpendicular = geometry.perpendicular_sides()
    parameter, shapes = geometry.positive_side_parameters()
    assert diagonal == perpendicular
    assert parameter == {r for r in diagonal if not geometry.axis(r)}
    presentations = [frozenset(r - geometry.BLACK) for r in diagonal]
    assert len(set(presentations)) == len(diagonal)
    degrees = [sum(row in rows for rows in word) for row in range(1, h + 1)]
    assert min(degrees) >= data.get('min_row_degree', 0)
    if 'row_partition_part' in data:
        part = set(data['row_partition_part'])
        assert all(sum(row in part for row in rows) == 1 for rows in word)
    result = dict(source=source.name, source_sha256=sha256(raw).hexdigest(),
                  status='PASS', height=h, width=w, word=word,
                  rectangle_count=len(diagonal), shape_count=len(shapes),
                  row_degrees=degrees,
                  white_count_histogram=dict(sorted(Counter(map(len, presentations)).items())))
    target = source.with_name(source.stem + '_independent_check.json')
    target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result), flush=True)
