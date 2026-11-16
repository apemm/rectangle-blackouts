# Classify every obstruction with a shallow (row-1 sea) point in one block.
import sys, random, time
from math import isqrt
from board import *
from collections import Counter
h=int(sys.argv[1]); T=int(sys.argv[2]); seed=int(sys.argv[3]); mode=sys.argv[4]
random.seed(seed)
A=(h+1)//2; K=h//2; s=(T-1)//2
I=[i for i in range(A) if 0<=i+s<K]
def S_T(T):
    out=set()
    for d in range(-h,h+1):
        if d==0: continue
        L2=16*d*d+(2*d+T)**2
        if isqrt(L2)**2==L2 and isqrt(L2)<h: out.add(abs(d))
    return out
D=S_T(T); order=I[:]; random.shuffle(order); cls=[]
for i in order:
    if all(abs(i-k) not in D for k in cls): cls.append(i)
slots=set(cls)
if mode=='r3': rows=[r for r in range(3,h+1) if r%4==3]
else: rows=[r for r in range(3,h+1) if r%2==1]
fill=lambda i,x: random.choice(rows)
t0=time.time()
cols,labels,base=build(h,T,slots,fill,2*Wh(h)+8,nslots=max(I)+1)
fatal,parked,bm=classify_triples(cols,h)
def kind(P): return bm[P][0] if P in bm else 'w'
fam=Counter()
for kd,key,Wp in fatal+[('P',k,w) for w,ks in parked.items() for k in ks]:
    sh=[P for P in key if P in bm and bm[P][0]=='S']
    if not sh: continue
    E=sh[0]; others=[P for P in key if P in bm and P!=E]
    W=[P for P in key if P not in bm]
    # vertex: the black corner adjacent to both other black corners = opposite to W
    Wp=W[0] if W else None
    # opposite of W is the corner Z with Z = sum - ... : opposite pairs have same midpoint
    pts=list(key); cx=sum(p[0] for p in pts); cy=sum(p[1] for p in pts)
    opp=(cx//2-Wp[0], cy//2-Wp[1]) if Wp else None
    if opp==E:
        if E[0]%2: f='Pa' 
        else:
            r=sorted(P[1]%8 for P in others)
            f='Pb' if all(P[1]%4==3 for P in others) else ('X1' if (any(P[1]%2==0 for P in others) and any(P[1]%8==5 for P in others)) else 'E?')
    else:
        V=opp; G=[P for P in others if P!=V][0]
        g=G[1]-V[1]
        f='X2' if (g%2 and V[1]%4==1 and G[1]%2==0) else ('Pc' if g%2==0 else 'E?')
    tags=tuple(sorted(bm[P][0] for P in others))
    fam[(kd if kd!='P' else 'park',f,tags)]+=1
for k,v in sorted(fam.items()): print('TRI',k,v)
mq,bm=mixed_quadruples(cols,h)
mf=Counter()
for sup,(Aa,B,C,Dd) in mq:
    roles=''.join('s' if bm[P][0]=='S' else 'd' for P in (Aa,B,C,Dd))
    if 's' not in roles: continue
    tags=tuple(bm[P][0] for P in (Aa,B,C,Dd))
    mf[(roles,tags)]+=1
for k,v in sorted(mf.items()): print('MQ',k,v)
print('labels',len(slots),'time',round(time.time()-t0,1))
for sup,(Aa,B,C,Dd) in mq:
    tags=tuple(bm[P] for P in (Aa,B,C,Dd))
    if any(t[0] in 'OE' for t in tags) and any(t[0]=='S' for t in tags):
        print('  detail',Aa,B,C,Dd,tags)
print('base',base,'slots',sorted(slots))
