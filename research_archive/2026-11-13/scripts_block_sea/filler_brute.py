# Admissible filler rows (= 3 mod 4) at each empty slot of one class, against
# every obstruction that contains that filler and otherwise only label points
# and row-1 sea points (fillers of other slots ignored).
import sys, random, time
from math import isqrt
from board import *
from collections import defaultdict
h=int(sys.argv[1]); Ts=list(map(int,sys.argv[2].split(','))); seed=int(sys.argv[3])
random.seed(seed); A=(h+1)//2; K=h//2
def S_T(T):
    out=set()
    for d in range(-h,h+1):
        if d==0: continue
        L2=16*d*d+(2*d+T)**2
        if isqrt(L2)**2==L2 and isqrt(L2)<h: out.add(abs(d))
    return out
rows=[r for r in range(3,h+1) if r%4==3]
t0=time.time(); summary=[]
for T in Ts:
    s=(T-1)//2; I=[i for i in range(A) if 0<=i+s<K]
    D=S_T(T); order=I[:]; random.shuffle(order); cls=[]
    for i in order:
        if all(abs(i-k) not in D for k in cls): cls.append(i)
    occ=set(cls); lo,hi=min(I),max(I)
    empty=[i for i in range(lo,hi+1) if i not in occ]
    cols,labels,base=build(h,T,occ,lambda i,x:None,2*Wh(h)+8,nslots=hi+1)
    for i in empty:
        for r in rows: cols[base+4*i].append((r,('C',i)))
    bm=black_map(cols)
    forb=defaultdict(set); why=defaultdict(set)
    iscand=lambda P: P in bm and bm[P][0]=='C'
    rects,_=tilted_triples(cols,h)
    for key in rects:
        cand=[P for P in key if iscand(P)]
        if len(cand)!=1: continue
        F=cand[0]
        black=[P for P in key if P in bm]; white=[P for P in key if P not in bm]
        if not white: fat=True; kind='V1'
        else:
            x,rho=white[0]; c=[rr for (rr,t) in cols[x] if t[0]!='C']
            if x==F[0]: c=[F[1]]
            if not c: fat=(rho%2==0)   # other empty column: odd filler later
            else: fat=any((rr-rho)%2 for rr in c)
            kind='tri'
        if fat: forb[F[0]].add(F[1]); why[kind].add(F)
    mq,_=mixed_quadruples(cols,h)
    for sup,quad in mq:
        cand=[P for P in sup if iscand(P)]
        if len(cand)!=1: continue
        forb[cand[0][0]].add(cand[0][1]); why['mq'].add(cand[0])
    rp,_=rival_pairs(cols,h)
    for C,Dd,j in rp:
        cand=[P for P in (C,Dd) if iscand(P)]
        if len(cand)!=1: continue
        forb[cand[0][0]].add(cand[0][1]); why['rp'].add(cand[0])
    good=[len(rows)-len(forb[base+4*i]) for i in empty]
    summary.append((T,len(occ),len(empty),min(good) if good else None, sum(good)/max(1,len(good))))
    print('T',T,'labels',len(occ),'empty',len(empty),'admissible rows per empty slot',good,'of',len(rows),{k:len(v) for k,v in why.items()})
print('time',round(time.time()-t0,1))
