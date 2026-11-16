# min M such that some additive psi on primes has 1 <= psi(rho_l) <= M on the Z-core (peeled rows are free).
import sys, numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
from core import zcore
B = int(sys.argv[1]); k = int(sys.argv[2])
L, rows, core = zcore(B, k)
primes = sorted({c for i in core for c in rows[i]}); pid = {c: j for j, c in enumerate(primes)}
n = len(primes); m = len(core)
A = lil_matrix((2 * m, n + 1)); b = np.zeros(2 * m)
for t, i in enumerate(core):
    for c, e in rows[i].items():
        A[t, pid[c]] = -e; A[m + t, pid[c]] = e
    b[t] = -1; A[m + t, n] = -1
cvec = np.zeros(n + 1); cvec[n] = 1
res = linprog(cvec, A_ub=A.tocsr(), b_ub=b, bounds=[(None, None)] * n + [(0, None)], method='highs')
print('B', B, 'core', m, 'primes', n, 'status', res.status, 'min M', res.fun if res.status == 0 else None)
