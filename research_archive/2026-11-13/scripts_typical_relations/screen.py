
# Screen: for odd T' >0, A(T',Lmax) = { |d| : d != 0, 20d^2+4T'd+T'^2 = L^2, L <= Lmax }.
# delta(A) = max_theta min_a ||theta a||, estimated on a grid, for T' with large |A|.
import sys, math
import numpy as np
from collections import defaultdict
Lmax = int(sys.argv[1]) if len(sys.argv) > 1 else 6000
Tmax = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
top = int(sys.argv[3]) if len(sys.argv) > 3 else 25
S = defaultdict(set)
# triangles x=4|d| (even leg, divisible by 4), y odd, L
for u in range(2, int(math.isqrt(Lmax)) + 2):
    for v in range(1, u):
        if (u - v) % 2 == 0 or math.gcd(u, v) != 1: continue
        H = u*u + v*v
        if H > Lmax: break
        x0, y0 = 2*u*v, u*u - v*v
        g = 1
        while g*H <= Lmax:
            x, y = g*x0, g*y0
            a = x // 4
            for d in (a, -a):
                for yy in (y, -y):
                    T = yy - 2*d
                    if T > 0 and T <= Tmax:
                        S[T].add(abs(d))
            g += 2
items = sorted(S.items(), key=lambda kv: -len(kv[1]))[:top]
for T, A in items:
    A = np.array(sorted(A), dtype=np.int64)
    amax = int(A.max())
    n = min(400000, 40 * amax)
    th = (np.arange(n) + 0.5) / (2*n)  # (0,1/2)
    best = np.ones(n)
    for a in A:
        z = (th * a) % 1.0
        z = np.minimum(z, 1 - z)
        np.minimum(best, z, out=best)
    i = int(best.argmax())
    fac = [p for p in range(2, T+1) if T % p == 0 and all(p % q for q in range(2, int(p**0.5)+1))]
    print(T, fac, 'k=', len(A), 'amax=', amax, 'delta~', round(float(best[i]), 4), 'theta~', round(float(th[i]), 6), flush=True)
