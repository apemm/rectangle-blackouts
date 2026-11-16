import sys, time
from core import *

def labels(h):
    return [(a,b) for a in range(1,h+1,2) for b in range(2,h+1,2)]

def rot(dx,dy): return (-dy,dx)

def ok_add(h, upper, upset, cells, c, rules):
    """cells: new upper cells (all in column c). upper: list of existing."""
    for (nx,ny) in cells:
        for (ex,ey) in upper:
            dx=abs(nx-ex); dy=abs(ny-ey)
            if 'P1' in rules and dx==dy: return False
            if 'P2' in rules and dx==ny+ey-2 and ny+ey<=h+1: return False
            if 'Iso' in rules:
                vx,vy=ex-nx,ey-ny
                rx,ry=rot(vx,vy)
                cand=[(nx+rx,ny+ry),(nx-rx,ny-ry),(ex+rx,ey+ry),(ex-rx,ey-ry)]
                if (vx+rx)%2==0 and (vy+ry)%2==0:
                    # right angle at P: P = midpoint +- rot(v)/2
                    mx2,my2=nx+ex,ny+ey
                    if mx2%2==0 and my2%2==0 or True:
                        # P = (n+e)/2 +- rot(e-n)/2
                        for sg in (1,-1):
                            px2=mx2+sg*rx; py2=my2+sg*ry
                            if px2%2==0 and py2%2==0: cand.append((px2//2,py2//2))
                for (px,py) in cand:
                    if px==nx or px==ex: continue
                    if py==1 and px>=1: return False
                    if (px,py) in upset: return False
    return True

def greedy(h, rules):
    upper=[]; upset=set(); cols={}; used=set()
    for (a,b) in labels(h):
        c=1
        while True:
            if c not in used:
                cells=[(c,b)]+([(c,a)] if a>=3 else [])
                if ok_add(h,upper,upset,cells,c,rules): break
            c+=1
        used.add(c); cols[c]=(a,b)
        for p in cells: upper.append(p); upset.add(p)
    return cols

def board(h,m,cols):
    S=set()
    for x in range(1,m+1):
        if x in cols:
            a,b=cols[x]; S.add((x,a)); S.add((x,b))
        else: S.add((x,1))
    return S

def kind(R):
    xs={p[0] for p in R}
    ys={p[1] for p in R}
    # axis-aligned if exactly two distinct x and two distinct y
    return "axis" if len(xs)==2 and len(ys)==2 else "diagonal"

def report(h, rules, ms_fn, tag, tmax):
    t=time.time()
    cols=greedy(h,rules); M0=max(cols); q=h*h//4
    out=f"{tag} h={h} q={q} M0={M0} M0/q={M0/q:.3f}"
    print(out, flush=True)
    for m in ms_fn(M0,q,h):
        if time.time()-t>tmax: print(f"   m={m} skipped (time)"); continue
        ok,pair=is_valid(h,m,board(h,m,cols))
        if ok: print(f"   m={m} valid",flush=True)
        else:
            print(f"   m={m} INVALID {pair[0]} [{kind(pair[0])}] vs {pair[1]} [{kind(pair[1])}]",flush=True)
    print(f"   ({time.time()-t:.1f}s)",flush=True)

if __name__=="__main__":
    task=sys.argv[1]; hs=range(int(sys.argv[2]),int(sys.argv[3])+1)
    for h in hs:
        if task=="full": report(h,{'P1','P2','Iso'},lambda M,q,h:[M,M+1,M+2,M+h],"FULL",120)
        if task=="p1p2": report(h,{'P1','P2'},lambda M,q,h:[M,M+h],"P1P2",120)
        if task=="p1": report(h,{'P1'},lambda M,q,h:[M,M+h],"P1",120)
        if task=="none": report(h,set(),lambda M,q,h:[q,q+h],"NONE",120)
