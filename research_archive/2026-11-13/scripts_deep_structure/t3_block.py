# One block of labels (greedy G_T-independent, i = iota8 mod 8) in a Q4 layer vs BH16.
import sys, time
from layout import build, report, greedy_class
h = int(sys.argv[1]); W = int(sys.argv[2]); variant = sys.argv[3]; svals = [int(v) for v in sys.argv[4].split(',')]
iota8 = int(sys.argv[5]) if len(sys.argv) > 5 else 1
r1 = (2 * iota8 + 1) % 16; r0 = 1 if iota8 % 2 else 3
A = (h + 1) // 2; mu = 0; nu = (iota8 + mu) % 2
M = 4 * ((W // 4 - A) // 8)            # block position, M = 0 mod 4 (so labels n = iota8 mod 4)
tops = [y for y in range(1, h + 1) if y % 16 == (r1 + 8) % 16]
Y = tops[-4]                            # four highest rows = r1+8 mod 16
R = max(y for y in range(1, h + 1) if y % 16 == r1); rho = R - 8
if variant == 'Q4':
    rowf = lambda n: Y + 16 * (n % 4)
    excl = ()
elif variant == 'BH16':
    rowf = lambda n: rho if n % 2 == nu else R
    excl = (R, R - 16)
t0 = time.time(); tot = {}
for s in svals:
    cls = greedy_class(h, s, iota8, excl_rows=excl)
    cls = [i for i in cls if not (r0 == 3 and i == 2)]
    S, k = build(h, W, r0, [(M, s, cls)], rowf)
    C, ex = report(S, k, h, W)
    bad = {a: b for a, b in C.items() if not a.startswith('Tparked')}
    park = sum(b for a, b in C.items() if a.startswith('Tparked'))
    print(variant, 'h', h, 's', s, 'labels', len(cls), 'parked', park, bad)
    for a in bad: print('    ', a, ex[a])
print('time', round(time.time() - t0, 1))
