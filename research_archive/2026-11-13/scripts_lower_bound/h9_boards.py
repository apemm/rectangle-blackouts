# sanity check: list all saturated parity boards at h=9 without 45-degree corner triples; test F45-validity by definition
import sys, time
from class_functions import run
from f45_search import f45_valid
h=9; q=20
deg={r:(4 if r%2==1 else 5) for r in range(1,h+1)}
c0,s0,to0,_=run(h,q,5,0,20); c1,s1,to1,_=run(h,q,5,1,20)
assert not to0 and not to1 and len(s0)==c0 and len(s1)==c1
byuse={}
for psi in s1:
    use=[0]*(h+1)
    for y in psi: use[y]+=1
    byuse.setdefault(tuple(use),[]).append(psi)
boards=[]
for phi in s0:
    use=[0]*(h+1)
    for y in phi: use[y]+=1
    if any(use[r]>deg[r] for r in range(1,h+1)): continue
    comp=tuple([0]+[deg[r]-use[r] for r in range(1,h+1)])
    for psi in byuse.get(comp,()):
        prs=[(min(a,b),max(a,b)) for a,b in zip(phi,psi)]
        if len(set(prs))==q: boards.append(prs)
print('boards:',len(boards))
nv=0
for b in boards:
    v=f45_valid(b,h)
    nv+=v
    print(' '.join('%d%d'%p for p in b),'| F45-valid (definition):',v)
print('F45-valid boards:',nv)
