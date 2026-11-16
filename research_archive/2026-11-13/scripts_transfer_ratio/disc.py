def disc3(a,b,c,d): return 18*a*b*c*d-4*b**3*d+b*b*c*c-4*a*c**3-27*a*a*d*d
def fac(n):
    n=abs(n); f={}; p=2
    while p*p<=n:
        while n%p==0: f[p]=f.get(p,0)+1; n//=p
        p+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
for u in (1,3,5,7,9):
    # C_u(x,1) = 4x^3 - 16u x^2 + (16u^2-3) x + 4u  (x = al/be)
    D=disc3(4,-16*u,16*u*u-3,4*u)
    # V_r(x,1) = x^3 - r x^2 - 3x + r with r = 4u
    r=4*u; DV=disc3(1,-r,-3,r)
    print("u",u,"disc C_u =",D,fac(D)," disc V_4u =",DV,fac(DV))
