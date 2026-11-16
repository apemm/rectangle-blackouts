import sys, time, threading
from math import isqrt
from pysat.solvers import Cadical153
T,k,n,secs=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),float(sys.argv[4])
D=sorted({abs(d) for d in range(-n,n+1) if d and isqrt(20*d*d+4*T*d+T*T)**2==20*d*d+4*T*d+T*T and abs(d)<n})
s=Cadical153(); v=lambda x,c: x*k+c+1
for x in range(n): s.add_clause([v(x,c) for c in range(k)])
for x in range(n):
    for d in D:
        if x+d<n:
            for c in range(k): s.add_clause([-v(x,c),-v(x+d,c)])
s.add_clause([v(0,0)])
tm=threading.Timer(secs,lambda: s.interrupt()); tm.start(); t0=time.time()
r=s.solve_limited(expect_interrupt=True); tm.cancel()
print(T,k,n,len(D),D[:30],r,"%.1fs"%(time.time()-t0))
if r:
    m=s.get_model(); col=[next(c for c in range(k) if m[x*k+c]>0) for x in range(n)]
    open("col_%d_%d_%d.txt"%(T,k,n),"w").write(''.join(map(str,col)))
