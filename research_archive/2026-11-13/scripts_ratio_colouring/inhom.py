# Inhomogeneous two-label two-filler family: Y1 = (P-8t)(P^2+w^2)/(8t(P+2w)), w = dp-2t, dp = filler row gap.
# (1) check the closed form against the original cubic; (2) count integer solutions with 1<=Y1<=h (superset, no congruences).
import sys, time, random
from sympy import divisors
t0=time.time()
def cubic(P,t,Y1,Y2): return P**3-8*t*P*P+((Y1-Y2)**2-8*t*Y1)*P-8*t*(Y2*Y2-Y1*Y1)
for _ in range(2000):
    t=random.randint(-50,50) or 1; dp=random.choice([0,8,-8,16,-16,24,-24]); P=random.randint(-300,300)
    w=dp-2*t
    if P+2*w==0: continue
    num=(P-8*t)*(P*P+w*w); den=8*t*(P+2*w)
    if num%den==0:
        Y1=num//den; assert cubic(P,t,Y1,Y1+w)==0
    # also general: any integer root P for integer Y1 must satisfy the identity
    Y1=random.randint(1,500); assert cubic(P,t,Y1,Y1+w)==(P-8*t)*(P*P+w*w)-8*t*Y1*(P+2*w)
print("closed form verified")
h=int(sys.argv[1]); DPS=[int(x) for x in sys.argv[2].split(",")]
for dp in DPS:
    cnt=0; cnt16=0
    for t in range(-h//2,h//2+1):
        if t==0: continue
        w=dp-2*t
        N=10*w*w*(dp+2*t)
        if N==0: continue
        for s0 in divisors(abs(N)):
            for s in (s0,-s0):
                P=s-2*w
                num=(P-8*t)*(P*P+w*w); den=8*t*s
                if num%den: continue
                Y1=num//den
                if 1<=Y1<=h and 1<=Y1+w<=h:
                    cnt+=1
                    if t%16==0: cnt16+=1
    print("dp=%3d  h=%d  solutions(all t)=%d  (t=0 mod 16)=%d"%(dp,h,cnt,cnt16), round(time.time()-t0,1),"s")
    if time.time()-t0>50: break
