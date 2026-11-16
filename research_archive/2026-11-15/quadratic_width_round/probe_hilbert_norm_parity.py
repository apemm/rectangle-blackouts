from pathlib import Path
from itertools import product
from check_hilbert_quadratic_clique_exclusions import OPTIONS
src=Path(__file__).with_name('probe_hilbert_all_strong_power_two.py').read_text()
exec(src.split('cache={}')[0])
counts={}
for t in range(6):
 totals={}
 for mask,edges,pos,coef,baseid in templates():
  C=128*(4**t);first=t//2+1
  cur={(*o,0,0,0,*(a*C for a in coef)) for o in product(range(4),repeat=4)}
  seen={};status='LIMIT'
  for depth in range(1,60):
   new=set()
   for st in cur:
    os=st[:4];cr,c1,c2=st[4:7];carry=st[7:]
    for bits in product(range(2),repeat=4):
     a,b,z,w=bits
     if depth<=2 and a!=b:continue
     rel=a+w-b-z+cr
     if rel%2:continue
     vals=[bits[baseid[i]]+carry[i] for i in range(8)]
     raw=[v%2 for v in vals]
     pq=[OPTIONS[os[i],raw[2*i],raw[2*i+1]] for i in range(4)]
     pp=tuple(v[0] for v in pq);qq=tuple(v[1] for v in pq)
     dd=(qq[1]-qq[0])%4
     if depth<first and dd!=0:continue
     if depth==first and (dd!=2 if t%2 else dd%2==0):continue
     ac=qq[0]-2*qq[1]+qq[2]+c1;bc=qq[1]-2*qq[2]+qq[3]+c2
     if ac%4 or bc%4:continue
     new.add((*pp,rel//2,ac//4,bc//4,*(v//2 for v in vals)))
   cur=new
   if (0,)*15 in cur:status='ACCEPT';break
   if not cur:status='EMPTY';break
   if depth>=max(2,first):
    fs=frozenset(cur)
    if fs in seen:status='CYCLE';break
    seen[fs]=depth
  totals[status]=totals.get(status,0)+1
  if status in ('ACCEPT','LIMIT'):print('FLAG',t,mask,status,depth,len(cur),flush=True)
 counts[t]=totals
 print(t,totals,flush=True)
