"""Positive control: one window holding every label i of diagonal s with i = iota (mod step),
ignoring the G_T colouring and the split. usage: py control_class.py h iota sigma s step"""
import sys
from collections import Counter
from lstar import params, type_params, diag_graph
from classify import WinBoard, run
h, iota, sigma, s, step = map(int, sys.argv[1:6])
W = params(h)['W']; tp = type_params(h, iota, sigma)
I, D = diag_graph(h, s)
labs = {}
base = 10 ** 6 * 16
for i in I:
    if i % step == iota % step and i != 0 and int(sys.argv[6]) <= i < int(sys.argv[7]):
        labs[base + i] = (i, i + s)
rho0 = next(iter(labs)) % 4
n_lo, n_hi = min(labs), max(labs)
X0 = 4 * n_lo - 2 * W - 64; Wd = 4 * (n_hi - n_lo) + 4 * W + 129
bd = WinBoard(h, X0, Wd, tp, rho0, labels=labs)
anc = []; wan = []
for n, (a, b) in labs.items():
    x = 4 * n - X0; anc += [(x, 2 * a + 1), (x, 2 * b + 2)]
    wan += [(x, y) for y in range(1, h + 1) if y not in (2 * a + 1, 2 * b + 2)]
out, oob = run(bd, anc, wan)
print('control h', h, 'T', 2 * s + 1, 'D_T', D, 'labels', len(labs), 'violations', len(out), 'oob', oob)
for k, v in Counter((o[0], o[1], o[2]) for o in out).most_common(40): print('  ', k, v)
