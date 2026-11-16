# Sanity check: R_IV^(4) edge count on [1,X] is O(X); g = gcd(F, be-al) divides 5.
from math import gcd
import sys
X = int(sys.argv[1]) if len(sys.argv)>1 else 10**6
k = 4
lams = []
gset = set()
be = 3
while True:
    found = False
    for al in range(1, be, 2):
        if gcd(al, be) != 1: continue
        d = be - al
        if (d & ((1 << (k-2)) - 1)) != 0: continue
        F = 4*(al - 2*be)**2 + be**2
        g = gcd(F, d)
        gset.add(g)
        q = al*F//g
        p = (al*F + 4*d*be*be)//g
        assert (al*F) % g == 0 and (al*F + 4*d*be*be) % g == 0
        assert gcd(p, q) == 1, (al, be, p, q)
        if p <= X:
            lams.append((al, be, q, p)); found = True
        if al*be*be > 5*X: break
    if be*be > 5*X: break
    be += 2
edges = 0
for (al, be, q, p) in lams:
    edges += (X//p + 1)//2   # odd m with p*m <= X
print("X", X, "lambdas with p<=X:", len(lams), "g values:", sorted(gset))
print("edges on [1,X]:", edges, " edges/X:", edges/X)
print("smallest (q,p):", sorted(lams, key=lambda t: t[3])[:5])
s = sum(1.0/p + 1.0/q for (_,_,q,p) in lams)
print("sum over lambdas of 1/p+1/q:", s)
