# Averaged 4-cycle energy test (sanity only).
# P = {(q,Y): Y odd, (Sq)^2+Y^2=L^2, L<=h-1}. Blocks of Y of length B; inside a block keep vectors
# with q >= M*(B/8)^2 so that a common window of width B is admissible for every edge.
# Count quadruples (v1,v2,v3,v4) in one block with |q1-q2+q3-q4| <= 4(M-1) (rank consistency)
# and record s = Y1-Y2+Y3-Y4. Compare s=0 with the mean over small nonzero even s.
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
hist=collections.Counter(); pair0=0; diag_equal=0; tot=0
for b,vs in blocks.items():
    # pairs (v1,v2) keyed by q1-q2 -> list of Y1-Y2 ; pairs (v4,v3) keyed by q4-q3
    pd=collections.defaultdict(list)
    for (Y1,q1) in vs:
        for (Y2,q2) in vs:
            pd[q1-q2].append((Y1-Y2, Y1==Y2, (Y1,q1)==(Y2,q2)))
    for D,lst in pd.items():
        for Dl in range(D-4*(M-1), D+4*(M-1)+1):   # q4-q3 = Dl, q1-q2+q3-q4 = D-Dl in [-8,8]
            lst2=pd.get(Dl)
            if not lst2: continue
            c2=collections.Counter(x[0] for x in lst2)
            for (a,eq,_) in lst:
                for sv,c in c2.items():
                    s=a-sv
                    if abs(s)<=40: hist[s]+=c
            # pairing solutions at s=0 with Y1=Y2 and Y3=Y4
            e1=sum(1 for x in lst if x[1]); e2=sum(1 for x in lst2 if x[1])
            pair0+=e1*e2
nb=[hist[s] for s in range(-40,41,2) if s!=0]
print("S=%d h=2^%s B=%d qmin=%d vectors kept=%d blocks=%d"%(S,sys.argv[2],B,qmin,len(vecs),len(blocks)))
print("count at s=0:",hist[0]," of which Y1=Y2 & Y3=Y4 pairings:",pair0)
print("mean count at nonzero even |s|<=40:",sum(nb)/len(nb)," min",min(nb)," max",max(nb))
print("s=0 excess ratio (all):",hist[0]/(sum(nb)/len(nb))," excluding Y1=Y2,Y3=Y4 pairings:",(hist[0]-pair0)/(sum(nb)/len(nb)))
