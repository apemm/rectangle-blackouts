# Sanity check of the R_FF parametrization (saw_residual_families (iii-b)).
from fractions import Fraction as Fr
import math, numpy as np
def F(p,u,v):
    d=u-v; return p**3-4*d*p*p+(d*d-4*d*u)*p+4*d*d*(u+v)
def UV(a,b):
    U=(a-4*b)*(a*a+b*b); V=a**3-4*a*a*b-3*a*b*b+4*b**3; return U,V
bad=0; gset=set(); SU=0.0; SUp=0.0; shapes=[]
R=400
for b in range(1,R+1):
    for a in range(-R*6,R*6+1):
        if math.gcd(a,b)!=1: continue
        U,V=UV(a,b)
        if U==0: continue
        d=4*b*b*(a-2*b); assert U-V==d
        x1=b*(a*a+b*b); p=x1-b*(-3*a*a+8*a*b+b*b)  # p = x1 - x2 ?
        g=math.gcd(U,V); gset.add(g)
        if 40%g: bad+=1
        SU+=1/abs(U); SUp+=g/abs(U)
        # check the line through the node: point (p',u,v)=(m d,U,V) with m=a/b on F
        assert F(Fr(a,b)*d,U,V)==0
        if U*V>0 and abs(U)<abs(V):   # d<0 thick orientation: L1 shallower
            shapes.append((abs(U)//g,abs(V)//g,a,b))
print("gcd(U,V) values seen:",sorted(gset)," not dividing 40:",bad)
print("partial S_U=sum 1/|U| =",round(SU,4)," sum 1/|U'| =",round(SUp,4))
shapes.sort()
print("smallest d<0 primitive depth pairs (u',v',a,b):",shapes[:12])
print("53:101 present:",[s for s in shapes if (s[0],s[1])==(53,101)])
# back-degree of depth delta: #{shapes: u'|delta}, delta<=H
H=10**6
bd=np.zeros(H+1,dtype=np.int32)
for (u,v,a,b) in shapes:
    if u<=H: bd[u::u]+=1
x=bd[1:]
print("H=",H," mean back-deg",x.mean()," max",x.max()," #>=2",(x>=2).sum()," #>=3",(x>=3).sum(), " #>=5",(x>=5).sum())
