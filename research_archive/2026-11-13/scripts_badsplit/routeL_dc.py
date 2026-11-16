from math import log
L3 = log(3)
def phi(x):
    y = x / L3
    return 0.5 - y + y*log(2*y)
# largest d with 2 - phi(2 - d) <= 1, i.e. phi(2-d) >= 1
lo, hi = 0.0, 0.2
for _ in range(100):
    mid = (lo+hi)/2
    if phi(2-mid) >= 1: lo = mid
    else: hi = mid
print("d0 =", lo, " phi(2) =", phi(2.0))
# Route L with degree cap: extra colours Lambda^d per piece, Bad cost Lambda^(2-k d); E(d) for given d
def E_of(d):
    lo, hi = 1.0, 1.6
    for _ in range(100):
        E = (lo+hi)/2
        ok = (2 - phi(2*E - d)) <= E
        if ok: hi = E
        else: lo = E
    return max(1.0, hi)
for k in (1, 2, 3, 5, 10, 40, 73):
    # need 2 - k d <= E and minimise; scan d
    best = min((max(E_of(d), 2 - k*d), d) for d in [i/4000 for i in range(1, 4001)])
    print("k =", k, " Route L exponent =", round(best[0], 5), " at d =", best[1])
