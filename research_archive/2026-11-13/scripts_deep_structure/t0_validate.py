# Validation of the checker: pure seas (Prop 3: clean), X2 example, M2a pair, BH16 block.
import time
from layout import build, report, greedy_class
t0 = time.time()
# 1. Sea(1,r), h=12 and 17, r > (h+1)/2: expect empty
for h in (12, 17):
    for r in range(h // 2 + 1, h + 1):
        S, k = build(h, 300, 1, [], lambda n, r=r: r)
        C, ex = report(S, k, h, 300)
        print('Sea(1,%d) h=%d' % (r, h), dict(C) if r > (h + 1) / 2 else ('(r<=(h+1)/2)', sum(C.values())))
# 2. X2 example from block_sea: E=(21,1),V=(16,9),G=(24,14),W=(29,6): T=1 labels slots 4 and 6, h large
h = 20
S, k = build(h, 120, 1, [(0, 0, [4, 6])], lambda n: 19)
C, ex = report(S, k, h, 120)
print('X2 test', {a: b for a, b in C.items() if 'fatal' in a}, [ex[a] for a in C if 'fatal' in a][:3])
# 3. BH16 single block, h=57, iota8=1, mu=0 -> nu=1, r1=3, R=max y<=h, y=3 mod16 ; rho=R-8
h = 57; A = (h + 1) // 2; R = max(y for y in range(1, h + 1) if y % 16 == 3); rho = R - 8
W = 1200; M = 2 * ((W // 4 - A) // 4)
for s in (0, 3, -5):
    cls = greedy_class(h, s, 1, excl_rows=(R, R - 16))
    S, k = build(h, W, 1, [(M, s, cls)], lambda n: rho if n % 2 == 1 else R)
    C, ex = report(S, k, h, W)
    bad = {a: b for a, b in C.items() if not a.startswith('Tparked')}
    print('BH16 s=%d' % s, cls, bad)
print('time', round(time.time() - t0, 1))
