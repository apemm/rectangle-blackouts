from pathlib import Path
from itertools import product
from collections import deque
from check_hilbert_quadratic_clique_exclusions import OPTIONS
src=Path(__file__).with_name('probe_hilbert_all_strong_power_two.py').read_text();exec(src.split('cache={}')[0])
BITS=tuple(product(range(2),repeat=4))
INIT={(*o,0,0,0) for o in product(range(4),repeat=4)}

def modstep(st,pos,mode='any',equal=False):
 *os,c0,c1,c2=st
 for a,b,z,w in BITS:
  if equal and a!=b:continue
  rel=a+w-b-z+c0
  if rel%2:continue
  xy=[(a,b)]*4;xy[pos[0]]=(z,b);xy[pos[1]]=(a,w)
  pq=[OPTIONS[os[i],*xy[i]] for i in range(4)]
  pp=tuple(v[0] for v in pq);qq=tuple(v[1] for v in pq);dd=(qq[1]-qq[0])%4
  if mode=='zero' and dd:continue
  if mode=='odd' and not dd%2:continue
  if mode=='two' and dd!=2:continue
  ac=qq[0]-2*qq[1]+qq[2]+c1;bc=qq[1]-2*qq[2]+qq[3]+c2
  if ac%4 or bc%4:continue
  yield (*pp,rel//2,ac//4,bc//4)

def apply(cur,pos,n=1,mode='any',equal=False):
 for _ in range(n):cur={nx for st in cur for nx in modstep(st,pos,mode,equal)}
 return cur

def seed_union(pos):
 union=set();report={}
 for t in range(4):
  j=t//2;cur=set(INIT)
  for depth in range(1,8+2*t):
   mode='zero' if depth<j+1 else ('two' if t%2 else 'odd') if depth==j+1 else 'any'
   cur=apply(cur,pos,mode=mode,equal=depth<=2)
  union|=cur
 report['small_t_counts']=[None]*4
 L=apply(INIT,pos,n=2,mode='zero',equal=True)
 states=[];seen={};cur=L
 while frozenset(cur) not in seen:
  seen[frozenset(cur)]=len(states);states.append(cur);cur=apply(cur,pos,mode='zero')
 pre=seen[frozenset(cur)];period=len(states)-pre
 report['zero_prefix']=[len(s) for s in states];report['zero_preperiod']=pre;report['zero_period']=period
 for n,zz in enumerate(states):
  j=n+2
  for eps in (0,1):
   source=apply(zz,pos,mode='two' if eps else 'odd')
   current=apply(source,pos,n=6+3*j+2*eps)
   union|=current
   if n>=pre:
    cycle_seen=set()
    while frozenset(current) not in cycle_seen:
     cycle_seen.add(frozenset(current));union|=current
     current=apply(current,pos,n=3*period)
 return union,report

cache={}
for mask,edges,pos,coef,base in templates():
 if pos not in cache:cache[pos]=seed_union(pos)
 ms,rep=cache[pos]
 seed={(*st,*coef) for st in ms};seen=set(seed);todo=deque(seed);target=False
 while todo:
  st=todo.popleft()
  if not any(st):target=True;break
  os=st[:4];cr,c1,c2=st[4:7];carry=st[7:]
  for bits in BITS:
   a,b,z,w=bits;rel=a+w-b-z+cr
   if rel%2:continue
   vals=[bits[base[i]]+carry[i] for i in range(8)];raw=[v%2 for v in vals]
   pq=[OPTIONS[os[i],raw[2*i],raw[2*i+1]] for i in range(4)]
   pp=tuple(v[0] for v in pq);qq=tuple(v[1] for v in pq)
   ac=qq[0]-2*qq[1]+qq[2]+c1;bc=qq[1]-2*qq[2]+qq[3]+c2
   if ac%4 or bc%4:continue
   ns=(*pp,rel//2,ac//4,bc//4,*(v//2 for v in vals))
   if ns not in seen:seen.add(ns);todo.append(ns)
 print(mask,pos,len(ms),len(seen),'ACCEPT' if target else 'EXCLUDED',rep,flush=True)
