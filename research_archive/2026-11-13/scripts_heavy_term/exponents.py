"""Exponent arithmetic for the heavy-term note (all exponents of log h)."""
from math import log

ln3 = log(3)

def E(a):
    return (1 + 3 ** a) / 2

def phi(x):
    # large-deviation exponent of #{T : 3^{omega_split(T)} >= Lambda^x} / h
    y = x / ln3
    if y <= 0.5:
        return 0.0
    return 0.5 - y + y * log(2 * y)

def rankin(x):
    # min over a > 0 of (a x - (E(a) - 1)); must equal phi(x)
    best = -1e9
    a = 0.0005
    while a < 6:
        best = max(best, a * x - (E(a) - 1))
        a += 0.0005
    return best

def bisect(f, lo, hi, it=200):
    for _ in range(it):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2

# theta* = min_a (E(a)+1)/(1+a)
best = (9, 0)
a = 0.3
while a < 2:
    v = (E(a) + 1) / (1 + a)
    if v < best[0]:
        best = (v, a)
    a += 1e-5
print("theta* = %.5f at a = %.4f" % best)
xs = bisect(lambda x: x - (2 - phi(x)), 1.0, 2.0)
print("root of x = 2 - phi(x): %.5f" % xs)
for x in (1.2, 1.4967, 1.5, 1.75, 2.0):
    print("x=%.4f phi=%.5f rankin=%.5f" % (x, phi(x), rankin(x)))

# Theorem N (old): max(x, 2 - phi(x), 3 - x)
f_old = lambda x: max(x, 2 - phi(x), 3 - x)
f_U = lambda x: max(x, 2 - phi(x), 2 - x)
grid = [1 + i * 1e-5 for i in range(100000)]
print("old board exponent: %.5f" % min(f_old(x) for x in grid))
print("with U (Bad_split Lambda^2/B): %.5f" % min(f_U(x) for x in grid))

# Route L (layers): with Bad_split: E solves 2 - phi(3E - 2) = E ; without: 2 - phi(2E) = E or 1
EL = bisect(lambda e: (2 - phi(3 * e - 2)) - e, 1.0, 1.5)
print("route L with Bad_split: %.5f (x' = %.4f)" % (EL, 3 * EL - 2))
EL0 = bisect(lambda e: (2 - phi(2 * e)) - e, 0.8, 1.5)
print("route L without Bad_split, heavy balance: %.5f; exponent = max(1, that) = %.5f" % (EL0, max(1, EL0)))

# heavy fraction exponent at the optimum
print("heavy fraction exponent -phi(theta*) = %.4f" % (-phi(best[0])))
