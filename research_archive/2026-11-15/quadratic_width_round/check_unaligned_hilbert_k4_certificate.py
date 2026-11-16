"""Exact S32/M3 private-tile K4, with unaligned physical row offset."""
from itertools import product
from pathlib import Path
import json
from check_hilbert_cross_order_independent import cell_from_rank
from check_hilbert_endpoint_p_obstruction import rank
from check_arbitrary_order_four_label_obstruction import rectangle

S=32
M=3
N=8192
POINTS=((3166,4705),(5728,5215),(4192,7777),(6752,6241))
RANKS=(32778237,35923967,39069697,42215427)
EDGES=((0,1),(2,0),(3,0),(1,2),(1,3),(2,3))
C=512
BASE_DIFFERENCE=2561

def audit():
    d=RANKS[1]-RANKS[0]
    assert d==3145730 and all(RANKS[i]==RANKS[0]+i*d for i in range(4))
    for p,r in zip(POINTS,RANKS):
        assert cell_from_rank(N,r)==p and rank(N,*p)==r
    B0=(S*M*d)**2//(8*C)
    assert 8*C*B0==(S*M*d)**2 and B0%2==1
    T=(B0-1)//2-BASE_DIFFERENCE
    assert T>0 and T%N==5635 and T%8==3
    full_side=4*N
    h=2*T+2*full_side
    # Two initial q0 descents swap twice, so these ranks and points persist.
    for p,r in zip(POINTS,RANKS):assert cell_from_rank(full_side,r)==p
    owners=[]
    edge_data=[]
    for u,v in EDGES:
        m=abs(v-u)
        i,j=POINTS[u][0],POINTS[v][1]
        assert j-i==BASE_DIFFERENCE-C*m*m
        owner=(i-C*m*m,j+C*m*m)
        assert all(0<=z<full_side for z in owner)
        assert owner not in POINTS
        rr=rank(full_side,*owner)
        assert cell_from_rank(full_side,rr)==owner
        owners.append((owner,rr))
        Y=B0-2*C*m*m
        L=B0+2*C*m*m
        X=S*M*d*m
        assert Y>0 and X*X+Y*Y==L*L
        edge_data.append(dict(role=[u,v],rank_multiplier=m,norm=[X,Y,L],owner=owner,owner_rank=rr))
    count=0;colorings=0
    for choices in product(range(3),repeat=4):
        count+=1
        k=next(k for k,(u,v) in enumerate(EDGES) if choices[u]==choices[v])
        u,v=EDGES[k];m=abs(v-u)
        a=2*POINTS[u][0]+1;b=2*(T+POINTS[v][1])+2
        P0=(S*(M*RANKS[u]+choices[u]),a)
        P1=(S*(M*RANKS[v]+choices[v]),b)
        L=B0+2*C*m*m
        assert (P0[0]-P1[0])**2+(a-b)**2==L*L
        lo,hi=(a+b-L)//2,(a+b+L)//2
        assert 1<=lo<hi<=h
        owner,rr=owners[k]
        assert lo==2*owner[0]+1 and hi==2*(T+owner[1])+2
        mid=(P0[0]+P1[0])//2
        assert 2*mid==P0[0]+P1[0]
        Q0,Q1=(mid,lo),(mid,hi)
        tilted={P0,P1,Q0,Q1}
        assert rectangle(tuple(tilted))
        for choice in range(3):
            x=S*(M*rr+choice)
            E,F=(x,lo),(x,hi)
            if x==mid:
                assert tilted<={P0,P1,E,F};colorings+=4;continue
            axis={E,F,Q0,Q1}
            assert axis!=tilted and rectangle(tuple(axis))
            for mask in range(4):
                black={P0,P1,E,F}|({Q0} if mask&1 else set())|({Q1} if mask&2 else set())
                assert tilted-black==axis-black
                colorings+=1
    assert count==81 and colorings==972
    return dict(status='PASS',S=S,M=M,side=N,extended_side=full_side,c=C,B0=B0,T=T,h=h,
                d=d,points=POINTS,ranks=RANKS,edges=edge_data,assignments=count,
                common_colorings=colorings,T_mod_side=T%N,
                scope='Integer-offset private tile; not a canonical aligned type.')

if __name__=='__main__':
    result=audit()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','B0','T','h','assignments','common_colorings','T_mod_side')}))
