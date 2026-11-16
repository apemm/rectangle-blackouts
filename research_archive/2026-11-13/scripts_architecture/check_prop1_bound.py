import math, sys
from stride_sets import triples, dsets
from collections import defaultdict
# (1) Prop 1 for stride s: full diagonal block, no right angle among black points (any orientation)
def right_angle_free(h,s,T):
    A=(h+1)//2; K=h//2; sd=(T-1)//2
    pts=[]
    for i in range(max(0,-sd),min(A,K-sd)):
        j=i+sd; pts.append((s*i,2*i+1)); pts.append((s*i,2*j+2))
    n=len(pts)
    for a in range(n):
        V=pts[a]
        vs=[(P[0]-V[0],P[1]-V[1]) for P in pts if P!=V]
        S=set(vs)
        for (x,y) in vs:
            # perpendicular vectors: need (x2,y2) with x x2 + y y2 = 0
            for (x2,y2) in vs:
                if x*x2+y*y2==0: return False
    return True
bad=0
for h in (12,17,24):
    for s in (2,4,6,8,10,12):
        for T in range(-(h-1),h,2):
            if not right_angle_free(h,s,T): bad+=1; print("angle",h,s,T)
print("prop1 failures:",bad)
# (2) bound |S_T| <= 2 tau(sigma^2) g_sigma(T) (1 + 2 log(3h/|T|)/log phi)
def fac(n):
    f={};p=2
    while p*p<=n:
        while n%p==0: f[p]=f.get(p,0)+1; n//=p
        p+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
def leg(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1
def g(T,Delta):
    r=1
    for p,e in fac(abs(T)).items():
        if p!=2 and Delta%p and leg(Delta,p)==1: r*=2*e+1
    return r
def tau(n): 
    r=1
    for e in fac(n).values(): r*=e+1
    return r
def Sfull(h,s,tr):
    S=defaultdict(set)
    for (x,y,L) in tr:
        if x%s or y%2==0: continue
        for sx in (1,-1):
            for sy in (1,-1):
                d=sx*x//s; T=sy*y-2*d
                if abs(T)<h: S[T].add(d)
    return S
h=int(sys.argv[1]) if len(sys.argv)>1 else 20000
tr=triples(h); phi=(1+5**.5)/2; worst=0
for sig in (1,2,4,6,10):
    s=2*sig; Delta=sig*sig+1; S=Sfull(h,s,tr)
    for T,ds in S.items():
        b=2*tau(sig*sig)*g(T,Delta)*(1+2*math.log(3*h/abs(T))/math.log(phi))
        worst=max(worst,len(ds)/b)
print("max |S_T|/bound:",worst)
