# sanity exploration: 45-degree corner-free one-per-column functions on long windows (no row cap)
import sys, collections, random
from class_functions import run
h=int(sys.argv[1]); 
for w in [int(t) for t in sys.argv[2].split(',')]:
    c,sols,to,el=run(h,w,10**9,0,25)
    print('h',h,'w',w,'count',c,'timeout',to,'sec',round(el,1))
random.seed(3)
for s in random.sample(sols,min(14,len(sols))):
    print('  ',''.join(str(y) for y in s))
# statistic: number of distinct rows used, and the set of (phi(x),phi(x+1)) transitions
