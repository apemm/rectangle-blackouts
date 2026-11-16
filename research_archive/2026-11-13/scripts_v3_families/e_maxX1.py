import sys, math
from d_shapes import divisors_signed
def run(h):
    best = (0,None); cnt = 0
    for yP in range(3, 64, 4):
        for Tm in (1, 3):
            off = 32 if Tm == 3 else 48
            Ts = max(y for y in range(h-70, h+1) if (y-yP-off) % 64 == 0)
            labrows = [y for y in range(yP, Ts-128, 64) if y > 177]
            for o1 in range(4):
                f1 = Ts-24+8*o1
                for o2 in range(4):
                    f2 = Ts-24+8*o2
                    for l1 in labrows:
                        for l2 in labrows:
                            Dy = l2-l1; Y1 = f1-l1
                            if (Dy-(f1-f2)) % 2: continue
                            ny = (Dy-(f1-f2))//2
                            if ny == 0 or f1+ny > h or l1+ny < 1: continue
                            for nx in divisors_signed(ny*Y1):
                                X1 = -ny*Y1//nx
                                S = 2*nx+X1; c0 = nx*nx+(Dy-ny)**2-Y1*Dy
                                disc = S*S-4*c0
                                if disc < 0: continue
                                r = math.isqrt(disc)
                                if r*r != disc or (S+r) % 2: continue
                                for Dx in {(S+r)//2, (S-r)//2}:
                                    Vx = X1+2*nx-2*Dx; Vy = Y1+2*ny-2*Dy
                                    if (Vx, Vy) in ((X1, Y1), (-X1, -Y1)): continue
                                    cnt += 1
                                    if abs(X1) > best[0]: best = (abs(X1), (l1,l2,f1,f2,nx,ny,X1,Dx,Vx,Vy))
    return cnt, best[0]/h, best[1]
for h in map(int, sys.argv[1:]):
    print(h, run(h))
