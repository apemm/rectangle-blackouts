# Sanity check of the mod-64 row lemma for three labels + one free point F.
# Model: one region; slots i = iota (mod 32); M_c = M0 (mod 16); T_c = T0 (mod 32).
# For every triple of label points, solve exactly for every integer F making
# {F, three labels} a mixed quadruple (Lemma mixedeq), with F in a deep column
# (x = 0 mod 4) and an odd row. Record (y_F - y_P) mod 64 by role pattern.
import random, math, sys
from collections import Counter, defaultdict

def isqrt_exact(n):
    if n < 0: return None
    r = math.isqrt(n)
    return r if r*r == n else None

def run(seed, iota, M0, T0, nclass, kmax, qrange, rrange):
    random.seed(seed)
    classes = []
    for c in range(nclass):
        T = T0 + 32*random.randint(-rrange, rrange)
        M = M0 + 16*random.randint(-qrange, qrange)
        classes.append((c, T, M))
    pts = []  # (x, y, parity 'o'/'e', class, T, i)
    for (c, T, M) in classes:
        for k in range(kmax):
            i = iota + 32*k
            pts.append((4*(i+M), 2*i+1, 'o', c, T, i))
            pts.append((4*(i+M), 2*i+1+T, 'e', c, T, i))
    yP = (2*iota+1) % 64
    res = defaultdict(Counter)
    nsol = 0
    N = len(pts)
    for b in range(N):
        B = pts[b]
        for c_ in range(N):
            for d in range(c_+1, N):
                if b in (c_, d): continue
                C = pts[c_]; D = pts[d]
                # F on the side: A = F, side {F,B}, diagonal {C,D}
                Wx = C[0]+D[0]-2*B[0]; Wy = C[1]+D[1]-2*B[1]
                R = (D[0]-C[0])**2 + (D[1]-C[1])**2
                W2 = Wx*Wx+Wy*Wy
                if W2 == 0 or R == 0: continue
                s = isqrt_exact(R*(W2-R))
                if s is None: continue
                for sg in (1, -1):
                    nx = -R*Wx + sg*s*(-Wy); ny = -R*Wy + sg*s*Wx
                    if nx % W2 or ny % W2: continue
                    ux, uy = nx//W2, ny//W2
                    Fx, Fy = B[0]-ux, B[1]-uy
                    if Fx % 4 or Fy % 2 == 0: continue
                    if ux == 0: continue  # vertical side excluded
                    # n = (C+D-A-B)/2 must be integral and nonzero
                    tx = C[0]+D[0]-Fx-B[0]; ty = C[1]+D[1]-Fy-B[1]
                    if tx % 2 or ty % 2 or (tx == 0 and ty == 0): continue
                    vx, vy = D[0]-C[0], D[1]-C[1]
                    if (vx, vy) in ((ux, uy), (-ux, -uy)): continue
                    assert (tx//2)*ux + (ty//2)*uy == 0 and ux*ux+uy*uy == vx*vx+vy*vy
                    pat = 'side:B=%s,diag=%s%s' % (B[2], ''.join(sorted(C[2]+D[2])), '' )
                    same = 'allsame' if B[3] == C[3] == D[3] else 'mixedcls'
                    key = pat + ',' + same
                    extra = ''
                    if B[2] == 'e':
                        Dv = C if C[2] == 'e' else D
                        extra = ',dT64=%d' % ((B[4]-Dv[4]) % 64)
                    res[key+extra][(Fy - yP) % 64] += 1
                    nsol += 1
    # F on the diagonal: D = F, side {A,B}, other diagonal end C
    for a in range(N):
        for b in range(a+1, N):
            A = pts[a]; B = pts[b]
            ux, uy = B[0]-A[0], B[1]-A[1]
            if ux == 0: continue
            g = math.gcd(ux, uy); ex, ey = -uy//g, ux//g
            U2 = ux*ux+uy*uy; e2 = ex*ex+ey*ey
            for c_ in range(N):
                if c_ in (a, b): continue
                C = pts[c_]
                W1x = A[0]+B[0]-2*C[0]; W1y = A[1]+B[1]-2*C[1]
                we = W1x*ex + W1y*ey; w2 = W1x*W1x+W1y*W1y
                disc = we*we - e2*(w2-U2)
                sq = isqrt_exact(disc)
                if sq is None: continue
                for sg in (1, -1):
                    num = -we + sg*sq
                    if num % (2*e2): continue
                    t = num//(2*e2)
                    if t == 0: continue
                    nxx, nyy = t*ex, t*ey
                    Fx = A[0]+B[0]-C[0]+2*nxx; Fy = A[1]+B[1]-C[1]+2*nyy
                    if Fx % 4 or Fy % 2 == 0: continue
                    vx, vy = Fx-C[0], Fy-C[1]
                    if (vx, vy) in ((ux, uy), (-ux, -uy)): continue
                    assert vx*vx+vy*vy == U2 and nxx*ux+nyy*uy == 0
                    same = 'allsame' if A[3] == B[3] == C[3] else ('sideSameCls' if A[3] == B[3] else 'sideCross')
                    key = 'diag:C=%s,side=%s,%s' % (C[2], ''.join(sorted(A[2]+B[2])), same)
                    if C[2] == 'e':
                        Ev = A if A[2] == 'e' else B
                        key += ',dT64=%d' % ((Ev[4]-C[4]) % 64)
                    res[key][(Fy - yP) % 64] += 1
                    nsol += 1
    return res, nsol

if __name__ == '__main__':
    tot = defaultdict(Counter)
    ns = 0
    for seed, iota, M0, T0 in [(1, 5, 3, 7), (2, 6, 11, 33), (3, 1, 0, 3), (4, 10, 7, 21)]:
        r, n = run(seed, iota, M0, T0, nclass=3, kmax=5, qrange=3, rrange=2)
        ns += n
        for k, v in r.items(): tot[k].update(v)
    print('solutions', ns)
    for k in sorted(tot):
        print(k, dict(sorted(tot[k].items())))
