# sanity exploration: max width of all-double windows (K_{A,B} pairs) under sub-families of tilted rectangles.
# fam: 'all', 'adj' (a side with |dx|=1), 'd45' (45-degree rectangles only), 'unit' (side (1,+-1) i.e. dx=1,|dy|=1)
# iterative deepening on best width with time limit; DFS order randomized by seed for a quick lower bound.
import sys, time, random
def run(h, A, fam, tl=50, seed=0):
    B=[r for r in range(1,h+1) if r not in A]
    pairs=[(min(r,s),max(r,s)) for r in A for s in B]
    q=len(pairs)
    rng=random.Random(seed)
    best=[0,None]
    t0=time.time()
    pts=[]; used=set(); cols=[]
    complete=[True]
    def allowed(ux,uy,vx,vy):
        if fam=='all': return True
        if fam=='adj': return abs(ux)==1 or abs(vx)==1
        if fam=='d45': return abs(ux)==abs(uy) and abs(vx)==abs(vy)
        if fam=='unit': return (abs(ux)==1 and abs(uy)==1) or (abs(vx)==1 and abs(vy)==1)
        raise ValueError
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
                        if not allowed(ux,uy,vx,vy): continue
                        fy=Y[1]+Z[1]-X[1]
                        if fy<1 or fy>h: continue
                        fx=Y[0]+Z[0]-X[0]
                        if fx<1: continue
                        if fx<=c: return False, lim
                        lim=min(lim,fx-1)
        return True, lim
    def dfs(c, lim):
        if c>best[0]:
            best[0]=c; best[1]=list(cols)
        if time.time()-t0>tl:
            complete[0]=False; return
        if c==q or c+1>lim: return
        order=pairs[:]
        if seed: rng.shuffle(order)
        for pr in order:
            if pr in used: continue
            newpts=[(c+1,pr[0]),(c+1,pr[1])]
            ok, l2 = new_ok(c+1,newpts)
            if not ok: continue
            used.add(pr); cols.append(pr); pts.extend(newpts)
            dfs(c+1, min(lim,l2))
            pts.pop(); pts.pop(); cols.pop(); used.discard(pr)
            if not complete[0]: return
    dfs(0,10**9)
    return best, complete[0], time.time()-t0, q
if __name__=='__main__':
    h=int(sys.argv[1]); A=tuple(int(t) for t in sys.argv[2].split(',')); fam=sys.argv[3]
    tl=float(sys.argv[4]) if len(sys.argv)>4 else 50
    seed=int(sys.argv[5]) if len(sys.argv)>5 else 0
    best,comp,el,q=run(h,A,fam,tl,seed)
    print('h',h,'A',A,'fam',fam,'q',q,'best width',best[0],'complete' if comp else 'TIMEOUT (lower bound only)','sec',round(el,1))
    print('  ',' '.join('%d-%d'%p for p in best[1]))
