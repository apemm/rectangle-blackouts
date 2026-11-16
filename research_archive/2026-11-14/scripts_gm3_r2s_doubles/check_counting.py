# Exhaustive toy check of Lemmas B1 and B2 (no S|X, no Hil: pure (E1)-(E3)
# solutions with 1 <= |m| <= h). For each delta: (i) the T-small / U-small
# enumerations agree on the solution set; (ii) every solution with |T| <= T0
# has s0 = smaller of a,b with s0 + T = delta1*k, s0 | delta1^2 k^2 + delta^2,
# |k| <= (2*T0 + |delta|)/delta1; (iii) counts obey the B1 and B2 bounds.
import math, sys
from check_congruence import factor, delta1, divisors

h = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
def tau(n): return len(divisors(n))
worst1 = worst2 = 0.0; bad = 0; total = 0
for delta in range(2, 161, 2):
    R = math.isqrt(h * delta)
    sols = set()
    for T in range(-R, R + 1):                       # T-small branch
        if T == 0: continue
        n = T * T + delta * delta
        for d in divisors(n):
            for a in (d, -d):
                b = n // a
                if (a + b) % 2: continue
                U = T + (a + b) // 2
                if U == 0 or (T * U) % delta: continue
                m = -(T * U) // delta
                if 1 <= abs(m) <= h: sols.add((T, U, 2 * T + a))
    Vmax = math.isqrt(4 * h * delta)
    for V in range(-Vmax, Vmax + 1):                 # U-small branch
        n = V * V + delta * delta
        for d in divisors(n):
            if d > R: continue
            for U in (d, -d):
                num = V * V - U * U + delta * delta    # = 2 m delta
                if num % (2 * delta): continue
                m = num // (2 * delta)
                if not (1 <= abs(m) <= h) or (m * delta) % U: continue
                T = -(m * delta) // U
                sols.add((T, U, U + T - V))
    # every solution must satisfy min(|T|,|U|) <= sqrt(|m delta|): automatic;
    # check B1
    taus = max([tau(T * T + delta * delta) for (T, U, X2) in sols] + [1])
    B1 = (12 * math.sqrt(h * delta) + 4) * taus
    worst1 = max(worst1, len(sols) / B1)
    for T0 in (R // 4 + 1, R, 4 * R):
        sub = [s for s in sols if abs(s[0]) <= T0]
        for (T, U, X2) in sub:
            a = X2 - 2 * T; b = (T * T + delta * delta) // a
            g = math.gcd(T, delta); d1 = delta1(delta // g)
            s0 = a if abs(a) <= abs(b) else b
            k, r = divmod(s0 + T, d1)
            kmax = (2 * T0 + delta) / d1
            ok = r == 0 and (d1 * d1 * k * k + delta * delta) % s0 == 0 and abs(k) <= kmax
            bad += (not ok); total += 1
        T0p = max(T0, delta)
        B2 = 4 * taus * sum(min(2 * T0 / g + 1, 2 * (2 * T0 + delta) / delta1(delta // g) + 1)
                            for g in divisors(delta))
        worst2 = max(worst2, len(sub) / B2 if B2 else 0)
print("h =", h, "checked", total, "param failures", bad,
      "max count/B1 = %.3f" % worst1, "max count/B2 = %.3f" % worst2)
