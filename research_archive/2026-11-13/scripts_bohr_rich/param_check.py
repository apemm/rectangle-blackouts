# Check: S_T(h) = { g x y / 2 : g>=1, y>=1, x!=0, gcd(x,y)=1, gxy even,
#   g (y^2 - x y - x^2) = T, g (x^2+y^2) < h }, bijectively, L = g(x^2+y^2).
import sys
from math import gcd, isqrt
from collections import defaultdict

def brute(h):
    S = defaultdict(set)
    for T in [t for t in range(-(h-1), h) if t % 2]:
        # 20 d^2 + 4 T d + T^2 = L^2 < h^2  => |d| small
        dmax = h  # 20 d^2 - 4|T||d| <= h^2 crude bound
        for d in range(-dmax, dmax+1):
            if d == 0: continue
            Q = 20*d*d + 4*T*d + T*T
            L = isqrt(Q)
            if L*L == Q and 0 < L < h:
                S[T].add((d, L))
    return S

def param(h):
    S = defaultdict(list)
    for y in range(1, isqrt(h)+2):
        for x in range(-isqrt(h)-1, isqrt(h)+2):
            if x == 0 or gcd(abs(x), y) != 1: continue
            r = x*x + y*y
            if r >= h: continue
            N = y*y - x*y - x*x
            for g in range(1, (h-1)//r + 1):
                if (g*x*y) % 2: continue
                T = g*N
                if T % 2 == 0 or abs(T) >= h: continue
                S[T].append((g*x*y//2, g*r))
    return S

h = int(sys.argv[1]) if len(sys.argv) > 1 else 120
B = brute(h); P = param(h)
bad = 0
for T in set(B) | set(P):
    lp = P.get(T, [])
    if len(lp) != len(set(lp)) or set(lp) != B.get(T, set()):
        bad += 1
        if bad < 5: print("mismatch", T, sorted(B.get(T, set())), sorted(lp))
print("h", h, "offsets", len(B), "total", sum(len(v) for v in B.values()), "mismatches", bad)
# min distance check |d| >= sqrt(|T|/12)
viol = [(T, d) for T in B for (d, L) in B[T] if 12*d*d < abs(T)]
print("min-distance violations", len(viol))
