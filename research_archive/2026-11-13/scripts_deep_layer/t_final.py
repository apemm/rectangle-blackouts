"""Rule BH16: region (iota8, parity of M). Labels i = iota8 mod 8, i>=1, at n = i+M.
nu = (iota8 + M) mod 2. r1 = 2*iota8+1 mod 16. R = max row <= h with R = r1 mod 16, rho = R-8.
base fillers (n != nu mod 2): row R ; hole fillers (n = nu mod 2): row rho.
usage: py t_final.py h iota8 s1,s2,... [M parity]"""
import sys, time
from collections import Counter
from driver import build, analyse
from board import shapes

def rows_for(h, iota8, D0=8):
    r1 = (2 * iota8 + 1) % 16
    R = max(y for y in range(2, h + 1) if y % 16 == r1)
    return R, R - D0

def run(h, iota8, s, Mpar, S, D0=8, holes_mod=2, imin=1):
    W = (h * h) // 4 + 1; A = (h + 1) // 2; K = h // 2
    M = ((W // 2 + 10) // 16) * 16 + 16 + Mpar
    nu = (iota8 + M) % holes_mod
    R, rho = rows_for(h, iota8, D0)
    labels = [(4 * (i + M), 2 * i + 1, 2 * (i + s) + 2) for i in range(imin, A)
              if 0 <= i + s < K and i % 8 == iota8]
    Wd = 4 * (M + A) + 2 * W + 40
    rule = lambda n: rho if n % holes_mod == nu else R
    kind = build(h, Wd, labels, rule)
    res, ex = analyse(h, kind, S)
    return res, ex, len(labels), (R, rho, M, nu)

if __name__ == '__main__':
    h = int(sys.argv[1]); iota8 = int(sys.argv[2])
    ss = [int(a) for a in sys.argv[3].split(',')]
    Mpar = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    D0 = int(sys.argv[5]) if len(sys.argv) > 5 else 8
    S = shapes(h); t = time.time()
    tot = Counter(); nl = 0
    for s in ss:
        res, ex, n, info = run(h, iota8, s, Mpar, S, D0)
        nl += n; tot.update(res)
        print('s', s, 'labels', n, info, dict(sorted(res.items())), flush=True)
        for k in sorted(res):
            print('      ', k, ex[k][0])
    print('h', h, 'iota8', iota8, 'labels', nl, 'total', sum(tot.values()), dict(sorted(tot.items())), 'time %.1f' % (time.time() - t))
