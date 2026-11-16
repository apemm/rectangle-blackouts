import sys
from collections import Counter
from test_rule import run

def Rrow(h, iota):
    return max(y for y in range(2, h + 1) if y % 8 == (2 * iota + 1) % 8)

hs = [int(a) for a in sys.argv[1].split(',')]
verbose = len(sys.argv) > 2
for h in hs:
    W = (h * h) // 4 + 1
    A = (h + 1) // 2; K = h // 2
    M = (W // 2 + 10) // 8 * 8 + 8
    for iota in range(4):
        r = Rrow(h, iota)
        tot = Counter(); nlab = 0
        for s in range(-(A - 1), K):
            res, ex = run(h, s, iota, M, lambda n, rnd, r=r: r)
            nlab += sum(1 for i in range(A) if 0 <= i + s < K and i % 4 == iota)
            tot.update(res)
            if verbose and res:
                print('   s', s, dict(res), {k: ex[k][:1] for k in res})
        print(h, 'iota', iota, 'row', r, 'labels', nlab, 'total', sum(tot.values()), dict(sorted(tot.items())))
