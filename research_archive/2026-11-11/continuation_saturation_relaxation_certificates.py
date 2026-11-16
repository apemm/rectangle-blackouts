"""Solver-free checks for the small analytical saturation reductions."""
from itertools import combinations, permutations
from pathlib import Path
import json
import verify_all_double_7x7 as geometry

HERE = Path(__file__).resolve().parent


def configure(h, word):
    w = len(word)
    geometry.H, geometry.W, geometry.WORD = h, w, word
    geometry.POINTS = {(x, y) for x in range(1, w + 1) for y in range(1, h + 1)}
    geometry.BLACK = {(x, y) for x, rows in enumerate(word, 1) for y in rows}
    first = geometry.equal_diagonals()
    assert first == geometry.perpendicular_sides()
    return first, geometry.BLACK


def main():
    by_part = {}
    for second in (2, 3, 4):
        part = {1, second}
        pairs = [tuple(sorted((a, b))) for a in part for b in set(range(1, 5)) - part]
        passing = []
        for word in permutations(pairs):
            rectangles, black = configure(4, word)
            tilted = [r for r in rectangles if not geometry.axis(r)]
            assert len(rectangles) == 44 and len(tilted) == 8
            if all(len(r & black) <= 2 for r in tilted):
                passing.append(word)
                seen = {}
                failed = False
                for rectangle in rectangles:
                    white = frozenset(rectangle - black)
                    if white in seen:
                        assert len(white) == 2
                        failed = True
                        break
                    seen[white] = rectangle
                assert failed
        by_part[str(sorted(part))] = passing
    assert [len(by_part[key]) for key in sorted(by_part)] == [0, 4, 0]

    word = ((5, 6), (2, 3), (4, 6), (2, 4), (1, 6), (3, 6), (1, 2))
    rectangles, black = configure(6, word)
    family = {frozenset(pair) for pair in word}
    assert len(family) == len(word)
    assert not any(all(frozenset(pair) in family for pair in combinations(rows, 2))
                   for rows in combinations(range(1, 7), 3))
    fortyfive = [r for r in rectangles
                if len({x - y for x, y in r}) == len({x + y for x, y in r}) == 2]
    assert len(fortyfive) == 70
    assert all(len(r & black) <= 2 for r in fortyfive)
    rectangle = frozenset(((5, 1), (6, 3), (4, 4), (3, 2)))
    rival = frozenset(((3, 2), (4, 2), (3, 4), (4, 4)))
    assert rectangle in rectangles and rival in rectangles
    assert rectangle - black == rival - black == {(3, 2)}
    result = dict(status='PASS', h4_corner_free_orders_by_part=by_part,
                  h6_width7_word=word, h6_45_rectangles=len(fortyfive),
                  h6_no_three_black_45=True,
                  h6_failing_non45_rectangle=sorted(rectangle),
                  h6_axis_rival=sorted(rival))
    (HERE / 'continuation_saturation_relaxation_certificates.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
