# For T = T0*p: chi of the window graph using (i) only new distances (p not dividing d), (ii) new + hub, (iii) all.
import sys, time
from step import dist
from pysat.solvers import Glucose4
import threading
def colorable(n,D,k,secs=25):
    s=Glucose4(); v=lambda x,c: x*k+c+1
    for x in range(n): s.add_clause([v(x,c) for c in range(k)])
    for x in range(n):
        for d in D:
            if x+d<n:
                for c in range(k): s.add_clause([-v(x,c),-v(x+d,c)])
    s.add_clause([v(0,0)])
    t=threading.Timer(secs, lambda: s.interrupt()); t.start()
    r=s.solve_limited(expect_interrupt=True); t.cancel(); s.delete(); return r
T,p,n=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
D=dist(T,n); new=[d for d in D if d%p]; hub=T//5 if T%5==0 else None
for name,DD in [("new",new),("new+hub",sorted(set(new)|({hub} if hub and hub<n else set()))),("all",D)]:
    res=[]
    for k in range(2,9):
        r=colorable(n,DD,k)
        res.append((k,r))
        if r: break
    print(T,p,n,name,len(DD),DD[:10],res,flush=True)
