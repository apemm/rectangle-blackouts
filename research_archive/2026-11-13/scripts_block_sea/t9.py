import sys
from board import *
for h in map(int,sys.argv[1].split(',')):
    margin=2*Wh(h)+8; res=[]
    for r in range(2,h+1):
        cols,labels,b=build(h,1,set(),lambda i,x:r,margin,nslots=8)
        fatal,parked,bm=classify_triples(cols,h)
        npark=sum(len(k) for k in parked.values())
        mq,bm=mixed_quadruples(cols,h); rp,bm=rival_pairs(cols,h)
        res.append((r,len(fatal),npark,len(mq),len(rp)))
    print('h',h,'(r, fatal, parked, mq, rp):',res)
