import math
E=lambda a:(1+3**a)/2
th=lambda a:(E(a)+1)/(1+a)
lo,hi=0.5,1.5
for _ in range(200):
    m1=lo+(hi-lo)/3; m2=hi-(hi-lo)/3
    if th(m1)<th(m2): hi=m2
    else: lo=m1
a=(lo+hi)/2; t=th(a)
print("a*=%.7f theta*=%.7f c=%.7f 4^a=%.4f"%(a,t,2-t,4**a))
# board exponent with Prop 3: max(x, E(a)+1-a x, 2-x) on grid
best=min((max(x,E(a)+1-a*x,2-x),x) for x in [1+i*1e-5 for i in range(100001)])
print("grid min over x at a*:",best)
print("v2 exponent max(x,E(.91)+1-.91x,3-x) at 1.5:",max(1.5,E(.91)+1-.91*1.5,1.5))
print("light width const 512*4*80*16*2.08 =",512*4*80*16*2.08)
# (P1) bounds
for h in (1501,2003,2501,4000): print(h,(h-623)//448+1)
# U1 thresholds: h^2/8+3h/2 < (1.04h)^2 for h>=?
print(all(h*h/8+1.5*h<(1.04*h)**2 for h in range(10,10**5)))
# 64p-4(A-1) > 2W_h+1 range with p>40h
print(max(h for h in range(10,20000) if 64*40*h-4*((h+1)//2-1) > 2*(((h-1)**2)//4+1)+1))
