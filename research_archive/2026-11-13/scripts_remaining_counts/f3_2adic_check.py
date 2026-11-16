# Direct check of side {L1,F1}, diagonal {L2,F2} (Lemma mixedeq) for odd label points
# L = (4n, y), within one class line L2-L1=(4t,2t) [mode 'class'] or cross-block L2-L1=(Dx,Dy) [mode 'cross'].
# Congruences ON: y_L = r (mod 64), label columns n = n0 (mod 4), fillers at columns n0+o (mod 4) with row
# f_o = Ts-24+8o, Ts = y_L + 32 (mod 64) (T=3 mod 4 type) or y_L+48 (T=1 type).  OFF: drop them (control).
import sys, itertools
mode = sys.argv[1]; cong = int(sys.argv[2]); h = int(sys.argv[3]); typ = int(sys.argv[4]) if len(sys.argv)>4 else 3
r = 1
Ts = max(y for y in range(h-70, h+1) if (y - r - (32 if typ==3 else 48)) % 64 == 0)
frow = [Ts-24+8*o for o in range(4)]
found = {}
def check(yL1, Dx, Dy, o1, o2, X1):
    f1, f2 = frow[o1], frow[o2]
    Y1 = f1 - yL1
    df = f1 - f2
    if (Dy - df) % 2: return 0
    ny = (Dy - df)//2
    if X1 == 0 or (ny*Y1) % X1: return 0
    nx = -(ny*Y1)//X1
    if nx == 0 and ny == 0: return 0
    Zx, Zy = Dx - nx, Dy - ny
    Wx, Wy = X1 - Zx, Y1 - Zy
    if Zx*Wx + Zy*Wy != 0: return 0
    # p = L1+n, q = F1+n rows in grid; L2 row in grid
    if not (1 <= yL1+ny <= h and 1 <= f1+ny <= h and 1 <= yL1+Dy <= h): return 0
    return 1
cnt = {}
ys = [y for y in range(1, Ts-128) if (not cong) or (y - r) % 64 == 0]
for yL1 in ys:
    for o1 in range(4):
        for o2 in range(4):
            if mode == 'class':
                ts = [t for t in range(-(h//2), h//2+1) if t != 0 and ((not cong) or t % 32 == 0)]
                pairs = [(4*t, 2*t) for t in ts]
            for (Dx, Dy) in pairs:
                if not (1 <= yL1 + Dy < Ts-128): continue
                # X1 range: |X1| <= 4h (local), congruence X1 = 4 o1 mod 16
                for X1 in range(-8*h, 8*h+1, 4):
                    if cong and (X1 - 4*o1) % 16: continue
                    if check(yL1, Dx, Dy, o1, o2, X1):
                        key = (frow[o1]-frow[o2])
                        cnt[key] = cnt.get(key, 0) + 1
print("mode", mode, "cong", cong, "h", h, "type", typ, "counts by df:", dict(sorted(cnt.items())))
