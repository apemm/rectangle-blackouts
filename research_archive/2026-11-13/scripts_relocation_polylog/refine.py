import numpy as np
src=open('holder_exponent3.py').read().split('for b in')[0]
src=src.replace('np.linspace(1.01, 6, 150)','np.linspace(1.005, 5, 400)').replace('np.linspace(0.0, 4, 41)','np.linspace(0.0, 3, 121)')
exec(src)
for b,(n0,n1,o0,o1) in [(1.5,(3,7,2.5,4.2)),(0.0,(6,10,3.5,5.0))]:
    worst=-1e9; arg=None
    for nu in np.linspace(n0,n1,21):
        for om in np.linspace(o0,o1,18):
            tt=terms(nu,om); t=max(tt)
            if t>b and t+nu>worst: worst,arg=t+nu,(round(nu,2),round(om,2))
    print(b, round(worst,3), arg)
