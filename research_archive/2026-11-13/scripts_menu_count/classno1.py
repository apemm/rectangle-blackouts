import math
def isprime(n):
    if n<2: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True
def leg(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1
# K=Q(sqrt D), D prime =1 mod 4, O_K=Z[w], N(x+yw)=x^2+xy-c y^2, c=(D-1)/4
for u in range(1,80,2):
    D=4*u*u+1
    if not isprime(D): continue
    c=(D-1)//4
    M=math.sqrt(D)/2
    ok=True; gens=[]
    for p in range(2,int(M)+1):
        if not isprime(p): continue
        if p==2: split = (D%8==1)
        else: split = leg(D,p)==1
        if not split: continue
        found=None
        for y in range(1,3000):
            # x^2+xy-c y^2 = +-p -> x = (-y + sqrt(y^2+4(c y^2 +- p)))/2
            for s in (p,-p):
                disc=y*y+4*(c*y*y+s)
                if disc<0: continue
                r=math.isqrt(disc)
                if r*r==disc and (r-y)%2==0: found=((r-y)//2,y,s);break
            if found: break
        if not found: ok=False; gens.append((p,None))
        else: gens.append((p,found))
    print(u,D,"h=1 proven" if ok else "h=1 NOT shown", gens)
