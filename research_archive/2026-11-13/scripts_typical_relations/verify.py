# Independent check of the certificate: membership from the definition and a random-theta test.
import math, random
A = [35, 51, 76, 99, 110, 121, 174, 190, 209, 225, 246, 260, 285, 330, 391, 399, 420, 434, 455, 475, 600, 616, 629, 684, 741, 825, 826, 950, 1035, 1045, 1240, 1254, 1449, 1716, 1815, 1925, 2024, 2491, 2700, 2926, 3135, 3625, 3834, 3990, 4199, 4675, 4884, 5776, 5985, 6351, 6560, 6700, 6909, 9165, 9374, 9666, 9875, 10621, 10830, 13090, 13299]
T = 1045; Lam = 0
for a in A:
    Ls = [math.isqrt(20*d*d+4*T*d+T*T) for d in (a, -a) if math.isqrt(20*d*d+4*T*d+T*T)**2 == 20*d*d+4*T*d+T*T]
    assert Ls, a
    Lam = max(Lam, min(Ls))
print('all members; Lambda =', Lam)
import numpy as np
d1 = 413/5000

th=np.random.default_rng(1).random(2000000)
best=np.ones_like(th)
for a in A:
    z=(th*a)%1.0; np.minimum(best,np.minimum(z,1-z),out=best)
print('max over 2e6 random theta of min ||theta a|| =', best.max(), ' bound 0.0826')
