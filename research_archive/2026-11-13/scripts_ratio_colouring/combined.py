# Combined back-degree beta(i) = b_IV(u(i)) + sum over 8 (row, parity) maps of b_U(delta(i)), superset graphs, one diagonal.
import numpy as np, math, sys
h=int(sys.argv[1]); T=int(sys.argv[2]); r0=1
H=h+100
def UV(a,b): return (a-4*b)*(a*a+b*b), a**3-4*a*a*b-3*a*b*b+4*b**3
bU=np.zeros(H+1,dtype=np.int32)
R=int((40*H)**(1/3))+5
for b in range(1,R+1):
    for a in range(-6*R,6*R+1):
        if math.gcd(a,b)!=1: continue
        U,V=UV(a,b)
        if U==0 or U*V<=0 or abs(U)>=abs(V): continue
        u=abs(U)//math.gcd(U,V)
        if u<=H: bU[u::u]+=1
bIV=np.zeros(H+1,dtype=np.int32)
be=3
while be**3<=5*H+10:
    for al in range(1,be,2):
        if math.gcd(al,be)==1 and (be-al)%4==0:
            F=4*(al-2*be)**2+be*be; g=math.gcd(F,be-al); p=(al*F+4*(be-al)*be*be)//g
            if p<=H: bIV[p::2*p]+=1
    be+=2
Tstar=h-((h-3)%16)   # some row = 3 mod 16 near h
n=(h-T)//2
i=np.arange(0,n)
beta=bIV[(2*i+1-r0)//2+0]*( ((2*i+1-r0)//2)>0 )
for o in range(4):
    Y=Tstar-24+8*o
    for par in (0,1):
        d=Y-(2*i+1)-(T if par else 0)
        ok=(d>=1)&(d<=H)
        beta=beta+np.where(ok,bU[np.clip(d,0,H)],0)
print("h=%d T=%d labels=%d  mean beta=%.3f  max beta=%d  #beta>=10: %d  #beta>=20: %d"%(h,T,n,beta.mean(),beta.max(),(beta>=10).sum(),(beta>=20).sum()))
