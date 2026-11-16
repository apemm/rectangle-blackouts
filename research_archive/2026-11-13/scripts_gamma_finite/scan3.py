# for each k, find whether any alpha=p/q (q<=Q) gives a colouring; report first hit
import sys, time
from bohr import build
from fractions import Fraction as Fr
T=int(sys.argv[1]); M=int(sys.argv[2]); N=int(sys.argv[3]); Qm=int(sys.argv[4]); ks=list(map(int,sys.argv[5].split(',')))
t0=time.time()
alphas=sorted({Fr(p,q) for q in range(1,Qm+1) for p in range(1,10*q+1)}, key=lambda a:(a.denominator,a))
for k in ks:
  hit=None
  for a in alphas:
    res,g,info=build(T,k,a,M,N,10**15,secs=1)
    if res: hit=(a,info); break
    if time.time()-t0>55: print("time"); sys.exit()
  print("k",k,"hit",hit,"%.1f"%(time.time()-t0),flush=True)
