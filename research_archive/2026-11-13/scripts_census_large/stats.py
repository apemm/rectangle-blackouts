"""Class statistics of L*** (v2 rules) at height h over all 512 types: kept labels, subclass sizes."""
import sys, time
from collections import Counter
from v2board import build_type_v2, params, admissible_primes
h = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'exact'
t0 = time.time()
P = params(h); ls, ps = admissible_primes(h); l, p = ls[0], ps[0]
print('h', h, 'B', P['B'], 'l', l, 'p', p, 'W', P['W'], 'h%4', h % 4)
tot = Counter(); bytype = []; heavyall = set()
for iota in range(32):
    for sigma in range(16):
        tp, subs, heavy = build_type_v2(h, iota, sigma, l, p, mode=mode)
        heavyall |= set(heavy)
        sz = Counter(len(s['labels']) for s in subs if s['labels'])
        tot += sz
        kept = sum(len(s['labels']) for s in subs)
        bytype.append((kept, max(sz) if sz else 0, sum(v for k, v in sz.items() if k >= 2), iota, sigma, tp['r0'], tp['D0'], tp['k'], tp['Ts']))
    if time.time() - t0 > 50:
        print('timeout at iota', iota); break
print('size histogram', sorted(tot.items()))
print('kept labels', sum(b[0] for b in bytype), 'heavy', sorted(heavyall)[:10], len(heavyall))
for kk in (0, 1, 2):
    for r0 in (1, 3):
        L = [b for b in bytype if b[7] == kk and b[5] == r0]
        if L:
            L.sort(reverse=True)
            print('k', kk, 'r0', r0, 'ntypes', len(L), 'top (kept, maxsize, #multi, iota, sigma, r0, D0, k, Ts):', L[:3])
print('time %.1f' % (time.time() - t0))
