# Symbolic checks of the identities used in Propositions parked/V3 (stride 4u layout).
import sympy as sp, random
u,p,b,r0=sp.symbols('u p b r0',integer=True)
def slot(i,t): return u*i+p*t+b
def odd(i,s,t): return sp.Matrix([4*slot(i,t), 2*i+1])
def even(i,s,t): return sp.Matrix([4*slot(i,t), 2*(i+s)+2])
Du=4*u**2+1
iV,sV,tV,iG,sG,tG,a,g,gam=sp.symbols('iV sV tV iG sG tG a g gam',integer=True)
# Pc odd-odd: V odd, G odd, E = V+(a,-f), f=2uV
V=odd(iV,sV,tV); G=odd(iG,sG,tG); uV=(V[1]-r0)/2
E=V+sp.Matrix([a,-2*uV])
dI=iG-iV
print('Pc oo', sp.expand((E-V).dot(G-V) - 4*(a*(u*dI+p*(tG-tV)) - uV*dI)))
# Pc ee: V even, G even
V=even(iV,sV,tV); G=even(iG,sG,tG); f=V[1]-r0
E=V+sp.Matrix([a,-f]); Dj=(iG+sG)-(iV+sV); N=u*(sG-sV)-p*(tG-tV)
print('Pc ee', sp.expand((E-V).dot(G-V) - 2*(2*a*(u*Dj-N) - f*Dj)))
# Fee: E1 even vertex, V filler at (4(n1+alpha), y1+d), E2 even
i1,s1,t1,i2,s2,t2,al,d=sp.symbols('i1 s1 t1 i2 s2 t2 al d',integer=True)
E1=even(i1,s1,t1); E2=even(i2,s2,t2); Vf=E1+sp.Matrix([4*al,d])
eta=(i2+s2)-(i1+s1); N=u*(s2-s1)-p*(t2-t1)
print('Fee', sp.expand((Vf-E1).dot(E2-E1) - 2*(8*al*(u*eta-N)+d*eta)))
# Foo label vertex: O1 odd, O2 odd of same type with Di=4eps
eps,e=sp.symbols('eps e',integer=True)
O1=odd(i1,s1,t1); O2=odd(i1+4*eps,s2,t2); Vf=O1+sp.Matrix([4*al,8*e])
print('Foo', sp.expand((Vf-O1).dot(O2-O1) - 16*(al*(4*u*eps+p*(t2-t1))+4*e*eps)))
# (P1) inversion: x_W - 4ud - 4b + 4uc' = Du*a + 4p t_V, with i_V = u a - c', c'=(1-r0)/2
dd,tc=sp.symbols('dd tc',integer=True)
cp=(1-r0)/2
iVv=u*a-cp
V=odd(iVv,sV,tc); uV=(V[1]-r0)/2
print('uV = u a', sp.simplify(uV-u*a))
W=V+sp.Matrix([4*u*dd,2*dd])+sp.Matrix([a,-2*uV])
print('P1 W row', sp.simplify(W[1]-(r0+2*dd)), 'P1 inversion', sp.expand(W[0]-4*u*dd-4*b+4*u*cp-(Du*a+4*p*tc)))
