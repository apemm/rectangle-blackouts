# Exact enumeration of S_T^inf ∩ [-B,B] via beta = a + b*phi with N(beta) = -T^2, d = (Tr beta - T)/10
from math import isqrt
def fund(T):
    T=abs(T); out=set()
    for L in range(1, int(1.7*T)+2):
        Y=5*L*L-4*T*T
        if Y<0: continue
        X=isqrt(Y)
        if X*X!=Y: continue
        for x in {X,-X}:
            if (x-L)%2==0: out.add(((x-L)//2, L))
    return out
def up(a,b): return (a+b, a+2*b)
def dn(a,b): return (2*a-b, b-a)
def S(T,B):
    res={}
    for (a0,b0) in fund(T):
        for s in (1,-1):
            for step in (up,dn):
                a,b=s*a0,s*b0
                for _ in range(400):
                    tr=2*a+b
                    if abs(tr)>10*B+abs(T)+10 and _>3: break
                    if (tr-T)%10==0:
                        d=(tr-T)//10
                        if d!=0 and abs(d)<=B:
                            res[d]=(a,b)
                    a,b=step(a,b)
    return res
def issq(n):
    if n<0: return False
    r=isqrt(n); return r*r==n
def adj(T,x):  # |x| in D_T^inf
    return x!=0 and (issq(20*x*x+4*T*x+T*T) or issq(20*x*x-4*T*x+T*T))
if __name__=="__main__":
    import sys
    T=int(sys.argv[1]); B=int(sys.argv[2])
    s=S(T,B); 
    # brute check small range
    br=[d for d in range(-3000,3001) if d and issq(20*d*d+4*T*d+T*T)]
    assert sorted(d for d in s if abs(d)<=3000)==br, "mismatch"
    print(T,len(s),sorted(s)[:10])
