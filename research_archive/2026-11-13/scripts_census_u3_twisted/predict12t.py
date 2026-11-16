"""predict12.py (scripts_census_u3) on the TWISTED board, with a scan mode.
usage: py predict12t.py h cmode rmode scan            -> types with predicted D12/D13 quadruples
       py predict12t.py h cmode rmode iota sigma      -> predicted vs observed (logT12_...) for one type"""
import sys, re
from collections import Counter
from lstar12t import build_type12t, slot
h = int(sys.argv[1]); cmode, rmode = sys.argv[2], sys.argv[3]
s = 12
shapes = []
for t in range(-(h // 2) // 32 * 32, 211, 32):
    if t == 0: continue
    for delta in range(-40 * h * s, 40 * h * s + 1, 16):
        den = 4 * (delta - s * t)
        if den == 0: continue
        num = delta * delta + 4 * t * t
        if num % den: continue
        a = num // den
        if a % 4: continue
        if (a * (delta - 2 * s * t)) % (2 * t): continue
        Y1 = a * (delta - 2 * s * t) // (2 * t); Y2 = Y1 - 2 * t
        if 1 <= Y1 < h and 1 <= Y2 < h:
            shapes.append((t, delta, a, a - delta, Y1, Y2))


def predict(io, sg):
    R = build_type12t(h, io, sg, cmode, rmode); p = R['p']; tp = R['tp']
    pred = {}
    for sc in R['subs']:
        labs = {slot(i, sc['t'], p): (i, j) for (i, j) in sc['labels']}
        if len(labs) < 2: continue
        rho0 = next(iter(labs)) % 4
        byi = {i: n for n, (i, j) in labs.items()}
        def black(X, y):
            if X % 4: return y == tp['r0']
            n = X // 4
            if n in labs: i, j = labs[n]; return y in (2 * i + 1, 2 * j + 2)
            return y == tp['Ts'] - 24 + 8 * ((n - rho0) % 4)
        for n1, (i1, j1) in labs.items():
            for (t, delta, a, c, Y1, Y2) in shapes:
                i2 = i1 + t
                if i2 not in byi: continue
                n2 = byi[i2]; j2 = labs[n2][1]
                for par in ('o', 'e'):
                    y1 = 2 * i1 + 1 if par == 'o' else 2 * j1 + 2
                    y2 = 2 * i2 + 1 if par == 'o' else 2 * j2 + 2
                    Y = y1 + Y1
                    if y2 != Y - Y2: continue
                    L1 = (4 * n1, y1); L2 = (4 * n2, y2); F1 = (4 * n1 + a, Y); F2 = (4 * n2 + c, Y)
                    if not all(black(*z) for z in (L1, F1, L2, F2)): continue
                    if (F1[0] // 4) in labs or (F2[0] // 4) in labs: continue
                    nv = ((2 * s * t - delta) // 2, t)
                    pp = (L1[0] + nv[0], L1[1] + nv[1]); q = (F1[0] + nv[0], F1[1] + nv[1])
                    if not all(1 <= z[1] <= h for z in (pp, q)): continue
                    pred[frozenset((L1, F1, L2, F2))] = (t, Y1, par, (i1, j1), (i2, j2))
    return pred, tp


print('h', h, 'shapes', len(shapes), sorted(set((x[0], x[4]) for x in shapes)))
if sys.argv[4] == 'scan':
    tot = Counter()
    for io in range(32):
        for sg in range(16):
            pred, tp = predict(io, sg)
            if pred:
                print('type', (io, sg), 'k', tp['k'], 'T*', tp['Ts'], 'predicted', len(pred),
                      sorted(Counter((v[0], v[1], v[2]) for v in pred.values()).items()))
                tot[(io, sg)] = len(pred)
    print('types with predictions', len(tot), 'total', sum(tot.values()))
else:
    io, sg = int(sys.argv[4]), int(sys.argv[5])
    pred, tp = predict(io, sg)
    obs = set()
    for ln in open('logT12_%d_%d_%d_%s_%s.txt' % (h, io, sg, cmode, rmode)):
        if ln.startswith('VIOL') and re.search(r'family D1[23]', ln):
            X0 = int(re.search(r' X0 (-?\d+)', ln).group(1))
            d = eval(re.search(r'data (\(.*\))', ln).group(1))
            obs.add(frozenset((z[0] + X0, z[1]) for z in d[:4]))
    print('predicted', len(pred), 'observed D12/D13', len(obs), 'equal', set(pred) == obs)
    for v in sorted(set(pred.values())):
        print('  ', v)
