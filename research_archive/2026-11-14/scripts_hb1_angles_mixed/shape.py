import sys, json, math, numpy as np
from collections import Counter
from angles import setup, enumerate_angles
h, S, M, seed = map(int, sys.argv[1:5])
D = setup(h, S, M, seed)
t = enumerate_angles(D, slots=True)
odd, even, slot = D['odd'], D['even'], D['slot']
cx2, clam, cb, cgam, ratio = Counter(), Counter(), Counter(), Counter(), []
for (v, p, f, g, sf, sg) in t:
    x2 = sg - slot[v]; x1 = sf - slot[v]
    yV = odd[v] if p == 0 else even[v]
    yG = even[g] if p == 0 else odd[g]
    Y2 = int(yG - yV)
    gam = math.gcd(abs(Y2), abs(int(x2)))
    a = Y2 // gam; b = -int(x2) // gam
    lam = int(x1) // a
    cx2[abs(int(x2))] += 1; clam[abs(lam)] += 1; cb[abs(b)] += 1; cgam[gam] += 1
    ratio.append(abs(a) / (M * S**4 / 16))
print(json.dumps({'h': h, 'M': M, 'n': len(t), 'x2': sorted(cx2.items())[:8], 'lam': sorted(clam.items()),
   'b': sorted(cb.items())[:6], 'gamma': sorted(cgam.items())[:6],
   'min_a_over_MS4_16': min(ratio) if ratio else None}))
