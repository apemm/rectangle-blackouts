"""Sanity check of the R2s algebra (no design, small integers).
Enumerate delta, m, signed factorizations g1*g2 = N = delta*(2m - delta);
U = (g2-g1)/2, V = (g1+g2)/2, T = -m*delta/U, X = (U+T-V)/2.
Check against the defining equations of a mixed quadruple
A=(0,y), B=(U, y+m), C=(X, y+delta), D=(X+V, y+m):
 |B-A|^2 = |D-C|^2 and (B-A).(C+D-A-B) = 0,
and the derived identities
 E4: 4 e1 (X-T) = T^2 + delta^2,   e1 = U - X
 E5: 4 e2 X = T^2 + delta^2 - 4 m delta,  e2 = e1 + T
 E6: 4 e1 U = (T + 2 e1)^2 + delta^2.
Then, among solutions with delta^2 < 2|X| and |X| >= X0, check the regime
inequalities: (c) |e1| <= |X|/2  =>  |X| (1 - 2/sqrt(2|X|)) < 2|m|;
(s) |e1| > |X|/2, |U| > |X|/2 => X^2 < 4|m delta|; (n) otherwise |T| > |X|/2.
Also check the converse: every integer (U,V,X) solving the two equations
arises this way (brute force over a box for small parameters).
"""
import math, itertools
def divisors(n):
    n = abs(n); out = set()
    for d in range(1, math.isqrt(n) + 1):
        if n % d == 0: out |= {d, n // d}
    return out
nsol = 0; bad = 0; reg = {'c': 0, 's': 0, 'n': 0}; regbad = 0
X0 = 40
for delta in range(-60, 61, 2):
    if delta == 0: continue
    for m in range(-300, 301):
        if m == 0: continue
        N = delta * (2 * m - delta)
        if N == 0: continue
        for g in divisors(N):
            for g1 in (g, -g):
                g2 = N // g1
                if (g1 - g2) % 2: continue
                U = (g2 - g1) // 2; V = (g1 + g2) // 2
                if U == 0 or V == 0: continue
                if (m * delta) % U: continue
                T = -(m * delta) // U
                if (U + T - V) % 2: continue
                X = (U + T - V) // 2
                if X == 0: continue
                # defining equations
                ok = (U*U + m*m == V*V + (m - delta)**2) and \
                     (U * (2*X + V - U) + m * delta == 0)
                e1 = U - X; e2 = e1 + T
                ok = ok and 4*e1*(X - T) == T*T + delta*delta
                ok = ok and 4*e2*X == T*T + delta*delta - 4*m*delta
                ok = ok and 4*e1*U == (T + 2*e1)**2 + delta*delta
                nsol += 1
                if not ok: bad += 1
                if delta*delta < 2*abs(X) and abs(X) >= X0:
                    if 2*abs(e1) <= abs(X):
                        reg['c'] += 1
                        if not abs(X)*(1 - 2/math.sqrt(2*abs(X))) < 2*abs(m): regbad += 1
                    elif 2*abs(U) > abs(X):
                        reg['s'] += 1
                        if not X*X < 4*abs(m*delta): regbad += 1
                    else:
                        reg['n'] += 1
                        if not 2*abs(T) > abs(X): regbad += 1
                        if not abs(U) * abs(X) < 2 * abs(m * delta): regbad += 1
                        if m * delta < 0:
                            reg['n-'] = reg.get('n-', 0) + 1
                            if not X * X < 2 * abs(m * delta): regbad += 1
print('solutions', nsol, 'identity failures', bad)
print('Hilbert-type solutions by regime', reg, 'regime-bound failures', regbad)
# converse on a box: all (U,V,X) with the two equations
cnt = 0; miss = 0
for delta in range(-12, 13, 2):
    if delta == 0: continue
    for m in range(-25, 26):
        if m == 0 or 2*m == delta: continue
        sols = set()
        N = delta * (2*m - delta)
        for g in divisors(N):
            for g1 in (g, -g):
                g2 = N // g1
                if (g1 - g2) % 2: continue
                U = (g2-g1)//2; V = (g1+g2)//2
                if U == 0 or (m*delta) % U: continue
                T = -(m*delta)//U
                if (U+T-V) % 2: continue
                sols.add((U, V, (U+T-V)//2))
        for U in range(-80, 81):
            if U == 0: continue
            for V in range(-80, 81):
                if U*U + m*m != V*V + (m-delta)**2: continue
                # (2X + V - U) U = -m delta
                if (m*delta) % U: continue
                t = -(m*delta)//U
                if (t - V + U) % 2: continue
                X = (t - V + U)//2
                cnt += 1
                if (U, V, X) not in sols: miss += 1
print('box solutions', cnt, 'not produced by the parametrization', miss)
