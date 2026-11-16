"""Independent CGK refinement table, 1D and 2D collision transfer matrices,
spectral radii, and an exact Collatz-Wielandt lower-bound certificate.
Corners are pairs (b1, b2) in {0,1}^2. Gate = (in, out), in != out."""
import itertools
from fractions import Fraction as F
import numpy as np

C = [(0, 0), (0, 1), (1, 0), (1, 1)]
G = [(a, b) for a in C for b in C if a != b]
GI = {g: i for i, g in enumerate(G)}

def J_ok(p, o, pn, i_n):
    for a in range(2):
        if p[a] != pn[a]:
            if o[a] != pn[a] or i_n[a] != p[a]:
                return False
        elif o[a] != i_n[a]:
            return False
    return True

def refs(g):
    gin, gout = g
    mids = [c for c in C if c not in g]
    out = []
    for m in itertools.permutations(mids):
        order = (gin,) + m + (gout,)
        for cg in itertools.product(G, repeat=4):
            if cg[0][0] != gin or cg[3][1] != gout:
                continue
            if all(J_ok(order[k], cg[k][1], order[k + 1], cg[k + 1][0]) for k in range(3)):
                out.append((order, cg))
    return out

R = {g: refs(g) for g in G}
isA = {g: sum(x != y for x, y in zip(*g)) == 1 for g in G}
print('refinement counts', sorted(set((isA[g], len(R[g])) for g in G)))
hil = (((0, 0), (0, 1), (1, 1), (1, 0)), (((0, 0), (0, 1)), ((0, 0), (1, 0)), ((0, 0), (1, 0)), ((1, 1), (1, 0))))
print('Hilbert refinement present:', hil in R[((0, 0), (1, 0))])

# fraction of A children of an A parent
for g in G:
    if isA[g]:
        fa = F(sum(isA[cg[k]] for (o, cg) in R[g] for k in range(4)), 4 * len(R[g]))
        shared = F(sum(cg[1] == cg[2] for (o, cg) in R[g]), len(R[g]))
        break
print('P(child A | parent A) =', fa, ' P(children 2,3 share gate | A parent) =', shared)
for g in G:
    if not isA[g]:
        print('D parent: child A frac', F(sum(isA[cg[k]] for (o, cg) in R[g] for k in range(4)), 4 * len(R[g])),
              ' share', F(sum(cg[1] == cg[2] for (o, cg) in R[g]), len(R[g])))
        break

def base_orders(g):
    mids = [c for c in C if c not in g]
    return [(g[0],) + m + (g[1],) for m in itertools.permutations(mids)]

def agree(p1, p2, mode):
    return p1 == p2 if mode == 2 else p1[mode] == p2[mode]

def build(mode):
    n = len(G)
    T = [[F(0)] * (n * n) for _ in range(n * n)]
    b = [F(0)] * (n * n)
    for g1 in G:
        for g2 in G:
            s = GI[g1] * n + GI[g2]
            w = F(1, 4 * len(R[g1]) * len(R[g2]))
            for (o1, c1) in R[g1]:
                for (o2, c2) in R[g2]:
                    for d in range(4):
                        if agree(o1[d], o2[d], mode):
                            t = GI[c1[d]] * n + GI[c2[d]]
                            T[s][t] += w
            B1, B2 = base_orders(g1), base_orders(g2)
            wb = F(1, 4 * len(B1) * len(B2))
            b[s] = sum(wb for x in B1 for y in B2 for d in range(4) if agree(x[d], y[d], mode))
    return T, b

for mode, name in [(0, 'coord 1'), (1, 'coord 2'), (2, '2D')]:
    T, b = build(mode)
    Tf = np.array([[float(x) for x in row] for row in T])
    ev = max(abs(np.linalg.eigvals(Tf)))
    # Perron vector by power iteration on T + I (aperiodic)
    u = np.ones(len(T))
    for _ in range(3000):
        u = Tf @ u + u
        u /= u.max()
    lam_est = min((Tf @ u)[i] / u[i] for i in range(len(u)) if u[i] > 1e-9)
    # exact certificate: rationalize u, find lam = min (Tu)_i/u_i over support, check support closed
    ur = [F(round(x * 10 ** 8), 10 ** 8) for x in u]
    sup = [i for i in range(len(ur)) if ur[i] > 0]
    Tu = [sum(T[i][j] * ur[j] for j in sup) for i in range(len(T))]
    lam = min(Tu[i] / ur[i] for i in sup)
    diag = [GI[g] * len(G) + GI[g] for g in G]
    cmin = min(b[i] / ur[i] for i in sup)
    udiag = min(ur[i] for i in diag)
    print(f'{name}: spectral radius {ev:.5f}; certified T u >= lam u with lam = {float(lam):.5f}'
          f' (exact rational); min_diag u = {float(udiag):.4f}; min b/u = {float(cmin):.4f}; support {len(sup)}/{len(T)}')
    # exact averaged collision for small k, min over diagonal states
    v = b[:]
    for k in range(1, 9):
        if k > 1:
            v = [sum(T[i][j] * v[j] for j in range(len(v)) if T[i][j]) for i in range(len(v))]
        m = min(v[i] for i in diag)
        M = max(v[i] for i in diag)
        print(f'   k={k}: min/max over gates of E_rho coll = {float(m):.5f} / {float(M):.5f};'
              f' ratio to 2^-k (1D) or 4^-k (2D): {float(m) * (2 if mode < 2 else 4) ** k:.3f}')
