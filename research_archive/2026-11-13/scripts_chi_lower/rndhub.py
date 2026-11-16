# null model with hub: D = {t} ∪ A ∪ (A+t), A random of size a in [lo, n-t)
import sys, random
from rnd import colorable
n,t,a,lo,trials,secs=map(float,sys.argv[1:7]); n,t,a,lo,trials=int(n),int(t),int(a),int(lo),int(trials)
random.seed(2); out=[]
for _ in range(trials):
    A=random.sample(range(lo,n-t),a)
    D=sorted(set([t]+A+[x+t for x in A]))
    chi=None
    for k in range(3,10):
        r=colorable(n,D,k,secs)
        if r is None: chi=">=%d?"%k; break
        if r: chi=k; break
    out.append(chi)
print("n",n,"t",t,"a",a,"chis",out)
