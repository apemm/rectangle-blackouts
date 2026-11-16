import random, numpy as np
from collections import Counter
from board import shapes, mixed_scan
h=23; Wd=500; S=shapes(h)
cnt=Counter()
for trial in range(8):
    rnd=random.Random(trial)
    blk=np.zeros((Wd,h+2),dtype=np.int64)
    for x in range(Wd):
        if x%4: blk[x,1]=1
        else:
            n=x//4
            ev=[y for y in range(2,h+1,2) if (y-2*n-2)%8==0]
            od=list(range(3,h+1,2))
            blk[x,rnd.choice(ev)]=1; blk[x,rnd.choice(od)]=1
    pts=np.argwhere(blk>0); px=pts[:,0].astype(np.int64); py=pts[:,1].astype(np.int64)
    M=mixed_scan(blk,h,Wd,S,px,py,(h*h)//4+1)
    seen=set()
    for (ax,ay,bx,by,cx,cy,dx,dy) in M:
        sup=frozenset([(ax,ay),(bx,by),(cx,cy),(dx,dy)])
        if sup in seen: continue
        seen.add(sup)
        sh=lambda x: (x%4!=0)
        if not sh(ax) and not sh(bx) and (sh(cx)+sh(dx))==1:
            yD = dy if sh(cx) else cy
            cnt[(ay%2,by%2,yD%8)]+=1
print('M1C (parA,parB,yD mod 8):',sorted(cnt.items()))
