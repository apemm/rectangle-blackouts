# sanity exploration: class functions on a window of width w with every row used at most cap times
import sys
from class_functions import run
h=int(sys.argv[1]); mult=int(sys.argv[2]); extra=int(sys.argv[3]); tl=float(sys.argv[4])
w=mult*h; cap=2*mult+extra   # (2/h)*w = 2*mult
c,sols,to,el=run(h,w,cap,0,tl)
print('h',h,'w',w,'cap',cap,'count',c,'timeout',to,'sec',round(el,1))
for s in sols[:6]:
    print('  ',' '.join(str(y) for y in s))
