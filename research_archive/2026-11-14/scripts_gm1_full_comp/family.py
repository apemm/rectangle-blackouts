"""Which members of the explicit families F1(x) = 0^H 2^x 1^(H-x) and F2(y) = 0^H 1^(H-y) 2^y (period P = 2H)
solve shift H (!=), beta (!= s), beta+1 (!= s-3) on Z/P?"""
import sys
def ok(seq, sh):
    P = len(seq); return all(seq[(k + a) % P] - seq[k] != d for a, d in sh for k in range(P))
for al in range(1, int(sys.argv[1]) + 1):
    H = 2 ** al; P = 2 * H; rows = []
    for s in (1, 2):
        for beta in range(1, P - 1):
            sh = [(H, 0), (beta, s), (beta + 1, s - 3)]
            f1 = [x for x in range(H + 1) if ok([0] * H + [2] * x + [1] * (H - x), sh)]
            f2 = [y for y in range(H + 1) if ok([0] * H + [1] * (H - y) + [2] * y, sh)]
            rows.append((s, beta, f1, f2))
    if al <= 3:
        for r in rows: print("alpha", al, "s", r[0], "beta", r[1], "F1 x:", r[2], "F2 y:", r[3])
    print("alpha", al, "uncovered by F1 or F2:", [(s, b) for s, b, f1, f2 in rows if not f1 and not f2])
