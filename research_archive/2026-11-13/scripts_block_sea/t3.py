# Full diagonals (all slots occupied), fillers random in rows = 3 mod 4.
# Check the classification of shallow-point obstructions; list label pairs.
import sys, random, time
from board import *
from collections import Counter, defaultdict
h=int(sys.argv[1]); Ts=list(map(int,sys.argv[2].split(','))); seed=int(sys.argv[3])
random.seed(seed)
A=(h+1)//2; K=h//2
rows=[r for r in range(3,h+1) if r%4==3]
bad=Counter(); pairs=defaultdict(set); t0=time.time()
for T in Ts:
    s=(T-1)//2
    I=[i for i in range(A) if 0<=i+s<K]
    slots=set(I)
    cols,labels,base=build(h,T,slots,lambda i,x: random.choice(rows),2*Wh(h)+8,nslots=max(I)+1)
    fatal,parked,bm=classify_triples(cols,h)
    for kd,key,Wp in fatal+[('P',k,w) for w,ks in parked.items() for k in ks]:
        sh=[P for P in key if P in bm and bm[P][0]=='S']
        if not sh: continue
        E=sh[0]; others=[P for P in key if P in bm and P!=E]
        if len(sh)>1 or len(others)!=2: bad[('tri-shape',kd)]+=1; continue
        pts=list(key); cx=sum(p[0] for p in pts); cy=sum(p[1] for p in pts)
        opp=(cx//2-Wp[0], cy//2-Wp[1])
        if opp==E:
            if E[0]%2: f='Pa' if all(P[1]%2==0 for P in others) else 'E?'
            elif all(P[1]%4==3 for P in others): f='Pb'
            elif any(P[1]%2==0 for P in others) and any(P[1]%8==5 for P in others): f='X1'
            else: f='E?'
        else:
            V=opp; G=[P for P in others if P!=V][0]; g=G[1]-V[1]
            f='X2' if (g%2 and V[1]%4==1 and G[1]%2==0) else ('Pc' if g%2==0 else 'E?')
        fat = kd!='P'
        if (f in ('X1','X2'))!=fat or f=='E?': bad[('tri',f,kd)]+=1
        if fat:
            labs=sorted(set(bm[P][1] for P in others if bm[P][0] in 'OE'))
            nf=sum(1 for P in others if bm[P][0]=='F')
            if nf: bad[('filler in fatal tri',f)]+=1
            pairs[(f,T)].add(tuple(labs))
    mq,bm=mixed_quadruples(cols,h)
    for sup,(Aa,B,C,Dd) in mq:
        roles=''.join('s' if bm[P][0]=='S' else 'd' for P in (Aa,B,C,Dd))
        if 's' not in roles: continue
        ok = roles in ('ssdd','sdsd','sdds','dssd','dsds') or roles in ('ddsd','ddds')
        if not ok: bad[('mq-roles',roles)]+=1; continue
        deep=[P for P in (Aa,B,C,Dd) if bm[P][0]!='S']
        labs=sorted(set(bm[P][1] for P in deep if bm[P][0] in 'OE'))
        nf=sum(1 for P in deep if bm[P][0]=='F')
        fam={'ssdd':'M2a'}.get(roles,'M1C' if roles in ('ddsd','ddds') else 'M2c')
        if fam=='M1C':
            a,b=Aa,B; dd= Dd if roles=='ddsd' else C; cc= C if roles=='ddsd' else Dd
            if not (a[1]%2==0 and b[1]%2==0 and dd[1]%4==1 and cc[0]%4==2): bad[('M1C-pred',)]+=1
        if fam=='M2a':
            from math import isqrt
            dx=Dd[0]-C[0]; dy=Dd[1]-C[1]; L=isqrt(dx*dx+dy*dy)
            pred = (L*L==dx*dx+dy*dy) and (L%4==2 or (L%8==4 and dx%8==0))
            if not pred: bad[('M2a-pred',)]+=1
        if nf==0: pairs[(fam,T)].add(tuple(labs))
        else: pairs[(fam+'-filler',T)].add((tuple(labs),nf))
print('violations of the classification:',dict(bad))
for k in sorted(pairs):
    v=sorted(pairs[k]); print(k,len(v),v[:12])
print('time',round(time.time()-t0,1))
