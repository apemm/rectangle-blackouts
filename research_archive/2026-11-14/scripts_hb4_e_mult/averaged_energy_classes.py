# Splits the s=0 solutions of the block 4-cycle count into:
#  (i)  identical-vector diagonals: v1=v2 & v3=v4, or v1=v4 & v2=v3 (repeated factors)
#  (ii) same-Y diagonals with some distinct q (two-leg Y's): Y1=Y2 & Y3=Y4 or Y1=Y4 & Y2=Y3, not (i)
#  (iii) off-diagonal
# and compares with the mean count at small nonzero even s (the random-model level).
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
hist=collections.Counter(); c=collections.Counter()
for b,vs in blocks.items():
    byq=collections.defaultdict(list)
    for v in vs: byq[v[1]].append(v[0])
    for v1 in vs:
        for v2 in vs:
            for v3 in vs:
                base=v1[1]-v2[1]+v3[1]
                for dl in range(-4*(M-1),4*(M-1)+1):
                    q4=base-dl
                    for Y4 in byq.get(q4,()):
                        v4=(Y4,q4); s=v1[0]-v2[0]+v3[0]-Y4
                        hist[s]+=1
                        if s: continue
                        ident=(v1==v2 and v3==v4) or (v1==v4 and v2==v3)
                        sameY=(v1[0]==v2[0] and v3[0]==Y4) or (v1[0]==Y4 and v2[0]==v3[0])
                        if ident: c['i']+=1
                        elif sameY: c['ii']+=1
                        else: c['iii']+=1
nb=[hist[s] for s in range(-40,41,2) if s!=0]; mean=sum(nb)/len(nb)
print("S=%d h=2^%s B=%d vectors=%d blocks=%d"%(S,sys.argv[2],B,len(vecs),len(blocks)))
print("s=0: identical-vector diagonals %d, two-leg-Y diagonals %d, off-diagonal %d"%(c['i'],c['ii'],c['iii']))
print("mean at nonzero even |s|<=40: %.1f; ratios to it: (ii) %.2f, (iii) %.2f"%(mean,c['ii']/mean,c['iii']/mean))
