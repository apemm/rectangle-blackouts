# per-diagonal: G_T, intra X1, intra M2c, intra X2 graphs; degeneracy and greedy (smallest-last) colours
import sys, time
from math import isqrt, gcd
def issq(n): return n>=0 and isqrt(n)**2==n
def v2(n):
    n=abs(n); c=0
    while n%2==0: n//=2; c+=1
    return c
def divs(n):
    out=[];d=1
    while d*d<=n:
        if n%d==0: out.append(d); out.append(n//d)
        d+=1
    return set(out)
def graphs(h,T):
    A=(h+1)//2; K=h//2; s=(T-1)//2
    L=[i for i in range(A) if 0<=i+s<K]; Ls=set(L)
    GT=set(); X1=set(); M2=set(); X2=set()
    for a in range(len(L)):
        for b in range(a+1,len(L)):
            d=L[b]-L[a]
            if issq(16*d*d+(2*d+T)**2) or issq(16*d*d+(2*d-T)**2): GT.add((L[a],L[b]))
    for iG in L:
        if iG%4!=2: continue
        u=iG//2; yG=2*iG+1
        for k in L:
            if k==iG: continue
            yF=2*(k+s)+2
            if yF+yG-1>h: continue
            w=k-3*u
            if issq(w*w-u*(5*u+T)): X1.add((min(iG,k),max(iG,k)))
    # M2c via parametrization over B
    for iB in L:
        for yB in (2*iB+1, 2*(iB+s)+2):
            u2=yB-1
            if u2<=0: continue
            for f in divs(10*u2):
                Y=1
                while Y*Y<=f:
                    X2_=f-Y*Y; X=isqrt(X2_)
                    if X*X==X2_:
                        for XX in {X,-X}:
                            beta=Y; alpha=XX+4*beta
                            if alpha<=0 or alpha>=2*beta or gcd(alpha,beta)!=1: continue
                            num=2*u2*(2*beta-alpha)*beta*beta; den=alpha*f
                            if num%den: continue
                            t=num//den
                            if (alpha*t)%beta: continue
                            n1=alpha*t//beta
                            if (t*u2)%n1: continue
                            z=-t*u2//n1
                            if z%4==0 or (2*n1-z)%4==0: continue
                            if yB+t>h or (iB+t) not in Ls: continue
                            if n1*((4*t-n1)**2+t*t)!=t*u2*(4*t-2*n1): continue
                            M2.add((iB,iB+t))
                    Y+=1
    # X2 intra: V odd pt slot i (i even>=2, row 2i+1=1 mod4), G even pt slot i+t, g=2t+T odd>0, a=i*g/(2t) integer, a!=0 mod 4
    for i in L:
        if i%2 or i<2: continue
        for k in L:
            t=k-i
            if t==0: continue
            g=2*t+T
            if g<=0 or 1+g>h: continue
            if (i*g)%(2*t): continue
            a=i*g//(2*t)
            if a%4==0: continue
            X2.add((min(i,k),max(i,k)))
    return L,GT,X1,M2,X2
def degeneracy_color(L,E):
    adj={v:set() for v in L}
    for a,b in E: adj[a].add(b); adj[b].add(a)
    deg={v:len(adj[v]) for v in L}; removed=set(); order=[]; dg=0
    import heapq
    hp=[(deg[v],v) for v in L]; heapq.heapify(hp)
    while hp:
        d,v=heapq.heappop(hp)
        if v in removed or d!=deg[v]: continue
        dg=max(dg,d); removed.add(v); order.append(v)
        for w in adj[v]:
            if w not in removed: deg[w]-=1; heapq.heappush(hp,(deg[w],w))
    col={}
    for v in reversed(order):
        used={col[w] for w in adj[v] if w in col}
        c=0
        while c in used: c+=1
        col[v]=c
    return dg, (max(col.values())+1 if col else 0), max((len(adj[v]) for v in L),default=0)
h=int(sys.argv[1]); Ts=[int(x) for x in sys.argv[2].split(',')]
t0=time.time()
for T in Ts:
    L,GT,X1,M2,X2=graphs(h,T)
    r=lambda E: degeneracy_color(L,E)
    def split(E,key): return {(a,b) for a,b in E if key(a)==key(b)}
    print(f"T={T} n={len(L)} |GT|={len(GT)} |X1|={len(X1)} |M2c|={len(M2)} |X2|={len(X2)}")
    print("  GT (degen,col,maxdeg)",r(GT)," X1",r(X1)," M2c",r(M2)," X2",r(X2))
    U=GT|X1|M2
    print("  GT+X1+M2c",r(U)," GT+X1+M2c+X2",r(U|X2))
    print("  X2 same v2 mod3:",len(split(X2,lambda i:v2(i)%3 if i else 99)))
    print("  M2c same i mod4:",len(split(M2,lambda i:i%4)),"mod16:",len(split(M2,lambda i:i%16)))
print("time",round(time.time()-t0,1))
