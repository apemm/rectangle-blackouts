"""Monte Carlo: rank-averaged one-coordinate displacement atoms of random CGK curves.
f_x(z) = (1/N) sum_r P(H(r+x)_1 - H(r)_1 = z). Report sqrt(x) * max_z f_x(z)
and for 2D: x * max_z (1/N) sum_r P(H(r+x) - H(r) = z)."""
import sys, time, itertools
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

NR = np.zeros(12, int)
POS = np.zeros((12, 6, 4, 2), int)
CG = np.zeros((12, 6, 4), int)
BPOS = np.zeros((12, 2, 4, 2), int)
for g in G:
    gi = GI[g]
    Rg = refs(g)
    NR[gi] = len(Rg)
    for j, (o, cg) in enumerate(Rg):
        POS[gi, j] = np.array(o)
        CG[gi, j] = [GI[c] for c in cg]
    mids = [c for c in C if c not in g]
    for j, m in enumerate(itertools.permutations(mids)):
        BPOS[gi, j] = np.array((g[0],) + m + (g[1],))

def curve(n, rng, root=0):
    # nodes at current level, in rank order
    gate = np.array([root])
    org = np.zeros((1, 2), int)
    for lev in range(n, 1, -1):  # node side 2^lev, children side 2^(lev-1) >= 2
        s = 1 << (lev - 1)
        j = (rng.random(len(gate)) * NR[gate]).astype(int)
        pos = POS[gate, j]            # (m,4,2)
        cg = CG[gate, j]              # (m,4)
        org = (org[:, None, :] + s * pos).reshape(-1, 2)
        gate = cg.reshape(-1)
    j = (rng.random(len(gate)) * 2).astype(int)
    pos = BPOS[gate, j]
    cells = (org[:, None, :] + pos).reshape(-1, 2)
    return cells

def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    reps = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    rng = np.random.default_rng(12345)
    xs = [2048, 2049, 3073, 4096, 4097, 4113, 4352, 5000, 6007, 9472, 9473, 9488, 9500, 9999]
    acc1 = {x: {} for x in xs}
    acc2 = {x: {} for x in xs}
    t0 = time.time()
    N = 4 ** n
    for rep in range(reps):
        c = curve(n, rng, root=rep % 12)
        H = c  # H[r] = cell at rank r
        assert len(np.unique(H[:, 0] * (1 << n) + H[:, 1])) == N
        for x in xs:
            d = H[x:] - H[:-x]
            v, cnt = np.unique(d[:, 0], return_counts=True)
            a = acc1[x]
            for vv, cc in zip(v.tolist(), cnt.tolist()):
                a[vv] = a.get(vv, 0) + cc
            key = d[:, 0] * 4096 + d[:, 1]
            v, cnt = np.unique(key, return_counts=True)
            a = acc2[x]
            for vv, cc in zip(v.tolist(), cnt.tolist()):
                a[vv] = a.get(vv, 0) + cc
        if time.time() - t0 > 45:
            reps = rep + 1
            break
    print(f'n={n}, curves={reps}, time {time.time()-t0:.1f}s')
    print('     x   v4  sqrt(x)*max1D   x*max2D   (ideal: O(1) and O(1))')
    for x in xs:
        tot = (N - x) * reps
        m1 = max(acc1[x].values()) / tot
        m2 = max(acc2[x].values()) / tot
        v4 = 0
        y = x
        while y % 4 == 0:
            v4 += 1
            y //= 4
        print(f'{x:6d}  {v4:2d}   {np.sqrt(x)*m1:8.3f}     {x*m2:9.2f}')

main()
