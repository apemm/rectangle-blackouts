# Sanity check of Lemma 1 (AP form of T2 (7) / sharper (2)):
# ratio R = [ (q/h) * sum_{t<=h, t=t0 mod q} F(t) ] / [ (1/h) * sum_{t<=h} F(t) ]
# should be <= C tau(q)^C uniformly in t0, q <= sqrt(h).
import numpy as np, math, random, time
t0_=time.time()
h=300000
N=8*h+10
tau=np.zeros(N+1,dtype=np.int64)
for d in range(1,N+1):
    tau[d::d]+=1
def T(arr): return tau[np.abs(arr)]
spf=np.zeros(N+1,dtype=np.int64)
for p in range(2,int(N**0.5)+1):
    if spf[p]==0:
        m=spf[p*p::p]; m[m==0]=p; spf[p*p::p]=m
def tsq1(n):
    n=abs(int(n)); r=1
    while n>1:
        p=spf[n] or n; a=0
        while n%p==0: n//=p; a+=1
        r*=2*a+1
    return r
def TS(arr): return np.array([tsq1(x) for x in arr],dtype=np.int64)
t=np.arange(1,h+1)
c1,c2,c3=12345,-777,40001   # constants O(h)
forms=[("tau(2t+c1)^2*tau((2t+c2)^2)", lambda t: T(2*t+c1)**2*TS(2*t+c2)),
       ("tau(2t+c1)^2*tau(2t+c2)*tau(2t+T+c3)", lambda t: T(2*t+c1)**2*T(2*t+c2)*T(4*t+c3)),
       ("tau((2t+c1)(2t+c2))^2", lambda t: T(2*t+c1)**2*T(2*t+c2)**2)]  # upper proxy
rng=random.Random(1)
for name,F in forms:
    vals=F(t).astype(np.float64)
    base=vals.mean()
    worst=[]
    for q in [3,5,7,9,15,30,60,105,210,420,511]:
        best=0;arg=None
        cand=list(range(q)) if q<=60 else rng.sample(range(q),40)
        # include residues where some form is divisible by q
        for c in (c1,c2,c3):
            for a in (2,4):
                for r in range(q):
                    if (a*r+c)%q==0: cand.append(r);break
        for r in set(cand):
            sub=vals[(t%q)==r]
            if len(sub)==0: continue
            R=sub.mean()/base
            if R>best: best=R;arg=r
        worst.append((q,int(tau[q]),round(best,2),arg))
    print(name,"mean",round(base,1)); print("  (q,tau(q),max ratio,residue):",worst)
print("time",round(time.time()-t0_,1))
