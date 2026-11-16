"""Exact mixed diagonal/side support search in the unshifted dyadic sea.

The N=0 row-pair case is treated analytically in the accompanying note.
This checker searches all N!=0 patterns, without a horizontal cutoff.
"""
from math import isqrt
from pathlib import Path
import json
from check_four_block_obstruction import rectangle


def norm_pairs(N):
    n=abs(N)
    for z in range(1,isqrt(n)+1):
        if n%z:
            continue
        aa=z if N>0 else -z
        bb=n//z
        if (aa+bb)%2:
            continue
        u,v=(aa+bb)//2,(bb-aa)//2
        if u>0 and v>0:
            yield u,v


def search(e, include_nonpositive=False):
    S=1<<e
    rows=[1<<j for j in range(e)]
    def sea(x):
        return None if x%S==0 else x&-x
    norm_cases=integer_cases=0
    witnesses=[]
    for a in rows:
      for b in rows:
       Y=b-a
       for c in rows:
        for d in rows:
         Z=d-c
         N=Z*Z-Y*Y
         if not N:
             continue
         for u,v in norm_pairs(N):
          norm_cases+=1
          num=u*(u-v)-Y*(c+d-a-b)
          if num%(2*u):
              continue
          t=num//(2*u)
          if (v-u)%2 or (c+d-a-b)%2:
              continue
          shift=(t+(v-u)//2,(c+d-a-b)//2)
          if shift==(0,0):
              continue
          py=a+shift[1];qy=b+shift[1]
          if not include_nonpositive and min(py,qy)<1:
              continue
          integer_cases+=1
          for x in range(a,S,2*a):
           if sea(x+u)!=b or sea(x+t)!=c or sea(x+t+v)!=d:
               continue
           A,B=(x,a),(x+u,b)
           C,D=(x+t,c),(x+t+v,d)
           P,Q=(x+shift[0],py),(x+u+shift[0],qy)
           side=(A,B,Q,P);diag=(C,P,D,Q)
           if len(set(side))<4 or len(set(diag))<4 or set(side)==set(diag):
               continue
           assert rectangle(side) and rectangle(diag)
           witnesses.append(dict(e=e,rows=[a,b,c,d],u=u,v=v,t=t,
                                 side=side,diag=diag,common=[P,Q],
                                 min_white_row=min(py,qy)))
           if len(witnesses)>=5:
               return dict(e=e,norm_cases=norm_cases,integer_cases=integer_cases,
                           witnesses=witnesses,complete=False)
    return dict(e=e,norm_cases=norm_cases,integer_cases=integer_cases,
                witnesses=witnesses,complete=True)


if __name__=='__main__':
    results=[]
    for e in range(2,9):
        item=search(e)
        results.append(item)
        print(json.dumps(item),flush=True)
        if item['witnesses']:
            break
    translated=search(6,True)
    result=dict(results=results,allow_nonpositive=translated,
                scope='N!=0 mixed supports in the unshifted power-of-two sea; '
                      'no label or full-board theorem.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'nonpositive_probe':translated}),flush=True)
