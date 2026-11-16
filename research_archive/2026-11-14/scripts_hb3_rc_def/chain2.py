"""(1) Which digit words mix the gate chain; (2) Monte Carlo check of collision formula;
(3) exact rational certificate ||T^L||_inf for the coordinate collision transfer matrix."""
import itertools, random
from fractions import Fraction as Fr
import numpy as np
from table import TABLE, GATES, bits
from curve import base_orders, build
import chain as C

G = C.G; IDX = C.IDX; P = C.P

def dob(seq):
    Mx = np.eye(G)
    for d in seq: Mx = Mx @ P[d]
    return C.dobrushin(Mx)

for L in (2, 3, 4, 5, 6):
    words = list(itertools.product(range(4), repeat=L))
    vals = [dob(w) for w in words]
    mid = [dob(w) for w in itertools.product((1, 2), repeat=L)]
    nmix = sum(v < 1 - 1e-12 for v in vals)
    print('L', L, 'words with coefficient < 1:', nmix, 'of', len(words),
          ' max coeff over {1,2}^L:', round(max(mid), 4), ' mean coeff all words:', round(np.mean(vals), 4))
# words with coefficient 1 at L=4: look at them
bad = [w for w in itertools.product(range(4), repeat=4) if dob(w) > 1 - 1e-12]
print('example non-contracting words L=4:', bad[:12], '... count', len(bad))
# is every non-contracting word constant?  check
print('non-contracting words that are not constant:', [w for w in bad if len(set(w)) > 1][:10])

# (2) Monte Carlo of E_rho P(agree in x) for same gate g, depth m
rng = random.Random(11)
Tx = C.transfer('x'); bx = C.base('x')
for m in (3, 4, 5):
    vec = bx.copy()
    for _ in range(m - 1): vec = Tx @ vec
    for g in [(0, 1), (0, 3)]:
        pred = vec[IDX[g] * G + IDX[g]]
        tot = 0.0; K = 300
        for _ in range(K):
            a = build(m, g, rng); b = build(m, g, rng)
            tot += np.mean(a[:, 0] == b[:, 0])
        print('m', m, 'gate', g, 'predicted', round(pred, 4), 'Monte Carlo', round(tot / K, 4))

# (3) exact certificate
def exact_T(mode):
    rows = {}
    for g1 in GATES:
        for g2 in GATES:
            R1, R2 = TABLE[g1], TABLE[g2]
            row = {}
            for (o1, c1), (o2, c2) in itertools.product(R1, R2):
                w = Fr(1, 4 * len(R1) * len(R2))
                for d in range(4):
                    if C.match(o1[d], o2[d], mode):
                        key = IDX[c1[d]] * G + IDX[c2[d]]
                        row[key] = row.get(key, 0) + w
            rows[IDX[g1] * G + IDX[g2]] = row
    return rows

T = exact_T('x')
v = [Fr(1)] * (G * G)
best = None
for L in range(1, 41):
    v = [sum(w * v[k] for k, w in T[i].items()) for i in range(G * G)]
    nrm = max(v)
    rate = float(nrm) ** (1.0 / L)
    if L in (1, 2, 5, 10, 20, 30, 40):
        print('L', L, '||T_x^L||_inf =', float(nrm), ' rate^(1/L) =', round(rate, 5))
    best = (L, nrm)
L, nrm = best
print('certificate: ||T_x^%d||_inf <= %.6e, i.e. lambda_cert = %.5f' % (L, float(nrm), float(nrm) ** (1.0 / L)))
