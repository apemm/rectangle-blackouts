# find split prime pairs (l1,l2) with s*eps^a*omega_l1^{+-1} == 1 mod 10*l2 and vice versa (pole order 1 each)
from math import isqrt
def mulm(x,y,m):
    a,b=x; c,d=y
    return ((a*c+b*d)%m, (a*d+b*c+b*d)%m)
def conj(x): a,b=x; return (a+b,-b)
def norm(x): a,b=x; return a*a+a*b-b*b
def invm(x,m):
    n=norm(x)%m; ni=pow(n,-1,m); c=conj(x); return ((c[0]*ni)%m,(c[1]*ni)%m)
def gen_pi(l):
    for b in range(1,200):
        for a in range(-300,300):
            if norm((a,b))==l: return (a,b)
def is_prime(n): return n>1 and all(n%p for p in range(2,isqrt(n)+1))
splits=[l for l in range(11,140) if is_prime(l) and l%5 in (1,4)]
PI={l:gen_pi(l) for l in splits}
def ok(l1,l2):
    m=10*l2; pi=PI[l1]; om=mulm(pi,invm(conj(pi),m),m)
    targets=[om, invm(om,m)]
    eps=(m-1,m-1)
    seen=set(); e=(1,0)
    for a in range(0,20000):
        for s in (1,m-1):
            v=( (s*e[0])%m, (s*e[1])%m )
            for t in targets:
                if mulm(v,t,m)==(1,0): return a
        e=mulm(e,eps,m)
        if e==(1,0) and a>0: break
    return None
res=[]
for i,l1 in enumerate(splits):
    for l2 in splits[i+1:]:
        a=ok(l1,l2); b=ok(l2,l1)
        if a is not None and b is not None: res.append((l1,l2,a,b))
print(len(splits), "split primes; good pairs:", len(res)); print(res[:15])
