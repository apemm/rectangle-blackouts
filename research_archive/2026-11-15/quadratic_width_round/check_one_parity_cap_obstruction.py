"""Exact ancestor check for the one-parity first-cap obstruction."""
import json
from pathlib import Path
from check_four_block_obstruction import point, rank


def check(N):
    n = N // 2
    checked = 0
    for k in range(1, n):
        r = rank(N, n - 1, k)
        assert tuple(reversed(point(N, r))) == (k, n - 1)
        length = 4
        while length <= N * N:
            start = r // length * length
            p = tuple(reversed(point(N, start)))
            q = tuple(reversed(point(N, start + length - 1)))
            role = 0 if p[0] == q[0] else 1
            assert p[role] == q[role]
            assert role == (0 if length == N * N else 1)
            length *= 4
        checked += 1
    return dict(side=N, checked_bad_coordinates=checked)


if __name__ == '__main__':
    cases = [check(2 ** e) for e in range(2, 11)]
    result = dict(status='PASS', cases=cases,
                  scope='first eligible odd-axis ancestor rule only')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2))
    print(json.dumps(result))
