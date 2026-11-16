# Direct search: M2c with B, D both U3 fillers (sea row 1), from the block_sea equation
# n1((Delta-n1)^2+e^2) = e*u2*(Delta-2n1), z=-e*u2/n1 integer, z!=0 mod 4, 2n1-z != 0 mod 4.
# Fillers: rows rho (n odd, nu=1), rho-8 (n=2 mod 4), rho-24 (n=0 mod 4), rho=T1 for h.
import itertools
hits=0; tested=0
for h in (131,139,155,163):
    r1=3; T1=max(y for y in range(1,h+1) if y%16==11); rho=T1
    row=lambda n: rho if n%2==1 else (rho-8 if n%4==2 else rho-24)
    for nB in range(4):
        for dn in range(-400,401):
            if dn==0: continue
            yB=row(nB); yD=row(nB+dn)
            if (yD-yB)%2 or yD<=yB: continue
            e=(yD-yB)//2; u2=yB-1; Delta=4*dn
            if yB+e>h: continue
            for n1 in range(-4*h*h//4, 4*h*h//4+1):
                if n1==0: continue
                tested+=1
                if (e*u2)%n1: continue
                z=-e*u2//n1
                if z%4==0 or (2*n1-z)%4==0: continue
                if n1*((Delta-n1)**2+e*e)==e*u2*(Delta-2*n1): hits+=1; print('hit',h,nB,dn,n1)
print('tested',tested,'hits',hits)
