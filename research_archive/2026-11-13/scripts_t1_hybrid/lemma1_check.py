# Sanity check of Lemma 1: a two-label mixed support with exactly one sea point
# has at most 2 relative geometries (offset X of label f, column xi of the sea point).
# Label e at column 0 with rows a,b; label f at column X with rows c,d; sea point (xi,s).
import numpy as np, random, sys
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
R = 350
Xs = np.arange(-R, R + 1)
X, XI = np.meshgrid(Xs, Xs, indexing="ij")

def count(role, a, b, c, d, s):
    # points as (col, row) arrays
    Pa = (0 * X, a + 0 * X); Pb = (0 * X, b + 0 * X)
    Pc = (X, c + 0 * X); Pd = (X, d + 0 * X); Ps = (XI, s + 0 * X)
    A, B, C, D = {
        "ac|bs": (Pa, Pc, Pb, Ps), "ac|ds": (Pa, Pc, Pd, Ps),
        "as|cd": (Pa, Ps, Pc, Pd), "as|bc": (Pa, Ps, Pb, Pc),
        "cs|ab": (Pc, Ps, Pa, Pb), "cs|ad": (Pc, Ps, Pa, Pd)}[role]
    u1, u2 = B[0] - A[0], B[1] - A[1]
    w1, w2 = D[0] - C[0], D[1] - C[1]
    z1, z2 = C[0] + D[0] - A[0] - B[0], C[1] + D[1] - A[1] - B[1]
    ok = (u1 * u1 + u2 * u2 == w1 * w1 + w2 * w2) & (u1 * z1 + u2 * z2 == 0)
    ok &= (X != 0) & (XI != 0) & (XI != X)            # sea point not in a label column
    ok &= ~((w1 == u1) & (w2 == u2)) & ~((w1 == -u1) & (w2 == -u2))
    ok &= (u1 != 0)                                    # nonvertical side
    return int(ok.sum())

roles = ["ac|bs", "ac|ds", "as|cd", "as|bc", "cs|ab", "cs|ad"]
worst = {r: 0 for r in roles}; total = {r: 0 for r in roles}
for trial in range(25):
    a, b, c, d = random.sample(range(10, 120), 4)
    s = random.choice([1, 2, 3, 130, 131])
    for r in roles:
        n = count(r, a, b, c, d, s)
        worst[r] = max(worst[r], n); total[r] += n
print("max solutions per row assignment:", worst)
print("total over trials:", total)
