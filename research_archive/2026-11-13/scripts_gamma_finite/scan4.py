import sys, time
from bohr import build
from fractions import Fraction as Fr
T=int(sys.argv[1]); k=int(sys.argv[2]); N=int(sys.argv[3]); Qm=int(sys.argv[4]); Ms=list(map(int,sys.argv[5].split(',')))
t0=time.time()
alphas=sorted({Fr(p,q) for q in range(1,Qm+1) for p in range(1,10*q+1)}, key=lambda a:(a.denominator,a))
for M in Ms:
  hits=[]
  for a in alphas:
    res,g,info=build(T,k,a,M,N,10**15,secs=1)
    if res: hits.append(a); print("SAT",T,k,a,M,N,info,flush=True); break
    if time.time()-t0>55: print("time",M,a); sys.exit()
  print("M",M,"done %.1f"%(time.time()-t0),flush=True)
