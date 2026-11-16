import math
for mu,nu in [(4,1),(8,1),(12,1),(4,3),(4,2)]:
    D=mu*mu+4*nu*nu; S=[]
    for m in range(-10**6,10**6):
        if m==0: continue
        v=(mu*m)**2+(1-2*nu*m)**2; r=math.isqrt(v)
        if r*r==v: S.append(m)
    print((mu,nu),"D",D,"S_1 within |m|<1e6:",S[:12])
