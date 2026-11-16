import random, sys, time
from collections import Counter
from obs import triples, mixed, rivals, v3
# Generic region test. Shallow sea in row rs at columns != 0 mod 4.
# Deep columns: random doubles (odd row from okodd, even row from okeven) or fillers (rows okfill).
def board(h, width, rs, okodd, okeven, okfill, seed, pdouble=0.7):
    rnd = random.Random(seed)
    S = set()
    for x in range(width):
        if x % 4:
            S.add((x, rs))
        else:
            if rnd.random() < pdouble:
                S.add((x, rnd.choice(okodd))); S.add((x, rnd.choice(okeven)))
            else:
                S.add((x, rnd.choice(okfill)))
    return S

def run(h, width, rs, okodd, okeven, okfill, seeds=2):
    shallow = lambda P: P[1] == rs and P[0] % 4 != 0
    C = Counter()
    for seed in range(seeds):
        S = board(h, width, rs, okodd, okeven, okfill, seed)
        tr = triples(S, h)
        for t in tr:
            ns = sum(shallow(P) for P in t[1:4])
            low = t[4][1] < rs
            if t[0] != 'parked' and (ns >= 1 or low):
                C[('T', t[0], 'ns=%d' % ns, 'Wlow' if low else '')] += 1
        for W, v in v3(tr).items():
            ns = max(sum(shallow(P) for P in t[1:4]) for t in v)
            C[('V3', 'maxns=%d' % ns, 'Wlow' if W[1] < rs else '')] += 1
        for (A, B, Cc, D, p, q) in mixed(S, h):
            ns = ''.join('1' if shallow(P) else '0' for P in (A, B, Cc, D))
            low = min(p[1], q[1]) < rs
            if ns != '0000' or low:
                C[('M', ns, 'pqlow' if low else '')] += 1
        for (Cc, D, j) in rivals(S, h):
            ns = shallow(Cc) + shallow(D)
            low = Cc[1] - j < rs
            if ns or low:
                C[('R', ns, 'low' if low else '')] += 1
    return C

if __name__ == '__main__':
    mode = sys.argv[1]; h = int(sys.argv[2]); width = int(sys.argv[3])
    t0 = time.time()
    if mode == 'A':   # row 1, odd i
        okodd = [y for y in range(3, h + 1, 2) if y % 4 == 3]
        okeven = list(range(2, h + 1, 2))
        okfill = [y for y in range(3, h + 1) if y % 4 == 3]
        rs = 1
    elif mode == 'C':  # row 3, i even >= 4, j = K+1 mod 2, j >= 2; fillers rows = 1 mod 4 >= 9
        K = h // 2
        okodd = [y for y in range(9, h + 1, 2) if y % 4 == 1]
        okeven = [2 * j + 2 for j in range(2, K) if j % 2 == (K + 1) % 2]
        okfill = [y for y in range(9, h + 1) if y % 4 == 1]
        rs = 3
    res = run(h, width, rs, okodd, okeven, okfill)
    for k, v in sorted(res.items(), key=lambda kv: -kv[1]):
        print(k, v)
    print('time', round(time.time() - t0, 1))
