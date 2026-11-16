# Toy cover for the Lemma F family in slot units (one parity).
# Option = (J, Y): slot J, label row index Y (row = r0 + 14Y, one label per row index).
# Conflict between (J1,Y1),(J2,Y2), Y1!=Y2: dJ^2 + (2 dY)^2 is a square (dJ != 0), or dJ == 0 (coincidence).
# For a central option o, count D, edges in N(o) that lie on a line through o (collinear), and cross edges.
import numpy as np, math, sys
def run(R, N, seed=0):
    J0, Y0 = N//2, R//2
    nb = []
    for Y in range(R):
        if Y == Y0: continue
        y = 2*(Y-Y0)
        nb.append((J0, Y))  # coincidence
        # X with X^2+y^2 square: (L-X)(L+X)=y^2
        yy = y*y; s=set()
        for u in range(1, abs(y)):
            if yy % u == 0:
                w = yy//u
                if (w-u) % 2 == 0:
                    X = (w-u)//2
                    for x in (X, -X):
                        if 0 <= J0+x < N and x != 0: s.add(x)
        for x in s: nb.append((J0+x, Y))
    nb = np.array(nb, dtype=np.int64)
    D = len(nb)
    a = nb[:,None,:]; b = nb[None,:,:]
    dJ = b[...,0]-a[...,0]; dY = b[...,1]-a[...,1]
    iu = np.triu_indices(D, 1)
    dJ = dJ[iu]; dY = dY[iu]
    q = dJ*dJ + 4*dY*dY
    r = np.round(np.sqrt(q.astype(np.float64))).astype(np.int64)
    sq = (r*r == q)
    adj = (dY != 0) & (sq | (dJ == 0))
    # collinear with o: (J1-J0, Y1-Y0) parallel to (J2-J1, Y2-Y1)
    v1J = nb[iu[0],0]-J0; v1Y = nb[iu[0],1]-Y0
    col = (v1J*dY - v1Y*dJ) == 0
    eline = int(np.sum(adj & col)); ecross = int(np.sum(adj & ~col))
    # random-model prediction for cross edges: D^2/2 * p, p = density of conflicting vectors among (dJ in [-N,N], dY in [-R,R])
    pairs = D*(D-1)//2
    return D, eline, ecross, pairs
for R, N in [(150, 1500), (300, 3000), (500, 5000)]:
    D, el, ec, P = run(R, N)
    print(f"R={R} N={N} D={D} D/R={D/R:.2f} line_edges={el} cross_edges={ec} pairs={P} line_frac={el/P:.4f} cross_frac={ec/P:.5f} D/(R*N)={D/(R*N):.5f}")
