from math import isqrt
def L(T,d):
    Q=20*d*d+4*T*d+T*T; r=isqrt(Q); return r if r*r==Q else None
T=1045; cl=[0,35,209,260,434]
for a in cl:
    for b in cl:
        if a<b:
            e=b-a; print(e, "d=+e L=",L(T,e)," d=-e L=",L(T,-e))
D=[d for d in range(1,700) if L(T,d) or L(T,-d)]
mL=max(min(x for x in (L(T,d),L(T,-d)) if x) for d in D)
print("witness n=700: |D|=",len(D),"max needed L=",mL)
# least h with n_T(h) >= 700 and h > mL
for h in range(2,20000):
    A=(h+1)//2; K=h//2; s=(T-1)//2; n=min(A,K-s)-max(0,-s)
    if n>=700 and h>mL: print("least h:",h); break
for (T,n) in [(55,54)]:
    D=[d for d in range(1,n) if L(T,d) or L(T,-d)]
    mL=max(min(x for x in (L(T,d),L(T,-d)) if x) for d in D); print("T=55 witness: D=",D,"max L",mL)
    for h in range(2,20000):
        A=(h+1)//2; K=h//2; s=(T-1)//2; m=min(A,K-s)-max(0,-s)
        if m>=n and h>mL: print("least h:",h); break
