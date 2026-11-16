import sys
from board import *
from collections import Counter
for h in map(int,sys.argv[1].split(',')):
    margin=2*Wh(h)+8; base=margin-margin%4; mstar=(base//4+(h-1)//2)%2
    res=[]
    for rho in range(3,h,2):
        if (rho-h-2)%4: continue
        fill=lambda i,x: h if (x//4)%2!=mstar else rho
        cols,labels,b=build(h,1,set(),fill,margin,nslots=8)
        fatal,parked,bm=classify_triples(cols,h)
        v3=sum(1 for w,ks in parked.items() if len(ks)>1)
        npark=sum(len(ks) for ks in parked.values())
        mq,bm=mixed_quadruples(cols,h); rp,bm=rival_pairs(cols,h)
        res.append((rho,len(fatal),v3,len(mq),len(rp),npark))
    print('h',h,'(rho, fatal, V3, mq, rp, parked):',res)
