import itertools
# rows: p,p2,a,b,c,d,e,z -> 0..7
p,p2,a,b,c,d,e,z = range(8)
cols = [{p,a,b},{p,p2,c},{p2,d,e},{a,d},{b,e},{z,a},{z,c},{z,e}]
def girth_ok(cols):
    # no two columns share 2 rows (C4); no three columns pairwise sharing three distinct rows (C6)
    for x,y in itertools.combinations(cols,2):
        if len(x&y) >= 2: return False, ('C4',x,y)
    for x,y,w in itertools.combinations(cols,3):
        for r1 in x&y:
            for r2 in y&w:
                for r3 in x&w:
                    if len({r1,r2,r3})==3: return False, ('C6',x,y,w)
    return True, None
print("8x8 construction:", girth_ok(cols), "cells:", sum(len(s) for s in cols))
# Neuwirth cubic bound for balanced n
def cubic_bound(v,w):
    e = 0
    while (e+1)**3 - (v+w)*(e+1)**2 + 2*v*w*(e+1) - v*v*w*w <= 0: e += 1
    return e
print([ (n, cubic_bound(n,n)) for n in range(3,13)])
try:
    import pysat
    print("pysat available", pysat.__version__)
except Exception as ex:
    print("no pysat:", ex)
