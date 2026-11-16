"""Sanity checks for the stride-4u shape identities (u odd).
Symbolic: I.2 identity, II conic identity, Foo label-vertex dot product,
D8 factorisation.  Numeric: coordinates of L***(u) labels (slot n = u i + p t + b,
column 4n) used to check the I.2 / II equations from true points, and the
A(iii) inversion (W determines the intra-class SLL triple)."""
import random, sympy as sp

u,a,T0,Tp,m,Dt,p,b,Ds = sp.symbols('u a T0 Tp m Dt p b Ds', integer=True)
# ---------- I.2 from coordinates ----------
i0,iC = sp.symbols('i0 iC', integer=True)
t0,b0 = sp.symbols('t0 b0', integer=True)
def odd(i,t): return (4*(u*i+p*t+b0), 2*i+1)
def even(i,t,T): return (4*(u*i+p*t+b0), 2*i+1+T)
A = odd(i0,t0); B = even(i0+a,t0,T0)
C = odd(iC,t0+Dt); D = even(iC+b,t0+Dt,Tp)
U = (B[0]-A[0], B[1]-A[1])
n2x = C[0]+D[0]-A[0]-B[0]; n2y = C[1]+D[1]-A[1]-B[1]
E2 = sp.expand(U[0]*n2x + U[1]*n2y)
mm = 2*iC+b-2*i0-a
Delta = 4*u**2+1
Ustar = 2*Delta*a+T0
n2 = mm + (Tp-T0)/2
DsE = (Tp-T0)/2
# claimed: E2 == 2*( m*Ustar + 16 u a p Dt + (2a+T0) Ds )
claim = 2*(mm*Ustar + 16*u*a*p*Dt + (2*a+T0)*DsE)
print('I.2 E2 form residual:', sp.simplify(E2-claim))
# claimed: n2*Ustar = 8ua(2N - u Ds) when E2=0, N = u Ds - p Dt
N = u*DsE - p*Dt
res = sp.expand(n2*Ustar - 8*u*a*(2*N-u*DsE) - (E2/2))
print('I.2 recovery residual (should be 0 mod E2):', sp.simplify(res))

# ---------- II conic identity ----------
S,Dd,H,De,U2 = sp.symbols('S Dd H De U2')
G = 16*u**2*Dd**2+De**2
X = 16*u**2*S*Dd - U2*H; Y = 4*u*S*(De+U2)
lhs = X**2+Y**2 - U2**2*(H**2+16*u**2*S**2)
print('II conic residual:', sp.factor(sp.expand(lhs - 16*u**2*S*(S*G + 2*U2*(De*S-Dd*H)))))

# ---------- II E1/E2 from coordinates, role (1,-1) ----------
iA,iB,d,dp,tA,tB,s0,sp_ = sp.symbols('iA iB d dp tA tB s0 sp_', integer=True)
T0e = 2*s0+1; Tpe = 2*sp_+1
A2 = odd(iA,tA); C2 = even(iA+d,tA,T0e)        # A odd, C even, same block
B2 = even(iB,tB,Tpe); D2 = odd(iB+dp,tB)        # B even, D odd, same block
U_ = (B2[0]-A2[0], B2[1]-A2[1]); g=(C2[0]-A2[0],C2[1]-A2[1]); gp=(D2[0]-B2[0],D2[1]-B2[1])
E2c = sp.expand(U_[0]*(g[0]+gp[0]) + U_[1]*(g[1]+gp[1]))
Sig = d+dp; Hh = g[1]+gp[1]
print('II E2 = 4u Sigma U1 + H U2 residual:', sp.simplify(E2c - (4*u*Sig*U_[0] + Hh*U_[1])))
V_ = (D2[0]-C2[0], D2[1]-C2[1])
E1c = sp.expand(V_[0]**2+V_[1]**2 - U_[0]**2-U_[1]**2)
Ddd = dp-d; Dee = gp[1]-g[1]
print('II E1 residual:', sp.simplify(E1c - (2*(U_[0]*4*u*Ddd + U_[1]*Dee) + 16*u**2*Ddd**2 + Dee**2)))
print('II U1 = 4(u k + p Dt):', sp.simplify(U_[0] - 4*(u*(iB-iA) + p*(tB-tA))))

# ---------- Foo with label vertex ----------
al,e,eps,DM = sp.symbols('al e eps DM', integer=True)
Vv = (4*al, 8*e); O2 = (4*(4*u*eps + DM), 8*eps)   # O2-O1 with Di = 4 eps
print('Foo dot/16 - (al*delta + 4 e eps):', sp.expand((Vv[0]*O2[0]+Vv[1]*O2[1])/16 - (al*(4*u*eps+DM) + 4*e*eps)))

# ---------- D8 factorisation ----------
Gs,R,e1,e2 = sp.symbols('Gs R e1 e2')
phi = lambda ek: 4*Gs*ek + R*e1*e2/ek     # gamma_k = G e_k, a_k = u g/(2 gamma_k) = N/(G e_k), N = R G e1 e2
print('D8 factorisation residual:', sp.factor(phi(e1)-phi(e2) - (e1-e2)*(4*Gs-R)))

# ---------- numeric: A(iii) inversion at stride 4u ----------
random.seed(1)
bad = 0; tested = 0
for trial in range(20000):
    uu = random.choice([3,5,7,9])
    h = random.randint(2000, 20000)
    P = 8*uu*uu+4
    pp = random.randint(P*h+1, 2*P*h)          # any integer of the size of p (only sizes used)
    r0 = random.choice([1,3])
    bb = random.randint(-50,50)
    # intra-class odd Pc needs u | u_V, u_V = i_V + (1-r0)//2 odd
    A_ = (h+1)//2
    av = random.randrange(1, (A_)//uu, 2)       # a = u_V/u odd
    uV = uu*av
    iV = uV - (1-r0)//2
    if not (0 <= iV < A_): continue
    tc = random.randint(0, 10**6)
    t = 32*random.randint(1, 5)
    xV = 4*(uu*iV + pp*tc + bb)
    xW = xV + 4*uu*t + av
    # invert: xW - 4ut - 4b = Delta*a - 4u c' + 4 p t_c, c' = (1-r0)//2
    cp = (1-r0)//2
    val = xW - 4*uu*t - 4*bb + 4*uu*cp
    a_rec = val % (4*pp); tc_rec = val // (4*pp)
    Dl = 4*uu*uu+1
    ok = (a_rec % Dl == 0) and a_rec//Dl == av and tc_rec == tc
    tested += 1
    bad += (not ok)
print('A(iii) inversion: tested', tested, 'failures', bad)
