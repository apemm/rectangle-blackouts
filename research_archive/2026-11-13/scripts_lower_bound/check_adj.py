# sanity check: the width-9 window at h=8 has no tilted rectangle with >=3 black corners among rectangles
# that have a side of horizontal extent 1, but has such rectangles among the others.
from check_board import rectangles
h=8
cols=[(1,4),(7,8),(6,7),(1,6),(5,8),(3,4),(3,8),(1,2),(1,8)]
m=len(cols)
black=set()
for i,(r,s) in enumerate(cols):
    black.add((i+1,r)); black.add((i+1,s))
bad_adj=0; bad_other=0; ex=None
for b in range(1,h):
    for d in range(1,h-b):
        n=b*d
        for a in range(1,n+1):
            if n%a: continue
            c=n//a
            for r in range(1+b,h-d+1):
                for x in range(1,m-a-c+1):
                    R=[(x,r),(x+a,r-b),(x+c,r+d),(x+a+c,r-b+d)]
                    k=sum(1 for p in R if p in black)
                    if k>=3:
                        if a==1 or c==1: bad_adj+=1
                        else:
                            bad_other+=1
                            if ex is None: ex=(R,(a,b,c,d))
print('pairs distinct parity edges:',len(set(cols))==m and all((p[0]+p[1])%2==1 for p in cols))
print('rectangles with a side of horizontal extent 1 and >=3 black corners:',bad_adj)
print('other tilted rectangles with >=3 black corners:',bad_other,'example',ex)
