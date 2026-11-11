"""Girth-8 incidence graphs laid out on an N x N grid.

Graphs.
  gqQ : points and lines of the symplectic generalized quadrangle W(Q), Q prime.
        N = (Q+1)(Q^2+1), every row and column has Q+1 black cells.
  dQ  : points (p1,p2,p3) and lines [l1,l2,l3] over GF(Q), incident when
        p2 + l2 = p1 l1 and p3 + l3 = p1 l2. N = Q^3, Q black cells per row
        and column.

The black set is {(row of point, column of line) : point on line}. The only
freedom is the order of the points and of the lines.

Usage:  py algebraic_layouts.py NAME SEARCH_SECONDS [SEED]
Output: data/layout_NAME.json
"""
import itertools
import json
import math
import random
import sys
import time
from pathlib import Path

import numpy as np
from numba import njit

from rectcore import State, add_cell, remove_cell, verify_board

HERE = Path(__file__).resolve().parent


# ------------------------------------------------------------------ fields

class Field:
    def __init__(self, q):
        self.q = q
        if q == 4:
            # GF(4) = {0, 1, w, w+1} coded 0..3, addition is xor
            self.addt = [[a ^ b for b in range(4)] for a in range(4)]
            mul = [[0] * 4 for _ in range(4)]
            for a in range(4):
                for b in range(4):
                    r = 0
                    if b & 1:
                        r ^= a
                    if b & 2:
                        r ^= (a << 1)
                    if r & 4:
                        r ^= 0b111          # w^2 = w + 1
                    mul[a][b] = r
            self.mult = mul
        else:
            assert all(q % d for d in range(2, q))
            self.addt = [[(a + b) % q for b in range(q)] for a in range(q)]
            self.mult = [[(a * b) % q for b in range(q)] for a in range(q)]
        self.negt = [next(b for b in range(q) if self.addt[a][b] == 0) for a in range(q)]

    def add(self, a, b):
        return self.addt[a][b]

    def mul(self, a, b):
        return self.mult[a][b]

    def neg(self, a):
        return self.negt[a]


# ------------------------------------------------------------------ graphs

def graph_d(q):
    F = Field(q)
    pts = list(itertools.product(range(q), repeat=3))
    lines = list(itertools.product(range(q), repeat=3))
    lidx = {l: j for j, l in enumerate(lines)}
    edges = []
    for i, (p1, p2, p3) in enumerate(pts):
        for l1 in range(q):
            l2 = F.add(F.mul(p1, l1), F.neg(p2))
            l3 = F.add(F.mul(p1, l2), F.neg(p3))
            edges.append((i, lidx[(l1, l2, l3)]))
    return pts, lines, edges


def graph_gq(q):
    pts = []
    for v in itertools.product(range(q), repeat=4):
        nz = next((x for x in v if x), None)
        if nz == 1:
            pts.append(v)
    pidx = {p: i for i, p in enumerate(pts)}

    def norm(v):
        nz = next(x for x in v if x)
        inv = pow(nz, -1, q)
        return tuple(x * inv % q for x in v)

    def form(x, y):
        return (x[0] * y[1] - x[1] * y[0] + x[2] * y[3] - x[3] * y[2]) % q

    lines = set()
    for a, b in itertools.combinations(pts, 2):
        if form(a, b) == 0:
            span = {pidx[b]}
            for t in range(q):
                span.add(pidx[norm(tuple((a[i] + t * b[i]) % q for i in range(4)))])
            lines.add(tuple(sorted(span)))
    lines = sorted(lines)
    edges = [(i, j) for j, L in enumerate(lines) for i in L]
    assert len(pts) == len(lines) == (q + 1) * (q * q + 1)
    return pts, lines, edges


def girth(n_left, n_right, edges):
    n = n_left + n_right
    adj = [[] for _ in range(n)]
    for i, j in edges:
        adj[i].append(n_left + j)
        adj[n_left + j].append(i)
    best = math.inf
    for s in range(n):
        dist = {s: 0}
        par = {s: -1}
        queue = [s]
        for u in queue:
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    par[v] = u
                    queue.append(v)
                elif par[u] != v:
                    best = min(best, dist[u] + dist[v] + 1)
    return best


# ------------------------------------------------------------------ orderings

def natural_orderings(name, q, pts, lines, edges):
    """List of (label, row position of each point, column position of each line)."""
    out = []
    if name.startswith('d'):
        perms = list(itertools.permutations(range(3)))
        for a in perms:
            for b in perms:
                rp = [sum(p[a[k]] * q ** (2 - k) for k in range(3)) for p in pts]
                cp = [sum(l[b[k]] * q ** (2 - k) for k in range(3)) for l in lines]
                out.append((f'points by {a}, lines by {b}', rp, cp))
    else:
        for a in itertools.permutations(range(4)):
            order = sorted(range(len(pts)), key=lambda i: tuple(pts[i][a[k]] for k in range(4)))
            rp = [0] * len(pts)
            for pos, i in enumerate(order):
                rp[i] = pos
            lorder = sorted(range(len(lines)), key=lambda j: sorted(rp[i] for i in lines[j]))
            cp = [0] * len(lines)
            for pos, j in enumerate(lorder):
                cp[j] = pos
            out.append((f'points by coordinates {a}, lines by sorted point ranks', rp, cp))
    return out


def cells_of(N, edges, rp, cp):
    return [rp[i] * N + cp[j] for i, j in edges]


# ------------------------------------------------------------------ search kernels

@njit(cache=True)
def _swap(h, m, black, blist, nb, pos, nP, tp, tot, kind, i, j, rem, add):
    nr = 0
    na = 0
    for c in range(m):
        if kind == 0:
            u = i * m + c
            v = j * m + c
        else:
            u = c * m + i
            v = c * m + j
        if black[u] != black[v]:
            if black[u]:
                rem[nr] = u
                add[na] = v
            else:
                rem[nr] = v
                add[na] = u
            nr += 1
            na += 1
    for k in range(nr):
        nb = remove_cell(h, m, black, blist, nb, pos, nP, tp, tot, rem[k])
    for k in range(na):
        nb = add_cell(h, m, black, blist, nb, pos, nP, tp, tot, add[k])
    return nb


@njit(cache=True)
def anneal(h, m, black, blist, nb, pos, nP, tp, tot, rowlab, collab, nmoves, T, seed):
    np.random.seed(seed)
    rem = np.empty(2 * m, np.int64)
    add = np.empty(2 * m, np.int64)
    E = tot[0] + tot[1]
    accepted = 0
    for it in range(nmoves):
        kind = np.random.randint(0, 2)
        i = np.random.randint(0, m)
        j = np.random.randint(0, m - 1)
        if j >= i:
            j += 1
        nb = _swap(h, m, black, blist, nb, pos, nP, tp, tot, kind, i, j, rem, add)
        E2 = tot[0] + tot[1]
        d = E2 - E
        if d <= 0 or (T > 0 and np.random.random() < np.exp(-d / T)):
            E = E2
            accepted += 1
            if kind == 0:
                t = rowlab[i]
                rowlab[i] = rowlab[j]
                rowlab[j] = t
            else:
                t = collab[i]
                collab[i] = collab[j]
                collab[j] = t
        else:
            nb = _swap(h, m, black, blist, nb, pos, nP, tp, tot, kind, i, j, rem, add)
        if E == 0:
            break
    return nb, accepted


@njit(cache=True)
def greedy_delete(h, m, black, blist, nb, pos, nP, tp, tot, deleted):
    """Lazy greedy hitting set: delete the cell in the most collisions until
    M4 + M6 = 0. The gain of a cell only decreases as other cells go."""
    NN = h * m
    ub = np.full(NN, -1, np.int64)
    for k in range(nb):
        ub[blist[k]] = 1 << 60
    nd = 0
    while tot[0] + tot[1] > 0:
        x = np.argmax(ub)
        E0 = tot[0] + tot[1]
        nb = remove_cell(h, m, black, blist, nb, pos, nP, tp, tot, x)
        g = E0 - (tot[0] + tot[1])
        ub[x] = -1
        if g >= ub.max():
            deleted[nd] = x
            nd += 1
        else:
            nb = add_cell(h, m, black, blist, nb, pos, nP, tp, tot, x)
            ub[x] = g
    return nb, nd


def valid_subset(N, cells, rng, orders=20):
    """Two ways to a valid subset of the given cells: greedy deletion followed
    by re-insertion, and insertion in random order. Returns the best."""
    best = None
    st = State(N, N, cells)
    deleted = np.zeros(len(cells), np.int64)
    st.nb, nd = greedy_delete(N, N, st.black, st.blist, st.nb, st.pos, st.nP, st.tp, st.tot, deleted)
    greedy_deletions = int(nd)
    for x in deleted[:nd]:
        st.add(int(x))
        if st.tot[0] + st.tot[1] > 0:
            st.remove(int(x))
    assert st.full_black() <= 1
    best = st.cells()
    after_reinsert = len(best)
    insert_sizes = []
    for _ in range(orders):
        order = list(cells)
        rng.shuffle(order)
        st = State(N, N)
        for x in order:
            st.add(x)
            if st.tot[0] + st.tot[1] > 0:
                st.remove(x)
        insert_sizes.append(st.nb)
        if st.nb > len(best) and st.full_black() <= 1:
            best = st.cells()
    return best, {'greedy_deletions': greedy_deletions, 'size_after_greedy_deletion': len(cells) - greedy_deletions,
                  'size_after_reinsertion': after_reinsert,
                  'random_insertion_sizes_max': int(max(insert_sizes)) if insert_sizes else None,
                  'random_insertion_sizes_mean': float(np.mean(insert_sizes)) if insert_sizes else None,
                  'best_valid_size': len(best)}


def stats(N, cells):
    s = State(N, N, cells).summary()
    s['E'] = s['M4'] + s['M6']
    s['E_per_cell'] = s['E'] / len(cells)
    return s


def mean_stats(rows):
    keys = ['M4', 'M6', 'full_black', 'right_angles', 'right_angles_completing_inside', 'E', 'E_per_cell']
    return {k: float(np.mean([r[k] for r in rows])) for k in keys} | {
        'E_min': int(min(r['E'] for r in rows)), 'E_max': int(max(r['E'] for r in rows)), 'samples': len(rows)}


def run(name, seconds, seed):
    rng = random.Random(seed)
    q = int(name[-1])
    pts, lines, edges = graph_gq(q) if name.startswith('gq') else graph_d(q)
    N = len(pts)
    ne = len(edges)
    out = {'graph': name, 'q': q, 'N': N, 'edges': ne, 'girth': girth(N, N, edges),
           'N^(6/5)': N ** 1.2, 'N^(4/3)': N ** (4 / 3), 'frame_bound_2N-1': 2 * N - 1}
    print(name, 'N', N, 'edges', ne, 'girth', out['girth'], flush=True)
    nsamp = 20 if N <= 64 else 6

    # (a) natural, random orderings, random sets
    nat = natural_orderings(name, q, pts, lines, edges)
    nat_rows = []
    for label, rp, cp in nat:
        s = stats(N, cells_of(N, edges, rp, cp))
        s['label'] = label
        nat_rows.append(s)
    nat_rows.sort(key=lambda r: r['E'])
    out['natural'] = {'count': len(nat_rows), 'best': nat_rows[0], 'worst': nat_rows[-1],
                      'mean': mean_stats(nat_rows), 'all_E': [r['E'] for r in nat_rows]}
    best_nat = next((rp, cp) for label, rp, cp in nat if label == nat_rows[0]['label'])
    rand_rows = []
    rand_orders = []
    for _ in range(nsamp):
        rp = list(range(N))
        cp = list(range(N))
        rng.shuffle(rp)
        rng.shuffle(cp)
        rand_orders.append((rp, cp))
        rand_rows.append(stats(N, cells_of(N, edges, rp, cp)))
    out['random_ordering'] = mean_stats(rand_rows)
    set_rows = []
    rand_sets = []
    for _ in range(nsamp):
        cells = rng.sample(range(N * N), ne)
        rand_sets.append(cells)
        set_rows.append(stats(N, cells))
    out['random_set'] = mean_stats(set_rows)
    print(' natural best/mean/worst E per cell', nat_rows[0]['E_per_cell'], out['natural']['mean']['E_per_cell'],
          nat_rows[-1]['E_per_cell'], '| random ordering', out['random_ordering']['E_per_cell'],
          '| random set', out['random_set']['E_per_cell'], flush=True)

    # (b) local search: half the time from the best natural ordering, half from a random one
    searches = []
    for start_label, (rp0, cp0) in (('best natural', best_nat), ('random', rand_orders[0])):
        budget = seconds / 2
        t0 = time.monotonic()
        st = State(N, N, cells_of(N, edges, rp0, cp0))
        rowlab = np.empty(N, np.int64)      # rowlab[r] = point shown in row r
        collab = np.empty(N, np.int64)
        for i, r in enumerate(rp0):
            rowlab[r] = i
        for j, c in enumerate(cp0):
            collab[c] = j
        E_start = int(st.tot[0] + st.tot[1])
        # calibrate
        t1 = time.monotonic()
        st.nb, _ = anneal(N, N, st.black, st.blist, st.nb, st.pos, st.nP, st.tp, st.tot, rowlab, collab, 50, 0.0, seed)
        rate = 50 / max(time.monotonic() - t1, 1e-3)
        chunk = max(20, int(rate * 2))
        T_hi, T_lo = 1.5, 0.05
        moves = 50
        best_E, best_lab = int(st.tot[0] + st.tot[1]), (rowlab.copy(), collab.copy())
        while True:
            frac = (time.monotonic() - t0) / budget
            if frac >= 1 or st.tot[0] + st.tot[1] == 0:
                break
            T = 0.0 if frac > 0.8 else T_hi * (T_lo / T_hi) ** (frac / 0.8)
            st.nb, _ = anneal(N, N, st.black, st.blist, st.nb, st.pos, st.nP, st.tp, st.tot, rowlab, collab,
                              chunk, T, rng.randrange(1 << 30))
            moves += chunk
            E = int(st.tot[0] + st.tot[1])
            if E < best_E:
                best_E, best_lab = E, (rowlab.copy(), collab.copy())
        rp = [0] * N
        cp = [0] * N
        for r in range(N):
            rp[int(best_lab[0][r])] = r
        for c in range(N):
            cp[int(best_lab[1][c])] = c
        s = stats(N, cells_of(N, edges, rp, cp))
        assert s['E'] == best_E
        searches.append({'start': start_label, 'E_start': E_start, 'moves': moves, 'seconds': round(time.monotonic() - t0, 1),
                         'result': s, 'row_of_point': rp, 'column_of_line': cp})
        print(' search from', start_label, ': E', E_start, '->', best_E, 'moves', moves, flush=True)
    searches.sort(key=lambda r: r['result']['E'])
    out['search'] = searches
    best = searches[0]

    # valid subsets
    out['valid_subsets'] = {}
    reports = [('best searched ordering', cells_of(N, edges, best['row_of_point'], best['column_of_line'])),
               ('best natural ordering', cells_of(N, edges, *best_nat)),
               ('random ordering', cells_of(N, edges, *rand_orders[0])),
               ('random set', rand_sets[0])]
    for label, cells in reports:
        board, info = valid_subset(N, cells, rng, orders=20 if N <= 64 else 5)
        ok, nrect, nkeys, coll = verify_board(N, N, board)
        info.update(verified=bool(ok), rectangles=nrect, presentations_compared=nkeys, cells=board)
        assert ok
        out['valid_subsets'][label] = info
        print(' valid subset,', label, ':', {k: v for k, v in info.items() if k != 'cells'}, flush=True)

    # (c) structure of the best ordering: do neighbouring rows share a coordinate value?
    if name.startswith('d'):
        struct = {}
        rows_sorted = sorted(range(N), key=lambda i: best['row_of_point'][i])
        cols_sorted = sorted(range(N), key=lambda j: best['column_of_line'][j])
        for k in range(3):
            struct[f'adjacent rows with equal p{k + 1}'] = sum(pts[rows_sorted[i]][k] == pts[rows_sorted[i + 1]][k] for i in range(N - 1))
            struct[f'adjacent columns with equal l{k + 1}'] = sum(lines[cols_sorted[i]][k] == lines[cols_sorted[i + 1]][k] for i in range(N - 1))
        struct['expected for a random order'] = (N - 1) * (q * q - 1) / (N - 1)
        out['best_ordering_structure'] = struct
    board = np.zeros((N, N), int)
    for v in cells_of(N, edges, best['row_of_point'], best['column_of_line']):
        board[v // N, v % N] = 1
    quarter = max(1, N // 4)
    centre = board[quarter:N - quarter, quarter:N - quarter].sum()
    out['best_ordering_centre_share'] = {'cells in the central half-by-half window': int(centre), 'share': centre / ne,
                                         'uniform share': ((N - 2 * quarter) / N) ** 2}
    (HERE / 'data').mkdir(exist_ok=True)
    (HERE / 'data' / f'layout_{name}.json').write_text(json.dumps(out))
    print('done', name, flush=True)


if __name__ == '__main__':
    run(sys.argv[1], float(sys.argv[2]) if len(sys.argv) > 2 else 240.0, int(sys.argv[3]) if len(sys.argv) > 3 else 1)
