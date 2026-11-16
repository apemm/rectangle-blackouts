import random, numpy as np
from collections import Counter
from board import shapes, mixed_scan
h=21; Wd=500; S=shapes(h)
cnt=Counter(); X1=Counter()
for trial in range(6):
    rnd=random.Random(trial)
    blk=np.zeros((Wd,h+2),dtype=np.int64)
    for x in range(Wd):
        if x%4: blk[x,1]=1
        else:
            for r in rnd.sample(range(2,h+1),2): blk[x,r]=1
    pts=np.argwhere(blk>0); px=pts[:,0].astype(np.int64); py=pts[:,1].astype(np.int64)
    M=mixed_scan(blk,h,Wd,S,px,py,(h*h)//4+1)
    seen=set()
    for (ax,ay,bx,by,cx,cy,dx,dy) in M:
        sup=frozenset([(ax,ay),(bx,by),(cx,cy),(dx,dy)])
        if sup in seen: continue
        seen.add(sup)
        sh=lambda x,y: (x%4!=0)
        sA,sB,sC,sD=sh(ax,ay),sh(bx,by),sh(cx,cy),sh(dx,dy)
        if not sA and not sB and (sC+sD)==1:
            yD = dy if sC else cy
            cnt[yD%8]+=1
print('M1C deep-D row mod 8:',sorted(cnt.items()))
