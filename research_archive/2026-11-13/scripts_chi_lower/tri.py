# triangles through 0 in Gamma restricted to (1/T)Z, T = l or 5l; list lucky primes
import sys, time
from sinf import S, adj
from sympy import isprime
def tris(T,B):
    s=S(T,B); V=sorted(set(s)|{-d for d in s}); hub=-(T//5) if T%5==0 else None
    out=[]
    for i in range(len(V)):
        for j in range(i+1,len(V)):
            a,b=V[i],V[j]
            if hub is not None and (hub in (a,b) or -hub in (a,b) or abs(a-b)==abs(hub)): continue
            if adj(T,b-a): out.append((a,b))
    return out
t0=time.time()
lucky=[];unl=[]
for l in range(11,int(sys.argv[1])):
    if not isprime(l) or l%5 not in (1,4): continue
    tr=tris(l,10**int(sys.argv[2])); tr5=tris(5*l,10**int(sys.argv[2]))
    (lucky if (tr or tr5) else unl).append(l)
    pass
print("lucky",lucky); print("unlucky",unl); print("t=%.1f"%(time.time()-t0))
