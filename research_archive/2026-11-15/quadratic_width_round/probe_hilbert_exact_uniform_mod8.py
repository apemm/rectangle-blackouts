from itertools import product
from collections import deque
from functools import lru_cache
from check_aligned_dyadic_quadratic_k4 import strong_templates,INITIAL,BITS
from check_hilbert_quadratic_clique_exclusions import OPTIONS

@lru_cache(None)
def ms(st,pos,mode='any',aa=-1,bb=-1):
 *os,c0,c1,c2=st;out=set()
 for a,b,z,w in BITS:
  if aa>=0 and (a!=aa or b!=bb):continue
  rel=a+w-b-z+c0
  if rel%2:continue
  xy=[(a,b)]*4;xy[pos[0]]=(z,b);xy[pos[1]]=(a,w)
  pq=[OPTIONS[os[i],*xy[i]] for i in range(4)];pp=tuple(x[0] for x in pq);q=tuple(x[1] for x in pq);d=(q[1]-q[0])%4
  if mode=='zero' and d:continue
  if mode=='odd' and not d%2:continue
  if mode=='two' and d!=2:continue
  cfirst=q[0]-2*q[1]+q[2]+c1;csecond=q[1]-2*q[2]+q[3]+c2
  if cfirst%4 or csecond%4:continue
  out.add((*pp,rel//2,cfirst//4,csecond//4))
 return frozenset(out)
def advance(cur,pos,n=1,mode='any',aa=-1,bb=-1):
 for _ in range(n):cur=frozenset(nx for st in cur for nx in ms(st,pos,mode,aa,bb))
 return frozenset(cur)
def low2(pos,b,t):
 union=set();j=t//2
 for ar in range(4):
  br=(ar+(b-1)//2)%4;cur=INITIAL
  for dep in (1,2):
   mode='zero' if dep<j+1 else ('two' if t%2 else 'odd') if dep==j+1 else 'any'
   cur=advance(cur,pos,mode=mode,aa=ar>>(dep-1)&1,bb=br>>(dep-1)&1)
  union|=cur
 return frozenset(union)
def prefix(pos,b):
 union=set()
 for t in range(4):union|=advance(low2(pos,b,t),pos,n=5+2*t)
 L=low2(pos,b,4);orbit=[];seen={};cur=L
 while cur not in seen:
  seen[cur]=len(orbit);orbit.append(cur);cur=advance(cur,pos,mode='zero')
 pre=seen[cur];period=len(orbit)-pre
 for n,z in enumerate(orbit):
  j=n+2
  for eps in (0,1):
   source=advance(z,pos,mode='two' if eps else 'odd')
   current=advance(source,pos,n=6+3*j+2*eps);union|=current
   if n>=pre:
    reps=set()
    while current not in reps:
     reps.add(current);union|=current;current=advance(current,pos,n=3*period)
 return union

def full(st,coef,base,cb):
 os=st[:4];c0,c1,c2=st[4:7];carry=st[7:]
 for bits in BITS:
  a,b,z,w=bits;rel=a+w-b-z+c0
  if rel%2:continue
  vals=[bits[base[i]]+coef[i]*cb+carry[i] for i in range(8)];xy=[v%2 for v in vals]
  pq=[OPTIONS[os[i],xy[2*i],xy[2*i+1]] for i in range(4)];pp=tuple(x[0] for x in pq);q=tuple(x[1] for x in pq)
  cfirst=q[0]-2*q[1]+q[2]+c1;csecond=q[1]-2*q[2]+q[3]+c2
  if cfirst%4 or csecond%4:continue
  yield (*pp,rel//2,cfirst//4,csecond//4,*(v//2 for v in vals))
cache={}
for temp in strong_templates():
 mask=temp['mask'];pos=temp['positions'];coef=temp['coeff'];base=temp['base']
 for b in (1,3,5,7):
  if (pos,b) not in cache:cache[pos,b]=prefix(pos,b)
  cur={(*st,*([0]*8)) for st in cache[pos,b]}
  for cb in (1,b>>1&1,b>>2&1):cur={nx for st in cur for nx in full(st,coef,base,cb)}
  seen=set(cur);todo=deque(cur);found=False
  while todo:
   st=todo.popleft()
   if not any(st):found=True;break
   for cb in (0,1):
    for nx in full(st,coef,base,cb):
     if nx not in seen:seen.add(nx);todo.append(nx)
  print(mask,b,len(cache[pos,b]),len(seen),'ACCEPT' if found else 'EXCLUDED',flush=True)
