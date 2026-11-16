import sys, time
from bohr import build
from fractions import Fraction as Fr
T=int(sys.argv[1]); k=int(sys.argv[2]); M=int(sys.argv[3]); N=int(sys.argv[4]); base=int(sys.argv[5]); qmax=int(sys.argv[6])
t0=time.time(); seen=set(); cnt=0
for q0 in range(1,qmax+1):
  q=base*q0
  for p in range(1,10*q+1):
    a=Fr(p,q)
    if a in seen: continue
    seen.add(a); cnt+=1
    res,g,info=build(T,k,a,M,N,10**15,secs=2)
    if res: print("SAT",T,k,a,M,N,info,flush=True)
    if time.time()-t0>55: print("time",a,cnt); sys.exit()
print("done %.1f"%(time.time()-t0),cnt)
