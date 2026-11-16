# type I.2 label-only mixed quadruples in a layout (stride 4); checks v2 identity and Ds=0 mod 2^nu kill
import sys, time
from math import isqrt
from layout import build
def v2(n):
    n=abs(n);c=0
    while n%2==0: n//=2;c+=1
    return c
h=int(sys.argv[1]); mode=sys.argv[2]; pmin=int(sys.argv[3])
p,Q,cls,pos,_=build(h,mode,pmin=pmin)
t0=time.time()
order=sorted(range(len(cls)),key=lambda c:pos[c]); rank={c:k for k,c in enumerate(order)}
R=(h*h)//(8*p)+3
sets=[set(c) for s,c in cls]
found=0; ident_ok=0; hist={}
for c0 in range(len(cls)):
    s0,sl0=cls[c0]; T0=2*s0+1
    k0=rank[c0]
    for kk in range(max(0,k0-3*R),min(len(order),k0+3*R+1)):
        c1=order[kk]
        if c1==c0: continue
        s1,sl1=cls[c1]; T1=2*s1+1; Ds=s1-s0; dM=p*(pos[c1]-pos[c0])
        if abs(dM)>h*h: continue
        for a in range(-h//2,h//2+1):
            if a==0: continue
            Na=16*a*a+(2*a+T0)**2
            disc=80*Na-64*T1*T1
            if disc<0: continue
            r=isqrt(disc)
            if r*r!=disc: continue
            for num in (-4*T1+r,-4*T1-r):
                if num%40: continue
                b=num//40
                if (b,T1)==(a,T0) or (b,T1)==(-a,-T0): continue
                lhs=-16*a*dM-(2*a+T0)*Ds; den=10*a+T0
                if lhs%den: continue
                m=lhs//den; n2=m+Ds
                for i0 in sl0:
                    if i0+a not in sets[c0]: continue
                    t=m+2*i0+a-b
                    if t%2: continue
                    iC=t//2
                    if iC not in sets[c1] or iC+b not in sets[c1]: continue
                    r1=2*i0+1+n2; r2=2*i0+2*a+1+T0+n2
                    if not(1<=r1<=h and 1<=r2<=h): continue
                    found+=1
                    E=2*(-(dM-Ds))-Ds  # 2*Dn - Ds with Dn = Ds - dM
                    if v2(n2)==3+v2(a)+v2(E): ident_ok+=1
                    k=min(v2(Ds),9) if Ds else 99
                    hist[k]=hist.get(k,0)+1
print(f"h={h} {mode} p={p} 2^nu={Q} I.2 found={found} v2-identity ok={ident_ok} hist v2(Ds)={dict(sorted(hist.items()))} {time.time()-t0:.1f}s")
