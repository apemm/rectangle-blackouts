# Read archive arc certificates (read-only) and report, for M0 = 3..8,
# (1/h) * sum over diagonals with M_T > M0 of (k_T + 1), and max M_T.
import json, sys
for f in sys.argv[1:]:
    d = json.load(open(f)); h = d['h']; C = d['classes']
    out = [h, len(C), max(c['M'] for c in C)]
    for M0 in (3, 4, 5, 6, 8):
        out.append(round(sum(len(c['blocked']) + 1 for c in C if c['M'] > M0) / h, 3))
    out.append(round(sum(len(c['blocked']) for c in C) / h, 3))
    print(out, flush=True)
