# Short odd relations among y-smooth rho_lambda: kernel lattice + LLL.
import sys, time
from collections import defaultdict
from sympy import factorint, primerange
from sympy import Matrix, ZZ
from sympy.polys.matrices import DomainMatrix
from f2sys import lams
B = int(sys.argv[1]); y = int(sys.argv[2]); k = int(sys.argv[3])
L = lams(B, k)
sm = []
for (al, be, q, p) in L:
    fp = factorint(p, limit=y + 1); fq = factorint(q, limit=y + 1)
    if max(list(fp) + list(fq)) > y: continue
    d = defaultdict(int)
    for r, e in fp.items(): d[r] += e
    for r, e in fq.items(): d[r] -= e
    sm.append(((al, be, q, p), d))
print('smooth lambdas', len(sm), flush=True)
pr = sorted({r for _, d in sm for r in d}); pid = {r: i for i, r in enumerate(pr)}
M = DomainMatrix([[ZZ(d.get(r, 0)) for (_, d) in sm] for r in pr], (len(pr), len(sm)), ZZ)
t = time.time()
K = M.to_Matrix().nullspace()
print('kernel dim', len(K), 'time', time.time() - t, flush=True)
from math import lcm, gcd
vecs = []
for v in K:
    den = 1
    for x in v: den = lcm(den, int(x.q))
    w = [int(x * den) for x in v]
    g = 0
    for x in w: g = gcd(g, x)
    vecs.append([x // g for x in w])
# saturate at 2 not needed if we LLL then check; LLL the integer kernel basis (not saturated: fine for finding short vectors in it)
D = DomainMatrix([[ZZ(x) for x in w] for w in vecs], (len(vecs), len(sm)), ZZ)
R = D.lll().to_list()
R = [[int(x) for x in r] for r in R]
odd = [r for r in R if sum(r) % 2]
print('LLL rows', len(R), 'odd-sum rows', len(odd))
R.sort(key=lambda r: sum(abs(x) for x in r))
for r in R[:8]:
    print('l1', sum(abs(x) for x in r), 'sum', sum(r), 'support', sum(1 for x in r if x))
best = min(odd, key=lambda r: sum(abs(x) for x in r)) if odd else None
if best:
    num = 1; den = 1
    for j, x in enumerate(best):
        q, p = sm[j][0][2], sm[j][0][3]
        if x > 0: num *= p ** x; den *= q ** x
        elif x < 0: num *= q ** (-x); den *= p ** (-x)
    print('shortest odd: l1', sum(abs(x) for x in best), 'sum', sum(best), 'exact product check', num == den)
    print([(sm[j][0], x) for j, x in enumerate(best) if x])
