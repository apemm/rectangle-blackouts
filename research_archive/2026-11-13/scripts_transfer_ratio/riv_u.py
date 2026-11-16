# R_IV at stride 4u: predicted edges vs definition-level brute force of in-class M2c
import sys, math
from math import gcd
def v2(x):
    x=abs(x); c=0
    while x%2==0: x//=2; c+=1
    return c
def pred_edges(u,k,X):
    E=set()
    be=1
    while True:
        if 4*u*be**3 > (4*u*u+1)*X: break   # p >= C_u/g >= 4u be^3/Delta_u
        for al in range(1,u*be,2):
            if be%2==0 or gcd(al,be)!=1: continue
            if v2(u*be-al) < k-2: continue
            F=4*(al-2*u*be)**2+be**2
            g=gcd(F,u*be-al)
            q=al*F//g; p=(al*F+4*(u*be-al)*be*be)//g
            assert (al*F)%g==0 and (al*F+4*(u*be-al)*be*be)%g==0
            assert (4*u*u+1)%g==0, (u,al,be,g)
            m=1
            while p*m<=X:
                E.add((q*m,p*m)); m+=2
        be+=2
    return E
def divisors(n):
    n=abs(n); ds=[]
    i=1
    while i*i<=n:
        if n%i==0:
            ds.append(i)
            if i*i!=n: ds.append(n//i)
        i+=1
    return ds
def brute(u,h,iota,mod):
    # odd label points of one class: slot i = iota mod `mod`, column 4u*i, row 2i+1; shallow sea row 1 at x != 0 mod 4
    labs=[i for i in range(iota,(h+1)//2,mod) if 2*i+1<=h]
    found=set()
    for iB in labs:
        xB,yB=4*u*iB,2*iB+1
        for iD in labs:
            if iD==iB: continue
            xD,yD=4*u*iD,2*iD+1
            e2=yD-yB
            if e2%2: continue
            e=e2//2
            Y=yB-1
            if Y<=0: continue
            for d in divisors(e*Y):
                for X in (d,-d):
                    if X%4==0: continue
                    if (e*Y)%X: continue
                    nx=-e*Y//X; ny=e
                    xA=xB-X
                    xC=xA+xB+2*nx-xD; yC=1
                    if xC%4==0: continue
                    if (xD-xC)**2+(yD-yC)**2 != X*X+Y*Y: continue
                    if (xD-xC,yD-yC) in ((X,Y),(-X,-Y)): continue
                    py=1+ny; qy=yB+ny
                    if not(1<=py<=h and 1<=qy<=h): continue
                    vB=(yB-1)//2; vD=(yD-1)//2
                    found.add((min(vB,vD),max(vB,vD)))
    return found
if __name__=="__main__":
    for (u,h,iota,mod,k) in [(1,1000,1,8,3),(3,2400,1,8,3),(3,2400,3,8,3),(5,2400,1,8,3)]:
        P=pred_edges(u,k,(h-1)//2)
        P={e for e in P if e[0]%mod==iota%mod}
        Bf=brute(u,h,iota,mod)
        print("u",u,"h",h,"iota",iota,"mod",mod,": predicted",sorted(P)[:8],"n=",len(P)," brute",sorted(Bf)[:8],"n=",len(Bf)," equal:",P==Bf)
    for u in (1,3,5,7,9):
        for k in (3,5):
            P=pred_edges(u,k,10**6)
            print("u",u,"k",k,"edges<=1e6:",len(P),"smallest:",sorted(P,key=lambda e:e[1])[:3])
