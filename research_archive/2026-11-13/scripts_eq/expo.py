import math
L3=math.log(3)
def phi(x):
    y=x/L3; return 0.5-y+y*math.log(2*y)
def bis(f,lo,hi):
    for _ in range(200):
        mid=(lo+hi)/2
        if f(lo)*f(mid)<=0: hi=mid
        else: lo=mid
    return (lo+hi)/2
E1=bis(lambda E:2-phi(3*E-2)-E,1.0,1.5); print("Route L with (iii):",E1, "x=",3*E1-2)
E2=bis(lambda E:2-phi(2*E)-E,0.8,1.2); print("no Bad_split with (iii):",E2)
# grid LP with Markov heavy term 3-q-b1
best=(9,None)
N=200
for i in range(N+1):
  q=2*i/N
  for j in range(N+1):
    b0=2*j/N
    for k in range(N+1):
      b1=2*k/N
      E=max(q+b0,b1,1,3-q-b1,2-b0)
      if E<best[0]: best=(E,(q,b0,b1))
print("Route L with Markov (grid):",best)
print("gap phi(x)-(x-1) at x=1.75:",phi(1.75)-0.75, " at 1.648:",phi(1.5*L3)-(1.5*L3-1))
for b in (1.01,1.05,1.2,1.5,2):
    print("b=%.2f (ii) fails for q >"%b,(3**b-3)/(2*(b-1)))
