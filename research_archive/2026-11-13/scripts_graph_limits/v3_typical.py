# chi(G_T(h)) at the actual height (typical regime h ~ c|T|), exact definitions; SAT with per-call time limit.
import sys, time, threading
from math import isqrt
from pysat.solvers import Glucose4
def GT(T,h):
    A=(h+1)//2; K=h//2; s=(T-1)//2
    lo=max(0,-s); hi=min(A,K-s); n=hi-lo
    D=set()
    for d in range(-(n-1),n):
        if d==0: continue
        Q=20*d*d+4*T*d+T*T; L=isqrt(Q)
        if L*L==Q and L<h: D.add(abs(d))
    return n,sorted(D)
def col(n,D,k,secs):
    s=Glucose4(); v=lambda x,c: x*k+c+1
    for x in range(n): s.add_clause([v(x,c) for c in range(k)])
    for x in range(n):
        for d in D:
            if x+d>=n: break
            for c in range(k): s.add_clause([-v(x,c),-v(x+d,c)])
    s.add_clause([v(0,0)])
    t=threading.Timer(secs, lambda: s.interrupt()); t.start()
    r=s.solve_limited(expect_interrupt=True); t.cancel(); s.delete(); return r
t0=time.time()
secs=float(sys.argv[1])
for arg in sys.argv[2:]:
    T,c=arg.split(':'); T=int(T); h=int(float(c)*abs(T))
    n,D=GT(T,h)
    res=[]
    for k in range(2,9):
        if not D: res=[(1,True)]; break
        r=col(n,D,k,secs); res.append((k,r))
        if r is not False: break
    print("T",T,"h",h,"n",n,"k_T",len(D),"->",res,"t=%.1f"%(time.time()-t0),flush=True)
    if time.time()-t0>50: break
