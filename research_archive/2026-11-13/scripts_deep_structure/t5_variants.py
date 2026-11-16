# Uniform 3-row layers (zones and gaps alike): base rows Rp (n = nu+1 mod 4), Rm (n = nu+3 mod 4),
# hole row rho (n = nu mod 2). Offsets given relative to R = top row = r1 mod 16.
import sys, time
from layout import build, report, greedy_class
h = int(sys.argv[1]); W = int(sys.argv[2]); svals = [int(v) for v in sys.argv[3].split(',')]
offs = [tuple(int(v) for v in o.split(':')) for o in sys.argv[4].split(',')]   # (dRp, dRm, drho)
iota8 = int(sys.argv[5]) if len(sys.argv) > 5 else 1
r1 = (2 * iota8 + 1) % 16; r0 = 1 if iota8 % 2 else 3
A = (h + 1) // 2; nu = iota8 % 2
R = max(y for y in range(1, h + 1) if y % 16 == r1)
M = 4 * ((W // 4 - A) // 8)
t0 = time.time()
for (dp, dm, dr) in offs:
    Rp, Rm, rho = R - dp, R - dm, R - dr
    rowf = lambda n: rho if n % 2 == nu else (Rp if n % 4 == (nu + 1) % 4 else Rm)
    tot = {}; nl = 0
    for s in svals:
        cls = greedy_class(h, s, iota8, excl_rows=(Rp, Rm, rho, R - 16, Rp - 16, Rm - 16))
        cls = [i for i in cls if not (r0 == 3 and i == 2)]
        nl += len(cls)
        S, k = build(h, W, r0, [(M, s, cls)], rowf)
        C, ex = report(S, k, h, W)
        for a, b in C.items():
            if not a.startswith('Tparked'): tot[a] = tot.get(a, 0) + b
    print('h', h, 'rows', (Rp, Rm, rho), 'labels', nl, tot)
print('time', round(time.time() - t0, 1))
