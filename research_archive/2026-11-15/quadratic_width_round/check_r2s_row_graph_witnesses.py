"""Direct rectangle verification of finite R2s row-graph obstructions."""
from pathlib import Path
import json


TRIANGLE=(
    (22250,22270,2220,2225,200,-2015),
    (22250,22306,2176,2225,560,-1567),
    (22270,22306,1456,1530,524,-858),
)
STAR=(
    (16575,16591,800,850,312,-438),
    (16575,16599,888,975,408,-393),
    (16575,16607,992,1105,480,-399),
    (16575,16623,2192,2210,360,-1814),
    (16575,16635,3820,3825,260,-3555),
    (16575,16731,14364,14365,180,-14183),
)
PATH=(
    (168510,168750,61648,61650,656,-60990),
    (168750,168950,31240,31250,1080,-30150),
    (168950,168970,640,5450,620,4790),
    (168970,169006,12460,12465,488,-11967),
)


def rectangle(v):
    a,b,c,d=v
    assert len(set(v))==4
    assert all(a[i]+c[i]==b[i]+d[i] for i in (0,1))
    assert sum((a[i]-c[i])**2 for i in (0,1))==sum((b[i]-d[i])**2 for i in (0,1))


def verify(z):
    n,target,X,U,T,V=z;delta=target-n
    assert delta>0 and delta%4==0 and T%2==0
    assert X>0 and X%4==0 and U%4 and (X+V)%4
    assert delta*delta<=2*X and T*U==n*delta
    assert V*V==U*U-2*n*delta-delta*delta
    assert 2*X==U+T-V
    A,B,C,D=(0,n+1),(U,1),(X,target+1),(X+V,1)
    P,Q=(T//2,n+1+delta//2),(U+T//2,1+delta//2)
    rectangle((A,B,Q,P));rectangle((C,P,D,Q))
    assert len({A,B,C,D,P,Q})==6
    assert min(p[1] for p in (A,B,C,D,P,Q))>=1
    assert max(p[1] for p in (A,B,C,D,P,Q))<=target+1
    assert max(p[0] for p in (A,B,C,D,P,Q))-min(p[0] for p in (A,B,C,D,P,Q))<=target
    for mask in range(4):
        black={A,B,C,D}|({P} if mask&1 else set())|({Q} if mask&2 else set())
        assert {A,B,Q,P}-black=={C,P,D,Q}-black


def audit():
    for edge in TRIANGLE+STAR+PATH:verify(edge)
    vertices=sorted({x for e in TRIANGLE for x in e[:2]})
    assert {(u,v) for u in vertices for v in vertices if u<v}=={e[:2] for e in TRIANGLE}
    assert len({e[0] for e in STAR})==1 and len({e[1] for e in STAR})==6
    assert all(PATH[i][1]==PATH[i+1][0] for i in range(3))
    return dict(status='PASS',triangle_rows=[v+1 for v in vertices],
                star_source_row=STAR[0][0]+1,outdegree_lower_bound=6,
                directed_path_rows=[PATH[0][0]+1]+[e[1]+1 for e in PATH],
                supports=13,common_corner_colorings=52,
                scope='Individual realizable row-pair edges, not a simultaneous placement of all graph edges.')


if __name__=='__main__':
    result=audit()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
