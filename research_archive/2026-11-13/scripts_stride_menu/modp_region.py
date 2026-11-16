"""One stride region: every label (i,j) placed in some block; each block holds a subset
of one residue progression of one diagonal; x = mu t + B_c, B_c = lambda*(first slot) mod p, B_c = 0 mod 4.
Check: every tilted right angle has an even vertex and an even end; report types."""
import random, math, sys
from collections import defaultdict
def isprime(n): return n>1 and all(n%q for q in range(2,int(n**.5)+1))
h=int(sys.argv[1]); mu=int(sys.argv[2]); nu=int(sys.argv[3]); seed=int(sys.argv[4])
random.seed(seed)
A=(h+1)//2; K=h//2; D=mu*mu+4*nu*nu
p=max(10*h, D*h)+1
while not isprime(p): p+=1
lam = mu*pow(nu,-1,p) % p
blocks=[]
for s in range(-(A-1),K):
    lo=max(0,-s); hi=min(A,K-s)
    for r in range(nu):
        prog=list(range(lo+r,hi,nu))
        if not prog: continue
        # random split into 1..3 classes
        nc=random.randint(1,3); cls=[[] for _ in range(nc)]
        for i in prog: cls[random.randrange(nc)].append(i)
        for c in cls:
            if c: blocks.append((s,lo+r,c))
pts=[]  # (x,y,parity,block)
for b,(s,first,c) in enumerate(blocks):
    base=4*p*b*2
    off=(lam*first)%p
    while off%4: off+=p
    B=base+off
    for i in c:
        t=(i-first)//nu
        x=mu*t+B
        assert (x-lam*i)%p==0
        pts.append((x,2*i+1,'O',b)); pts.append((x,2*(i+s)+2,'E',b))
types=defaultdict(int); bad=0
for v in pts:
    dirs=defaultdict(list)
    for w in pts:
        if w is v: continue
        dx,dy=w[0]-v[0],w[1]-v[1]
        if dx==0 or dy==0: continue
        g=math.gcd(dx,dy); key=(dx//g,dy//g)
        if key[0]<0: key=(-key[0],-key[1])
        dirs[key].append(w)
    for (a,bq),L in dirs.items():
        perp=(bq,-a) if bq>0 else (-bq,a)
        if perp in dirs and (a,bq)<perp:
            for w1 in L:
                for w2 in dirs[perp]:
                    ends=''.join(sorted(w1[2]+w2[2]))
                    same=('in' if w1[3]==v[3] else 'x')+('in' if w2[3]==v[3] else 'x')
                    types[(v[2],ends,same)]+=1
                    if v[2]=='O' or ends=='OO': bad+=1
print("h",h,"stride",(mu,nu),"p",p,"blocks",len(blocks),"points",len(pts))
print("types (vertex, ends, in-block flags):",dict(types))
print("angles violating 'even vertex and even end':",bad)
