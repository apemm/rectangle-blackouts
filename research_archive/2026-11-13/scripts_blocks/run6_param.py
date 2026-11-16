"""Same E/D/switch layout as run4 for another (h, profile), given on the command line."""
import sys, time, random
from collections import Counter
from blib import *
t0 = time.time()
h = int(sys.argv[1]); prof = tuple(int(t) for t in sys.argv[2].split(',')); seed = int(sys.argv[3])
assert profile_ok(h, *prof)
D = 2 * Wh(h) + 1
rows = [r for r in range(1, h + 1) if row_ok(h, prof, r)]
labs = [(a, b) for a in rows if a % 2 for b in rows if b % 2 == 0]
nb1 = sum(class_violations(h, prof, D, 1, {e: 0})[1] > 0 for e in labs)
diags = [T for T, _ in Counter(b - a for a, b in labs).most_common()]
rng = random.Random(seed)
E = [e for e in labs if e[1] - e[0] in diags[:3]]
v = {e: vweight(prof, e) for e in E}; med = sorted(v.values())[len(E) // 2]
Ecls = [c for c in ([e for e in E if v[e] < med], [e for e in E if v[e] >= med]) if c]
S = [e for e in labs if e[1] - e[0] in diags[3:9]]
Y = [e for e in S if rng.random() < 0.5]
ED = [rng.choice(Y)] if Y else []
Yp = [e for e in Y if e not in ED]
vy = {e: vweight(prof, e) for e in Yp}; my = sorted(vy.values())[len(Yp) // 2] if Yp else 0
Dcls = [c for c in ([e for e in Yp if vy[e] < my], [e for e in Yp if vy[e] >= my]) if c]
print('h=%d prof=%s D=%d rows=%d labels=%d one-label failures=%d | E diags %s n=%d | D diags %s |S|=%d |Y|=%d placed=%d'
      % (h, prof, D, len(rows), len(labs), nb1, diags[:3], len(E), diags[3:9], len(S), len(Y), len(Yp)), flush=True)
blocks = []
for name, cl, mult in (('E', Ecls, None), ('D', Dcls, 30 * len(S) // max(1, len(Dcls)))):
    cs = []
    for c in cl:
        N = mult if mult else 30 * len(c)
        place, hist = place_class(h, prof, D, c, N, rng, strict=True)
        assert place is not None
        print(name, 'class n=%d N=%d its=%d' % (len(c), N, len(hist)), flush=True)
        cs.append((N, place))
    blocks.append((name, cs))
lay = Layout(h)
lay.seg(D, lambda x: 1, 'row1'); z = lay.x()
for name, cs in blocks:
    build_block(lay, prof, cs, D)
lay.seg(D, lambda x: h, 'tail_h')
f, st = check_windows(lay, D)
dbl = {x: tuple(sorted(lay.col[x])) for x in range(len(lay.col)) if len(lay.col[x]) == 2}
recv = set(tuple(sorted(e)) for e in E + Yp)
print('width', len(lay.col), 'windows', len(st), 'records', {k: len(x) for k, x in f.items()},
      '| doubles', len(dbl), 'distinct', len(set(dbl.values())), '== received:', set(dbl.values()) == recv,
      '| singletons elsewhere:', all(len(lay.col[x]) == 1 for x in range(len(lay.col)) if x not in dbl),
      '| last column', lay.col[-1], '| rows used', sorted(set(r for c in lay.col for r in c) - set(rows)), round(time.time() - t0, 1))
