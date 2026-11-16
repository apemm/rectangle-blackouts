# Within-class F3 (side {L1,F1}, diagonal {L2,F2}, L2-L1=(4t,2t)) checked directly against Lemma mixedeq:
# build the 4 points, verify n.(B-A)=0, C+D=A+B+2n, |D-C|=|B-A|, D-C != +-(B-A), p,q rows in grid.
# layer: 'saw' (y_L = r mod 32, t = 0 mod 16, T* = r mod 16) or 'saws' (y_L = r mod 64, t = 0 mod 32, T* = r+32/48 mod 64)
# par: 'o' labels at odd rows y_L; 'e' labels at even rows y_L + T (T odd, fixed).
import sys
from sympy import divisors
layer, par, h, T = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
r = int(sys.argv[5]) if len(sys.argv)>5 else 1
if layer == 'saw':
    Ts = max(y for y in range(h-20, h+1) if (y - r) % 16 == 0); ymod, tmod = 32, 16
else:
    Ts = max(y for y in range(h-70, h+1) if (y - r - (32 if T % 4 == 3 else 48)) % 64 == 0); ymod, tmod = 64, 32
frow = [Ts-24+8*o for o in range(4)]
cnt = {}
for yP in range(r, Ts-128-T, ymod):
    yL1 = yP if par == 'o' else yP + T
    for t in range(-(h//2), h//2+1, tmod):
        if t == 0: continue
        L1 = (0, yL1); L2 = (4*t, yL1 + 2*t)
        if not (1 <= L2[1] < Ts-128): continue
        for o1 in range(4):
            for o2 in range(4):
                f1, f2 = frow[o1], frow[o2]; Y1 = f1 - yL1; df = f1 - f2
                ny = (2*t - df)//2
                if ny == 0: continue
                for d in divisors(abs(ny*Y1)):
                    for X1 in (d, -d):
                        if (X1 - 4*o1) % 16: continue
                        if (ny*Y1) % X1: continue
                        nx = -(ny*Y1)//X1
                        F1 = (X1, f1); n = (nx, ny)
                        F2 = (L1[0]+F1[0]+2*nx-L2[0], L1[1]+F1[1]+2*ny-L2[1])
                        if F2[1] != f2 or (F2[0] - L1[0] - 4*o2) % 16: continue
                        A, B, C, D = L1, F1, L2, F2
                        U = (B[0]-A[0], B[1]-A[1]); V = (D[0]-C[0], D[1]-C[1])
                        assert n[0]*U[0]+n[1]*U[1] == 0
                        if U[0]**2+U[1]**2 != V[0]**2+V[1]**2: continue
                        if V == U or V == (-U[0], -U[1]): continue
                        p = (A[0]+nx, A[1]+ny); q = (B[0]+nx, B[1]+ny)
                        if not (1 <= p[1] <= h and 1 <= q[1] <= h): continue
                        cnt[df] = cnt.get(df,0)+1
                        if len(sys.argv)>6: print("  sol", "L1",L1,"F1",F1,"L2",L2,"F2",F2,"n",n)
print(layer, par, "h", h, "T", T, "counts by df (f1-f2):", dict(sorted(cnt.items())))
