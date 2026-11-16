"""Check the (E;O,E) cross-block formula against brute-force geometry.
Stride 4, block c at columns 4(i + P c). Small P on purpose (formula is algebra, valid for any P>2h)."""
import sys, random, math
import numpy as np
from common import *

h = int(sys.argv[1]); P = int(sys.argv[2]); seed = int(sys.argv[3])
random.seed(seed)
A, K = params(h)
cls = all_classes(h)
random.shuffle(cls)
C = len(cls)
# points
blk = []  # per block: (s, set slots)
for c, (s, sl) in enumerate(cls):
    blk.append((s, set(sl)))
even = []  # (x, y, c, i)
for c, (s, sl) in enumerate(cls):
    for i in sl:
        even.append((4*(i+P*c), 2*(i+s)+2, c, i))
E = np.array(even)
# brute force: V even, Pt odd in V's block, Q even in other block, right angle at V
brute = set()
for (xv, yv, c0, i0) in even:
    s0 = blk[c0][0]; T0 = 2*s0+1
    for i1 in blk[c0][1]:
        if i1 == i0: continue
        a = 4*(i1-i0); b = (2*i1+1) - yv
        X = E[:,0]-xv; Y = E[:,1]-yv
        mask = (E[:,2] != c0) & (a*X + b*Y == 0)
        for k in np.nonzero(mask)[0]:
            brute.add((c0, i0, i1, int(E[k,2]), int(E[k,3])))
# formula: for (V, t1, c'), u = -ds + 8 t1 N/(10 t1 - T0), N = ds - P dc
form = set(); fourth_ok = True
for (xv, yv, c0, i0) in even:
    s0 = blk[c0][0]; T0 = 2*s0+1
    for i1 in blk[c0][1]:
        t1 = i1 - i0
        if t1 == 0: continue
        for c1 in range(C):
            if c1 == c0: continue
            s1 = blk[c1][0]; ds = s1 - s0; dc = c1 - c0
            N = ds - P*dc
            num = 8*t1*N; den = 10*t1 - T0
            if num % den: continue
            u = -ds + num//den
            iq = i0 + u
            if iq in blk[c1][1]:
                form.add((c0, i0, i1, c1, iq))
                # fourth corner
                Pp = (4*(i1+P*c0), 2*i1+1); Q = (4*(iq+P*c1), 2*(iq+s1)+2)
                R = (Pp[0]+Q[0]-xv, Pp[1]+Q[1]-yv)
                if R != (4*(iq+t1+P*c1), 2*(iq+t1+ds)+1): fourth_ok = False
                # divisibility claim m | N
                g = math.gcd(t1, T0); m = abs(den)//g
                if N % m: fourth_ok = False
print("h", h, "P", P, "classes", C, "brute", len(brute), "formula", len(form), "equal", brute == form, "fourth/m-claims ok", fourth_ok)
