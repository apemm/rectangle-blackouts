import sys
from math import gcd
from collections import Counter
h=int(sys.argv[1])
sols=[]
for e in range(78,h):
    for s in range(2, e//77+1):
        g=gcd(e,s*s); step=e//g
        n1=step
        while n1<s:
            Y=s-n1
            num=n1*(e*e+s*s)
            if num%(e*Y)==0:
                u2=num//(e*Y)
                if e+u2<=h-1 and (e*u2)%n1==0 and e*u2//n1 - Y>=78*h:
                    sols.append((n1,Y,e,u2))
            n1+=step
print('h',h,'count',len(sols))
ys=Counter(); smax=0
for (n1,Y,e,u2) in sols:
    s=n1+Y; sg=gcd(e,s); ys[s//sg]+=1; smax=max(smax,s)
print('y dist',sorted(ys.items())[:15],'smax',smax,'h^.5',round(h**.5))
# e-involution integrality: e'=s^2/e integer?
print('ratio u2/h quantiles', sorted(round(u2/h,2) for (_,_,_,u2) in sols)[::max(1,len(sols)//8)])
