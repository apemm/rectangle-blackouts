"""Check the explicit rule of the even-a proof on a long rank interval, for every
a <= 40 even, b <= 120, s in {1,2}, every phase phi < 2g and offset kappa:
  w = v3(a), g = 3^w if floor(b/3^w) != 1 mod 3 else 2*3^w, n = floor(b/g),
  c = 3-s if n = 0 mod 3, c = s if n = 2 mod 3,  xi_r = (c*floor((r+phi)/g) + kappa) mod 3.
Also check: the 4-rank set {0,1,2,3} with gaps {3,6,9} at M=3 has no solution."""
import itertools
from lists import slots

def v3(n):
    k = 0
    while n % 3 == 0:
        n //= 3; k += 1
    return k

R = range(-150, 400)
bad = 0; systems = 0; checked = 0
for a in range(2, 41, 2):
    w = v3(a)
    for b in range(0, 121):
        for s in (1, 2):
            g = 3 ** w if (b // 3 ** w) % 3 != 1 else 2 * 3 ** w
            assert a % g == 0 and (a // g) % 3 != 0
            n = b // g
            assert n % 3 != 1
            c = 3 - s if n % 3 == 0 else s
            for phi in range(2 * g):
                for kap in range(3):
                    xi = {r: (c * ((r + phi) // g) + kap) % 3 for r in R}
                    systems += 1
                    for q in (3 * a, 3 * b + s):
                        for d, de in slots(q, 3):
                            for r in R:
                                if r + d in xi:
                                    checked += 1
                                    if xi[r + d] - xi[r] == de:
                                        bad += 1
print("rule instances", systems, "constraints", checked, "violations", bad)

ok = False
for x in itertools.product(range(3), repeat=4):
    if all(x[i] != x[j] for i in range(4) for j in range(i + 1, 4)):
        ok = True
print("gaps {3,6,9} on ranks 0..3 solvable at M=3:", ok)
