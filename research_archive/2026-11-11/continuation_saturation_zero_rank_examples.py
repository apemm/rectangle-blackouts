"""Saturated row-pair layouts with zero cycle rank in every tilted direction.

These examples are not valid blackouts. The script independently checks
the forest certificates and identifies local failures they do not detect.
"""

from pathlib import Path
from math import gcd
import json
import verify_all_double_7x7 as geometry

HERE = Path(__file__).resolve().parent
EXAMPLES = {
    5: ((4, 5), (3, 4), (2, 5), (1, 4), (2, 3), (1, 2)),
    6: ((1, 2), (3, 6), (1, 6), (5, 6), (3, 4), (2, 3), (1, 4), (2, 5), (4, 5)),
    7: ((5, 6), (4, 7), (1, 6), (1, 4), (4, 5), (3, 4),
        (1, 2), (3, 6), (2, 5), (6, 7), (2, 7), (2, 3)),
}


def cycle_rank(points, a, b):
    parent = {}
    def root(vertex):
        parent.setdefault(vertex, vertex)
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex
    rank = 0
    for x, y in sorted(points):
        first = root((0, b * x - a * y))
        second = root((1, a * x + b * y))
        if first == second:
            rank += 1
        else:
            parent[first] = second
    components = len({root(vertex) for vertex in parent})
    assert rank == len(points) - len(parent) + components
    return dict(a=a, b=b, cycle_rank=rank,
                occupied_lines=len(parent), components=components)


def main():
    records = []
    for h, word in EXAMPLES.items():
        w = len(word)
        assert w == h * h // 4
        assert {frozenset(pair) for pair in word} == {
            frozenset((a, b)) for a in range(1, h + 1, 2) for b in range(2, h + 1, 2)}
        black = {(x, y) for x, rows in enumerate(word, 1) for y in rows}
        directions = [cycle_rank(black, a, b)
                      for a in range(1, h) for b in range(1, h) if gcd(a, b) == 1]
        assert all(d['cycle_rank'] == 0 for d in directions)
        geometry.H, geometry.W, geometry.WORD = h, w, word
        geometry.POINTS = {(x, y) for x in range(1, w + 1) for y in range(1, h + 1)}
        geometry.BLACK = black
        rectangles = geometry.equal_diagonals()
        assert rectangles == geometry.perpendicular_sides()
        parameters, shapes = geometry.positive_side_parameters()
        assert parameters == {r for r in rectangles if not geometry.axis(r)}
        triples = sorted((sorted(r), sorted(r - black)) for r in parameters if len(r & black) == 3)
        assert triples
        presentations = {}
        mixed_pairs = []
        for rectangle in sorted(rectangles, key=lambda r: tuple(sorted(r))):
            white = frozenset(rectangle - black)
            assert white
            if white in presentations and len(white) == 2:
                mixed_pairs.append(dict(white=sorted(white), rectangle=sorted(rectangle),
                                        other=sorted(presentations[white])))
            else:
                presentations[white] = rectangle
        record = dict(height=h, width=w, word=word, status='PASS',
                      saturated_complete_parity_family=True,
                      all_tilted_cycle_ranks_zero=True,
                      checked_primitive_directions=len(directions),
                      direction_certificates=directions,
                      tilted_three_black_count=len(triples),
                      first_three_black_rectangle=triples[0],
                      two_white_collision_count=len(mixed_pairs),
                      first_two_white_collision=mixed_pairs[0] if mixed_pairs else None)
        records.append(record)
        print(json.dumps({k: v for k, v in record.items() if k != 'direction_certificates'}), flush=True)
    (HERE / 'continuation_saturation_zero_rank_examples.json').write_text(
        json.dumps(records, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
