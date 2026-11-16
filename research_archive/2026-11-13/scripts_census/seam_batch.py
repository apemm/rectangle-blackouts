"""Batch driver for the seam census. Jobs: one line per (h, r0, D0, k, end, phase).
usage: py seam_batch.py jobs.txt start   (stops after ~48 s, prints the next start index)"""
import sys, time
from collections import Counter
from lstar import params, type_params, g_of, j1star_bad
from classify import WinBoard, run
jobs = [tuple(int(z) if z.lstrip('-').isdigit() else z for z in ln.split()) for ln in open(sys.argv[1]) if ln.strip()]
st = int(sys.argv[2]); t0 = time.time(); i = st
while i < len(jobs) and time.time() - t0 < 40:
    h, r0, D0, k, end, ph = jobs[i]
    W = params(h)['W']; g = g_of(h)
    tp = next(q for q in (type_params(h, a, b) for a in range(32) for b in range(16)) if q['r0'] == r0 and q['D0'] == D0)
    tq = dict(tp); tq['k'] = k; tq['Ts'] = tp['T0'] - 64 * k
    ns = 10 ** 6 + ph; Xs = 4 * ns; marg = 4 * W + 160; X0 = Xs - marg; Wd = 2 * marg
    bd = WinBoard(h, X0, Wd, tq, 0, seam=(end, ns), g=g)
    rng = range(Xs - X0 - 2 * W - 16, Xs - X0) if end == 'R' else range(Xs - X0, Xs - X0 + 2 * W + 16)
    anc = [(x, int(bd.R1[x])) for x in rng if (x + X0) % 4 == 0]
    out, oob = run(bd, anc, [], req=g)
    c = Counter((v[0], v[1], v[2]) for v in out)
    rv = []
    for v in out:
        if v[0] == 'V5':
            a, b = (v[3][0], v[3][1]), (v[3][2], v[3][3])
            f = a if bd.tag(*a) != 'g' else b
            rv.append((bd.tag(*f)[1:], abs(a[0] - b[0]) // 4, v[3][4]))
    print('JOB', i, 'h', h, 'r0', r0, 'D0', D0, 'k', k, 'T*', tq['Ts'], 'end', end, 'ph', ph, 'nviol', len(out),
          dict(c), 'rival(o,kap,j)', sorted(set(rv)), 'J1*bad', j1star_bad(h, r0, D0) if k == 0 else [], 'oob', oob, flush=True)
    i += 1
print('NEXT', i, 'of', len(jobs), 'time %.1f' % (time.time() - t0))
