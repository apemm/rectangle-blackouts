import numpy as np
exec(open('holder_exponent.py').read().split('def need_a')[0])
def worst_by_nu(b, nus):
    out=[]
    for nu in nus:
        w=-1e9; arg=None
        for om in np.linspace(0, 20, 201):
            tt = terms(nu, om); t=max(tt)
            if t > b and t+nu > w: w, arg = t+nu, (om, tt.index(max(tt)))
        out.append((nu, round(w,2), arg))
    return out
for b in [0.0, 1.5]:
    print("b=",b, worst_by_nu(b, [0,2,4,6,8,10,12,16,20,30]))
