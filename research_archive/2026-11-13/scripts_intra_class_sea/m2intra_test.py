# sampled cross-class M2c: B,D deep label points same parity, A,C shallow. Uses tau^2+tau z+e(u2+e)=0, tau=Delta-n1, n1 z=-e u2
import sys, time, random
from layout import build
def divs(n):
    out=[];d=1
    while d*d<=n:
        if n%d==0: out+=[d,n//d]
        d+=1
    return out
h=int(sys.argv[1]); mode=sys.argv[2]; pmin=int(sys.argv[3]); S=int(sys.argv[4])
p,Q,cls,pos,pts=build(h,mode,pmin=pmin)
keys=list(pts.keys()); random.Random(5).shuffle(keys)
minax=0; cnt={'ee':0,'oo':0}; t0=time.time(); done=0
for B in keys[:S]:
    xB,yB=B; kB,cB,iB=pts[B]; u2=yB-1
    if u2<=0: continue
    done+=1
    for e in range(1,h):
        if yB+2*e>h: break
        Nn=e*(u2+e)
        for tau0 in divs(Nn):
            if tau0<minax-2*h: continue
            for tau in (tau0,-tau0):
                z=-(tau+Nn//tau)
                if z==0 or (e*u2)%z: continue
                n1=-(e*u2)//z
                if n1==0: continue
                Dl=tau+n1
                if abs(Dl)<minax: continue
                if z%4==0 or (2*n1-z)%4==0: continue
                if yB+e>h: continue
                if n1*((Dl-n1)**2+e*e)!=e*u2*(Dl-2*n1): continue
                D=(xB+Dl,yB+2*e)
                if D in pts and pts[D][0]==kB and pts[D][1]==cB: cnt['ee' if kB=='e' else 'oo']+=1
print(f"h={h} {mode} p={p} sampled B={done} M2c cross {cnt} per sampled B {sum(cnt.values())/done:.4f} {time.time()-t0:.1f}s")
