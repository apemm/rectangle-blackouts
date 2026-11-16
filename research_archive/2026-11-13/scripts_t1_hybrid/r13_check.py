# Check of Proposition D': with label columns = 0 mod 16, label rows fixed mod 16 per parity,
# F-L = 8 mod 16, H-L = eps-o+4 mod 8, no two-label mixed support of type R1 (side = two
# label points, diagonal = two sea points) or R3 (side = two sea points, diagonal = two label
# points) exists unless the sea pair is horizontal. Label columns random (no rigid rule).
import math, random
random.seed(5)
h = 400; o, eps = 1, 0
L, F = 3, 3 + 8 * 3 + 0           # F-L = 24 = 8 mod 16, both = o+2 mod 4
H = None
for cand in range(h - 1, h - 60, -1):
    if cand % 2 == 0 and (cand - L) % 8 == (eps - o + 4) % 8: H = cand; break
seas = [L, F, H]
labs = [(i, j) for i in range(h // 2) for j in range(h // 2)
        if (2*i+1) % 16 == o and (2*j+2) % 16 == eps and 40 <= 2*i+1 <= H-10 and 40 <= 2*j+2 <= H-10]
cols = random.sample(range(0, 40 * h * h // 16), len(labs))
pts = []
for k, (i, j) in enumerate(labs):
    x = 16 * cols[k]; pts.append((x, 2*i+1, k)); pts.append((x, 2*j+2, k))
lab = {q[0] for q in pts}
hits = {"R1": 0, "R3": 0, "R1h": 0, "R3h": 0}; pairs = 0
for a in range(len(pts)):
    for b in range(a + 1, len(pts)):
        P1, P2 = pts[a], pts[b]
        if P1[2] == P2[2]: continue
        X, Dy = P2[0] - P1[0], P2[1] - P1[1]
        if abs(X) > h * h: continue
        pairs += 1
        for s1 in seas:
            for s2 in seas:
                ds = s2 - s1
                if (P1[1] + P2[1] - s1 - s2) % 2: continue
                N0 = X * X + Dy * Dy - ds * ds
                if N0 <= 0: continue
                xi = math.isqrt(N0)
                if xi * xi != N0: continue
                for xs in (xi, -xi):
                    # R3: side S1S2=(xs,ds), diagonal P1P2; perp: xs*(x1+x2-c1-c2)+ds*(y1+y2-s1-s2)=0
                    num = ds * (P1[1] + P2[1] - s1 - s2)
                    if num % xs == 0:
                        csum = P1[0] + P2[0] + num // xs
                        if (csum - xs) % 2 == 0:
                            c1 = (csum - xs) // 2; c2 = c1 + xs
                            if c1 not in lab and c2 not in lab and (xs, ds) not in {(X, Dy), (-X, -Dy)}:
                                hits["R3h" if ds == 0 else "R3"] += 1
                    # R1: side P1P2, diagonal S1S2=(xs,ds); perp: X*(c1+c2-x1-x2)+Dy*(s1+s2-y1-y2)=0
                    num = -Dy * (s1 + s2 - P1[1] - P2[1])
                    if X != 0 and num % X == 0:
                        csum = P1[0] + P2[0] + num // X
                        if (csum - xs) % 2 == 0:
                            c1 = (csum - xs) // 2; c2 = c1 + xs
                            if c1 not in lab and c2 not in lab and (xs, ds) not in {(X, Dy), (-X, -Dy)}:
                                hits["R1h" if ds == 0 else "R1"] += 1
print("labels", len(labs), "label-point pairs in range", pairs, "H", H, "hits", hits)
