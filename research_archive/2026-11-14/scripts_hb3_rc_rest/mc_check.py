# Monte Carlo cross-check of the exact rank-view law (atoms.py) for a fixed root type.
import random, numpy as np
from rqc import TYPES, sample_curve, configs
from atoms import cf, TI

def law_for_type(k, o, tau_root):
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
    return D[TI[tau_root]]

rng = random.Random(11)
k = 5; root = ((0,0),(1,0))
for o in (5, 300, 777):
    exact = law_for_type(k, o, root)
    N = 4000; emp = np.zeros(2**k)
    for _ in range(N):
        H = sample_curve(k, rng, root)
        emp[H[o][0]] += 1
    emp /= N
    print("o=%d  max|emp-exact| = %.4f  (sd scale %.4f)  exact max atom %.3f" %
          (o, np.abs(emp-exact).max(), np.sqrt(exact.max()/N), exact.max()))
