# Targeted search: {F,o,e,e} with F paired to an even label (cases (c) and (beta2')).
import math, random
from collections import Counter, defaultdict
def sq(n):
    if n < 0: return None
    r = math.isqrt(n); return r if r*r == n else None
res = defaultdict(Counter); ex = {}
for seed in range(3):
    random.seed(100+seed)
    iota = random.randrange(32); M0 = random.randrange(16); T0 = 2*random.randrange(16)+1
    cls = [(c, T0+32*random.randint(-4,4), M0+16*random.randint(-3,3)) for c in range(18)]
    O = []; E = []
    for (c,T,M) in cls:
        for k in range(6):
            i = iota+32*k
            O.append((4*(i+M), 2*i+1, c, T)); E.append((4*(i+M), 2*i+1+T, c, T))
    yP = (2*iota+1) % 64; rho0 = (iota+M0) % 4
    # (beta2'): side {A=o, B=e}, diagonal {C=e', D=F}
    for A in O:
        for B in E:
            ux, uy = B[0]-A[0], B[1]-A[1]
            if ux == 0: continue
            g = math.gcd(ux, uy); exx, eyy = -uy//g, ux//g; e2 = exx*exx+eyy*eyy; U2 = ux*ux+uy*uy
            for C in E:
                if C is B: continue
                W1x = A[0]+B[0]-2*C[0]; W1y = A[1]+B[1]-2*C[1]
                we = W1x*exx+W1y*eyy; w2 = W1x*W1x+W1y*W1y
                s = sq(we*we - e2*(w2-U2))
                if s is None: continue
                for sg in (1,-1):
                    num = -we+sg*s
                    if num % (2*e2): continue
                    t = num//(2*e2)
                    if t == 0: continue
                    Fx = A[0]+B[0]-C[0]+2*t*exx; Fy = A[1]+B[1]-C[1]+2*t*eyy
                    if Fx % 4 or Fy % 2 == 0: continue
                    if (Fx-C[0], Fy-C[1]) in ((ux,uy),(-ux,-uy)): continue
                    r = (Fy-yP) % 64; off = (Fx//4 - rho0) % 4
                    key = ('beta2', (B[3]-C[3]) % 64, 'T%d' % (T0 % 4))
                    res[key][(r, off)] += 1
                    if r == 32: ex[key] = (A, B, C, (Fx, Fy))
    # (c): side {A=F, B=e}, diagonal {C=o, D=e'}
    for B in E:
        for C in O:
            for D in E:
                if D is B: continue
                Wx = C[0]+D[0]-2*B[0]; Wy = C[1]+D[1]-2*B[1]
                R = (D[0]-C[0])**2+(D[1]-C[1])**2; W2 = Wx*Wx+Wy*Wy
                if W2 == 0: continue
                s = sq(R*(W2-R))
                if s is None: continue
                for sg in (1,-1):
                    nx = -R*Wx+sg*s*(-Wy); ny = -R*Wy+sg*s*Wx
                    if nx % W2 or ny % W2: continue
                    ux, uy = nx//W2, ny//W2
                    if ux == 0: continue
                    Fx, Fy = B[0]-ux, B[1]-uy
                    if Fx % 4 or Fy % 2 == 0: continue
                    tx = C[0]+D[0]-Fx-B[0]; ty = C[1]+D[1]-Fy-B[1]
                    if tx % 2 or ty % 2 or (tx == 0 and ty == 0): continue
                    if (D[0]-C[0], D[1]-C[1]) in ((ux,uy),(-ux,-uy)): continue
                    r = (Fy-yP) % 64; off = (Fx//4 - rho0) % 4
                    key = ('c', (B[3]-D[3]) % 64, 'T%d' % (T0 % 4))
                    res[key][(r, off)] += 1
                    if r == 32: ex[key] = (B, C, D, (Fx, Fy))
for k in sorted(res): print(k, dict(res[k]))
for k in ex: print('example', k, ex[k])
