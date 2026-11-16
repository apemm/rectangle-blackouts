# 2-adic dichotomy check: integral distances between label points of different classes
# in rigid layouts (stride 4 vs 8 vs 12), aligned families as in thmB_check.
import math, sys
from collections import Counter
from thmB_check import isprime
def layout(h, stride, o, eps, H, pmod5=True, legendre_kill=True):
    sigma = stride // 2; K, A = h // 2, (h + 1) // 2
    p = max(20 * h, (stride * stride // 2 + 4) * h) + 1
    q = sigma * sigma + 1
    while not (isprime(p) and (not legendre_kill or pow(q % p, (p - 1) // 2, p) == p - 1)): p += 1
    nu = 1
    while 2 ** nu < K: nu += 1
    mod = 2 ** nu
    labels = [(i, j) for i in range(A) for j in range(K)
              if (2*i+1) % 8 == o and (2*j+2) % 8 == eps and 9 <= 2*i+1 <= H-4 and 9 <= 2*j+2 <= H-4]
    pinv = pow(p, -1, mod); used = Counter(); M = {}
    for s in sorted({j - i for i, j in labels}):
        r = (pinv * s) % mod; M[s] = p * (r + mod * used[r]); used[r] += 1
    pts = []
    for lab, (i, j) in enumerate(labels):
        x = stride * (i + M[j - i])
        pts.append((x, 2*i+1, lab, j - i, 1)); pts.append((x, 2*j+2, lab, j - i, 0))
    return pts, p
if __name__ == '__main__':
    h = int(sys.argv[1])
    for stride in (4, 8, 12):
        pts, p = layout(h, stride, 1, 0, h - 2)
        cnt = Counter()
        for a in range(len(pts)):
            for b in range(a + 1, len(pts)):
                P, Q = pts[a], pts[b]
                if P[2] == Q[2] or P[4] != Q[4]: continue
                X, D = Q[0] - P[0], Q[1] - P[1]
                if D == 0 or abs(X) > h * h: continue
                n = X * X + D * D; r = math.isqrt(n)
                if r * r == n:
                    cnt[("EE" if P[4] == 0 else "OO", "intra" if P[3] == Q[3] else "cross")] += 1
        print(f"stride={stride} p={p} integral-distance same-parity pairs:", dict(cnt))
