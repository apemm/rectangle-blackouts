import math
ln3=math.log(3)
def phi(x):
    y=x/ln3
    if y<=0.5: return 0.0
    return 0.5-y+y*math.log(2*y)
def theta(beta):
    best=(9,None)
    for k in range(1,400001):
        x=k*1e-5*4
        v=max(x,beta-phi(x),beta-x)
        if v<best[0]: best=(v,x)
    return best
for beta in [2.0,1.9,1.8,1.75,1.69,1.6,1.5,1.4,1.3,1.2,1.1,1.0]:
    v,x=theta(beta); print(f"beta={beta:.3f} theta={v:.5f} at x={x:.4f} phi={phi(x):.4f}")
# profile-sorting exponent for private factor
for K in [1,2,3,4,6,10,100]:
    print(K, K*(2**(1/K)-1))
