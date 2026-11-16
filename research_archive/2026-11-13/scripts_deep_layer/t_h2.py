import sys, time
from test_hole import run_rule, Rrow
h=int(sys.argv[1]); gap=int(sys.argv[2]); t=time.time()
def fac(h, iota, nu):
    R = Rrow(h, iota)
    return lambda n: R - gap if n % 4 == nu else R
for iota in range(4):
    R=Rrow(h,iota)
    if R-gap < 2: print(h,iota,'skip'); continue
    tot,nlab,exs=run_rule(h,iota,fac,Ms=(0,1,2,3))
    print(h,iota,'R',R,'rho',R-gap,'labels',nlab,'total',sum(tot.values()),dict(sorted(tot.items())),flush=True)
print('time',time.time()-t)
