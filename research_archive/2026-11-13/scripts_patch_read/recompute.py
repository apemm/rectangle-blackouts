from math import log
E=lambda a:(1+3**a)/2
f=lambda a:(E(a)+1)/(1+a)
lo,hi=0.1,3.0
for _ in range(200):
    m1=lo+(hi-lo)/3; m2=hi-(hi-lo)/3
    if f(m1)<f(m2): hi=m2
    else: lo=m1
a=(lo+hi)/2; th=f(a)
print('a*=%.7f theta*=%.7f E=%.7f 4^a=%.4f 2-th=%.7f'%(a,th,E(a),4**a,2-th))
# exponent of max(x, E(a)+1-a x, 2-x) minimized over a and x
best=min((max(x,min(E(b)+1-b*x for b in [i/2000 for i in range(1,6000)]),2-x),x) for x in [1.49+i*1e-5 for i in range(1000)])
print('grid minmax',best)
print('width const',512*4*80*16*2.08)
h=1e10;L=log(h)
print('Lambda ratio',(1+L)/L,'ell ratio',(1+log(log(3*h)))/log(L),'(1+1/L)^3',(1+1/L)**3)
print('1+10/614',1+10/614)
print('2F-L',2*1000-13,2*3743-1)
for s in [0.5,a,1.0,2.0]:
    print('s',round(s,4),'3^s-1',3**s-1,'2(2^s-1)',2*(2**s-1))
ok=all(100*(2*((hh-1)**2//4+1)+1)<=50*hh*hh+300 for hh in range(3,20000))
print('100 gaps <= 50h^2+300',ok)
