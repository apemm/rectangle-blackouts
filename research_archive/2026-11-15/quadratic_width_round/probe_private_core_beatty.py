"""Exact open Beatty-interval test for the six saved weighted cores."""
from fractions import Fraction as F
from pathlib import Path
import json


def beatty_intervals(constraints):
    intervals = [(F(0), F(1))]
    for d, gain in sorted(constraints):
        allowed = []
        for k in range(-1, d + 1):
            left, right = F(3 * k + gain + 1, 3 * d), F(3 * k + gain + 2, 3 * d)
            if right > 0 and left < 1:
                allowed.append((max(F(0), left), min(F(1), right)))
        new = []
        i = j = 0
        while i < len(intervals) and j < len(allowed):
            lo = max(intervals[i][0], allowed[j][0])
            hi = min(intervals[i][1], allowed[j][1])
            if lo < hi:
                new.append((lo, hi))
            if intervals[i][1] < allowed[j][1]:
                i += 1
            else:
                j += 1
        intervals = new
        if not intervals:
            return []
    return intervals


def main():
    folder = Path(__file__).resolve().parent
    data = json.loads((folder / 'private_tile_gain_cores_side16.json').read_text())
    result = []
    for item in data['small_final_cores']:
        vertices = item['vertices']
        constraints = {(vertices[j] - vertices[i], gain)
                       for i, j, gains in item['edges'] for gain in gains}
        intervals = beatty_intervals(constraints)
        entry = {'offset': item['offset'], 'gap_gains': sorted(constraints),
                 'open_intervals': [[str(x), str(y)] for x, y in intervals]}
        if intervals:
            tau = sum(intervals[0]) / 2
            assignment = [int(3 * tau * r) % 3 for r in vertices]
            assert all((assignment[j] - assignment[i]) % 3 not in gains
                       for i, j, gains in item['edges'])
            entry.update(tau=str(tau), assignment=assignment)
        result.append(entry)
    (folder / 'private_core_beatty.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
