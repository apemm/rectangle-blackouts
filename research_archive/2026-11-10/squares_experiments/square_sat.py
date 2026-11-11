"""SAT search on the n x n grid.

Encoding (presentation fibers, see research/2026-11-09/full_problem_push/
presentation_fiber_factorization.md): one variable per cell; one flag per pair
Q of corners of a rectangle, triggered when both cells of Q are black; for each
pair P, at most one of the flags of the complementary pairs R minus P over the
rectangles R containing P; one flag per (rectangle, corner), triggered when the
other three corners are black; for each cell p, at most one such flag; one flag
per rectangle, triggered when all four corners are black, at most one in total.
The rectangles come from rectcore.rects_by_sides. The number of black cells is
bounded below by a totalizer.

Symmetry: the eight symmetries of the square act on valid sets. With sym=True
the board is required to be lexicographically least among its eight images
(row-major reading, black = 1), which keeps one board or more per orbit.

Usage:
  py square_sat.py decide N K [SECONDS] [CUBE_INDEX CUBE_BITS]
  py square_sat.py windows N K [SECONDS] [CUBE_INDEX CUBE_BITS] [AxB=V ...]
      as decide, with the bound f(a, b) on every window of consecutive rows
      and columns (recorded values, see f_known); AxB=V adds or overrides a bound
  py square_sat.py enumerate N K [SECONDS]
"""
import json
import sys
import time
from itertools import combinations
from pathlib import Path
import multiprocessing as mp

from pysat.card import CardEnc, EncType
from pysat.solvers import Solver

from rectcore import rects_by_sides, verify_board, verify_plain

HERE = Path(__file__).resolve().parent


def amo(clauses, lits, new):
    k = len(lits)
    if k < 2:
        return
    if k <= 4:
        for a, b in combinations(lits, 2):
            clauses.append([-a, -b])
        return
    s = [new() for _ in range(k - 1)]
    for i in range(k - 1):
        clauses.append([-lits[i], s[i]])
    for i in range(1, k - 1):
        clauses.append([-s[i - 1], s[i]])
    for i in range(1, k):
        clauses.append([-lits[i], -s[i - 1]])


def d4_images(n):
    """The seven non-identity symmetries as permutations of cell indices."""
    maps = []
    for t in range(1, 8):
        perm = []
        for r in range(n):
            for c in range(n):
                rr, cc = r, c
                if t & 4:
                    rr, cc = cc, rr
                if t & 1:
                    rr = n - 1 - rr
                if t & 2:
                    cc = n - 1 - cc
                perm.append(rr * n + cc)
        maps.append(perm)
    return maps


def f_known(a, b):
    """Recorded values of f(a, b) used as window bounds (README.md of the
    project, and research/2026-11-09/CLAIM_LEDGER.md row F1 for 7 x 9 to 7 x 12).
    None when no exact value is recorded."""
    a, b = min(a, b), max(a, b)
    if a == 1:
        return b
    if a == 2:
        return 4 if b == 2 else b + 1
    if a == 3:
        return b + 2
    if a == 4:
        return {4: 7, 5: 8}.get(b, b + 4)
    if a == 5:
        return {5: 10, 6: 11, 7: 12}.get(b, b + 6)
    if a == 6:
        if b <= 7:
            return {6: 12, 7: 13}[b]
        return b + 7 if b <= 11 else b + 8 if b <= 14 else b + 9
    if a == 7:
        return {7: 14, 8: 16, 9: 17, 10: 18, 11: 20, 12: 21}.get(b)
    return None


def encode(n, k, sym=True, windows=False, extra_bounds=None):
    NN = n * n
    top = [NN]

    def new():
        top[0] += 1
        return top[0]

    clauses = []
    rects = rects_by_sides(n, n)
    pair_flag = {}
    by_pair = {}
    by_point = [[] for _ in range(NN)]
    hidden = []
    for R in rects:
        for Q in combinations(R, 2):
            if Q not in pair_flag:
                f = new()
                pair_flag[Q] = f
                clauses.append([-(Q[0] + 1), -(Q[1] + 1), f])
        for P in combinations(R, 2):
            Q = tuple(v for v in R if v not in P)
            by_pair.setdefault(P, []).append(pair_flag[Q])
        for p in R:
            f = new()
            clauses.append([-(v + 1) for v in R if v != p] + [f])
            by_point[p].append(f)
        z = new()
        clauses.append([-(v + 1) for v in R] + [z])
        hidden.append(z)
    for lits in by_pair.values():
        amo(clauses, lits, new)
    for lits in by_point:
        amo(clauses, lits, new)
    amo(clauses, hidden, new)
    if sym:
        for perm in d4_images(n):
            # x <=_lex y with x = board, y = image
            prev = None
            for i in range(NN):
                x, y = i + 1, perm[i] + 1
                if x == y:
                    continue
                if prev is None:
                    clauses.append([-x, y])
                    e = new()
                    clauses.append([x, y, e])
                    clauses.append([-x, -y, e])
                else:
                    clauses.append([-prev, -x, y])
                    e = new()
                    clauses.append([-prev, x, y, e])
                    clauses.append([-prev, -x, -y, e])
                prev = e
    if windows:
        # a valid set restricted to a window of consecutive rows and columns is
        # valid on that window, so it has at most f(a, b) cells there
        bounds = dict(extra_bounds or {})
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if (a, b) == (n, n):
                    continue
                bound = bounds.get((min(a, b), max(a, b)), f_known(a, b))
                if bound is None or bound >= a * b:
                    continue
                for r0 in range(n - a + 1):
                    for c0 in range(n - b + 1):
                        lits = [(r0 + i) * n + c0 + j + 1 for i in range(a) for j in range(b)]
                        card = CardEnc.atmost(lits=lits, bound=bound, top_id=top[0], encoding=EncType.seqcounter)
                        clauses.extend(card.clauses)
                        top[0] = max(top[0], card.nv)
    if k > 0:
        card = CardEnc.atleast(lits=list(range(1, NN + 1)), bound=k, top_id=top[0], encoding=EncType.totalizer)
        clauses.extend(card.clauses)
        top[0] = max(top[0], card.nv)
    return clauses, len(rects)


def cube_cells(n, bits):
    """Cells used for case splits: the four corners, then cells near the centre."""
    c = n // 2
    order = [0, n - 1, (n - 1) * n, n * n - 1, (c - 1) * n + c - 1, (c - 1) * n + c, c * n + c - 1, c * n + c]
    return order[:bits]


def _decide_child(conn, clauses, assumptions, solver_name):
    with Solver(name=solver_name, bootstrap_with=clauses) as s:
        res = s.solve(assumptions=assumptions)
        conn.send((res, s.get_model() if res else None))


def _enumerate_child(conn, clauses, n):
    with Solver(name='cadical195', bootstrap_with=clauses) as s:
        while s.solve():
            model = s.get_model()
            cells = [v for v in range(n * n) if model[v] > 0]
            conn.send(cells)
            s.add_clause([-(v + 1) for v in cells])
        conn.send('done')


def decide(n, k, seconds, cube=None, solver_name='cadical195', windows=False, extra_bounds=None):
    """The solver runs in a child process, which is killed at the deadline."""
    t0 = time.monotonic()
    clauses, nrect = encode(n, k, sym=True, windows=windows, extra_bounds=extra_bounds)
    assumptions = []
    if cube is not None:
        idx, bits = cube
        cells = cube_cells(n, bits)
        assumptions = [(v + 1) if (idx >> j) & 1 else -(v + 1) for j, v in enumerate(cells)]
    parent, child = mp.Pipe(duplex=False)
    proc = mp.Process(target=_decide_child, args=(child, clauses, assumptions, solver_name))
    proc.start()
    res, model = (None, None)
    if parent.poll(max(1.0, seconds - (time.monotonic() - t0))):
        res, model = parent.recv()
        proc.join()
    else:
        proc.terminate()
        proc.join()
    out = {'n': n, 'k': k, 'rectangles': nrect, 'clauses': len(clauses), 'solver': solver_name,
           'window_bounds': windows, 'extra_bounds': None if not extra_bounds else {f'{a}x{b}': v for (a, b), v in extra_bounds.items()},
           'cube': None if cube is None else {'index': cube[0], 'bits': cube[1],
                                              'cells': cube_cells(n, cube[1])},
           'seconds': round(time.monotonic() - t0, 2)}
    if res is True:
        cells = [v for v in range(n * n) if model[v] > 0]
        ok = verify_board(n, n, cells, full=True)[0] and verify_plain(n, n, cells)[0]
        out.update(status='SAT', cells=cells, size=len(cells), verified=bool(ok))
    elif res is False:
        out.update(status='UNSAT')
    else:
        out.update(status='UNRESOLVED')
    return out


def enumerate_all(n, k, seconds):
    """All valid sets with k or more black cells (no symmetry reduction).
    When k is the maximum these are exactly the maximum sets."""
    t0 = time.monotonic()
    clauses, nrect = encode(n, k, sym=False)
    boards = []
    complete = False
    parent, child = mp.Pipe(duplex=False)
    proc = mp.Process(target=_enumerate_child, args=(child, clauses, n))
    proc.start()
    while True:
        left = seconds - (time.monotonic() - t0)
        if left <= 0 or not parent.poll(left):
            break
        msg = parent.recv()
        if msg == 'done':
            complete = True
            break
        boards.append(msg)
    proc.terminate()
    proc.join()
    return {'n': n, 'k': k, 'complete': complete, 'count': len(boards), 'boards': boards,
            'seconds': round(time.monotonic() - t0, 2)}


if __name__ == '__main__':
    mode, n, k = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    seconds = float(sys.argv[4]) if len(sys.argv) > 4 else 600.0
    if mode in ('decide', 'windows'):
        rest = [a for a in sys.argv[5:] if '=' not in a]
        extra = {}
        for a in sys.argv[5:]:
            if '=' in a:
                dims, val = a.split('=')
                x, y = sorted(int(t) for t in dims.split('x'))
                extra[(x, y)] = int(val)
        cube = (int(rest[0]), int(rest[1])) if len(rest) > 1 else None
        out = decide(n, k, seconds, cube, windows=(mode == 'windows'), extra_bounds=extra)
        tag = '' if cube is None else f'_cube{cube[0]}of{2 ** cube[1]}'
        path = HERE / 'data' / f'{mode}_n{n}_k{k}{tag}.json'
    else:
        out = enumerate_all(n, k, seconds)
        path = HERE / 'data' / f'optima_n{n}_k{k}.json'
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(out))
    print({key: val for key, val in out.items() if key not in ('boards', 'cells')}, flush=True)
