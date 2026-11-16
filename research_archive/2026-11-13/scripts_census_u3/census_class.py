"""Label-centric census of L*** class windows.
usage: py census_class.py h iota sigma mode(relaxed|exact) start [seed] [lp_index]
Each subclass with kept labels gets its own window (labels + SAW*-shift fillers + shallow sea,
2W_h+64 columns of margin on each side). Anchors: every label point, and every white point of a
label column (for V2 with W in a double column). Prints one line per violation and a summary."""
import sys, time
from collections import Counter
from lstar import params, admissible_primes, build_type
from classify import WinBoard, run

h = int(sys.argv[1]); iota = int(sys.argv[2]); sigma = int(sys.argv[3]); mode = sys.argv[4]
st = int(sys.argv[5]); seed = int(sys.argv[6]) if len(sys.argv) > 6 else 1
lpi = int(sys.argv[7]) if len(sys.argv) > 7 else 0
P = params(h); W = P['W']
ls, ps = admissible_primes(h)
l = ls[lpi % len(ls)]; p = ps[lpi % len(ps)]
tp, subs, heavy = build_type(h, iota, sigma, l, p, seed=seed, mode=mode)
t0 = time.time()
ts = sorted(s['t'] for s in subs)
mingap = min((b - a) for a, b in zip(ts, ts[1:])) * 4 * p - 4 * P['A'] if len(ts) > 1 else None
if st == 0:
    print('HDR h', h, 'B', P['B'], 'l', l, 'p', p, 'type', (iota, sigma), {k: tp[k] for k in ('r0', 'yP', 'T0', 'D0', 'k', 'Ts', 'frows')},
          'subclasses', len(subs), 'kept labels', sum(len(s['labels']) for s in subs),
          'removed', sum(len(s['removed']) for s in subs), 'heavy diagonals', heavy,
          'min column gap between subclasses', mingap, '2W+1', 2 * W + 1, flush=True)
fam = Counter(); i = st
while i < len(subs) and time.time() - t0 < 40:
    sc = subs[i]
    if sc['labels']:
        labs = {}
        for (a, b) in sc['labels']:
            labs[a + p * sc['t']] = (a, b)   # slot n = i + p t (b_tau = 0, kappa = 0)
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
        for (kind, f, det, data) in out:
            # labels involved
            pts = []
            if kind == 'V1': pts = list(data)
            elif kind == 'V2': pts = list(data[0])
            elif kind == 'V3': pts = [z for R in data[1] for z in R] + [data[0]]
            elif kind == 'V4': pts = list(data[:4])
            else: pts = [(data[0], data[1]), (data[2], data[3])]
            L = sorted(set(bd.label_of(z[0]) for z in pts if bd.islabelcol(z[0])))
            maxrow = max(max(2 * a + 1, 2 * b + 2) for a, b in L) if L else None
            depth = tp['Ts'] - maxrow if L else None
            nb = all(max(2 * a + 1, 2 * b + 2) >= tp['Ts'] - 320 or 2 * a + 1 <= 300 for a, b in L)
            fam[(kind, f)] += 1
            print('VIOL sub', i, 'T', sc['T'], 'kind', kind, 'family', f, 'comp', det, 'labels', L, 'depth', depth,
                  'all_removed_by_exact_rules', nb, 'oob', oob, 'data', data if kind != 'V3' else (data[0], len(data[1])), flush=True)
    i += 1
print('SUMMARY type', (iota, sigma), 'subclasses', st, 'to', i, 'of', len(subs), dict(fam), 'time %.1f' % (time.time() - t0))
print('NEXT', i, len(subs))
