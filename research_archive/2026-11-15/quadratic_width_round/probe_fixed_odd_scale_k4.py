from itertools import product
from pathlib import Path
from check_aligned_dyadic_quadratic_k4 import strong_templates,BITS
from check_hilbert_quadratic_clique_exclusions import OPTIONS
import json

def run(temp,b,t=0):
 coef=temp['coeff'];base=temp['base'];c=128*(4**t)*b;first=t//2+1;target=(b-1)//2%4
 initial={(*o,0,0,0,*(a*c for a in coef),0) for o in product(range(4),repeat=4)}
 cur=initial;maps=[];seen={}
 for depth in range(1,70):
  nxmap={}
  for node in cur:
   st=node[:15];Cmod=node[15];os=st[:4];cr,c1,c2=st[4:7];carry=st[7:]
   for bits in BITS:
    a,bb,z,w=bits;rel=a+w-bb-z+cr
    if rel%2:continue
    nC=(Cmod+(bb-a)*(1<<(depth-1)))%4
    if depth==2 and nC!=target:continue
    vals=[bits[base[i]]+carry[i] for i in range(8)];xy=[v%2 for v in vals]
    pq=[OPTIONS[os[i],xy[2*i],xy[2*i+1]] for i in range(4)]
    pp=tuple(v[0] for v in pq);q=tuple(v[1] for v in pq);dd=(q[1]-q[0])%4
    if depth<first and dd:continue
    if depth==first and (dd!=2 if t%2 else not dd%2):continue
    ac=q[0]-2*q[1]+q[2]+c1;bc=q[1]-2*q[2]+q[3]+c2
    if ac%4 or bc%4:continue
    ns=(*pp,rel//2,ac//4,bc//4,*(v//2 for v in vals),nC)
    nxmap.setdefault(ns,(node,bits,q))
  cur=set(nxmap);maps.append(nxmap)
  accept=(*([0]*15),target)
  if accept in cur:
   node=accept;bases=[0]*4;ranks=[0]*4
   for j in range(depth-1,-1,-1):
    prev,bits,q=maps[j][node]
    for i in range(4):bases[i]+=bits[i]<<j;ranks[i]+=q[i]<<(2*j)
    node=prev
   d=ranks[1]-ranks[0];D=d//(1<<t);C0=bases[1]-bases[0];n=1<<depth
   div=(9*D*D)%b==0
   diff=9*D*D-b*(2*C0+1)
   valuation=(abs(diff)&-abs(diff)).bit_length()-1 if diff else 9999
   result=dict(b=b,t=t,mask=temp['mask'],depth=depth,c=c,bases=bases,ranks=ranks,d=d,D=D,C=C0,
               norm_v2=valuation,odd_divisibility=div,aligned=div and valuation>=depth+1)
   return result
  if not cur:return None
  if depth>=max(2,first):
   fs=frozenset(cur)
   if fs in seen:return None
   seen[fs]=depth
 return {'limit':True,'b':b,'mask':temp['mask'],'t':t}

results=[]
for b in (3,5,7,9,11,13,15):
 count=0
 for temp in strong_templates():
  result=run(temp,b)
  if result:
   results.append(result);count+=1
   if result.get('aligned'):
    print('ALIGNED',json.dumps(result),flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(results,indent=2)+'\n')
    raise SystemExit
 print('b',b,'geometric_admissible',count,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(results,indent=2)+'\n')
print('finished',len(results),'max_residue',max(r.get('norm_v2',0) for r in results),flush=True)
