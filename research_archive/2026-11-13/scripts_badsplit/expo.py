# Exponent optimisation for Route L and Proposition 5, with and without truncation.
from math import log
LN3 = log(3)
def phi(xi):
    y = xi/LN3
    if y < 0.5: return 0.0   # below Rankin range the heavy count is ~ h (phi=0 bound used conservatively)
    return 0.5 - y + y*log(2*y)

def bisect(f, lo, hi):
    for _ in range(50):
        mid = (lo+hi)/2
        if f(mid) > 0: lo = mid
        else: hi = mid
    return (lo+hi)/2

# Route L original: b0 = 2-E, q = 2E-2, b1 = E, need 2 - phi(q+b1) = E.
E0 = bisect(lambda E: (2 - phi(3*E - 2)) - E, 1.0, 1.5)
print("Route L original:", E0)
# Route L truncated: terms max(b0, b1, 2y/3, q+b0, q+2y/3, 1), 2-phi(q+b1), 2-b0-y/3.
# optimum: 2y/3 = b0, b0 + y/3 = 2 - E -> b0 = (2-E)/1.5 ; q = E - b0 ; b1 = E.
E1 = bisect(lambda E: (2 - phi(2*E - (2-E)/1.5)) - E, 1.0, 1.5)
b0 = (2-E1)/1.5; print("Route L truncated:", E1, " b0 =", b0, " y =", 1.5*b0, " q =", E1-b0, " b1 =", E1)
# brute-force grid check of the truncated optimum
best = (9, None)
import itertools
st = 0.01
for q in [i*0.03 for i in range(0, 41)]:
    for b0 in [i*0.03 for i in range(0, 41)]:
        for y in [i*0.05 for i in range(0, 41)]:
            b1 = None
            # choose b1 minimal s.t. heavy term <= current candidate: scan
            rest = max(b0, 2*y/3, q+b0, q+2*y/3, 1, 2-b0-y/3)
            # heavy: 2 - phi(q+b1) decreasing in b1; b1 itself in max
            lo, hi = 0.0, 3.0
            # minimise max(b1, 2-phi(q+b1)) over b1
            b1 = bisect(lambda b: (2 - phi(q+b)) - b, 0.0, 3.0)
            val = max(rest, b1, 2 - phi(q+b1))
            if val < best[0]: best = (val, (q, b0, y, b1))
print("grid optimum Route L truncated:", best)
# Prop 5 truncated: max(k, 2y/3, 2 - y/3 - k)
best5 = min((max(k, 2*y/3, 2 - y/3 - k), k, y) for k in [i*0.002 for i in range(0, 1001)] for y in [j*0.004 for j in range(0, 1001)])
print("Prop 5 truncated optimum:", best5)
