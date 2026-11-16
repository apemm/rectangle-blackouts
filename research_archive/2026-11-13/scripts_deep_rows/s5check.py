"""Cross-block label-label deep M2a (S5) in a rigid layout.  Blocks at M = p*k with diagonal s,
M = s - kappa (mod 2^nu).  Labels i = iota8 (mod 8) (all such slots, a superset of any class).
Counts block pairs and Delta i with 4 delta^2 + eps^2 a nonzero square, eps = 0 mod 4 (Lemma A2):
 odd-odd: delta = Di + DM, eps = Di;  even-even: delta = Di + DM, eps = Di + Ds."""
import sys, random
from math import isqrt
def isprime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
h = int(sys.argv[1]); pmod = sys.argv[2]; nufac = int(sys.argv[3]); nb = int(sys.argv[4])
A = (h + 1) // 2; K = h // 2; iota8 = 1; kappa = 0
nu = 0
while 2 ** nu < K / nufac: nu += 1
pf = int(sys.argv[5]) if len(sys.argv) > 5 else 20
p = next(q for q in range(pf * h + 1, 80 * h) if isprime(q) and ((q % 5 in (2, 3)) if pmod == 'nr' else (q % 5 in (1, 4))))
rnd = random.Random(5)
blocks = []
for k in range(1, nb + 1):
    M = p * k
    r = (M + kappa) % (2 ** nu)
    cand = [s for s in range(-(A - 1), K) if s % (2 ** nu) == r]
    blocks.append((M, rnd.choice(cand)))
reach = h * h // 16
oo = ee = 0
for a in range(nb):
    for b in range(nb):
        if a == b: continue
        (M1, s1), (M2, s2) = blocks[a], blocks[b]
        DM = M2 - M1
        if abs(DM) > reach + A: continue
        for Di in range(-(A - 1), A):
            if Di % 8: continue
            d = Di + DM
            for kind, eps in (('o', Di), ('e', Di + s2 - s1)):
                if eps == 0 or eps % 4: continue
                v = 4 * d * d + eps * eps
                r = isqrt(v)
                if r * r == v:
                    if kind == 'o': oo += 1
                    else: ee += 1
print('h', h, 'p', p, 'p mod 5', p % 5, '2^nu', 2 ** nu, 'K', K, 'blocks', nb, 'odd-odd A2 (block pair, Di):', oo, 'even-even:', ee)
