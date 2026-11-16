# cross-validation of class_functions.run against a definition-level brute force
import itertools, sys
from class_functions import run
def brute(h,w,cap,par):
    rows=[[y for y in range(1,h+1) if (x+y)%2==par] for x in range(1,w+1)]
    rects=[]
    for x in range(1,w+1):
        for y in range(1,h+1):
            for s in range(1,h):
                for t in range(1,h):
                    c=((x,y),(x+s,y+s),(x+t,y-t),(x+s+t,y+s-t))
                    if all(1<=p[0]<=w and 1<=p[1]<=h for p in c): rects.append(c)
    n=0; sols=set()
    for f in itertools.product(*rows):
        if max(f.count(r) for r in set(f))>cap: continue
        S=set((i+1,f[i]) for i in range(w))
        if all(sum(1 for p in c if p in S)<=2 for c in rects):
            n+=1; sols.add(f)
    return n,sols
ok=True
for (h,w,cap,par) in [(6,6,3,0),(6,7,3,1),(6,9,3,0),(6,9,9,0),(8,8,4,0),(8,9,4,1),(5,6,3,0),(7,8,4,1)]:
    n,sols=brute(h,w,cap,par)
    c,s2,to,el=run(h,w,cap,par,30)
    same = (n==c and sols==set(s2))
    ok = ok and same
    print((h,w,cap,par),'brute',n,'dfs',c,'identical sets:',same)
print('ALL OK' if ok else 'MISMATCH')
