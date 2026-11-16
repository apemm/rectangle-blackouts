# sanity exploration: number of corner-triple-free all-double windows by width (K_{A,B} pairs)
import sys, time, itertools
def run(h, A, tl=50):
    B=[r for r in range(1,h+1) if r not in A]
    pairs=[(min(r,s),max(r,s)) for r in A for s in B]
    q=len(pairs)
    counts=[0]*(q+2)
    examples={}
    t0=time.time()
    pts=[]   # black points list
    used=set()
    cols=[]
    limit=[10**9]
    def new_ok(c, newpts):
        # check all tilted right angles involving a new point; return (ok, newlimit)
        lim=10**9
        allp=pts+newpts
        n=len(allp)
        for N in newpts:
            for i in range(n):
                P=allp[i]
                if P==N: continue
                for j in range(i+1,n):
                    Q=allp[j]
                    if Q==N: continue
                    # three points N,P,Q: test right angle at each
                    for (X,Y,Z) in ((N,P,Q),(P,N,Q),(Q,N,P)):
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
        counts[c]+=1
        if c not in examples: examples[c]=[]
        if len(examples[c])<3: examples[c].append(list(cols))
        if time.time()-t0>tl: return
        if c==q or c+1>lim: return
        for pr in pairs:
            if pr in used: continue
            newpts=[(c+1,pr[0]),(c+1,pr[1])]
            ok, l2 = new_ok(c+1,newpts)
            if not ok: continue
            used.add(pr); cols.append(pr); pts.extend(newpts)
            dfs(c+1, min(lim,l2))
            pts.pop(); pts.pop(); cols.pop(); used.discard(pr)
    dfs(0,10**9)
    return counts, examples, time.time()-t0
if __name__=='__main__':
    h=int(sys.argv[1])
    A=tuple(int(t) for t in sys.argv[2].split(','))
    counts,ex,el=run(h,A)
    print('h',h,'A',A,'counts by width',[c for c in counts if c], 'sec',round(el,1))
    w=max(i for i,c in enumerate(counts) if c)
    for e in ex[w]: print('  ',' '.join('%d-%d'%p for p in e))
