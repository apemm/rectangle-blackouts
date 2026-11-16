from math import isqrt, gcd
def sq(n): return n>=0 and isqrt(n)**2==n
B=3000
out=[]
for v in range(1,B):
    for u in range(-3*B,3*B):
        if u==0 or gcd(u,v)!=1: continue
        if sq(20*u*u+4*u*v+v*v) and sq(20*u*u-4*u*v+v*v): out.append((u,v))
print(out)
