# Verify the explicit Beatty solutions xi(r)=floor(theta r) mod 3 for the M=3 two-gap system:
#  xi(r+a)!=xi(r); xi(r+b)-xi(r)!=s; xi(r+b+1)-xi(r)!=s-3, all r in Z.
from fractions import Fraction as F
from math import ceil
import sys
def theta2(a,b):
    # s=2 choice of theta = 3*tau, for a>=2
    if b<=a-1: return F(1,a)
    if b<=2*a: return F(-2,b)
    if b<=3*a-1: return F(-3,b+1)
    m=-(-b//(3*a))
    return F(3*m,b)
def check(theta,a,b,s):
    p,q=theta.numerator,theta.denominator
    per=3*q
    xi=lambda r:(p*r//q)%3
    for r in range(per):
        if xi(r+a)==xi(r): return False
        if b>=1 and xi(r+b)-xi(r)==s: return False
        if xi(r+b+1)-xi(r)==s-3: return False
    return True
A=int(sys.argv[1]);B=int(sys.argv[2]);bad=[];n=0
for a in range(2,A+1):
    for b in range(0,B+1):
        th=theta2(a,b)
        for s,t in ((2,th),(1,-th)):
            n+=1
            if not check(t,a,b,s): bad.append((a,b,s))
print("checked",n,"bad",len(bad),bad[:20])
