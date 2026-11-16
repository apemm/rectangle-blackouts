# sanity exploration: class functions with complementary row usage; how many distinct pairs can they realize?
import sys, collections
from class_functions import run
h=int(sys.argv[1]); w=h*h//4; cap=h//2
c0,s0,_,_=run(h,w,cap,0,20); c1,s1,_,_=run(h,w,cap,1,20)
byuse=collections.defaultdict(list)
for psi in s1:
    u=[0]*(h+1)
    for y in psi: u[y]+=1
    byuse[tuple(u)].append(psi)
best=0; bestex=None; n=0
hist=collections.Counter()
for phi in s0:
    u=[0]*(h+1)
    for y in phi: u[y]+=1
    comp=tuple([0]+[cap-u[r] for r in range(1,h+1)])
    for psi in byuse.get(comp,()):
        n+=1
        d=len(set((min(a,b),max(a,b)) for a,b in zip(phi,psi)))
        hist[d]+=1
        if d>best: best=d; bestex=(phi,psi)
print('h',h,'complementary (phi,psi) pairs:',n,'histogram of number of distinct row pairs:',sorted(hist.items()))
print('best',best,'of',w)
print(' phi',bestex[0]); print(' psi',bestex[1])
# print a few complementary examples with usage vectors
k=0
for phi in s0:
    u=[0]*(h+1)
    for y in phi: u[y]+=1
    comp=tuple([0]+[cap-u[r] for r in range(1,h+1)])
    if comp in byuse and k<6:
        k+=1
        print('usage',u[1:],'phi',phi,'psi example',byuse[comp][0])
