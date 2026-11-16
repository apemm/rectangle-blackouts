"""Exact finite check for saturated_diagonal_forest.md."""
from collections import defaultdict
from itertools import combinations
import json
from pathlib import Path

h, m = 7, 4
columns = [(1, 7), (3, 7), (1, 5), (4, 6)]
black = {(x, y) for x, rows in enumerate(columns, 1) for y in rows}
points = [(x, y) for x in range(1, m + 1) for y in range(1, h + 1)]
diagonals = defaultdict(list)
for A, B in combinations(points, 2):
    key = (A[0] + B[0], A[1] + B[1], sum((a-b)**2 for a,b in zip(A,B)))
    diagonals[key].append((A, B))
rectangles = set()
for pairs in diagonals.values():
    for first, second in combinations(pairs, 2):
        corners = frozenset(first + second)
        if len(corners) == 4:
            rectangles.add(corners)
presentations = {}
for corners in rectangles:
    shown = corners - black
    assert shown not in presentations, (corners, presentations.get(shown), shown)
    presentations[shown] = corners
    if len({x for x,y in corners}) > 2:
        assert len(corners & black) <= 2

lines = defaultdict(set)
for x, y in black:
    lines[("+", y-x)].add((x,y))
    lines[("-", y+x)].add((x,y))
adj = defaultdict(set)
for x, y in black:
    u, v = ("+", y-x), ("-", y+x)
    adj[u].add(v)
    adj[v].add(u)
components = []
unseen = set(adj)
while unseen:
    root = min(unseen)
    stack, component = [root], set()
    while stack:
        v = stack.pop()
        if v in component:
            continue
        component.add(v)
        stack.extend(adj[v] - component)
    unseen -= component
    edges = sum(len(adj[v]) for v in component) // 2
    assert edges == len(component) - 1
    components.append({"vertices":len(component), "edges":edges})
empty = 2*(m+h-1) - len(adj)
assert len(components)+empty == 2*h-2

V = (3,5)
assert {V,(4,6),(1,7),(4,4)} <= black
assert (2,8) not in points and (5,5) not in points
# V has two consecutive neighbors on its minus line, one on its plus line.
assert len(lines[("-",8)]) == 3
assert len(lines[("+",2)]) == 2

out = {
    "status":"PASS", "height":h, "width":m, "columns":columns,
    "rectangles":len(rectangles), "distinct_presentations":len(presentations),
    "components":components, "empty_diagonal_lines":empty,
    "components_plus_empty":len(components)+empty,
    "boundary_junction":{"vertex":V, "NE":(4,6), "NW":(1,7), "SE":(4,4),
                         "outside_completions":[(2,8),(5,5)]},
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps(out, indent=2))

