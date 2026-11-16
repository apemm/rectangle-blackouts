# Cross-class F3 check (SAW*, odd: Dx = 4(Di+DM), Dy = 2Di, Di = 0 mod 32, DM = 0 mod 4 (L**));
# even with R1: Dx = 4(Di+DM), Dy = 2(Di+Ds), Di = 0 mod 32, Ds = 0 mod 16, DM = Ds mod 16.
# cong=0 control: Di, DM, Ds arbitrary.  Direct mixedeq verification as in f3_class_general.py.
import sys
from sympy import divisors
par, cong, h, T, r, Rm = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
Ts = max(y for y in range(h-70, h+1) if (y - r - (32 if T % 4 == 3 else 48)) % 64 == 0)
frow = [Ts-24+8*o for o in range(4)]
vecs = set()
for Di in range(-(h//2), h//2+1):
    if cong and Di % 32: continue
    for DM in range(-Rm, Rm+1):
        if par == 'o':
            if cong and DM % 4: continue
            if Di == 0 and DM == 0: continue
            vecs.add((4*(Di+DM), 2*Di))
        else:
            for Ds in range(-8, 9) if not cong else (-16, 0, 16):
                if cong and (DM - Ds) % 16: continue
                if Di == 0 and DM == 0 and Ds == 0: continue
                vecs.add((4*(Di+DM), 2*(Di+Ds)))
cnt = {}
for yP in range(r, Ts-128-T, 64 if cong else 2):
    yL1 = yP if par == 'o' else yP + T
    for (Dx, Dy) in vecs:
        L1 = (0, yL1); L2 = (Dx, yL1 + Dy)
        if not (1 <= L2[1] < Ts-128): continue
        for o1 in range(4):
            for o2 in range(4):
                f1, f2 = frow[o1], frow[o2]; Y1 = f1 - yL1; df = f1 - f2
                if (Dy - df) % 2: continue
                ny = (Dy - df)//2
                if ny == 0: continue
                for d in divisors(abs(ny*Y1)):
                    for X1 in (d, -d):
                        if (X1 - 4*o1) % 16: continue
                        nx = -(ny*Y1)//X1
                        F1 = (X1, f1)
                        F2 = (F1[0]+2*nx-L2[0], F1[1]+L1[1]+2*ny-L2[1])
                        if F2[1] != f2 or (F2[0] - 4*o2) % 16: continue
                        U = (F1[0], F1[1]-L1[1]); V = (F2[0]-L2[0], F2[1]-L2[1])
                        if U[0]**2+U[1]**2 != V[0]**2+V[1]**2 or V == U or V == (-U[0],-U[1]): continue
                        if not (1 <= L1[1]+ny <= h and 1 <= F1[1]+ny <= h): continue
                        cnt[df] = cnt.get(df,0)+1
print(par, "cong", cong, "h", h, "T", T, "r", r, "DMrange", Rm, "counts by df:", dict(sorted(cnt.items())))
