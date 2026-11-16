"""Sparse exact verification of the four-private-choice K5 example."""
from itertools import product
from pathlib import Path
import json
from check_arbitrary_order_four_label_obstruction import rectangle

R=(0,2,6,4,7)
U=(36,16,16,24,57)
V=(8,32,0,12,15)
EDGES=tuple((i,(i+j)%5) for i in range(5) for j in (1,2))

def check(S,s,d):
    M=4
    A=(S*M//2)**2
    c=A//2
    assert S%4==0 and s>57*c and d%2==1 and 7*d<=s*s-1 and d>7*S*M/2
    T=(d*d-1)//2
    h=d*d-1+2*s
    labels=[(c*U[i],c*V[i]) for i in range(5)]
    owners=[(c*V[j],c*U[i]) for i,j in EDGES]
    assert not set(labels)&set(owners)
    rank_protected=[d*r for r in R]
    owner_rank={}
    r=0
    for owner in owners:
        if owner in owner_rank:
            continue
        while r in rank_protected:
            r+=1
        owner_rank[owner]=r
        r+=1
    assert r<s*s
    assert sum((R[(i+1)%5]-R[i])**2 for i in range(5))==82
    assert sum((R[(i+2)%5]-R[i])**2 for i in range(5))==82
    for k,(i,j) in enumerate(EDGES):
        m=abs(R[j]-R[i])
        assert V[j]-U[i]==-m*m
        assert owners[k]==(c*(U[i]-m*m),c*(V[j]+m*m))
        assert all(0<=z<s for z in owners[k])
    assignments=0
    common_colorings=0
    for choices in product(range(4),repeat=5):
        assignments+=1
        k=next(k for k,(i,j) in enumerate(EDGES) if choices[i]==choices[j])
        i,j=EDGES[k]
        m=abs(R[j]-R[i])
        a=2*c*U[i]+1
        b=2*(T+c*V[j])+2
        C=(S*(M*rank_protected[i]+choices[i]),a)
        D=(S*(M*rank_protected[j]+choices[j]),b)
        L=d*d+A*m*m
        assert (C[0]-D[0])**2+(a-b)**2==L*L
        lo,hi=(a+b-L)//2,(a+b+L)//2
        assert 1<=lo<hi<=h
        oi,oj=owners[k]
        assert lo==2*oi+1 and hi==2*(T+oj)+2
        mid=(C[0]+D[0])//2
        assert 2*mid==C[0]+D[0]
        P,Q=(mid,lo),(mid,hi)
        tilted={C,P,D,Q}
        assert rectangle(tuple(tilted))
        for ownchoice in range(4):
            ox=S*(M*owner_rank[owners[k]]+ownchoice)
            E,F=(ox,lo),(ox,hi)
            if ox==mid:
                assert tilted<={C,D,E,F}
                common_colorings+=4
                continue
            axis={E,P,Q,F}
            assert axis!=tilted and rectangle(tuple(axis))
            for mask in range(4):
                black={C,D,E,F}|({P} if mask&1 else set())|({Q} if mask&2 else set())
                assert tilted-black==axis-black
                common_colorings+=1
    return dict(S=S,s=s,d=d,h=h,assignments=assignments,common_colorings=common_colorings,distinct_owners=len(owner_rank))

def main():
    cases=[]
    for S,s in ((4,2048),(8,8192),(32,131072)):
        d=(s*s-1)//7
        d-=1-d%2
        cases.append(check(S,s,d))
    result={'status':'PASS','cases':cases,'scope':'Arbitrary prescribed tile order, not Hilbert.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','cases':len(cases),'assignments':sum(c['assignments'] for c in cases),'common_colorings':sum(c['common_colorings'] for c in cases)}))

if __name__=='__main__':
    main()
