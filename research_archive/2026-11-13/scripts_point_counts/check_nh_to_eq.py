from math import gcd
from eq_enum import spf_sieve, EQ
h=20000
sols=[]
for e in range(78,h):
    for s in range(2, e//77+1):
        g=gcd(e,s*s); step=e//g; n1=step
        while n1<s:
            Y=s-n1; num=n1*(e*e+s*s)
            if num%(e*Y)==0:
                u2=num//(e*Y)
                if e+u2<=h-1 and (e*u2)%n1==0 and e*u2//n1-Y>=78*h: sols.append((n1,Y,e,u2))
            n1+=step
spf=spf_sieve(2*2*h+5); cache={}; miss=0
for (n1,Y,e,u2) in sols:
    Q=u2+2*e
    if Q not in cache: cache[Q]=set((a,b,c,d) for (a,b,c,d) in EQ(Q,spf))
    X=e*u2//n1-Y-2*n1
    if (e,n1,X,Y) not in cache[Q]: miss+=1
print('N_h tuples',len(sols),'not found as E(Q) witnesses',miss)
