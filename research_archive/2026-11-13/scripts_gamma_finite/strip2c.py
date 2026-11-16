import sys, time, math
from fractions import Fraction as F
exec(open('strip2.py').read().split("z1 = z2 = 0")[0].replace("print(\"strip elements","pass #"))
z1 = z2 = 0; t0=time.time()
def okp(Z,u,m): 
    if m==1: return False
    v=(Z*u)%m; return min(F(v,m),1-F(v,m))>=cz
for j in range(1, J+1):
    E = lev.get(j, []); F1=set(); F2=set(); joint=[]
    for (k1,k2,r) in E:
        u1,m1=part(r,l1); u2,m2=part(r,l2)
        if abs(k1)==j and abs(k2)<j:
            if okp(z2,u2,m2): continue
            F1|={d for d in range(l1) if not okp(z1+d*l1**(j-1),u1,m1)}
        elif abs(k2)==j and abs(k1)<j:
            if okp(z1,u1,m1): continue
            F2|={d for d in range(l2) if not okp(z2+d*l2**(j-1),u2,m2)}
        else: joint.append((u1,m1,u2,m2))
    good=[(d1,d2) for d1 in range(l1) if d1 not in F1 for d2 in range(l2) if d2 not in F2
          if all(okp(z1+d1*l1**(j-1),a,b) or okp(z2+d2*l2**(j-1),c,d) for (a,b,c,d) in joint)]
    print("level",j,"elems",len(E),"forbidden d1",len(F1),"of",l1,"forbidden d2",len(F2),"of",l2,"joint",len(joint),"good",len(good),"%.0fs"%(time.time()-t0),flush=True)
    if not good: break
    d1,d2=good[0]; z1+=d1*l1**(j-1); z2+=d2*l2**(j-1)
