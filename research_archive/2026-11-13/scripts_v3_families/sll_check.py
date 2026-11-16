"""Brute-force check of the SLL claims in a synthetic L** row-1 region:
all tilted rectangles with a shallow corner (row 1, column != 0 mod 4) and two
label corners; classify vertex/end type, same class or not, W parked/fatal,
and count V3 collisions at a common W.  One class per diagonal, rigid rule."""
import sys
from sympy import isprime
from collections import defaultdict
h, iota, cpair = int(sys.argv[1]), int(sys.argv[2]), [int(x) for x in sys.argv[3].split(',')]
K = h // 2; nu = (K - 1).bit_length(); N2 = 2 ** nu; assert N2 >= K
p = next(q for q in range(20 * h + 1, 40 * h) if isprime(q) and q % 20 in (3, 7))
kappa = 0; pinv = pow(p, -1, N2)
pts = {}  # (x,y) -> (class id, parity)
cls = 0; used_m = set()
for s in range(-K, K):
    if s % 16 not in cpair: continue
    m = ((s - kappa) * pinv) % N2
    while m in used_m: m += N2
    used_m.add(m)
    M = p * m
    for i in range(iota, K + 1, 32):
        j = i + s
        if 2 * i + 1 > h or j < 0 or 2 * j + 2 > h or i == 0: continue
        n = i + M
        assert (s - M - kappa) % N2 == 0
        pts[(4 * n, 2 * i + 1)] = (cls, 'o'); pts[(4 * n, 2 * j + 2)] = (cls, 'e')
    cls += 1
cols = defaultdict(list)
for (x, y), v in pts.items(): cols[x].append(y)
def black(x, y):
    if y == 1 and x % 4: return True
    return (x, y) in pts
W2 = ((h - 1) ** 2) // 4 + 1
L = sorted(pts)
stats = defaultdict(int); atW = defaultdict(list)
def record(kind, E, A, B, W):
    xw, yw = W
    if not (1 <= yw <= h): return
    if black(xw, yw): stats['fully_black ' + kind] += 1; return
    col = [1] if xw % 4 else cols.get(xw, [])
    par = all((y - yw) % 2 == 0 for y in col)
    same = pts[A][0] == pts[B][0]
    key = f"{kind} {'parked' if par else 'FATAL'} {'intra' if same else 'cross'} {pts[A][1]}{pts[B][1]}"
    stats[key] += 1
    if par: atW[W].append((kind, E, A, B))
for a in range(len(L)):
    P = L[a]
    for b in range(a + 1, len(L)):
        Q = L[b]
        if Q[0] - P[0] > 2 * W2: break
        if Q[0] == P[0]: continue
        # E vertex: (xP-x)(xQ-x) + (yP-1)(yQ-1) = 0
        S = P[0] + Q[0]; C = P[0] * Q[0] + (P[1] - 1) * (Q[1] - 1)
        D = S * S - 4 * C
        if D >= 0:
            r = int(D ** 0.5)
            while r * r > D: r -= 1
            while (r + 1) ** 2 <= D: r += 1
            if r * r == D and (S + r) % 2 == 0:
                for x in {(S + r) // 2, (S - r) // 2}:
                    if x % 4: record('Evertex', (x, 1), P, Q, (P[0] + Q[0] - x, P[1] + Q[1] - 1))
        # E end, vertex V in {P,Q}, other end G
        for V, G in ((P, Q), (Q, P)):
            dx, dy = G[0] - V[0], G[1] - V[1]
            f = V[1] - 1
            if (f * dy) % dx == 0:
                aa = f * dy // dx
                xE = V[0] + aa
                if xE % 4 and aa != 0:
                    record('Pc-like', (xE, 1), V, G, (xE + dx, 1 + dy))
for k in sorted(stats): print(k, stats[k])
v3 = sum(1 for W, l in atW.items() if len(l) > 1)
print("h", h, "p", p, "labels", len(L) // 2, "classes", cls, "W with >=2 parked SLL triples:", v3)
