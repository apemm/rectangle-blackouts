import sys, time
from math import isqrt
from layout import build
def v2(n):
    n=abs(n);c=0
    while n%2==0: n//=2;c+=1
    return c
def divs(n):
    out=[];d=1
    while d*d<=n:
        if n%d==0: out+=[d,n//d]
        d+=1
    return set(out)
h=int(sys.argv[1]); mode=sys.argv[2]; pmin=int(sys.argv[3]) if len(sys.argv)>3 else None
t0=time.time()
p,Q,cls,pos,pts=build(h,mode,pmin=pmin)
nlab=sum(len(c) for s,c in cls)
print(f"h={h} mode={mode} p={p} 2^nu={Q} classes={len(cls)} labels={nlab} build {time.time()-t0:.1f}s")
minax=4*(p-h)
# M2a
fl={}
for dy in range(2,h,2):
    sq=dy*dy; fl[dy]=[f for f in divs(sq) if (sq//f-f)%2==0 and (sq//f-f)//2>=minax and ((sq//f-f)//2)%4==0]
m2a={'ee':0,'oo':0}; hv={}
for (xC,yC),(kC,cC,iC) in pts.items():
    for dy,lst in fl.items():
        yD=yC+dy
        if yD>h: break
        for f in lst:
            ax=(dy*dy//f-f)//2
            for xD in (xC+ax,xC-ax):
                D=(xD,yD)
                if D not in pts: continue
                kD,cD,iD=pts[D]
                if kD!=kC or cD==cC: continue
                L=ax+f; s2=xC+xD-L
                if s2%2: continue
                xA=s2//2; xB=xA+L
                if xA%4==0 or xB%4==0: continue
                m2a['ee' if kC=='e' else 'oo']+=1
                if kC=='o':
                    k=v2(pos[cD]-pos[cC]); hv[k]=hv.get(k,0)+1
print("M2a cross:",m2a,"odd-odd v2(dM):",hv,f"{time.time()-t0:.1f}s")
x1=0
for (xF,yF),(kF,cF,iF) in pts.items():
    if kF!='e': continue
    for iG in range(2,(h+1)//2,4):
        yG=2*iG+1
        if yF+yG-1>h: break
        M=(yF-1)*(yG-1)//4
        if M+1 < minax//2: continue
        for d in divs(M):
            S=d+M//d
            if d*d>M or 2*S<minax: continue
            for xG in (xF+2*S,xF-2*S):
                G=(xG,yG)
                if G in pts and pts[G][0]=='o' and pts[G][1]!=cF: x1+=1
print("X1 cross:",x1,"per label",round(x1/nlab,5),f"{time.time()-t0:.1f}s")
import sys as _s; _s.exit(0)
x2=0
for (xV,yV),(kV,cV,iV) in pts.items():
    if kV!='o' or yV%4!=1 or yV<5: continue
    for yG in range(yV+1,h+1,2):
        g=yG-yV; N=(yV-1)*g
        amax=N//minax
        for a in range(1,amax+1):
            if a%4==0 or N%a: continue
            for sa in (a,-a):
                G=(xV+N//sa,yG)
                if G in pts and pts[G][0]=='e' and pts[G][1]!=cV: x2+=1
print("X2 cross:",x2,"per label",round(x2/nlab,5),f"{time.time()-t0:.1f}s")
