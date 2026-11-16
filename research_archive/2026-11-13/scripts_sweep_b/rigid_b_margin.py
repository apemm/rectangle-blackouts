# Sanity check for rigid_layout_cross_block Theorem 2 under v3 spacing.
# Configuration: T0 odd, 1 <= |T0| <= h-1; g | T0, t' with gcd(t', T0/g) = 1, t1 = g t';
# b = 10t' - T' (T' = T0/g); q != 0 with |c2| = 8|q||t'| <= K-1 and |N| = |q||b| >= minN.
# Old spacing |DM| >= 20h+1 gives minN = 19h+3; v3 spacing |DM| >= p > 40h gives minN = 39h+3.
# Report max |b|/(h-1) and min |q| over admissible configurations.
import math

def divisors(n):
    out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
        d += 1
    return out

def scan(h, minN):
    K = h // 2
    tmax = (K - 1) // 8
    best_b, min_q = 0.0, None
    for T0 in range(-(h - 1), h, 2):
        for g in divisors(abs(T0)):
            Tp = T0 // g
            for tp in range(-tmax, tmax + 1):
                if tp == 0 or math.gcd(abs(tp), abs(Tp)) != 1:
                    continue
                b = 10 * tp - Tp
                qmax = (K - 1) // (8 * abs(tp))
                if qmax * abs(b) < minN:
                    continue
                qmin = -(-minN // abs(b))
                best_b = max(best_b, abs(b) / (h - 1))
                min_q = qmin if min_q is None else min(min_q, qmin)
    return best_b, min_q

for h in (801, 1601):
    old = scan(h, 19 * h + 3)
    new = scan(h, 39 * h + 3)
    print(h, "old: max|b|/(h-1)=%.4f min|q|=%s" % old, "| v3: max|b|/(h-1)=%.4f min|q|=%s" % new)
print("bounds 1+10/294=%.4f 1+10/614=%.4f" % (1 + 10 / 294, 1 + 10 / 614))
