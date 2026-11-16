"""Node-branch (beta -> 0 2-adically) homogeneous Fo/Fo shapes in SAW*.
For coprime (alpha, beta), alpha odd, v2(beta) = j-1 >= 1, 2 < alpha/beta < 4, build the primitive integer
vector w = (x1, u, x2, v, d) (kappa < 0), the scale lambda = 2 * odd, and an explicit SAW* configuration;
verify Lemma mixedeq from scratch in original coordinates. Report per level j the smallest required height
and the weight sum 1/u over shapes with v <= Vmax (the per-label expected load up to the 1/B and slot factors).
Usage: py node_branch.py Bmax Vmax"""
import sys
from math import gcd

def v2(n):
    n = abs(n); c = 0
    if n == 0: return 99
    while n % 2 == 0: n //= 2; c += 1
    return c

def shape(a, b):
    w = [b * (a*a + b*b), (a - 4*b) * (a*a + b*b), b * (-3*a*a + 8*a*b + b*b),
         a**3 - 4*a*a*b - 3*a*b*b + 4*b**3, 4*b*b*(a - 2*b)]
    g = 0
    for c in w: g = gcd(g, abs(c))
    w = [-c // g for c in w]          # kappa < 0: u, v > 0, d < 0 on 2 < m < 4
    return w, g

def check_config(w, lam, iota=1, T=3, M=0):
    """Place the shape in a SAW* region: T* = y_P + 32 (mod 64) for T = 3 (mod 4).
    Returns (ok, needed_h, info)."""
    x1, u, x2, v, d = [lam * c for c in w]
    # pick a label i1 = iota mod 32 with offset-0 filler row R = T* - 24 at depth u (Y units of 4 rows)
    # T* = 2*iota+1+32 (mod 64); take T* large: R - y_L1 = 4u.
    yL1 = 2 * iota + 1
    # find i1 ≡ iota (mod 32) and R ≡ (2 iota + 1 + 32 - 24) (mod 64) with R - (2 i1 + 1) = 4u
    # choose i1 so that y_L2 = y_L1 + 4d >= 1 and later rows fit; i1 = iota + 32 k
    need = 1 - 4 * d - (2 * iota + 1)          # need 2*(iota+32k)+1 + 4d >= 1
    k = max(0, -(-need // 64))
    i1 = iota + 32 * k
    yL1 = 2 * i1 + 1
    assert yL1 + 4 * d >= 1
    R = yL1 + 4 * u
    Tstar = R + 24
    okT = (Tstar - (2 * iota + 1) - 32) % 64 == 0
    n1 = i1 + M
    A = (4 * n1, yL1); B = (4 * (n1 + x1), R)
    C = (4 * (n1 + 2 * d), yL1 + 4 * d); D = (4 * (n1 + 2 * d + x2), R)
    S = (C[0] + D[0] - A[0] - B[0], C[1] + D[1] - A[1] - B[1])
    if S[0] % 2 or S[1] % 2: return False, None, 'n not integral'
    n = (S[0] // 2, S[1] // 2)
    BA = (B[0] - A[0], B[1] - A[1]); DC = (D[0] - C[0], D[1] - C[1])
    perp = n[0] * BA[0] + n[1] * BA[1] == 0
    eqlen = BA[0]**2 + BA[1]**2 == DC[0]**2 + DC[1]**2
    notpm = DC != BA and DC != (-BA[0], -BA[1]) and n != (0, 0)
    p = (A[0] + n[0], A[1] + n[1]); q = (B[0] + n[0], B[1] + n[1])
    rows = [A[1], B[1], C[1], D[1], p[1], q[1]]
    i2 = i1 + 2 * d
    slotF1 = x1 % 32 == 0; slotF2 = (2 * d + x2) % 32 == 0   # class-residue slots (relative to n1)
    classL2 = (2 * d) % 32 == 0
    ok = perp and eqlen and notpm and min(rows) >= 1 and okT and classL2
    return ok, max(rows) + 0, dict(perp=perp, eqlen=eqlen, notpm=notpm, okT=okT, minrow=min(rows),
                                   classslotF=(slotF1, slotF2), Tstar=Tstar, i1=i1, i2=i2, R=R)

Bmax = int(sys.argv[1]); Vmax = int(sys.argv[2])
levels = {}
for b in range(2, Bmax + 1, 2):
    for a in range(2 * b + 1, 4 * b):
        if a % 2 == 0 or gcd(a, b) != 1: continue
        w, g = shape(a, b)
        x1, u, x2, v, d = w
        j = v2(b) + 1
        # lambda = 2*odd, with lambda*u = 2 mod 8 relative condition (u = 2 mod 8 in SAW*): choose smallest
        lam = None
        for L in range(2, 66, 4):
            if (L * u) % 16 == 2: lam = L; break
        if lam is None: continue
        ok, H, info = check_config(w, lam)
        assert v2(lam * x1) == j and v2(lam * d) == 2 * j + 1, (a, b)
        rec = levels.setdefault(j, dict(n=0, wsum=0.0, best=None, fails=0))
        if not ok: rec['fails'] += 1
        if lam * v <= Vmax:
            rec['n'] += 1; rec['wsum'] += 1.0 / u
        if rec['best'] is None or H < rec['best'][0]:
            rec['best'] = (H, a, b, lam, w, info['classslotF'])
for j in sorted(levels):
    r = levels[j]
    print('level j=%d: shapes with v<=%d: %d, sum 1/u = %.3e, mixedeq/placement failures %d' % (j, Vmax, r['n'], r['wsum'], r['fails']))
    H, a, b, lam, w, cs = r['best']
    print('     smallest: alpha/beta=%d/%d lambda=%d w=%s  needs h >= %d  F slots class-residue mod 32: %s' % (a, b, lam, w, H, cs))
