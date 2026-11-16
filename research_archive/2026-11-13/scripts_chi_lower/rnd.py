# Compare: chi of window graph [0,n) for random distance sets of the same size and range as D_T ∩ [1,n)
import sys, random, threading
from pysat.solvers import Glucose4
def colorable(n,D,k,secs):
    s=Glucose4(); v=lambda x,c: x*k+c+1
    for x in range(n): s.add_clause([v(x,c) for c in range(k)])
    for x in range(n):
        for d in D:
            if x+d<n:
                for c in range(k): s.add_clause([-v(x,c),-v(x+d,c)])
    s.add_clause([v(0,0)])
    t=threading.Timer(secs, lambda: s.interrupt()); t.start()
    r=s.solve_limited(expect_interrupt=True); t.cancel(); s.delete(); return r
if __name__=="__main__":
 n,m,lo,trials,secs=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),float(sys.argv[5])
 random.seed(1)
 out=[]
 for _ in range(trials):
    D=sorted(random.sample(range(lo,n),m))
    chi=None
    for k in range(3,10):
        r=colorable(n,D,k,secs)
        if r is None: chi=">=%d?"%k; break
        if r: chi=k; break
    out.append(chi)
 print("n",n,"m",m,"range",lo,"chis",out)
