# Seam checker: SAW region | Sea(r0,g) buffer (and the mirror), one point per column.
# Definitions follow sec5 (obstructions) and block_sea criterion (V1)-(V5).
# Usage: py seam.py h r0 g phase side   (side = R: SAW left of seam; L: SAW right of seam)
import sys
import numpy as np
from numba import njit

def Wh(h):
    return (h - 1) * (h - 1) // 4 + 1

@njit(cache=True)
def _gcd(a, b):
    a = abs(a); b = abs(b)
    while b:
        a, b = b, a % b
    return a

@njit(cache=True)
def triples(row, h, m, W, out):
    # row[x] = the unique black row of column x. Tilted right angle at V with black P, Q.
    cnt = 0
    for xv in range(m):
        yv = row[xv]
        for xp in range(max(0, xv - W), min(m, xv + W + 1)):
            if xp == xv:
                continue
            yp = row[xp]
            dx = xp - xv; dy = yp - yv
            if dy == 0:
                continue
            g = _gcd(dx, dy)
            ux = -dy // g; uy = dx // g
            if uy > 0:
                tlo = -((yv - 1) // uy); thi = (h - yv) // uy
            else:
                tlo = -((h - yv) // (-uy)); thi = (yv - 1) // (-uy)
            for t in range(tlo, thi + 1):
                if t == 0:
                    continue
                xq = xv + t * ux; yq = yv + t * uy
                if xq < 0 or xq >= m or ux == 0:
                    continue
                if row[xq] != yq:
                    continue
                if xq < xp:
                    continue
                xf = xp + xq - xv; yf = yp + yq - yv
                if yf < 1 or yf > h:
                    continue
                if xf < 0 or xf >= m:
                    continue
                if cnt < out.shape[0]:
                    out[cnt, 0] = xv; out[cnt, 1] = yv
                    out[cnt, 2] = xp; out[cnt, 3] = yp
                    out[cnt, 4] = xq; out[cnt, 5] = yq
                    out[cnt, 6] = xf; out[cnt, 7] = yf
                cnt += 1
    return cnt

@njit(cache=True)
def mixed(row, h, m, W, rs, ra, rb, out):
    cnt = 0
    L2max = rs.shape[0] - 2
    for xc in range(m):
        yc = row[xc]
        for xd in range(xc + 1, min(m, xc + 2 * W + 1)):
            yd = row[xd]
            ddx = xd - xc; ddy = yd - yc
            L2 = ddx * ddx + ddy * ddy
            if L2 > L2max:
                continue
            for r in range(rs[L2], rs[L2 + 1]):
                a = ra[r]; b = rb[r]
                if (a == ddx and b == ddy) or (a == -ddx and b == -ddy):
                    continue
                sx = xc + xd - a; sy = yc + yd - b
                if sx % 2 != 0 or sy % 2 != 0:
                    continue
                xp = sx // 2; yp = sy // 2
                xq = xp + a; yq = yp + b
                if yp < 1 or yp > h or yq < 1 or yq > h:
                    continue
                g = _gcd(a, b)
                nx = -b // g; ny = a // g
                for k in range(-2 * h, 2 * h + 1):
                    if k == 0:
                        continue
                    xa = xp - k * nx; ya = yp - k * ny
                    xb = xq - k * nx; yb = yq - k * ny
                    if ya < 1 or ya > h or yb < 1 or yb > h:
                        continue
                    if xa == xb:
                        continue  # AB vertical: not a mixed quadruple
                    if xa < 0 or xa >= m or xb < 0 or xb >= m:
                        continue
                    if row[xa] != ya or row[xb] != yb:
                        continue
                    if cnt < out.shape[0]:
                        out[cnt, 0] = xa; out[cnt, 1] = ya
                        out[cnt, 2] = xb; out[cnt, 3] = yb
                        out[cnt, 4] = xc; out[cnt, 5] = yc
                        out[cnt, 6] = xd; out[cnt, 7] = yd
                    cnt += 1
    return cnt

@njit(cache=True)
def rivals(row, h, m, W, out):
    cnt = 0
    for xc in range(m):
        for xd in range(xc + 1, min(m, xc + 2 * W + 1)):
            dx = xd - xc; dy = row[xd] - row[xc]
            if (xc + xd) % 2 != 0:
                continue
            L2 = dx * dx + dy * dy
            L = int(np.sqrt(L2) + 0.5)
            while L * L > L2:
                L -= 1
            while (L + 1) * (L + 1) <= L2:
                L += 1
            if L * L != L2 or L % 2 == 0:
                continue
            s = row[xc] + row[xd]
            if (s - L) % 2 != 0:
                continue
            yp = (s - L) // 2; yq = (s + L) // 2
            if yp < 1 or yq > h:
                continue
            if cnt < out.shape[0]:
                out[cnt, 0] = xc; out[cnt, 1] = row[xc]
                out[cnt, 2] = xd; out[cnt, 3] = row[xd]
            cnt += 1
    return cnt

def reps_table(h, W):
    L2max = 4 * W * W + (h - 1) * (h - 1)
    lst = []
    for a in range(1, 2 * W + 1):
        for b in range(-(h - 1), h):
            L2 = a * a + b * b
            if L2 <= L2max:
                lst.append((L2, a, b))
            L2b = a * a + b * b
    # also negative a handled by symmetry of (a,b) -> (-a,-b) in pq: include a<0 with all b
    # vertical pq (a = 0): pq vertical, allowed (gives axis R1 or rival-type); include
    for b in range(1, h):
        lst.append((b * b, 0, b)); lst.append((b * b, 0, -b))
    lst.sort()
    arr = np.array(lst, dtype=np.int64)
    rs = np.zeros(L2max + 2, dtype=np.int64)
    counts = np.bincount(arr[:, 0], minlength=L2max + 1)
    rs[1:] = np.cumsum(counts[:L2max + 1])
    return rs, arr[:, 1].copy(), arr[:, 2].copy()

def saw_rows(h, r1):
    Ts = max(y for y in range(1, h + 1) if (y - r1) % 16 == 0)
    return [Ts - 24, Ts - 16, Ts - 8, Ts], Ts

def build(h, r0, r1, g, phase, side, rho0=0):
    W = Wh(h)
    m = 4 * (2 * W + 8)
    m -= m % 4
    z0 = (m // 2) // 4 * 4
    rows, Ts = saw_rows(h, r1)
    row = np.zeros(m, dtype=np.int64)
    kind = np.zeros(m, dtype=np.int64)  # 0 shallow, 1 SAW, 2 g
    n0 = z0 // 4
    for x in range(m):
        if x % 4 != 0:
            row[x] = r0; kind[x] = 0
            continue
        n = x // 4
        saw_side = (n < n0) if side == 'R' else (n >= n0)
        if saw_side:
            # phase: shift so that offset of slot n is (n - n0 + phase) mod 4
            o = (n - n0 + phase) % 4
            row[x] = rows[o]; kind[x] = 1
        else:
            row[x] = g; kind[x] = 2
    return row, kind, m, W, rows, Ts

def run(h, r0, r1, g, phase, side, verbose=True):
    row, kind, m, W, rows, Ts = build(h, r0, r1, g, phase, side)
    out = np.zeros((2000000, 8), dtype=np.int64)
    c = triples(row, h, m, W, out)
    tri = out[:min(c, out.shape[0])]
    rs, ra, rb = reps_table(h, W)
    out2 = np.zeros((2000000, 8), dtype=np.int64)
    c2 = mixed(row, h, m, W, rs, ra, rb, out2)
    mq = out2[:min(c2, out2.shape[0])]
    out3 = np.zeros((200000, 4), dtype=np.int64)
    c3 = rivals(row, h, m, W, out3)
    rv = out3[:min(c3, out3.shape[0])]
    def seamy(xs):
        ks = set(int(kind[x]) for x in xs)
        return (1 in ks) and (2 in ks)
    # triples: classify
    fatal = []; parked_W = {}
    for t in tri:
        xv, yv, xp, yp, xq, yq, xf, yf = [int(v) for v in t]
        if not seamy([xv, xp, xq]):
            continue
        if row[xf] == yf:
            fatal.append(('full', tuple(t)))
        elif (row[xf] - yf) % 2 != 0:
            fatal.append(('fatal', tuple(t)))
        else:
            parked_W.setdefault((xf, yf), []).append(tuple(t))
    # V3 among all parked (seam ones vs any)
    allpark = {}
    for t in tri:
        xv, yv, xp, yp, xq, yq, xf, yf = [int(v) for v in t]
        if row[xf] != yf and (row[xf] - yf) % 2 == 0:
            allpark.setdefault((xf, yf), []).append((xv, xp, xq))
    v3 = [w for w, l in allpark.items() if len(l) > 1 and any(seamy(list(z)) for z in l)]
    mqs = [tuple(q) for q in mq if seamy([int(q[0]), int(q[2]), int(q[4]), int(q[6])])]
    rvs = [tuple(r) for r in rv if seamy([int(r[0]), int(r[2])])]
    if verbose:
        print(f"h={h} r0={r0} r1={r1} g={g} phase={phase} side={side} T*={Ts} rows={rows} | "
              f"tri_total={c} mq_total={c2} rv_total={c3} | seam: fatal/full={len(fatal)} parked={sum(len(v) for v in parked_W.values())} V3={len(v3)} MQ={len(mqs)} RIV={len(rvs)}")
        for r in rvs[:4]:
            print("   rival", r)
        for f in fatal[:3]:
            print("   tri", f)
        for q in mqs[:3]:
            print("   mq", q)
    return len(fatal), len(v3), len(mqs), len(rvs)

if __name__ == '__main__':
    h, r0, r1, g, phase = [int(a) for a in sys.argv[1:6]]
    side = sys.argv[6]
    run(h, r0, r1, g, phase, side)
