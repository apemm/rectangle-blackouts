import math
from sympy import factorint, primerange, isprime
# 1. prime zeta(2) minus 1/4
s=sum(1.0/p/p for p in primerange(3,10**7))
# tail bound: sum_{n>10^7} 1/n^2 < 1e-7
print("sum odd primes 1/p^2 ~", s, "upper <", s+1e-7)
# 2. explicit menu greedy
def sqfree(n): return all(e==1 for e in factorint(n).values())
menu=[];vecs=[];skipped=[]
basis={}  # GF(2) elimination over primes
def indep_add(fac):
    v=set(p for p,e in fac.items() if e%2)
    # reduce
    while v:
        piv=max(v)
        if piv in basis: v=v^basis[piv]
        else:
            basis[piv]=v; return True
    return False
u=1
while len(menu)<12:
    D=4*u*u+1; f=factorint(D)
    if not sqfree(D): skipped.append((u,D,f))
    else:
        if indep_add(f): menu.append((u,D,f))
        else: skipped.append((u,D,'dep'))
    u+=2
for m in menu: print(m)
print("skipped",skipped)
print("4*173^2+1 =",factorint(4*173*173+1))
# 3. x_inf and x_m
def xm(m):
    best=(9,None)
    for i in range(1,40000):
        a=i*1e-4
        if m==0: b=3**(a/2)-1
        else: b=((1+3**(a/m))/2)**m-1
        val=(b+2)/(1+a)
        if val<best[0]: best=(val,a)
    return best
for m in [1,2,5,10,50,200,0]: print(m, xm(m))
# 4. Lemma SQ construction for P={5}: q=13
def sq_step(P):
    q=5
    while not (q%4==1 and isprime(q) and q not in P): q+=4
    r=next(x for x in range(q) if (4*x*x+1)%q==0)
    rp=next(x for x in range(q*q) if x%q==r and (4*x*x+1)%(q*q)==0)
    roots=[x for x in range(q*q) if (4*x*x+1)%(q*q)==0]
    c=next(x for x in range(2*q*q) if x%2==1 and x%q==r and x%(q*q)!=rp)
    u=c
    while not sqfree(4*u*u+1): u+=2*q*q
    D=4*u*u+1
    assert D%q==0 and D%(q*q)!=0
    return q,r,rp,len(roots),c,u,factorint(D)
P=set([5]); U=[1]
for k in range(5):
    q,r,rp,nr,c,u,f=sq_step(P); print("q",q,"r",r,"r'",rp,"#roots mod q^2",nr,"c",c,"u",u,f)
    U.append(u); P|=set(f)
# check independence of U
basis.clear()
print("indep:", all(indep_add(factorint(4*x*x+1)) for x in U), U)
# 5. density of squarefree 4u^2+1 in a class, compare to bound
q=13; c=None
