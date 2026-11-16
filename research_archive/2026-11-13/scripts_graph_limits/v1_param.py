# Check: d in S_T^inf  <=>  d = (T/N) * p*q/2 with gcd(p,q)=1, pq even, N=p^2-pq-q^2 dividing T; L = |T|(p^2+q^2)/|N|.
import sys, time
from math import isqrt, gcd
t0=time.time()
def brute(T,B):
    out={}
    for d in range(-B,B+1):
        if d==0: continue
        Q=20*d*d+4*T*d+T*T; L=isqrt(Q)
        if L*L==Q: out[d]=L
    return out
def param(T,B):
    out={}
    # |d| = |T/N| |pq|/2 <= B and |N|>=1 => |pq| <= 2B ; also N | T so |N| <= |T|
    P=2*B+2
    for p in range(-P,P+1):
        if p==0: continue
        for q in range(1,P+1):
            if abs(p*q)>2*B*abs(T): break
            if gcd(p,q)!=1 or (p*q)%2: continue
            N=p*p-p*q-q*q
            if T%N: continue
            d=(T//N)*(p*q//2)
            if d==0 or abs(d)>B: continue
            L=abs(T)*(p*p+q*q)//abs(N)
            assert abs(T)*(p*p+q*q)%abs(N)==0
            if d in out: assert out[d]==L
            out[d]=L
    return out
bad=0
for T in [1,-1,3,5,-5,7,11,-11,15,19,29,31,55,95,121,145,209,605,1045,-1045,2255]:
    B=min(4000, 300*abs(T))
    a=brute(T,B); b=param(T,min(B,600))
    a2={d:L for d,L in a.items() if abs(d)<=min(B,600)}
    if a2!=b: bad+=1; print("MISMATCH",T,sorted(set(a2)^set(b))[:8])
print("mismatches",bad,"t=%.1f"%(time.time()-t0))
