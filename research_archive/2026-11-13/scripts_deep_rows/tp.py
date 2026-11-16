import sys, time
from collections import Counter
from obs import triples, mixed, rivals, v3
from t4_blocks import GT_adj
# One block window, region type (iota8=1, mu=0): nu=1, r1=3, row-1 sea.
# variants: BH16, BH16m4, PSTAR (rows: R at n=nu+1 mod 4, rho elsewhere)
h = int(sys.argv[1]); s = int(sys.argv[2]); width = int(sys.argv[3]); variant = sys.argv[4]
excl = sys.argv[5].split(',') if len(sys.argv) > 5 else []
verbose = 'v' in sys.argv[6:] if len(sys.argv) > 6 else False
A = (h + 1) // 2; K = h // 2; nu = 1; r1 = 3
R = max(y for y in range(1, h + 1) if y % 16 == r1); rho = R - 8
M = 2 * ((width // 4 - A) // 4)
T = 2 * s + 1; Dset = GT_adj(T, h)
bad_rows = set(int(e) for e in excl if e)
cls = []
if s < 999:
    for i in range(1, A):
        if i % 8 == 1 and 0 <= i + s < K and 2 * i + 1 not in bad_rows and not any(abs(i - k) in Dset for k in cls):
            cls.append(i)
def frow(n):
    if variant == 'BH16':
        return rho if n % 2 == nu else R
    if variant == 'BH16m4':
        if n % 2 == nu: return rho
        return R if n % 4 == (nu + 1) % 4 else R - 16
    if variant == 'PSTAR':
        return R if n % 4 == (nu + 1) % 4 else rho
    if variant == 'PSTAR2':  # mirror: b at nu+3
        return R if n % 4 == (nu + 3) % 4 else rho
S = set(); lab = set()
for x in range(width):
    if x % 4: S.add((x, 1)); continue
    n = x // 4; i = n - M
    if 0 <= i < A and i in cls:
        S.add((x, 2 * i + 1)); S.add((x, 2 * (i + s) + 2)); lab.add(x); continue
    S.add((x, frow(n)))
tag = lambda Q: 'S' if (Q[1] == 1 and Q[0] % 4) else ('L' + ('o' if Q[1] % 2 else 'e') if Q[0] in lab else 'F')
t0 = time.time(); C = Counter()
tr = triples(S, h)
for t in tr:
    C[('T', t[0], ''.join(sorted(tag(Q) for Q in t[1:4])))] += 1
    if verbose and t[0] != 'parked': print('T', t)
for W, v in v3(tr).items():
    C[('V3', tuple(sorted(''.join(sorted(tag(Q) for Q in t[1:4])) for t in v)))] += 1
    if verbose: print('V3', W, v)
for (a, b, c, d, p, q) in mixed(S, h):
    C[('M', ''.join(tag(Q) for Q in (a, b)) + '/' + ''.join(tag(Q) for Q in (c, d)))] += 1
    if verbose: print('M', (a, b, c, d), 'p', p, 'q', q, [Q[0]//4 % 4 for Q in (a,b,c,d)])
for (c, d, j) in rivals(S, h):
    C[('R', tag(c) + tag(d))] += 1
    if verbose: print('R', c, d, j)
print(variant, 'h', h, 's', s, 'R', R, 'rho', rho, 'labels', cls)
for k, v in sorted(C.items()): print('  ', k, v)
print('time', round(time.time() - t0, 1))
