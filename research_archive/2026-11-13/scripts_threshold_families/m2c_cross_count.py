# Count cross-block M2c shapes (|Delta| >= 78h) for given h via (n1,w>0,e): e | n1 m^2, m=n1+w,
# u2 = n1(m^2+e^2)/(e w) in [1, h-1-e], Delta = e*u2/n1 - w >= 78h, shallow conditions. Sign-symmetric (x2).
import sys
from sympy import divisors
def cnt(h):
    c=0; ex=None
    for n1 in range(1, h//312+2):
        for w in range(1, h//77+2):
            m=n1+w
            for e in divisors(n1*m*m):
                if e>=h: break
                num=n1*(m*m+e*e)
                if num%(e*w): continue
                u2=num//(e*w)
                if u2<1 or u2+e>h-1: continue
                if (e*u2)%n1: continue
                D=e*u2//n1-w
                if D<78*h: continue
                z=-(D+w)
                if z%4==0 or (2*n1-z)%4==0: continue
                c+=1; ex=(n1,w,e,u2,D)
    return 2*c, ex
for h in map(int,sys.argv[1:]):
    print(h, cnt(h)); sys.stdout.flush()
