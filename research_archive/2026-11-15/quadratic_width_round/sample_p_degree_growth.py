"""Sample the P degree of random labels in the aligned Hilbert tile.

Tile of side s = 2^k, offset T = -2s, stride S, M choices. A label u at cell
(x, y) with rank r has slot M r + xi. A P event with partner v and choice
difference delta (|delta| < M) is an integer solution of

    (S q)^2 + Y^2 = L^2,   q = |M (r_v - r_u) + delta|,
    Y = |2T + 1 + 2(y_v - x_u)|  or  |2T + 1 + 2(y_u - x_v)|.

Every solution is Y = g e f, q = g (f^2 - e^2)/(2S) with g, e, f odd,
e < f coprime, f = +-e (mod S). The script lists all such triples once, then
for each sampled label finds its partners by decoding the candidate ranks.
The degree of a label is its number of distinct (partner, delta) pairs.
"""
import sys, json, math, time
import numpy as np


def decode(ranks, side):
    work = ranks.copy()
    x = np.zeros_like(ranks); y = np.zeros_like(ranks)
    scale = 1
    while scale < side:
        rx = (work // 2) & 1
        ry = (work ^ rx) & 1
        refl = (ry == 0) & (rx == 1)
        x = np.where(refl, scale - 1 - x, x); y = np.where(refl, scale - 1 - y, y)
        sw = ry == 0
        x, y = np.where(sw, y, x), np.where(sw, x, y)
        x += scale * rx; y += scale * ry
        work //= 4; scale *= 2
    return x, y


def triples(ymin, ymax, S, qmax):
    Ys, qs = [], []
    e = 1
    while e * (e + 2) <= ymax:
        fs = []
        for res in (e % S, (-e) % S):
            start = e + ((res - e) % S)
            if start <= e:
                start += S
            fs.append(np.arange(start, ymax // e + 1, S, dtype=np.int64))
        f = np.unique(np.concatenate(fs))
        f = f[np.gcd(f, e) == 1]
        ef = e * f
        base_q = (f * f - e * e) // (2 * S)
        for efv, bq in zip(ef.tolist(), base_q.tolist()):
            glo = -(-ymin // efv); ghi = ymax // efv
            if glo % 2 == 0:
                glo += 1
            if glo > ghi:
                continue
            g = np.arange(glo, ghi + 1, 2, dtype=np.int64)
            q = g * bq
            keep = q <= qmax
            Ys.append(g[keep] * efv); qs.append(q[keep])
        e += 2
    return np.concatenate(Ys), np.concatenate(qs)


def main():
    k, samples, S, M = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    side = 1 << k; n = side * side; off = -2 * side
    t0 = time.monotonic()
    Y, q = triples(2 * side + 1, 6 * side - 1, S, M * n)
    a = (-Y - 2 * off - 1) // 2          # y_v - x_u (role A) or y_u - x_v (role B)
    rng = np.random.default_rng(12345 + k)
    ranks = rng.integers(0, n, samples).astype(np.int64)
    xs, ys = decode(ranks, side)
    degs = []
    for r, x, y in zip(ranks.tolist(), xs.tolist(), ys.tolist()):
        found = set()
        for role, target in (('A', x + a), ('B', y - a)):
            ok = (target >= 0) & (target < side)
            qq = q[ok]; tt = target[ok]
            for delta in range(-(M - 1), M):
                for sign in (1, -1):
                    num = sign * qq - delta
                    m = num % M == 0
                    d = num[m] // M
                    rv = r + d
                    inside = (rv >= 0) & (rv < n) & (d != 0)
                    rv = rv[inside]; tg = tt[m][inside]
                    if not len(rv):
                        continue
                    xv, yv = decode(rv, side)
                    hit = (yv == tg) if role == 'A' else (xv == tg)
                    for v in rv[hit].tolist():
                        found.add((v, delta))
        degs.append(len(found))
    degs = np.array(degs)
    res = dict(side=side, stride=S, choices=M, triples=int(len(Y)), samples=samples,
               mean_degree=float(degs.mean()), std_error=float(degs.std(ddof=1) / math.sqrt(samples)),
               max_degree=int(degs.max()), share_degree_ge_M=float((degs >= M).mean()),
               seconds=round(time.monotonic() - t0, 1))
    print(json.dumps(res), flush=True)


if __name__ == '__main__':
    main()
