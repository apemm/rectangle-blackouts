"""Theorem E block (whole diagonals -7, 7, 21) and Theorem D block (random half of the labels of
diagonals 3, 35, -21, minus a simulated exceptional set E_D, with S's slot count), strict T1 mode
(no tilted rectangle with 3 black corners and a label corner), glued right of a row-1/row-h switch."""
import time, random
from blib import *
t0 = time.time()
h = 112; prof = (3, 9, 110, 2); D = 2 * Wh(h) + 1
rows = [r for r in range(1, h + 1) if row_ok(h, prof, r)]
labs = [(a, b) for a in rows if a % 2 for b in rows if b % 2 == 0]
rng = random.Random(14112026)
# Theorem E instance
E = [e for e in labs if e[1] - e[0] in (-7, 7, 21)]
v = {e: vweight(prof, e) for e in E}
med = sorted(v.values())[len(E) // 2]
Ecls = [[e for e in E if v[e] < med], [e for e in E if v[e] >= med]]
# Theorem D instance: Y independent across diagonals (here iid Bernoulli(1/2) per label)
S = [e for e in labs if e[1] - e[0] in (3, 35, -21)]
Y = [e for e in S if rng.random() < 0.5]
ED = [rng.choice(Y)]
Yp = [e for e in Y if e not in ED]
print('E: n=%d classes %s | D: |S|=%d |Y|=%d |E_D|=%d placed %d' % (len(E), [len(c) for c in Ecls], len(S), len(Y), len(ED), len(Yp)))
blocks = []
for name, cl, Nfun in (('E', Ecls, lambda c: 30 * len(c)), ('D', [Yp], lambda c: 30 * len(S))):
    cs = []
    for c in cl:
        N = Nfun(c)
        place, hist = place_class(h, prof, D, c, N, rng, strict=True)
        assert place is not None
        print(name, 'class n=%d N=%d its=%d first=%s last=%s' % (len(c), N, len(hist), hist[0][2], hist[-1][2]), flush=True)
        cs.append((N, place))
    blocks.append((name, cs))
lay = Layout(h)
lay.seg(D, lambda x: 1, 'row1'); z = lay.x()
spans = []
for name, cs in blocks:
    a = lay.x(); build_block(lay, prof, cs, D); spans.append((name, a, lay.x()))
lay.seg(D, lambda x: h, 'tail_h')
print('z =', z, 'spans', spans, 'width', len(lay.col), flush=True)
f, st = check_windows(lay, D)
print('records', {k: len(x) for k, x in f.items()}, 'windows', len(st), round(time.time() - t0, 1))
# bookkeeping
dbl = {x: tuple(sorted(lay.col[x])) for x in range(len(lay.col)) if len(lay.col[x]) == 2}
recv = set(tuple(sorted(e)) for e in E + Yp)
print('doubles', len(dbl), 'distinct', len(set(dbl.values())), '== received E u (Y minus E_D):', set(dbl.values()) == recv,
      '| E_D placed?', any(tuple(sorted(e)) in set(dbl.values()) for e in ED),
      '| non-label columns singletons:', all(len(lay.col[x]) == 1 for x in range(len(lay.col)) if x not in dbl),
      '| max points per column', max(len(c) for c in lay.col))
for name, a, b in spans:
    inner = [x for x in dbl if a <= x < b]
    print(name, 'block: first/last column rows', lay.col[a], lay.col[b - 1], 'label columns', len(inner),
          'gap to nearest other window >= D:', all(abs(x - y) > D for x in inner for (n2, a2, b2) in spans if n2 != name for y in dbl if a2 <= y < b2))
unused = sum(1 for x in range(len(lay.col)) if lay.tag[x].startswith('core') and x % 7 == 0)
print('unused period-zero slots holding F:', unused, all(lay.col[x] == (prof[1],) for x in range(len(lay.col)) if lay.tag[x].startswith('core') and x % 7 == 0))
print('time', round(time.time() - t0, 1))
