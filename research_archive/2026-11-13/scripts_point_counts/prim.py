import sys
from math import gcd
H=int(sys.argv[1]); R=float(sys.argv[2])
prim=[]
for e in range(2,H):
    for s in range(2, int(e/(R-1))+2):
        g=gcd(e,s*s); step=e//g
        n1=step
        while n1<s:
            Y=s-n1
            num=n1*(e*e+s*s)
            if num%(e*Y)==0:
                u2=num//(e*Y)
                if e+u2<=H and (e*u2)%n1==0:
                    D=e*u2//n1 - Y
                    if D>=R*(e+u2) and gcd(gcd(n1,Y),gcd(e,u2))==1:
                        prim.append((e+u2,D/(e+u2),n1,Y,e,u2))
            n1+=step
prim.sort()
print('H',H,'R',R,'#prim',len(prim))
for k in [H//8,H//4,H//2,H]:
    print(k, sum(1 for p in prim if p[0]<=k))
for p in prim[:25]: print(p)
