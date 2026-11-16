import numpy as np, math, time
def hilbert(q):
    pts = np.zeros((1, 2), dtype=np.int64); s = 1
    while s < q:
        x = pts[:, 0]; y = pts[:, 1]
        pts = np.concatenate([np.stack([y, x], 1), np.stack([x, y + s], 1), np.stack([x + s, y + s], 1), np.stack([2*s-1-y, s-1-x], 1)])
        s *= 2
    return pts

h, S, M = 2**12, 8, 3
l = 512                      # tile side (diagonal tile), labels with l/2 <= |j-i| < l
I0 = J0 = 512
Q2 = 2 * l
H = hilbert(Q2)
ncell = Q2 * Q2
# vector table: is (S q, Y) Pythagorean with L <= h-1, Y odd
qmax = (h - 1) // S
Ymax = 4 * l
vec = np.zeros((qmax + 1, Ymax + 1), dtype=bool)
for qq in range(1, qmax + 1):
    X = S * qq
    for Y in range(1, Ymax + 1, 2):
        L2 = X * X + Y * Y
        L = math.isqrt(L2)
        if L * L == L2 and L <= h - 1:
            vec[qq, Y] = True
# V_R exact over Y in [l/2, 3l]
VR = int(vec[:, l // 2: 3 * l + 1].sum())
Wd = (h - 1) // (S * M) + 1
t0 = time.time()
mus = []
Js = list(range(0, l, 37))
for J in Js:
    li = H[:, 0] + I0              # label i of cell
    lj = H[:, 1] + J0 - J          # label j of cell
    T = lj - li
    keep = (np.abs(T) >= l // 2) & (np.abs(T) < l) & (H[:, 0] < l) & (H[:, 1] >= J) & (H[:, 1] < J + l)
    Nret = int(keep.sum())
    E = 0
    for d in range(1, Wd + 1):
        a = np.arange(0, ncell - d)
        b = a + d
        both = keep[a] & keep[b]
        aa = a[both]; bb = b[both]
        Y1 = np.abs(2 * (lj[bb] - li[aa]) + 1)
        Y2 = np.abs(2 * (lj[aa] - li[bb]) + 1)
        for delta in range(-(M - 1), M):
            qq = M * d + delta
            if qq < 1 or qq > qmax:
                continue
            row = vec[qq]
            for Y in (Y1, Y2):
                ok = Y <= Ymax
                E += int(row[Y[ok]].sum())
    mus.append(2 * E / Nret)
    if time.time() - t0 > 45:
        break
print("J values used", len(mus), "mean degree per J (first 6)", [round(x, 4) for x in mus[:6]])
print("average over sampled J", round(float(np.mean(mus)), 4), " bound 256*V_R/l =", round(256 * VR / l, 2),
      " V_R =", VR)
