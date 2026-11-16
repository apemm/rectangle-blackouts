"""Positive control (not the board): K consecutive slots of one diagonal s, starting at slot index i0,
put in one class at stride 12 (slot n = 3 i + p t, column 4n).  This breaks G_T independence and the
mod-32 rule, so the checker must report A2 rival pairs (o, e) at slot distances in D_T (stride 12).
usage: py ctrl12.py h s i0 K iota"""
import sys, time
from collections import Counter
from lstar12 import params, primes12, diag_graph12, slot
from lstar import type_params
from classify import WinBoard, run
h, s, i0, K, iota = map(int, sys.argv[1:6])
P = params(h); W = P['W']; l, p = primes12(h)
sigma = s % 16; tp = type_params(h, iota, sigma)
I, D = diag_graph12(h, s)
V = I[i0:i0 + K]
t = (pow(p, -1, 16 * l) * s) % (16 * l)
labs = {slot(i, t, p): (i, i + s) for i in V}
rho0 = slot(V[0], t, p) % 4
n_lo, n_hi = min(labs), max(labs)
X0 = 4 * n_lo - 2 * W - 64; Wd = 4 * (n_hi - n_lo) + 4 * W + 129
bd = WinBoard(h, X0, Wd, tp, rho0, labels=labs)
anc = []
for n, (a, b) in labs.items():
    x = 4 * n - X0; anc += [(x, 2 * a + 1), (x, 2 * b + 2)]
t0 = time.time()
out, oob = run(bd, anc, [])
c = Counter((v[0], v[1]) for v in out)
print('h', h, 's', s, 'T', 2 * s + 1, 'D_T', D, 'slots', V[0], '..', V[-1], 'violations', len(out), dict(c), 'oob', oob, 'time %.1f' % (time.time() - t0))
a2 = [v for v in out if v[1] == 'A2']
dist = Counter()
for v in a2:
    (x1, y1, x2, y2, j) = v[3]
    dist[abs(x2 - x1) // 12] += 1
print('A2 slot distances', dict(dist), 'all in D_T:', all(d in D for d in dist))
