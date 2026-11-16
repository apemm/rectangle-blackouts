from itertools import product
from check_hilbert_quadratic_clique_exclusions import OPTIONS
COEFF=(9,5,6,0,1,5,4,0)
BASE=(0,1,0,3,0,1,2,1)
K=7
current={(*o,0,0,0,*([0]*8)) for o in product(range(4),repeat=4)}
parents=[]
seen={}
for depth in range(1,101):
 nxtmap={}
 cvalues=(0,) if depth<=K else (1,) if depth==K+1 else (0,1)
 for st in current:
  os=st[:4];cr,c1,c2=st[4:7];carry=st[7:]
  for cbit in cvalues:
   for bits in product(range(2),repeat=4):
    a,b,z,w=bits;rel=a+w-b-z+cr
    if rel%2:continue
    vals=[bits[BASE[i]]+COEFF[i]*cbit+carry[i] for i in range(8)]
    raw=[v%2 for v in vals]
    pairs=[OPTIONS[os[i],raw[2*i],raw[2*i+1]] for i in range(4)]
    pp=tuple(v[0] for v in pairs);qq=tuple(v[1] for v in pairs)
    if depth==1 and (qq[1]-qq[0])%2==0:continue
    ac=qq[0]-2*qq[1]+qq[2]+c1;bc=qq[1]-2*qq[2]+qq[3]+c2
    if ac%4 or bc%4:continue
    ns=(*pp,rel//2,ac//4,bc//4,*(v//2 for v in vals))
    if ns not in nxtmap:nxtmap[ns]=(st,bits,qq,cbit)
 current=set(nxtmap);parents.append(nxtmap)
 
 if depth%5==0 or depth<10: print(depth,len(current),flush=True)
 if (0,)*15 in current:
  st=(0,)*15;base=[0]*4;ranks=[0]*4;c=0
  for j in range(depth-1,-1,-1):
   prev,bits,qq,cb=parents[j][st]
   for i in range(4):base[i]+=bits[i]<<j;ranks[i]+=qq[i]<<(2*j)
   c+=cb<<j;st=prev
  d=ranks[1]-ranks[0]
  print('FOUND',{'depth':depth,'base':base,'ranks':ranks,'step':d,'c':c,'odd_factor':c>>K,'divides':(96*d)**2%(8*c)==0},flush=True)
  break
 if not current:break
 if len(current)>500000:print('STATE CAP');break
 if depth>K+1:
  fs=frozenset(current)
  if fs in seen:print('REPEATED',seen[fs],depth);break
  seen[fs]=depth
