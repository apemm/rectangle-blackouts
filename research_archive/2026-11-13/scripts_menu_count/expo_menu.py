import math
L3=math.log(3)
def Am(a,m):
    if m==0: return 3**(a/2)  # limit
    return ((1+3**(a/m))/2)**m
def f(a,m,b=2.0): return (Am(a,m)-1+b)/(1+a)
def golden(g,lo,hi,it=200):
    r=(5**.5-1)/2
    c=hi-r*(hi-lo); d=lo+r*(hi-lo)
    for _ in range(it):
        if g(c)<g(d): hi=d
        else: lo=c
        c=hi-r*(hi-lo); d=lo+r*(hi-lo)
    return (lo+hi)/2
def dAm(a,m):
    if m==0: return 3**(a/2)*L3/2
    A=(1+3**(a/m))/2
    return A**(m-1)*3**(a/m)*L3/2
for m in [1,2,3,4,5,6,8,10,20,50,100,0]:
    a=golden(lambda t:f(t,m),1e-6,10)
    x=f(a,m)
    # stationarity: x = dAm(a)  (since (A-1+2)'(1+a) = A+1 -> A' = x)
    # grid check
    g=min(f(i/20000,m) for i in range(1,200000))
    # heavy fraction exponent: beta_m(a)-a*x
    hf=Am(a,m)-1-a*x
    print(("inf" if m==0 else m), "x=%.7f a*=%.6f  A'(a*)=%.7f grid=%.7f beta(a*)=%.6f heavyfrac_exp=%.6f 2-x=%.6f"%(x,a,dAm(a,m),g,Am(a,m)-1,hf,2-x))
# Legendre check: phi_m(x)= sup_a (a x - beta_m(a)); root of x = 2-phi_m(x)
print("Legendre check")
for m in [1,2,5,0]:
    def phi(x): 
        a=golden(lambda t:-(t*x-(Am(t,m)-1)),1e-9,30); return a*x-(Am(a,m)-1)
    lo,hi=1.0,2.0
    for _ in range(100):
        mid=(lo+hi)/2
        if mid-(2-phi(mid))>0: hi=mid
        else: lo=mid
    print(m, "root x=2-phi_m(x): %.7f"%lo)
