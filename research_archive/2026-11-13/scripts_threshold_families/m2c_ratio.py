# Shapes via (n1,w>0, e | n1*m^2, m=n1+w): u2 = n1(m^2+e^2)/(e w) integer, Delta = e*u2/n1 - w.
# Record the largest ratio Delta/(e+u2+1) (a lower bound proxy for Delta/h since h >= e+u2+1).
import sys
from sympy import divisors
N1=int(sys.argv[1]); W=int(sys.argv[2])
best=[]
for n1 in range(1,N1+1):
    for w in range(1,W+1):
        m=n1+w; X=n1*m*m
        for e in divisors(X):
            num=n1*(m*m+e*e)
            if num%(e*w): continue
            u2=num//(e*w)
            if (e*u2)%n1: continue
            D=e*u2//n1-w
            z=-(D+w)
            if z%4==0 or (2*n1-z)%4==0: continue
            r=D/(e+u2+1)
            best.append((r,n1,w,e,u2,D))
best.sort(reverse=True)
for b in best[:8]: print(b)
print('count',len(best))
