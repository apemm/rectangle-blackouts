# Same as f3_2adic_check.py but X1 runs over the divisors of n_y*Y1 (n_x = -n_y Y1/X1 must be an integer).
# mode class: L2-L1 = (4t,2t).  cong=1: SAW* congruences (y_L = r mod 64, t = 0 mod 32, X1 = 4 o1 mod 16,
# filler rows by offset).  cong=0: y_L any odd row, t any, X1 any multiple of 4 (control).
import sys
from sympy import divisors
mode = sys.argv[1]; cong = int(sys.argv[2]); h = int(sys.argv[3]); typ = int(sys.argv[4])
r = 1
Ts = max(y for y in range(h-70, h+1) if (y - r - (32 if typ==3 else 48)) % 64 == 0)
frow = [Ts-24+8*o for o in range(4)]
cnt = {}; ex = {}
ys = [y for y in range(1, Ts-128, 2) if (not cong) or (y - r) % 64 == 0]
tstep = 32 if cong else 1
for yL1 in ys:
    for t in range(-(h//2), h//2+1):
        if t == 0 or t % tstep: continue
        Dx, Dy = 4*t, 2*t
        if not (1 <= yL1 + Dy < Ts-128): continue
        for o1 in range(4):
            for o2 in range(4):
                f1, f2 = frow[o1], frow[o2]; Y1 = f1 - yL1; df = f1 - f2
                ny = (Dy - df)//2
                if ny == 0: continue
                if not (1 <= yL1+ny <= h and 1 <= f1+ny <= h): continue
                for d in divisors(abs(ny*Y1)):
                    for X1 in (d, -d):
                        if X1 % 4: continue
                        if cong and (X1 - 4*o1) % 16: continue
                        nx = -(ny*Y1)//X1
                        if nx % 2: continue
                        Zx, Zy = Dx - nx, Dy - ny
                        Wx, Wy = X1 - Zx, Y1 - Zy
                        if Zx*Wx + Zy*Wy: continue
                        cnt[df] = cnt.get(df,0)+1
                        ex.setdefault(df, (yL1, t, o1, o2, X1, nx, ny))
print("cong",cong,"h",h,"type",typ,"counts by df:",dict(sorted(cnt.items())))
for k,v in sorted(ex.items()): print(" example df",k,v)
