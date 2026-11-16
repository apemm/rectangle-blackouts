import sys
from collections import Counter
from driver import build, analyse
from board import shapes

def labels_of(h, s, iota, M, imin=1):
    A = (h + 1) // 2; K = h // 2
    return [(4 * (i + M), 2 * i + 1, 2 * (i + s) + 2) for i in range(imin, A)
            if 0 <= i + s < K and i % 4 == iota]

def Rrow(h, iota):
    return max(y for y in range(2, h + 1) if y % 8 == (2 * iota + 1) % 8)

def run_rule(h, iota, rule_factory, Ms=(0,), verbose=0, imin=1):
    W = (h * h) // 4 + 1; A = (h + 1) // 2; K = h // 2
    S = shapes(h)
    tot = Counter(); nlab = 0; exs = {}
    for M0 in Ms:
        M = ((W // 2 + 10) // 16) * 16 + 16 + M0
        nu = (iota + M) % 4
        rule = rule_factory(h, iota, nu)
        Wd = 4 * (M + A) + 2 * W + 40
        for s in range(-(A - 1), K):
            labels = labels_of(h, s, iota, M, imin)
            if not labels: continue
            nlab += len(labels)
            kind = build(h, Wd, labels, rule)
            res, ex = analyse(h, kind, S)
            tot.update(res)
            for k in res:
                exs.setdefault(k, (s, M, ex[k][0]))
            if verbose and res:
                print('  s', s, 'M', M, dict(res))
    return tot, nlab, exs

def two_level(h, iota, nu):
    R = Rrow(h, iota)
    return lambda n: R - 8 if n % 4 == nu else R

def one_level(h, iota, nu):
    R = Rrow(h, iota)
    return lambda n: R

if __name__ == '__main__':
    hs = [int(a) for a in sys.argv[1].split(',')]
    which = sys.argv[2]
    fac = {'one': one_level, 'two': two_level}[which]
    for h in hs:
        for iota in range(4):
            tot, nlab, exs = run_rule(h, iota, fac, Ms=(0, 1, 2, 3))
            print(h, iota, 'R', Rrow(h, iota), 'labels', nlab, 'total', sum(tot.values()), dict(sorted(tot.items())))
            for k, v in sorted(exs.items()):
                print('     ', k, v)
