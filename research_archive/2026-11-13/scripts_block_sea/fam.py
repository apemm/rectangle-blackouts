# Formula-level predicates for the shallow families (row-1 sea at x != 0 mod 4).
from math import isqrt
def divisors(N):
    N=abs(N); out=[]
    d=1
    while d*d<=N:
        if N%d==0:
            out.append(d)
            if d*d!=N: out.append(N//d)
        d+=1
    return out
def X1(F,G,h):
    """F even deep, G deep row = 5 mod 8. Number of shallow vertices E."""
    (xF,yF),(xG,yG)=F,G
    if yF%2 or yG%8!=5 or xF==xG: return 0
    if yF+yG-1>h: return 0
    M=(yF-1)*(yG-1)//4
    n=abs(xF-xG)//2   # = 2|n1-n2|
    return sum(1 for d in divisors(M) if d+M//d==n)
def X2(V,G,h):
    (xV,yV),(xG,yG)=V,G
    if yV%4!=1 or yV<5 or yG%2 or yG<=yV or xV==xG: return 0
    f=yV-1; g=yG-yV; X=xG-xV
    if (f*g)%X: return 0
    a=f*g//X
    return 1 if a%4 else 0
def mq_check(A,B,C,D,h):
    (ax,ay),(bx,by),(cx,cy),(dx,dy)=A,B,C,D
    u=(bx-ax,by-ay)
    if u[0]==0: return False
    sx,sy=cx+dx-ax-bx,cy+dy-ay-by
    if sx%2 or sy%2: return False
    n=(sx//2,sy//2)
    if n==(0,0) or n[0]*u[0]+n[1]*u[1]: return False
    w=(dx-cx,dy-cy)
    if w[0]**2+w[1]**2!=u[0]**2+u[1]**2 or w in (u,(-u[0],-u[1])): return False
    p=(ax+n[0],ay+n[1]); q=(bx+n[0],by+n[1])
    for P in (A,B,C,D,p,q):
        if not 1<=P[1]<=h: return False
    return True
def M2c(B,D,h):
    """B,D deep; count (A,C) shallow with A,C,B,D a mixed quadruple, A,C in row 1."""
    (bx,by),(dx,dy)=B,D
    if (dy-by)%2 or dy<=by: return 0
    e=(dy-by)//2; Dl=dx-bx; u2=by-1; cnt=0
    cands=[]
    if u2>0:
        for n1 in divisors(e*u2): cands+= [n1,-n1]
    else:
        cands=[0]
    for n1 in cands:
        if u2>0:
            z=-e*u2//n1
        else:
            if Dl==0 or (Dl*Dl+e*e)%Dl: continue
            z=-(Dl*Dl+e*e)//Dl
        if z==0: continue
        alpha=bx-z
        if alpha%4==0: continue
        A=(alpha,1); kappa=alpha+bx+2*n1-dx
        if kappa%4==0: continue
        C=(kappa,1)
        if mq_check(A,B,C,D,h): cnt+=1
    return cnt
def M1C(A,B,D,h):
    """A,B even deep, D deep; C shallow computed."""
    (ax,ay),(bx,by),(dx,dy)=A,B,D
    if bx==ax: return 0
    t=1+dy-ay-by
    if t%2: return 0
    n2=t//2; u1=bx-ax; u2=by-ay
    if (n2*u2)%u1: return 0
    n1=-n2*u2//u1
    cx=ax+bx+2*n1-dx
    if cx%4==0: return 0
    return 1 if mq_check(A,B,(cx,1),D,h) else 0
