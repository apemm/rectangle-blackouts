"""Search the four compact windows with each prefix and suffix filled."""
import sys,json,pathlib,math
from collections import defaultdict
sys.path.insert(0,'research_archive/2026-11-18')
import search_127_filled_phases as f
from assemble_127_filled_board import phases,read_phase
from core_mixed_witness import from_record
from one_filler_check import triangle_masks,mixed_masks,virtual_vertical_masks
from two_level_filler_check import three_diameter_traps,pair_implications
from pysat.solvers import Cadical195
import zlib,base64,hashlib,time
folder=pathlib.Path('research_archive/2026-11-18');old=from_record(127,96,186)
groups=defaultdict(list)
for rec in phases():groups[tuple(rec['levels'])].append(rec)
def assemble(pair,sep):
 raw={};shifts=[];nextx=0
 for rec in groups[pair]:
  rows=read_phase(rec,old)[4];a,b=min(rows),max(rows)
  for x,(y,z) in rows.items():raw[nextx+x-a]=(y,z)
  shifts.append((rec['group'],rec.get('columns'),nextx-(a+rec['base'])))
  nextx=((nextx+b-a+sep+3)//4)*4
 return raw,shifts
def search(pair,sep,source=None):
 start=time.monotonic()
 raw,shifts=assemble(pair,sep) if source is None else source
 halo=7941;rows={x+halo:v for x,v in raw.items()};width=max(rows)+halo+1;bounds=(0,width-1)
 if pair in three_diameter_traps(rows,127):
  print('three-diameter trap',pair,sep,flush=True);return None
 masks=defaultdict(int)
 for rs in (triangle_masks(rows,127,bounds),mixed_masks(rows,127,pair,bounds),virtual_vertical_masks(rows,127,pair,bounds)):
  for x,v in rs.items():masks[x]|=v
 low,high=pair;bits=1<<low|1<<high
 if any(v&bits==bits for v in masks.values()):
  print('unary trap',pair,sep,flush=True);return None
 print('unaries',pair,sep,len(rows),width,round(time.monotonic()-start,1),flush=True)
 with Cadical195() as solver:
  for x,m in masks.items():
   if m>>low&1:solver.add_clause([x+1])
   if m>>high&1:solver.add_clause([-(x+1)])
  for c in pair_implications(rows,127,pair,bounds):solver.add_clause(c)
  if not solver.solve():print('2true unsat',pair,sep,flush=True);return None
  f.single_angles(rows,pair,solver,bounds)
  if not solver.solve():print('1true unsat',pair,sep,flush=True);return None
  f.mixed_shapes(rows,pair,solver,bounds)
  for j in range(40):
   if not solver.solve():print('mixed/6 unsat',pair,sep,j,flush=True);return None
   cols,parked,new=f.audit_triangles(rows,pair,solver,bounds)
   print('solve',pair,sep,j,parked,new,round(time.monotonic()-start,1),flush=True)
   if new:continue
   data=bytearray((width+7)//8)
   for x in cols:
    if 0<=x<width and x not in rows:data[x//8]|=1<<(x%8)
   return {'height':127,'levels':list(pair),'width':width,'doubles':len(rows),'halo':halo,'groups':shifts,'base':-halo,'sep':sep,'high_sha256':hashlib.sha256(data).hexdigest(),'high_zlib_base64':base64.b64encode(zlib.compress(data,9)).decode('ascii')}
if __name__=='__main__':
 import argparse
 parser=argparse.ArgumentParser(description="Search the four compact height-127 window assignments")
 parser.add_argument('--output-folder',type=pathlib.Path,required=True)
 args=parser.parse_args()
 for pair,sep in (((1,122),1024),((1,124),256),((1,126),256),((2,127),256)):
  result=search(pair,sep)
  if result is None:raise RuntimeError((pair,sep))
  output=args.output_folder/f'phase_127_merged_{pair[0]}_{pair[1]}.json'
  with output.open('x') as stream:json.dump(result,stream,indent=2)
