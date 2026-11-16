"""Supplementary exhaustive check of the three-label integer lemma."""
from itertools import combinations, product
import json

sets = [set(c) for size in (0, 1, 2) for c in combinations(range(-2, 3), size)]
count = 0
for ab, ac, bc in product(sets, repeat=3):
    assert any(b - a not in ab and c - a not in ac and c - b not in bc
               for a, b, c in product(range(3), repeat=3))
    count += 1
print(json.dumps({"status": "PASS", "systems": count}))
