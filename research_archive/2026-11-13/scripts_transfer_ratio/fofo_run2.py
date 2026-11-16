import sys,os,time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fofo_u import run
t0=time.time()
for (u,H,iota,res) in [(1,5000,1,8),(1,5000,1,24),(3,5000,1,8),(3,5000,1,24)]:
    Y=H-24
    while (Y-(2*iota+1))%64!=res: Y-=1
    hs=run(u,H,iota,32,Y)
    print("u",u,"H",H,"Y",Y,"depth res",res,"hits",len(hs),"ratio ok",all(h[5] for h in hs),"a odd b even",all(h[6] for h in hs),"2u<m<4u",all(h[7] for h in hs),"v2(A)-beta",sorted(set(h[8] for h in hs)),"t=",sorted(set(h[2] for h in hs))[:6],"shapes",sorted(set((h[3],h[4]) for h in hs))[:6], round(time.time()-t0,1),"s",flush=True)
