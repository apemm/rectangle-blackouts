# sanity check: maximal corner-triple-free all-double windows (condition N only), h = 8, a slice of the 35 balanced partitions
import sys, itertools, time
from explore_windows import run
h=8
parts=[A for A in itertools.combinations(range(1,h+1),4) if 1 in A]
lo=int(sys.argv[1]); hi=int(sys.argv[2])
t0=time.time()
for i in range(lo,min(hi,len(parts))):
    A=parts[i]
    best,nodes,to,el,q=run(h,A,'N',50-(time.time()-t0))
    print(i,'A',A,'maxwidth',best['w'],'count',best['count'],'nodes',nodes,'timeout',to,'sec',round(el,1),flush=True)
    if time.time()-t0>50: print('STOP'); break
print('total sec',round(time.time()-t0,1))
