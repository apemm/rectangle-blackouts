"""Collect the boards found by annealing and SAT into data/boards_n*_k*.json and
print the Markdown tables used in README.md.

Usage: py make_tables.py
"""
import json
from pathlib import Path

from rectcore import verify_board, verify_plain

HERE = Path(__file__).resolve().parent
DATA = HERE / 'data'


def collect():
    found = {}
    for path in sorted(DATA.glob('anneal_n*_k*_s*.json')):
        d = json.loads(path.read_text())
        for b in d['boards']:
            found.setdefault((d['n'], d['k']), set()).add(tuple(b))
    for path in sorted(DATA.glob('decide_n*_k*.json')) + sorted(DATA.glob('windows_n*_k*.json')):
        d = json.loads(path.read_text())
        if d['status'] == 'SAT':
            found.setdefault((d['n'], d['k']), set()).add(tuple(d['cells']))
    best = {}
    for (n, k), boards in found.items():
        best[n] = max(best.get(n, 0), k)
    for (n, k), boards in sorted(found.items()):
        if n < 8 or k < best[n]:
            continue
        boards = sorted(boards)
        for b in boards:
            assert verify_board(n, n, b, full=True)[0] and verify_plain(n, n, b)[0]
        (DATA / f'boards_n{n}_k{k}.json').write_text(json.dumps(
            {'n': n, 'k': k, 'complete': False, 'count': len(boards), 'boards': [list(b) for b in boards],
             'source': 'annealing (anneal_square.py) and SAT models (square_sat.py), all rechecked'}))
        print(f'boards_n{n}_k{k}.json: {len(boards)} boards')


def sat_table():
    print('\n| n | k | mode | cube | status | seconds |\n|---|---|---|---|---|---|')
    rows = []
    for path in sorted(DATA.glob('decide_n*_k*.json')) + sorted(DATA.glob('windows_n*_k*.json')):
        d = json.loads(path.read_text())
        cube = '' if not d.get('cube') else f"{d['cube']['index']} of 2^{d['cube']['bits']}"
        rows.append((d['n'], d['k'], path.name.split('_')[0], cube, d['status'], d['seconds']))
    for r in sorted(rows, key=lambda r: (r[0], r[1], r[2], r[3])):
        print('| ' + ' | '.join(str(v) for v in r) + ' |')
    print('\n| n | k | seed | seconds | restarts | least collisions | valid boards |\n|---|---|---|---|---|---|---|')
    for path in sorted(DATA.glob('anneal_n*_k*_s*.json')):
        d = json.loads(path.read_text())
        print(f"| {d['n']} | {d['k']} | {d['seed']} | {d['seconds']} | {d['restarts']} | {d['least_collisions_at_end_of_a_run']} | {d['valid_boards_found']} |")


def layout_tables():
    base = json.loads((DATA / 'baseline_insertion.json').read_text())
    names = ['d2', 'gq2', 'd3', 'gq3', 'd4', 'd5']
    ds = [json.loads((DATA / f'layout_{g}.json').read_text()) for g in names if (DATA / f'layout_{g}.json').exists()]
    print('\nCollisions per black cell, (M4 + M6) / edges\n')
    print('| graph | N | edges | girth | random set | random ordering | natural: best / mean / worst | after search | search / random ordering |')
    print('|---|---|---|---|---|---|---|---|---|')
    for d in ds:
        nat = d['natural']
        s = d['search'][0]['result']
        print(f"| {d['graph']} | {d['N']} | {d['edges']} | {d['girth']} | {d['random_set']['E_per_cell']:.1f} | "
              f"{d['random_ordering']['E_per_cell']:.1f} | {nat['best']['E_per_cell']:.1f} / {nat['mean']['E_per_cell']:.1f} / "
              f"{nat['worst']['E_per_cell']:.1f} | {s['E_per_cell']:.1f} | {s['E_per_cell'] / d['random_ordering']['E_per_cell']:.2f} |")
    print('\nCounts by type (fully black rectangles F, four-cell M4, six-cell M6, right angles RA and those completing inside)\n')
    print('| graph | layout | F | M4 | M6 | RA | RA inside | F per cell | M4 per cell | M6 per cell |')
    print('|---|---|---|---|---|---|---|---|---|---|')
    for d in ds:
        e = d['edges']
        for label, r in (('random set (mean)', d['random_set']), ('random ordering (mean)', d['random_ordering']),
                         ('natural (best)', d['natural']['best']), ('natural (mean)', d['natural']['mean']),
                         ('after search', d['search'][0]['result'])):
            print(f"| {d['graph']} | {label} | {r['full_black']:.0f} | {r['M4']:.0f} | {r['M6']:.0f} | {r['right_angles']:.0f} | "
                  f"{r['right_angles_completing_inside']:.0f} | {r['full_black'] / e:.2f} | {r['M4'] / e:.1f} | {r['M6'] / e:.1f} |")
    print('\nValid subsets (every one rechecked by the diagonal enumeration)\n')
    print('| graph | N | edges | searched ordering | best natural | random ordering | random set, same size | random insertion, whole grid (max) | frame 2N-1 | N^(6/5) | N^(4/3) |')
    print('|---|---|---|---|---|---|---|---|---|---|---|')
    for d in ds:
        v = d['valid_subsets']
        b = base[str(d['N'])]
        print(f"| {d['graph']} | {d['N']} | {d['edges']} | {v['best searched ordering']['best_valid_size']} | "
              f"{v['best natural ordering']['best_valid_size']} | {v['random ordering']['best_valid_size']} | "
              f"{v['random set']['best_valid_size']} | {b['max']} | {2 * d['N'] - 1} | {d['N'] ** 1.2:.0f} | {d['N'] ** (4 / 3):.0f} |")
    print('\nGreedy deletions needed (lazy greedy hitting set, before re-insertion)\n')
    print('| graph | searched ordering | best natural | random ordering | random set |\n|---|---|---|---|---|')
    for d in ds:
        v = d['valid_subsets']
        print(f"| {d['graph']} | " + ' | '.join(str(v[k]['greedy_deletions']) for k in
              ('best searched ordering', 'best natural ordering', 'random ordering', 'random set')) + ' |')
    print('\nNeighbouring rows or columns of the searched ordering that share a coordinate value\n')
    for d in ds:
        if 'best_ordering_structure' in d:
            print(f"- {d['graph']}: {d['best_ordering_structure']}")


if __name__ == '__main__':
    collect()
    sat_table()
    layout_tables()
