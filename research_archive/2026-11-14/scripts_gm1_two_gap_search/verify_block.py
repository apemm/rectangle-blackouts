"""Independent check of the block-linear theorem for even a (no import of tg.py).
For a even, b>=0, s in {1,2}: g = a if floor(b/a) % 3 != 1 else a//2;
c = s*(floor(b/g)+2) mod 3;  xi_r = (c*floor(r/g)) mod 3.
Checks, for r over one full period 3g and also r in [-3g, 0):
  xi[r+a] != xi[r];  xi[r+b]-xi[r] != s (if b>=1);  xi[r+b+1]-xi[r] != s-3.
"""
import sys, numpy as np
AMAX, BMAX = int(sys.argv[1]), int(sys.argv[2])
bad = 0; n = 0
for a in range(2, AMAX + 1, 2):
    for b in range(0, BMAX + 1):
        for s in (1, 2):
            g = a if (b // a) % 3 != 1 else a // 2
            c = (s * ((b // g) + 2)) % 3
            assert c in (1, 2)
            r = np.arange(-3 * g, 3 * g)
            X = lambda t: (c * np.floor_divide(t, g)) % 3
            x0 = X(r)
            ok = not np.any(X(r + a) == x0)
            if b >= 1: ok &= not np.any(X(r + b) - x0 == s)
            ok &= not np.any(X(r + b + 1) - x0 == s - 3)
            n += 1
            if not ok:
                bad += 1
                if bad < 10: print("FAIL", a, b, s, g, c)
print("checked", n, "failures", bad)
