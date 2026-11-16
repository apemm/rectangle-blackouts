import sys, time
from step import dist
from pysat.solvers import Cadical153
T,k=int(sys.argv[1]),int(sys.argv[2])
for n in map(int,sys.argv[3:]):
    D=dist(T,n); s=Cadical153(); v=lambda x,c: x*k+c+1
    for x in range(n): s.add_clause([v(x,c) for c in range(k)])
    for x in range(n):
        for d in D:
            if x+d<n:
                for c in range(k): s.add_clause([-v(x,c),-v(x+d,c)])
    s.add_clause([v(0,0)])
    t0=time.time(); r=s.solve(); print(T,k,n,len(D),r,"%.1fs"%(time.time()-t0),flush=True); s.delete()
