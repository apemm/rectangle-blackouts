# Large-h census of the label+shallow families on the real rigid layout of Corollary B
# (true p > 20h, p = 3 or 7 mod 20), every region type. Families searched by exact
# equations, each hit re-checked from the definition (mixed quadruple / tilted rectangle):
#   M2c  : A, C shallow (row r0), B, D label points (any classes, any blocks)
#   SLL  : tilted rectangles with one shallow corner and two label corners (Pa, Pb, Pc, X1, X2)
#   V3   : two SLL triples (parked) with the same white corner
import sys, time
from math import isqrt, gcd
import numpy as np
from numba import njit
from board import gt_edges

def primes_mod(lo, hi):
    out = []
    for n in range(lo + 1, hi + 1):
        if n % 20 in (3, 7) and all(n % q for q in range(2, isqrt(n) + 1)):
            out.append(n)
    return out

SPLIT = 1
def layout(h, iota, mu, kappa, p, nu, colors):
    A = (h + 1) // 2; K = h // 2
    r0 = 1 if iota % 2 else 3
    mod = 2 ** nu; inv = pow(p, -1, mod)
    cnt = {}; pts = []
    for s in range(-(A - 1), K):
        if (s - kappa - mu) % 2:
            continue
        col = colors[s]
        byc = {}
        for i, c in col.items():
            j = i + s
            if i % 8 != iota or i == 0:
                continue
            if iota % 2 == 0 and (i == 2 or j in (0, 1)):
                continue
            byc.setdefault((c, (i // 8) % SPLIT), []).append(i)
        for c in sorted(byc):
            base = (inv * (s - kappa)) % mod
            k = cnt.get(base, 0); cnt[base] = k + 1
            pos = base + mod * k
            M = p * pos
            for i in byc[c]:
                x = 4 * (i + M)
                pts.append((x, 2 * i + 1, 0, pos, s, i))
                pts.append((x, 2 * (i + s) + 2, 1, pos, s, i))
    return pts, r0

def colorings(h):
    A = (h + 1) // 2; K = h // 2
    colors = {}
    for s in range(-(A - 1), K):
        T = 2 * s + 1
        E = gt_edges(T, h)
        col = {}
        for i in range(A):
            if not (0 <= i + s < K):
                continue
            used = {col[i - d] for d in E if (i - d) in col}
            c = 0
            while c in used:
                c += 1
            col[i] = c
        colors[s] = col
    return colors

def divisor_table(N):
    # CSR
    deg = np.zeros(N + 1, np.int64)
    for d in range(1, N + 1):
        deg[d::d] += 1
    start = np.zeros(N + 2, np.int64)
    start[1:] = np.cumsum(deg)
    data = np.zeros(start[-1], np.int64)
    fillp = start[:-1].copy()
    for d in range(1, N + 1):
        idx = np.arange(d, N + 1, d)
        data[fillp[idx]] = d
        fillp[idx] += 1
    return start, data

@njit(cache=True)
def find_idx(keys, k):
    i = np.searchsorted(keys, k)
    if i < keys.shape[0] and keys[i] == k:
        return i
    return -1

@njit(cache=True)
def m2c_search(px, py, keys, h, r0, dstart, ddata, out):
    H1 = h + 1
    n = px.shape[0]; c = 0
    for b in range(n):
        xB = px[b]; yB = py[b]
        u2 = yB - r0
        if u2 <= 0:
            continue
        for e in range(1, (h - yB) // 2 + 1):
            N1 = e * u2
            M = 4 * e * (u2 + e)
            for t in range(dstart[M], dstart[M + 1]):
                f1 = ddata[t]; f2 = M // f1
                if f1 > f2 or (f1 - f2) % 2:
                    continue
                zz = (f1 + f2) // 2; w = (f2 - f1) // 2
                for sg in (1, -1):
                    z = sg * zz
                    if N1 % z:
                        continue
                    n1 = -N1 // z
                    for s2 in (1, -1):
                        if w == 0 and s2 == -1:
                            continue
                        num = -z + s2 * w
                        if num % 2:
                            continue
                        tau = num // 2
                        Dl = n1 + tau
                        xD = xB + Dl; yD = yB + 2 * e
                        d = find_idx(keys, xD * H1 + yD)
                        if d < 0:
                            continue
                        xA = xB - z
                        xC = 2 * n1 + 2 * xB - z - xD
                        if xA % 4 == 0 or xC % 4 == 0:
                            continue
                        if c < out.shape[0]:
                            out[c, 0] = b; out[c, 1] = d; out[c, 2] = xA; out[c, 3] = xC
                        c += 1
    return c

def check_mixed(A, B, C, D, h):
    U = (B[0] - A[0], B[1] - A[1]); V = (D[0] - C[0], D[1] - C[1])
    if U[0] ** 2 + U[1] ** 2 != V[0] ** 2 + V[1] ** 2:
        return False
    s = (C[0] + D[0] - A[0] - B[0], C[1] + D[1] - A[1] - B[1])
    if s[0] % 2 or s[1] % 2:
        return False
    nn = (s[0] // 2, s[1] // 2)
    if nn == (0, 0) or nn[0] * U[0] + nn[1] * U[1] != 0:
        return False
    if V == U or V == (-U[0], -U[1]) or U[0] == 0:
        return False
    pp = (A[0] + nn[0], A[1] + nn[1]); qq = (B[0] + nn[0], B[1] + nn[1])
    return 1 <= pp[1] <= h and 1 <= qq[1] <= h

def sll_triples(pts, r0, h, Xmax):
    """Tilted rectangles with exactly one shallow corner E (row r0, column != 0 mod 4) and two
    label corners. Returns list of (type, E, F, G, W, parked)."""
    out = []
    xs = np.array([q[0] for q in pts]); order = np.argsort(xs, kind='stable')
    P = [pts[k] for k in order]
    n = len(P)
    for a in range(n):
        for b in range(a + 1, n):
            if P[b][0] - P[a][0] > Xmax:
                break
            for (F, G) in ((P[a], P[b]),):
                # E vertex
                f = F[1] - r0; g = G[1] - r0
                if f > 0 and g > 0:
                    disc = (F[0] - G[0]) ** 2 - 4 * f * g
                    if disc >= 0:
                        r = isqrt(disc)
                        if r * r == disc and (F[0] + G[0] + r) % 2 == 0:
                            for xE in {(F[0] + G[0] + r) // 2, (F[0] + G[0] - r) // 2}:
                                if xE % 4 == 0:
                                    continue
                                W = (F[0] + G[0] - xE, F[1] + G[1] - r0)
                                if W[1] > h:
                                    continue
                                out.append(('vertex', (xE, r0), F, G, W, (W[1] - r0) % 2 == 0))
                # E an end: vertex V in {F, G}
                for (V, Gq) in ((F, G), (G, F)):
                    gx = Gq[0] - V[0]; gy = Gq[1] - V[1]
                    if gx == 0 or gy == 0:
                        continue
                    d = gcd(abs(gx), abs(gy))
                    px_, py_ = -gy // d, gx // d
                    if (r0 - V[1]) % py_:
                        continue
                    k = (r0 - V[1]) // py_
                    if k == 0:
                        continue
                    E = (V[0] + k * px_, r0)
                    if E[0] % 4 == 0:
                        continue
                    W = (E[0] + gx, E[1] + gy)
                    if not (1 <= W[1] <= h):
                        continue
                    out.append(('end', E, V, Gq, W, (W[1] - r0) % 2 == 0))
    return out

if __name__ == '__main__':
    h = int(sys.argv[1]); nu_extra = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    types = None
    if len(sys.argv) > 3:
        types = [(int(a), int(b)) for a, b in (s.split(',') for s in sys.argv[3].split(';'))]
    t0 = time.time()
    if len(sys.argv) > 4:
        SPLIT = int(sys.argv[4])
    K = h // 2
    nu = 0
    while 2 ** nu < K / 8:
        nu += 1
    nu += nu_extra
    p = primes_mod(20 * h, 40 * h)[0]
    colors = colorings(h)
    chi = max(max(c.values()) + 1 for c in colors.values())
    Xmax = (h - 1) ** 2 // 4 + h + 4
    Mmax = 2 * h * h + 8
    dstart, ddata = divisor_table(Mmax)
    print('h=%d p=%d nu=%d max chi(G_T)=%d prep %.1fs' % (h, p, nu, chi, time.time() - t0)); sys.stdout.flush()
    tot = dict(labels=0, m2c=0, m2c_intra=0, m2c_cross=0, sll_parked=0, sll_fatal=0, v3=0)
    examples = []
    if types is None:
        types = [(a, b) for a in range(8) for b in range(2)]
    for (iota, mu) in types:
        pts, r0 = layout(h, iota, mu, 0, p, nu, colors)
        if not pts:
            continue
        tot['labels'] += len(pts) // 2
        H1 = h + 1
        px = np.array([q[0] for q in pts], np.int64); py = np.array([q[1] for q in pts], np.int64)
        key = px * H1 + py
        o = np.argsort(key); keys = key[o]; pxs = px[o]; pys = py[o]
        meta = [pts[k] for k in o]
        out = np.zeros((100000, 4), np.int64)
        c = m2c_search(pxs, pys, keys, h, r0, dstart, ddata, out)
        for r in range(min(c, out.shape[0])):
            b, d, xA, xC = out[r]
            B = meta[b]; D = meta[d]
            if not check_mixed((xA, r0), (B[0], B[1]), (xC, r0), (D[0], D[1]), h):
                print('  M2c candidate failed definition check', B, D); continue
            tot['m2c'] += 1
            same = (B[3] == D[3])
            tot['m2c_intra' if same else 'm2c_cross'] += 1
            if len(examples) < 12:
                examples.append(('M2c', iota, mu, 'odd' if B[2] == 0 else 'even', 'same block' if same else 'cross',
                                 'B slot', B[5], 'D slot', D[5], 'rows', B[1], D[1], 'A', (xA, r0), 'C', (xC, r0)))
        tr = sll_triples(pts, r0, h, Xmax)
        Wc = {}
        for t in tr:
            if t[5]:
                tot['sll_parked'] += 1
                Wc.setdefault(t[4], []).append(t)
            else:
                tot['sll_fatal'] += 1
                if len(examples) < 20:
                    examples.append(('fatal SLL', iota, mu, t))
        for W, lst in Wc.items():
            if len(lst) > 1:
                tot['v3'] += 1
                if len(examples) < 24:
                    examples.append(('V3', iota, mu, lst))
        print('type (%d,%d) r0=%d labels=%d M2c=%d SLL parked=%d | %.1fs' % (iota, mu, r0, len(pts) // 2, c,
              sum(1 for t in tr if t[5]), time.time() - t0)); sys.stdout.flush()
    print(tot)
    for e in examples:
        print(e)
