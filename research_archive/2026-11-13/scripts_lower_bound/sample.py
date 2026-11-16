# sanity exploration: list corner-triple-free all-double windows of a given width (parity partition)
import sys, time, random, collections
def run(h, A, target, maxlist=40):
    B=[r for r in range(1,h+1) if r not in A]
    pairs=[(min(r,s),max(r,s)) for r in A for s in B]
    q=len(pairs)
    res=[]
    pts=[]; used=set(); cols=[]
    def new_ok(c, newpts):
        lim=10**9
        allp=pts+newpts
        n=len(allp)
        for Nn in newpts:
            for i in range(n):
                P=allp[i]
                if P==Nn: continue
                for j in range(i+1,n):
                    Q=allp[j]
                    if Q==Nn: continue
                    for (X,Y,Z) in ((Nn,P,Q),(P,Nn,Q),(Q,Nn,P)):
                        ux=Y[0]-X[0]; uy=Y[1]-X[1]; vx=Z[0]-X[0]; vy=Z[1]-X[1]
                        if ux*vx+uy*vy!=0: continue
                        if ux==0 or uy==0: continue
                        fy=Y[1]+Z[1]-X[1]
                        if fy<1 or fy>h: continue
                        fx=Y[0]+Z[0]-X[0]
                        if fx<1: continue
                        if fx<=c: return False, lim
                        lim=min(lim,fx-1)
        return True, lim
    def dfs(c, lim):
        if c==target:
            res.append(list(cols)); return
        if c+1>lim: return
        for pr in pairs:
            if pr in used: continue
            newpts=[(c+1,pr[0]),(c+1,pr[1])]
            ok, l2 = new_ok(c+1,newpts)
            if not ok: continue
            used.add(pr); cols.append(pr); pts.extend(newpts)
            dfs(c+1, min(lim,l2))
            pts.pop(); pts.pop(); cols.pop(); used.discard(pr)
    dfs(0,10**9)
    return res
h=int(sys.argv[1]); A=tuple(int(t) for t in sys.argv[2].split(',')); target=int(sys.argv[3])
res=run(h,A,target)
print(len(res),'windows of width',target)
# statistics: number of consecutive column pairs sharing a row; row usage profile
shareprof=collections.Counter(); 
for w in res:
    sh=sum(1 for i in range(len(w)-1) if set(w[i])&set(w[i+1]))
    shareprof[sh]+=1
print('number of adjacent pairs sharing a row -> count',sorted(shareprof.items()))
offs=collections.Counter()
for w in res:
    offs[tuple(sorted(p[1]-p[0] for p in w))]+=1
print('offset multisets (top 8):',offs.most_common(8))
random.seed(1)
for w in random.sample(res,min(25,len(res))):
    print('  ',' '.join('%d%d'%p for p in w))
