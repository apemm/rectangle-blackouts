# Control experiment: same aligned sea, but block positions M = p*m in random order
# (no 2-adic rule), and a second control with fully random label columns = 0 mod 4.
import random, math, sys
from collections import Counter
import thmB_check as T   # reuse isprime; run() is redefined below
random.seed(3)
def run(h, stride, o, eps, L, F, H, mode):
    K, A = h // 2, (h + 1) // 2
    p = max(20 * h, (stride * stride // 2 + 4) * h) + 1
    while not (T.isprime(p) and p % 5 in (2, 3)): p += 1
    labels = [(i, j) for i in range(A) for j in range(K)
              if (2*i+1) % 8 == o and (2*j+2) % 8 == eps and 9 <= 2*i+1 <= H-4 and 9 <= 2*j+2 <= H-4]
    diags = sorted({j - i for i, j in labels})
    pos = list(range(len(diags))); random.shuffle(pos)
    Mpos = {s: p * pos[k] for k, s in enumerate(diags)}
    pts = []
    for lab, (i, j) in enumerate(labels):
        if mode == "randomblocks": x = stride * (i + Mpos[j - i])
        else: x = stride * random.randrange(0, 3 * h * h)
        pts.append((x, 2*i+1, lab, j - i, 1)); pts.append((x, 2*j+2, lab, j - i, 0))
    labcols = {q[0] for q in pts}
    kinds = Counter()
    for V in pts:
        for C in pts:
            if C[2] == V[2]: continue
            X, D = C[0] - V[0], C[1] - V[1]
            if abs(X) > 2 * h * h: continue
            for s in (L, F, H):
                num = -D * (s - V[1])
                if num % X == 0:
                    Y = num // X
                    if Y != 0 and V[0] + Y not in labcols:
                        par = "EE" if V[4] == 0 == C[4] else "OO" if V[4] == 1 == C[4] else "mixed"
                        kinds[("Lvertex", par, "H" if s == H else "low",
                               "intra" if V[3] == C[3] and mode == "randomblocks" else "cross")] += 1
                if V[2] < C[2]:
                    Dd = X * X - 4 * (V[1] - s) * (C[1] - s)
                    if Dd >= 0:
                        r = math.isqrt(Dd)
                        if r * r == Dd and (V[0] + C[0] + r) % 2 == 0:
                            for x in {(V[0]+C[0]+r)//2, (V[0]+C[0]-r)//2}:
                                if x not in labcols:
                                    kinds[("Svertex", "same" if V[4] == C[4] else "mixed",
                                           "same" if (s - V[1]) % 2 == 0 else "opp")] += 1
    print(f"mode={mode} h={h} stride={stride} labels={len(labels)}")
    for k, v in sorted(kinds.items()): print("  ", k, v)
h = int(sys.argv[1])
run(h, 4, 1, 0, 3, 7, h - 2, "randomblocks")
run(h, 4, 1, 0, 3, 7, h - 2, "randomcols")
run(h, 8, 1, 0, 3, 7, h - 2, "randomcols")
run(h, 8, 5, 4, 7, 11, h - 4, "randomcols")
