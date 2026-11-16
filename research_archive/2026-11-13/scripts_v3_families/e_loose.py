"""Family (e): cross-block odd-odd mixed quadruple, side {L1,F1}, diagonal {L2,F2}.
Shape (Dy, Y1, n_x, filler offsets) -> X1 = -n_y Y1/n_x, Dx from
Dx^2 - (2n_x+X1)Dx + n_x^2 + (Dy-n_y)^2 - Y1*Dy = 0.  Every hit is re-checked
against Lemma mixedeq directly (C+D = A+B+2n, n.u = 0, |D-C| = |u|)."""
import sys, math
from sympy import primerange
from d_shapes import divisors_signed
THR=float(sys.argv[1])
def run(h, mod_s=8):
    P = set(p for p in primerange(20*h+1, 40*h+1) if p % 20 in (3, 7))
    shapes = 0; real = 0; ex = None
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
                                pass
                                S = 2*nx+X1; c0 = nx*nx+(Dy-ny)**2-Y1*Dy
                                disc = S*S-4*c0
                                if disc < 0: continue
                                r = math.isqrt(disc)
                                if r*r != disc: continue
                                for Dx in {(S+r)//2, (S-r)//2} if (S+r) % 2 == 0 else set():
                                    if abs(Dx) < THR*h or abs(Dx) > h*h: continue
                                    pass
                                    Vx = X1+2*nx-2*Dx
                                    pass
                                    Vy = Y1+2*ny-2*Dy
                                    # direct mixedeq check with L1 at origin
                                    A=(0,l1); B=(X1,f1); C=(Dx,l2); D=(Dx+Vx,l2+Vy)
                                    assert D[1] == f2
                                    assert C[0]+D[0]-A[0]-B[0] == 2*nx and C[1]+D[1]-A[1]-B[1] == 2*ny
                                    assert nx*X1+ny*Y1 == 0 and Vx*Vx+Vy*Vy == X1*X1+Y1*Y1
                                    if (Vx, Vy) in ((X1, Y1), (-X1, -Y1)): continue
                                    shapes += 1
                                    q = abs(Dx-2*Dy)//4
                                    for k in range(1, q//(20*h)+1):
                                        if q % k == 0 and q//k in P:
                                            real += 1; ex = (h, l1, l2, f1, f2, nx, ny, X1, Dx, q//k)
    return shapes, len(P), real, ex
for h in map(int, sys.argv[2:]):
    print(h, run(h))
