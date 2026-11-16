import sys, time
from collections import Counter
from obs import triples, mixed, rivals, v3
from t4_blocks import GT_adj
# One BH16 block window: region type (iota8=1, mu=0): nu=1, r1=3. Compare BH16 and BH16m4.
h = int(sys.argv[1]); s = int(sys.argv[2]); width = int(sys.argv[3]); variant = sys.argv[4]
A = (h + 1) // 2; K = h // 2; nu = 1; r1 = 3
R = max(y for y in range(1, h + 1) if y % 16 == r1); rho = R - 8
M = 2 * ((width // 4 - A) // 4)  # even block position, block roughly centred
T = 2 * s + 1; Dset = GT_adj(T, h)
cls = []
for i in range(1, A):
    if i % 8 == 1 and 0 <= i + s < K and 2 * i + 1 not in (R, R - 16) and not any(abs(i - k) in Dset for k in cls):
        cls.append(i)
S = set(); lab = set()
for x in range(width):
    if x % 4: S.add((x, 1)); continue
    n = x // 4; i = n - M
    if 0 <= i < A and i in cls:
        S.add((x, 2 * i + 1)); S.add((x, 2 * (i + s) + 2)); lab.add(x); continue
    if n % 2 == nu: S.add((x, rho))
    elif variant == 'BH16' or n % 4 == (nu + 1) % 4: S.add((x, R))
    else: S.add((x, R - 16))
tag = lambda Q: 'S' if (Q[1] == 1 and Q[0] % 4) else ('L' + ('o' if Q[1] % 2 else 'e') if Q[0] in lab else 'F')
t0 = time.time(); C = Counter()
tr = triples(S, h)
for t in tr:
    if t[0] != 'parked': C[('T', t[0], ''.join(sorted(tag(Q) for Q in t[1:4])))] += 1
for W, v in v3(tr).items():
    C[('V3', tuple(sorted(''.join(sorted(tag(Q) for Q in t[1:4])) for t in v)))] += 1
for (a, b, c, d, p, q) in mixed(S, h):
    C[('M', ''.join(tag(Q) for Q in (a, b)) + '/' + ''.join(tag(Q) for Q in (c, d)))] += 1
for (c, d, j) in rivals(S, h):
    C[('R', tag(c) + tag(d))] += 1
print(variant, 's', s, 'labels', cls, dict(C), round(time.time() - t0, 1))
