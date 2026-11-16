# rigid 2-adic layout (stride 4), classes = greedy colouring of G_T; optional regions by s mod 4; optional random order
import random
from math import isqrt
def issq(n): return n>=0 and isqrt(n)**2==n
def isprime(n):
    if n<2: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True
def classes_for(h,T):
    A=(h+1)//2; K=h//2; s=(T-1)//2
    L=[i for i in range(A) if 0<=i+s<K]
    adj={i:set() for i in L}
    for a in range(len(L)):
        for b in range(a+1,len(L)):
            d=L[b]-L[a]
            if issq(16*d*d+(2*d+T)**2) or issq(16*d*d+(2*d-T)**2):
                adj[L[a]].add(L[b]); adj[L[b]].add(L[a])
    col={}
    for v in sorted(L,key=lambda v:-len(adj[v])):
        used={col[w] for w in adj[v] if w in col}; c=0
        while c in used: c+=1
        col[v]=c
    nc=max(col.values())+1 if col else 0
    return s,[[i for i in L if col[i]==c] for c in range(nc)]
def build(h,mode='rigid',seed=1,pmin=None):
    K=h//2
    p=20*h+1 if pmin is None else pmin
    while not isprime(p): p+=1
    nu=0
    while 2**nu*8<K: nu+=1
    Q=2**nu; kappa=0; pinv=pow(p,-1,Q)
    cls=[]  # (s, slots)
    for T in range(-(h-1),h,2):
        s,cl=classes_for(h,T)
        for c in cl: cls.append((s,c))
    pos={}
    if mode=='random':
        idx=list(range(len(cls))); random.Random(seed).shuffle(idx)
        for k,ci in enumerate(idx): pos[ci]=k
    else:
        byres={}
        for ci,(s,c) in enumerate(cls): byres.setdefault((s-kappa)%Q,[]).append(ci)
        B=max(len(v) for v in byres.values())
        if mode=='rigid':
            for r,lst in byres.items():
                base=(pinv*r)%Q
                for k,ci in enumerate(lst): pos[ci]=base+Q*k
        elif mode=='region4':
            gap=((h*h)//(8*p)+3); gap=((gap+Q-1)//Q)*Q
            for sig in range(4):
                R=sig*(Q*B+gap)
                for r,lst in byres.items():
                    if (r+kappa)%4!=sig: continue
                    base=(pinv*r)%Q
                    for k,ci in enumerate(lst): pos[ci]=R+base+Q*k
    pts={}  # (x,y)->(kind,ci,i)
    for ci,(s,c) in enumerate(cls):
        M=p*pos[ci]
        for i in c:
            x=4*(i+M)
            pts[(x,2*i+1)]=('o',ci,i); pts[(x,2*(i+s)+2)]=('e',ci,i)
    return p,Q,cls,pos,pts
