from pathlib import Path
from itertools import product
from collections import deque
import json
from check_aligned_dyadic_quadratic_k4 import strong_templates,BITS
from check_hilbert_quadratic_clique_exclusions import OPTIONS
from check_hilbert_cross_order_independent import cell_from_rank
from check_hilbert_endpoint_p_obstruction import rank

L=6;K=7;MASK=13
TEMPLATE=next(x for x in strong_templates() if x['mask']==MASK)
COEF=TEMPLATE['coeff'];BASE=TEMPLATE['base']

def steps(st,cb):
 os=st[:4];c0,c1,c2=st[4:7];carry=st[7:]
 for bits in BITS:
  a,b,z,w=bits;rel=a+w-b-z+c0
  if rel%2:continue
  values=[bits[BASE[i]]+COEF[i]*cb+carry[i] for i in range(8)]
  xy=[v%2 for v in values]
  pq=[OPTIONS[os[i],xy[2*i],xy[2*i+1]] for i in range(4)]
  parent=tuple(v[0] for v in pq);q=tuple(v[1] for v in pq)
  first=q[0]-2*q[1]+q[2]+c1;second=q[1]-2*q[2]+q[3]+c2
  if first%4 or second%4:continue
  yield (*parent,rel//2,first//4,second//4,*(v//2 for v in values)),bits,q

initial={(*o,0,0,0,*([0]*8),0,0) for o in product(range(4),repeat=4)}
cur=initial;prefix=[]
for depth in range(1,K+1):
 nx={}
 for node in cur:
  st=node[:15];cr,dr=node[15:]
  for new,bits,q in steps(st,0):
   if depth==1 and (q[1]-q[0])%2==0:continue
   cc=(cr+(bits[1]-bits[0])*(1<<(depth-1)))%(1<<(L-1))
   dd=(dr+(q[1]-q[0])*(1<<(2*(depth-1))))%(1<<L)
   key=(*new,cc,dd)
   if key not in nx:nx[key]=(node,bits,q)
 cur=set(nx);prefix.append(nx);print('prefix',depth,len(cur),flush=True)
compressed={}
for node in cur:
 st=node[:15];cc,dd=node[15:]
 target=(9*dd*dd*pow(2*cc+1,-1,1<<L))%(1<<L)
 key=(*st,target)
 compressed.setdefault(key,node)
cur=set(compressed);post=[]
for j in range(L):
 nx={}
 for node in cur:
  st=node[:15];target=node[15];cb=(target>>j)&1
  for new,bits,q in steps(st,cb):
   key=(*new,target)
   if key not in nx:nx[key]=(node,bits,q,cb)
 cur=set(nx);post.append(nx);print('normbits',j+1,len(cur),flush=True)
roots={}
for node in cur:roots.setdefault(node[:15],node)
seen=set(roots);todo=deque(roots);back={};accept=None
while todo:
 st=todo.popleft()
 if not any(st):accept=st;break
 for cb in (0,1):
  for new,bits,q in steps(st,cb):
   if new not in seen:
    seen.add(new);todo.append(new);back[new]=(st,bits,q,cb)
 if len(seen)>200000:raise RuntimeError('state cap')
print('closure',len(seen),'accept',accept is not None,flush=True)
if accept is None:raise SystemExit
trail=[];st=accept
while st not in roots:
 prev,bits,q,cb=back[st];trail.append((bits,q,cb));st=prev
node=roots[st]
for j in range(L-1,-1,-1):
 prev,bits,q,cb=post[j][node];trail.append((bits,q,cb));node=prev
node=compressed[node]
for j in range(K-1,-1,-1):
 prev,bits,q=prefix[j][node];trail.append((bits,q,0));node=prev
trail.reverse();bases=[0]*4;ranks=[0]*4;c=0
for j,(bits,q,cb) in enumerate(trail):
 for i in range(4):bases[i]+=bits[i]<<j;ranks[i]+=q[i]<<(2*j)
 c+=cb<<j
n=1<<len(trail);points=[(bases[BASE[2*i]]+COEF[2*i]*c,bases[BASE[2*i+1]]+COEF[2*i+1]*c) for i in range(4)]
for p,r in zip(points,ranks):assert cell_from_rank(n,r)==p and rank(n,*p)==r
D=ranks[1]-ranks[0];C=bases[1]-bases[0];b=c>>K
assert D%2 and c%(1<<K)==0 and b%2
assert all(ranks[i]==ranks[0]+i*D for i in range(4))
assert (b*(2*C+1)-9*D*D)%(1<<L)==0
v=b*(2*C+1)-9*D*D
result=dict(mask=MASK,L=L,depth=len(trail),side=n,base=bases,points=points,ranks=ranks,D=D,C=C,c=c,b=b,
            norm_difference=v,valuation=(abs(v)&-abs(v)).bit_length()-1 if v else None,
            odd_divisibility=(9*D*D)%b==0,edges=TEMPLATE['edges'],coeff=COEF,base_ids=BASE)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
