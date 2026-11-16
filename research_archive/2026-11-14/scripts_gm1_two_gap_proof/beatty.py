# Beatty test: exists t with {ta} in [1/3,2/3], {tb},{t(b+1)} in [2/3,1] (closed mod 1)
from fractions import Fraction as F
import sys
def v2(n):
    if n==0: return 10**9
    c=0
    while n%2==0: n//=2; c+=1
    return c
def inJ(x):  # x mod 1 in [2/3,1] U {0}
    f=x-(x.numerator//x.denominator)
    return f==0 or f>=F(2,3)
def inI(x):
    f=x-(x.numerator//x.denominator)
    return F(1,3)<=f<=F(2,3)
def beatty(a,b):
    crit=set()
    for d in (3*a,3*b,3*(b+1)):
        for k in range(d): crit.add(F(k,d))
    crit=sorted(crit); crit.append(F(1))
    pts=list(crit)+[(crit[i]+crit[i+1])/2 for i in range(len(crit)-1)]
    for t in pts:
        if inI(t*a) and inJ(t*b) and inJ(t*(b+1)): return t
    return None
A=int(sys.argv[1]); B=int(sys.argv[2])
fails=[]; cnt=0
for a in range(2,A+1,2):
    al=v2(a); m=2**(al+1)
    for b in range(1,B+1):
        if b%m in (0,m-1): continue
        cnt+=1
        t=beatty(a,b)
        if t is None: fails.append((a,b))
print("cases",cnt,"beatty fails",len(fails))
print(fails[:200])
