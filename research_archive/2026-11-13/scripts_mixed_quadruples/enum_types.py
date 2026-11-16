"""Equation-based enumeration of the two surviving label-only mixed-quadruple types,
with a definition-level check of every hit.

Scaffold: stride s even, P = p prime > max(20h,(s^2/2+4)h); class c at columns s(i+Pc);
label (i, i+s_T) of offset T: odd point (s(i+Pc), 2i+1), even point (s(i+Pc), 2i+1+T).
Classes are taken as FULL diagonals (supersets of any class).

Type I.2: A odd, B even in block c (offset T), slots iA, iA+a; C odd, D even in block c+dc
          (offset T2), slots iC, iC+b.
   E1: (s^2+4)a^2+4aT+T^2 = (s^2+4)b^2+4bT2+T2^2
   E2: m*kappa = -(2 s^2 a P dc + (2a+T)(T2-T)),  kappa=(s^2+4)a+2T, m = iC+iD-iA-iB.
Type II: A,C in block c (offset T), B,D in block c+dc (offset T2), one odd and one even point
          in each block.  g = C-A = (s d, 2d + tau T), g' = D-B = (s d2, 2d2 + tau2 T2),
          U = B-A = (s(P dc + k), U2), U2 = 2k + eB T2 - eA T.
   E*: 4 U2 (d2*eta - d*eta2) = (d+d2)|g'-g|^2,   eta = 2d+tau T, eta2 = 2d2+tau2 T2
   E**: s^2 P dc d = |g'-g|^2/4 - s^2 d k - U2 eta   (or the d2-version if d = 0).
usage: py enum_types.py h s [maxprint]
"""
import sys
from math import isqrt
from collections import Counter

def isprime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

h, s = int(sys.argv[1]), int(sys.argv[2])
maxprint = int(sys.argv[3]) if len(sys.argv) > 3 else 3
A = (h + 1) // 2; K = h // 2
p = max(20 * h, (s * s // 2 + 4) * h) + 1
while not isprime(p): p += 1
P = p
W = (h - 1) ** 2 // 4

def slots(T):
    st = (T - 1) // 2
    return [i for i in range(A) if 0 <= i + st < K]

def point(c, T, i, e):
    return (s * (i + P * c), 2 * i + 1 + (T if e else 0))

def is_mixed(Ap, Bp, Cp, Dp):
    ux, uy = Bp[0] - Ap[0], Bp[1] - Ap[1]
    vx, vy = Dp[0] - Cp[0], Dp[1] - Cp[1]
    if ux == 0: return False
    if ux * ux + uy * uy != vx * vx + vy * vy: return False
    nx2 = Cp[0] + Dp[0] - Ap[0] - Bp[0]; ny2 = Cp[1] + Dp[1] - Ap[1] - Bp[1]
    if nx2 % 2 or ny2 % 2: return False
    nx, ny = nx2 // 2, ny2 // 2
    if (nx, ny) == (0, 0) or nx * ux + ny * uy != 0: return False
    if (vx, vy) in ((ux, uy), (-ux, -uy)): return False
    if len({Ap, Bp, Cp, Dp}) < 4: return False
    return 1 <= Ap[1] + ny <= h and 1 <= Bp[1] + ny <= h

odd_offsets = [T for T in range(-h + 1, h) if T % 2 and slots(T)]
Q = lambda T, a: (s * s + 4) * a * a + 4 * a * T + T * T
# ---------------- Type I.2 ----------------
amax = 2 * (h - 1) ** 2 // (s * s * (2 * P - h - 1)) + 1
cnt1 = Counter(); ex1 = []
bylen = {}
for T2 in odd_offsets:
    for b in range(-A, A + 1):
        if b == 0: continue
        bylen.setdefault(Q(T2, b), []).append((T2, b))
dcmax = 30
for T in odd_offsets:
    sl = set(slots(T))
    for a in range(-amax, amax + 1):
        if a == 0: continue
        kappa = (s * s + 4) * a + 2 * T
        for (T2, b) in bylen.get(Q(T, a), []):
            if (b, T2) in ((a, T), (-a, -T)): continue
            sl2 = set(slots(T2))
            for dc in range(-dcmax, dcmax + 1):
                if dc == 0: continue
                num = -(2 * s * s * a * P * dc + (2 * a + T) * (T2 - T))
                if num % kappa: continue
                m = num // kappa
                if (m + a - b) % 2: continue
                e = (m + a - b) // 2  # iC - iA
                for iA in sl:
                    if iA + a not in sl or iA + e not in sl2 or iA + e + b not in sl2: continue
                    Ap = point(0, T, iA, 0); Bp = point(0, T, iA + a, 1)
                    Cp = point(dc, T2, iA + e, 0); Dp = point(dc, T2, iA + e + b, 1)
                    ok = is_mixed(Ap, Bp, Cp, Dp)
                    refl = (b == -a and T2 == T + 4 * a) or (b == a and T2 == -T - 4 * a)
                    cnt1[(ok, refl)] += 1
                    if ok and len(ex1) < maxprint: ex1.append((T, a, T2, b, dc, iA, m, Ap, Bp, Cp, Dp))
print("h", h, "s", s, "P", P, "amax", amax)
print("Type I.2 candidates (definition check ok, reflection family):", dict(cnt1))
for x in ex1: print("  I.2", x)
if len(sys.argv) > 4 and sys.argv[4] == "noII": sys.exit(0)
# ---------------- Type II ----------------
dmax = h // (38 * (s // 2) ** 2) + 2
cnt2 = Counter(); ex2 = []
for T in odd_offsets:
    sl = set(slots(T))
    for T2 in odd_offsets:
        sl2 = set(slots(T2))
        for tau in (1, -1):
            eA = 0 if tau == 1 else 1
            for tau2 in (1, -1):
                eB = 0 if tau2 == 1 else 1
                for d in range(-dmax, dmax + 1):
                    eta = 2 * d + tau * T
                    for d2 in range(-dmax, dmax + 1):
                        eta2 = 2 * d2 + tau2 * T2
                        gx = s * (d2 - d); gy = eta2 - eta
                        G = gx * gx + gy * gy
                        if G == 0: continue
                        coef = 4 * (d2 * eta - d * eta2)
                        rhs = (d + d2) * G
                        if coef == 0: continue
                        if rhs % coef: continue
                        U2 = rhs // coef
                        t = U2 - (eB * T2 - eA * T)
                        if t % 2: continue
                        k = t // 2
                        if d != 0:
                            psi = G // 4 - s * s * d * k - U2 * eta
                            den = s * s * P * d
                        else:
                            psi = -G // 4 - s * s * d2 * k - U2 * eta2
                            den = s * s * P * d2
                        if psi % den: continue
                        dc = psi // den
                        if dc == 0: continue
                        for iA in sl:
                            iC = iA + d; iB = iA + k; iD = iB + d2
                            if iC not in sl or iB not in sl2 or iD not in sl2: continue
                            Ap = point(0, T, iA, eA); Cp = point(0, T, iC, 1 - eA)
                            Bp = point(dc, T2, iB, eB); Dp = point(dc, T2, iD, 1 - eB)
                            ok = is_mixed(Ap, Bp, Cp, Dp)
                            cnt2[(ok, d == 0 or d2 == 0, eA, eB)] += 1
                            if ok and len(ex2) < maxprint: ex2.append((T, T2, tau, tau2, d, d2, k, dc, iA, Ap, Bp, Cp, Dp))
print("Type II candidates (ok, three-label, eA, eB):", dict(cnt2))
for x in ex2: print("  II", x)
