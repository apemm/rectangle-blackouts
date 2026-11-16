# Check: R_IV generator (al,be) gives the nodal-cubic point (a,b)=(4be-2al,be) with V/U = p/q.
import math
from fractions import Fraction as Fr
def UV(a,b): return (a-4*b)*(a*a+b*b), a**3-4*a*a*b-3*a*b*b+4*b**3
n=0
for be in range(3,400,2):
    for al in range(1,be,2):
        if math.gcd(al,be)!=1: continue
        F=4*(al-2*be)**2+be*be; C=al*F+4*(be-al)*be*be
        g=math.gcd(F,be-al); q=al*F//g; p=C//g
        a,b=4*be-2*al,be; U,V=UV(a,b)
        assert U==-2*al*F and V==-2*C
        assert Fr(V,U)==Fr(p,q)
        n+=1
print("checked",n,"generators (all odd coprime al<be): U=-2 al F, V=-2C, V/U=p/q")
# first k=4 edge
al,be=None,None
for be in range(3,60,2):
    for al in range(1,be,2):
        if math.gcd(al,be)==1 and (be-al)%4==0:
            F=4*(al-2*be)**2+be*be; g=math.gcd(F,be-al)
            if al*F//g==349: print("edge (349,749) from (al,be)=",(al,be),"-> (a,b)=",(4*be-2*al,be), "m=",Fr(4*be-2*al,be))
