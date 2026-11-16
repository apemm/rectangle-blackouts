"""Count admissible (g, t', q) for a vertex class of offset T0 (stride 4, P = 20h).
Admissible: g | T0, t' != 0, gcd(t', T0/g) = 1, b = 10t' - T0/g,
P - h + 2 <= |q b|, 8|q t'| <= K - 1.
Heuristic expected fatal configurations per label in a random block order:
rho^3 * count / P (one class per block position, diagonal uniform).
"""
import sys
from math import gcd, log

def divisors(n):
    n = abs(n); out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n: out.append(n // d)
        d += 1
    return out

def count(T0, h):
    K = h // 2; P = 20 * h
    tot = 0
    for g in divisors(T0):
        Tp = T0 // g
        a = 1
        while 8 * a <= K - 1:
            for tp in (a, -a):
                if gcd(a, abs(Tp)) != 1: continue
                b = abs(10 * tp - Tp)
                qmax = (K - 1) // (8 * a)
                qmin = -(-(P - h + 2) // b)
                if qmax >= qmin:
                    tot += 2 * (qmax - qmin + 1)
            a += 1
    return tot

h = int(sys.argv[1])
P = 20 * h
for T0 in [int(x) for x in sys.argv[2:]]:
    c = count(T0, h)
    tau = len(divisors(T0))
    print("T0", T0, "tau", tau, "count", c, "count/P", round(c / P, 4),
          "tau ln h/320", round(tau * log(h) / 320, 4), "tau ln(T0/294)/80", round(tau * log(T0 / 294) / 80, 4))
