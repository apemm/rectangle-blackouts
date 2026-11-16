import random, sys
from obs import mixed
from t4_blocks import make
h = int(sys.argv[1]); P = int(sys.argv[2]); nb = int(sys.argv[3])
rnd = random.Random(1); A = (h + 1) // 2; K = h // 2
for seed in range(2):
    diags = [rnd.randrange(-(A - 1) + 3, K - 3) for _ in range(nb)]
    S, labels, rs = make(h, 'C', diags, P, seed)
    labcols = {x for (x, i, s) in labels}
    def tag(Q):
        if Q[1] == rs and Q[0] % 4: return 'S'
        if Q[0] in labcols: return 'L'
        return 'F'
    for (a, b, c, d, p, q) in mixed(S, h):
        if min(p[1], q[1]) < rs:
            print(''.join(tag(Q) for Q in (a, b, c, d)), a, b, c, d, 'p', p, 'q', q)
