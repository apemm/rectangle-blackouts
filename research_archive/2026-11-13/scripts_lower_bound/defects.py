# sanity exploration: for class functions phi on [1,w] (row cap), the number of x with phi(x+2) != phi(x)
import sys, collections
from class_functions import run
h=int(sys.argv[1]); w=int(sys.argv[2]); cap=int(sys.argv[3])
c,sols,to,el=run(h,w,cap,0,30)
hist=collections.Counter()
worst=None
for s in sols:
    d=sum(1 for i in range(w-2) if s[i]!=s[i+2])
    hist[d]+=1
    if worst is None or d>worst[0]: worst=(d,s)
print('h',h,'w',w,'cap',cap,'functions',c,'timeout',to)
print('histogram of #defects (positions x in 1..w-2 with phi(x+2)!=phi(x)):',sorted(hist.items()))
print('max defects',worst[0],'of',w-2,'example',worst[1])
