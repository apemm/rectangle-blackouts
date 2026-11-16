import sys
from collections import Counter
h, s = int(sys.argv[1]), int(sys.argv[2])
def isprime(n):
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return n>1
A=(h+1)//2; K=h//2
p=max(20*h,(s*s//2+4)*h)+1
while not isprime(p): p+=1
P=p
def slots(T):
    st=(T-1)//2
    return [i for i in range(A) if 0<=i+st<K]
offs=[T for T in range(-h+1,h) if T%2 and slots(T)]
Q=lambda T,a:(s*s+4)*a*a+4*a*T+T*T
bylen={}
for T2 in offs:
    for b in range(-A,A+1):
        if b: bylen.setdefault(Q(T2,b),[]).append((T2,b))
st=Counter()
amax=2*(h-1)**2//(s*s*(2*P-h-1))+1
for T in offs:
    for a in range(-amax,amax+1):
        if a==0: continue
        kap=(s*s+4)*a+2*T
        for (T2,b) in bylen.get(Q(T,a),[]):
            if (b,T2) in ((a,T),(-a,-T)): continue
            st['rep']+=1
            for dc in range(-20,21):
                if dc==0: continue
                num=-(2*s*s*a*P*dc+(2*a+T)*(T2-T))
                st['dc']+=1
                if num%kap: continue
                m=num//kap
                st['int']+=1
                if abs(m)>=2*A: continue
                st['range']+=1
                if (m+a-b)%2: continue
                st['par']+=1
                e=(m+a-b)//2
                sl=set(slots(T)); sl2=set(slots(T2))
                n=sum(1 for i in sl if i+a in sl and i+e in sl2 and i+e+b in sl2)
                if n:
                    st["slot"]+=1; st["slotcount"]+=n
                    if st["slot"]<=5: print("HIT T",T,"a",a,"T2",T2,"b",b,"dc",dc,"m",m,"e",e,"n",n)
print(h,s,P,amax,dict(st))
