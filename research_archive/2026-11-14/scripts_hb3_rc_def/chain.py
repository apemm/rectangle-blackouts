"""Gate chain mixing and collision transfer matrices for uniform CGK curves."""
import itertools
from fractions import Fraction as Fr
import numpy as np
from table import TABLE, GATES, bits
from curve import base_orders

G = len(GATES); IDX = {g: k for k, g in enumerate(GATES)}

# gate transition P_delta[g, g'] (digit delta = position in rank order)
P = np.zeros((4, G, G))
for g in GATES:
    R = TABLE[g]
    for order, cg in R:
        for d in range(4):
            P[d, IDX[g], IDX[cg[d]]] += 1.0 / len(R)

def dobrushin(Mx):
    return max(0.5 * np.abs(Mx[a] - Mx[b]).sum() for a in range(G) for b in range(G))

for L in range(1, 6):
    worst = 0.0
    for seq in itertools.product(range(4), repeat=L):
        Mx = np.eye(G)
        for d in seq:
            Mx = Mx @ P[d]
        worst = max(worst, dobrushin(Mx))
    print('max Dobrushin coefficient over digit words of length', L, ':', round(worst, 6))
Pavg = P.mean(axis=0)
w, v = np.linalg.eig(Pavg.T)
k = np.argmin(abs(w - 1)); pi = np.real(v[:, k]); pi /= pi.sum()
print('stationary law (averaged digits): A-gate mass', round(sum(pi[IDX[g]] for g in GATES if bin(g[0]^g[1]).count('1')==1), 4))

# collision transfer: state (g1, g2); coordinate mode 'x', 'y', 'v' (both)
def match(c1, c2, mode):
    b1, b2 = bits(c1), bits(c2)
    if mode == 'x': return b1[0] == b2[0]
    if mode == 'y': return b1[1] == b2[1]
    return b1 == b2

def transfer(mode):
    T = np.zeros((G * G, G * G))
    for g1 in GATES:
        for g2 in GATES:
            R1, R2 = TABLE[g1], TABLE[g2]
            row = IDX[g1] * G + IDX[g2]
            for (o1, c1), (o2, c2) in itertools.product(R1, R2):
                wgt = 1.0 / (4 * len(R1) * len(R2))
                for d in range(4):
                    if match(o1[d], o2[d], mode):
                        T[row, IDX[c1[d]] * G + IDX[c2[d]]] += wgt
    return T

def base(mode):
    b = np.zeros(G * G)
    for g1 in GATES:
        for g2 in GATES:
            B1, B2 = base_orders(g1), base_orders(g2)
            s = 0.0
            for o1, o2 in itertools.product(B1, B2):
                for d in range(4):
                    s += match(o1[d], o2[d], mode)
            b[IDX[g1] * G + IDX[g2]] = s / (4 * len(B1) * len(B2))
    return b

for mode in ('x', 'y', 'v'):
    T = transfer(mode); b = base(mode)
    ev = np.linalg.eigvals(T); rho = max(abs(ev))
    # Perron certificate: w = positive right eigenvector, check T w <= lam w
    vals, vecs = np.linalg.eig(T)
    kk = np.argmax(abs(vals)); wv = np.abs(np.real(vecs[:, kk]))
    ratio = (T @ wv) / np.maximum(wv, 1e-300)
    # diagonal states g1 = g2 (same gate) and the max over all starting states
    m_rates = []
    vec = b.copy()
    for m in range(1, 13):
        if m > 1: vec = T @ vec
        m_rates.append(vec.max())
    print('mode', mode, 'spectral radius', round(rho, 6), 'min w', wv.min(), 'max (Tw)_i/w_i', round(ratio.max(), 6))
    print('   max over gate pairs of E_rho P(agree), side 2^m, m=1..12:', [round(x, 5) for x in m_rates])
    print('   per-level ratio at m=12:', round(m_rates[-1] / m_rates[-2], 5), ' compare 1/2 (x or y), 1/4 (v)')
