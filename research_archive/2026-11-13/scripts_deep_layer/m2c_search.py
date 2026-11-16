import math, sys
from collections import Counter
# M2c: A=(alpha,1), C shallow row 1; B=(0,yB), D=(Delta,yD) deep (x=0 mod 4). e=(yD-yB)/2.
# n1 z + e u2 = 0 ; Delta^2 + (z-2n1)Delta + (n1^2+e^2-2 n1 z) = 0 ; z = xB - alpha != 0 mod 4 ; 2n1 - z != 0 mod 4
def sols(H):
    out=[]
    for yB in range(2,H+1):
        for yD in range(yB+2,H+1,2):
            e=(yD-yB)//2; u2=yB-1
            if yB+e>H: continue
            N=e*u2
            for z in range(-4*N-4, 4*N+5):
                if z==0 or z%4==0: continue
                if N % z: continue
                n1=-N//z
                if (2*n1-z)%4==0: continue
                bq=z-2*n1; cq=n1*n1+e*e-2*n1*z
                disc=bq*bq-4*cq
                if disc<0: continue
                r=math.isqrt(disc)
                if r*r!=disc: continue
                for Dl in {(-bq+r)//2, (-bq-r)//2}:
                    if (-bq+r)%2: continue
                    if Dl%4: continue
                    out.append((yB,yD,Dl,z,n1,e))
    return out
H=int(sys.argv[1])
S=sols(H)
c=Counter((s[0]%8,s[1]%8) for s in S)
print(len(S)); print(sorted(c.items()))
print([s for s in S if s[0]%8==s[1]%8][:10])
