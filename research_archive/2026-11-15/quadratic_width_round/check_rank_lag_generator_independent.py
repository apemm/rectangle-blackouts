"""Independent direct-pair and Euclid/vector audits of the rank-lag generator.

This writes only its own audit summary when run as a script.  No producer
geometry or Pythagorean generator is reused by the reference routines.
"""
from math import gcd, isqrt
from pathlib import Path
import importlib.util
import json
import time
import numpy as np


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'rank_lag_producer', HERE / 'probe_hilbert_rank_difference_automaton.py')
producer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(producer)


def coordinate_vectors(side, outer):
    """The independent rotate/add Hilbert inversion on all rank values."""
    ranks = np.arange(side * side, dtype=np.int64)
    work = ranks.copy()
    x = np.zeros_like(ranks)
    y = np.zeros_like(ranks)
    scale = 1
    while scale < side:
        rx = (work // 2) & 1
        ry = (work ^ rx) & 1
        reflected = (ry == 0) & (rx == 1)
        x = np.where(reflected, scale - 1 - x, x)
        y = np.where(reflected, scale - 1 - y, y)
        swapped = (ry == 0)
        x, y = np.where(swapped, y, x), np.where(swapped, x, y)
        x += scale * rx
        y += scale * ry
        scale *= 2
        work //= 4
    if outer & 1:
        x, y = y, x
    if outer & 2:
        x, y = side - 1 - x, side - 1 - y
    return x, y


def direct_pairs(side, offset, outer, stride=32, choices=3):
    x, y = coordinate_vectors(side, outer)
    events = set()
    for r in range(side * side):
        for s in range(r + 1, side * side):
            for delta in range(1 - choices, choices):
                horizontal = stride * (choices * (s-r) + delta)
                for k in (int(y[s]-x[r]), int(y[r]-x[s])):
                    vertical = 2 * offset + 1 + 2 * k
                    norm = horizontal * horizontal + vertical * vertical
                    root = isqrt(norm)
                    if root * root == norm:
                        events.add((r, s, delta % choices))
    return events


def euclidean_vectors(side, offset, outer, stride=32, choices=3):
    x, y = coordinate_vectors(side, outer)
    size = side * side
    ymax = abs(2 * offset + 1) + 2 * (side - 1)
    qmax = choices * (size - 1) + choices - 1
    legs = set()
    # An odd vertical leg has primitive form m^2-n^2, with odd scale.
    # m^2-n^2 >= 2m-1 gives the complete finite m bound below.
    for m in range(2, (ymax + 1) // 2 + 1):
        for n in range(1, m):
            if (m-n) % 2 == 0 or gcd(m, n) != 1:
                continue
            yy, xx = m*m-n*n, 2*m*n
            if yy > ymax:
                continue
            for factor in range(1, ymax // yy + 1, 2):
                horizontal = factor * xx
                if horizontal % stride == 0:
                    q = horizontal // stride
                    if q <= qmax:
                        legs.add((q, factor * yy))
    events = set()
    for q, vertical in legs:
        for delta in range(1 - choices, choices):
            if (q-delta) % choices:
                continue
            lag = (q-delta) // choices
            if not 0 < lag < size:
                continue
            for signed in (-vertical, vertical):
                target = (signed - 2 * offset - 1) // 2
                if abs(target) >= side:
                    continue
                for values in (y[lag:] - x[:-lag], y[:-lag] - x[lag:]):
                    sources = np.flatnonzero(values == target)
                    events.update((int(r), int(r)+lag, delta % choices)
                                  for r in sources)
    return events, len(legs)


def audit():
    start = time.monotonic()
    records = []
    # Direct squared-distance checks use every pair and every integer delta.
    for side, offset in ((4,-4), (4,0), (4,4), (8,-8), (8,8), (16,-16)):
        for outer in range(4):
            exact = direct_pairs(side, offset, outer)
            generated, metadata = producer.build(side, offset, outer=outer)
            assert exact == set(generated), (side, offset, outer)
            independent, _ = euclidean_vectors(side, offset, outer)
            assert exact == independent
            records.append(dict(method='all pairs / integer squared norms',
                                **metadata))
    # Larger systems use an independent Euclidean parametrization and vectors.
    for side, offset, outer in ((32,-32,0), (64,-64,0), (64,64,3),
                                (128,-128,0), (256,-256,0), (256,256,1)):
        exact, norms = euclidean_vectors(side, offset, outer)
        generated, metadata = producer.build(side, offset, outer=outer)
        assert exact == set(generated), (side, offset, outer)
        records.append(dict(method='Euclidean triples / direct coordinate vectors',
                            reference_norms=norms, **metadata))
    return dict(status='PASS', complete_systems=len(records), cases=records,
                seconds=round(time.monotonic()-start,3),
                scope='Complete certified modular constraints. Integer choice deltas '
                      'are tested before reduction modulo the palette size.')


if __name__ == '__main__':
    result = audit()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'cases'}))
