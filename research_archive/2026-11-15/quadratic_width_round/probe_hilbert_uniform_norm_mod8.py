from pathlib import Path
from itertools import product
from collections import deque
from check_hilbert_quadratic_clique_exclusions import OPTIONS
src=Path(__file__).with_name('probe_hilbert_all_strong_power_two.py').read_text();exec(src.split('cache={}')[0])
AGE=7
ALLBITS=tuple(product(range(2),repeat=4))
def step(st,coef,base,cbit,bitslist=ALLBITS):
 os=st[:4];cr,c1,c2=st[4:7];carry=st[7:]
 for bits in bitslist:
  a,b,z,w=bits;rel=a+w-b-z+cr
  if rel%2:continue
  vals=[bits[base[i]]+coef[i]*cbit+carry[i] for i in range(8)]
  raw=[v%2 for v in vals]
  pq=[OPTIONS[os[i],raw[2*i],raw[2*i+1]] for i in range(4)]
  pp=tuple(v[0] for v in pq);qq=tuple(v[1] for v in pq)
  ac=qq[0]-2*qq[1]+qq[2]+c1;bc=qq[1]-2*qq[2]+qq[3]+c2
  if ac%4 or bc%4:continue
  yield (*pp,rel//2,ac//4,bc//4,*(v//2 for v in vals)),(qq[1]-qq[0])%4

def seedset(coef,base,bb):
 want=(bb-1)//2;seeds=set()
 initial={(*o,0,0,0,*([0]*8),0) for o in product(range(4),repeat=4)}
 for ar in range(4):
  br=(ar+want)%4;cur=initial
  for lev in range(2):
   bitslist=tuple(bits for bits in ALLBITS if bits[0]==(ar>>lev&1) and bits[1]==(br>>lev&1))
   nx=set()
   for full in cur:
    st,age=full[:-1],full[-1]
    for new,delta in step(st,coef,base,0,bitslist):
     na=min(AGE,age+1) if age else int(delta!=0)
     nx.add((*new,na))
   cur=nx
  seeds|=cur
 seen=set(seeds);todo=deque(seeds)
 while todo:
  full=todo.popleft();st,age=full[:-1],full[-1]
  for new,delta in step(st,coef,base,0):
   na=min(AGE,age+1) if age else int(delta!=0)
   ns=(*new,na)
   if ns not in seen:seen.add(ns);todo.append(ns)
 return {st[:-1] for st in seen if st[-1]==AGE},len(seen)

for mask,edges,pos,coef,base in templates():
 for bb in (1,3,5,7):
  seed,prefix=seedset(coef,base,bb)
  cur=seed
  for cb in (1,(bb>>1)&1,(bb>>2)&1):
   cur={new for st in cur for new,delta in step(st,coef,base,cb)}
  seen=set(cur);todo=deque(cur);found=False
  while todo:
   st=todo.popleft()
   if not any(st):found=True;break
   for cb in (0,1):
    for new,delta in step(st,coef,base,cb):
     if new not in seen:seen.add(new);todo.append(new)
   if len(seen)>200000:
    print('CAP',mask,bb,len(seen),flush=True);raise SystemExit
  print(mask,bb,prefix,len(seed),len(cur),len(seen),'ACCEPT' if found else 'EXCLUDED',flush=True)
