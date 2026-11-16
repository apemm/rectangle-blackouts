"""Sanity check for the stride-4u constant sweep (menu board).
Part 1: margins and constants for odd u (exact rationals).
Part 2: region congruences on true positions for u in {3,5,7,13}:
  (C1) slot residue mod 16, the twisted type phase, the even-label lattice
  u*y = 2n + 2u + 2*kappa_tau (mod 32), and the failure of the stride-4 phase formula.
"""
from fractions import Fraction as Fr
import random, sys

def is_prime(n):
    if n < 2: return False
    for q in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % q == 0: return n == q
    d, s = n-1, 0
    while d % 2 == 0: d//=2; s+=1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x = pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(s-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True

def jacobi(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3,5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0

def P(u): return max(40, 8*u*u+4)

print("Part 1: constants by u")
worst = {}
for u in range(1, 400, 2):
    D = 4*u*u+1; Pu = P(u)
    rigid = 1 + Fr(D, 8*u*(Pu-u) - D)
    ladic = 1 + Fr(u, 2*Pu - 3*u)
    p1c = 1 + Fr(D, 4*u*(2*Pu-3*u) - 1)
    gap = 4*(Pu - Fr(u,2))
    prop4 = Fr(420*420, 4) / (Pu - Fr(u,2))   # h needed: 4*gap*h > 420^2
    F2 = 4*(Pu-u); Foo = 16*(Pu-u); I2 = 8*u*(2*Pu-u)
    for k,v in (("rigid",rigid),("ladic",ladic),("p1c",p1c)):
        worst[k] = max(worst.get(k, 0), v) if u >= 3 else worst.get(k, 0)
    if u in (1,3,5,7,13):
        print(f"u={u:3d} D={D} P={Pu} rigid={float(rigid):.5f} ladic={float(ladic):.5f} "
              f"p1c={float(p1c):.5f} gap={float(gap):.1f}h prop4_h>={float(prop4):.1f} "
              f"F2=h/{F2} Foo=h/{Foo} I2=h/{I2} lsep_over_h2={66.56*Pu:.0f}")
print("max over odd 3<=u<400:", {k: float(v) for k,v in worst.items()})

print("Part 2: true-position congruences")
random.seed(1)
for u in (3,5,7,13):
    D = 4*u*u+1; Pu = P(u)
    for h in (1001, 1500):
        l = next(q for q in range(int(1.04*h)+1, int(2.08*h)+1) if is_prime(q) and jacobi(D,q) == -1)
        p = next(q for q in range(Pu*h+1, 2*Pu*h+1) if is_prime(q) and q % 4 == 3 and jacobi(D,q) == -1)
        A = (h+1)//2; K = h//2; M = 16*l
        pinv = pow(p, -1, M)
        bad = {"C1":0, "lat":0, "C7":0, "inj":0}; old_wrong = 0; tested = 0
        for _ in range(6):
            iota = random.randrange(32); sigma = random.randrange(16)
            kappa = random.randrange(1000); b = random.randrange(1000)
            kt = kappa - b
            rho_tau = (u*(iota+sigma) - kt) % 16
            old = (iota + sigma - kt) % 16
            labs = []
            for i in range(iota, A, 32):
                for j in range(K):
                    if (j - i - sigma) % 16: continue
                    s = j - i
                    k = random.randrange(8)
                    t = (pinv*(u*s - kappa)) % M + M*k
                    n = u*i + p*t + b
                    labs.append((i, j, n))
            seen = set()
            for (i, j, n) in labs:
                tested += 1
                if n % 16 != rho_tau: bad["C1"] += 1
                if (u*(2*j+2) - (2*n + 2*u + 2*kt)) % 32: bad["lat"] += 1
                if (n - (u*j - kt)) % M: bad["C7"] += 1
                if n in seen: bad["inj"] += 1
                seen.add(n)
            if old % 4 != rho_tau % 4: old_wrong += 1
        print(f"u={u} h={h} l={l} p={p} labels={tested} failures={bad} "
              f"types_where_stride4_rho0_wrong={old_wrong}/6")
