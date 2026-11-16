# Finite check: all-filler mixed quadruples (tilted side) for a filler row map f: Z/4 -> rows
# (rows given as offsets below R).  Conditions:  16*Sig*a = -alpha*beta ;  16(a^2-c^2) = gamma^2-alpha^2 ;
# a = rB-rA, c = rD-rC (mod 4);  (Sig+a-c)/2 = rC-rA (mod 4);  V != +-U;  N != 0.  alpha = 0 is the
# horizontal case (handled by the DH lemma) and is skipped.  Positions are free in a long gap.
import sys
from math import isqrt
def divisors(n):
    n = abs(n); out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n: out.append(n // d)
    return out
def sols(f):
    out = []
    for rA in range(4):
        for rB in range(4):
            al = f[rB] - f[rA]
            if al == 0: continue
            for rC in range(4):
                for rD in range(4):
                    ga = f[rD] - f[rC]; be = f[rC] + f[rD] - f[rA] - f[rB]
                    if be == 0: continue
                    if (al * be) % 16: continue
                    tgt = -(al * be) // 16
                    for d in divisors(tgt):
                        for a in (d, -d):
                            if (a - (rB - rA)) % 4: continue
                            Sig = tgt // a
                            num = ga * ga - al * al
                            if num % 16: continue
                            c2 = a * a - num // 16
                            if c2 < 0: continue
                            c = isqrt(c2)
                            if c * c != c2: continue
                            for cc in {c, -c}:
                                if (cc - (rD - rC)) % 4: continue
                                if (Sig + a - cc) % 2: continue
                                if ((Sig + a - cc) // 2 - (rC - rA)) % 4: continue
                                if (cc, ga) in ((a, al), (-a, -al)): continue
                                out.append((rA, rB, rC, rD, a, cc, Sig, be // 2))
    return out
nu = 1
for (dp, dm, dr) in [(8, 24, 0), (24, 8, 0), (0, 16, 8), (0, 16, 24), (16, 0, 24), (0, 48, 8), (0, 16, 40), (0, 48, 24), (0, 16, -8)]:
    f = [None] * 4
    f[nu % 4] = f[(nu + 2) % 4] = -dr; f[(nu + 1) % 4] = -dp; f[(nu + 3) % 4] = -dm
    s = sols(f)
    print((dp, dm, dr), 'all-filler tilted quadruples:', len(s), s[:2])
