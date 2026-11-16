# sanity exploration: can K_{2,3} or K_{2,2}+pendant etc. be a corner-triple-free all-double window?
import sys, itertools
def tilted_ok(cols, h):
    k = len(cols)
    black = set()
    for i,(r,s) in enumerate(cols):
        black.add((i+1,r)); black.add((i+1,s))
    pts = sorted(black)
    for X in pts:
        for Y in pts:
            if Y==X: continue
            u=(Y[0]-X[0],Y[1]-X[1])
            if u[0]==0 or u[1]==0: continue
            for Z in pts:
                if Z<=Y or Z==X: continue
                v=(Z[0]-X[0],Z[1]-X[1])
                if u[0]*v[0]+u[1]*v[1]!=0: continue
                F=(Y[0]+Z[0]-X[0],Y[1]+Z[1]-X[1])
                if 1<=F[0]<=k and 1<=F[1]<=h:
                    return False
    return True
h=int(sys.argv[1])
found=0
for A in itertools.combinations(range(1,h+1),2):
    rest=[r for r in range(1,h+1) if r not in A]
    for B in itertools.combinations(rest,3):
        pairs=[(min(a,b),max(a,b)) for a in A for b in B]
        for perm in itertools.permutations(pairs):
            if perm[0]>perm[-1]: continue
            if tilted_ok(perm,h):
                found+=1
                if found<=5: print('h',h,'A',A,'B',B,perm)
print('h',h,'K23 corner-free windows (up to reversal):',found)
