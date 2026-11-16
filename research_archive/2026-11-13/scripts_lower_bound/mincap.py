# sanity exploration: smallest row-usage cap for which a class function exists on a window of width w
import sys, time
from class_functions import run
h=int(sys.argv[1]); w=int(sys.argv[2]); tl=float(sys.argv[3])
lo=w//h  # uniform usage
t0=time.time()
for cap in range(lo, w//2+2):
    c,sols,to,el=run(h,w,cap,0,min(8.0,tl-(time.time()-t0)))
    print('h',h,'w',w,'cap',cap,'(cap*h/w = %.2f)'%(cap*h/w),'count',c,'timeout',to)
    if c>0:
        for s in sols[:3]: print('   ',' '.join(str(y) for y in s))
        break
    if time.time()-t0>tl: break
