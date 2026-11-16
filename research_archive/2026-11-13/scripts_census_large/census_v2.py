"""Label-centric census of consolidated_board_v2 (B7) survivors, one region type per run.
usage: py census_v2.py h iota sigma mode start [nosplit] [relocfile]
 mode: exact (v2 R-a, R-b with the k=2 extension, R-c) or exactS1L (without the 444 extension).
 Windows, anchors and the checker are those of scripts_census/census_class.py (validated):
 each subclass with kept labels gets its own window (label columns +- (2W_h + 64)), anchors are
 every label point and every white point of a label column.
 relocfile: lines 'iota sigma i j' of labels relocated by census-driven rules (closure run)."""
import sys, time, os
import numpy as np
from collections import Counter
import checker
from core import _divcount, _divfill
from v2board import build_type_v2, params, admissible_primes
from classify import WinBoard, run
from fastboard import FastWinBoard, Template
NCHECK = int(os.environ.get('NCHECK', '3'))


def divisor_table32(NMAX):
    cnt = np.zeros(NMAX + 1, dtype=np.int64)
    _divcount(NMAX, cnt)
    dstart = np.zeros(NMAX + 2, dtype=np.int64)
    np.cumsum(cnt, out=dstart[1:])
    del cnt
    dlist = np.zeros(dstart[-1], dtype=np.int32)
    _divfill(NMAX, dstart, dlist)
    return dstart, dlist


h = int(sys.argv[1]); iota = int(sys.argv[2]); sigma = int(sys.argv[3]); mode = sys.argv[4]
st = int(sys.argv[5]); nosplit = len(sys.argv) > 6 and sys.argv[6] == 'nosplit'
relf = sys.argv[7] if len(sys.argv) > 7 else None
TL = float(os.environ.get('TL', '45'))
t00 = time.time()
checker._DIV[h * h] = divisor_table32(h * h)
tdiv = time.time() - t00
reloc = set()
if relf:
    for ln in open(relf):
        a = ln.split()
        if len(a) == 4 and int(a[0]) == iota and int(a[1]) == sigma:
            reloc.add((int(a[2]), int(a[3])))
P = params(h); W = P['W']
ls, ps = admissible_primes(h); l, p = ls[0], ps[0]
tp, subs, heavy = build_type_v2(h, iota, sigma, l, p, mode=mode, nosplit=nosplit, reloc=reloc, graph=bool(os.environ.get('GRAPH')))
t0 = time.time()
sizes = Counter(len(s['labels']) for s in subs if s['labels'])
if st == 0:
    print('HDR h', h, 'B', P['B'], 'l', l, 'p', p, 'type', (iota, sigma), 'mode', mode, 'nosplit', nosplit, 'NOCOLOUR', os.environ.get('NOCOLOUR'), 'RHOSHIFT', os.environ.get('RHOSHIFT'), 'GRAPH', os.environ.get('GRAPH'),
          {k: tp[k] for k in ('r0', 'yP', 'T0', 'D0', 'k', 'Ts', 'frows')},
          'subclasses', len(subs), 'kept', sum(len(s['labels']) for s in subs), 'relocfile', len(reloc),
          'sizes', sorted(sizes.items()), 'removal reasons', dict(Counter(w.split(' |')[0] if 'R_FF^oo' in w or 'R_FF^ee' in w else w for s_ in subs for r in s_['removed'] for w in set(r[2]))), 'heavy', heavy, 'divtable %.1fs' % tdiv, flush=True)
fam = Counter(); i = st; nwin = 0; tmpl = None; nchecked = 0
while i < len(subs) and time.time() - t0 < TL:
    sc = subs[i]
    if sc['labels']:
        labs = {a + p * sc['t']: (a, b) for (a, b) in sc['labels']}
        rho0 = (next(iter(labs)) + int(os.environ.get('RHOSHIFT', '0'))) % 4   # RHOSHIFT != 0 breaks [F1] (control)
        n_lo = min(labs); n_hi = max(labs)
        X0 = 4 * n_lo - 2 * W - 64; Wd = 4 * (n_hi - n_lo) + 4 * W + 129
        if tmpl is None:
            Lmax = max(4 * (max(a + p * s_['t'] for a, b in s_['labels']) - min(a + p * s_['t'] for a, b in s_['labels'])) for s_ in subs if s_['labels']) + 4 * W + 129
            tmpl = Template(tp, rho0, Lmax)
        bd = FastWinBoard(h, X0, Wd, tp, rho0, labs, tmpl)
        if nwin < NCHECK:   # the fast board must equal the validated WinBoard
            ref = WinBoard(h, X0, Wd, tp, rho0, labels=labs)
            assert (ref.R1 == bd.R1).all() and (ref.R2 == bd.R2).all() and (ref.rows() == bd.rows()).all()
            nchecked += 1
        anc = []; wan = []
        for n, (a, b) in labs.items():
            x = 4 * n - X0
            anc += [(x, 2 * a + 1), (x, 2 * b + 2)]
            wan += [(x, y) for y in range(1, h + 1) if y not in (2 * a + 1, 2 * b + 2)]
        out, oob = run(bd, anc, wan)
        nwin += 1
        for (kind, f, det, data) in out:
            if kind == 'V1': pts = list(data)
            elif kind == 'V2': pts = list(data[0])
            elif kind == 'V3': pts = [z for R in data[1] for z in R] + [data[0]]
            elif kind == 'V4': pts = list(data[:4])
            else: pts = [(data[0], data[1]), (data[2], data[3])]
            L = sorted(set(bd.label_of(z[0]) for z in pts if bd.islabelcol(z[0])))
            fam[(kind, f)] += 1
            print('VIOL sub', i, 'size', len(labs), 'T', sc['T'], 'cT', sc['cT'], 'kind', kind, 'family', f, 'comp', det,
                  'labels', L, 'oob', oob, 'data', data if kind != 'V3' else (data[0], len(data[1])), flush=True)
    i += 1
print('SUMMARY type', (iota, sigma), 'subclasses', st, 'to', i, 'of', len(subs), 'windows', nwin, 'fastboard-checked', nchecked, dict(fam),
      'time %.1f' % (time.time() - t0))
print('NEXT', i, len(subs))
