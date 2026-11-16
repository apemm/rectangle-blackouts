"""Exact finite private-slot systems over every integer coordinate offset.

This concerns candidate P constraints only. It does not fill the other
columns or verify complete blackout validity. Factorization generates
every offset with a nonempty system, without a height cutoff.
"""
import argparse
from collections import defaultdict, deque
import hashlib
import json
from math import isqrt
from pathlib import Path
import time


def hilbert(side):
    xy = [(0, 0)]
    n = 1
    while n < side:
        xy = ([(y, x) for x, y in xy]
              + [(x, y+n) for x, y in xy]
              + [(x+n, y+n) for x, y in xy]
              + [(2*n-1-y, n-1-x) for x, y in xy])
        n *= 2
    assert n == side
    return xy


def square_divisors(q):
    factors = []
    p = 2
    while p*p <= q:
        e = 0
        while q % p == 0:
            q //= p
            e += 1
        if e:
            factors.append((p, 2*e))
        p = 3 if p == 2 else p+2
    if q > 1:
        factors.append((q, 2))
    ds = [1]
    for p, e in factors:
        old = ds[:]
        power = 1
        for _ in range(e):
            power *= p
            ds.extend(d*power for d in old)
    return ds


def vertical_legs(x):
    assert x > 0 and x % 4 == 0
    q = x//2
    sq = q*q
    ys = []
    for r in square_divisors(q):
        if r >= q:
            continue
        s = sq//r
        if (s-r) % 2:
            y = s-r
            assert x*x+y*y == (r+s)**2
            ys.append(y)
    return ys


def systems(side, stride, choices):
    xy = hilbert(side)
    n = len(xy)
    out = defaultdict(set)
    for d in range(1, n):
        for delta in range(1-choices, choices):
            x = stride*(choices*d+delta)
            ys = vertical_legs(x)
            for r in range(n-d):
                s = r+d
                offsets = {xy[s][1]-xy[r][0], xy[r][1]-xy[s][0]}
                for y in ys:
                    for sign in (-1, 1):
                        half = (sign*y-1)//2
                        for offset in offsets:
                            out[half-offset].add((r, s, delta))
    return out


def solve(n, events, choices, certified):
    """Finite-domain AC-3 search. A returned assignment is rechecked."""
    masks = defaultdict(lambda: [((1 << choices)-1) for _ in range(choices)])
    for r, s, delta in events:
        forward = masks[r, s]
        backward = masks[s, r]
        for a in range(choices):
            for b in range(choices):
                bad = ((b-a-delta) % choices == 0) if certified else (b-a == delta)
                if bad:
                    forward[a] &= ~(1 << b)
                    backward[b] &= ~(1 << a)
    neighbors = [[] for _ in range(n)]
    for r, s in masks:
        neighbors[r].append(s)
    nodes = 0

    def propagate(dom, queue):
        while queue:
            r, s = queue.popleft()
            nr = 0
            for a in range(choices):
                if dom[r] & (1 << a) and masks[r, s][a] & dom[s]:
                    nr |= 1 << a
            if not nr:
                return False
            if nr != dom[r]:
                dom[r] = nr
                queue.extend((t, r) for t in neighbors[r] if t != s)
        return True

    def search(dom, queue):
        nonlocal nodes
        nodes += 1
        if not propagate(dom, queue):
            return None
        remaining = [v for v in range(n) if dom[v].bit_count() > 1 and neighbors[v]]
        if not remaining:
            return [(d & -d).bit_length()-1 for d in dom]
        v = min(remaining, key=lambda r: (dom[r].bit_count(), -len(neighbors[r])))
        for c in range(choices):
            if dom[v] & (1 << c):
                nxt = dom[:]
                nxt[v] = 1 << c
                sol = search(nxt, deque((t, v) for t in neighbors[v]))
                if sol is not None:
                    return sol
        return None

    sol = search([(1 << choices)-1]*n, deque(masks))
    if sol is not None:
        for r, s, d in events:
            assert ((sol[s]-sol[r]-d) % choices != 0) if certified else (sol[s]-sol[r] != d)
    return sol, nodes


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--side', type=int, default=4)
    p.add_argument('--stride', type=int, default=32)
    p.add_argument('--choices', type=int, default=3)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    start = time.monotonic()
    data = systems(args.side, args.stride, args.choices)
    print(json.dumps({'generated_offsets': len(data), 'seconds': time.monotonic()-start}), flush=True)
    stats = {'side': args.side, 'stride': args.stride, 'choices': args.choices,
             'nonempty_offsets': len(data), 'constant_zero_offsets': 0,
             'certified_solved': 0, 'integer_only_solved': 0,
             'unsatisfiable': [], 'maximum_events': 0, 'maximum_search_nodes': 0}
    certs = {}
    digest = hashlib.sha256()
    for ix, (offset, events) in enumerate(sorted(data.items())):
        edges = sorted(events)
        digest.update(json.dumps([offset, edges], separators=(',', ':')).encode())
        stats['maximum_events'] = max(stats['maximum_events'], len(edges))
        if all(d % args.choices for _, _, d in edges):
            stats['constant_zero_offsets'] += 1
            continue
        sol, nodes = solve(args.side**2, edges, args.choices, True)
        kind = 'certified'
        if sol is None:
            sol, more = solve(args.side**2, edges, args.choices, False)
            nodes += more
            kind = 'integer'
        stats['maximum_search_nodes'] = max(stats['maximum_search_nodes'], nodes)
        if sol is None:
            stats['unsatisfiable'].append({'offset': offset, 'events': edges})
        else:
            stats['certified_solved' if kind == 'certified' else 'integer_only_solved'] += 1
            certs[str(offset)] = {'kind': kind, 'assignment': ''.join(map(str, sol))}
        if ix % 5000 == 0:
            print(json.dumps({'processed': ix+1, 'seconds': time.monotonic()-start,
                              'integer_only': stats['integer_only_solved'],
                              'unsat': len(stats['unsatisfiable'])}), flush=True)
    stats['constraint_sha256'] = digest.hexdigest()
    stats['seconds'] = time.monotonic()-start
    args.out.write_text(json.dumps({'statistics': stats, 'certificates': certs}, indent=2)+'\n')
    print(json.dumps(stats), flush=True)


if __name__ == '__main__':
    main()
