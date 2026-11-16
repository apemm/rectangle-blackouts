# Constructive check of Theorem F / F2(i) at r = 4u: build the predicted in-class Fo/Fo and test Lemma mixedeq
from fractions import Fraction as Fr
def v2(x):
    x=abs(x); c=0
    while x and x%2==0: x//=2; c+=1
    return c
def build(u,a,b,o):
    r=4*u; beta=v2(b)
    # A = alpha1/4 with v2(A)=beta+1 ; t = 4A(2a-rb)b/(a^2+b^2) integer ; Y1 = 4A(a-rb)/b > 0
    base=None
    for A in range(-4,-10**7,-4):
        if v2(A)!=beta+1: continue
        if (4*A*(2*a-r*b)*b)%(a*a+b*b): continue
        if (4*A*(a-r*b))%b: continue
        Y1=4*A*(a-r*b)//b
        if Y1<=0: continue
        if Y1%64 not in (8,24): continue
        o-=1
        if o==0: base=A; break
    A=base; t=4*A*(2*a-r*b)*b//(a*a+b*b); Y1=4*A*(a-r*b)//b
    yL1=10**6+1  # odd label row (absolute row irrelevant for the identities)
    L1=(0,yL1); F1=(4*A,yL1+Y1); L2=(4*u*t,yL1+2*t); Y=yL1+Y1
    X=F1[0]-L1[0]
    assert (t*Y1)%X==0
    n=(-t*Y1//X,t)
    C=(L1[0]+F1[0]+2*n[0]-L2[0], L1[1]+F1[1]+2*n[1]-L2[1])
    BA=(X,Y1); DC=(L2[0]-C[0],L2[1]-C[1])
    ok_perp = n[0]*BA[0]+n[1]*BA[1]==0
    ok_len = BA[0]**2+BA[1]**2==DC[0]**2+DC[1]**2
    ok_ne = DC not in (BA,(-BA[0],-BA[1]))
    ok_row = C[1]==Y
    # filler columns: slot offsets from L1 must be = 0 mod 4 (hole row, w=0) and never a label slot (label slots = 0 mod 32u relative)
    offF1=F1[0]//4; offC=C[0]//4
    ok_fill = offF1%4==0 and offC%4==0 and offF1%(32*u)!=0 and offC%(32*u)!=0 and offF1%16!=0 and offC%16!=0
    m=Fr(X-(C[0]-L2[0]),2*t)
    U=(a-r*b)*(a*a+b*b); V=a**3-r*a*a*b-3*a*b*b+r*b**3
    Y2=Y-L2[1]
    return dict(u=u,a=a,b=b,A=A,t=t,Y1=Y1,Y2=Y2,m=m,ratio_ok=Fr(Y2,Y1)==Fr(V,U),perp=ok_perp,len=ok_len,ne=ok_ne,row=ok_row,fill=ok_fill,t32=t%32==0,v2t=v2(t),pred_v2t=2*v2(b)+4,pq_rows=(L1[1]+n[1]-yL1, F1[1]+n[1]-yL1))
for (u,a,b) in [(1,5,2),(1,7,2),(3,13,2),(3,23,2),(3,25,4),(5,21,2),(5,39,2),(9,37,2)]:
    print(build(u,a,b,1))
