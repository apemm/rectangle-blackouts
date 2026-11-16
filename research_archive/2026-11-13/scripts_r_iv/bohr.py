# Search theta: core primes -> R/Z maximizing eps = min_l ||theta(rho_l)|| (Bohr colouring with ~1/eps colours).
import sys, numpy as np
from scipy.sparse import csr_matrix
from core import zcore
B = int(sys.argv[1]); k = int(sys.argv[2]); restarts = int(sys.argv[3])
L, rows, core = zcore(B, k)
pr = sorted({c for i in core for c in rows[i]}); pid = {c: j for j, c in enumerate(pr)}
ri, ci, vv = [], [], []
for t, i in enumerate(core):
    for c, e in rows[i].items(): ri.append(t); ci.append(pid[c]); vv.append(e)
A = csr_matrix((vv, (ri, ci)), shape=(len(core), len(pr))).astype(float); AT = A.T.tocsr()
rng = np.random.default_rng(1)
def dist(x): return np.abs(x - np.round(x))
best = 0
for r in range(restarts):
    th = rng.random(len(pr))
    for it in range(3000):
        x = A @ th
        # soft objective: push ||x|| up; weight small ones strongly
        d = dist(x)
        w = np.exp(-d / 0.03)
        s = np.sign(x - np.round(x)); s[s == 0] = 1
        g = AT @ (w * s)
        th += 0.002 * g / (1 + np.abs(g).max())
    eps = dist(A @ th).min()
    best = max(best, eps)
print('B', B, 'k', k, 'core', len(core), 'primes', len(pr), 'best eps', round(best, 4), '(colours ~', int(np.ceil(1 / best)) if best > 0 else None, ')')
