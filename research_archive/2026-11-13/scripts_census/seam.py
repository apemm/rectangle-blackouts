"""Definition-level census of the seam SAW*-shift | Sea(r0, g) (both ends, all 4 phases).
Every obstruction with a SAW* filler and any other point is found: all fillers within 2W_h+16
columns of the seam are anchors. Reports violations that contain a row-g point (seam) and,
as a sanity check, those without one (must be none: pure gap is clean).
usage: py seam.py h r0 Ts_override(-1) end(R/L) phases(e.g. 0123) [D0 list filter]"""
import sys, time
from collections import Counter
from lstar import params, type_params, g_of, j1star_bad, k_shift
from classify import WinBoard, run

h = int(sys.argv[1]); r0 = int(sys.argv[2]); end = sys.argv[3]; phases = [int(c) for c in sys.argv[4]]
D0s = [int(z) for z in sys.argv[5].split(',')]
ks = [int(z) for z in sys.argv[6].split(',')] if len(sys.argv) > 6 else None
P = params(h); W = P['W']; g = g_of(h)
t0 = time.time()
for D0 in D0s:
    # find a type with this (r0, D0)
    tp = None
    for iota in range(32):
        for sigma in range(16):
            q = type_params(h, iota, sigma)
            if q['r0'] == r0 and q['D0'] == D0:
                tp = q; break
        if tp: break
    if tp is None:
        print('no type with r0', r0, 'D0', D0); continue
    for k in (ks if ks is not None else [tp['k']]):
        tq = dict(tp); tq['k'] = k; tq['Ts'] = tp['T0'] - 64 * k
        tq['frows'] = [tq['Ts'] - 24 + 8 * o for o in range(4)]
        for ph in phases:
            ns = 10 ** 6 + ph  # rho0 = 0, so n0 - rho0 = ph
            Xs = 4 * ns
            marg = 4 * W + 160
            X0 = Xs - marg; Wd = 2 * marg
            bd = WinBoard(h, X0, Wd, tq, 0, seam=(end, ns), g=g)
            if end == 'R':
                anc = [(x, int(bd.R1[x])) for x in range(Xs - X0 - 2 * W - 16, Xs - X0) if (x + X0) % 4 == 0]
            else:
                anc = [(x, int(bd.R1[x])) for x in range(Xs - X0, Xs - X0 + 2 * W + 16) if (x + X0) % 4 == 0]
            out, oob = run(bd, anc, [])
            c = Counter((v[0], v[1], v[2]) for v in out)
            # rival pairs filler-g: offsets and slot distance
            rv = sorted(set(((bd.tag(v[3][0], v[3][1]) if bd.tag(v[3][0], v[3][1]) != 'g' else bd.tag(v[3][2], v[3][3])),
                             abs(v[3][2] - v[3][0]) // 4, v[3][4]) for v in out if v[0] == 'V5'))
            pred_bad = j1star_bad(h, r0, D0) if k == 0 else []
            print('h', h, 'r0', r0, 'g', g, 'D0', D0, 'k', k, 'T*', tq['Ts'], 'end', end, 'phase', ph, 'anchors', len(anc),
                  'violations', len(out), dict(c), 'rival(offset,kappa,j)', rv, 'J1* bad pair', pred_bad, 'oob', oob,
                  'time %.1f' % (time.time() - t0), flush=True)
