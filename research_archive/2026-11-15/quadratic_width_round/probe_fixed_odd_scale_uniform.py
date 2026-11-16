from pathlib import Path
from collections import deque
from check_aligned_dyadic_quadratic_k4 import strong_templates
src=Path(__file__).with_name('probe_hilbert_exact_uniform_mod8.py').read_text();exec(src.split('cache={}')[0])
cache={}
for b in (1,3,5,7,9,11,13,15,17,19,21,23,25,27,31,33,63,127,421):
 count=0;maxstates=0;masks=[]
 for temp in strong_templates():
  pos=temp['positions'];coef=temp['coeff'];base=temp['base']
  if (pos,b%8) not in cache:cache[pos,b%8]=prefix(pos,b%8)
  seed={(*st,*(b*a for a in coef)) for st in cache[pos,b%8]}
  seen=set(seed);todo=deque(seed);found=False
  while todo:
   st=todo.popleft()
   if not any(st):found=True;break
   for nx in full(st,coef,base,0):
    if nx not in seen:seen.add(nx);todo.append(nx)
  if found:count+=1;masks.append(temp['mask'])
  maxstates=max(maxstates,len(seen))
 print(b,count,maxstates,masks,flush=True)
