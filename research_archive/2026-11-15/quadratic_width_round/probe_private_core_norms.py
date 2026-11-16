from collections import Counter
from math import isqrt
from pathlib import Path
import json

folder = Path(__file__).resolve().parent
data = json.loads((folder / 'private_tile_gain_cores_side16.json').read_text())
results = []
for item in data['small_final_cores']:
    counts = Counter()
    for u, v, gains in item['edges']:
        r, s = item['vertices'][u], item['vertices'][v]
        ir, jr = item['cells'][u]
        ii, js = item['cells'][v]
        for delta in range(-2, 3):
            if delta % 3 not in gains:
                continue
            q = 3 * (s - r) + delta
            x = 32 * q
            for y in {abs(2 * item['offset'] + 1 + 2 * (js - ir)),
                      abs(2 * item['offset'] + 1 + 2 * (jr - ii))}:
                length = isqrt(x * x + y * y)
                if length * length == x * x + y * y:
                    counts[q, y, (length - y) // 2] += 1
    results.append({'offset': item['offset'],
                    'norms': [{'q': q, 'Y': y, 'half_factor': a, 'count': count}
                              for (q, y, a), count in sorted(counts.items())]})
(folder / 'private_core_norms.json').write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps(results, indent=2))
