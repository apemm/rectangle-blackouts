import math, time
from fractions import Fraction
t0=time.time()
# (1) geometry check of the R3-horizontal fatal family
def sq(n):
    r=math.isqrt(n); return r*r==n
def rect_ok(P):  # P list of 4 points in cyclic order -> is rectangle
    import itertools
    a,b,c,d=P
    v1=(b[0]-a[0],b[1]-a[1]); v2=(d[0]-a[0],d[1]-a[1])
    return (a[0]+c[0]==b[0]+d[0] and a[1]+c[1]==b[1]+d[1] and v1[0]*v2[0]+v1[1]*v2[1]==0 and v1!=(0,0) and v2!=(0,0))
bad=0; cnt=0
for X in range(1,60):
    for y in range(2,60,2):
        L2=X*X+y*y
        if not sq(L2): continue
        L=math.isqrt(L2)
        a=101; c=a+y; s0=5; xe=1000
        C=(xe,a); D=(xe+X,c)
        A=(xe+(X-L)//2,s0); B=(xe+(X+L)//2,s0)
        mid=(a+c)//2; p=(A[0],mid); q=(B[0],mid)
        R1=[A,B,q,p]; R2=[p,C,q,D]
        cnt+=1
        ok = rect_ok(R1) and rect_ok(R2) and set(R1)^set(R2)=={A,B,C,D} and (X-L)%2==0
        if not ok: bad+=1
print("geometry: configs",cnt,"failures",bad)
# (2) counting: per-label average number of (partner row, X) with m|y, X in mZ, X<=Xmax, X^2+y^2 square
def divisors_of_square(z):
    # return sorted divisors of z^2
    f={}; n=z; p=2
    while p*p<=n:
        while n%p==0: f[p]=f.get(p,0)+1; n//=p
        p+=1
    if n>1: f[n]=f.get(n,0)+1
    ds=[1]
    for p,e in f.items():
        ds=[d*p**k for d in ds for k in range(2*e+1)]
    return ds
def leg_count(z,Xpmax):
    # number of X'>0, X'<=Xpmax with X'^2+z^2 square
    z2=z*z; c=0
    for u in divisors_of_square(z):
        v=z2//u
        if u<v and (v-u)%2==0 and (v-u)//2<=Xpmax: c+=1
    return c
m=7
for h in [1000,4000,16000,64000]:
    Lam=math.log(h)
    Xmax=h*int(math.sqrt(h))//2   # R1 = sqrt(h): W ~ h^1.5
    zmax=h//(2*m)   # odd rows 2i+1, i<h/2: y=2(i'-i), need 7|y -> z=y/7 even.. use y=m*z
    # odd row differences y=2k, |k|<h/2; m|y <=> m|k ; z = y/m = 2k/m
    tot=0; npairs=0
    A=h//2
    # per a: average over partners c; use distribution of k=i'-i over i,i' in [0,A)
    for k in range(m, A, m):
        w=2*(A-k)  # ordered pairs with |i'-i|=k, both signs
        z=2*k//m
        tot+=w*leg_count(z, Xmax//m)
    per_label=tot/A   # average over e of sum over partners (one label per odd row)
    print(f"h={h} per-label count={per_label:.1f}  /Lam^2={per_label/Lam**2:.3f}  /(Lam^2/m)... per-partner avg over all partners={tot/(A*A):.4f}  time={time.time()-t0:.1f}s")
