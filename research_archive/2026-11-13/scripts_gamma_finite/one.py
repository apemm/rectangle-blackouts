import sys, time
from bohr import build
from fractions import Fraction as Fr
T=int(sys.argv[1]); k=int(sys.argv[2]); a=Fr(sys.argv[3]); M=int(sys.argv[4]); N=int(sys.argv[5]); B=int(float(sys.argv[6])); secs=float(sys.argv[7])
t0=time.time()
res,g,info=build(T,k,a,M,N,B,secs=secs)
print(T,k,a,M,N,B,res,info,"%.1fs"%(time.time()-t0))
