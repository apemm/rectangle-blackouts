# Same test as averaged_energy_test.py, but splits s=0 into the two diagonal classes
# (Y1=Y2 & Y3=Y4) and (Y1=Y4 & Y2=Y3) and the off-diagonal rest.
import math, collections, sys
S=int(sys.argv[1]); M=3; h=2**int(sys.argv[2]); B=int(sys.argv[3])
qmin=M*(B//8)**2
vecs=[]
for ep in range(1, 2*math.isqrt(h)//S+2):
    E=S*ep//2
    if E*E+1>h-1: break
    O=1
    while E*E+O*O<=h-1:
        if math.gcd(ep,O)==1:
            k=1
            while k*(E*E+O*O)<=h-1:
                q=k*ep*O; Y=k*abs(E*E-O*O)
                if q>=qmin: vecs.append((Y,q))
                k+=2
        O+=2
blocks=collections.defaultdict(list)
for Y,q in vecs: blocks[Y//B].append((Y,q))
s_hist=collections.Counter(); offdiag0=0; cls1=0; cls2=0; both=0; offdiag_examples=[]
for b,vs in blocks.items():
    n=len(vs)
    byq=collections.defaultdict(list)
    for v in vs: byq[v[1]].append(v[0])
    qs=sorted(byq)
    # direct enumeration over (v1,v2,v3), v4 determined by q4 in window and Y4 = Y1-Y2+Y3-s
    Yset=collections.Counter((Y,q) for Y,q in vs)
    for (Y1,q1) in vs:
        for (Y2,q2) in vs:
            for (Y3,q3) in vs:
                base=q1-q2+q3
                for dl in range(-4*(M-1),4*(M-1)+1):
                    q4=base-dl
                    if q4 not in byq: continue
                    for Y4 in byq[q4]:
                        s=Y1-Y2+Y3-Y4
                        s_hist[s]+=1
                        if s==0:
                            a=(Y1==Y2 and Y3==Y4); c=(Y1==Y4 and Y2==Y3)
                            if a: cls1+=1
                            if c: cls2+=1
                            if a and c: both+=1
                            if not a and not c:
                                offdiag0+=1
                                if len(offdiag_examples)<6: offdiag_examples.append(((Y1,q1),(Y2,q2),(Y3,q3),(Y4,q4)))
nb=[s_hist[s] for s in range(-40,41,2) if s!=0]
mean=sum(nb)/len(nb)
print("S=%d h=2^%s B=%d vectors=%d"%(S,sys.argv[2],B,len(vecs)))
print("s=0 total",s_hist[0],"class Y1=Y2&Y3=Y4",cls1,"class Y1=Y4&Y2=Y3",cls2,"both",both,"off-diagonal",offdiag0)
print("mean at nonzero even |s|<=40: %.1f (min %d max %d)"%(mean,min(nb),max(nb)))
print("off-diagonal s=0 / mean nonzero = %.3f"%(offdiag0/mean))
for e in offdiag_examples: print(" off-diag example",e)
