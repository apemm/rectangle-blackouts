# Sanity check of the two exact leg-count formulas (A1) and (A2).
# (A1) number of odd Y>0 with (Sq)^2+Y^2 square (any L) equals tau(q_odd^2)
# (A2) q -> alpha = L - Sq is a bijection onto {alpha | Y^2, alpha<Y, alpha = +-Y mod 2^s}
from math import isqrt
def tau(n):
    c=1; p=2
    while p*p<=n:
        e=0
        while n%p==0: n//=p; e+=1
        c*=e+1; p+=1
    if n>1: c*=2
    return c
def divisors(n):
    ds=[]; i=1
    while i*i<=n:
        if n%i==0:
            ds.append(i)
            if i*i!=n: ds.append(n//i)
        i+=1
    return ds
bad=0
for s in (2,3,4,5):
    S=2**s
    for q in range(1,400):
        X=S*q; N=X*X
        # X^2 = (L-Y)(L+Y): u=L-Y, v=L+Y, u<v, same parity, Y=(v-u)/2 odd
        ys=set()
        for u in divisors(N):
            v=N//u
            if u<v and (v-u)%2==0:
                Y=(v-u)//2
                if Y%2==1: ys.add(Y)
        qo=q
        while qo%2==0: qo//=2
        if len(ys)!=tau(qo*qo): bad+=1; print("A1 fail",S,q,len(ys),tau(qo*qo))
    for Y in range(1,2000,2):
        legs=set()
        Lmax=(Y*Y+1)//2
        for a in divisors(Y*Y):
            b=Y*Y//a
            if a<b and (b-a)%(2*S)==0: legs.add((b-a)//(2*S))
        alph=[a for a in divisors(Y*Y) if a<Y and ((a-Y)%S==0 or (a+Y)%S==0)]
        if len(legs)!=len(alph): bad+=1; print("A2 fail",S,Y)
        for a in alph:
            q=(Y*Y//a-a)//(2*S); L=(Y*Y//a+a)//2
            if (S*q)**2+Y*Y!=L*L: bad+=1; print("A2 param fail",S,Y,a)
print("failures:",bad)
