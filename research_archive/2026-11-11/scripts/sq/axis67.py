import itertools
def girth_ok(cols):
    for x,y in itertools.combinations(cols,2):
        if len(x&y) >= 2: return False
    for x,y,w in itertools.combinations(cols,3):
        for r1 in x&y:
            for r2 in y&w:
                for r3 in x&w:
                    if len({r1,r2,r3})==3: return False
    return True
c6 = [{1,2,3},{4,5,6},{1,4},{2,5},{3,6},{1}]
c7 = [{1,2,3},{4,5,6},{1,4},{2,5},{3,6},{7,1},{7,5}]
for name, cols, n in [("6x6", c6, 6), ("7x7", c7, 7)]:
    print(name, "columns", len(cols), "points", sum(len(s) for s in cols), "girth>=8:", girth_ok(cols))
