"""Theorem E block at definition level: h = 112, profile (3, 9, 110, 2), whole diagonals T in
{-7, 7, 21}, two weight classes (split at the median of v), centres by resampling."""
import time, random, json
from blib import *
t0 = time.time()
h = 112; prof = (3, 9, 110, 2); D = 2 * Wh(h) + 1
rows = [r for r in range(1, h + 1) if row_ok(h, prof, r)]
labs = [(a, b) for a in rows if a % 2 for b in rows if b % 2 == 0]
E = [e for e in labs if e[1] - e[0] in (-7, 7, 21)]
v = {e: vweight(prof, e) for e in E}
med = sorted(v.values())[len(E) // 2]
cls = [[e for e in E if v[e] < med], [e for e in E if v[e] >= med]]
print('n =', len(E), 'class sizes', [len(c) for c in cls], 'v range', min(v.values()), max(v.values()))
rng = random.Random(20261114)
classes = []
for c in cls:
    N = 30 * len(c)
    place, hist = place_class(h, prof, D, c, N, rng)
    print('class n=%d N=%d iterations=%d first=%s' % (len(c), N, len(hist), hist[0]), flush=True)
    assert place is not None
    classes.append((N, place))
lay = Layout(h)
lay.seg(D, lambda x: 1, 'row1'); z = lay.x()          # switch z: row 1 left, row h right
build_block(lay, prof, classes, D)
print('switch z =', z, 'width', len(lay.col), 'time', round(time.time() - t0, 1), flush=True)
f, st = check_windows(lay, D)
print('records', {k: len(x) for k, x in f.items()})
# bookkeeping: singletons / doubles / placed edges
dbl = [x for x in range(len(lay.col)) if len(lay.col[x]) == 2]
edges = [tuple(sorted(lay.col[x])) for x in dbl]
print('columns', len(lay.col), 'doubles', len(dbl), 'distinct edges', len(set(edges)),
      'received', len(E), 'edges == received:', set(edges) == set(tuple(sorted(e)) for e in E),
      'all parity edges:', all((a + b) % 2 == 1 for a, b in edges),
      'other columns singletons:', all(len(lay.col[x]) == 1 for x in range(len(lay.col)) if x not in set(dbl)))
print('left end rows', set(r for c in lay.col[z:z + D] for r in c), 'right end rows', set(r for c in lay.col[-D:] for r in c))
json.dump({'h': h, 'prof': prof, 'classes': [[N, [[list(e), s] for e, s in p.items()]] for N, p in classes]},
          open('eblock_h112.json', 'w'))
print('time', round(time.time() - t0, 1))
