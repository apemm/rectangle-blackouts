# Search for 4-cycle configurations i_a=i_c (pairing solutions Y1=Y2=Y, Y3=Y4=Y', Y!=Y')
# and evaluate the literal pointwise (E) ratio: count / (prod N_k / range).
import math, collections, sys
S=32; M=3; h=2**21
qmax=(h-1)//S
legs=collections.defaultdict(set)   # Y -> set of q
byq=collections.defaultdict(list)    # q -> list of Y
# T1: q = k e' O, E = S e'/2, Y = k|E^2-O^2|, L = k(E^2+O^2), k,O odd, gcd(e',O)=1
for ep in range(1, 2*math.isqrt(h)//S+2):
    E=S*ep//2
    if E*E+1>h-1: break
    O=1
    while E*E+O*O<=h-1:
        if math.gcd(ep,O)==1:
            k=1
            while k*(E*E+O*O)<=h-1:
                q=k*ep*O; Y=k*abs(E*E-O*O)
                legs[Y].add(q); byq[q].append(Y)
                k+=2
        O+=2
def window_count(d,center):
    w=8*math.sqrt(d); n=0; ys=[]
    for dl in range(-(M-1),M):
        q=M*d+dl
        if q<1: continue
        for Y in byq.get(q,()):
            if abs(Y-center)<=w: n+=1; ys.append((Y,q))
    return n,ys
two=[Y for Y in legs if len(legs[Y])>=2]
idx=collections.defaultdict(list)    # leg difference D -> (Y,q_small,q_big)
for Y in two:
    L=sorted(legs[Y])
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            idx[L[j]-L[i]].append((Y,L[i],L[j]))
best=[]
checked=0
for Y in two:
    L=sorted(legs[Y])
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            q2,q1=L[i],L[j]; D=q1-q2
            if D%M: continue
            g=D//M
            for (Yp,q3,q4) in idx[D]:
                if Yp==Y: continue
                d1,d2=q1//M,q2//M
                if q1-M*d1>M-1 or q2-M*d2>M-1: continue
                d1=round(q1/M); d2=d1-g; d3=round(q3/M); d4=d3+g
                ds=[d1,d2,d3,d4]; qs=[q1,q2,q3,q4]
                if min(ds)<1 or any(abs(qs[t]-M*ds[t])>M-1 for t in range(4)): continue
                dmin=min(ds)
                if abs(Y-Yp)>8*math.sqrt(dmin): continue
                center=(Y+Yp)//2
                if center%2==0: center+=1
                Ns=[]; wins=[]
                for t in range(4):
                    n,ys=window_count(ds[t],center); Ns.append(n); wins.append(ys)
                # exact count of tuples with Y1-Y2+Y3-Y4=0 (same branch), multiplicity over legs
                cnt=0
                c4=collections.Counter(y for y,_ in wins[3])
                for y1,_ in wins[0]:
                    for y2,_ in wins[1]:
                        for y3,_ in wins[2]:
                            cnt+=c4.get(y1-y2+y3,0)
                rng=sum(8*math.sqrt(d) for d in ds)
                rhs=Ns[0]*Ns[1]*Ns[2]*Ns[3]/rng
                checked+=1
                best.append((cnt/rhs,Y,Yp,qs,ds,Ns,cnt,round(rng,1)))
best.sort(reverse=True)
print("P-vectors:",sum(len(v) for v in byq.values()),"two-leg Y:",len(two),"configurations:",checked)
for b in best[:12]: print("ratio %.1f Y=%d Y'=%d q=%s d=%s N=%s count=%d range=%s"%b)
print("configs with ratio>100:",sum(1 for b in best if b[0]>100),", >1000:",sum(1 for b in best if b[0]>1000))
