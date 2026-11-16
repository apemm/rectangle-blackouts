from itertools import product
from pathlib import Path
import json
from check_aligned_dyadic_quadratic_k4 import strong_templates,BITS
from check_hilbert_quadratic_clique_exclusions import OPTIONS

CASES=((3,0,13),(63,1,6),(421,0,13),(421,2,13))
for b,t,mask in CASES:
 temp=next(x for x in strong_templates() if x['mask']==mask)
 coeff=temp['coeff'];base=temp['base'];c=128*(4**t)*b;first=t//2+1
 cur={(*o,0,0,0,*(z*c for z in coeff),0,0) for o in product(range(4),repeat=4)}
 maps=[];total=0
 for depth in range(1,61):
  nx={}
  for node in cur:
   st=node[:15];Cd,dd=node[15:];os=st[:4];cr,c1,c2=st[4:7];carry=st[7:]
   for bits in BITS:
    aa,bb,z,w=bits;rel=aa+w-bb-z+cr
    if rel%2:continue
    vals=[bits[base[i]]+carry[i] for i in range(8)];xy=[v%2 for v in vals]
    pq=[OPTIONS[os[i],xy[2*i],xy[2*i+1]] for i in range(4)]
    pp=tuple(v[0] for v in pq);q=tuple(v[1] for v in pq);delta=(q[1]-q[0])%4
    if depth<first and delta:continue
    if depth==first and (delta!=2 if t%2 else not delta%2):continue
    ac=q[0]-2*q[1]+q[2]+c1;bc=q[1]-2*q[2]+q[3]+c2
    if ac%4 or bc%4:continue
    newC=Cd+(bb-aa)*(1<<(depth-1));newd=dd+(q[1]-q[0])*(1<<(2*(depth-1)))
    if depth>=first:
     assert newd%(1<<t)==0
     D=newd//(1<<t);power=min(depth,2*depth-t)
     if (b*(2*newC+1)-9*D*D)%(1<<power):continue
    ns=(*pp,rel//2,ac//4,bc//4,*(v//2 for v in vals),newC,newd)
    nx.setdefault(ns,(node,bits,q))
  cur=set(nx);maps.append(nx);total+=len(cur)
  print('state',b,t,mask,depth,len(cur),flush=True)
  if not cur:break
  accepts=[node for node in cur if not any(node[:15]) and (9*(node[16]//(1<<t))**2)%b==0 and (b*(2*node[15]+1)-9*(node[16]//(1<<t))**2)%(1<<(depth+1))==0]
  if accepts:
   node=accepts[0];bases=[0]*4;ranks=[0]*4
   for j in range(depth-1,-1,-1):
    prev,bits,q=maps[j][node]
    for i in range(4):bases[i]+=bits[i]<<j;ranks[i]+=q[i]<<(2*j)
    node=prev
   d=ranks[1]-ranks[0];D=d//(1<<t);C=bases[1]-bases[0];B0=9*D*D//b;T=(B0-1)//2-C
   pts=[(bases[base[2*i]]+coeff[2*i]*c,bases[base[2*i+1]]+coeff[2*i+1]*c) for i in range(4)]
   result=dict(b=b,t=t,mask=mask,depth=depth,c=c,bases=bases,points=pts,ranks=ranks,d=d,D=D,C=C,B0=B0,T=T)
   Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
   print('ALIGNED',json.dumps(result),flush=True);raise SystemExit
  if len(cur)>200000 or total>1000000:print('MEMORY CAP',flush=True);break
