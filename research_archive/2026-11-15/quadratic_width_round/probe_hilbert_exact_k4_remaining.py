from pathlib import Path
from itertools import product
from check_hilbert_quadratic_clique_exclusions import OPTIONS
src=Path(__file__).with_name('probe_hilbert_all_strong_power_two.py').read_text()
exec(src.split('cache={}')[0])
for mask,edges,pos,coef,baseid in templates():
 if mask not in (6,20,43,57):continue
 C=512
 cur={(*o,0,0,0,*(a*C for a in coef)) for o in product(range(4),repeat=4)}
 maps=[];sets={}
 for depth in range(1,40):
  nxmap={}
  for st in cur:
   os=st[:4];cr,c1,c2=st[4:7];carry=st[7:]
   for bits in product(range(2),repeat=4):
    a,b,z,w=bits;rel=a+w-b-z+cr
    if rel%2:continue
    vals=[bits[baseid[i]]+carry[i] for i in range(8)]
    raw=[v%2 for v in vals]
    pq=[OPTIONS[os[i],raw[2*i],raw[2*i+1]] for i in range(4)]
    pp=tuple(v[0] for v in pq);qq=tuple(v[1] for v in pq)
    if depth==1 and (qq[1]-qq[0])%4!=2:continue
    ac=qq[0]-2*qq[1]+qq[2]+c1;bc=qq[1]-2*qq[2]+qq[3]+c2
    if ac%4 or bc%4:continue
    ns=(*pp,rel//2,ac//4,bc//4,*(v//2 for v in vals))
    if ns not in nxmap:nxmap[ns]=(st,bits,qq)
  cur=set(nxmap);maps.append(nxmap)
  if (0,)*15 in cur:
   st=(0,)*15;bases=[0]*4;ranks=[0]*4
   for j in range(depth-1,-1,-1):
    prev,bits,qq=maps[j][st]
    for i in range(4):bases[i]+=bits[i]<<j;ranks[i]+=qq[i]<<(2*j)
    st=prev
   pts=[(bases[baseid[2*i]]+coef[2*i]*C,bases[baseid[2*i+1]]+coef[2*i+1]*C) for i in range(4)]
   d=ranks[1]-ranks[0];C0=bases[1]-bases[0];B0=(96*d)**2//(8*C);T=(B0-1)//2-C0
   print('FOUND',dict(mask=mask,depth=depth,c=C,bases=bases,pts=pts,ranks=ranks,d=d,Tmod=T%(1<<depth),Tmod8=T%8,edges=edges),flush=True)
   break
  fs=frozenset(cur)
  if fs in sets:print('EXCLUDED',mask,sets[fs],depth,len(cur));break
  sets[fs]=depth
