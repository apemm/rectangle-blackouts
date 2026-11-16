# Generate in-class Fo/Fo candidates from the general-stride parametrization
#   alpha1 = t(m^2+1)/(2m-r), P = 2tm, alpha2 = alpha1 - P, Y1 = (m-r) alpha1, r = mu (nu=1)
# then verify each with the raw mixed-pair equations, and tabulate 2-adic types.
# Row rule: Y1 = 8(w+c) mod 64 (c in {1,3}), w = A mod 4 (SAW*-type, offsets mod 4).
import sys
from fractions import Fraction as Fr
from math import gcd
from collections import Counter

def v2(x):
    if x == 0: return 99
    k = 0
    while x % 2 == 0: x //= 2; k += 1
    return k

def raw_ok(mu, t, A, A2, Y1):
    Dx, Dy = mu*t, 2*t
    U = (4*A, Y1); V = (4*A2, Y1 - Dy)
    Sx, Sy = 2*Dx + V[0] - U[0], 2*Dy + V[1] - U[1]
    if Sx % 2 or Sy % 2: return False
    n = (Sx//2, Sy//2)
    if n == (0, 0): return False
    if n[0]*U[0] + n[1]*U[1] != 0: return False
    if U[0]**2 + U[1]**2 != V[0]**2 + V[1]**2: return False
    if V == U or V == (-U[0], -U[1]): return False
    return True

def run(mu, AB, KT):
    r = mu
    out = Counter(); ex = {}
    for b in range(1, AB+1):
        for a in range(-AB*r, AB*r+1):
            if gcd(a, b) != 1: continue
            m = Fr(a, b)
            if 2*m - r == 0 or m - r == 0: continue
            for k in range(1, KT+1):
                t = -32*k
                al1 = Fr(t)*(m*m+1)/(2*m - r)
                if al1.denominator != 1 or al1.numerator % 4: continue
                P = 2*t*m
                if P.denominator != 1: continue
                al2 = al1 - P
                if al2.denominator != 1 or al2.numerator % 4: continue
                Y1 = (m - r)*al1
                if Y1.denominator != 1 or Y1 <= 0: continue
                A = al1.numerator//4; A2 = al2.numerator//4; Y1 = Y1.numerator
                w = A % 4
                if ((mu//4)*t + A2 - A) % 4: continue
                if Y1 % 64 not in ((8*(w+1)) % 64, (8*(w+3)) % 64): continue
                if not raw_ok(mu, t, A, A2, Y1):
                    print("RAW FAIL", mu, a, b, t); continue
                key = (w, a % 2, min(v2(b), 9), min(v2(a), 9), v2(A) - v2(b), v2(t))
                out[key] += 1
                ex.setdefault(key, (a, b, t, A, Y1))
    return out, ex

AB = int(sys.argv[1]); KT = int(sys.argv[2])
for mu in (4, 8):
    out, ex = run(mu, AB, KT)
    print("stride (%d,1): verified solutions %d" % (mu, sum(out.values())))
    for k in sorted(out):
        print("  (w, a mod 2, v2 b, v2 a, v2A-v2b, v2 t) =", k, out[k], " e.g. (a,b,t,A,Y1) =", ex[k])
