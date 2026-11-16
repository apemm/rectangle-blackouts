"""Targeted exact offset window for larger canonical Hilbert P systems.

This is a finite P-system experiment, not a board validity check.
"""
import argparse
from collections import defaultdict, Counter
import hashlib
import json
from pathlib import Path
import sys
import time

from check_all_offset_private_tiles import hilbert, vertical_legs, solve
from probe_private_tile_gain_cores import gains_from_events, peel, compact


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--side', type=int, default=32)
    parser.add_argument('--lo', type=int, default=-10000)
    parser.add_argument('--hi', type=int, default=10000)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    sys.setrecursionlimit(10000)
    started = time.monotonic()
    xy = hilbert(args.side)
    n = len(xy)
    data = defaultdict(list)
    for d in range(1, n):
        offsets = [(xy[r+d][1]-xy[r][0], xy[r][1]-xy[r+d][0])
                   for r in range(n-d)]
        for delta in range(-2, 3):
            ys = vertical_legs(32*(3*d+delta))
            halves = [(sign*y-1)//2 for y in ys for sign in (-1, 1)]
            halves = [half for half in halves
                      if args.lo-args.side < half < args.hi+args.side]
            for half in halves:
                for r, (oa, ob) in enumerate(offsets):
                    code = (r*n+r+d)*5+delta+2
                    for offset in (oa,) if oa == ob else (oa, ob):
                        t = half-offset
                        if args.lo <= t <= args.hi:
                            data[t].append(code)
        if d % 256 == 0:
            print(json.dumps({'generated_rank_gaps': d, 'offsets': len(data),
                              'seconds': round(time.monotonic()-started, 2)}), flush=True)
    stats = Counter()
    records = []
    digest = hashlib.sha256()
    for t, codes in sorted(data.items()):
        events = []
        for code in sorted(set(codes)):
            pair, rem = divmod(code, 5)
            r, s = divmod(pair, n)
            events.append((r, s, rem-2))
        digest.update(json.dumps([t, events], separators=(',', ':')).encode())
        stats['nonempty_offsets'] += 1
        stats['constraints'] += len(events)
        gains = gains_from_events(events)
        core, _ = peel(gains)
        if not core:
            stats['weighted_two_degenerate'] += 1
            continue
        stats['nonempty_core_offsets'] += 1
        vertices = sorted({v for pair in core for v in pair})
        stats['maximum_core_vertices'] = max(stats['maximum_core_vertices'], len(vertices))
        number = {v: i for i, v in enumerate(vertices)}
        core_events = [(number[r], number[s], g) for (r, s), gs in core.items() for g in gs]
        sol, nodes = solve(len(vertices), core_events, 3, True)
        stats['maximum_core_search_nodes'] = max(stats['maximum_core_search_nodes'], nodes)
        record = {'offset': t, 'core_vertices': len(vertices), 'core_edges': len(core),
                  'search_nodes': nodes, 'certified_solved': sol is not None}
        if sol is None:
            stats['certified_unsatisfiable'] += 1
            record.update(compact(core, xy))
            # The actual integer-choice relation is weaker than the modular one.
            actual = [(r, s, d) for r, s, d in events if r in number and s in number]
            actual = [(number[r], number[s], d) for r, s, d in actual]
            actual_sol, actual_nodes = solve(len(vertices), actual, 3, False)
            record['actual_integer_assignment'] = actual_sol
            record['actual_integer_search_nodes'] = actual_nodes
            stats['integer_unsatisfiable'] += int(actual_sol is None)
        else:
            stats['certified_solved_cores'] += 1
            record['vertices'] = vertices
            record['assignment'] = sol
        records.append(record)
        if len(records) % 50 == 0 or sol is None:
            print(json.dumps({'processed_offsets': stats['nonempty_offsets'],
                              'cores': len(records), 'latest': record['offset'],
                              'certified_unsat': stats['certified_unsatisfiable'],
                              'seconds': round(time.monotonic()-started, 2)}), flush=True)
    result = {'side': args.side, 'stride': 32, 'choices': 3,
              'offset_interval': [args.lo, args.hi], 'statistics': dict(stats),
              'constraint_sha256': digest.hexdigest(), 'cores': records,
              'seconds': round(time.monotonic()-started, 3)}
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ('statistics', 'seconds')}, indent=2), flush=True)


if __name__ == '__main__':
    main()
