import sys, time
from collections import Counter
from obs import triples, mixed, rivals, v3
# Pure gap of BH16 (rows R base, rho hole) and of the mod-4 variant (base rows R / R-16 by n mod 4).
h = int(sys.argv[1]); width = int(sys.argv[2]); r1 = int(sys.argv[3]); nu = 0
R = max(y for y in range(1, h + 1) if y % 16 == r1 % 16); rho = R - 8
for variant in ('BH16', 'BH16m4'):
    S = set()
    for x in range(width):
        if x % 4: S.add((x, 1)); continue
        n = x // 4
        if n % 2 == nu: S.add((x, rho))
        elif variant == 'BH16' or n % 4 == (nu + 1) % 4: S.add((x, R))
        else: S.add((x, R - 16))
    t0 = time.time(); C = Counter()
    tr = triples(S, h)
    for t in tr:
        if t[0] != 'parked': C[('T', t[0])] += 1
    C[('V3',)] = len(v3(tr)); C[('M',)] = len(mixed(S, h)); C[('R',)] = len(rivals(S, h))
    print(variant, 'R', R, 'rho', rho, dict(C), round(time.time() - t0, 1))
