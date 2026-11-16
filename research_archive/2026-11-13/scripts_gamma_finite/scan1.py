import sys, time
from bohr import build
from fractions import Fraction as Fr
T=int(sys.argv[1]); k=int(sys.argv[2]); M=int(sys.argv[3]); N=int(sys.argv[4])
t0=time.time()
for q in range(1,13):
  for p in range(1,10*q+1):
    if Fr(p,q).denominator!=q: continue
    res,g,info=build(T,k,Fr(p,q),M,N,10**15,secs=3)
    if res: print("SAT",T,k,p,q,M,N,info,flush=True)
    if time.time()-t0>50: print("time",p,q); sys.exit()
print("done %.1f"%(time.time()-t0))
