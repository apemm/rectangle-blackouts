"""Compare a twisted census log with the untwisted one of the same (h, type, modes).
VIOL lines are compared as multisets after deleting the window origin ' X0 <int>' (data are window-local).
usage: py cmp_tw.py logT12_... untw/log12_..."""
import sys, re
from collections import Counter


def viol(f):
    c = Counter(); x0 = []
    for ln in open(f):
        if ln.startswith('VIOL'):
            m = re.search(r' X0 (-?\d+)', ln)
            x0.append(int(m.group(1)))
            c[re.sub(r' X0 -?\d+', '', ln.strip())] += 1
    return c, x0


a, xa = viol(sys.argv[1]); b, xb = viol(sys.argv[2])
fa = Counter(); fb = Counter()
for k, v in a.items():
    fa[re.search(r'family (.*?) comp', k).group(1)] += v
for k, v in b.items():
    fb[re.search(r'family (.*?) comp', k).group(1)] += v
print(sys.argv[1], 'twisted', sum(a.values()), 'untwisted', sum(b.values()), 'identical multiset', a == b,
      'only-twisted', sum((a - b).values()), 'only-untwisted', sum((b - a).values()))
print('   families twisted', dict(sorted(fa.items())))
if fa != fb:
    print('   families untwisted', dict(sorted(fb.items())))
