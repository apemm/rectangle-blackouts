# Brute force over rows: for each delta and each m with 1 <= |m| <= h, all
# signed factorizations g1*g2 = N = delta(2m - delta) (Theorem A), keep those
# with U = (g2-g1)/2 != 0 dividing m*delta. Compare with the union of the
# T-small and U-small branches (min(|T|,|U|) <= sqrt(|m delta|)).
import math
from check_congruence import divisors
h = 600; miss = 0; tot = 0
for delta in range(2, 61, 2):
    brute = set()
    for m in list(range(-h, 0)) + list(range(1, h + 1)):
        N = delta * (2 * m - delta)
        if N == 0: continue
        for d in divisors(abs(N)):
            for g1 in (d, -d):
                g2 = N // g1
                if (g2 - g1) % 2: continue
                U = (g2 - g1) // 2
                if U == 0 or (m * delta) % U: continue
                T = -(m * delta) // U; V = (g1 + g2) // 2
                brute.add((T, U, U + T - V))
    for (T, U, X2) in brute:
        tot += 1
        m = -(T * U) // delta
        miss += not (min(abs(T), abs(U)) <= math.isqrt(abs(m * delta)))
print("brute solutions", tot, "outside both branches", miss)
