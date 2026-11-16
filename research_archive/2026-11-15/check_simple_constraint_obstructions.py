"""Check the two abstract small obstructions by integer assignments."""
from itertools import combinations, product
import json

k4 = sum(all(values[j] - values[i] != 0 for i, j in combinations(range(4), 2))
         for values in product(range(3), repeat=4))
forbidden = [({0, 2}, {0, 1}), ({0, 1}, {-1, 0}), ({0, 1}, {-2, -1})]
k23 = 0
for a, b, c1, c2, c3 in product(range(3), repeat=5):
    if all(c - a not in left and c - b not in right
           for c, (left, right) in zip((c1, c2, c3), forbidden)):
        k23 += 1
assert k4 == k23 == 0
print(json.dumps({"status": "PASS", "K4_assignments_tested": 81,
                  "K23_assignments_tested": 243,
                  "K4_solutions": k4, "K23_solutions": k23}))
