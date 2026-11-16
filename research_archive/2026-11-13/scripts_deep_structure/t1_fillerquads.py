# Finite, h-independent check: all-filler tilted-side mixed quadruples in the Q4 layer.
# Fillers at (4n, Y + 16*phi(n mod 4)). Quadruple data: residues rA!=rB, rC!=rD,
# a = nB-nA (a = rB-rA mod 4), c = nD-nC, Sigma = nC+nD-nA-nB.
# Conditions (derived):  a*Sigma = -16*dAB*S,  a^2 - c^2 = 16*(dCD^2 - dAB^2),
# Sigma = rC+rD-rA-rB (mod 4), Sigma + a - c even, V != +-U, N != 0.
from itertools import permutations
from math import isqrt

def divisors(n):
    n = abs(n); out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n: out.append(n // d)
    return out

def solutions(phi):
    sols = []
    for rA in range(4):
        for rB in range(4):
            if rA == rB: continue
            for rC in range(4):
                for rD in range(4):
                    if rC == rD: continue
                    dAB = phi[rB] - phi[rA]; dCD = phi[rD] - phi[rC]
                    S = phi[rC] + phi[rD] - phi[rA] - phi[rB]
                    if S == 0: continue  # then Sigma = 0, N = 0
                    tgt = 16 * dAB * S
                    for d in divisors(tgt):
                        for a in (d, -d):
                            if (a - (rB - rA)) % 4: continue
                            Sig = -tgt // a
                            if (Sig - (rC + rD - rA - rB)) % 4: continue
                            c2 = a * a - 16 * (dCD * dCD - dAB * dAB)
                            if c2 < 0: continue
                            c = isqrt(c2)
                            if c * c != c2: continue
                            for cc in {c, -c}:
                                if (cc - (rD - rC)) % 4: continue
                                if (Sig + a - cc) % 2: continue
                                if ((Sig + a - cc) // 2 - (rC - rA)) % 4: continue
                                if (cc, dCD) in ((a, dAB), (-a, -dAB)): continue
                                sols.append((rA, rB, rC, rD, a, cc, Sig, 8 * S))
    return sols

good = []
for phi in permutations(range(4)):
    s = solutions(phi)
    print(phi, len(s), s[:3])
    if not s: good.append(phi)
print('phi with no all-filler tilted quadruple:', good)
# also spread patterns phi in {0,1,2,4},{0,1,3,4},... (rows not consecutive)
for base in ([0, 1, 2, 4], [0, 1, 3, 4], [0, 2, 3, 4], [0, 1, 2, 5], [0, 1, 3, 7]):
    for phi in permutations(base):
        if not solutions(phi): print('good spread', phi)
