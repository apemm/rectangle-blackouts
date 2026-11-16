import sys
from board import *
h=int(sys.argv[1])
margin=2*Wh(h)+8; base=margin-margin%4; mstar=(base//4+(h-1)//2)%2
best=[]
for rho in range(2,h):
    fill=lambda i,x: h if (x//4)%2!=mstar else rho
    cols,labels,b=build(h,1,set(),fill,margin,nslots=8)
    fatal,parked,bm=classify_triples(cols,h)
    # empty-column convention irrelevant here (no empty columns)
    v3=sum(1 for w,ks in parked.items() if len(ks)>1)
    mq,bm=mixed_quadruples(cols,h); rp,bm=rival_pairs(cols,h)
    best.append((rho,len(fatal),v3,len(mq),len(rp)))
print('h',h,[b for b in best])
