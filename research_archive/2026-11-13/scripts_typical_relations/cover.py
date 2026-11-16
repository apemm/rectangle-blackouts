
# For given odd T' and Lmax: A = { |d| : d != 0, Q(T',d) = L^2, L <= Lmax } found by direct search over d.
# delta(A) by bisection on a float interval-cover test; then exact certificate that A is
# delta1-covering (delta1 = rational just above) using integer arithmetic.
import sys, math
import numpy as np
from fractions import Fraction

def Aset(T, Lmax):
    A = set(); Ls = {}
    dmax = Lmax // 4 + 1
    for d in range(-dmax, dmax + 1):
        if d == 0: continue
        q = 20*d*d + 4*T*d + T*T
        L = math.isqrt(q)
        if L*L == q and L <= Lmax:
            A.add(abs(d)); Ls[abs(d)] = max(Ls.get(abs(d), 0), L)
    return sorted(A), Ls

def covers_float(A, dl):
    lefts = []; rights = []
    for a in A:
        j = np.arange(0, a // 2 + 2)
        lefts.append((j - dl) / a); rights.append((j + dl) / a)
    l = np.concatenate(lefts); r = np.concatenate(rights)
    keep = l < 0.5
    l = l[keep]; r = r[keep]
    o = np.argsort(l); l = l[o]; r = r[o]
    cm = np.maximum.accumulate(r)
    ok = np.all(l[1:] < cm[:-1] - 1e-13) and l[0] < 0 and cm[-1] > 0.5
    return bool(ok)

def covers_exact(A, P, Q):
    # intervals ((Qj-P)/(Qa), (Qj+P)/(Qa)) on [0,1/2]; check open cover of [0,1/2]
    iv = []
    for a in A:
        for j in range(0, a // 2 + 2):
            iv.append((Fraction(Q*j - P, Q*a), Fraction(Q*j + P, Q*a)))
    iv.sort()
    if not iv[0][0] < 0: return False
    reach = iv[0][1]
    for lo, hi in iv[1:]:
        if reach > Fraction(1, 2): return True
        if not lo < reach: return False
        if hi > reach: reach = hi
    return reach > Fraction(1, 2)

T = int(sys.argv[1]); Lmax = int(sys.argv[2]); exact = len(sys.argv) > 3
A, Ls = Aset(T, Lmax)
lo, hi = 0.0, 0.2
for _ in range(int(sys.argv[4]) if len(sys.argv) > 4 else 30):
    mid = (lo + hi) / 2
    if covers_float(A, mid): hi = mid
    else: lo = mid
print('T', T, 'Lmax', Lmax, 'k', len(A), 'amax', max(A), 'Lused', max(Ls.values()), 'delta(A) in', (round(lo, 6), round(hi, 6)), flush=True)
if exact:
    Q = 10000; P = math.ceil(hi * Q) + 1
    print('exact cover at', Fraction(P, Q), covers_exact(A, P, Q), flush=True)
    print('A =', A)
