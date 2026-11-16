# Symbolic checks of the identities in the label-only cells (A1, A3/A4) and D1.
import sympy as sp
u,p,b=sp.symbols('u p b',integer=True)
def slot(i,t): return u*i+p*t+b
def odd(i,s,t): return sp.Matrix([4*slot(i,t), 2*i+1])
def even(i,s,t): return sp.Matrix([4*slot(i,t), 2*(i+s)+2])
Du=4*u**2+1
# A1: V even of (i0,s0,t0); P odd of (i0+d,s0,t0); Q even of (i2,s2,t2)
i0,s0,t0,d,i2,s2,t2=sp.symbols('i0 s0 t0 d i2 s2 t2',integer=True)
V=even(i0,s0,t0); P=odd(i0+d,s0,t0); Q=even(i2,s2,t2)
T0=2*s0+1; c2=(i2+s2)-(i0+s0); N=u*(s2-s0)-p*(t2-t0)
dot=(P-V).dot(Q-V)
print('A1', sp.expand(dot-2*(c2*(2*Du*d-T0)-8*u*d*N)))
print('A1 legs', sp.simplify(P-V-sp.Matrix([4*u*d,2*d-T0])), sp.simplify(Q-V-sp.Matrix([4*(u*c2-N),2*c2])))
# I.2: A odd(i0,s0,t0), B even(i0+a,s0,t0), C odd(iC,s1,t1), D even(iC+bb,s1,t1)
a,iC,bb,s1,t1=sp.symbols('a iC bb s1 t1',integer=True)
A=odd(i0,s0,t0); B=even(i0+a,s0,t0); C=odd(iC,s1,t1); D=even(iC+bb,s1,t1)
U=B-A; twon=C+D-A-B; n2=twon[1]/2
N=u*(s1-s0)-p*(t1-t0); Ds=s1-s0
print('I.2 U', sp.simplify(U-sp.Matrix([4*u*a,2*a+T0])))
# U.n=0  <=>  (2Du a+T0) n2 - 8ua(2N-u Ds) = 0 ? check U.twon/2 == -( (2Du a+T0) n2 - 8ua(2N-uDs) ) up to factor
expr=sp.expand(U.dot(twon)/2)
target=sp.expand((2*Du*a+T0)*n2-8*u*a*(2*N-u*Ds))
print('I.2 E2', sp.simplify(expr-target), sp.simplify(expr+target))
# II(-1,-1): A even(iA,s0,t0), C odd(iA+d,s0,t0), B even(iB,s1,t1), D odd(iB+dp,s1,t1)
iA,iB,dp=sp.symbols('iA iB dp',integer=True)
A=even(iA,s0,t0); C=odd(iA+d,s0,t0); B=even(iB,s1,t1); D=odd(iB+dp,s1,t1)
U=B-A; twon=C+D-A-B; Sig=d+dp; S=s0+s1+1; Dj=(iB+s1)-(iA+s0); N=u*(s1-s0)-p*(t1-t0)
print('II(-1,-1)', sp.expand(U.dot(twon)-4*(Dj*(Du*Sig-S)-4*u*Sig*N)))
# II(1,1): A odd(iA,s0,t0), C even(iA+d,s0,t0), B odd(iB,s1,t1), D even(iB+dp,s1,t1)
A=odd(iA,s0,t0); C=even(iA+d,s0,t0); B=odd(iB,s1,t1); D=even(iB+dp,s1,t1)
U=B-A; twon=C+D-A-B; k=iB-iA; T1=2*s1+1
M=2*Du*Sig+T0+T1
print('II(1,1)', sp.expand(U.dot(twon)-(2*k*M+16*u*p*(t1-t0)*Sig)))
# II(1,-1): A odd(iA,s0,t0), C even(iA+d,s0,t0), B even(iB,s1,t1), D odd(iB+dp,s1,t1)
A=odd(iA,s0,t0); C=even(iA+d,s0,t0); B=even(iB,s1,t1); D=odd(iB+dp,s1,t1)
U=B-A; twon=C+D-A-B
print('II(1,-1) U', sp.simplify(U-sp.Matrix([4*(u*k+p*(t1-t0)),2*k+T1])))
print('II(1,-1) E2', sp.expand(U.dot(twon)-(16*u*Sig*(u*k+p*(t1-t0))+(2*k+T1)*(2*Sig+T0-T1))))
