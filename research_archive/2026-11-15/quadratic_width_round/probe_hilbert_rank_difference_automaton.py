"""Exact Hilbert rank-lag enumeration by a bounded-width digit automaton.

This is an experimental constraint generator, not a solvability proof.
No producer is imported. Hilbert coordinates are checked independently.
"""
from functools import lru_cache
from math import isqrt
from pathlib import Path
import argparse
import hashlib
import json
import time


def action(g, x, y, top):
    if g & 1:
        x, y = y, x
    if g & 2:
        x, y = top - x, top - y
    return x, y


QPOS = ((0, 0), (0, 1), (1, 1), (1, 0))
QROT = (1, 0, 0, 3)
# Current state is the orientation below this digit. The output state is
# the parent orientation. The final parent is the requested outer one.
STEP = tuple(tuple((g ^ QROT[q], *action(g ^ QROT[q], *QPOS[q], 1))
                   for q in range(4)) for g in range(4))


def cell(side, rank):
    x = y = 0
    level = 1
    while level < side:
        q = rank % 4
        rank //= 4
        if q == 0:
            x, y = y, x
        elif q == 1:
            y += level
        elif q == 2:
            x += level
            y += level
        else:
            x, y = 2 * level - 1 - y, level - 1 - x
        level *= 2
    return x, y


def enumerate_lag(side, lag, difference, role=0, outer=0, counts_only=False):
    """r with s=r+lag, and y_s-x_r=difference (role0) or y_r-x_s.

    Carries contain the unprocessed signed constant, rather than a
    separately stored digit sequence. Initial orientations are free;
    the terminal outer orientation fixes them uniquely for each rank.
    """
    assert side > 0 and side & (side - 1) == 0
    depth = side.bit_length() - 1
    if not 0 < lag < side * side or abs(difference) >= side:
        return (0, 0) if counts_only else []

    @lru_cache(None)
    def count(level, gr, gs, rank_carry, row_carry):
        if level == depth:
            return int(gr == gs == outer and rank_carry == row_carry == 0)
        answer = 0
        for qr in range(4):
            qs = (qr + rank_carry) % 4
            nc = (qr + rank_carry) // 4
            nr, xr, yr = STEP[gr][qr]
            ns, xs, ys = STEP[gs][qs]
            residual = (xr + row_carry - ys if role == 0
                        else xs + row_carry - yr)
            if residual % 2 == 0:
                answer += count(level + 1, nr, ns, nc, residual // 2)
        return answer

    total = sum(count(0, gr, gs, lag, difference)
                for gr in range(4) for gs in range(4))
    if counts_only:
        return total, count.cache_info().currsize

    found = []

    def descend(level, gr, gs, rank_carry, row_carry, prefix):
        if level == depth:
            found.append(prefix)
            return
        for qr in range(4):
            qs = (qr + rank_carry) % 4
            nc = (qr + rank_carry) // 4
            nr, xr, yr = STEP[gr][qr]
            ns, xs, ys = STEP[gs][qs]
            residual = (xr + row_carry - ys if role == 0
                        else xs + row_carry - yr)
            if residual % 2 == 0 and count(level + 1, nr, ns, nc, residual // 2):
                descend(level + 1, nr, ns, nc, residual // 2,
                        prefix + (qr << (2 * level)))

    for gr in range(4):
        for gs in range(4):
            if count(0, gr, gs, lag, difference):
                descend(0, gr, gs, lag, difference, 0)
    assert len(found) == total
    return found


def self_check(max_side):
    start = time.monotonic()
    cases = matches = 0
    for side in (2, 4, 8, 16):
        if side > max_side:
            continue
        canonical = [cell(side, r) for r in range(side * side)]
        for outer in range(4):
            xy = [action(outer, *p, side - 1) for p in canonical]
            for lag in range(1, side * side):
                for role in range(2):
                    expected = {}
                    for r in range(side * side - lag):
                        s = r + lag
                        k = (xy[s][1] - xy[r][0] if role == 0
                             else xy[r][1] - xy[s][0])
                        expected.setdefault(k, []).append(r)
                    for k in range(1 - side, side):
                        got = sorted(enumerate_lag(side, lag, k, role, outer))
                        assert got == expected.get(k, []), (side, outer, lag, role, k)
                        cases += 1
                        matches += len(got)
    return {'status': 'PASS', 'max_side': max_side, 'cases': cases,
            'matches': matches, 'seconds': round(time.monotonic() - start, 3)}


def odd_legs(limit, stride, max_q):
    spf = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == p:
            for q in range(p * p, limit + 1, p):
                if spf[q] == q:
                    spf[q] = p
    for y in range(1, limit + 1, 2):
        z = y
        divisors = [1]
        while z > 1:
            p = spf[z]
            e = 0
            while z % p == 0:
                e += 1
                z //= p
            old = divisors[:]
            power = 1
            for _ in range(2 * e):
                power *= p
                divisors.extend(v * power for v in old)
        for a in divisors:
            if a >= y:
                continue
            x = (y * y // a - a) // 2
            if x % stride == 0 and 0 < x // stride <= max_q:
                yield x // stride, y


def build(side, offset, stride=32, choices=3, outer=0, as_array=False):
    n = side * side
    ymax = max(abs(2 * offset + 1 - 2 * (side - 1)),
               abs(2 * offset + 1 + 2 * (side - 1)))
    events = set()
    tests = norms = 0
    start = time.monotonic()
    for q, y in odd_legs(ymax, stride, choices * (n - 1) + choices - 1):
        norms += 1
        for signed_y in (y, -y):
            k = (signed_y - 2 * offset - 1) // 2
            if abs(k) >= side:
                continue
            for lag in {q // choices, (q + choices - 1) // choices}:
                delta = q - choices * lag
                for role in range(2):
                    tests += 1
                    for r in enumerate_lag(side, lag, k, role, outer):
                        if as_array:
                            events.add(((r * n + r + lag) * choices) + delta % choices)
                        else:
                            events.add((r, r + lag, delta % choices))
    if as_array:
        import numpy as np
        packed = np.fromiter(events, dtype=np.uint64, count=len(events))
        del events
        packed.sort()
        events = np.empty((len(packed), 3), dtype=np.int32)
        events[:, 2] = packed % choices
        packed //= choices
        events[:, 1] = packed % n
        events[:, 0] = packed // n
        digest = hashlib.sha256(events.astype('<i4', copy=False).tobytes()).hexdigest()
    else:
        events = sorted(events)
        digest = hashlib.sha256(json.dumps(events, separators=(',', ':')).encode()).hexdigest()
    return events, {'side': side, 'offset': offset, 'stride': stride,
                    'choices': choices, 'outer': outer, 'events': len(events),
                    'norms': norms, 'automata': tests, 'sha256': digest,
                    'digest_format': 'little_endian_int32_triples' if as_array else 'compact_json',
                    'seconds': round(time.monotonic() - start, 3)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', type=int)
    ap.add_argument('--side', type=int, default=64)
    ap.add_argument('--offset', type=int)
    ap.add_argument('--outer', type=int, default=0)
    ap.add_argument('--choices', type=int, default=3)
    ap.add_argument('--out', type=Path)
    ap.add_argument('--events', type=Path)
    ap.add_argument('--array', action='store_true')
    args = ap.parse_args()
    if args.check:
        result = self_check(args.check)
    else:
        ev, result = build(args.side, args.offset if args.offset is not None else -args.side,
                           choices=args.choices, outer=args.outer, as_array=args.array)
        if args.events:
            if args.array:
                import numpy as np
                np.save(args.events, ev)
            else:
                args.events.write_text(json.dumps(ev, separators=(',', ':')) + '\n')
    print(json.dumps(result), flush=True)
    if args.out:
        args.out.write_text(json.dumps(result, indent=2) + '\n')


if __name__ == '__main__':
    main()
