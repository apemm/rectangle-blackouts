import sys
from board import *
from collections import Counter
h=int(sys.argv[1]); mode=sys.argv[2]
margin=2*Wh(h)+8; base=margin-margin%4; mstar=(base//4+(h-1)//2)%2
def fill(i,x):
    if mode=='one': return h
    if mode=='two': return h if (x//4)%2!=mstar else h-2
cols,labels,b=build(h,1,set(),fill,margin,nslots=8)
fatal,parked,bm=classify_triples(cols,h)
print('fatal sea-only',len(fatal))
c=Counter()
for w,ks in parked.items():
    if len(ks)>1:
        c[len(ks)]+=1
print('V3 multiplicities',dict(c))
n=0
for w,ks in parked.items():
    if len(ks)>1 and n<3:
        n+=1; print(w,[sorted(k) for k in ks])
mq,bm=mixed_quadruples(cols,h); print('mq sea-only',len(mq))
rp,bm=rival_pairs(cols,h); print('rp sea-only',len(rp))
