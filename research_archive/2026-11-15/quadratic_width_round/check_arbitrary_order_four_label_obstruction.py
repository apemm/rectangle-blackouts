"""Sparse exact checks of the arbitrary-order three-choice K4 obstruction."""
from itertools import product
from pathlib import Path
import json

EDGES=((0,1),(1,2),(2,0),(3,0),(3,1),(2,3))
NORMALIZED=((6,0),(2,5),(4,1),(9,3))
OWNERS=((5,6),(1,2),(0,4),(0,9),(5,9),(3,4))

def rectangle(points):
    if len(set(points)) != 4:
        return False
    a,b,c,d=points
    for p,q,r,s in ((a,b,c,d),(a,c,b,d),(a,d,b,c)):
        if (p[0]+q[0],p[1]+q[1]) != (r[0]+s[0],r[1]+s[1]):
            continue
        if (p[0]-q[0])**2+(p[1]-q[1])**2 == (r[0]-s[0])**2+(r[1]-s[1])**2:
            return True
    return False

def check(S,s,q):
    assert S%4==0 and q%6==3 and q>3*S/2 and q<=s*s-1
    c=S*S//8
    assert s>9*c
    d=q//3
    T=(q*q-1)//2
    h=2*T+2*s
    labels=[(c*i,c*j) for i,j in NORMALIZED]
    owners=[(c*i,c*j) for i,j in OWNERS]
    assert len(set(labels+owners))==10
    rank_protected=[k*d for k in range(4)]
    rank_owners=[]
    r=0
    while len(rank_owners)<6:
        if r not in rank_protected:
            rank_owners.append(r)
        r+=1
    assert r<=s*s
    for k,(u,v) in enumerate(EDGES):
        m=abs(v-u)
        i,j=labels[u][0],labels[v][1]
        assert j-i==-c*m*m
        assert owners[k]==(i-c*m*m,j+c*m*m)
        assert all(0<=z<s for z in owners[k])
    assignments=0
    common_colorings=0
    for choices in product(range(3),repeat=4):
        assignments+=1
        k=next(k for k,(u,v) in enumerate(EDGES) if choices[u]==choices[v])
        u,v=EDGES[k]
        m=abs(v-u)
        odd=2*labels[u][0]+1
        even=2*(T+labels[v][1])+2
        C=(S*(3*rank_protected[u]+choices[u]),odd)
        D=(S*(3*rank_protected[v]+choices[v]),even)
        L=q*q+S*S*m*m//4
        assert (C[0]-D[0])**2+(odd-even)**2==L*L
        lo,hi=(odd+even-L)//2,(odd+even+L)//2
        assert 1<=lo<hi<=h
        oi,oj=owners[k]
        assert lo==2*oi+1 and hi==2*(T+oj)+2
        midpoint=(C[0]+D[0])//2
        assert 2*midpoint==C[0]+D[0]
        P,Q=(midpoint,lo),(midpoint,hi)
        tilted={C,P,D,Q}
        assert rectangle(tuple(tilted))
        for owner_choice in range(3):
            ox=S*(3*rank_owners[k]+owner_choice)
            E,F=(ox,lo),(ox,hi)
            if ox==midpoint:
                assert tilted<={C,D,E,F}
                common_colorings+=4
                continue
            axis={E,P,Q,F}
            assert rectangle(tuple(axis)) and axis!=tilted
            for mask in range(4):
                black={C,D,E,F}|({P} if mask&1 else set())|({Q} if mask&2 else set())
                assert tilted-black==axis-black
                common_colorings+=1
    return dict(S=S,s=s,q=q,h=h,assignments=assignments,common_colorings=common_colorings)

def main():
    cases=[]
    for S,s in ((4,32),(8,128),(32,2048),(128,32768)):
        q=s*s-1
        q-= (q-3)%6
        cases.append(check(S,s,q))
    result={'status':'PASS','cases':cases,'scope':'Arbitrary prescribed tile order, not Hilbert.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','cases':len(cases),'assignments':sum(c['assignments'] for c in cases),'common_colorings':sum(c['common_colorings'] for c in cases)}))

if __name__=='__main__':
    main()
