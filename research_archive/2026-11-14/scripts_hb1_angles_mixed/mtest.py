import math
from collections import defaultdict
def search(pts, h):
    n = len(pts); pairs = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            (xi, yi), (xj, yj) = pts[i][:2], pts[j][:2]
            pairs[(xi+xj, yi+yj, (xi-xj)**2+(yi-yj)**2)].append((i, j))
    found = []
    for i in range(n):
        for j in range(n):
            if i == j: continue
            (Ax, Ay), (Bx, By) = pts[i][:2], pts[j][:2]
            X, Y = Bx-Ax, By-Ay
            if X <= 0: continue
            g = math.gcd(X, abs(Y)); Xp, Yp = X//g, Y//g
            kmax = (2*h)//Xp + 2
            for k in range(-kmax, kmax+1):
                if k == 0: continue
                Tx, Ty = -k*Yp, k*Xp
                if not (1 <= Ay+Ty <= h and 1 <= By+Ty <= h): continue
                for (c, d) in pairs.get((Ax+Bx+2*Tx, Ay+By+2*Ty, X*X+Y*Y), ()):
                    for (ci, di) in ((c, d), (d, c)):
                        if {ci, di} & {i, j}: continue
                        Cx, Cy = pts[ci][:2]; Dx, Dy = pts[di][:2]
                        if (Dx-Cx, Dy-Cy) in ((X, Y), (-X, -Y)): continue
                        found.append((i, j, ci, di))
    return found
rows = [(0, 32769, 4), (32, 32771, 2), (1048544, 33795, 1026), (1048576, 33793, 1028)]
pts = []
for x, a, b in rows:
    pts += [(x+1, a), (x+1, b)]
f = search(pts, 34000)
print(len(f), [tuple(pts[z] for z in t) for t in f[:2]])
