"""Bounded saturated all-double corner-free relaxation.

This enforces every edge of one complete balanced row bipartition once,
and forbids all tilted rectangles with at least three black corners.
It does not encode mixed two-white collisions. Every SAT candidate is
then checked independently against all actual rectangle presentations.
"""

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


def tilted_rectangles(h, w):
    out = set()
    for b in range(1, h - 1):
        for d in range(1, h - b):
            for a in range(1, w - 1):
                if (b * d) % a:
                    continue
                c = b * d // a
                if a + c >= w:
                    continue
                for x in range(w - a - c):
                    for y in range(h - b - d):
                        pts = ((x + c, y), (x + c + a, y + b),
                               (x, y + d), (x + a, y + b + d))
                        out.add(tuple(sorted(r * w + col for col, r in pts)))
    return sorted(out)


def worker(connection, clauses):
    with Solver(name='cadical195', bootstrap_with=clauses) as solver:
        answer = solver.solve()
        connection.send((answer, solver.get_model() if answer else None))
    connection.close()


def run(h, part=None, seconds=20, shape_mode='all', width=None, min_row_degree=0):
    start = time.monotonic()
    general = part is False
    if general:
        part, other = tuple(range(h)), ()
        pairs = tuple(combinations(range(h), 2))
        w = h * h // 4 if width is None else width
    else:
        if part is None:
            part = tuple(range(0, h, 2))
        other = tuple(r for r in range(h) if r not in part)
        assert abs(len(part) - len(other)) <= 1
        pairs = tuple((a, b) for a in part for b in other)
        w = len(pairs) if width is None else width
    assert 1 <= w <= len(pairs)
    n = h * w
    clauses = []
    top = n
    for col in range(w):
        for rows in ((part,) if general else (part, other)):
            card = CardEnc.equals([r * w + col + 1 for r in rows], 2 if general else 1,
                                  top_id=top, encoding=EncType.seqcounter)
            clauses.extend(card.clauses)
            top = card.nv
    pair_flags = {}
    for a, b in pairs:
        owners = []
        for col in range(w):
            top += 1
            owner = top
            owners.append(owner)
            av, bv = a * w + col + 1, b * w + col + 1
            clauses.extend([[-owner, av], [-owner, bv], [owner, -av, -bv]])
        encode = CardEnc.equals if w == len(pairs) else CardEnc.atmost
        card = encode(owners, 1, top_id=top, encoding=EncType.seqcounter)
        clauses.extend(card.clauses)
        top = card.nv
        if general:
            top += 1
            pair_flags[a, b] = top
            clauses.extend([[-owner, top] for owner in owners])
            clauses.append([-top] + owners)
    if general:
        for a, b, c in combinations(range(h), 3):
            clauses.append([-pair_flags[a, b], -pair_flags[a, c], -pair_flags[b, c]])
    if min_row_degree:
        for r in range(h):
            card = CardEnc.atleast([r * w + col + 1 for col in range(w)],
                                  min_row_degree, top_id=top, encoding=EncType.seqcounter)
            clauses.extend(card.clauses)
            top = card.nv
    all_tilted = tilted_rectangles(h, w)
    if shape_mode == 'all':
        tilted = all_tilted
    elif shape_mode == 'unit':
        tilted = [r for r in all_tilted
                  if max(p % w for p in r) - min(p % w for p in r) == 2
                  and max(p // w for p in r) - min(p // w for p in r) == 2]
    elif shape_mode == '45':
        tilted = [r for r in all_tilted
                  if len({p % w - p // w for p in r}) == 2
                  and len({p % w + p // w for p in r}) == 2]
    else:
        raise ValueError(shape_mode)
    supports = {subset for rectangle in tilted for subset in combinations(rectangle, 3)}
    clauses.extend([-(p + 1) for p in support] for support in sorted(supports))
    build = time.monotonic() - start
    context = mp.get_context('spawn')
    receive, send = context.Pipe(duplex=False)
    process = context.Process(target=worker, args=(send, clauses))
    process.start()
    send.close()
    process.join(seconds)
    if process.is_alive():
        process.terminate()
        process.join()
        answer, model = None, None
    elif receive.poll():
        answer, model = receive.recv()
    else:
        raise RuntimeError(f'Solver worker exited without a result: {process.exitcode}')
    receive.close()
    result = dict(height=h, width=w, row_part=None if general else [r + 1 for r in part],
                  status={True: 'SAT', False: 'UNSAT', None: 'UNKNOWN'}[answer],
                  corner_shape_mode=shape_mode,
                  complete_family=(w == h * h // 4 if general else w == len(pairs)),
                  min_row_degree=min_row_degree, unrestricted_triangle_free_graph=general,
                  solver='cadical195', pysat_version=pysat_version,
                  process_limit_seconds=seconds, limit_enforced=True,
                  build_seconds=build, elapsed_seconds=time.monotonic() - start,
                  tilted_rectangle_count=len(tilted), corner_supports=len(supports),
                  variables=top, clauses=len(clauses),
                  formal_unsat_proof_saved=False)
    if model:
        black = {p for p in range(n) if model[p] > 0}
        word = [[r + 1 for r in range(h) if r * w + col in black] for col in range(w)]
        assert len({frozenset(rows) for rows in word}) == w
        assert all(len(rows) == 2 for rows in word)
        assert all(sum(p in black for p in rectangle) <= 2 for rectangle in tilted)
        result['word'] = word
        all_rectangles = list(all_tilted)
        for a, b in combinations(range(h), 2):
            for x, z in combinations(range(w), 2):
                all_rectangles.append((a * w + x, a * w + z, b * w + x, b * w + z))
        seen = {}
        collisions = []
        for rectangle in all_rectangles:
            white = tuple(sorted(set(rectangle) - black))
            if white in seen:
                if len(collisions) < 20:
                    def points(items):
                        return [(p % w + 1, p // w + 1) for p in items]
                    collisions.append(dict(white=points(white),
                                           rectangle=points(rectangle),
                                           other=points(seen[white])))
            else:
                seen[white] = rectangle
        result['full_presentation_check'] = 'PASS' if len(seen) == len(all_rectangles) else 'FAIL'
        result['rectangle_count'] = len(all_rectangles)
        result['distinct_presentations'] = len(seen)
        result['first_collisions'] = collisions
    return result


if __name__ == '__main__':
    for h in map(int, sys.argv[1:] or ['4', '5', '6', '7', '8']):
        result = run(h)
        print(json.dumps(result), flush=True)
        (HERE / f'continuation_saturation_corner_h{h}.json').write_text(
            json.dumps(result, indent=2) + '\n', encoding='utf-8')
