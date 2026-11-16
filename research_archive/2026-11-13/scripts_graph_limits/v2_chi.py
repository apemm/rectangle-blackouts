# Re-check lower bounds chi(Cay([0,n), D)) > k with two SAT solvers. Clique colours fixed (valid symmetry breaking).
import sys, time, threading
from math import isqrt
from pysat.solvers import Cadical153, Glucose4
def dist(T,B):
    s=set()
    for d in range(-B,B+1):
        if d==0: continue
        Q=20*d*d+4*T*d+T*T; L=isqrt(Q)
        if L*L==Q: s.add(abs(d))
    return sorted(s)
def col(n,D,k,clique,S,secs):
    s=S(); v=lambda x,c: x*k+c+1
    for x in range(n): s.add_clause([v(x,c) for c in range(k)])
    for x in range(n):
        for d in D:
            if x+d<n:
                for c in range(k): s.add_clause([-v(x,c),-v(x+d,c)])
    for c,x in enumerate(clique): s.add_clause([v(x,c)])
    t=threading.Timer(secs, lambda: s.interrupt()); t.start()
    r=s.solve_limited(expect_interrupt=True); t.cancel(); s.delete(); return r
T,n,k,secs=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),float(sys.argv[4])
cl=[int(x) for x in sys.argv[5].split(',')] if len(sys.argv)>5 else [0]
D=[d for d in dist(T,n) if d<n]
for x in cl:
    for y in cl:
        assert x==y or abs(x-y) in D
t0=time.time()
for S in (Cadical153, Glucose4):
    print("T",T,"n",n,"|D|",len(D),"k",k,S.__name__,"->",col(n,D,k,cl,S,secs),"t=%.1f"%(time.time()-t0),flush=True)
