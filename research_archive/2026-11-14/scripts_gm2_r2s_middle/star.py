# Two solutions (g1,h1)=(ab,cd), (g2,h2)=(ac,bd) of one curve, N=abcd, K=N+d^2.
# Check: X_i = -(g_i + K/D_i)/2, D1=cd-ab, D2=bd-ac. J := X1-X2.  Derive star and expand with c=b+t.
import sympy as sp
a,b,c,d,dl,J,t = sp.symbols('a b c d delta J t')
K = a*b*c*d + dl**2
D1 = c*d-a*b; D2 = b*d-a*c
X1 = -(a*b + K/D1)/2; X2 = -(a*c + K/D2)/2
star = sp.expand(sp.numer(sp.together(2*(X1-X2) - 2*J)))
star2 = sp.expand(K*(c-b)*(a+d) - D1*D2*(2*J - a*(c-b)))
print('star equals derived (up to sign):', sp.simplify(star - star2)==0, sp.simplify(star + star2)==0)
F = sp.expand(star2.subs(c, b+t))
P = sp.Poly(F, b, d)
for mon, co in sorted(P.terms(), key=lambda x: -sum(x[0])):
    print(mon, sp.factor(co))
