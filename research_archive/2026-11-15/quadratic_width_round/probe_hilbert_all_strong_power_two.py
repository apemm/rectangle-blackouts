from itertools import product
from collections import deque,Counter
from check_hilbert_quadratic_clique_exclusions import OPTIONS,transitions

def templates():
 pairs=[(i,j) for i in range(4) for j in range(i+1,4)]
 for mask in range(64):
  edges=[(j,i) if mask>>k&1 else (i,j) for k,(i,j) in enumerate(pairs)]
  score=sorted(sum(i==u for i,j in edges) for u in range(4))
  if score!=[1,1,2,2]:continue
  adj=[[] for _ in range(8)]
  for i,j in edges:
   w=-(j-i)**2;adj[i].append((4+j,w));adj[4+j].append((i,-w))
  comp=[None]*8;pot=[None]*8;groups=[]
  for v in range(8):
   if pot[v] is not None:continue
   g=[];pot[v]=0;comp[v]=len(groups);todo=[v]
   while todo:
    u=todo.pop();g.append(u)
    for z,w in adj[u]:
     if pot[z] is None:pot[z]=pot[u]+w;comp[z]=comp[u];todo.append(z)
     else:assert pot[z]==pot[u]+w
   groups.append(g)
  assert sorted(map(len,groups))==[2,6]
  big=max(range(2),key=lambda j:len(groups[j]));small=1-big
  for group in groups:
   lo=min(pot[v] for v in group)
   for v in group:pot[v]-=lo
  si=next(v for v in groups[small] if v<4);ti=next(v-4 for v in groups[small] if v>=4)
  coeff=tuple(z for i in range(4) for z in (pot[i],pot[4+i]))
  base=tuple(z for i in range(4) for z in (0 if comp[i]==big else 2,1 if comp[4+i]==big else 3))
  yield mask,edges,(si,ti),coeff,base

def modseeds(positions):
 cur={(*o,0,0,0) for o in product(range(4),repeat=4)}
 cur={nx for st in cur for nx,d in transitions(st,positions) if d}
 seen={};union=set();j=1
 while True:
  fs=frozenset(cur)
  if j>=7:
   union|=cur
   if fs in seen:break
   seen[fs]=j
  cur={nx for st in cur for nx,d in transitions(st,positions)};j+=1
  assert j<50
 return union,j
cache={}
for mask,edges,pos,coef,base in templates():
 if pos not in cache:cache[pos]=modseeds(pos)
 ms,perioddepth=cache[pos]
 seed={(*st,*coef) for st in ms};seen=set(seed);todo=deque(seed)
 target=False
 while todo:
  st=todo.popleft()
  if not any(st):target=True;break
  os=st[:4];cr,c1,c2=st[4:7];carry=st[7:]
  for bits in product(range(2),repeat=4):
   a,b,z,w=bits;rel=a+w-b-z+cr
   if rel%2:continue
   vals=[bits[base[i]]+carry[i] for i in range(8)]
   raw=[v%2 for v in vals]
   pq=[OPTIONS[os[i],raw[2*i],raw[2*i+1]] for i in range(4)]
   pp=[z[0] for z in pq];qq=[z[1] for z in pq]
   ac=qq[0]-2*qq[1]+qq[2]+c1;bc=qq[1]-2*qq[2]+qq[3]+c2
   if ac%4 or bc%4:continue
   ns=(*pp,rel//2,ac//4,bc//4,*(v//2 for v in vals))
   if ns not in seen:seen.add(ns);todo.append(ns)
  if len(seen)>1000000:raise RuntimeError('cap')
 print(mask,pos,len(ms),len(seen),'ACCEPT' if target else 'EXCLUDED',flush=True)
