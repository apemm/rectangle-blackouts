# chi test of Cay([0,n), D) for explicit D, k colours; prints SAT/UNSAT and a periodic check
import sys, threading
from pysat.solvers import Cadical153
def col(n,D,k,secs=20,fix0=True):
    s=Cadical153(); v=lambda x,c: x*k+c+1
    for x in range(n): s.add_clause([v(x,c) for c in range(k)])
    for x in range(n):
        for d in D:
            if x+d<n:
                for c in range(k): s.add_clause([-v(x,c),-v(x+d,c)])
    if fix0: s.add_clause([v(0,0)])
    t=threading.Timer(secs, lambda: s.interrupt()); t.start()
    r=s.solve_limited(expect_interrupt=True); t.cancel()
    m=None
    if r:
        mod=s.get_model(); m=[next(c for c in range(k) if mod[x*k+c]>0) for x in range(n)]
    s.delete(); return r,m
if __name__=="__main__":
    D=[int(x) for x in sys.argv[1].split(',')]; n=int(sys.argv[2]); k=int(sys.argv[3])
    r,m=col(n,D,k)
    print(D,n,k,r)
    if m: print(''.join(map(str,m[:200])))
