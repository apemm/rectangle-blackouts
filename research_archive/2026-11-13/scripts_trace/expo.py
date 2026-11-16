import math
E=lambda a:(1+3**a)/2
f=lambda a:(E(a)+1)/(1+a)
lo,hi=0.1,3.0
for _ in range(200):
    m1=lo+(hi-lo)/3; m2=hi-(hi-lo)/3
    if f(m1)<f(m2): hi=m2
    else: lo=m1
a=(lo+hi)/2; th=f(a)
print("a*",a,"theta*",th,"c",2-th,"4^a*",4**a,"E(a*)",E(a))
# grid: min over x of max(x, E(a)+1-a x, 2-x), and also optimise a too
best=(9,None)
for i in range(1,30001):
    x=1+i*1e-5*1.0
    v=max(x,E(a)+1-a*x,2-x)
    if v<best[0]: best=(v,x)
print("grid at a*",best)
# phi duality: root of x=2-phi(x)
def phi(x):
    y=x/math.log(3); return 0.5-y+y*math.log(2*y)
lo,hi=1.2,1.8
for _ in range(200):
    mid=(lo+hi)/2
    if mid-(2-phi(mid))>0: hi=mid
    else: lo=mid
print("root x=2-phi(x)",lo)
print("light const",512*4*80*16*2.08)
# v2 exponent
print("v2", min(max(x/1000, 2.8588-0.91*x/1000, 3-x/1000) for x in range(1000,2000)))
# lcm/size checks
print("h^2/8+3h/2<(1.04h)^2 at h=10:", 100/8+15 < (10.4)**2)
