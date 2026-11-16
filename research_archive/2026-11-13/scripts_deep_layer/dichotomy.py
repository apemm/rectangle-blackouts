# Verify: deep C,D same row parity, D-C=(4d,2e), 4d^2+e^2=L'^2.
# e != 0 mod 4 -> shallow witnesses A,B=(2(nC+nD) -/+ L',1) have columns != 0 mod 4 and form a mixed quadruple.
# e == 0 mod 4 -> deep witnesses A,B=(4(nC+nD -/+ L'/2)/2, r) form a mixed quadruple for any row r != (yC+yD)/2.
import math, random
def is_mq(A,B,C,D,h):
    sx=C[0]+D[0]-A[0]-B[0]; sy=C[1]+D[1]-A[1]-B[1]
    if sx%2 or sy%2: return False
    n=(sx//2,sy//2)
    if n==(0,0): return False
    u=(B[0]-A[0],B[1]-A[1]); w=(D[0]-C[0],D[1]-C[1])
    if u[0]==0: return False
    if n[0]*u[0]+n[1]*u[1]!=0: return False
    if u[0]**2+u[1]**2!=w[0]**2+w[1]**2: return False
    if w==u or w==(-u[0],-u[1]): return False
    p=(A[0]+n[0],A[1]+n[1]); q=(B[0]+n[0],B[1]+n[1])
    return all(1<=P[1]<=h for P in (A,B,C,D,p,q))
h=60; bad=0; nsh=0; ndeep=0; nsafe=0
for d in range(1,400):
  for e in range(-29,30):
    if e==0: continue
    L2=4*d*d+e*e; L=math.isqrt(L2)
    if L*L!=L2: continue
    for yC in range(2,h+1):
      yD=yC+2*e
      if not (2<=yD<=h): continue
      nC=1000; nD=nC+d; C=(4*nC,yC); D=(4*nD,yD)
      if e%4:
        xs=[2*(nC+nD)-L,2*(nC+nD)+L]
        if any(x%4==0 for x in xs): bad+=1; continue
        if not is_mq((xs[0],1),(xs[1],1),C,D,h): bad+=1
        else: nsh+=1
      else:
        if (nC+nD-L//2)%2: bad+=1; continue
        nA=(nC+nD-L//2)//2; nB=(nC+nD+L//2)//2
        for r in range(1,h+1):
          if 2*r==yC+yD: continue
          if not is_mq((4*nA,r),(4*nB,r),C,D,h): continue
          ndeep+=1
print('shallow ok',nsh,'deep ok',ndeep,'failures',bad)
