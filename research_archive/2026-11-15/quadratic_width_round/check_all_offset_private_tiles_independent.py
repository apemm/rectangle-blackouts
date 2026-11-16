"""Independent complete-offset/certificate checker; no constraint solver.

Euclid parameters replace divisor generation. A low-digit rank decoder
replaces recursive coordinate concatenation. Nothing imports the producer.
"""
from collections import defaultdict
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path
import argparse
import json
import time


def rank_cell(side, rank):
    x = y = 0
    scale = 1
    remaining = rank
    while scale < side:
        rx = (remaining // 2) & 1
        ry = (remaining ^ rx) & 1
        if ry == 0:
            if rx:
                x = scale - 1 - x
                y = scale - 1 - y
            x, y = y, x
        x += scale * rx
        y += scale * ry
        remaining //= 4
        scale *= 2
    return x, y


def euclid_legs(max_x, stride):
    """All positive odd Y with X a positive stride multiple <=max_x."""
    legs = defaultdict(set)
    for u in range(2, max_x // 2 + 1):
        for v in range(1, min(u - 1, max_x // (2 * u)) + 1):
            if (u - v) % 2 == 0 or gcd(u, v) != 1:
                continue
            px = 2 * u * v
            py = u * u - v * v
            pl = u * u + v * v
            for odd_scale in range(1, max_x // px + 1, 2):
                x = px * odd_scale
                if x % stride:
                    continue
                y = py * odd_scale
                length = pl * odd_scale
                assert x * x + y * y == length * length
                assert y % 2 == length % 2 == 1
                legs[x].add(y)
    return legs


def independent_systems(side, stride, choices):
    cells = [rank_cell(side, r) for r in range(side * side)]
    assert len(set(cells)) == side * side
    n = len(cells)
    legs = euclid_legs(stride * (choices * (n - 1) + choices - 1), stride)
    systems = defaultdict(set)
    for r, (ir, jr) in enumerate(cells):
        for s in range(r + 1, n):
            js = cells[s][1]
            ii = cells[s][0]
            for delta in range(-choices + 1, choices):
                x = stride * (choices * (s - r) + delta)
                for y in legs[x]:
                    for signed_y in (y, -y):
                        # Directly solve 2T + 2j + 1 - 2i = signed_y.
                        for twice_base in (2 * js + 1 - 2 * ir,
                                           2 * jr + 1 - 2 * ii):
                            twice_t = signed_y - twice_base
                            assert twice_t % 2 == 0
                            systems[twice_t // 2].add((r, s, delta))
    return systems, cells, legs


def verify(path):
    start = time.monotonic()
    saved = json.loads(path.read_text())
    stats = saved['statistics']
    side, stride, choices = (stats[k] for k in ('side', 'stride', 'choices'))
    systems, cells, legs = independent_systems(side, stride, choices)
    assert len(systems) == stats['nonempty_offsets']
    assert not stats['unsatisfiable'] and stats['integer_only_solved'] == 0
    digest = sha256()
    zero_count = nonzero_count = edge_count = 0
    checked_keys = set()
    maximum_events = 0
    for t, event_set in sorted(systems.items()):
        events = sorted(event_set)
        digest.update(json.dumps([t, events], separators=(',', ':')).encode())
        maximum_events = max(maximum_events, len(events))
        if all(delta % choices for _, _, delta in events):
            assignment = [0] * (side * side)
            assert str(t) not in saved['certificates']
            zero_count += 1
        else:
            cert = saved['certificates'][str(t)]
            assert cert['kind'] == 'certified'
            assignment = list(map(int, cert['assignment']))
            checked_keys.add(str(t))
            nonzero_count += 1
        assert len(assignment) == side * side
        assert all(0 <= z < choices for z in assignment)
        for r, s, delta in events:
            assert (assignment[s] - assignment[r] - delta) % choices
            # Recheck each generated constraint by its defining norm.
            x = stride * (choices * (s - r) + delta)
            y1 = 2 * t + 2 * cells[s][1] + 1 - 2 * cells[r][0]
            y2 = 2 * t + 2 * cells[r][1] + 1 - 2 * cells[s][0]
            norms = (x * x + y1 * y1, x * x + y2 * y2)
            assert any(isqrt(z) ** 2 == z for z in norms)
            edge_count += 1
    assert checked_keys == set(saved['certificates'])
    assert zero_count == stats['constant_zero_offsets']
    assert nonzero_count == stats['certified_solved']
    assert maximum_events == stats['maximum_events']
    assert digest.hexdigest() == stats['constraint_sha256']
    # The swap/central reflection identity preserves r,s,delta.
    for t, events in systems.items():
        transformed_t = -t - 1
        for r, s, delta in events:
            x = stride * (choices * (s - r) + delta)
            ys = (2 * transformed_t + 1 + 2 * (cells[s][0] - cells[r][1]),
                  2 * transformed_t + 1 + 2 * (cells[r][0] - cells[s][1]))
            assert any(abs(y) in legs[x] for y in ys)
    return {
        'status': 'PASS', 'side': side, 'stride': stride, 'choices': choices,
        'nonempty_offsets': len(systems), 'constant_zero_offsets': zero_count,
        'certified_assignments': nonzero_count, 'checked_constraints': edge_count,
        'maximum_events': maximum_events, 'constraint_sha256': digest.hexdigest(),
        'certificate_file_sha256': sha256(path.read_bytes()).hexdigest(),
        'seconds': round(time.monotonic() - start, 3),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sides', nargs='+', type=int, default=[4, 8, 16])
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    folder = Path(__file__).resolve().parent
    results = []
    for side in args.sides:
        result = verify(folder / f'all_offset_private_tiles_side{side}.json')
        results.append(result)
        print(json.dumps(result), flush=True)
    if args.out:
        args.out.write_text(json.dumps({'results': results}, indent=2) + '\n')


if __name__ == '__main__':
    main()
