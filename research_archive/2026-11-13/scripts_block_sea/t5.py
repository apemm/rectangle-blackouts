# Two-level deep sea: row 1 at x != 0 mod 4; empty column 4m gets row h if
# m != m* (mod 2), row h-2 if m = m* (mod 2), m* = n-parity of slot (h-1)/2.
# h odd. Boundary labels i in {0, A-2, A-1} removed. Lists every obstruction
# with a sea point.
import sys, random, time
from math import isqrt
from board import *
from collections import Counter, defaultdict
h=int(sys.argv[1]); Ts=list(map(int,sys.argv[2].split(','))); seed=int(sys.argv[3]); full=sys.argv[4]=='full'
lev2 = sys.argv[5] if len(sys.argv)>5 else 'two'
random.seed(seed); A=(h+1)//2; K=h//2
def S_T(T):
    out=set()
    for d in range(-h,h+1):
        if d==0: continue
        L2=16*d*d+(2*d+T)**2
        if isqrt(L2)**2==L2 and isqrt(L2)<h: out.add(abs(d))
    return out
t0=time.time(); out=Counter(); ex=defaultdict(list)
margin=2*Wh(h)+8; base=margin-margin%4; mstar=(base//4+(h-1)//2)%2
def fill(i,x):
    if lev2=='one': return h
    rho = h-2 if lev2=="two" else int(lev2)
    return h if (x//4)%2!=mstar else rho
for T in Ts:
    s=(T-1)//2; I=[i for i in range(A) if 0<=i+s<K and i not in (0,A-2,A-1)]
    if not I: continue
    if full: occ=set(I)
    else:
        D=S_T(T); order=I[:]; random.shuffle(order); cls=[]
        for i in order:
            if all(abs(i-k) not in D for k in cls): cls.append(i)
        occ=set(cls)
    cols,labels,b=build(h,T,occ,fill,margin,nslots=max(I)+1)
    assert b==base
    fatal,parked,bm=classify_triples(cols,h)
    for kd,key,Wp in fatal:
        tg=[bm[P] for P in key if P in bm]
        nS=sum(t[0]=='S' for t in tg); nF=sum(t[0]=='F' for t in tg); labs=len(set(t[1] for t in tg if t[0] in 'OE'))
        if nS+nF==0: continue
        k=('tri',kd,'S%d F%d L%d'%(nS,nF,labs)); out[k]+=1; ex[k].append((T,sorted(key),Wp))
    out[('V3 collisions',)]+=sum(1 for w,ks in parked.items() if len(ks)>1)
    mq,bm=mixed_quadruples(cols,h)
    for sup,quad in mq:
        tg=[bm[P] for P in quad]
        nS=sum(t[0]=='S' for t in tg); nF=sum(t[0]=='F' for t in tg); labs=len(set(t[1] for t in tg if t[0] in 'OE'))
        if nS+nF==0: continue
        roles=''.join(t[0] for t in tg)
        k=('mq',roles,'L%d'%labs); out[k]+=1; ex[k].append((T,quad))
    rp,bm=rival_pairs(cols,h)
    for C,Dd,j in rp:
        if bm[C][0] in 'SF' or bm[Dd][0] in 'SF':
            k=('rp',bm[C][0]+bm[Dd][0]); out[k]+=1; ex[k].append((T,C,Dd))
for k,v in sorted(out.items()): print(k,v, ex[k][:2] if k in ex else '')
print('time',round(time.time()-t0,1))
