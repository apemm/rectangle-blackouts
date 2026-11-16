"""Complete census of the pure SAW*-shift gap with its shallow sea, for every distinct (r0, T*)
occurring among the 512 region types at height h. The pattern is 16-periodic, so anchoring every
black point of one period finds every obstruction up to translation.
usage: py pure_gap.py h [start count]"""
import sys, time
from collections import Counter
from lstar import params, type_params
from classify import WinBoard, run

h = int(sys.argv[1])
P = params(h); W = P['W']
cases = {}
for iota in range(32):
    for sigma in range(16):
        tp = type_params(h, iota, sigma)
        cases.setdefault((tp['r0'], tp['Ts']), tp)
keys = sorted(cases)
st = int(sys.argv[2]) if len(sys.argv) > 2 else 0
cnt = int(sys.argv[3]) if len(sys.argv) > 3 else len(keys)
t0 = time.time()
print('h', h, 'W_h', W, 'distinct (r0, T*):', len(keys))
for key in keys[st:st + cnt]:
    tp = cases[key]
    marg = 2 * W + 64
    Xc = 4 * (10 ** 6)  # core period start (deep slot 10^6, rho0 = 0)
    X0 = Xc - marg; Wd = 2 * marg + 16
    bd = WinBoard(h, X0, Wd, tp, 0)
    anchors = [(x, int(bd.R1[x])) for x in range(Xc - X0, Xc - X0 + 16)]
    out, oob = run(bd, anchors, [])
    c = Counter((v[0], v[1], v[2]) for v in out)
    print('r0', key[0], 'T*', key[1], 'D0', tp['D0'], 'k', tp['k'], 'filler rows', tp['frows'],
          'violations', len(out), dict(c), 'oob', oob, 'time %.1f' % (time.time() - t0), flush=True)
