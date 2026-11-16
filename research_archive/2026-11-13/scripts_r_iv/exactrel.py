# Exact rational kernel of the exponent matrix on the peeled core; report kernel vectors (integer, primitive) and sums.
import sys
from fractions import Fraction
from math import gcd, lcm
from collections import defaultdict
from sympy import factorint
from f2sys import lams
B = int(sys.argv[1]); k = int(sys.argv[2])
L = lams(B, k)
rows = []
for (_, _, q, p) in L:
    d = defaultdict(int)
    for r, e in factorint(p).items(): d[r] += e
    for r, e in factorint(q).items(): d[r] -= e
    rows.append({r: e for r, e in d.items() if e})
col = defaultdict(set)
for i, r in enumerate(rows):
    for c in r: col[c].add(i)
alive = set(range(len(rows)))
stack = [c for c in col if len(col[c]) == 1]
while stack:
    c = stack.pop()
    if len(col[c]) != 1: continue
    (i,) = tuple(col[c]); alive.discard(i)
    for c2 in rows[i]:
        col[c2].discard(i)
        if len(col[c2]) == 1: stack.append(c2)
core = sorted(alive)
primes = sorted({c for i in core for c in rows[i]})
# equations: for each prime, sum_l e_{p,l} n_l = 0. Gaussian elimination (RREF) over Q.
eqs = []
for pr in primes:
    eqs.append({jj: Fraction(rows[i][pr]) for jj, i in enumerate(core) if pr in rows[i]})
pivots = {}  # col -> eq (normalized, pivot coeff 1)
for e in eqs:
    e = dict(e)
    for c in list(pivots):
        if c in e:
            f = e[c]
            for j, x in pivots[c].items():
                e[j] = e.get(j, 0) - f * x
                if e[j] == 0: del e[j]
    if not e: continue
    c = min(e); f = e[c]
    e = {j: x / f for j, x in e.items()}
    for c2 in list(pivots):
        if c in pivots[c2]:
            g = pivots[c2][c]
            for j, x in e.items():
                pivots[c2][j] = pivots[c2].get(j, 0) - g * x
                if pivots[c2][j] == 0: del pivots[c2][j]
    pivots[c] = e
free = [j for j in range(len(core)) if j not in pivots]
print('core', len(core), 'rank', len(pivots), 'kernel dim', len(free))
basis = []
for fcol in free:
    vec = {fcol: Fraction(1)}
    for c, e in pivots.items():
        if fcol in e: vec[c] = -e[fcol]
    den = 1
    for x in vec.values(): den = lcm(den, x.denominator)
    iv = {j: int(x * den) for j, x in vec.items()}
    g = 0
    for x in iv.values(): g = gcd(g, x)
    iv = {j: x // g for j, x in iv.items()}
    basis.append(iv)
    print('kernel vector: support', len(iv), 'sum', sum(iv.values()), 'max|n|', max(abs(x) for x in iv.values()))
# 2-saturate the lattice spanned by basis
from itertools import product
n = len(core)
V = [[iv.get(j, 0) for j in range(n)] for iv in basis]
def dep2(V):
    # a nonzero c in F_2^len(V) with sum c_i V_i = 0 mod 2, or None
    piv = {}
    for i, v in enumerate(V):
        m = 0
        for j, x in enumerate(v):
            if x & 1: m |= 1 << j
        comb = 1 << i
        while m:
            b = m.bit_length() - 1
            if b in piv:
                pm, pc = piv[b]; m ^= pm; comb ^= pc
            else:
                piv[b] = (m, comb); break
        if m == 0:
            return [(comb >> t) & 1 for t in range(len(V))]
    return None
while True:
    c = dep2(V)
    if c is None: break
    w = [sum(c[i] * V[i][j] for i in range(len(V))) for j in range(n)]
    i0 = c.index(1)
    V[i0] = [x // 2 for x in w]; it = globals().get("it", 0) + 1; globals()["it"] = it
    if it % 100 == 0: print("iter", it, max(max(abs(x) for x in v) for v in V).bit_length(), flush=True)
sums = [sum(v) for v in V]
print('2-saturated sums parity:', [s % 2 for s in sums])
W = V
import json
for w in W:
    if sum(w) % 2:
        tot = defaultdict(int)
        for j, x in enumerate(w):
            for pr, e in rows[core[j]].items(): tot[pr] += x * e
        print('odd relation, all prime exponents cancel:', all(t == 0 for t in tot.values()), 'support', sum(1 for x in w if x), 'sum', sum(w), 'max|n|', max(abs(x) for x in w))
        json.dump({'lams': [list(L[core[j]]) for j in range(n) if w[j]], 'n': [w[j] for j in range(n) if w[j]]}, open('oddrel_%d.json' % B, 'w'))
        break
