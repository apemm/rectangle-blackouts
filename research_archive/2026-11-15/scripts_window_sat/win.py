"""SAT search for all-double windows.

A window of width k at height h is a set of points with 2 points in every
column, in rows on opposite sides of a balanced partition of the rows, with
distinct row pairs, such that every tilted lattice rectangle of the h x k
grid has at most 2 corners in the set.

Usage:  python win.py h k        (partition left free)
        python win.py h k par    (parity partition)
Needs the PySAT package.
"""
import sys, time
from math import gcd
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool

def rects(h,k):
    out=[]
    for a in range(1,k):
        for b in range(1,h):
            g=gcd(a,b); ux,uy=-b//g,a//g
            t=1
            while True:
                ex,ey=t*ux,t*uy
                if -ex+a>k-1 or b+ey>h-1: break
                # Z=(x,y), corners Z, Z+(a,b), Z+(ex,ey), Z+(a+ex,b+ey); x range
                for x in range(1-ex if ex<0 else 1, k-a+1):
                    if x+ex<1 or x+a>k: continue
                    for y in range(1,h-(b+ey)+1):
                        out.append(((x,y),(x+a,y+b),(x+ex,y+ey),(x+a+ex,y+b+ey)))
                t+=1
    return out

def build(h,k,parity=False,fixA=None):
    vp=IDPool(); P=lambda x,r: vp.id(('p',x,r)); S=lambda r: vp.id(('s',r))
    cl=[]
    for x in range(1,k+1):
        e=CardEnc.equals(lits=[P(x,r) for r in range(1,h+1)],bound=2,vpool=vp,encoding=EncType.seqcounter)
        cl+=e.clauses
        for r in range(1,h+1):
            for r2 in range(r+1,h+1):
                cl.append([-P(x,r),-P(x,r2),S(r),S(r2)]); cl.append([-P(x,r),-P(x,r2),-S(r),-S(r2)])
                for x2 in range(x+1,k+1):
                    cl.append([-P(x,r),-P(x,r2),-P(x2,r),-P(x2,r2)])
    if parity:
        for r in range(1,h+1): cl.append([S(r) if r%2 else -S(r)])
    elif fixA is not None:
        for r in range(1,h+1): cl.append([S(r) if r in fixA else -S(r)])
    else:
        e=CardEnc.equals(lits=[S(r) for r in range(1,h+1)],bound=(h+1)//2,vpool=vp,encoding=EncType.seqcounter); cl+=e.clauses
    R=rects(h,k)
    for c in R:
        v=[P(*q) for q in c]
        for i in range(4):
            cl.append([-v[j] for j in range(4) if j!=i])
    return vp,cl,P,S,len(R)

def solve(h,k,**kw):
    t=time.time(); vp,cl,P,S,nr=build(h,k,**kw)
    s=Cadical153(bootstrap_with=cl); ok=s.solve()
    res=None
    if ok:
        m=set(l for l in s.get_model() if l>0)
        res=[tuple(r for r in range(1,h+1) if P(x,r) in m) for x in range(1,k+1)]
        A=[r for r in range(1,h+1) if S(r) in m]
        res=(res,A)
    return ok,res,nr,time.time()-t

if __name__=="__main__":
    h=int(sys.argv[1]); k=int(sys.argv[2]); par=len(sys.argv)>3 and sys.argv[3]=='par'
    ok,res,nr,dt=solve(h,k,parity=par)
    print(h,k,'parity' if par else 'any', 'SAT' if ok else 'UNSAT', 'rects',nr,'%.1fs'%dt, flush=True)
    if ok: print(res)
