from itertools import product
from pathlib import Path
import json
from check_hilbert_quadratic_clique_exclusions import OPTIONS

# Strong tournament with isolated edge3->1.
# Points: (A+9c,B+5c),(A+6c,W),(A+c,B+5c),(Z+4c,B), W+A=B+Z.
C=128
OFFSET=(9*C,5*C,6*C,0,C,5*C,4*C,0)
BASE=(0,1,0,3,0,1,2,1) #A,B,Z,W
initial={(*o,0,0,0,*OFFSET) for o in product(range(4),repeat=4)}
current=initial
parents=[]
seen_sets={}
for depth in range(1,25):
 nxtmap={}
 for st in current:
  os=st[:4];cr,c1,c2=st[4:7];carry=st[7:]
  for bits in product(range(2),repeat=4):
   a,b,z,w=bits
   rel=a+w-b-z+cr
   if rel%2:continue
   vals=[bits[BASE[i]]+carry[i] for i in range(8)]
   raw=[v%2 for v in vals]
   pairs=[OPTIONS[os[i],raw[2*i],raw[2*i+1]] for i in range(4)]
   pp=tuple(v[0] for v in pairs);qq=tuple(v[1] for v in pairs)
   if depth==1 and (qq[1]-qq[0])%2==0:continue
   ac=qq[0]-2*qq[1]+qq[2]+c1;bc=qq[1]-2*qq[2]+qq[3]+c2
   if ac%4 or bc%4:continue
   ns=(*pp,rel//2,ac//4,bc//4,*(v//2 for v in vals))
   if ns not in nxtmap:nxtmap[ns]=(st,bits,qq)
 current=set(nxtmap)
 parents.append(nxtmap)
 print(depth,len(current),flush=True)
 accepts=[st for st in current if all(v==0 for v in st)]
 if accepts:
  st=accepts[0];base=[0]*4;ranks=[0]*4
  for j in range(depth-1,-1,-1):
   prev,bits,qq=parents[j][st]
   for i in range(4):base[i]+=bits[i]<<j;ranks[i]+=qq[i]<<(2*j)
   st=prev
  print('FOUND',{'depth':depth,'base':base,'ranks':ranks,'step':ranks[1]-ranks[0]},flush=True)
  break
 if not current:break
 if len(current)>500000:
  print('STATE CAP');break
 fs=frozenset(current)
 if depth>12 and fs in seen_sets:
  print('REPEATED',seen_sets[fs],depth);break
 if depth>12:seen_sets[fs]=depth
