# SAT on bin model using only a chosen subset of shifts: mode 'tails' or 'exact' or 'all'
import sys, time, threading
import mpmath as mp
from bohr import shifts
from fractions import Fraction as Fr
from pysat.solvers import Cadical153
def solve(sh,M,N,k,secs=20):
    V=lambda j,s,c: ((j*M+s)*k+c)+1
    cl=set()
    for (lo,hi,r) in sh:
        f1=int(mp.floor(N*lo)); f2=int(mp.ceil(N*hi))
        for j in range(N):
            for t in range(f1,f2+1):
                for s in range(M):
                    a=(j,s); b=((j+t)%N,(s+r)%M)
                    if a==b: return None
                    cl.add((min(a,b),max(a,b)))
    so=Cadical153()
    for j in range(N):
        for s in range(M): so.add_clause([V(j,s,c) for c in range(k)])
    for (a,b) in cl:
        for c in range(k): so.add_clause([-V(a[0],a[1],c),-V(b[0],b[1],c)])
    so.add_clause([V(0,0,0)])
    tm=threading.Timer(secs,lambda: so.interrupt()); tm.start()
    r=so.solve_limited(expect_interrupt=True); tm.cancel(); so.delete(); return r,len(cl)
if __name__=="__main__":
    T,k,a,M,N,B,mode=int(sys.argv[1]),int(sys.argv[2]),Fr(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(float(sys.argv[6])),sys.argv[7]
    sh,ex,nt,rad=shifts(T,a,M,B)
    if mode=='tails': sh=[x for x in sh if x[0]!=x[1]]
    if mode=='exact': sh=[x for x in sh if x[0]==x[1]]
    print(mode,len(sh),solve(sh,M,N,k))
