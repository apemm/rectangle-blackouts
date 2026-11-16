# Odd relation test over Z_2: exists n in Z^Lambda with M n = 0 (exponent matrix of rho's) and sum n odd?
# Solve [M; 1^T] n = (0; 1) over Z_2 by Smith elimination mod 2^N. Not bipartite (group level) iff solvable.
import sys
import numpy as np
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
# peeled lambdas cannot appear in any relation, so restrict to core
primes = sorted({c for i in core for c in rows[i]})
pidx = {c: j for j, c in enumerate(primes)}
NR = len(primes) + 1; NC = len(core)
N = 31; MOD = 1 << N
A = np.zeros((NR, NC + 1), dtype=np.int64)
for jj, i in enumerate(core):
    for c, e in rows[i].items(): A[pidx[c], jj] = e % MOD
    A[NR - 1, jj] = 1
A[NR - 1, NC] = 1
def v2(x):
    x = int(x) % MOD
    if x == 0: return N
    return (x & -x).bit_length() - 1
r = 0
cols_left = list(range(NC))
pivv = []
Rm = list(range(NR))
active_rows = np.ones(NR, bool)
while True:
    sub = A[active_rows][:, :NC]
    if sub.size == 0: break
    # minimal valuation entry
    vals = np.where(sub % MOD == 0, N, 0)
    nz = np.argwhere(sub % MOD != 0)
    if len(nz) == 0: break
    best = None
    ar = np.nonzero(active_rows)[0]
    # compute valuations vectorised
    x = sub[sub % MOD != 0] % MOD
    lowbit = x & (-x)
    vv = np.log2(lowbit.astype(np.float64)).astype(int)
    m = int(vv.argmin()); vmin = int(vv[m])
    i0, j0 = nz[m]; pr = ar[i0]
    piv = int(A[pr, j0]) % MOD
    unit = piv >> vmin
    inv = pow(unit, -1, MOD)
    # eliminate column j0 in all other rows (active and the rest)
    for rr in range(NR):
        if rr == pr: continue
        a = int(A[rr, j0]) % MOD
        if a == 0: continue
        f = ((a >> vmin) * inv) % MOD
        A[rr] = (A[rr] - (f * A[pr]) % MOD) % MOD
    # clear pivot row by column ops (variables change, rhs column untouched)
    rowp = A[pr, :NC] % MOD
    for jj in np.nonzero(rowp)[0]:
        if jj == j0: continue
        f = ((int(rowp[jj]) >> vmin) * inv) % MOD
        A[:, jj] = (A[:, jj] - (f * A[:, j0]) % MOD) % MOD
    pivv.append((pr, vmin))
    active_rows[pr] = False
# check solvability
ok = True
for (pr, vmin) in pivv:
    if v2(A[pr, NC]) < vmin: ok = False
for rr in np.nonzero(active_rows)[0]:
    if A[rr, NC] % MOD != 0: ok = False
print('lambdas', len(L), 'core', NC, 'primes', len(primes), 'rank', len(pivv), 'max pivot v2', max(v for _, v in pivv))
print('odd relation exists (non-bipartite):', ok)
