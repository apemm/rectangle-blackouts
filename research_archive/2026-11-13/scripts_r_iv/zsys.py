# Integer relations among rho_lambda = p/q (be <= B): peel rows with a private prime, then rank over Q (mod a big prime).
import sys
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
cols = sorted({c for i in core for c in rows[i]})
print('lambdas', len(L), 'Z-core rows', len(core), 'cols', len(cols))
P = 2**61 - 1
idx = {c: j for j, c in enumerate(cols)}
piv = {}
rank = 0
for i in core:
    v = {idx[c]: e % P for c, e in rows[i].items()}
    while v:
        b = max(v)
        if b in piv:
            pv = piv[b]; f = v[b] * pow(pv[b], P - 2, P) % P
            for j, x in pv.items():
                v[j] = (v.get(j, 0) - f * x) % P
                if v[j] == 0: del v[j]
        else:
            piv[b] = v; rank += 1; break
print('rank mod P', rank, '-> relations', len(core) - rank)
print('primes in core:', cols[:40])
