# Census driver: build one region type, run the definition-level census, classify by family.
import sys, time, json
from collections import Counter
import numpy as np
from board import build
from census import run

LET = {1: 'S', 2: 'F', 3: 'H', 4: 'o', 5: 'e'}

def classify(viol, kind, blk, h):
    H1 = h + 1
    pt = lambda i: (i // H1, i % H1)
    def K(i):
        x, y = pt(i); return LET[int(kind[x, y])]
    def B(i):
        x, y = pt(i); return int(blk[x, y])
    def nblocks(ids):
        bs = {B(i) for i in ids if K(i) in 'oe'}
        return len(bs)
    fam = Counter(); examples = {}
    for v in viol:
        t = v[0]
        if t == 'V1':
            ids = v[1]
            name = 'V1 fully black ' + ''.join(sorted(K(i) for i in ids))
        elif t == 'V2':
            ia, ib, iv = v[1]
            name = 'V2 fatal triple (V=%s; %s,%s)' % (K(iv), *sorted([K(ia), K(ib)]))
            ids = v[1]
        elif t == 'V3':
            trip = ['(%s;%s,%s)' % (K(r[2]), *sorted([K(r[0]), K(r[1])])) for r in v[1]]
            name = 'V3 collision ' + '|'.join(sorted(trip))
            ids = [i for r in v[1] for i in r]
        elif t == 'A2':
            ia, ib = v[1]; w1, w2, mode = v[2]
            (x1, y1), (x2, y2) = pt(w1), pt(w2)
            if x1 == x2:
                sub = 'white pair vertical (rival-type)'
            elif y1 == y2:
                sub = 'white pair horizontal'
            else:
                sub = 'axis rectangle on white pair (R2 axis-aligned)'
            name = 'V4/V5 tilted %s-black %s%s + axis, %s' % ('side' if mode == 0 else 'diag', *sorted([K(ia), K(ib)]), sub)
            ids = v[1]
        else:  # T2
            recs = v[1]
            modes = sorted(r[2] for r in recs)
            if len(recs) == 2 and modes == [0, 1]:
                side = [r for r in recs if r[2] == 0][0]; diag = [r for r in recs if r[2] == 1][0]
                AB = ''.join(sorted([K(side[0]), K(side[1])])); CD = ''.join(sorted([K(diag[0]), K(diag[1])]))
                name = 'V4 mixed quadruple side %s / diag %s' % (AB, CD)
                ids = [side[0], side[1], diag[0], diag[1]]
                if 'S' not in AB + CD and 'F' not in AB + CD and 'H' not in AB + CD:
                    bA = {B(side[0]), B(side[1])}; bC = {B(diag[0]), B(diag[1])}
                    if len(bA | bC) == 1:
                        name += ' [I.1]'
                    elif len(bA) == 1 and len(bC) == 1:
                        name += ' [I.2]'
                    else:
                        name += ' [II or 3-block]'
            else:
                name = 'T2 same-type pair (compress) modes %s' % modes
                ids = [i for r in recs for i in r[:2]]
        nb = nblocks(ids)
        if nb >= 2:
            name += ' {cross-block}'
        fam[name] += 1
        if name not in examples:
            examples[name] = v
    return fam, examples

if __name__ == '__main__':
    h = int(sys.argv[1]); p = int(sys.argv[2]); nu = int(sys.argv[3])
    types = [(int(a), int(b)) for a, b in (s.split(',') for s in sys.argv[4].split(';'))]
    kappa = int(sys.argv[5]) if len(sys.argv) > 5 else 0
    split = int(sys.argv[6]) if len(sys.argv) > 6 else 1
    total = Counter()
    for (iota, mu) in types:
        t0 = time.time()
        kind, blk, info, labels, blocks = build(h, iota, mu, kappa, p, nu, extra_split=split)
        viol, st = run(kind, h, info['Xmax'])
        fam, ex = classify(viol, kind, blk, h)
        print('type iota=%d mu=%d r0=%d R=%d rho=%d blocks=%d labels=%d width=%d maxpos=%d | rect2=%d rect3=%d | %.1fs'
              % (iota, mu, info['r0'], info['R'], info['rho'], info['nblocks'], info['nlabels'],
                 info['width'], info['maxpos'], st['rect2'], st['rect3'], time.time() - t0))
        for k, c in sorted(fam.items(), key=lambda kv: -kv[1]):
            print('   %5d  %s' % (c, k))
        total.update(fam)
        sys.stdout.flush()
    print('TOTAL over types')
    for k, c in sorted(total.items(), key=lambda kv: -kv[1]):
        print('   %5d  %s' % (c, k))
