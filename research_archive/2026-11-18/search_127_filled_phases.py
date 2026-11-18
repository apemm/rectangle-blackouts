import sys,itertools,math
from collections import defaultdict
from functools import cache
from itertools import product
sys.path.insert(0,'research_archive/2026-11-18')
from core_mixed_witness import from_record
from fiber_translation_search import group_key
from one_filler_check import core_pairs,triangle_masks,mixed_masks,virtual_vertical_masks
from two_level_filler_check import pair_implications,three_diameter_traps
from pysat.solvers import Cadical195
h=127
@cache
def divisors(n):
 ds=set()
 for i in range(1,math.isqrt(abs(n))+1):
  if n%i==0:ds.update((i,-i,n//i,-n//i))
 return ds
@cache
def shapes(ya,low,high):
 result=set();lev=(low,high)
 for s,t in product(lev,repeat=2):
  # Other two friends are the future sea points. Any tilted rectangle
  # containing all three is obtained with one of their three pivots.
  prod=-(s-ya)*(t-ya)
  if prod and 1<=s+t-ya<=h:
   for u in divisors(prod):
    v=prod//u
    result.add((u,s,v,t,u+v,s+t-ya))
  prod=-(t-s)*(ya-s)
  if prod and 1<=t+ya-s<=h:
   for u in divisors(prod):
    v=prod//u
    result.add((-u,s,-u+v,t,v,t+ya-s))
 return result
def single_angles(rows,pair,solver,bounds):
 low,high=pair;xmin,xmax=bounds;lev=(low,high)
 def neg(x,y):return x+1 if y==low else -(x+1)
 for x,ys in rows.items():
  for a in ys:
   for du,s,dv,t,dw,w in shapes(a,low,high):
    u=x+du;v=x+dv;z=x+dw
    if not xmin<=min(u,v,z)<=max(u,v,z)<=xmax or u==v:continue
    if u in rows and s not in rows[u] or v in rows and t not in rows[v]:continue
    c=[neg(f,y) for f,y in ((u,s),(v,t)) if f not in rows]
    if z in rows:
     solver.add_clause(c)
    else:
     for y in lev:
      if y==w or (y-w)%2:solver.add_clause(c+[neg(z,y)])
@cache
def patterns(a,b,c,d):
 v1=b-a;v2=d-c;sy=c+d-a-b
 if sy%2 or not 1<=min(a+sy//2,b+sy//2)<=max(a+sy//2,b+sy//2)<=h:return ()
 new=set()
 n=v2*v2-v1*v1
 dot=v1*sy
 if n:
  ratios=[]
  for k in divisors(n):
   kk=n//k
   if (k+kk)%2==0:ratios.append(((k+kk)//2,(kk-k)//2))
 else:
  if dot==0:return ()
  ratios=[(u,v) for u in divisors(dot) for v in (u,-u)]
 for u,v in ratios:
  if not u or u*v2==v*v1 or dot%u:continue
  tx=-dot//u
  if tx%2 or (u+tx-v)%2 or (sy==0 and tx==0):continue
  cx=(u+tx-v)//2;dx=cx+v
  pts=((0,a),(u,b),(cx,c),(dx,d))
  P=(tx//2,a+sy//2);Q=(u+tx//2,b+sy//2)
  if len({pts[0],pts[1],P,Q})!=4 or len({pts[2],pts[3],P,Q})!=4 or len(set(pts))!=4:continue
  new.add(((0,u,cx,dx),min(P[0],Q[0]),max(P[0],Q[0])))
 return tuple(new)
def mixed_shapes(rows,pair,solver,bounds):
 byrow=defaultdict(list)
 for x,ys in rows.items():
  for y in ys:byrow[y].append(x)
 xmin,xmax=bounds;lo,hi=pair
 total=0
 for tr in ((0,),(2,),(0,1),(2,3),(0,2)):
  cand=[byrow.keys() if i in tr else pair for i in range(4)]
  for ys in product(*cand):
   for coords,wlo,whi in patterns(*ys):
    for anchor in byrow[ys[tr[0]]]:
     base=anchor-coords[tr[0]]
     if not xmin<=base+min(coords)<=base+max(coords)<=xmax or base+wlo<xmin or base+whi>xmax:continue
     if len(tr)==2 and ys[tr[1]] not in rows.get(base+coords[tr[1]],()):continue
     c=[]
     for i in range(4):
      if i in tr:continue
      x=base+coords[i];y=ys[i]
      if x in rows:
       if y not in rows[x]:break
      else:c.append(x+1 if y==lo else -(x+1))
     else:
      solver.add_clause(c);total+=1
 return total
def audit_triangles(rows,pair,solver,bounds):
 model=solver.get_model();low,high=pair
 highcols={v-1 for v in model if v>0}
 xmin,xmax=bounds;seen={};cuts=set();seen_tri=0
 def black(x,y):return y in rows[x] if x in rows else y==(high if x in highcols else low)
 def subtract(pts):
  return [x+1 if y==low else -(x+1) for x,y in pts if x not in rows]
 def accept(abc,w):
  nonlocal seen_tri
  wx,wy=w
  corners=set(abc)|{w}
  if len(corners)!=4 or not all(xmin<=x<=xmax and 1<=y<=h for x,y in corners):return
  if len({x for x,y in corners})==len({y for x,y in corners})==2:return
  if not all(black(x,y) for x,y in abc):return
  if black(*w):
   cuts.add(tuple(sorted(set(subtract(corners)))));return
  if wx in rows or ((high if wx in highcols else low)-wy)%2:
   bad=subtract(abc)
   if wx not in rows:bad.extend(subtract(((wx,high if wx in highcols else low),)))
   cuts.add(tuple(sorted(set(bad))));return
  tag=frozenset(abc)
  if w in seen:
   if seen[w]!=tag:cuts.add(tuple(sorted(set(subtract(tag|seen[w])))))
  else:seen[w]=tag;seen_tri+=1
 for a,b in core_pairs(rows,h):
  ax,ay=a;bx,by=b;dx=bx-ax;dy=by-ay
  for fy in pair:
   if dx and dy:
    for u,v in ((a,b),(b,a)):
     ky=fy-u[1]
     if ky and (ky*dy)%dx==0:
      kx=-ky*dy//dx
      accept((a,b,(u[0]+kx,fy)),(v[0]+kx,v[1]+ky))
   n=dx*dx+dy*dy-(2*fy-ay-by)**2
   if n<0:continue
   root=math.isqrt(n)
   if root*root!=n or (ax+bx+root)%2:continue
   for sign in (-1,1):
    fx=(ax+bx+sign*root)//2
    accept((a,b,(fx,fy)),(ax+bx-fx,ay+by-fy))
 for ax,ys in rows.items():
  for ay in ys:
   for u,r,v,s,t,z in shapes(ay,low,high):
    accept(((ax,ay),(ax+u,r),(ax+v,s)),(ax+t,z))
 for c in cuts:solver.add_clause(c)
 return highcols,seen_tri,len(cuts)
import json,zlib,base64,hashlib
from pathlib import Path
import argparse
def makeblock(key,raw,original_level=0):
 h=127
 halo=2*(1+(h-1)**2//4)+1
 base=min(raw)-halo
 rows={x-base:vals for x,vals in raw.items()}
 width=max(rows)+halo+1;bounds=(0,width-1)
 ordered=[(1,122),(1,124),(1,126),(1,120),(2,127),(4,127),(6,127),(8,127)]
 for a in range(1,9):
  for b in range(119,128):
   if (a,b) not in ordered:ordered.append((a,b))
 levels=sorted({y for p in ordered for y in p})
 masks=defaultdict(int)
 for rs in (triangle_masks(rows,h,bounds),mixed_masks(rows,h,levels,bounds),virtual_vertical_masks(rows,h,levels,bounds)):
  for x,v in rs.items():masks[x]|=v
 traps=three_diameter_traps(rows,h)
 for pair in ordered:
  low,high=pair
  if (high-low)%2==0 or (low,high) in traps:continue
  if any(math.isqrt(j*(high-low+j))**2==j*(high-low+j) for j in range(1,min(low-1,h-high)+1)):continue
  bits=(1<<low)|(1<<high)
  if any(v&bits==bits for v in masks.values()):continue
  with Cadical195() as solver:
   for x,ms in masks.items():
    for r in pair:
     if ms>>r&1:solver.add_clause([x+1 if r==low else -(x+1)])
   for clause in pair_implications(rows,h,pair,bounds):solver.add_clause(clause)
   if not solver.solve():continue
   single_angles(rows,pair,solver,bounds)
   if not solver.solve():continue
   mixed_shapes(rows,pair,solver,bounds)
   for attempt in range(30):
    if not solver.solve():break
    cols,parked,new=audit_triangles(rows,pair,solver,bounds)
    if new:continue
    data=bytearray((width+7)//8)
    for x in cols:
     if 0<=x<width and x not in rows:data[x//8]|=1<<(x%8)
    print('filled',key,len(rows),pair,'width',width,'parked',parked,'rounds',attempt,flush=True)
    return {'height':h,'group':list(key),'levels':list(pair),'base':base,'width':width,'doubles':len(rows),'halo':halo,'high_sha256':hashlib.sha256(data).hexdigest(),'high_zlib_base64':base64.b64encode(zlib.compress(data,9)).decode('ascii')}
 print('miss',key,len(raw),flush=True)
 return None

def main():
 p=argparse.ArgumentParser()
 p.add_argument('--output',default=None)
 p.add_argument('--split-misses',action='store_true',help='split an infeasible group into alternating column ranks and retry')
 p.add_argument('--scales',type=int,nargs='+',default=[1,3,9,27,81])
 args=p.parse_args()
 groups=defaultdict(dict)
 for x,a,b in from_record(127,96,186):
  key=group_key(a,b)[:3]
  if key[0] in args.scales:groups[key][x]=(a,b)
 out=[]
 def search_group(key,items,subset=False):
  rec=makeblock(key,dict(items))
  if rec:
   if subset:rec['columns']=[x for x,_ in items]
   out.append(rec)
   return
  if args.split_misses and len(items)>1:
   search_group(key,items[::2],True)
   search_group(key,items[1::2],True)
 for key,raw in groups.items():
  search_group(key,sorted(raw.items()))
 if args.output:
  with Path(args.output).open('x') as stream:json.dump(out,stream,indent=2)
 print('total filled',len(out),'of',len(groups),'labels',sum(r['doubles'] for r in out),flush=True)
if __name__=='__main__':main()

