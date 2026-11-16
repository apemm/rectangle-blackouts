# realistic-p estimate: rigid layout, p>20h, each diagonal split into CH random classes; sampled X1 (per F) and X2 (per V) cross loads
import sys, random, time
from layout import isprime
def divs(n):
    out=[];d=1
    while d*d<=n:
        if n%d==0: out+=[d,n//d]
        d+=1
    return set(out)
h=int(sys.argv[1]); CH=int(sys.argv[2]); S=int(sys.argv[3]); rnd=random.Random(7)
A=(h+1)//2; K=h//2; p=20*h+1
while not isprime(p) or p%5 not in (2,3): p+=1
nu=0
while 2**nu*8<K: nu+=1
Q=2**nu; pinv=pow(p,-1,Q)
cls=[]
for T in range(-(h-1),h,2):
    s=(T-1)//2; L=[i for i in range(A) if 0<=i+s<K]
    parts=[[] for _ in range(CH)]
    for i in L: parts[rnd.randrange(CH)].append(i)
    for c in parts: cls.append((s,c))
byres={}
for ci,(s,c) in enumerate(cls): byres.setdefault(s%Q,[]).append(ci)
pos={}
for r,lst in byres.items():
    for k,ci in enumerate(lst): pos[ci]=(pinv*r)%Q+Q*k
pts={}
for ci,(s,c) in enumerate(cls):
    M=p*pos[ci]
    for i in c:
        x=4*(i+M); pts[(x,2*i+1)]=('o',ci); pts[(x,2*(i+s)+2)]=('e',ci)
minax=4*(p-h); t0=time.time()
F=[P for P,v in pts.items() if v[0]=='e']; V=[P for P,v in pts.items() if v[0]=='o' and P[1]%4==1 and P[1]>=5]
rnd.shuffle(F); rnd.shuffle(V)
x1=0
for (xF,yF) in F[:S]:
    cF=pts[(xF,yF)][1]
    for iG in range(2,A,4):
        yG=2*iG+1
        if yF+yG-1>h: break
        Mv=(yF-1)*(yG-1)//4
        if Mv+1<minax//2: continue
        for d in divs(Mv):
            Ssum=d+Mv//d
            if d*d>Mv or 2*Ssum<minax: continue
            for xG in (xF+2*Ssum,xF-2*Ssum):
                G=(xG,yG)
                if G in pts and pts[G][0]=='o' and pts[G][1]!=cF: x1+=1
x2=0
for (xV,yV) in V[:S]:
    cV=pts[(xV,yV)][1]
    for yG in range(yV+1,h+1,2):
        g=yG-yV; N=(yV-1)*g
        for a in range(1,N//minax+1):
            if a%4==0 or N%a: continue
            for sa in (a,-a):
                G=(xV+N//sa,yG)
                if G in pts and pts[G][0]=='e' and pts[G][1]!=cV: x2+=1
print(f"h={h} p={p} chi={CH} width/h^2={max(x for x,y in pts)/h/h:.0f} X1/F={x1/S:.4f} X2/V={x2/S:.4f} (V share of labels {len(V)/len(F):.2f}) {time.time()-t0:.1f}s")
