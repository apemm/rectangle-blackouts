import sys
from math import log, isqrt
from common import all_D
def divisors(n):
    n = abs(n); s = [g for g in range(1, isqrt(n) + 1) if n % g == 0]
    return sorted(set(s + [n // g for g in s]))
for h in [int(a) for a in sys.argv[1:]]:
    D = all_D(h)
    E = Ems = 0.0; changed = 0; sk = 0
    for T, d in D.items():
        k = len(d); sk += k
        e = max(1.0, k / log(h))
        m = e
        for q in divisors(T):
            if q == 1 or q >= h / 3: continue
            Kq = sum(1 for x in d if x % q == 0)
            m = max(m, Kq / log(h / q))
        E += e; Ems += m; changed += (m > e)
    print("h", h, "diagonals", len(D), "sum k", sk, "sum max(1,k/ln h) %.0f" % E,
          "sum multiscale %.0f" % Ems, "ratio to h: %.3f %.3f" % (E / h, Ems / h), "T where max is at q>1:", changed)
