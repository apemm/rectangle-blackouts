import sys
from obs import mixed, triples
from t2_regionC import board
h = int(sys.argv[1]); width = int(sys.argv[2])
K = h // 2
okodd = [y for y in range(9, h + 1, 2) if y % 4 == 1]
okeven = [2 * j + 2 for j in range(2, K) if j % 2 == (K + 1) % 2]
okfill = [y for y in range(9, h + 1) if y % 4 == 1]
rs = 3
sh = lambda P: P[1] == rs and P[0] % 4 != 0
for seed in range(3):
    S = board(h, width, rs, okodd, okeven, okfill, seed)
    for (A, B, C, D, p, q) in mixed(S, h):
        if min(p[1], q[1]) < rs:
            ns = ''.join('1' if sh(P) else '0' for P in (A, B, C, D))
            # relative to the deep points
            print(ns, 'A', A, 'B', B, 'C', C, 'D', D, 'p', p, 'q', q,
                  'u', (B[0]-A[0], B[1]-A[1]), 'n', ((p[0]-A[0]), (p[1]-A[1])))
    for t in triples(S, h):
        if t[0] != 'parked' and t[4][1] < rs:
            print('T', t)
