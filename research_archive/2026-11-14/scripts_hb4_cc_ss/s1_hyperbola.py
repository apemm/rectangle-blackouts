# Sanity check of the hyperbola lemma:
# if xy = N has >= 3 lattice points with x in a window of w consecutive
# integers and y in a window of w consecutive integers, then |N| <= (w-1)^6/16.
# Also checks the exact area identity (2*Area)^2 = |Px*Py|/|N|.
# Exhaustive over 1 <= N <= NMAX, positive branch (negative is symmetric).
import sys, time
from fractions import Fraction
t0 = time.time()
NMAX = 40000
W = [2, 3, 4, 5, 6, 7]
# divisor lists by sieve
divs = [[] for _ in range(NMAX + 1)]
for d in range(1, NMAX + 1):
    for k in range(d, NMAX + 1, d):
        divs[k].append(d)
maxN = {w: 0 for w in W}
ident_fail = 0
checked_triples = 0
for N in range(1, NMAX + 1):
    ds = divs[N]
    L = len(ds)
    for w in W:
        # max number of divisors x in a window of w consecutive ints with N/x in a window of w
        i = 0
        best = 0
        for a in range(L):
            # divisors in [ds[a], ds[a]+w-1]
            pts = [x for x in ds[a:a + w] if x <= ds[a] + w - 1]
            # cofactors decreasing; need spread <= w-1 for some subset of size 3
            ys = [N // x for x in pts]
            # largest subset with x-spread<=w-1 (true) and y-spread<=w-1: sliding over pts (ys decreasing)
            for s in range(len(pts)):
                for e in range(s, len(pts)):
                    if ys[s] - ys[e] <= w - 1:
                        best = max(best, e - s + 1)
        if best >= 3:
            maxN[w] = max(maxN[w], N)
    # identity check on first few triples of divisors
    if N <= 3000 and L >= 3:
        for a in range(min(L - 2, 4)):
            x1, x2, x3 = ds[a], ds[a + 1], ds[a + 2]
            y1, y2, y3 = N // x1, N // x2, N // x3
            area2 = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
            Px = (x2 - x1) * (x3 - x1) * (x3 - x2)
            Py = (y1 - y2) * (y1 - y3) * (y2 - y3)
            checked_triples += 1
            if Fraction(area2 * area2) != Fraction(abs(Px * Py), N):
                ident_fail += 1
print("NMAX", NMAX)
for w in W:
    print("w=%d  largest N with >=3 points: %d   bound (w-1)^6/16 = %.1f" % (w, maxN[w], (w - 1) ** 6 / 16))
print("identity checks", checked_triples, "failures", ident_fail)
print("time %.1f s" % (time.time() - t0))
