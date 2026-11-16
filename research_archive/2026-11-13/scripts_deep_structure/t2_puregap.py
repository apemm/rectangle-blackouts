# Pure Q4 gap (no labels), sea row r0; fillers at row Y + 16*phi(n mod 4).
import sys, time
from layout import build, report
h = int(sys.argv[1]); W = int(sys.argv[2]); r0 = int(sys.argv[3]); Y = int(sys.argv[4])
phi = tuple(int(c) for c in sys.argv[5])
t0 = time.time()
S, k = build(h, W, r0, [], lambda n: Y + 16 * phi[n % 4])
C, ex = report(S, k, h, W)
print('h', h, 'W', W, 'r0', r0, 'rows', [Y + 16 * p for p in phi], dict(C))
for a in list(C)[:6]: print(' ', a, ex.get(a))
print('time', round(time.time() - t0, 1))
