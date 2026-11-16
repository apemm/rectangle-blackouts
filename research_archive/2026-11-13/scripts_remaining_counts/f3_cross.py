# Cross-block F3 check: L2 - L1 = (Dx, Dy) with Dx = 2Dy + 4*DM (odd points) or Dx = 4*(Dy/2 + DM') style.
# parity 'o': y_L odd, y_L = r mod 64 (cong), Dy = 0 mod 64, DM = 0 mod 4, |Dx| >= 78h.
# parity 'e': y_E = y_P + T, Y1 odd; Dy = 0 mod 32 (R1), Dx = 4*(Dy/2 - Ds + DM), Ds = 0 mod 16, DM = Ds mod 16.
# Sizes: DM in a window; X1 over divisors of n_y*Y1.  cong=0 drops the residue conditions (control).
import sys
from sympy import divisors
par = sys.argv[1]; cong = int(sys.argv[2]); h = int(sys.argv[3]); typ = int(sys.argv[4]); DMmax = int(sys.argv[5])
RAT = float(sys.argv[6]); r = 1; T = 3 if typ == 3 else 1
Ts = max(y for y in range(h-70, h+1) if (y - r - (32 if typ==3 else 48)) % 64 == 0)
frow = [Ts-24+8*o for o in range(4)]
cnt = {}
if par == 'o':
    ys = [y for y in range(1, Ts-128, 2) if (not cong) or (y - r) % 64 == 0]
else:
    ys = [y + T for y in range(1, Ts-128-T, 2) if (not cong) or (y - r) % 64 == 0]
dystep = (64 if par=='o' else 32) if cong else 2
for yL1 in ys:
    for Dy in range(-(h-1), h, dystep):
        if not (1 <= yL1 + Dy < Ts-128): continue
        for o1 in range(4):
            for o2 in range(4):
                f1, f2 = frow[o1], frow[o2]; Y1 = f1 - yL1; df = f1 - f2
                if (Dy - df) % 2: continue
                ny = (Dy - df)//2
                if ny == 0 or not (1 <= yL1+ny <= h and 1 <= f1+ny <= h): continue
                for d in divisors(abs(ny*Y1)):
                    for X1 in (d, -d):
                        if X1 % 4: continue
                        if cong and (X1 - 4*o1) % 16: continue
                        nx = -(ny*Y1)//X1
                        if nx % 2: continue
                        # Z.W' = 0 with Zx = Dx - nx, W'x = X1 - Zx: quadratic in Dx; solve
                        Zy = Dy - ny; Wy = Y1 - Zy
                        # Zx*(X1 - Zx) = -Zy*Wy  ->  Zx^2 - X1 Zx - Zy*Wy = 0
                        disc = X1*X1 + 4*Zy*Wy
                        if disc < 0: continue
                        s = int(round(disc**0.5))
                        while s*s > disc: s -= 1
                        while (s+1)*(s+1) <= disc: s += 1
                        if s*s != disc: continue
                        for Zx2 in {X1 + s, X1 - s}:
                            if Zx2 % 2: continue
                            Zx = Zx2//2; Dx = Zx + nx
                            if abs(Dx) < RAT*h: continue
                            if par == 'o':
                                if (Dx - 2*Dy) % 4: continue
                                DM = (Dx - 2*Dy)//4
                                if cong and DM % 4: continue
                            else:
                                if Dx % 4: continue
                                if cong and Dx % 16: continue
                            cnt[df] = cnt.get(df,0)+1
print("par",par,"cong",cong,"h",h,"type",typ,"counts by df:",dict(sorted(cnt.items())))
