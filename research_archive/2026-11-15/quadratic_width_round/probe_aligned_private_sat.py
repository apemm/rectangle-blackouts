"""Solve the weighted 3-core of a saved exact aligned private system.

SAT output is checked directly against every core edge before it is saved.
UNSAT is only a solver report until an independently checked proof exists.
"""
from pathlib import Path
import argparse
import hashlib
import json
import sys
import threading
import time
import numpy as np

FOLDER = Path(__file__).resolve().parent
sys.path.insert(0, str(FOLDER / 'local_sat_dependencies'))
from pysat.solvers import Solver


def core(n, events, choices=3):
    alive = np.ones(len(events), dtype=bool)
    rounds = 0
    while True:
        e = events[alive]
        deg = np.bincount(e[:, 0], minlength=n) + np.bincount(e[:, 1], minlength=n)
        low = deg < choices
        kill = alive & (low[events[:, 0]] | low[events[:, 1]])
        if not np.any(kill):
            return np.flatnonzero(deg), e, rounds
        alive[kill] = False
        rounds += 1


def actual_delta_masks(side, offset, outer, events, choices=3):
    """Reconstruct actual integer deltas from defining squared norms."""
    xy = np.zeros((1, 2), dtype=np.int64)
    scale = 1
    while scale < side:
        z = np.empty((4 * len(xy), 2), dtype=np.int64)
        z[:len(xy)] = xy[:, ::-1]
        z[len(xy):2 * len(xy)] = xy + (0, scale)
        z[2 * len(xy):3 * len(xy)] = xy + (scale, scale)
        z[3 * len(xy):, 0] = 2 * scale - 1 - xy[:, 1]
        z[3 * len(xy):, 1] = scale - 1 - xy[:, 0]
        xy = z
        scale *= 2
    if outer & 1:
        xy = xy[:, ::-1]
    if outer & 2:
        xy = side - 1 - xy
    r, s, g = events.T
    y0 = 2 * offset + 1 + 2 * (xy[s, 1] - xy[r, 0])
    y1 = 2 * offset + 1 + 2 * (xy[r, 1] - xy[s, 0])
    lag = (s - r).astype(np.int64)

    def is_square(v):
        root = np.sqrt(v).astype(np.int64)
        # Exact integer comparisons remove floating-point roundoff.
        return ((root * root == v) | ((root + 1) ** 2 == v)
                | ((root - 1) ** 2 == v))

    masks = []
    for delta in (g, np.where(g == 0, 0, g - choices)):
        x = 32 * (choices * lag + delta)
        masks.append(is_square(x * x + y0 * y0) | is_square(x * x + y1 * y1))
    assert np.all(masks[0] | masks[1])
    return masks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('events', type=Path)
    ap.add_argument('--side', type=int, required=True)
    ap.add_argument('--conflicts', type=int, default=20000)
    ap.add_argument('--solver', default='g4')
    ap.add_argument('--seconds', type=float, default=120)
    ap.add_argument('--integer', action='store_true')
    ap.add_argument('--offset', type=int)
    ap.add_argument('--outer', type=int, default=0)
    ap.add_argument('--choices', type=int, default=3)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    started = time.monotonic()
    events = np.load(args.events)
    n = args.side * args.side
    choices = args.choices
    vertices, ce, rounds = core(n, events, choices)
    result = {'side': args.side, 'events_file': args.events.name,
              'choices': choices,
              'events': len(events), 'core_vertices': len(vertices),
              'core_events': len(ce), 'peeling_rounds': rounds,
              'solver': args.solver, 'conflict_budget': args.conflicts,
              'seconds_budget': args.seconds,
              'constraint_model': 'actual_integer_differences' if args.integer else 'certified_modular',
              'event_sha256': hashlib.sha256(events.astype('<i4', copy=False).tobytes()).hexdigest()}
    print(json.dumps({'stage': 'core', **result}), flush=True)
    if not len(vertices):
        result['status'] = 'EMPTY_CORE'
        result['seconds'] = round(time.monotonic() - started, 3)
        args.out.write_text(json.dumps(result, indent=2) + '\n')
        return
    index = np.full(n, -1, dtype=np.int32)
    index[vertices] = np.arange(len(vertices), dtype=np.int32)
    if args.integer:
        assert args.offset is not None
        delta_masks = actual_delta_masks(args.side, args.offset, args.outer, ce, choices)
    with Solver(name=args.solver) as sat:
        for i in range(len(vertices)):
            x = choices * i + 1
            sat.add_clause([x + c for c in range(choices)])
            for c in range(choices):
                for d in range(c + 1, choices):
                    sat.add_clause([-x - c, -x - d])
        if not args.integer:
            sat.add_clause([1])  # Cyclic translation holds only for modular constraints.
        for event_index, (u, v, gain) in enumerate(ce):
            a = choices * int(index[u]) + 1
            b = choices * int(index[v]) + 1
            g = int(gain)
            for color in range(choices):
                other = (color + g) % choices
                actual_delta = other - color
                if (not args.integer or
                        delta_masks[0 if actual_delta == g else 1][event_index]):
                    sat.add_clause([-a - color, -b - other])
        sat.conf_budget(args.conflicts)
        timer = threading.Timer(args.seconds, sat.interrupt)
        timer.daemon = True
        timer.start()
        try:
            answer = sat.solve_limited(expect_interrupt=True)
        finally:
            timer.cancel()
        result['solver_stats'] = sat.accum_stats()
        if answer is True:
            model = sat.get_model()
            colors = np.full(len(vertices), -1, dtype=np.int8)
            for literal in model:
                if literal > 0 and literal <= choices * len(vertices):
                    colors[(literal - 1) // choices] = (literal - 1) % choices
            assert np.all(colors >= 0)
            actual = colors[index[ce[:, 1]]] - colors[index[ce[:, 0]]]
            modular_hit = (actual - ce[:, 2]) % choices == 0
            if args.integer:
                mask = np.where(actual == ce[:, 2], delta_masks[0], delta_masks[1])
                assert not np.any(modular_hit & mask)
            else:
                assert not np.any(modular_hit)
            cert = args.out.with_suffix('.npz')
            np.savez_compressed(cert, vertices=vertices.astype(np.int32), colors=colors)
            result['status'] = 'SAT_DIRECTLY_CHECKED_CORE'
            result['certificate'] = cert.name
        elif answer is False:
            result['status'] = 'UNSAT_SOLVER_REPORT_NOT_INDEPENDENTLY_PROVED'
        else:
            result['status'] = 'UNKNOWN_CONFLICT_OR_TIME_BUDGET'
    result['seconds'] = round(time.monotonic() - started, 3)
    args.out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
