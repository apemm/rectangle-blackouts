import sys, time
from test_hole import run_rule, Rrow
def two_level(h, iota, nu):
    R = Rrow(h, iota)
    return lambda n: R - 8 if n % 4 == nu else R
h=int(sys.argv[1]); t=time.time()
for iota in range(4):
    R=Rrow(h,iota)
    if R-8 <= (h+1)/2: print(h,iota,'skip R',R); continue
    tot,nlab,exs=run_rule(h,iota,two_level,Ms=(0,1,2,3))
    print(h,iota,'R',R,'labels',nlab,'total',sum(tot.values()),dict(sorted(tot.items())),flush=True)
    for k,v in sorted(exs.items()): print('     ',k,v)
print('time',time.time()-t)
