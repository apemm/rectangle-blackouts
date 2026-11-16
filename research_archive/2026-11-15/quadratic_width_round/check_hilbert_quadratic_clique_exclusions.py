"""Exact finite carry certificate for the middle-edge quadratic K4 template."""
from itertools import product
from collections import deque
from pathlib import Path
import json

TABLE=(((1,0),(0,1),(3,3),(0,2)),
       ((0,0),(2,3),(1,1),(1,2)),
       ((2,2),(1,3),(2,1),(3,0)),
       ((3,2),(3,1),(0,3),(2,0)))

def build_table():
    ans={}
    for child,a,b in product(range(4),range(2),range(2)):
        choices=[]
        for parent in range(4):
            x,y=(b,a) if parent&1 else (a,b)
            x^=parent>>1;y^=parent>>1
            digit={(0,0):0,(0,1):1,(1,1):2,(1,0):3}[x,y]
            rotation=(1,0,0,3)[digit]
            if parent^rotation==child:
                choices.append((parent,digit))
        assert len(choices)==1
        ans[child,a,b]=choices[0]
        assert choices[0]==TABLE[child][2*a+b]
    return ans

OPTIONS=build_table()

def transitions(state,positions=(1,2)):
    *orient,c0,c1,c2=state
    for a,b,f,g in product(range(2),repeat=4):
        v=f+b-g-a+c0
        if v%2:continue
        bits=[(a,b)]*4
        bits[positions[0]]=(f,b)
        bits[positions[1]]=(a,g)
        pairs=[OPTIONS[orient[i],*bits[i]] for i in range(4)]
        parent=[z[0] for z in pairs]
        q=[z[1] for z in pairs]
        v1=q[0]-2*q[1]+q[2]+c1
        v2=q[1]-2*q[2]+q[3]+c2
        if v1%4 or v2%4:continue
        carry=(v//2,v1//4,v2//4)
        assert all(-1<=c<=1 for c in carry)
        yield (*parent,*carry),(q[1]-q[0])%4

def audit():
    initial={(*o,0,0,0) for o in product(range(4),repeat=4)}
    zero=set(initial);todo=deque(initial)
    while todo:
        state=todo.popleft()
        for nxt,delta in transitions(state):
            if delta==0 and nxt not in zero:
                zero.add(nxt);todo.append(nxt)
    assert zero==initial
    first={nxt for state in zero for nxt,delta in transitions(state) if delta}
    odd_first=[(state,nxt,delta) for state in zero for nxt,delta in transitions(state) if delta%2]
    assert not odd_first
    levels=[]
    current=first
    for _ in range(5):
        levels.append(sorted(current))
        current={nxt for state in current for nxt,delta in transitions(state)}
    assert [len(level) for level in levels]==[120,112,48,16,0]
    assert not current
    return {'status':'PASS','zero_states':sorted(zero),'first_nonzero_digit':2,
            'level_counts':[len(level) for level in levels],'level_states':levels,
            'scope':'Canonical Hilbert orientations, middle isolated edge; modular overgraph.'}

if __name__=='__main__':
    result=audit()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ('status','first_nonzero_digit','level_counts')}))
