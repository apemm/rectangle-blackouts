"""Independent Euclid generation and greedy certificate extension.

No constraint solver or producer module is imported.
"""
from collections import defaultdict, deque
from hashlib import sha256
import json
from pathlib import Path
import time

from check_all_offset_private_tiles_independent import euclid_legs, rank_cell


def verify(path):
    started = time.monotonic()
    saved = json.loads(path.read_text())
    side, stride, choices = (saved[k] for k in ('side', 'stride', 'choices'))
    n = side * side
    low, high = saved['offset_interval']
    cells = [rank_cell(side, r) for r in range(n)]
    legs = euclid_legs(stride * (choices*n-1), stride)
    by_offset = defaultdict(list)
    for gap in range(1, n):
        for delta in range(1-choices, choices):
            x = stride * (choices*gap+delta)
            candidates = []
            for y in legs[x]:
                for sign in (-1, 1):
                    base = (sign*y-1)//2
                    if low-side < base < high+side:
                        candidates.append(base)
            for base in candidates:
                for r in range(n-gap):
                    s = r+gap
                    code = (r*n+s)*(2*choices-1)+delta+choices-1
                    for offset in {cells[s][1]-cells[r][0], cells[r][1]-cells[s][0]}:
                        t = base-offset
                        if low <= t <= high:
                            by_offset[t].append(code)
    certificates = {item['offset']: item for item in saved['cores']}
    digest = sha256()
    checked = core_count = 0
    for t, codes in sorted(by_offset.items()):
        events = []
        adjacency = defaultdict(lambda: defaultdict(set))
        for code in sorted(set(codes)):
            pair, rem = divmod(code, 2*choices-1)
            r, s = divmod(pair, n)
            delta = rem-choices+1
            events.append((r, s, delta))
            adjacency[r][s].add(delta % choices)
            adjacency[s][r].add((-delta) % choices)
        digest.update(json.dumps([t, events], separators=(',', ':')).encode())
        degree = {v: sum(len(gs) for gs in row.values()) for v, row in adjacency.items()}
        remaining = set(degree)
        queue = deque(v for v, d in degree.items() if d < choices)
        removed = []
        while queue:
            v = queue.popleft()
            if v not in remaining:
                continue
            remaining.remove(v)
            removed.append(v)
            for w, gs in adjacency[v].items():
                if w in remaining:
                    degree[w] -= len(gs)
                    if degree[w] < choices:
                        queue.append(w)
        values = {}
        if remaining:
            cert = certificates.pop(t)
            assert cert['certified_solved']
            assert sorted(remaining) == cert['vertices']
            assert len(cert['assignment']) == len(remaining)
            values.update(zip(cert['vertices'], cert['assignment']))
            core_count += 1
        else:
            assert t not in certificates
        for v in reversed(removed):
            forbidden = {(values[w]-g) % choices
                         for w, gs in adjacency[v].items() if w in values for g in gs}
            values[v] = min(set(range(choices))-forbidden)
        assert all(0 <= value < choices for value in values.values())
        for r, s, delta in events:
            assert (values[s]-values[r]-delta) % choices != 0
        checked += len(events)
    assert not certificates
    assert digest.hexdigest() == saved['constraint_sha256']
    assert checked == saved['statistics']['constraints']
    assert len(by_offset) == saved['statistics']['nonempty_offsets']
    assert core_count == saved['statistics']['nonempty_core_offsets']
    return {'status': 'PASS', 'side': side, 'offset_interval': [low, high],
            'checked_offsets': len(by_offset), 'checked_constraints': checked,
            'checked_core_assignments': core_count,
            'constraint_sha256': digest.hexdigest(),
            'seconds': round(time.monotonic()-started, 3)}


if __name__ == '__main__':
    folder = Path(__file__).resolve().parent
    results = []
    for side in (32, 64):
        result = verify(folder / f'private_tiles_offset_window_side{side}.json')
        results.append(result)
        print(json.dumps(result), flush=True)
    (folder / 'private_tile_offset_windows_independent.json').write_text(
        json.dumps(results, indent=2)+'\n')
