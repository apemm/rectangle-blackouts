import sys, time, random
from math import isqrt
from collections import Counter
from obs import triples, mixed, rivals, v3
# Structured test: blocks = constant-offset classes (independent in G_T, slots of one i-parity),
# stride 4, block positions spaced by P slots. Region 'A': row-1 sea, i odd, fillers rows = 3 mod 4,
# gap deep columns at row g.  Region 'C': row-3 sea, i even (i >= 4), j >= 2, fillers rows = 1 mod 4 (>= 9),
# extra forbidden pairs (i, i-2) for i in {4, 8, 16}.
def GT_adj(T, h):
    D = set()
    for d in range(1, h):
        L2 = 20 * d * d + 4 * T * d + T * T
        L = isqrt(L2)
        if L * L == L2 and 0 < L < h:
            D.add(d)
        L2 = 20 * d * d - 4 * T * d + T * T
        L = isqrt(L2)
        if L * L == L2 and 0 < L < h:
            D.add(d)
    return D

def make(h, mode, diag_list, P, seed):
    rnd = random.Random(seed)
    A = (h + 1) // 2; K = h // 2
    g = h if h % 2 == 0 else h - 1
    S = set(); labels = []
    rs = 1 if mode == 'A' else 3
    fill_rows = [y for y in range(9, h) if (y % 4 == 3 if mode == 'A' else y % 4 == 1) and y != g]
    width = 4 * P * (len(diag_list) + 1)
    used = {}
    for b, s in enumerate(diag_list):
        T = 2 * s + 1
        Dset = GT_adj(T, h)
        M = P * (b + 1)
        cls = []
        cand = [i for i in range(1, A) if 0 <= i + s < K]
        if mode == 'A':
            cand = [i for i in cand if i % 2 == 1]
        else:
            cand = [i for i in cand if i % 2 == 0 and i >= 4 and i + s >= 2]
        rnd.shuffle(cand)
        for i in cand:
            if any(abs(i - i2) in Dset for i2 in cls):
                continue
            if mode == 'C' and any((i, i2) in ((4, 2), (8, 6), (16, 14), (2, 4), (6, 8), (14, 16)) for i2 in cls):
                continue
            cls.append(i)
        for i in range(0, A):
            x = 4 * (i + M)
            if i in cls:
                S.add((x, 2 * i + 1)); S.add((x, 2 * (i + s) + 2)); labels.append((x, i, s))
            else:
                S.add((x, rnd.choice(fill_rows)))
            used[x] = True
    for x in range(width):
        if x % 4:
            S.add((x, rs))
        elif x not in used:
            S.add((x, g))
    return S, labels, rs

if __name__ == '__main__':
    mode = sys.argv[1]; h = int(sys.argv[2]); P = int(sys.argv[3]); nb = int(sys.argv[4])
    t0 = time.time()
    rnd = random.Random(1)
    A = (h + 1) // 2; K = h // 2
    C = Counter()
    for seed in range(2):
        diags = [rnd.randrange(-(A - 1) + 3, K - 3) for _ in range(nb)]
        S, labels, rs = make(h, mode, diags, P, seed)
        sh = lambda Q: Q[1] == rs and Q[0] % 4 != 0
        tr = triples(S, h)
        for t in tr:
            if t[0] != 'parked':
                ns = sum(sh(Q) for Q in t[1:4])
                C[('T', t[0], 'ns=%d' % ns, 'Wlow' if t[4][1] < rs else '')] += 1
        for W, v in v3(tr).items():
            C[('V3', len(v))] += 1
        for (a, b, c, d, p, q) in mixed(S, h):
            ns = ''.join('1' if sh(Q) else '0' for Q in (a, b, c, d))
            C[('M', ns, 'pqlow' if min(p[1], q[1]) < rs else '')] += 1
        for r in rivals(S, h):
            C[('R',)] += 1
    for k, v in sorted(C.items(), key=lambda kv: -kv[1]):
        print(k, v)
    print('time', round(time.time() - t0, 1))
