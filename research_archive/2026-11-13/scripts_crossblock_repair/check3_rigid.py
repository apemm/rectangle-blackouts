"""Brute-force check of the 2-adic rigid rule s_c - P*pos_c = const mod 2^r, 2^(r+3) >= K.
Counts ALL tilted right angles (E;O,E) with V,P in one block and Q an even point of another block,
by geometry only (no formula). Compares a random layout with the rigid layout.
Also counts every tilted right angle among all label points (any type) when full=1."""
import sys, random
import numpy as np
from common import *

h = int(sys.argv[1]); P = int(sys.argv[2]); seed = int(sys.argv[3]); full = int(sys.argv[4]) if len(sys.argv) > 4 else 0
random.seed(seed)
A, K = params(h)
cls = all_classes(h)
C = len(cls)
r = 0
while 2**(r+3) < K: r += 1
M = 2**r
Pinv = pow(P, -1, M) if M > 1 else 0

def layout_random():
    order = cls[:]; random.shuffle(order)
    return [(s, sl, c) for c, (s, sl) in enumerate(order)]
def layout_rigid():
    nxt = {}
    out = []
    order = cls[:]; random.shuffle(order)
    for (s, sl) in order:
        rho = (Pinv*s) % M if M > 1 else 0
        k = nxt.get(rho, 0); nxt[rho] = k+1
        out.append((s, sl, rho + M*k))
    return out

def count_EOE(lay):
    even = []; odd = []
    for b, (s, sl, pos) in enumerate(lay):
        for i in sl:
            even.append((4*(i+P*pos), 2*(i+s)+2, b)); odd.append((4*(i+P*pos), 2*i+1, b))
    E = np.array(even)
    cnt = 0
    for b, (s, sl, pos) in enumerate(lay):
        for i0 in sl:
            xv, yv = 4*(i0+P*pos), 2*(i0+s)+2
            for i1 in sl:
                if i1 == i0: continue
                a = 4*(i1-i0); bb = (2*i1+1) - yv
                X = E[:,0]-xv; Y = E[:,1]-yv
                cnt += int(np.count_nonzero((E[:,2] != b) & (a*X + bb*Y == 0)))
    return cnt

def count_all_tilted(lay):
    pts = []
    for b, (s, sl, pos) in enumerate(lay):
        for i in sl:
            pts.append((4*(i+P*pos), 2*i+1)); pts.append((4*(i+P*pos), 2*(i+s)+2))
    Pa = np.array(pts)
    tot = 0
    for k in range(len(pts)):
        D = Pa - Pa[k]
        nz = np.any(D != 0, axis=1)
        Dn = D[nz]
        G = Dn @ Dn.T
        # pairs (u,v) with u.v = 0, u != v, both legs non-axis (tilted)
        tilt = (Dn[:,0] != 0) & (Dn[:,1] != 0)
        Z = (G == 0) & np.outer(tilt, tilt)
        tot += int(np.count_nonzero(np.triu(Z, 1)))
    return tot

for name, lay in (("random", layout_random()), ("rigid", layout_rigid())):
    span = max(p for _, _, p in lay) + 1
    msg = f"h={h} P={P} 2^r={M} classes={C} layout={name} positions={span} EOE_crossblock={count_EOE(lay)}"
    if full: msg += f" all_tilted_right_angles={count_all_tilted(lay)}"
    print(msg)
