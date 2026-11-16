"""Rule BH-alt (four filler rows by class c = (n - nu) mod 4, labels at class 0, i = iota8 mod 8).
r1 = 2*iota8+1 mod 16. X = largest row <= h with X = r1+4 mod 8.
class1: X ; class2: X-8 ; class3: X-16 ; class0 (holes): largest row <= h with = r1+8 mod 16.
usage: py t_alt.py h iota8 s-list [M mod 4] [swap]"""
import sys, time
from collections import Counter
from driver import build, analyse
from board import shapes

def rows_alt(h, iota8):
    r1 = (2 * iota8 + 1) % 16
    X = max(y for y in range(2, h + 1) if y % 8 == (r1 + 4) % 8)
    r0 = max(y for y in range(2, h + 1) if y % 16 == (r1 + 8) % 16)
    return {0: r0, 1: X, 2: X - 8, 3: X - 16}

def run(h, iota8, s, Mres, S, imin=1, rows=None):
    W = (h * h) // 4 + 1; A = (h + 1) // 2; K = h // 2
    M = ((W // 2 + 10) // 16) * 16 + 16 + Mres
    nu = (iota8 + M) % 4
    rows = rows or rows_alt(h, iota8)
    labels = [(4 * (i + M), 2 * i + 1, 2 * (i + s) + 2) for i in range(imin, A)
              if 0 <= i + s < K and i % 8 == iota8]
    Wd = 4 * (M + A) + 2 * W + 40
    rule = lambda n: rows[(n - nu) % 4]
    kind = build(h, Wd, labels, rule)
    res, ex = analyse(h, kind, S)
    return res, ex, len(labels), rows

if __name__ == '__main__':
    h = int(sys.argv[1]); iota8 = int(sys.argv[2])
    ss = [int(a) for a in sys.argv[3].split(',')]
    Mres = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    S = shapes(h); t = time.time(); tot = Counter(); nl = 0
    for s in ss:
        res, ex, n, rows = run(h, iota8, s, Mres, S)
        nl += n; tot.update(res)
        print('s', s, 'labels', n, rows, dict(sorted(res.items())), flush=True)
        for k in sorted(res):
            print('      ', k, ex[k][0])
    print('h', h, 'iota8', iota8, 'labels', nl, 'total', sum(tot.values()), dict(sorted(tot.items())), 'time %.1f' % (time.time() - t))
