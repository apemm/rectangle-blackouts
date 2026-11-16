"""Exact polynomial audit of the three-direction P cycle."""
from itertools import combinations, permutations
from math import isqrt
import json
from pathlib import Path


def points(t):
    a = 2000*t+3
    return [(0,a), (0,a+715*t+8),
            (624*t,a+4), (624*t,a+715*t),
            (2052*t,a+8), (2052*t,a+715*t+4)]


def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def norm(x): return dot(x,x)


def polynomial(f):
    c, v1, v2 = (f(t) for t in range(3))
    assert (v2-2*v1+c)%2 == 0
    a=(v2-2*v1+c)//2
    return a,v1-a-c,c


def value(poly,t):
    a,b,c=poly
    return (a*t+b)*t+c


def positive_integer_roots(poly):
    a,b,c=poly
    if a==b==c==0: return None
    if a==0:
        return {-c//b} if b and -c%b==0 and -c//b>0 else set()
    disc=b*b-4*a*c
    if disc<0: return set()
    z=isqrt(disc)
    if z*z!=disc:return set()
    return {n//(2*a) for n in (-b-z,-b+z)
            if n%(2*a)==0 and n//(2*a)>0}


def audit():
    triangle_roots=[]
    for ids in combinations(range(6),3):
        for v in ids:
            ends=[i for i in ids if i!=v]
            poly=polynomial(lambda t: dot(sub(points(t)[ends[0]],points(t)[v]),
                                         sub(points(t)[ends[1]],points(t)[v])))
            roots=positive_integer_roots(poly)
            assert roots is not None
            triangle_roots.extend((ids,v,t) for t in roots)
    mixed_roots=[]
    for a,b,c,d in permutations(range(6),4):
        eq1=polynomial(lambda t: norm(sub(points(t)[b],points(t)[a]))
                      -norm(sub(points(t)[d],points(t)[c])))
        eq2=polynomial(lambda t: dot(sub(points(t)[b],points(t)[a]),
                     sub(add(points(t)[c],points(t)[d]),
                         add(points(t)[a],points(t)[b]))))
        roots=positive_integer_roots(eq1)
        if roots is None: roots=positive_integer_roots(eq2)
        assert roots is not None
        mixed_roots.extend(((a,b,c,d),t) for t in roots
                           if value(eq1,t)==value(eq2,t)==0)
    assert not [x for x in triangle_roots if x[-1]>=33]
    assert not [x for x in mixed_roots if x[-1]>=33]
    cases=[]
    for t in [33,37,65,101,1001]:
        p=points(t);h=4000*t
        for u,v,z in [(0,1,949),(1,2,1597),(2,0,2173)]:
            odd,even=p[2*u],p[2*v+1]
            X=abs(odd[0]-even[0]);Y=even[1]-odd[1]
            assert Y==715*t and X*X+Y*Y==(z*t)**2
            rows=((odd[1]+even[1]-z*t)//2,
                  (odd[1]+even[1]+z*t)//2)
            assert (odd[1]+even[1]-z*t)%2==0
            assert 1<=rows[0]<rows[1]<=h
            reverse=norm(sub(p[2*v],p[2*u+1]))
            assert isqrt(reverse)**2!=reverse
        cases.append(dict(t=t,height=h))
    return dict(status='PASS', forward_triples=[[624,715,949],
                [1428,715,1597],[2052,715,2173]],
                triangle_integer_roots=triangle_roots,
                mixed_integer_roots=mixed_roots,cases=cases,
                scope='six protected points; no Hilbert embedding or full private-block higher-support audit')


if __name__=='__main__':
    result=audit()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result))
