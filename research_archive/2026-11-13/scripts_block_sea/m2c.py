# Solve M2c for deep pairs B, D=B+(Dx, 2e), e>0, with shallow A, C in row 1.
def sols(Dx,e,u2,h=10**9):
    out=[]
    # z divides e*u2 (n1 integer) ; enumerate divisors of e*u2 (if u2>0)
    N=abs(e*u2)
    cands=set()
    if N==0:
        return out
    d=1
    while d*d<=N:
        if N%d==0:
            for q in (d,N//d): cands|={q,-q}
        d+=1
    for z in cands:
        if Dx*z**3+(Dx*Dx+2*e*u2+e*e)*z*z+2*Dx*e*u2*z+e*e*u2*u2!=0: continue
        if z%4==0: continue
        n1=-e*u2//z
        # alpha = xB - z ; kappa = alpha + xB + 2 n1 - xD  ; mod 4 with xB = xD = 0 mod 4
        kappa=(-z+2*n1)%4  # relative to multiples of 4
        if kappa==0: continue
        if u2+1+e>h: continue
        out.append((z,n1))
    return out
if __name__=='__main__':
    import sys
    res=[]
    for t in range(1,40):
        for u2 in range(0,120):
            for z,n1 in sols(4*t,t,u2):
                res.append((t,u2,z,n1))
    for r in res[:60]: print(r)
    print(len(res))
