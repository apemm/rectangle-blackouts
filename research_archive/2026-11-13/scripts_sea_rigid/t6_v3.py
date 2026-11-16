import random, sys
from collections import Counter
from obs import triples, v3, mixed
from t4_blocks import make
mode = sys.argv[1]; h = int(sys.argv[2]); P = int(sys.argv[3]); nb = int(sys.argv[4])
rnd = random.Random(1); A = (h + 1) // 2; K = h // 2
C = Counter()
for seed in range(2):
    diags = [rnd.randrange(-(A - 1) + 3, K - 3) for _ in range(nb)]
    S, labels, rs = make(h, mode, diags, P, seed)
    labcols = {x for (x, i, s) in labels}
    lab = lambda Q: Q[0] in labcols
    shl = lambda Q: Q[1] == rs and Q[0] % 4 != 0
    tag = lambda Q: 'S' if shl(Q) else ('L' if lab(Q) else 'F')
    tr = triples(S, h)
    for W, v in v3(tr).items():
        tags = tuple(sorted(''.join(sorted(tag(Q) for Q in t[1:4])) for t in v))
        C[('V3',) + tags] += 1
    for (a, b, c, d, p, q) in mixed(S, h):
        tg = ''.join(tag(Q) for Q in (a, b, c, d))
        if 'F' not in tg:
            C[('M', tg)] += 1
for k, v in sorted(C.items(), key=lambda kv: -kv[1]): print(k, v)
