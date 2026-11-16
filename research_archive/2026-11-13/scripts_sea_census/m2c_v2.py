# Check the 2-adic M2c theorem on rigid layouts, including stress block spacing.
import sys, time
import numpy as np
from collections import Counter
import large
from large import layout, colorings, divisor_table, m2c_search, check_mixed
def v2(n):
    n = abs(n); c = 0
    if n == 0: return 99
    while n % 2 == 0: n //= 2; c += 1
    return c
h = int(sys.argv[1]); p = int(sys.argv[2]); nu = int(sys.argv[3]); large.SPLIT = int(sys.argv[4])
types = [(a, b) for a in range(8) for b in range(2)]
colors = colorings(h)
dstart, ddata = divisor_table(2 * h * h + 8)
stat = Counter(); t0 = time.time()
for (iota, mu) in types:
    pts, r0 = layout(h, iota, mu, 0, p, nu, colors)
    H1 = h + 1
    px = np.array([q[0] for q in pts], np.int64); py = np.array([q[1] for q in pts], np.int64)
    key = px * H1 + py; o = np.argsort(key); meta = [pts[k] for k in o]
    out = np.zeros((200000, 4), np.int64)
    c = m2c_search(px[o], py[o], key[o], h, r0, dstart, ddata, out)
    for r in range(min(c, out.shape[0])):
        b, d, xA, xC = out[r]; B = meta[b]; D = meta[d]
        if not check_mixed((xA, r0), (B[0], B[1]), (xC, r0), (D[0], D[1]), h):
            stat['FAILED CHECK'] += 1; continue
        e = (D[1] - B[1]) // 2; u2 = B[1] - r0; z = B[0] - xA; n1 = -e * u2 // z
        dM = p * (D[3] - B[3])
        par = 'odd' if B[2] == 0 else 'even'
        where = 'intra' if D[3] == B[3] else 'cross'
        if par == 'even':
            stat[(par, where, 'v2e', v2(e), 'v2n1', v2(n1))] += 1
        else:
            a = v2(e); bb = v2(n1); cM = v2(dM)
            ok = (bb == a + 1 and v2(e + dM) == a) or (bb == a and v2(e + dM) == a - 1)
            stat[(par, where, 'case', 'b=a+1' if bb == a + 1 else ('b=a' if bb == a else 'other'), 'predicted' if ok else 'NOT PREDICTED', 'v2(dM)>=4' if cM >= 4 else 'v2(dM)<4')] += 1
print('h=%d p=%d nu=%d split=%d  %.1fs' % (h, p, nu, large.SPLIT, time.time() - t0))
for k, v in sorted(stat.items(), key=str):
    print('  ', v, k)
