import sys
from math import gcd
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
                if e+u2<=h-1:
                    D=e*u2//n1 - Y  # Delta (need n1|e u2)
                    if (e*u2)%n1==0 and D>=78*h:
                        sols.append((n1,Y,e,u2,D))
            n1+=step
print(h,len(sols))
for t in sols[:60]:
    n1,Y,e,u2,D=t; s=n1+Y; sg=gcd(e,s)
    print(t,'s',s,'sig',sg,'x',e//sg,'y',s//sg,'c',n1*sg*sg//e, 'D/h',round(D/h,1))
