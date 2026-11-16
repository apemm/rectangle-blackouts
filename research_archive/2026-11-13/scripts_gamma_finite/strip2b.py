# like strip2 but reports, per level, #active elements (both coordinates undecided-unsafe) and #good digit pairs
import sys, time, math
from fractions import Fraction as F
exec(open('strip2.py').read().split("z1 = z2 = 0")[0].replace("print(\"strip elements","pass #"))
z1 = z2 = 0
for j in range(1, J+1):
    E = lev.get(j, []); info=[]
    for (k1,k2,r) in E:
        u1,m1=part(r,l1); u2,m2=part(r,l2); info.append((k1,k2,u1,m1,u2,m2))
    good=[]
    for d1 in range(l1):
        Z1 = z1 + d1*l1**(j-1)
        for d2 in range(l2):
            Z2 = z2 + d2*l2**(j-1); bad=0
            for (k1,k2,u1,m1,u2,m2) in info:
                p1 = F((Z1*u1) % m1, m1) if m1 > 1 else F(0); p2 = F((Z2*u2) % m2, m2) if m2 > 1 else F(0)
                if not (ok(p1) or ok(p2)): bad=1; break
            if not bad: good.append((Z1,Z2))
    # active: elements whose phase at the prime with smaller exponent is already unsafe
    act=0
    for (k1,k2,u1,m1,u2,m2) in info:
        if abs(k1)<j: 
            p1=F((z1*u1)%m1,m1) if m1>1 else F(0)
            if not ok(p1): act+=1
        elif abs(k2)<j:
            p2=F((z2*u2)%m2,m2) if m2>1 else F(0)
            if not ok(p2): act+=1
        else: act+=1
    print("level",j,"elements",len(E),"active",act,"good pairs",len(good),"of",l1*l2,flush=True)
    if not good: break
    z1,z2=good[len(good)//2]
