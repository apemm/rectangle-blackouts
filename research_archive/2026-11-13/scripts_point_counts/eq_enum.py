import sys
from math import gcd
def spf_sieve(n):
    s=list(range(n+1))
    for i in range(2,int(n**.5)+1):
        if s[i]==i:
            for j in range(i*i,n+1,i):
                if s[j]==j: s[j]=i
    return s
def fac(n,spf,d):
    while n>1:
        p=spf[n]; d[p]=d.get(p,0)+1; n//=p
def divs(d):
    r=[1]
    for p,a in d.items():
        r=[x*p**k for x in r for k in range(a+1)]
    return r
def EQ(Q,spf):
    out=[]
    for e in range(1,(Q+1)//2):
        if 2*e>=Q: break
        d={}; fac(e,spf,d); fac(Q-e,spf,d)
        N=e*(Q-e)
        for s in divs(d):
            t=N//s
            if (s*s+e*e)%(s+t)==0:
                Y=(s*s+e*e)//(s+t); n1=s-Y; X=t-n1
                if n1>=1 and Y>=1 and X>=1:
                    out.append((e,n1,X,Y)); 
    return out
if __name__=='__main__':
    Qs=[int(a) for a in sys.argv[1:]]
    spf=spf_sieve(max(Qs))
    for Q in Qs:
        o=EQ(Q,spf); es=sorted(set(x[0] for x in o))
        print(Q,'|E|',len(es),'pts',len(o), es[:20])
