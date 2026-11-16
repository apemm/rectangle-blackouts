import sys, time, random
from collections import Counter
from obs import triples, mixed, rivals, v3
from t4_blocks import GT_adj
# Region A (row-1 sea), labels i = 1 mod 4, rigid: M = s - kappa mod 2^nu (kappa=0).
# Deep layer 'lat': every non-label deep column n gets an even row y = 2(n+1) mod 2^(nu+1).
# Deep layer 'bh': BH16-like odd rows (base R / hole rho by n parity), for comparison.
h = int(sys.argv[1]); nb = int(sys.argv[2]); layer = sys.argv[3]; seed = int(sys.argv[4])
A = (h + 1) // 2; K = h // 2
nu = 0
while 2 ** nu < K / 2: nu += 1
mod = 2 ** (nu + 1)
rnd = random.Random(seed)
S = set(); lab = set(); used = set()
Pslots = 3 * A
# positions: M_b = s_b mod 2^nu, increasing
pos = 0; blocks = []
for b in range(nb):
    s = rnd.randrange(-(A - 1) + 2, K - 2)
    M = pos + ((s - pos) % (2 ** nu))
    pos = M + Pslots
    T = 2 * s + 1; Dset = GT_adj(T, h)
    cls = []
    cand = [i for i in range(1, A) if i % 4 == 1 and 0 <= i + s < K]
    rnd.shuffle(cand)
    for i in cand:
        if not any(abs(i - k) in Dset for k in cls): cls.append(i)
    for i in cls:
        x = 4 * (i + M); S.add((x, 2 * i + 1)); S.add((x, 2 * (i + s) + 2)); lab.add(x)
width = 4 * (pos + A)
r1 = 3; R = max(y for y in range(1, h + 1) if y % 16 == r1); rho = R - 8
for x in range(width):
    if x % 4: S.add((x, 1)); continue
    if x in lab: continue
    n = x // 4
    if layer == 'lat':
        rows = [y for y in range(2, h + 1, 2) if (y - 2 * (n + 1)) % mod == 0]
        S.add((x, rnd.choice(rows)))
    else:
        S.add((x, rho if n % 2 == 1 else R))
sh = lambda Q: Q[1] == 1 and Q[0] % 4 != 0
tag = lambda Q: 'S' if sh(Q) else ('L' + ('o' if Q[1] % 2 else 'e') if Q[0] in lab else 'F')
t0 = time.time(); C = Counter()
tr = triples(S, h)
for t in tr:
    if t[0] != 'parked': C[('T', t[0], ''.join(sorted(tag(Q) for Q in t[1:4])))] += 1
for W, v in v3(tr).items():
    C[('V3', tuple(sorted(''.join(sorted(tag(Q) for Q in t[1:4])) for t in v)))] += 1
for (a, b, c, d, p, q) in mixed(S, h):
    C[('M', ''.join(sorted(tag(Q) for Q in (a, b))) + '/' + ''.join(sorted(tag(Q) for Q in (c, d))))] += 1
for (c, d, j) in rivals(S, h):
    C[('R', ''.join(sorted(tag(c) + tag(d))))] += 1
print(layer, 'h', h, 'nu', nu, 'width', width, 'labels', len(lab), dict(sorted(C.items(), key=lambda kv: -kv[1])), round(time.time() - t0, 1))
