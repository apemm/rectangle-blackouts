from core import *
# hand checks
# h=2,m=2: only rectangle is the full 2x2 square (no diagonal fits). 1 rectangle -> valid for any S
print(len(rects(2,2)), is_valid(2,2,set()))
# h=2,m=3: axis rects: 3 column pairs; diagonal: need s,t nonzero with |s|,|t|<=1: V=(1,1)? points (2,2),(2,0) out. V=(2,1): (3,2)... (3,0) out. none.
print(len(rects(2,3)))
print("no black:", is_valid(2,3,set()))  # all white, distinct corner sets -> valid
print("all black:", is_valid(2,3,{(x,y) for x in (1,2,3) for y in (1,2)}))  # two fully black rects collide
print("col1 black:", is_valid(2,3,{(1,1),(1,2)}))  # rects {1,2},{1,3}: whites (2,1),(2,2) vs (3,1),(3,2) distinct -> valid
print("cols1,2 black:", is_valid(2,3,{(1,1),(1,2),(2,1),(2,2)}))  # {1,2} all black ; {1,3} whites at col3 ; {2,3} whites col3 -> collision
# h=3,m=3: diagonal: V=(2,2)? s=1,t=1: (3,3),(3,1),(4,2) out. V=(1,2),s=1,t=1: (2,3),(2,1),(3,2): diamond. 
print(len(rects(3,3)), sum(1 for r in rects(3,3) if len({p[0] for p in r})==3))
