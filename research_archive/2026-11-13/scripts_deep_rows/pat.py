"""Pattern tester. Region iota8 (odd), labels i = iota8 mod 8 (1 <= i < A, 0<=i+s<K) in one block at n = i+M.
Relative slot r = n - (iota8 + M); labels at r = 0 mod 8.  Filler row = R0 + 8*off[r mod P],
R0 = max{y<=h : y = r1 mod 16}.  usage: py pat.py h iota8 s_list off_list [exclrows] [gaponly]"""
import sys, time
from collections import Counter
from driver import build, analyse
from board import shapes

def run(h, iota8, s, off, S, excl=(), gaponly=False, M0=None):
    W = (h * h) // 4 + 1; A = (h + 1) // 2; K = h // 2
    r1 = (2 * iota8 + 1) % 16
    R0 = max(y for y in range(2, h + 1) if y % 16 == r1)
    M = ((W // 2 + 10) // 16) * 16 + 16 if M0 is None else M0
    base = iota8 + M; P = len(off)
    rows = set(R0 + 8 * o for o in off)
    labels = [] if gaponly else [(4 * (i + M), 2 * i + 1, 2 * (i + s) + 2) for i in range(1, A)
              if 0 <= i + s < K and i % 8 == iota8 and (2 * i + 1) not in excl]
    Wd = 4 * (M + A) + 2 * W + 40
    rule = lambda n: R0 + 8 * off[(n - base) % P]
    kind = build(h, Wd, labels, rule)
    res, ex = analyse(h, kind, S)
    return res, ex, len(labels), (R0, sorted(rows), M)

if __name__ == '__main__':
    h = int(sys.argv[1]); iota8 = int(sys.argv[2])
    ss = [int(a) for a in sys.argv[3].split(',')]
    off = [int(a) for a in sys.argv[4].split(',')]
    excl = [int(a) for a in sys.argv[5].split(',')] if len(sys.argv) > 5 and sys.argv[5] != '-' else []
    gaponly = len(sys.argv) > 6 and sys.argv[6] == 'gap'
    S = shapes(h); t = time.time(); tot = Counter(); nl = 0
    for s in ss:
        res, ex, n, info = run(h, iota8, s, off, S, excl, gaponly)
        nl += n; tot.update(res)
        print('s', s, 'labels', n, info, dict(sorted(res.items())), flush=True)
        for k in sorted(res):
            print('      ', k, ex[k][0])
        if gaponly: break
    print('h', h, 'off', off, 'labels', nl, 'total', sum(tot.values()), dict(sorted(tot.items())), 'time %.1f' % (time.time() - t))
