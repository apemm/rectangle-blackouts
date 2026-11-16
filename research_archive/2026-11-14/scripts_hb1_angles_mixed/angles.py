"""Cross-parity label right angles in the Hilbert placement x = S(M r + xi).

Enumerator uses the parametrization (proved in the write-up):
  V vertex, F same parity as V, G opposite parity,
  G - V = (S*x2, Y2), gamma = gcd(Y2, x2), a = Y2/gamma, b = -x2/gamma,
  F - V = lam * (S*a, S^2*b), lam != 0,
  |lam| < 64(|a| + M - 1)/(M S^4 b^2).
Brute force (small h) checks completeness by direction hashing.
"""
import sys, math, json, random
import numpy as np


def hilbert(q):
    if q == 1:
        return [(0, 0)]
    n = q // 2
    s = hilbert(n)
    return ([(y, x) for x, y in s] + [(x, y + n) for x, y in s]
            + [(x + n, y + n) for x, y in s]
            + [(2 * n - 1 - y, n - 1 - x) for x, y in s])


def setup(h, S, M, seed):
    A, K = (h + 1) // 2, h // 2
    q = 1 << (max(A, K) - 1).bit_length()
    xy = np.array(hilbert(q), dtype=np.int64)
    act = (xy[:, 0] < A) & (xy[:, 1] < K)
    rng = np.random.default_rng(seed)
    xi = rng.integers(0, M, size=q * q) if M > 1 else np.zeros(q * q, np.int64)
    slot = M * np.arange(q * q, dtype=np.int64) + xi
    owner = -np.ones(M * q * q + 1, dtype=np.int64)
    owner[slot[act]] = np.nonzero(act)[0]
    odd = 2 * xy[:, 0] + 1
    even = 2 * xy[:, 1] + 2
    return dict(h=h, S=S, M=M, q=q, xy=xy, act=act, slot=slot, owner=owner,
                odd=odd, even=even)


def enumerate_angles(D, slots=False):
    h, S, M = D['h'], D['S'], D['M']
    act, slot, owner, odd, even = D['act'], D['slot'], D['owner'], D['odd'], D['even']
    nslot = owner.shape[0] - 1
    V = np.nonzero(act)[0]
    # |x2| = |b| gamma, |a| gamma <= h-1, M S^4 b^2 < 64(|a|+M-1)
    W2 = 1
    for aa in range(1, h):
        bmax2 = 64 * (aa + M - 1) / (M * S ** 4)
        if bmax2 > 1:
            W2 = max(W2, int(math.sqrt(bmax2) * (h - 1) / aa) + 1)
    found = []
    for vpar in (0, 1):  # 0: vertex is odd point
        yV = odd[V] if vpar == 0 else even[V]
        for x2 in range(-W2, W2 + 1):
            if x2 == 0:
                continue
            sg = slot[V] + x2
            ok = (sg >= 0) & (sg < nslot)
            g = np.full(V.shape, -1)
            g[ok] = owner[sg[ok]]
            m = g >= 0
            if not m.any():
                continue
            vv, gg, yv = V[m], g[m], yV[m]
            yG = even[gg] if vpar == 0 else odd[gg]
            Y2 = yG - yv
            gam = np.gcd(np.abs(Y2), abs(x2))
            a = Y2 // gam
            b = -x2 // gam
            lam_max = (64 * (np.abs(a) + M - 1)) // (M * S ** 4 * b * b)
            top = int(lam_max.max()) if lam_max.size else 0
            for lam in range(1, top + 1):
                sel = lam_max >= lam
                if not sel.any():
                    break
                for sgn in (1, -1):
                    L = sgn * lam
                    v2, g2, a2, b2, yv2, Y22 = vv[sel], gg[sel], a[sel], b[sel], yv[sel], Y2[sel]
                    sf = slot[v2] + L * a2
                    ok2 = (sf >= 0) & (sf < nslot)
                    f = np.full(v2.shape, -1)
                    f[ok2] = owner[sf[ok2]]
                    m2 = f >= 0
                    if not m2.any():
                        continue
                    f, v3, g3, a3, b3, yv3, Y23 = f[m2], v2[m2], g2[m2], a2[m2], b2[m2], yv2[m2], Y22[m2]
                    yF = odd[f] if vpar == 0 else even[f]
                    hit = (yF - yv3) == L * S * S * b3
                    hit &= (f != v3)
                    # fourth corner row in strip
                    yW = yF + (yv3 + Y23) - yv3
                    hit &= (yW >= 1) & (yW <= h)
                    for k in np.nonzero(hit)[0]:
                        if slots:
                            found.append((int(v3[k]), vpar, int(f[k]), int(g3[k]), int(slot[v3[k]] + L * a3[k]), int(slot[v3[k]] + x2)))
                        else:
                            found.append((int(v3[k]), vpar, int(f[k]), int(g3[k])))
    return sorted(set(found))


def brute(D):
    """All tilted label right angles (any parity pattern) by direction hashing."""
    h, S = D['h'], D['S']
    act, slot, odd, even = D['act'], D['slot'], D['odd'], D['even']
    R = np.nonzero(act)[0]
    X = np.concatenate([S * slot[R], S * slot[R]])
    Y = np.concatenate([odd[R], even[R]])
    lab = np.concatenate([R, R])
    par = np.concatenate([np.zeros(len(R), int), np.ones(len(R), int)])
    n = len(X)
    out = []
    B = 1 << 31
    for k in range(n):
        dx = X - X[k]
        dy = Y - Y[k]
        msk = (dx != 0) & (dy != 0)  # tilted legs only
        idx = np.nonzero(msk)[0]
        dx, dy = dx[idx], dy[idx]
        gg = np.gcd(np.abs(dx), np.abs(dy))
        p, qq = dx // gg, dy // gg
        sgn = np.where(p < 0, -1, 1)
        p, qq = p * sgn, qq * sgn
        key = p * B + qq
        # perpendicular (-qq, p) normalized
        pp, pq = -qq, p
        s2 = np.where(pp < 0, -1, 1)
        pp, pq = pp * s2, pq * s2
        pkey = pp * B + pq
        common = np.intersect1d(key, pkey)
        if common.size == 0:
            continue
        for c in common:
            i1 = idx[key == c]
            # perpendicular partners: those whose key is perp of c
            p0 = (int(c) + B // 2) // B
            q0 = int(c) - p0 * B
            pp0, pq0 = -q0, p0
            if pp0 < 0:
                pp0, pq0 = -pp0, -pq0
            i2 = idx[key == pp0 * B + pq0]
            for u in i1:
                for w in i2:
                    yW = Y[u] + Y[w] - Y[k]
                    if 1 <= yW <= h:
                        out.append((k, u, w))
    res = set()
    for k, u, w in out:
        # classify
        pk, pu, pw = par[k], par[u], par[w]
        if pu == pk and pw != pk:
            F, G = u, w
        elif pw == pk and pu != pk:
            F, G = w, u
        else:
            res.add(('other', int(lab[k]), int(pk), int(lab[u]), int(lab[w])))
            continue
        res.add(('cross', int(lab[k]), int(pk), int(lab[F]), int(lab[G])))
    return res


if __name__ == '__main__':
    mode = sys.argv[1]
    h, S, M, seed = map(int, sys.argv[2:6])
    D = setup(h, S, M, seed)
    if mode == 'check':
        e = set(('cross',) + t for t in enumerate_angles(D))
        b = brute(D)
        bc = {t for t in b if t[0] == 'cross'}
        print(json.dumps({'h': h, 'S': S, 'M': M, 'enum': len(e), 'brute_cross': len(bc),
                          'brute_other': len(b) - len(bc), 'match': e == bc}))
    else:
        t = enumerate_angles(D)
        nl = int(D['act'].sum())
        inc = np.zeros(D['q'] ** 2, np.int64)
        two = 0
        for (v, p, f, g) in t:
            for z in {v, f, g}:
                inc[z] += 1
            if f == g:
                two += 1
        print(json.dumps({'h': h, 'S': S, 'M': M, 'seed': seed, 'labels': nl, 'angles': len(t),
                          'two_label': two, 'mean_inc': 3 * len(t) / nl,
                          'max_inc': int(inc.max()), 'labels_hit': int((inc > 0).sum()),
                          'sample': t[:3]}))
