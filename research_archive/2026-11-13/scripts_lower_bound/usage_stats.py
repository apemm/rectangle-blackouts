# sanity exploration: row-usage vectors of 45-degree corner-free one-per-column functions (one bishop class)
import sys, collections
from class_functions import run
h=int(sys.argv[1]); w=int(sys.argv[2]); cap=int(sys.argv[3])
res={}
for par in (0,1):
    c,sols,to,el=run(h,w,cap,par,25)
    uses=collections.Counter()
    for s in sols:
        u=[0]*(h+1)
        for y in s: u[y]+=1
        uses[tuple(u[1:])]+=1
    res[par]=uses
    print('par',par,'functions',c,'timeout',to,'distinct usage vectors',len(uses))
    # max usage of middle rows
    for k in range(1,h//2+1):
        mid=list(range(h//2-k+1,h//2+k+1))
        mx=max(sum(u[y-1] for y in mid) for u in uses)
        print('   max total usage of rows',mid[0],'..',mid[-1],':',mx,' (needed on average per class:',cap*len(mid)/2,')')
# complementary usage pairs
n=0
for u in res[0]:
    comp=tuple(cap-a for a in u)
    if comp in res[1]: n+=1
print('usage vectors of class 0 having a complementary class-1 vector:',n)
# for each row set, max over classes of usage: check whether max0(M)+max1(M) < cap*|M|
for k in range(1,h//2+1):
    mid=list(range(h//2-k+1,h//2+k+1))
    m0=max(sum(u[y-1] for y in mid) for u in res[0]); m1=max(sum(u[y-1] for y in mid) for u in res[1])
    print('rows',mid[0],'..',mid[-1],'max0+max1 =',m0+m1,'needed',cap*len(mid))
