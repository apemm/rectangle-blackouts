# Exact atoms of RQC: (a) rank view: x-coordinate of the cell at offset o in a level-k node;
# (b) cell view: rank offset of a fixed cell in a level-k node. Max over the 12 types.
import random, numpy as np
from rqc import TYPES, configs
TI = {t:i for i,t in enumerate(TYPES)}
CF = {}
def cf(tau, s):
    key = (tau, s>1)
    if key not in CF: CF[key] = configs(tau, s)
    return CF[key]

def rank_view(k, o):
    D = [np.array([1.0]) for _ in TYPES]          # level 0: cell, x = 0
    for j in range(1, k+1):
        d = (o >> (2*(j-1))) & 3
        s = 1 << (j-1)
        ND = []
        for tau in TYPES:
            arr = np.zeros(2*s)
            for (p, order, ct) in cf(tau, s):
                q = order[d]
                child = D[TI[ct[d]]] if ct[d] is not None else D[0]
                arr[q[0]*s:q[0]*s+s] += p*child
            ND.append(arr)
        D = ND
    return max(a.max() for a in D)

def cell_view(k, cx, cy):
    D = [np.array([1.0]) for _ in TYPES]
    for j in range(1, k+1):
        s = 1 << (j-1)
        q = ((cx >> (j-1)) & 1, (cy >> (j-1)) & 1)
        ND = []
        for tau in TYPES:
            arr = np.zeros(4*s*s)
            for (p, order, ct) in cf(tau, s):
                pos = order.index(q)
                child = D[TI[ct[pos]]] if ct[pos] is not None else D[0]
                arr[pos*s*s:pos*s*s+s*s] += p*child
            ND.append(arr)
        D = ND
    return max(a.max() for a in D)

rng = random.Random(7)
print("rank view: 2^k * max_x P(x | type, o), quantiles over random o")
for k in range(3, 12):
    vals = sorted(rank_view(k, rng.randrange(4**k)) * 2**k for _ in range(60))
    print(k, "median %.2f  90%% %.2f  max %.2f" % (vals[30], vals[54], vals[-1]))
print("cell view: max_y P(offset = y | type, cell); scaled by 2^k and by 4^k")
for k in range(3, 9):
    vals = sorted(cell_view(k, rng.randrange(2**k), rng.randrange(2**k)) for _ in range(30))
    med = vals[15]
    print(k, "median*2^k %.2f  median*4^k %.1f  max*2^k %.2f" % (med*2**k, med*4**k, vals[-1]*2**k))
