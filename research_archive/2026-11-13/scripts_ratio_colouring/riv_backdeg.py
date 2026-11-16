# Sanity check: R_IV^(4) back-degree b(u) = #{lambda : p_lambda | u}, odd u <= U.
import numpy as np, math, sys, time
t0=time.time()
U=int(sys.argv[1]) if len(sys.argv)>1 else 5_000_000
lams=[]
be=3
while be**3 <= 5*U+10:
    for al in range(1,be):
        if al%2==0 or math.gcd(al,be)!=1: continue
        d=be-al
        if (d & 3)!=0: continue   # v2(be-al) >= 2
        F=4*(al-2*be)**2+be*be
        g=math.gcd(F,d)
        q=al*F//g; p=(al*F+4*d*be*be)//g
        assert (al*F)%g==0 and (al*F+4*d*be*be)%g==0
        assert math.gcd(p,q)==1 and p%2==1 and q%2==1
        assert p*5 >= be**3, (al,be,p)
        lams.append((al,be,q,p))
    be+=2
S1=sum(1.0/l[3] for l in lams)
# tail estimate for S1 beyond: sum_{be>Bmax} 5(be+3)/(4 be^3) over odd be
print("lambdas:",len(lams),"partial S_IV=sum 1/p:",round(S1,5), "smallest edges:",sorted((l[2],l[3]) for l in lams)[:3])
b=np.zeros(U+1,dtype=np.int32)
for (al,be_,q,p) in lams:
    if p<=U:
        b[p::2*p]+=1   # odd multiples of p
odd=b[1::2]
print("U=",U,"#odd u:",odd.size,"mean b:",odd.mean(),"pred S_IV/2-ish:",S1/2*1.0)
mx=odd.max(); print("max b:",mx,"at u=",2*int(odd.argmax())+1)
for D in [1,2,3,4,5,6,8]:
    n=(odd>=D).sum(); print(" D=%d  #{b>=D}=%d  frac=%.3e  Markov bound frac<=%.3e"%(D,n,n/odd.size,odd.mean()/D))
print("time",round(time.time()-t0,1))
