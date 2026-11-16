# Theorem B check: aligned sea + rigid layout. Enumerates every tilted right angle
# with one point of label e, one point of label f != e, and one sea point in a row of
# {L,F,H} at ANY non-label column (no mod-7 sea pattern is modelled), and classifies it.
import math, sys
from collections import Counter

def isprime(n):
    return n > 1 and all(n % q for q in range(2, int(n ** 0.5) + 1))

def run(h, stride, o, eps, L, F, H):
    sigma = stride // 2
    K, A = h // 2, (h + 1) // 2
    p = max(20 * h, (stride * stride // 2 + 4) * h) + 1
    while not (isprime(p) and p % 5 in (2, 3)): p += 1
    nu = 1
    while 2 ** nu < K: nu += 1
    mod = 2 ** nu
    labels = [(i, j) for i in range(A) for j in range(K)
              if (2 * i + 1) % 8 == o and (2 * j + 2) % 8 == eps
              and 9 <= 2 * i + 1 <= H - 4 and 9 <= 2 * j + 2 <= H - 4]
    # one class per diagonal s = j - i, rigid rule n(c) = s - M = 0 mod 2^nu, M = p*m
    diags = sorted({j - i for i, j in labels})
    pinv = pow(p, -1, mod)
    used = Counter(); Mpos = {}
    for s in diags:
        r = (pinv * s) % mod
        Mpos[s] = p * (r + mod * used[r]); used[r] += 1
    pts = []  # (x, y, label, class, parity)
    for lab, (i, j) in enumerate(labels):
        x = stride * (i + Mpos[j - i])
        pts.append((x, 2 * i + 1, lab, j - i, 1)); pts.append((x, 2 * j + 2, lab, j - i, 0))
    labcols = {q[0] for q in pts}
    seas = [L, F, H]
    kinds = Counter()
    for V in pts:
        for C in pts:
            if C[2] == V[2]: continue
            X, D = C[0] - V[0], C[1] - V[1]
            for s in seas:
                # label vertex V, ends C and sea S = V + (Y, s - yV)
                num = -D * (s - V[1])
                if num % X == 0:
                    Y = num // X
                    if Y != 0 and V[0] + Y not in labcols:
                        intra = V[3] == C[3]
                        key = ("Lvertex", "EE" if V[4] == 0 and C[4] == 0 else
                               "OO" if V[4] == 1 and C[4] == 1 else "mixed",
                               "H" if s == H else "low", "Yodd" if Y % 2 else "Yeven",
                               "intra" if intra else "cross")
                        kinds[key] += 1
                if V[2] < C[2]:
                    # sea vertex S=(x,s): x^2-(xV+xC)x+xV*xC+(yV-s)(yC-s)=0
                    Dd = X * X - 4 * (V[1] - s) * (C[1] - s)
                    if Dd >= 0:
                        r = math.isqrt(Dd)
                        if r * r == Dd and (V[0] + C[0] + r) % 2 == 0:
                            for x in {(V[0] + C[0] + r) // 2, (V[0] + C[0] - r) // 2}:
                                if x not in labcols:
                                    kinds[("Svertex", "same" if V[4] == C[4] else "mixed",
                                           "seaparity=" + ("same" if (s - V[1]) % 2 == 0 else "opp"))] += 1
    print(f"h={h} stride={stride} p={p} 2^nu={mod} labels={len(labels)}")
    for k, v in sorted(kinds.items()): print("  ", k, v)

if __name__ == "__main__":
  h = int(sys.argv[1]) if len(sys.argv) > 1 else 160
  run(h, 4, o=1, eps=0, L=3, F=7, H=h - 2)
  run(h, 8, o=1, eps=0, L=3, F=7, H=h - 2)
