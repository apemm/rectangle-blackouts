"""Finite complete presentation checks for the one-label classification.

Enumerate every rectangle with >=2 black corners from a black side or
black diagonal. Any collision has at most two common white corners.
"""
from collections import defaultdict
from itertools import combinations
from math import gcd
from pathlib import Path
import json


def check(a,b,radius):
    h=max(a,b)
    left,right=-radius,radius
    black={(x,2 if x%4==0 else 1) for x in range(left,right+1) if x!=0}
    black|={(0,a),(0,b)}
    vectors=defaultdict(list)
    for dx in range(0,right-left+1):
        for dy in range(-h+1,h):
            if dx==0 and dy<=0:
                continue
            vectors[dx*dx+dy*dy].append((dx,dy))
    rectangles=set()
    def inside(point):
        x,y=point
        return left<=x<=right and 1<=y<=h
    for A,B in combinations(sorted(black),2):
        dx,dy=B[0]-A[0],B[1]-A[1]
        g=gcd(abs(dx),abs(dy))
        nx,ny=-dy//g,dx//g
        bound=max(right-left,h-1)
        for k in range(-bound,bound+1):
            if k==0:
                continue
            C=(A[0]+k*nx,A[1]+k*ny)
            D=(B[0]+k*nx,B[1]+k*ny)
            if inside(C) and inside(D):
                rectangles.add(frozenset((A,B,C,D)))
        sx,sy=A[0]+B[0],A[1]+B[1]
        for vx,vy in vectors[dx*dx+dy*dy]:
            if (sx+vx)%2 or (sy+vy)%2:
                continue
            C=((sx+vx)//2,(sy+vy)//2)
            D=((sx-vx)//2,(sy-vy)//2)
            rect=frozenset((A,B,C,D))
            if len(rect)==4 and inside(C) and inside(D):
                rectangles.add(rect)
    presentations=defaultdict(list)
    hidden=[]
    for rect in rectangles:
        white=rect-black
        if not white:
            hidden.append(rect)
        if len(white)<=2:
            presentations[white].append(rect)
    assert not hidden
    collisions={w:rs for w,rs in presentations.items() if len(rs)>1}
    parked={w:rs for w,rs in presentations.items() if len(w)==1}
    z=(b-2)//4
    for white,rs in parked.items():
        assert len(rs)==1
        (wx,wy),=white
        assert wy==b-1 and wx%2==1 and z%abs(wx)==0
    for white,rs in collisions.items():
        assert len(white)==2
        P,Q=sorted(white)
        assert P[1]==Q[1]==(b+2)//2
        assert P[0]%4==Q[0]%4==2
        assert any((0,b) in rect for rect in rs)
        assert any({(P[0],1),(Q[0],1)}<=rect for rect in rs)
    if b==6:
        assert not collisions
    else:
        assert collisions
    return {'a':a,'b':b,'radius':radius,'rectangles_with_two_black':len(rectangles),
            'parked_white_cells':len(parked),'colliding_presentations':len(collisions),
            'status':'PASS'}


def main():
    cases=[check(a,b,radius) for a,b,radius in
           [(3,6,20),(7,6,20),(11,6,20),(3,14,20),(11,14,20),(19,22,50)]]
    result={'status':'PASS','cases':cases}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
