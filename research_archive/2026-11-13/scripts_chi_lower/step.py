# Is Cay([0,n), D_T^inf ∩ [1,n)) k-colourable?  Usage: py step.py T n k secs
import sys, time, threading
from math import isqrt
from pysat.solvers import Cadical153, Glucose4
def dist(T,n):
    s=set()
    for d in range(-n,n+1):
        if d==0: continue
        Q=20*d*d+4*T*d+T*T; L=isqrt(Q)
        if L*L==Q: s.add(abs(d))
    return sorted(x for x in s if x<n)
def clique(n,D):
    # greedy max clique among small vertices (for symmetry breaking)
    Ds=set(D); best=[0]
    import itertools
    V=list(range(min(n,400)))
    def ext(cl,cand):
        nonlocal best
        if len(cl)>len(best): best=cl[:]
        for i,v in enumerate(cand):
            if len(cl)+len(cand)-i<=len(best): return
            ext(cl+[v],[u for u in cand[i+1:] if abs(u-v) in Ds])
    ext([0],[u for u in V if u in Ds])
    return best
def col(n,D,k,cl,secs):
    s=Glucose4(); v=lambda x,c: x*k+c+1
    for x in range(n): s.add_clause([v(x,c) for c in range(k)])
    for x in range(n):
        for d in D:
            if x+d<n:
                for c in range(k): s.add_clause([-v(x,c),-v(x+d,c)])
    for c,x in enumerate(cl[:k]): s.add_clause([v(x,c)])
    t=threading.Timer(secs, lambda: s.interrupt()); t.start()
    r=s.solve_limited(expect_interrupt=True); t.cancel(); s.delete(); return r
if __name__=="__main__":
  T,n,k,secs=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),float(sys.argv[4])
  D=dist(T,n); cl=clique(n,D)
  t0=time.time(); r=col(n,D,k,cl,secs)
  print("T",T,"n",n,"|D|",len(D),"D[:12]",D[:12],"clique",cl,"k",k,"->",r,"t=%.1f"%(time.time()-t0))
