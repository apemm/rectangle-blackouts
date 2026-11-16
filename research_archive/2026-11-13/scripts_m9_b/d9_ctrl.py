"""D9 control: only low labels (2i+1 <= 205, i >= 4) at offset-0 slots; count
Pb triples (shallow vertex E, label point L, filler F, W in grid) and check
V2-6: L odd, F a base (odd offset), y_L <= 205.  Also the wrong-offset
variant (labels at offset 2) to see that the offset matters."""
import random, math
h, u = 1001, 3
def run(iota, sigma, kt, seed, shift):
    rnd = random.Random(seed)
    yP = 2*iota+1; r0 = 1 if iota % 2 else 3
    add = 32 if (2*sigma+1) % 4 == 3 else 48
    Ts = max(y for y in range(1, h+1) if (y-yP-add) % 64 == 0)
    rho_tau = (u*(iota+sigma)-kt) % 16; rho0 = rho_tau % 4
    labels = {}
    for n in range(1200):
        if (n - rho_tau - shift) % 16 == 0:
            i = iota + 32*rnd.randrange(0, 4)
            if i < 4: i += 32
            s = sigma + 16*rnd.randrange(-(h//32), h//32)
            j = i + s
            if 2 <= j <= h//2-1 and 2*i+1 <= 205:
                labels[n] = (2*i+1, 2*j+2)
    fillers = {n: Ts-24+8*((n-rho0) % 4) for n in range(1200) if n not in labels}
    hits = []
    for nL, ys in labels.items():
        for yL in ys:
            L = (4*nL, yL)
            for nF, yF in fillers.items():
                F = (4*nF, yF)
                c = (L[1]-r0)*(F[1]-r0); B_ = -(L[0]+F[0]); C_ = L[0]*F[0]+c
                disc = B_*B_-4*C_
                if disc < 0: continue
                r = math.isqrt(disc)
                if r*r != disc: continue
                for num in {-B_+r, -B_-r}:
                    if num % 2: continue
                    xE = num//2
                    if xE % 4 == 0: continue
                    if 1 <= L[1]+F[1]-r0 <= h:
                        hits.append((yL, (nF-rho0) % 4))
    bad = [x for x in hits if x[0] % 2 == 0 or x[0] > 205 or x[1] % 2 == 0]
    return r0, len(labels), len(hits), len(bad)
for args in [(2,5,3,1),(7,3,1,2),(1,1,6,4),(4,10,0,3)]:
    for shift in (0, 2):
        print(args, "shift", shift, "r0,labels,Pb hits,violating V2-6:", run(*args, shift))
