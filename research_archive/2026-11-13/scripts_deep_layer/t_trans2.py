import numpy as np
from driver import analyse
from board import shapes
from t_trans import board
for h in (17,21,25,29):
    W=(h*h)//4+1; Wd=4*W+40; x0=(Wd//8)*4; S=shapes(h)
    res_list=[]
    for g in [r for r in range(h//2+2,h+1) if r%2==0]:
        for R in [r for r in range(h//2+2,h+1) if r%2==1]:
            k=board(h,Wd,x0,lambda x: 1 if x%4 else g, lambda x: 1 if x%4 else R)
            r1,_=analyse(h,k,S,only_filler=False)
            k=board(h,Wd,x0,lambda x: 1 if x%4 else R, lambda x: 1 if x%4 else g)
            r2,_=analyse(h,k,S,only_filler=False)
            res_list.append((g,R,sum(r1.values()),sum(r2.values())))
    print(h,[t for t in res_list])
