"""Bounded exact all-double square search, with direct presentation checks."""

from collections import defaultdict
from itertools import combinations
from pathlib import Path
import json
import multiprocessing as mp
import sys
import time

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / '2026-11-09/full_problem_push/.runtime'))
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver
from pysat import __version__ as pysat_version


def rectangles(h, w):
    points = [(x, y) for y in range(h) for x in range(w)]
    groups = defaultdict(list)
    for a, b in combinations(points, 2):
        key = (a[0] + b[0], a[1] + b[1],
               (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
        groups[key].append((a, b))
    out = set()
    for diagonals in groups.values():
        for first, second in combinations(diagonals, 2):
            corners = set(first + second)
            if len(corners) == 4:
                out.add(sum(1 << (y * w + x) for x, y in corners))
    return sorted(out)


def positions(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def solve_worker(connection, clauses):
    with Solver(name='cadical195', bootstrap_with=clauses) as solver:
        answer = solver.solve()
        connection.send((answer, solver.get_model() if answer else None))
    connection.close()


def run(h, seconds=60, part=None, min_row_degree=0):
    started = time.monotonic()
    w = h
    rects = rectangles(h, w)
    columns = [sum(1 << (y * w + x) for y in range(h)) for x in range(w)]
    supports = set()
    for first, second in combinations(rects, 2):
        support = first ^ second
        if all((support & col).bit_count() <= 2 for col in columns):
            supports.add(support)
    # Under two cells per column, supports with three cells in a column
    # can never be entirely black. The remaining clauses are exact.
    minimal = []
    buckets = defaultdict(set)
    for support in sorted(supports, key=int.bit_count):
        bits = tuple(1 << p for p in positions(support))
        if any(sum(subset) in buckets[k]
               for k in buckets if k < len(bits)
               for subset in combinations(bits, k)):
            continue
        buckets[len(bits)].add(support)
        minimal.append(support)
    clauses = [[-(p + 1) for p in positions(support)] for support in minimal]
    top = h * w
    for x in range(w):
        encoded = CardEnc.equals([y * w + x + 1 for y in range(h)], 2,
                                 top_id=top, encoding=EncType.seqcounter)
        clauses.extend(encoded.clauses)
        top = encoded.nv
        if part is not None:
            clauses.append([y * w + x + 1 for y in range(h) if y + 1 in part])
            clauses.append([y * w + x + 1 for y in range(h) if y + 1 not in part])
    if min_row_degree:
        for y in range(h):
            encoded = CardEnc.atleast([y * w + x + 1 for x in range(w)],
                                     min_row_degree, top_id=top,
                                     encoding=EncType.seqcounter)
            clauses.extend(encoded.clauses)
            top = encoded.nv
    build_seconds = time.monotonic() - started
    context = mp.get_context('spawn')
    receiving, sending = context.Pipe(duplex=False)
    process = context.Process(target=solve_worker, args=(sending, clauses))
    process.start()
    sending.close()
    process.join(seconds)
    if process.is_alive():
        process.terminate()
        process.join()
        answer, model = None, None
    elif receiving.poll():
        answer, model = receiving.recv()
    else:
        raise RuntimeError(f'Solver worker exited without a result: {process.exitcode}')
    receiving.close()
    result = dict(height=h, width=w, rectangles=len(rects),
                  raw_supports=len(supports), minimal_supports=len(minimal),
                  variables=top, clauses=len(clauses),
                  build_seconds=build_seconds,
                  solve_status={True: 'SAT', False: 'UNSAT', None: 'UNKNOWN'}[answer],
                  seconds=time.monotonic() - started, solver='cadical195',
                  pysat_version=pysat_version, solver_time_limit_seconds=seconds,
                  solver_time_limit_enforced=True, solver_limit_method='separate process',
                  min_row_degree=min_row_degree,
                  formal_unsat_proof_saved=False)
    if part is not None:
        result['row_partition_part'] = sorted(part)
    if model:
        black = sum(1 << p for p in range(h * w) if model[p] > 0)
        presentations = [R & ~black for R in rects]
        assert len(set(presentations)) == len(rects)
        assert all((black & col).bit_count() == 2 for col in columns)
        result['word'] = [[y + 1 for y in range(h) if black & (1 << (y * w + x))]
                          for x in range(w)]
        result['direct_presentation_check'] = 'PASS'
    return result


if __name__ == '__main__':
    for h in map(int, sys.argv[1:] or ['6', '7', '8']):
        result = run(h)
        print(json.dumps(result), flush=True)
        (HERE / f'all_double_square_h{h}.json').write_text(
            json.dumps(result, indent=2) + '\n', encoding='utf-8')
