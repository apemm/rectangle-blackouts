"""Color the normalized Hilbert graph and audit its edges by a separate enumeration."""
import json
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path
import sys

import numpy as np
from numba import njit

from check_unit_stride import coords
from integer_star import enumerate_lag, odd_legs

HERE = Path(__file__).resolve().parent


def edges(side, stride):
    n = side * side
    chunks = []
    for lag, y in odd_legs(6 * (side - 1) + 1, stride, n - 1):
        for signed in (y, -y):
            if signed % 6 != 1:
                continue
            delta = (signed - 1) // 6
            for role in (0, 1):
                hits = enumerate_lag(side, lag, delta, role)
                if hits:
                    r = np.asarray(hits, dtype=np.int64)
                    chunks.append(r*n + r + lag)
    if not chunks:
        return np.empty((0, 2), dtype=np.int32)
    keys = np.unique(np.concatenate(chunks))
    return np.column_stack((keys // n, keys % n)).astype(np.int32)


@njit(cache=False)
def color(n, pairs):
    offsets = np.zeros(n + 1, np.int64)
    for a, b in pairs:
        offsets[a + 1] += 1
        offsets[b + 1] += 1
    offsets = np.cumsum(offsets)
    degree = offsets[1:] - offsets[:-1]
    cursor = offsets[:-1].copy()
    neighbors = np.empty(2 * len(pairs), np.int32)
    for a, b in pairs:
        neighbors[cursor[a]] = b
        neighbors[cursor[b]] = a
        cursor[a] += 1
        cursor[b] += 1
    queue = np.empty(n, np.int32)
    head = tail = 0
    for a in range(n):
        if degree[a] < 3:
            queue[tail] = a
            tail += 1
    while head < tail:
        a = queue[head]
        head += 1
        for k in range(offsets[a], offsets[a + 1]):
            b = neighbors[k]
            degree[b] -= 1
            if degree[b] == 2:
                queue[tail] = b
                tail += 1
    colors = np.full(n, -1, np.int8)
    if tail == n:
        for a in queue[::-1]:
            available = 7
            for k in range(offsets[a], offsets[a + 1]):
                c = colors[neighbors[k]]
                if c >= 0:
                    available &= ~(1 << c)
            assert available
            colors[a] = 0 if available & 1 else (1 if available & 2 else 2)
    return n - tail, colors


def euclidean_lags(side, stride):
    limit = 6 * (side - 1) + 1
    lags = {}
    for u in range(2, (limit + 1) // 2 + 1):
        for v in range(max(1, isqrt(max(0, u*u - limit))), u):
            if (u - v) % 2 == 0 or gcd(u, v) != 1:
                continue
            base = u*u - v*v
            for scale in range(1, limit // base + 1, 2):
                x, y = 2*scale*u*v, scale*base
                if x % stride == 0 and x // stride < side*side and y % 3:
                    lags.setdefault(x // stride, set()).add(y)
    return lags


@njit(cache=False)
def scan(lag, table, i, j, colors):
    total = bad = 0
    for u in range(len(colors) - lag):
        v = u + lag
        if (table[abs(6*(j[u] - i[v]) + 1)] or
                table[abs(6*(j[v] - i[u]) + 1)]):
            total += 1
            if colors[u] == colors[v]:
                bad += 1
    return total, bad


def main():
    stride = int(sys.argv[1])
    assert stride > 8 and stride % 12 == 0
    for side in map(int, sys.argv[2:]):
        assert side > 0 and side & (side - 1) == 0
        graph = edges(side, stride)
        core, colors = color(side*side, graph)
        record = dict(side=side, stride=stride, edges=len(graph), three_core=int(core))
        if core == 0:
            i, j = coords(side)
            assert len(np.unique(i.astype(np.int64)*side + j)) == side*side
            total = bad = 0
            table = np.zeros(6*(side - 1) + 2, np.bool_)
            for lag, ys in euclidean_lags(side, stride).items():
                idx = list(ys)
                table[idx] = True
                a, b = scan(lag, table, i, j, colors)
                total += a
                bad += b
                table[idx] = False
            assert total == len(graph) and bad == 0
            record.update(independent_edges=total, monochromatic=bad,
                          sha256=sha256(colors.tobytes()).hexdigest())
        print(json.dumps(record), flush=True)
        (HERE / f'ternary_graph_{stride}_{side}.json').write_text(
            json.dumps(record, indent=2) + '\n')


if __name__ == '__main__':
    main()
