# Sanity check of the stride-4u constants and the twisted placement.
# Sanity only: the proofs are analytic.
import random
from fractions import Fraction as Fr

def is_prime(n):
    if n < 2: return False
    for q in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % q == 0: return n == q
    d, s = n-1, 0
    while d % 2 == 0: d//=2; s+=1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x = pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(s-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True

def jacobi(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3,5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0

print("== constants ==")
for u in [1,3,5,7,9,13,21,99,399]:
    D = 4*u*u+1; P = max(40, 8*u*u+4)
    gap = 4*(P - Fr(u,2))
    rig = 1 + Fr(D, 8*u*(P-u) - D)
    lad = 1 + Fr(u, 2*P - 3*u)
    p1c = 1 + Fr(D, 4*u*(2*P-3*u) - 1)
    i2 = 8*u*(2*P-u)
    f2 = 4*(P-u)
    h_prop4 = (420**2)//(4*gap) + 1   # least h with 4*gap*h > 420^2
    j4 = 64*Fr(104,100)*P
    print(u, D, P, "gap", float(gap), "margins", round(float(rig),5), round(float(lad),5), round(float(p1c),5),
          "I2 1/", i2, "F2 1/", f2, "h_prop4", h_prop4, "J4", float(j4), ">2600", j4 > 2600,
          "all<1.04", max(rig,lad,p1c) < Fr(104,100))

def setup(h, u, seed):
    rnd = random.Random(seed)
    D = 4*u*u+1; P = max(40, 8*u*u+4)
    L = [l for l in range(int(1.04*h)+1, int(2.08*h)+1) if is_prime(l) and jacobi(D,l) == -1]
    Ps = []
    x = P*h+1
    while len(Ps) < 5 and x <= 2*P*h:
        if x % 4 == 3 and is_prime(x) and jacobi(D,x) == -1: Ps.append(x)
        x += 2 if x % 2 else 1
    return rnd, D, P, rnd.choice(L), rnd.choice(Ps)

fails = 0
for (h,u,seed) in [(1001,3,1),(1201,5,2),(1500,7,3),(2003,13,4),(1601,13,5)]:
    rnd, D, P, l, p = setup(h,u,seed)
    A, K = (h+1)//2, h//2
    iota, sigma = rnd.randrange(32), rnd.randrange(16)
    kappa, b = rnd.randrange(10**6), rnd.randrange(10**6)
    B = 6
    pinv = pow(p, -1, 16*l)
    labels = []
    for i in range(iota, A, 32):
        for j in range(K):
            s = j - i
            if (s - sigma) % 16: continue
            k = rnd.randrange(B)
            rho = pinv*(u*s - kappa) % (16*l)
            t = rho + 16*l*k
            n = u*i + p*t + b
            labels.append((i,j,s,t,n))
    rho_tau = (u*(iota+sigma) - kappa + b) % 16
    for (i,j,s,t,n) in labels:
        if n % 16 != rho_tau: fails += 1
        if (n - u*j + kappa - b) % (16*l): fails += 1
    slots = [x[4] for x in labels]
    if len(set(slots)) != len(slots): fails += 1
    odd = lambda L: (4*L[4], 2*L[0]+1)
    even = lambda L: (4*L[4], 2*L[1]+2)
    x0 = (4*labels[0][4]) % 64
    for L in labels:
        if (4*L[4]) % 64 != x0: fails += 1
    gapmin = None
    for _ in range(20000):
        L1, L2 = rnd.choice(labels), rnd.choice(labels)
        o1, o2, e1, e2 = odd(L1), odd(L2), even(L1), even(L2)
        if (o2[0]-o1[0]) % 64 or (o2[1]-o1[1]) % 64: fails += 1
        if (e2[0]-e1[0]) % 64 or (e2[1]-e1[1]) % 32: fails += 1
        Ds, Dt, Di, Dj = L2[2]-L1[2], L2[3]-L1[3], L2[0]-L1[0], L2[1]-L1[1]
        DM = p*Dt; N = u*Ds - DM
        if N % (16*l): fails += 1
        if (Dt == 0) != (N == 0): fails += 1
        if Fr(o2[0]-o1[0],4) - Fr(u*(o2[1]-o1[1]),2) != DM: fails += 1
        if Fr(e2[0]-e1[0],4) - Fr(u*(e2[1]-e1[1]),2) != -N: fails += 1
        if Dt != 0:
            g = abs(o2[0]-o1[0])
            gapmin = g if gapmin is None else min(gapmin, g)
            if g <= 4*(P - Fr(u,2))*h + 2*u - 1: fails += 1
        # rigid right-angle identity: V even of L1, P odd of slot i0+t1 same class (synthetic), Q even of L2
        t1 = rnd.choice([-64,-32,32,64]); T0 = 2*L1[2]+1
        V = e1; Pp = (4*(L1[4]+u*t1), 2*(L1[0]+t1)+1); Q = e2
        c2 = Dj
        lhs = (Pp[0]-V[0])*(Q[0]-V[0]) + (Pp[1]-V[1])*(Q[1]-V[1])
        if lhs != 2*(c2*(2*D*t1 - T0) - 8*u*t1*N): fails += 1
        # B1 type II(-1,-1): A,B even (L1,L2), C,D odd of slots iA+d, iB+d' in the same classes (synthetic)
        d, dd = 32*rnd.randrange(-3,4), 32*rnd.randrange(-3,4)
        Aq, Bq = e1, e2
        Cq = (4*(L1[4]+u*d), 2*(L1[0]+d)+1); Dq = (4*(L2[4]+u*dd), 2*(L2[0]+dd)+1)
        U = (Bq[0]-Aq[0], Bq[1]-Aq[1]); n2v = (Cq[0]+Dq[0]-Aq[0]-Bq[0], Cq[1]+Dq[1]-Aq[1]-Bq[1])
        Sig = d+dd; S = L1[2]+L2[2]+1
        if U[0]*n2v[0]+U[1]*n2v[1] != 4*(Dj*(D*Sig - S) - 4*u*Sig*N): fails += 1
        # I.2: A odd slot i0 c0, B even slot i0+a c0, C odd slot iC c', D even slot iC+bb c'
        a, bb = 32*rnd.choice([-2,-1,1,2]), 32*rnd.choice([-2,-1,1,2])
        T0, Tp = 2*L1[2]+1, 2*L2[2]+1
        Aq = odd(L1); Bq = (4*(L1[4]+u*a), 2*(L1[0]+a+L1[2])+2)
        Cq = odd(L2); Dq = (4*(L2[4]+u*bb), 2*(L2[0]+bb+L2[2])+2)
        U = (Bq[0]-Aq[0], Bq[1]-Aq[1]); n2v = (Cq[0]+Dq[0]-Aq[0]-Bq[0], Cq[1]+Dq[1]-Aq[1]-Bq[1])
        m = (L2[0]) + (L2[0]+bb) - L1[0] - (L1[0]+a); n2 = m + Ds
        Ustar = 2*D*a + T0
        if U[0]*n2v[0]+U[1]*n2v[1] != 2*(n2*Ustar - 8*u*a*(2*N - u*Ds)): fails += 1
    print("h,u,l,p", h, u, l, p, "labels", len(labels), "min cross gap/h", round(gapmin/h,2) if gapmin else None)
print("failures:", fails)
