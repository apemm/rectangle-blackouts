"""Label-centric census of one region type of L***(3) (stride 12).
usage: py census12.py h iota sigma cmode rmode [start] [seed]
 cmode: board | stress | nocolour ; rmode: relaxed | exact ; RELOC env: file of 'iota sigma i j' lines to relocate.
Windows, anchors and classifier exactly as census_class.py: each subclass with kept labels gets the window
[4 n_lo - 2W_h - 64, 4 n_hi + 2W_h + 64]; anchors = every label point and every white point of a label column.
Writes every violation to log12_<h>_<iota>_<sigma>_<cmode>_<rmode>.txt and prints a summary."""
import sys, os, time
from collections import Counter
from lstar12 import params, build_type12, slot
from classify import WinBoard, run

h, iota, sigma = map(int, sys.argv[1:4]); cmode, rmode = sys.argv[4], sys.argv[5]
st = int(sys.argv[6]) if len(sys.argv) > 6 else 0
seed = int(sys.argv[7]) if len(sys.argv) > 7 else 1
reloc = None
if os.environ.get('RELOC'):
    reloc = set(tuple(map(int, ln.split())) for ln in open(os.environ['RELOC']) if ln.strip())
R = build_type12(h, iota, sigma, cmode, rmode, seed=seed, reloc=reloc)
P, p, tp, subs = R['P'], R['p'], R['tp'], R['subs']; W = P['W']
logf = 'log12_%d_%d_%d_%s_%s%s.txt' % (h, iota, sigma, cmode, rmode, '_reloc' if reloc else '')
log = open(logf, 'a' if st else 'w')
nlab = sum(len(s['labels']) for s in subs)
hdr = ('HDR h %d B %d l %d p %d type (%d,%d) r0 %d T0 %d D0 %d k %d T* %d frows %s subclasses %d kept %d removed %d heavy %d edges %d'
       % (h, P['B'], R['l'], p, iota, sigma, tp['r0'], tp['T0'], tp['D0'], tp['k'], tp['Ts'], tp['frows'],
          sum(1 for s in subs if s['labels']), nlab, sum(len(s['removed']) for s in subs), len(R['heavy']), R['nedges']))
if st == 0:
    print(hdr, file=log); print(hdr)
t0 = time.time(); fam = Counter(); i = st; npairs = 0; ntrip = 0; oobt = 0
while i < len(subs) and time.time() - t0 < 45:
    sc = subs[i]
    if sc['labels']:
        labs = {slot(a, sc['t'], p): (a, b) for (a, b) in sc['labels']}
        k = len(labs); npairs += k * (k - 1) // 2; ntrip += k * (k - 1) * (k - 2) // 6
        rho0 = next(iter(labs)) % 4
        n_lo = min(labs); n_hi = max(labs)
        X0 = 4 * n_lo - 2 * W - 64; Wd = 4 * (n_hi - n_lo) + 4 * W + 129
        bd = WinBoard(h, X0, Wd, tp, rho0, labels=labs)
        anc = []; wan = []
        for n, (a, b) in labs.items():
            x = 4 * n - X0
            anc += [(x, 2 * a + 1), (x, 2 * b + 2)]
            wan += [(x, y) for y in range(1, h + 1) if y not in (2 * a + 1, 2 * b + 2)]
        out, oob = run(bd, anc, wan)
        oobt += oob
        for (kind, f, det, data) in out:
            if kind == 'V1': pts = list(data)
            elif kind == 'V2': pts = list(data[0])
            elif kind == 'V3': pts = [z for Rr in data[1] for z in Rr] + [data[0]]
            elif kind == 'V4': pts = list(data[:4])
            else: pts = [(data[0], data[1]), (data[2], data[3])]
            L = sorted(set(bd.label_of(z[0]) for z in pts if bd.islabelcol(z[0])))
            nb = all(max(2 * a + 1, 2 * b + 2) >= tp['Ts'] - 320 or 2 * a + 1 <= 300 for a, b in L)
            fam[(kind, f, len(L), 'nearband' if nb else 'deep')] += 1
            print('VIOL sub', i, 'T', sc['T'], 'kind', kind, 'family', f, 'comp', det, 'nL', len(L), 'labels', L,
                  'nb', nb, 'X0', X0, 'data', data if kind != 'V3' else (data[0], len(data[1])), file=log)
    i += 1
summ = 'SUMMARY type (%d,%d) %s %s subs %d..%d of %d oob %d pairs %d triples %d time %.1f' % (
    iota, sigma, cmode, rmode, st, i, len(subs), oobt, npairs, ntrip, time.time() - t0)
print(summ, file=log); print(summ)
for key, v in sorted(fam.items()):
    print('  ', key, v, file=log); print('  ', key, v)
print('NEXT', i, len(subs)); print('NEXT', i, len(subs), file=log)
