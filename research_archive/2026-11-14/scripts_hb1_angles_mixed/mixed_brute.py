"""Brute-force nonvertical mixed four-supports among label points (small h).
Side A,B (X>0), diagonal C,D; C+D = A+B+2T, T perp U=B-A, |D-C|=|U|, T!=0, D-C != +-U.
Checks the sharpened bounds:
  even-vertical, mixed parity: |c-b| > M S^4/16 ;  odd vertical: |Y| > sqrt(M) S^4/(128 sqrt2)."""
import sys, json, math
import numpy as np
from collections import defaultdict
from angles import setup
h, S, M, seed = map(int, sys.argv[1:5])
D = setup(h, S, M, seed)
R = np.nonzero(D['act'])[0]
pts = [(int(S*D['slot'][r]), int(D['odd'][r]), r, 0) for r in R] + \
      [(int(S*D['slot'][r]), int(D['even'][r]), r, 1) for r in R]
n = len(pts)
pairs = defaultdict(list)
for i in range(n):
    xi, yi = pts[i][0], pts[i][1]
    for j in range(i+1, n):
        xj, yj = pts[j][0], pts[j][1]
        pairs[(xi+xj, yi+yj, (xi-xj)**2+(yi-yj)**2)].append((i, j))
found = []
xmin = min(p[0] for p in pts); xmax = max(p[0] for p in pts)
for i in range(n):
    for j in range(n):
        if i == j: continue
        Ax, Ay = pts[i][0], pts[i][1]; Bx, By = pts[j][0], pts[j][1]
        X, Y = Bx-Ax, By-Ay
        if X <= 0: continue
        g = math.gcd(X, abs(Y)); Xp, Yp = X//g, Y//g
        L2 = X*X+Y*Y
        kmax = (2*h)//Xp + 2
        for k in range(-kmax, kmax+1):
            if k == 0: continue
            Tx, Ty = -k*Yp, k*Xp
            # common corners in strip
            if not (1 <= Ay+Ty <= h and 1 <= By+Ty <= h): continue
            key = (Ax+Bx+2*Tx, Ay+By+2*Ty, L2)
            for (c, d) in pairs.get(key, ()):
                for (ci, di) in ((c, d), (d, c)):
                    Cx, Cy = pts[ci][0], pts[ci][1]; Dx, Dy = pts[di][0], pts[di][1]
                    if {ci, di} & {i, j}: continue
                    if (Dx-Cx, Dy-Cy) in ((X, Y), (-X, -Y)): continue
                    found.append((i, j, ci, di))
res = {'h': h, 'S': S, 'M': M, 'supports': len(found)}
viol = 0; cases = defaultdict(int); minr = {}
for (i, j, ci, di) in found:
    A, B, C, Dd = pts[i], pts[j], pts[ci], pts[di]
    Y = B[1]-A[1]
    if Y % 2 == 0:
        if A[3] == C[3]:
            cases['even_same_parity'] += 1; continue
        # R2 axis aligned: rows of C and D; |c - b| where C shares row with B+T
        cb = min(abs(C[1]-B[1]), abs(Dd[1]-B[1]))
        r = max(abs(C[1]-B[1]), abs(Dd[1]-B[1])) / (M*S**4/16)
        cases['even_mixed'] += 1
        minr['even_mixed'] = min(minr.get('even_mixed', 9e9), r)
        if r <= 1: viol += 1
    else:
        # orient C same parity as A
        if C[3] != A[3]: C, Dd = Dd, C
        m, nn = C[0]-A[0], Dd[0]-B[0]
        tag = 'odd_same_sign' if m*nn > 0 else 'odd_opp_sign'
        r = abs(Y) / (math.sqrt(M)*S**4/(128*math.sqrt(2)))
        cases[tag] += 1
        minr[tag] = min(minr.get(tag, 9e9), r)
        if r <= 1: viol += 1
res.update({'cases': dict(cases), 'min_ratio': minr, 'bound_violations': viol})
print(json.dumps(res))
