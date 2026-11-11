"""Tabulate the result files of this folder into summary.json and print tables."""
import json
import os

CLASSES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 19, 20, 25]
SOLVERS = ('cadical195', 'glucose4')


def load(name):
    if not os.path.exists(name):
        return []
    return [json.loads(l) for l in open(name) if l.strip()]


def main():
    out = {}
    # height 7 equality instances
    table = {}
    for r in load('struct_results.jsonl'):
        cell = table.setdefault(r['m'], {s: {} for s in SOLVERS})
        cell[r['solver']][r['part_index']] = (r['status'], r['solve_seconds'])
    out['height_7_equality'] = {}
    print('width | cadical195 UNSAT classes | glucose4 UNSAT classes | both | seconds')
    for m in sorted(table):
        row = {}
        for s in SOLVERS:
            done = sorted(p for p, (st, _) in table[m][s].items() if st == 'UNSAT')
            other = sorted(p for p, (st, _) in table[m][s].items() if st != 'UNSAT')
            row[s] = {'unsat_classes': done, 'other': other,
                      'seconds': round(sum(t for _, t in table[m][s].values()), 1)}
        both = sorted(set(row[SOLVERS[0]]['unsat_classes']) & set(row[SOLVERS[1]]['unsat_classes']))
        row['both'] = both
        row['missing_any'] = sorted(set(CLASSES) - set(row[SOLVERS[0]]['unsat_classes'])
                                    - set(row[SOLVERS[1]]['unsat_classes']))
        out['height_7_equality'][m] = row
        print(m, '|', len(row[SOLVERS[0]]['unsat_classes']), '|', len(row[SOLVERS[1]]['unsat_classes']),
              '|', len(both), '|', row[SOLVERS[0]]['seconds'], row[SOLVERS[1]]['seconds'],
              '| SAT or other:', row[SOLVERS[0]]['other'], row[SOLVERS[1]]['other'])
    out['incidents'] = load('struct_incidents.jsonl')
    # window bounds
    w = load('window_results.jsonl')
    kept = [r for r in w if os.path.exists(os.path.join('proofs', r['proof']['drat']['file']))]
    out['window_bounds'] = {'instances': len(w), 'unsat': sum(r['status'] == 'UNSAT' for r in w),
                            'proof_files_kept': len(kept),
                            'proof_bytes_kept': sum(r['proof']['drat']['bytes'] for r in kept),
                            'proof_bytes_total': sum(r['proof']['drat']['bytes'] for r in w),
                            'solve_seconds': round(sum(r['solve_seconds'] for r in w), 1)}
    print('window instances', out['window_bounds'])
    # small heights
    small = {}
    for r in load('sanity_small_heights.jsonl'):
        key = f"{r['kind']} h={r['h']} m={r['m']}" + (f" k={r['k']}" if 'k' in r else '')
        cell = small.setdefault(key, {})
        cell.setdefault(r['solver'], {}).setdefault(r['status'], 0)
        cell[r['solver']][r['status']] += 1
    out['small_heights'] = small
    for k in sorted(small):
        print(k, small[k])
    out['acceptance'] = [{'part_index': r['part_index'], 'word': r['fixed_word'], 'status': r['status']}
                         for r in load('acceptance_results.jsonl')]
    json.dump(out, open('summary.json', 'w'), indent=1)


if __name__ == '__main__':
    main()
