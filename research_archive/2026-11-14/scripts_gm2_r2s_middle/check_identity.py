"""Checks for the two-solution identity of one R2s curve (sanity only).
For a solution g (= V-U) of the curve with N = delta(2m-delta), K = N + delta^2:
  D = N/g - g = 2U,  X = -(g + K/D)/2.
Identity: with u = g2-g1, J = X1-X2, r = N/(g1 g2), L = u^2 - 2uJ - delta^2,
  Q(r) = u(2r^2 - r + 1) - 2J(r-1)^2,   N Q(r) = u r (L r - delta^2).
"""
import sympy as sp, random
g1,g2,N,dl,r0,u = sp.symbols('g1 g2 N delta r0 u')
K = N + dl**2
X = lambda g: -(g + K/(N/g - g))/2
J = sp.simplify(X(g1) - X(g2)); uu = g2 - g1; r = N/(g1*g2)
L = uu**2 - 2*uu*J - dl**2
Q = uu*(2*r**2 - r + 1) - 2*J*(r-1)**2
print('identity N Q(r) - u r (L r - delta^2) == 0 :', sp.simplify(N*Q - uu*r*(L*r - dl**2)) == 0)
# Theorem A cross-check: X equals (U+T-V)/2 with U=(g2'-g)/2, V=(g+g2')/2, T=-K/(2U)
g = sp.symbols('g'); h = N/g; U=(h-g)/2; V=(g+h)/2; T=-K/(2*U)
print('X formula matches Theorem A:', sp.simplify((U+T-V)/2 - X(g)) == 0)
# Theorem P algebra: Q(r0)=0 and L r0 = delta^2 imply delta^2 (r0-1)^2 = -u^2 r0^2 unless r0 = -1
Jsym = sp.symbols('J')
Qr = u*(2*r0**2 - r0 + 1) - 2*Jsym*(r0-1)**2
Lr = (u**2 - 2*u*Jsym - dl**2)*r0 - dl**2
Jsol = sp.solve(Qr, Jsym)[0]
print('L r0 - delta^2 at Q(r0)=0, factored:', sp.factor(Lr.subs(Jsym, Jsol)))
# numeric: random two factorizations of one N with integer X's (no S|X), check identity numerically
random.seed(1); hits = 0
for trial in range(4000):
    d0 = 28*random.randint(1, 40) * random.choice([1,-1]); m = random.randint(10**5, 10**7) * random.choice([1,-1])
    NN = d0*(2*m - d0); KK = NN + d0*d0
    sols = []
    for gg in sp.divisors(abs(NN)):
        for s in (gg, -gg):
            D = NN//s - s
            if D != 0 and KK % D == 0 and (s + KK//D) % 2 == 0: sols.append((s, -(s + KK//D)//2))
    if len(sols) >= 2:
        (a1,x1),(a2,x2) = sols[0], sols[-1]
        if a1*a2 == 0 or a1 == a2: continue
        uv = a2-a1; Jv = x1-x2; rv = sp.Rational(NN, a1*a2); Lv = uv**2 - 2*uv*Jv - d0*d0
        Qv = uv*(2*rv**2 - rv + 1) - 2*Jv*(rv-1)**2
        assert NN*Qv == uv*rv*(Lv*rv - d0*d0); hits += 1
    if hits >= 200: break
print('numeric identity checks passed on', hits, 'curves with two integer-X factorizations')
