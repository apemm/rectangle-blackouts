"""Toy brute force: which multi-label support roles occur in an aligned
period-seven block with label columns = 0 mod 28 placed at RANDOM
(no Hilbert locality).  Prediction from the mod-7 sieve and the 2-adic
alignment lemmas: the only corner triples with >= 2 labels are
  PT  : right angle at a label point, other end a same-parity point of
        another label, third corner a sea point;
  LBL : label-only;
and the only mixed quadruples with >= 2 labels are
  R2s : side (label pt, sea) and diagonal (label pt, sea), same label
        parity and same sea row;
  HOR : a same-parity label pair at integral distance against a
        horizontal sea pair (R1/R3 with horizontal sea side or diagonal);
  LBL : label-only.
Anything else is printed as UNEXPECTED.
usage: py toy_roles.py block seed
"""
import sys, random, math
import numpy as np

block = sys.argv[1]; seed = int(sys.argv[2]); random.seed(seed)
h = 420
L, F, H = 17, 41, 396   # MISALIGNED control
oddres = 17                   # odd label rows = 17 mod 28 (=3 mod 7, 1 mod 4)
evenres = 8 if block == 'mixed' else 24   # 8: =1 mod 7 (5g, g=1); 24: =3 mod 7
assert evenres % 4 == 0
QR = {1, 2, 4}
def sea(x):
    r = x % 7
    return F if r == 0 else (H if r in QR else L)

odd_rows = [a for a in range(60, 400) if a % 28 == oddres]
even_rows = [b for b in range(60, 400) if b % 28 == evenres]
pairs = [(a, b) for a in odd_rows for b in even_rows]
random.shuffle(pairs)
nlab = int(sys.argv[3])
labs = pairs[:nlab]
cols = random.sample(range(0, int(sys.argv[4])), nlab)
cols = [28 * c for c in cols]
X0, X1 = -800, 28*int(sys.argv[4]) + 800
lab_at = {c: lab for c, lab in zip(cols, labs)}
black = {}
for x in range(X0, X1):
    if x in lab_at:
        a, b = lab_at[x]
        black[(x, a)] = ('O', x); black[(x, b)] = ('E', x)
    else:
        black[(x, sea(x))] = ({L: 'L', F: 'F', H: 'H'}[sea(x)], None)
def isb(p):
    return p in black
labpts = [(x, y) for x in cols for y in lab_at[x]]

def typ(p):
    t, c = black[p]; return t
def labof(p):
    return black[p][1]

found = {}
def rec(kind, key, ex):
    found.setdefault((kind, key), ex)

# corner triples with >= 2 label points from >= 2 labels
xs = np.arange(X0, X1)
for i in range(len(labpts)):
    for j in range(len(labpts)):
        if i == j: continue
        P, Q = labpts[i], labpts[j]
        if P[0] == Q[0]:
            # same label: right angle at third point R on circle of diameter PQ
            pass
        # right angle at P, other end Q, third point R:  (R-P).(Q-P)=0
        dx, dy = Q[0]-P[0], Q[1]-P[1]
        if dx == 0 or dy == 0:
            continue
        for x in range(X0, X1):
            num = -dx * (x - P[0])
            if num % dy: continue
            y = P[1] + num // dy
            R = (x, y)
            if R == P or R == Q or not isb(R): continue
            W = (Q[0] + R[0] - P[0], Q[1] + R[1] - P[1])
            if not (1 <= W[1] <= h): continue
            if R[0] == P[0]: continue
            labs_used = {labof(T) for T in (P, Q, R) if labof(T) is not None}
            if len(labs_used) < 2: continue
            tt = (typ(P), typ(Q), typ(R))
            if typ(R) in 'LFH':
                kind = 'PT' if tt[0] == tt[1] else 'UNEXPECTED'
            else:
                kind = 'LBL'
            rec(kind, 'vertex%s|%s,%s' % tt, (P, Q, R, W))
# right angle at a sea point with two label ends (circle of diameter PQ)
for i in range(len(labpts)):
    for j in range(i+1, len(labpts)):
        P, Q = labpts[i], labpts[j]
        for x in range(X0, X1):
            # (R-P).(R-Q)=0 -> (x-P0)(x-Q0) + (y-P1)(y-Q1) = 0
            c = (x-P[0])*(x-Q[0])
            # y^2 - (P1+Q1) y + P1 Q1 + c = 0
            s_, p_ = P[1]+Q[1], P[1]*Q[1] + c
            disc = s_*s_ - 4*p_
            if disc < 0: continue
            r = math.isqrt(disc)
            if r*r != disc: continue
            for y in {(s_+r)//2, (s_-r)//2}:
                if (s_ + r) % 2: continue
                R = (x, y)
                if R in (P, Q) or not isb(R) or typ(R) not in 'LFH': continue
                W = (P[0]+Q[0]-x, P[1]+Q[1]-y)
                if not (1 <= W[1] <= h): continue
                if x in (P[0], Q[0]) or y in (P[1], Q[1]): continue
                if labof(P) == labof(Q): continue
                rec('UNEXPECTED', 'seavertex%s|%s,%s' % (typ(R), typ(P), typ(Q)), (R, P, Q, W))

# mixed quadruples: side A,B ; diagonal C,D.  Enumerate with two label points
# placed among the three "given" points, solve the fourth.
def solve_D(A, B, C):
    U = (B[0]-A[0], B[1]-A[1]); nU = U[0]**2 + U[1]**2
    if nU == 0: return []
    k = -(U[0]*(2*C[0]-A[0]-B[0]) + U[1]*(2*C[1]-A[1]-B[1]))  # U.V = k, |V|^2=nU
    out = []
    # parametrize V = (k U + t U_perp)/nU with t^2 = nU*nU - k^2 ... over integers
    t2 = nU*nU - k*k
    if t2 < 0: return out
    t = math.isqrt(t2)
    if t*t != t2: return out
    for sgn in ({t, -t}):
        vx = k*U[0] - sgn*U[1]; vy = k*U[1] + sgn*U[0]
        if vx % nU or vy % nU: continue
        out.append((C[0]+vx//nU, C[1]+vy//nU))
    return out
def solve_B(C, D, A):
    # U = B-A with |U|^2 = |V|^2 and U.(C+D-2A) = |U|^2
    V = (D[0]-C[0], D[1]-C[1]); nV = V[0]**2 + V[1]**2
    G = (C[0]+D[0]-2*A[0], C[1]+D[1]-2*A[1]); nG = G[0]**2 + G[1]**2
    if nG == 0: return []
    # U.G = nV, |U|^2 = nV -> U = (nV G + t Gperp)/nG, t^2 = nV nG - nV^2
    t2 = nV*nG - nV*nV
    if t2 < 0: return []
    t = math.isqrt(t2)
    if t*t != t2: return []
    out = []
    for sgn in ({t, -t}):
        ux = nV*G[0] - sgn*G[1]; uy = nV*G[1] + sgn*G[0]
        if ux % nG or uy % nG: continue
        out.append((A[0]+ux//nG, A[1]+uy//nG))
    return out

def check_quad(A, B, C, D):
    pts = (A, B, C, D)
    if len(set(pts)) < 4 or not all(isb(p) for p in pts): return
    U = (B[0]-A[0], B[1]-A[1]); V = (D[0]-C[0], D[1]-C[1])
    if U[0] == 0: return               # vertical side -> rival, not here
    if V == U or V == (-U[0], -U[1]): return
    Tx2, Ty2 = C[0]+D[0]-A[0]-B[0], C[1]+D[1]-A[1]-B[1]
    if Tx2 % 2 or Ty2 % 2 or (Tx2, Ty2) == (0, 0): return
    if U[0]*Tx2 + U[1]*Ty2 != 0 or U[0]**2+U[1]**2 != V[0]**2+V[1]**2: return
    p = (A[0]+Tx2//2, A[1]+Ty2//2); q = (B[0]+Tx2//2, B[1]+Ty2//2)
    if not (1 <= p[1] <= h and 1 <= q[1] <= h): return
    labs_used = {labof(T) for T in pts if labof(T) is not None}
    if len(labs_used) < 2: return
    side = ''.join(sorted(typ(A)+typ(B))); diag = ''.join(sorted(typ(C)+typ(D)))
    nlabpts = sum(t in 'OE' for t in side+diag)
    if nlabpts == 4:
        kind = 'LBL'
    elif nlabpts == 2 and side[0] in 'OE' and side[1] in 'LFH' and diag[0] in 'OE' and diag[1] in 'LFH':
        kind = 'R2s' if (side == diag) else 'UNEXPECTED'
    elif nlabpts == 2 and ((A[1] == B[1] and side[0] in 'LFH') or (C[1] == D[1] and diag[0] in 'LFH')):
        kind = 'HOR'
    else:
        kind = 'UNEXPECTED'
    rec(kind, side + '|' + diag, pts)

allpts = list(black.keys())
for i in range(len(labpts)):
    for j in range(len(labpts)):
        if i == j: continue
        P, Q = labpts[i], labpts[j]
        if labof(P) == labof(Q): continue
        for R in allpts:
            # (P,Q | R, D), (P,R | Q, D), (R,P | Q, D) with D solved
            for D in solve_D(P, Q, R): check_quad(P, Q, R, D)
            for D in solve_D(P, R, Q): check_quad(P, R, Q, D)
            # diagonal (P,Q), side (R, B)
            for Bp in solve_B(P, Q, R): check_quad(R, Bp, P, Q)
for (kind, key), ex in sorted(found.items()):
    print(kind, key, ex)
print('labels', nlab, 'done')
