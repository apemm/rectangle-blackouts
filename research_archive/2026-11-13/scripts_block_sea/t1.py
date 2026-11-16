import sys, time
from board import *
h=int(sys.argv[1]); T=int(sys.argv[2]); slots=set(map(int,sys.argv[3].split(',')))
t0=time.time()
cols,labels,base=build(h,T,slots,lambda i,x:None,2*Wh(h)+8)
fatal,parked,bm=classify_triples(cols,h)
for kind,key,Wp in fatal:
    tags=tagset(key,bm)
    if any('O' in t or 'E' in t for t in tags):
        print(kind,sorted(key),'W=',Wp,tags)
mq,bm=mixed_quadruples(cols,h)
for sup,(A,B,C,D) in mq:
    tags=tagset(sup,bm)
    if any('O' in t or 'E' in t for t in tags):
        print('MQ',A,B,C,D,tags)
rp,bm=rival_pairs(cols,h)
for C,D,j in rp: print('RP',C,D,j,bm[C],bm[D])
print('time',time.time()-t0)
