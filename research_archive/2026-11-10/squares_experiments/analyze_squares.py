"""Structure of the boards in data/optima_n*_k*.json.

For every board: validity by the diagonal enumeration (rectcore.verify_board,
all rectangles), boundary share, row and column counts, the row-column graph
(components, girth), black right angles (three black corners of a rectangle,
axis or tilted) and how many have their fourth corner in the grid.

Usage: py analyze_squares.py     (writes data/square_structure.json and prints a summary)
"""
import json
import math
from collections import Counter
from itertools import combinations
from pathlib import Path

from rectcore import verify_board
from square_sat import d4_images

HERE = Path(__file__).resolve().parent


def graph_stats(n, cells):
    adj = {}
    for v in cells:
        r, c = divmod(v, n)
        adj.setdefault(('r', r), []).append(('c', c))
        adj.setdefault(('c', c), []).append(('r', r))
    girth = math.inf
    for s in adj:
        dist, par, queue = {s: 0}, {s: None}, [s]
        for u in queue:
            for w in adj[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    par[w] = u
                    queue.append(w)
                elif par[u] != w:
                    girth = min(girth, dist[u] + dist[w] + 1)
    seen, comps = set(), 0
    for s in adj:
        if s not in seen:
            comps += 1
            stack = [s]
            seen.add(s)
            while stack:
                u = stack.pop()
                for w in adj[u]:
                    if w not in seen:
                        seen.add(w)
                        stack.append(w)
    cyclomatic = len(cells) - len(adj) + comps
    return girth, comps, cyclomatic, 2 * n - len(adj)


def right_angles(n, cells):
    """Black triples a, b, c with a right angle at b; (axis, tilted) x (completes inside, outside)."""
    S = set(cells)
    pts = [divmod(v, n) for v in cells]
    out = Counter()
    for b in pts:
        others = [p for p in pts if p != b]
        for a, c in combinations(others, 2):
            u = (a[0] - b[0], a[1] - b[1])
            w = (c[0] - b[0], c[1] - b[1])
            if u[0] * w[0] + u[1] * w[1] == 0:
                p = (a[0] + c[0] - b[0], a[1] + c[1] - b[1])
                kind = 'axis' if (u[0] == 0 or u[1] == 0) else 'tilted'
                inside = 0 <= p[0] < n and 0 <= p[1] < n
                out[(kind, 'inside' if inside else 'outside')] += 1
                if inside and p[0] * n + p[1] in S:
                    out['fully black'] += 1
    return out


def board_text(n, cells):
    S = set(cells)
    return [''.join('#' if r * n + c in S else '.' for c in range(n)) for r in range(n)]


def analyse(n, boards):
    maps = d4_images(n)
    orbits = {}
    rows = []
    for cells in boards:
        ok = verify_board(n, n, cells, full=True)[0]
        assert ok, (n, cells)
        S = frozenset(cells)
        canon = min([tuple(sorted(S))] + [tuple(sorted(perm[v] for v in S)) for perm in maps])
        orbits.setdefault(canon, []).append(cells)
        rc = [0] * n
        cc = [0] * n
        boundary = corners = 0
        for v in cells:
            r, c = divmod(v, n)
            rc[r] += 1
            cc[c] += 1
            on = r in (0, n - 1) or c in (0, n - 1)
            boundary += on
            corners += r in (0, n - 1) and c in (0, n - 1)
        girth, comps, cyc, isolated = graph_stats(n, cells)
        ra = right_angles(n, cells)
        rows.append({'canon': canon, 'size': len(cells), 'boundary': boundary, 'corners': corners, 'row_counts': rc, 'col_counts': cc,
                     'girth': None if girth == math.inf else girth, 'components': comps, 'cyclomatic': cyc,
                     'empty_lines': isolated,
                     'ra_axis_inside': ra[('axis', 'inside')], 'ra_axis_outside': ra[('axis', 'outside')],
                     'ra_tilted_inside': ra[('tilted', 'inside')], 'ra_tilted_outside': ra[('tilted', 'outside')],
                     'fully_black': ra['fully black']})
    k = rows[0]['size']
    nb = len(rows)
    ring = 4 * n - 4
    summ = {
        'n': n, 'size': k, 'boards': nb, 'orbits': len(orbits),
        'orbit_sizes': dict(Counter(len(set(map(tuple, v))) for v in orbits.values())),
        'boundary_cells_in_grid_share': ring / (n * n),
        'boundary_share_mean': sum(r['boundary'] for r in rows) / (nb * k),
        'boundary_count_distribution': dict(sorted(Counter(r['boundary'] for r in rows).items())),
        'corner_count_distribution': dict(sorted(Counter(r['corners'] for r in rows).items())),
        'sorted_row_counts_distribution': {str(key): val for key, val in Counter(tuple(sorted(r['row_counts'], reverse=True)) for r in rows).most_common(8)},
        'row_counts_by_position_mean': [sum(r['row_counts'][i] for r in rows) / nb for i in range(n)],
        'col_counts_by_position_mean': [sum(r['col_counts'][i] for r in rows) / nb for i in range(n)],
        'max_line_count_distribution': dict(sorted(Counter(max(r['row_counts'] + r['col_counts']) for r in rows).items())),
        'girth_distribution': {str(key): val for key, val in Counter(r['girth'] for r in rows).items()},
        'components_distribution': dict(sorted(Counter(r['components'] for r in rows).items())),
        'cyclomatic_distribution': dict(sorted(Counter(r['cyclomatic'] for r in rows).items())),
        'empty_lines_distribution': dict(sorted(Counter(r['empty_lines'] for r in rows).items())),
        'right_angles_mean': {key: sum(r[key] for r in rows) / nb for key in
                              ('ra_axis_inside', 'ra_axis_outside', 'ra_tilted_inside', 'ra_tilted_outside')},
        'right_angles_inside_total_distribution': dict(sorted(Counter(r['ra_axis_inside'] + r['ra_tilted_inside'] for r in rows).items())),
        'fully_black_rectangles_max': max(r['fully_black'] for r in rows),
        'representatives': [{'cells': list(canon), 'picture': board_text(n, canon), 'orbit_size': len(set(map(tuple, v)))}
                            for canon, v in sorted(orbits.items())[:12]],
        'all_verified': True,
    }
    return summ


if __name__ == '__main__':
    out = {}
    for path in sorted((HERE / 'data').glob('optima_n*_k*.json')):
        d = json.loads(path.read_text())
        if not d['boards']:
            continue
        s = analyse(d['n'], d['boards'])
        s['enumeration_complete'] = d['complete']
        out[f"n{d['n']}_k{d['k']}"] = s
        print(f"\n== n = {s['n']}, size {s['size']}: {s['boards']} boards in {s['orbits']} orbits"
              f" (complete: {d['complete']})")
        for key in ('boundary_share_mean', 'boundary_cells_in_grid_share', 'boundary_count_distribution',
                    'corner_count_distribution', 'sorted_row_counts_distribution', 'row_counts_by_position_mean',
                    'max_line_count_distribution', 'girth_distribution', 'components_distribution',
                    'cyclomatic_distribution', 'empty_lines_distribution', 'right_angles_mean',
                    'right_angles_inside_total_distribution'):
            print(' ', key, s[key])
        for rep in s['representatives'][:4]:
            print('   ' + '\n   '.join(rep['picture']) + '\n')
    (HERE / 'data' / 'square_structure.json').write_text(json.dumps(out, indent=1))
