import sympy as sp
a,c,e,b,J,d,t = sp.symbols('a c e b J d t')
# coefficients from lines.py with b=0
X,Y1,Y2=sp.symbols('X Y1 Y2')
E = (-J**3*Y1 - 3*J**2*X*Y1 - J**2*Y1*Y2 - 3*J*X**2*Y1 - 2*J*X*Y1*Y2 + J*Y1*Y2**2 - J*Y1*d**2 - X**3*Y1 + X**3*Y2 - X*Y1**2*Y2 + X*Y1*Y2**2 - X*Y1*d**2 + X*Y2*d**2 - Y1**3*Y2 + Y1*Y2**3)
for (bb,ee,label) in [(0,e,'b=0'),(b,0,'e=0')]:
    sub=sp.expand(E.subs({X:a*t+bb,Y1:t,Y2:c*t+ee}))
    cs=sp.Poly(sub,t).all_coeffs()
    print(label,[sp.factor(x) for x in cs])
# subcase c=1,b=0, eps=(3a-1)/(a^2-a+2)
eps=(3*a-1)/(a**2-a+2)
pol=sp.factor(sp.together(-(3*a+1)+2*eps*(1-a)+eps**2*(a+3)))
print('c=1 subcase poly in a:',pol)
