# Exact law of the x-displacement H(r+d)_x - H(r)_x in RQC (worst node type at the split level).
import random, numpy as np
from rqc import TYPES, configs
from atoms import cf, TI

def child_dists(k, o):
    """list over types of x-distribution of offset o in a level-k node"""
    D = [np.array([1.0]) for _ in TYPES]
    for j in range(1, k+1):
        d = (o >> (2*(j-1))) & 3; s = 1 << (j-1); ND = []
        for tau in TYPES:
            arr = np.zeros(2*s)
            for (p, order, ct) in cf(tau, s):
                q = order[d]; child = D[TI[ct[d]]] if ct[d] is not None else D[0]
                arr[q[0]*s:q[0]*s+s] += p*child
            ND.append(arr)
        D = ND
    return D

def disp(r, d):
    r2 = r + d
    L = 1
    while (r >> (2*L)) != (r2 >> (2*L)): L += 1
    s = 1 << (L-1); p1 = (r >> (2*(L-1))) & 3; p2 = (r2 >> (2*(L-1))) & 3
    o1 = r & (s*s-1); o2 = r2 & (s*s-1)
    D1 = child_dists(L-1, o1); D2 = child_dists(L-1, o2)
    best = None
    for tau in TYPES:
        law = np.zeros(4*s - 1)   # dx in [-(2s-1), 2s-1]
        for (p, order, ct) in cf(tau, s):
            q1, q2 = order[p1], order[p2]
            a = D1[TI[ct[p1]]] if ct[p1] is not None else D1[0]
            b = D2[TI[ct[p2]]] if ct[p2] is not None else D2[0]
            c = np.convolve(b, a[::-1])          # x2 - x1 + (s-1)
            off = (q2[0]-q1[0])*s - (s-1) + (2*s-1)
            law[off:off+len(c)] += p*c
        if best is None or law.max() > best.max(): best = law
    return best, 2*s - 1

rng = random.Random(3)
for k in range(3, 10):
    d = 4**k
    rows = []
    for _ in range(12):
        r = rng.randrange(4**(k+2))
        law, z = disp(r, d)
        xs = np.arange(len(law)) - z
        atom = law.max()*np.sqrt(d)
        m = k - 1
        dy = law[(xs % (1 << m)) == 0].sum() * (1 << m)    # ratio P(dx = 0 mod 2^(k-1)) / 2^-(k-1)
        rows.append((atom, dy))
    rows.sort()
    print(k, "sqrt(d)*max atom: median %.2f max %.2f;  2^m * P(dx = 0 mod 2^m), m=k-1: median %.2f max %.2f" %
          (rows[6][0], rows[-1][0], sorted(x[1] for x in rows)[6], max(x[1] for x in rows)))
