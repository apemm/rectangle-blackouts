"""Collect the certified window bounds into window_caps.json.

A bound (class, k) -> d is recorded only when the instance "at least d + 1
two-cell columns in a k-window" is UNSAT for both solvers in
window_results.jsonl.
"""
import json

SOLVERS = ('cadical195', 'glucose4')
seen = {}
for line in open('window_results.jsonl'):
    r = json.loads(line)
    assert r['kind'] == 'window' and r['h'] == 7
    key = (r['part_index'], r['m'], r['doubles_at_least'])
    seen.setdefault(key, {})[r['solver']] = r['status']
caps = {}
for (pi, k, d), res in sorted(seen.items()):
    if all(res.get(s) == 'UNSAT' for s in SOLVERS):
        cur = caps.setdefault(str(pi), {})
        cur[str(k)] = min(cur.get(str(k), k), d - 1)
json.dump({'solvers': SOLVERS, 'caps': {'7': caps}}, open('window_caps.json', 'w'), indent=1)
for pi, v in caps.items():
    print(pi, v)
print(len(caps), 'classes')
