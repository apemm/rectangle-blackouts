"""Exact law of the cell h_g(rho) of a level-K CGK curve with gate g at local offset rho.
Checks Theorem A (block-start histories) and prints the exact certificate constants."""
import itertools
from fractions import Fraction as F
import numpy as np

C = [(0, 0), (0, 1), (1, 0), (1, 1)]
G = [(a, b) for a in C for b in C if a != b]

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

def digits(rho, K):
    return [(rho >> (2 * (j - 1))) & 3 for j in range(K, 0, -1)]  # top first

def law(g, rho, K):
    """dict cell -> probability (Fraction)"""
    st = {(g, (0, 0)): F(1)}
    ds = digits(rho, K)
    for lev, d in zip(range(K, 0, -1), ds):
        s = 1 << (lev - 1)
        new = {}
        for (gg, org), p in st.items():
            if lev >= 2:
                w = p / len(R[gg])
                for order, cg in R[gg]:
                    pos = order[d]
                    key = (cg[d], (org[0] + s * pos[0], org[1] + s * pos[1]))
                    new[key] = new.get(key, 0) + w
            else:
                mids = [c for c in C if c not in gg]
                for m in itertools.permutations(mids):
                    order = (gg[0],) + m + (gg[1],)
                    pos = order[d]
                    key = (None, (org[0] + pos[0], org[1] + pos[1]))
                    new[key] = new.get(key, 0) + p / 2
        st = new
    out = {}
    for (_, cell), p in st.items():
        out[cell] = out.get(cell, 0) + p
    return out

print('Theorem A check: x = 4^k + 1 at a block start; block level K; min over gates of max atom; max support size')
for k in range(1, 5):
    for K in (k + 2, k + 3):
        x = 4 ** k + 1
        atoms, sups, atoms1 = [], [], []
        for g in G:
            L = law(g, x, K)
            atoms.append(max(L.values()))
            sups.append(len(L))
            m1 = {}
            for c, p in L.items():
                m1[c[0]] = m1.get(c[0], 0) + p
            atoms1.append(max(m1.values()))
        print(f'  k={k} K={K}: min_g 2D atom = {min(atoms)} (={float(min(atoms)):.4f}), support <= {max(sups)},'
              f' min_g 1D atom = {float(min(atoms1)):.4f};  C*4^v4/x would need C >= {float(min(atoms))*x:.1f}')

# conditional-on-block-start average over x of the max 1D atom, versus 2^{v4(x)}/sqrt(x)
print('Block-start history: sum_{x<4^K} max_z P(h(x)_1 = z) versus sum_x 2^{v4(x)} x^{-1/2}')
for K in range(2, 7):
    g = G[0]
    tot = F(0)
    for x in range(1, 4 ** K):
        L = law(g, x, K)
        m1 = {}
        for c, p in L.items():
            m1[c[0]] = m1.get(c[0], 0) + p
        tot += max(m1.values())
    ref = 0.0
    for x in range(1, 4 ** K):
        v, y = 0, x
        while y % 4 == 0:
            v += 1
            y //= 4
        ref += 2 ** v / np.sqrt(x)
    print(f'  K={K}: sum of atoms = {float(tot):9.2f}; reference sum = {ref:8.2f}; ratio {float(tot)/ref:.3f}')
