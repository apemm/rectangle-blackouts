# Sea(1,h): row 1 at x != 0 mod 4, row h at every column = 0 mod 4 without a double.
# Enumerate all obstructions; report those with a sea point, by family and labels.
import sys, random, time
from math import isqrt
from board import *
from collections import Counter, defaultdict
h=int(sys.argv[1]); Ts=list(map(int,sys.argv[2].split(','))); seed=int(sys.argv[3]); full=sys.argv[4]=='full'
random.seed(seed); A=(h+1)//2; K=h//2
def S_T(T):
    out=set()
    for d in range(-h,h+1):
        if d==0: continue
        L2=16*d*d+(2*d+T)**2
        if isqrt(L2)**2==L2 and isqrt(L2)<h: out.add(abs(d))
    return out
t0=time.time(); out=Counter(); ex=defaultdict(list)
for T in Ts:
    s=(T-1)//2; I=[i for i in range(A) if 0<=i+s<K]
    if full: occ=set(I)
    else:
        D=S_T(T); order=I[:]; random.shuffle(order); cls=[]
        for i in order:
            if all(abs(i-k) not in D for k in cls): cls.append(i)
        occ=set(cls)
    cols,labels,base=build(h,T,occ,lambda i,x:h,2*Wh(h)+8,nslots=max(I)+1)
    fatal,parked,bm=classify_triples(cols,h)
    for kd,key,Wp in fatal:
        tg=[bm[P] for P in key if P in bm]
        nS=sum(t[0]=='S' for t in tg); nF=sum(t[0]=='F' for t in tg); labs=len(set(t[1] for t in tg if t[0] in 'OE'))
        if nS+nF==0: continue
        k=('tri',kd,'S%d F%d L%d'%(nS,nF,labs)); out[k]+=1; ex[k].append((T,sorted(key)))
    nV3=sum(1 for w,ks in parked.items() if len(ks)>1)
    out[('V3 collisions',)]+=nV3
    mq,bm=mixed_quadruples(cols,h)
    for sup,quad in mq:
        tg=[bm[P] for P in quad]
        nS=sum(t[0]=='S' for t in tg); nF=sum(t[0]=='F' for t in tg); labs=len(set(t[1] for t in tg if t[0] in 'OE'))
        if nS+nF==0: continue
        roles=''.join(t[0] for t in tg)
        k=('mq',roles,'L%d'%labs); out[k]+=1; ex[k].append((T,quad))
    rp,bm=rival_pairs(cols,h)
    for C,Dd,j in rp:
        if bm[C][0] in 'SF' or bm[Dd][0] in 'SF': out[('rp-sea',)]+=1
for k,v in sorted(out.items()): print(k,v, ex[k][:1] if k in ex else '')
print('time',round(time.time()-t0,1))
