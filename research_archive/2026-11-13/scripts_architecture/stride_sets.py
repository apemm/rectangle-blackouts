# Distance sets D_T^{(s)} for stride s: (s d)^2 + (2d+T)^2 = L^2, 0<L<h, d != 0, |d| < n_T.
import sys, math
from collections import defaultdict
def triples(h):
    # all (x,y,L) with x^2+y^2=L^2, 0<L<h, x>0,y>0 (x,y integers), via Euclid with scaling
    out=[]
    u=2
    while u*u+1<h:
        for v in range(1,u):
            if (u-v)%2==1 and math.gcd(u,v)==1:
                a=u*u-v*v; b=2*u*v; c=u*u+v*v
                g=1
                while g*c<h:
                    out.append((g*a,g*b,g*c)); out.append((g*b,g*a,g*c)); g+=1
        u+=1
    return out
def dsets(h,s,tr):
    A=(h+1)//2; K=h//2
    D=defaultdict(set)
    for (x,y,L) in tr:
        if x%s or y%2==0: continue
        for sx in (1,-1):
            for sy in (1,-1):
                d=sx*x//s; Y=sy*y; T=Y-2*d
                if abs(T)>=h: continue
                sd=(T-1)//2
                lo=max(0,-sd); hi=min(A,K-sd)
                n=hi-lo
                if n>=1 and abs(d)<n: D[T].add(abs(d))
    return D
if __name__=="__main__":
    h=int(sys.argv[1]); strides=[int(a) for a in sys.argv[2:]]
    tr=triples(h)
    Ds={s:dsets(h,s,tr) for s in strides}
    Ts=[t for t in range(-h+1,h) if t%2]
    A=(h+1)//2; K=h//2
    Ts=[T for T in Ts if min(A,K-(T-1)//2)-max(0,-(T-1)//2)>=1]
    for s in strides:
        print("stride",s,"sum k_T",sum(len(Ds[s].get(T,())) for T in Ts))
    tot=sum(min(len(Ds[s].get(T,())) for s in strides) for T in Ts)
    print("diagonals",len(Ts),"sum min_s k_T",tot, "ratio per h", tot/h, "log h", math.log(h))
