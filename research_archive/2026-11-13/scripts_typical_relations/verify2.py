# Independent sanity check: rebuild A from the definition by a different loop (over L), test random theta.
import math, sys, numpy as np
T = int(sys.argv[1]); Lmax = int(sys.argv[2]); bound = float(sys.argv[3])
A = set()
for L in range(1, Lmax + 1):
    X2 = 5*L*L - 4*T*T          # X = 10d + T, X^2 = 5L^2 - 4T^2
    if X2 < 0: continue
    X = math.isqrt(X2)
    if X*X != X2: continue
    for XX in (X, -X):
        if (XX - T) % 10 == 0 and XX != T:
            A.add(abs((XX - T)//10))
A = sorted(A)
print('k', len(A), 'amax', A[-1])
rng = np.random.default_rng(7); best = 0.0
for _ in range(10):
    th = rng.random(400000); b = np.ones_like(th)
    for a in A:
        z = (th*a) % 1.0; np.minimum(b, np.minimum(z, 1-z), out=b)
    best = max(best, float(b.max()))
print('max over 4e6 random theta of min ||theta a|| =', best, '< bound', best < bound)
