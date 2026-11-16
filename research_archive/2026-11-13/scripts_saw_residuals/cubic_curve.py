"""Plane cubic of the two-label Fo/Fo (and Fe/Fe) quadruples with both fillers in one row (homogeneous case).
Side A = L1, B = F1; diagonal C = L2, D = F2; L on the class line (2a, a) in (n, Y) units, F in one row (Y = 0).
U = F1 - L1 = (x1, u), V = F2 - L2 = (x2, v), u, v = depths of L1, L2 below the filler row, d = a2 - a1 = u - v.
Conditions |U| = |V| and |U - V|^2 = 4 d (2 x1 + u). With p = x1 - x2 and q = x1 + x2 = (v^2 - u^2)/p:
F(p, u, v) = p^3 - 4 d p^2 + (d^2 - 4 d u) p + 4 d^2 (u + v) = 0."""
import sympy as sp
from math import gcd
p, u, v = sp.symbols('p u v')
d = u - v
F = sp.expand(p**3 - 4*d*p**2 + (d**2 - 4*d*u)*p + 4*d**2*(u + v))
print('F =', F)
# singular points in P^2
eqs = [sp.diff(F, w) for w in (p, u, v)]
print('singular points (affine charts):')
for chart, sub in (('v=1', {v: 1}), ('u=1', {u: 1}), ('p=1', {p: 1})):
    sol = sp.solve([e.subs(sub) for e in eqs] + [F.subs(sub)], dict=True)
    print('  ', chart, sol)
# factorization over Q and over Q(i), Q(sqrt5)
print('factor:', sp.factor(F), sp.factor(F, extension=sp.sqrt(5)), sp.factor(F, extension=sp.I))
# rational points of small height
pts = set()
B = 60
for a in range(-B, B + 1):
    for b in range(-B, B + 1):
        # solve the cubic in p for (u, v) = (a, b): integer roots p (scale-free search)
        if (a, b) == (0, 0): continue
        if gcd(abs(a), abs(b)) != 1: continue
        poly = sp.Poly(F.subs({u: a, v: b}), p)
        for r in poly.ground_roots():
            if r.is_rational:
                g = sp.ilcm(sp.denom(r), 1)
                trip = (sp.Rational(r), a, b)
                pts.add(trip)
print('rational points (p, u, v) with gcd(u,v)=1, |u|,|v| <=', B, ':')
for t in sorted(pts, key=lambda t: max(abs(t[1]), abs(t[2]))):
    print('  ', t)
