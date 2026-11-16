# Inside-class label-label M2c with A, C shallow in sea row r0, for slope s = Delta/e (s = 4: stride (4,1); s = 8: stride (8,1)).
# B = (0, yB), D = (s e, yB + 2e), e = 0 mod 2^k. Shallow = column != 0 mod 4. Equations of block_sea Theorem 2 (M2c),
# each hit re-checked from the definition of a mixed quadruple (equal side/diagonal lengths, perpendicular midpoint offset).
import sys
from sympy import divisors
s = int(sys.argv[1]); k = int(sys.argv[2]); H = int(sys.argv[3]); r0 = 1
def m2c(yB, e):
    Dl = s * e; u2 = yB - r0; hits = []
    N = abs(e * u2)
    if N == 0: return hits
    for d in divisors(N):
        for n1 in (d, -d):
            if n1 * ((Dl - n1) ** 2 + e * e) != e * u2 * (Dl - 2 * n1): continue
            z = -e * u2 // n1
            xA = -z; xC = 2 * n1 - z - Dl
            if xA % 4 == 0 or xC % 4 == 0: continue
            A = (xA, r0); B = (0, yB); C = (xC, r0); D = (Dl, yB + 2 * e)
            U = (B[0] - A[0], B[1] - A[1]); V = (D[0] - C[0], D[1] - C[1])
            S = (C[0] + D[0] - A[0] - B[0], C[1] + D[1] - A[1] - B[1])
            if S[0] % 2 or S[1] % 2: continue
            n = (S[0] // 2, S[1] // 2)
            if U[0]**2 + U[1]**2 == V[0]**2 + V[1]**2 and n[0]*U[0] + n[1]*U[1] == 0 and n != (0, 0) and V != U and V != (-U[0], -U[1]):
                hits.append((A, B, C, D))
    return hits
res = {}
for par in ('odd', 'even'):
    cnt = 0; ex = None
    for yB in range(2, H):
        if (yB % 2 == 1) != (par == "odd"): continue
        if (yB - r0) % 4 == 0: continue  # Theorem A: c = v2(yB - r0) in {0, 1}
        for e in range(2 ** k, (H - yB) // 2 + 1, 2 ** k):
            hh = m2c(yB, e)
            if hh:
                cnt += len(hh); ex = ex or hh[0]
    res[par] = (cnt, ex)
print('slope', s, 'k', k, 'H', H, res)
