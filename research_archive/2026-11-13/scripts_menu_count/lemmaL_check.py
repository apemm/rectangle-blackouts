import math, sys
def leg(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1
def factor(n):
    f={};d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
def g(T,D):
    r=1
    for p,e in factor(T).items():
        if p!=2 and D%p and leg(D,p)==1: r*=2*e+1
    return r
def fund_unit(D):
    # smallest unit >1 in O_K, K=Q(sqrt D), D=1 mod 4: (a+b sqrt D)/2, a^2-Db^2=+-4
    for b in range(1,10**6):
        for s in (-4,4):
            a2=D*b*b+s
            a=math.isqrt(a2)
            if a*a==a2: return a,b,s
def kT(T,u,h):
    s=4*u; A=(h+1)//2; K=h//2; st=(T-1)//2
    nT=min(A,K-st)-max(0,-st)
    D=set()
    for d in range(-nT+1,nT):
        if d==0: continue
        Q=s*s*d*d+(2*d+T)**2
        L=math.isqrt(Q)
        if L*L==Q and L<h: D.add(abs(d))
    return len(D)
h=int(sys.argv[1]) if len(sys.argv)>1 else 20000
for u,q in ([(1,None)] if h<=50000 else [])+[(3,3),(5,17),(7,7),(13,13)]:
    D=4*u*u+1
    a,b,sg=fund_unit(D)
    caseA = (a%2==0)  # unit in Z[sqrt D] (a,b even) -> = 1 mod 2
    eta=(a+b*math.sqrt(D))/2
    N=2 if caseA else 6
    R=math.cosh(N*math.log(eta))
    Tmax=int(math.sqrt(D)*h/(2*u*R))
    viol=0;tested=0;minratio=9;zeroq=0;nq=0
    for T in range(1,Tmax+1,2):
        if T%D==0: continue
        if caseA and not (T%q==0 and (T//q)%q!=0): 
            # also record T with g>=3 but no q
            continue
        gg=g(T,D); k=kT(T,u,h); tested+=1
        bound=(2*gg/3-1)/2 if caseA else (2*gg-1)/2
        if k<bound-1e-9: viol+=1
        minratio=min(minratio,k/gg)
    print("u=%d D=%d unit=(%d+%d sqrtD)/2 N=%d caseA=%s Tmax=%d tested=%d violations=%d min k/g=%.3f"%(u,D,a,b,sg,caseA,Tmax,tested,viol,minratio))
