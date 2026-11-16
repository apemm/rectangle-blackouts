# Brute force: in-class homogeneous Fo/Fo quadruples {L1,F1 side; L2,F2 diagonal}
# directly from the mixed-pair equations (no parametrization).
# Stride (mu,1): L1=(0,0), L2=(mu t, 2t), t = 0 mod 32, t<0.
# Fillers F1=(4A, Y1), F2=(mu t + 4A2, Y1) in one row; slot offsets mod 4 equal:
#   F1 offset A mod 4 ; F2 slot = (mu/4) t + A2, offset ((mu/4)t + A2) mod 4 == A mod 4.
# Row rule (SAW*-type): depth Y1 = 8(w+c) mod 64, w = A mod 4, c in {1,3}.
# Conditions (Lemma mixedeq): S = L2+F2-L1-F1 even, n = S/2, n.(F1-L1)=0, |F2-L2|=|F1-L1|.
import sys
from math import gcd
from fractions import Fraction
from collections import Counter

def v2(x):
    if x == 0: return 99
    k = 0
    while x % 2 == 0: x //= 2; k += 1
    return k

def run(mu, TMAX, AMAX):
    out = Counter(); ex = []
    for t in range(-32, -TMAX-1, -32):
        Dx, Dy = mu*t, 2*t
        for A in range(-AMAX, AMAX+1):
            w = A % 4
            # unknowns: Y1 (>0), A2. From n.U=0 and |V|=|U| solve exactly:
            # U=(4A,Y1), V=(Dx+4A2-Dx, Y1-Dy) = (4A2, Y1-Dy) relative to L2.
            # S = 2(Dx,Dy) + V - U ; condition S.U = 0 and |V|^2=|U|^2.
            # |V|=|U|: 16A2^2 + (Y1-Dy)^2 = 16A^2 + Y1^2 -> 16(A2^2-A^2) = 2DyY1 - Dy^2
            # S.U = (2Dx + 4A2 - 4A)*4A + (2Dy - Dy)*Y1 = 0 -> Y1 = -(2Dx+4A2-4A)*4A/Dy
            for A2 in range(-AMAX, AMAX+1):
                if ((mu//4)*t + A2 - A) % 4: continue
                num = -(2*Dx + 4*A2 - 4*A)*4*A
                if num % Dy: continue
                Y1 = num // Dy
                if Y1 <= 0: continue
                if 16*(A2*A2 - A*A) != 2*Dy*Y1 - Dy*Dy: continue
                if (Y1 % 64) not in (8*(w+1) % 64, 8*(w+3) % 64): continue
                Sx = 2*Dx + 4*A2 - 4*A; Sy = Dy
                if Sx % 2 or Sy % 2: continue
                if (4*A2, Y1-Dy) == (4*A, Y1) or (4*A2, Y1-Dy) == (-4*A, -Y1): continue
                P = 4*A - 4*A2
                m = Fraction(P, Dy)  # P = 2 nu t m with nu=1 -> m = P/(2t)
                a, b = m.numerator, m.denominator
                key = (w, a % 2, min(v2(b), 9), min(v2(a), 9), v2(A) - v2(b), v2(t))
                out[key] += 1
                if len(ex) < 6: ex.append((t, A, A2, Y1, a, b))
    return out, ex

for mu in (4, 8):
    out, ex = run(mu, int(sys.argv[1]), int(sys.argv[2]))
    print("stride", mu, "solutions", sum(out.values()))
    for k, v in sorted(out.items()):
        print("  (w, a mod 2, v2 b, v2 a, v2A - v2b, v2 t) =", k, v)
    print("  examples (t,A,A2,Y1,a,b):", ex)
