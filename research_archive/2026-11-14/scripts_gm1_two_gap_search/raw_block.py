"""Raw slot-rule check of both versions of the even-a construction.
Version H: h = 3^{v_3(a)}, g = 2h if floor(b/2h) % 3 != 1 else h.   Version A: h = a/2 (same rule with 2h = a).
xi_r = c*floor(r/g) mod 3, c = s*(floor(b/g)+2) mod 3.  Forbidden: 3(u-r) + xi_u - xi_r in {3a, 3b+s} for u>r."""
import sys
def v3(n):
    k = 0
    while n % 3 == 0: n //= 3; k += 1
    return k
AMAX, BMAX = int(sys.argv[1]), int(sys.argv[2])
n = bad = 0
for a in range(2, AMAX + 1, 2):
    for b in range(0, BMAX + 1):
        for s in (1, 2):
            Q = {3 * a, 3 * b + s}
            for h in (3 ** v3(a), a // 2):
                g = 2 * h if (b // (2 * h)) % 3 != 1 else h
                c = (s * (b // g + 2)) % 3
                xi = [(c * (r // g)) % 3 for r in range(3 * g + max(a, b + 1) + 2)]
                ok = all(3 * d + xi[r + d] - xi[r] not in Q
                         for r in range(3 * g) for d in (a, b, b + 1) if d >= 1)
                n += 1
                if not ok: bad += 1; print("BAD", a, b, s, h, g, c)
print("checked", n, "bad", bad)
