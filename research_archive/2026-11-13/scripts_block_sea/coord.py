# Check the earlier (E;O,E) formula by direct search on a stride-4 scaffold.
import random
from math import gcd
random.seed(5); bad=0; found=0
for trial in range(20000):
    h=random.randint(20,400); A=(h+1)//2; K=h//2; P=random.choice([41,43,47])*h
    s0=random.randint(-A+1,K-1); s1=random.randint(-A+1,K-1); T0=2*s0+1
    c0=0; dc=random.choice([1,-1,2,-2,3])
    i0=random.randint(max(0,-s0),min(A-1,K-1-s0)) if max(0,-s0)<=min(A-1,K-1-s0) else None
    if i0 is None: continue
    t1=random.randint(-6,6)
    if t1==0: continue
    N=(s1-s0)-P*dc; den=10*t1-T0
    if (8*t1*N)%den: continue
    u=-(s1-s0)+8*t1*N//den
    V=(4*(i0+P*c0),2*(i0+s0)+2); Pp=(4*(i0+t1+P*c0),2*(i0+t1)+1)
    iQ=i0+u; Q=(4*(iQ+P*dc),2*(iQ+s1)+2)
    a=(Pp[0]-V[0],Pp[1]-V[1]); b=(Q[0]-V[0],Q[1]-V[1])
    found+=1
    if a[0]*b[0]+a[1]*b[1]!=0: bad+=1
    R=(Pp[0]+Q[0]-V[0],Pp[1]+Q[1]-V[1])
    if R!=(4*(iQ+t1+P*dc),2*(iQ+t1+(s1-s0))+1): bad+=1
    m=abs(den)//gcd(T0,t1)
    if N%m: bad+=1
print('integral solutions',found,'failures',bad)
