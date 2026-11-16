"""Q3 sanity check: three label points + one filler mixed quadruples in a synthetic
L*** region. For every label triple and every role assignment, solve Lemma mixedeq
exactly for the fourth point F, then test F against the SAW*-shift filler rule.
Controls: (1) filler rule with c even; (2) any deep odd-row point accepted.
Usage: py -I q3_solver.py h iota sigma kappa ndiag nclass seed
"""
import sys, random, math
from itertools import combinations
from math import gcd, isqrt

def is_prime(n):
    if n < 2: return False
    for q in range(2, isqrt(n) + 1):
        if n % q == 0: return False
    return True

def setup(h, iota, sigma, kappa, ndiag, nclass, seed):
    rnd = random.Random(seed)
    l = next(x for x in range(int(1.04*h)+1, int(2.08*h)+1) if is_prime(x) and x % 5 in (2, 3))
    p = next(x for x in range(40*h+1, 80*h+1) if is_prime(x) and x % 20 in (3, 7))
    M16l = 16*l
    pinv = pow(p, -1, M16l)
    b = 7
    K = h // 2
    # diagonals s = sigma (mod 16), |s| < K
    svals = [s for s in range(-K+1, K) if (s - sigma) % 16 == 0]
    rnd.shuffle(svals)
    svals = svals[:ndiag]
    T0 = (2*sigma+1) % 32
    labels = []  # (nu, yo, ye, class id)
    cid = 0
    for s in svals:
        rho_s = (pinv*(s - kappa)) % M16l
        for k in range(nclass):
            t = rho_s + M16l*k
            M = p*t + b
            for i in range(0, h):
                if i % 32 != iota % 32: continue
                yo, ye = 2*i+1, 2*(i+s)+2
                if yo > h or ye < 2 or ye > h: continue
                if rnd.random() < 0.7:
                    labels.append((i + M, yo, ye, cid))
            cid += 1
    rho0 = (iota + sigma - kappa + b) % 4
    yP = (2*iota+1) % 64
    Tmod4 = T0 % 4
    add = 32 if Tmod4 == 3 else 48
    T0star = max(y for y in range(1, h+1) if (y - yP - add) % 64 == 0)
    return labels, rho0, yP, T0star, p, l

def main():
    h, iota, sigma, kappa, ndiag, nclass, seed = map(int, sys.argv[1:8])
    labels, rho0, yP, Tst, p, l = setup(h, iota, sigma, kappa, ndiag, nclass, seed)
    labcols = set(L[0] for L in labels)
    pts = []
    for (nu, yo, ye, c) in labels:
        pts.append(((4*nu, yo), 'o', c))
        pts.append(((4*nu, ye), 'e', c))
    def filler_ok(F, shift):
        x, y = F
        if x % 4: return False
        nu = x // 4
        if nu in labcols: return False
        return y == Tst - 24 + shift + 8*((nu - rho0) % 4)
    def deep_odd(F):
        x, y = F
        return x % 4 == 0 and y % 2 == 1 and (x//4) not in labcols
    def check(A, B, C, D):
        sx, sy = C[0]+D[0]-A[0]-B[0], C[1]+D[1]-A[1]-B[1]
        if sx % 2 or sy % 2: return False
        n = (sx//2, sy//2)
        if n == (0, 0): return False
        U = (B[0]-A[0], B[1]-A[1]); V = (D[0]-C[0], D[1]-C[1])
        if n[0]*U[0]+n[1]*U[1] != 0: return False
        if V[0]**2+V[1]**2 != U[0]**2+U[1]**2: return False
        if V == U or V == (-U[0], -U[1]): return False
        for P in (A, B, C, D, (A[0]+n[0], A[1]+n[1]), (B[0]+n[0], B[1]+n[1])):
            if not (1 <= P[1] <= h): return False
        return True
    found = {'rule': 0, 'ceven': 0, 'anydeep': 0}
    comps = {}
    sols = 0
    for tri in combinations(pts, 3):
        P = [t[0] for t in tri]
        for r in range(3):
            # F on diagonal with label P3=P[r]; side = other two
            P3 = P[r]; P1, P2 = [P[k] for k in range(3) if k != r]
            U = (P2[0]-P1[0], P2[1]-P1[1])
            g = gcd(U[0], U[1])
            if g == 0: continue
            u0 = (-U[1]//g, U[0]//g)
            W = (P1[0]+P2[0]-2*P3[0], P1[1]+P2[1]-2*P3[1])
            a2 = 4*(u0[0]**2+u0[1]**2); a1 = 4*(W[0]*u0[0]+W[1]*u0[1])
            a0 = W[0]**2+W[1]**2-U[0]**2-U[1]**2
            disc = a1*a1-4*a2*a0
            cands = []
            if disc >= 0:
                sq = isqrt(disc)
                if sq*sq == disc:
                    for sg in (1, -1):
                        num = -a1+sg*sq
                        if num % (2*a2) == 0:
                            t = num//(2*a2)
                            if t != 0: cands.append(t)
            for t in set(cands):
                n = (t*u0[0], t*u0[1])
                F = (P1[0]+P2[0]+2*n[0]-P3[0], P1[1]+P2[1]+2*n[1]-P3[1])
                if not check(P1, P2, P3, F): continue
                sols += 1
                if deep_odd(F): found['anydeep'] += 1
                if filler_ok(F, 0): found['rule'] += 1; comps.setdefault('diag', []).append((tri, F))
                if filler_ok(F, 8) or filler_ok(F, -8): found['ceven'] += 1
            # F on side with label P1=P[r]; diag = other two
            P1 = P[r]; P2, P3 = [P[k] for k in range(3) if k != r]
            W = (P2[0]+P3[0]-2*P1[0], P2[1]+P3[1]-2*P1[1])
            R2 = (P3[0]-P2[0])**2+(P3[1]-P2[1])**2
            WW = W[0]**2+W[1]**2
            if WW == 0: continue
            k2 = WW-R2
            if k2 % 2: continue
            al = k2//2
            num = k2*WW
            if num % 4: continue
            b2 = num//4-al*al
            if b2 < 0: continue
            be = isqrt(b2)
            if be*be != b2: continue
            for sg in ((1, -1) if be else (1,)):
                bb = sg*be
                nx = al*W[0]-bb*W[1]; ny = al*W[1]+bb*W[0]
                if nx % WW or ny % WW: continue
                n = (nx//WW, ny//WW)
                F = (P2[0]+P3[0]-P1[0]-2*n[0], P2[1]+P3[1]-P1[1]-2*n[1])
                if not check(F, P1, P2, P3): continue
                sols += 1
                if deep_odd(F): found['anydeep'] += 1
                if filler_ok(F, 0): found['rule'] += 1; comps.setdefault('side', []).append((tri, F))
                if filler_ok(F, 8) or filler_ok(F, -8): found['ceven'] += 1
    print(f"h={h} iota={iota} sigma={sigma} p={p} l={l} labels={len(labels)} points={len(pts)} T*={Tst}")
    print("geometric solutions:", sols, "| F deep odd non-label:", found['anydeep'],
          "| F on SAW* rule:", found['rule'], "| F on c-even rule (control):", found['ceven'])
    for k, v in comps.items():
        print(k, v[:3])

main()
