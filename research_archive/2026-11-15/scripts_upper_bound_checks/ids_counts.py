# Checks for the counted cells: eq:Nh from (I1),(I2); E0 identities; the type-II conic identity;
# the 2L2F map to E0; norm classes of Lemma normclass by residues.
import sympy as sp, itertools
n1,w,e,u2,D=sp.symbols('n1 w e u2 Delta')
# (I2) gives Delta = 2n1 + (e^2+n1^2)/w ; substitute in (I1): e u2 = n1(Delta+w)
Dl=2*n1+(e**2+n1**2)/w
print('eq:Nh', sp.simplify(sp.expand((e*u2-n1*(Dl+w))*w) - sp.expand(e*w*u2-n1*(e**2+(n1+w)**2))))
# E0 identities: L^2-W^2 = 4e(Q-e) given XY=e^2+n1^2, n1 L = e(Q-2e)
X,Y,Q=sp.symbols('X Y Q')
L=X+Y+2*n1; W=X-Y
expr=sp.expand(L**2-W**2-4*X*Y-4*n1*(X+Y)-4*n1**2)
print('E0 (a) step', expr)
# conic identity for type II
u,Sg,dd,H,de,U2=sp.symbols('u Sigma Dd H De U2')
G=16*u**2*dd**2+de**2
Xc=16*u**2*Sg*dd-U2*H; Yc=4*u*Sg*(de+U2)
print('conic', sp.expand(Xc**2+Yc**2-U2**2*(H**2+16*u**2*Sg**2) - 16*u**2*Sg*(Sg*G+2*U2*(Sg*de-H*dd))))
# 2L2F map: roots Zx, Wx of z^2 - X1 z + e(e+A) ; k X1 = e A ; X=Zx-k, Y=Wx-k
k,A,Zx=sp.symbols('k A Zx')
X1=e*A/k; Wx=X1-Zx
rel=sp.expand(Zx**2-X1*Zx+e*(e+A))  # =0 on the configuration
XYv=sp.expand((Zx-k)*(Wx-k)-(e**2+k**2))
print('2L2F XY', sp.simplify(XYv + rel))  # XY-(e^2+k^2) = -(Zx^2 - X1 Zx + e(e+A)) ?
print('2L2F sum', sp.simplify(k*((Zx-k)+(Wx-k)+2*k)-e*A))
# Norm classes by residues: label slot residue rho mod 16, odd rows yP mod 64, even rows yP+tauT mod 32,
# filler at offset w: slot = rho+w mod 4, row = yP + 8(w+c) mod 64, c odd.
ok=True
for c in (1,3):
  for tauT in range(1,32,2):
    for w0 in range(4):
      for a in range(0,64):            # a = n_F - n_label, need a = w0 mod 4
        if a%4!=w0: continue
        for b8 in range(8):            # f - y_o = 8(w+c) + 64 t  -> mod 512 use t in 0..7
          b=8*(w0+c)+64*b8
          N=16*a*a+b*b
          v=(N & -N).bit_length()-1
          if v!={0:6,1:4,2:7,3:4}[w0]: ok=False
          be=b-tauT                    # f - y_e = 8(w+c) - tauT mod 32
          for t2 in range(4):
            Ne=16*a*a+(be+32*t2)**2
            if (Ne-tauT*tauT-16)%32!=0: ok=False
print('norm classes N3,N4', ok)
