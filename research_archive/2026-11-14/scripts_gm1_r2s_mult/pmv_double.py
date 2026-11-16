"""Search for +-V doubles on one R2s curve, sea row F: solutions (U, V) and (U, -V) with S | V,
so both X and X + V are multiples of S and lie in one window (|v| <= 2(M-1)).
Here delta > 0 (N < 0).  With R = S^2 v^2 + delta^2, U = R / j, T = (U - j)/2, X = (U - V + T)/2.
Prints (role, m, delta, U, V, X/S, X'/S)."""
from sympy import divisors
S = 6272
found = []
for v in range(1, 5):
    for k in range(1, 41):
        delta = 196 * k
        R = S * S * v * v + delta * delta
        for j0 in divisors(R):
            for j in (j0, -j0):
                U = R // j
                if abs(U) * abs(U) <= R: continue      # need U^2 > R so that K < 0 (m < 0)
                if (U - j) % 4: continue                # T = (U - j)/2 even
                T = (U - j) // 2
                K = R - U * U                            # = 2 m delta
                if K % (2 * delta): continue
                m = K // (2 * delta)
                if m > -100000: continue
                if U % 7: continue
                for V in (S * v, -S * v):
                    assert V * V - U * U == delta * (2 * m - delta)
                    assert T * U == -m * delta
                    x2 = U - V + T
                    if x2 % 2: continue
                    X = x2 // 2
                    Xp = X + V
                    if X % S or Xp % S: continue
                    if X * Xp <= 0: continue
                    if 2 * min(abs(X), abs(Xp)) <= delta * delta: continue
                    if U - X == 0 or U - X + T == 0 or U - Xp == 0 or U - Xp + T == 0: continue
                    rl = 'odd' if m % 28 == 10 else ('even' if m % 2 and m % 7 in (3, 5) else None)
                    if rl is None: continue
                    found.append((rl, m, delta, U, V, X // S, Xp // S, j))
found = sorted(set(found), key=lambda t: abs(t[1]))
print(len(found))
for f in found[:25]: print(f)
