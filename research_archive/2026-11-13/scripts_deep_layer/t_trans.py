import numpy as np, sys
from driver import analyse
from board import shapes
def board(h, Wd, x0, left, right):
    kind=np.zeros((Wd,h+2),dtype=np.int64)
    for x in range(Wd):
        f = left if x < x0 else right
        r = f(x)
        if r is not None: kind[x,r] = 1 if r==1 else 2
    return kind
for h in (17,21,25):
    W=(h*h)//4+1; Wd=4*W+40; x0=(Wd//8)*4; S=shapes(h)
    odd=[r for r in range(h//2+2,h+1) if r%2==1]
    out=[]
    for R in odd:
        for R2 in odd:
            if R2<=R: continue
            k=board(h,Wd,x0,lambda x: 1 if x%4 else R, lambda x: 1 if x%4 else R2)
            res,ex=analyse(h,k,S,only_filler=False)
            out.append((R,R2,sum(res.values())))
    # T25-like junction: row 1 everywhere on the left, Sea(1,R) on the right
    t25=[]
    for R in odd+[r for r in range(h//2+2,h+1) if r%2==0]:
        k=board(h,Wd,x0,lambda x: 1, lambda x: 1 if x%4 else R)
        res,ex=analyse(h,k,S,only_filler=False)
        t25.append((R,sum(res.values()),dict(res) if sum(res.values())<6 else ''))
    print(h,'R->R2 junctions',out); print(h,'row1->Sea(1,R) junctions',t25)
