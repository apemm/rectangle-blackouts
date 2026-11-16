# Search for lines on the two-solution surface phi(X,Y1) = phi(X+J,Y2).
import sympy as sp
X,Y1,Y2,J,d,t,a,b,c,e = sp.symbols('X Y1 Y2 J d t a b c e')
P = lambda x: x**3 + d**2*x
phi = lambda x,y: P(x)/y + x**2 - x*y - y**2 - d**2
E = sp.expand(sp.together((phi(X,Y1)-phi(X+J,Y2))*Y1*Y2))
E = sp.expand(sp.numer(sp.together(E)))
print('E =', sp.factor(E))
sub = sp.expand(E.subs({X:a*t+b, Y1:t, Y2:c*t+e}))
coeffs = sp.Poly(sub, t).all_coeffs()
for co in coeffs: print(sp.factor(co))
print('--- solving')
for extra in [{b:0},{e:0}]:
    cs=[sp.expand(co.subs(extra)) for co in coeffs]
    sols=sp.solve(cs,[a,b,c,e,J],dict=True)
    for s in sols: print(extra, s)
