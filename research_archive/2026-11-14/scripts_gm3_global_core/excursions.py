"""Excursion decomposition check for the local P block systems G_B^o (S = 32).

Usage: py -I excursions.py B orient M version
  orient in {id, swap}; version in {cand, gen}.

Builds the local candidate system of a main-diagonal block of side B with my own
code (Hilbert recursion (2) of the placement note, vectors by divisor pairs of Y^2),
then
  (1) checks that no constraint joins two labels in different excursions, where an
      excursion is a maximal rank interval that starts at a diagonal cell (x, x)
      and contains no other diagonal cell;
  (2) checks Lemma B directly: no constraint enters a main-diagonal aligned
      sub-block from an earlier rank;
  (3) computes the weighted M-core and splits it by excursion.
"""
import sys, time
import numpy as np
import numba as nb

S = 32


def hilbert(q):
    """Cells of H_q in rank order, recursion (2): (y,x), (x,y+q), (x+q,y+q), (2q-1-y,q-1-x)."""
    xs = np.zeros(1, dtype=np.int64)
    ys = np.zeros(1, dtype=np.int64)
    n = 1
    while n < q:
        x, y = xs, ys
        xs = np.concatenate([y, x, x + n, 2 * n - 1 - y])
        ys = np.concatenate([x, y + n, y + n, n - 1 - x])
        n *= 2
    return xs, ys


def vectors(ymax):
    """All (q, Y): Y odd <= ymax, (S q)^2 + Y^2 = L^2. Returns list of (q, Y, L)."""
    out = []
    for Y in range(1, ymax + 1, 2):
        Y2 = Y * Y
        u = 1
        while u * u < Y2:
            if Y2 % u == 0:
                w = Y2 // u
                X = (w - u) // 2
                L = (w + u) // 2
                if X % S == 0 and X > 0:
                    out.append((X // S, Y, L))
            u += 2
    return out


@nb.njit(cache=True)
def scan(ii, jj, d, yv, lv, B, gen, out_r):
    """Ranks r such that (r, r+d) carries a cross pair with |b - a| = yv (either role).
    gen: require the owner of the completion rows to lie outside the block."""
    N = ii.shape[0]
    cnt = 0
    for r in range(N - d):
        s = r + d
        ok = False
        for role in range(2):
            if role == 0:
                io = ii[r]; je = jj[s]
            else:
                io = ii[s]; je = jj[r]
            U = je - io
            Y = 2 * U + 1
            if Y < 0:
                Y = -Y
            if Y != yv:
                continue
            if gen == 0:
                ok = True
                break
            a = 2 * io + 1
            b = 2 * je + 2
            ssum = a + b
            r1 = (ssum - lv) // 2
            r2 = (ssum + lv) // 2
            if r1 % 2 == 1:
                odd = r1; ev = r2
            else:
                odd = r2; ev = r1
            io2 = (odd - 1) // 2
            je2 = (ev - 2) // 2
            inside = (odd >= 1) and (ev >= 2) and (io2 < B) and (je2 < B)
            if not inside:
                ok = True
                break
        if ok:
            out_r[cnt] = r
            cnt += 1
    return cnt


@nb.njit(cache=True)
def weighted_core(n, er, es, M):
    deg = np.zeros(n, dtype=np.int64)
    m = er.shape[0]
    for k in range(m):
        deg[er[k]] += 1
        deg[es[k]] += 1
    # adjacency in CSR
    start = np.zeros(n + 1, dtype=np.int64)
    for k in range(m):
        start[er[k] + 1] += 1
        start[es[k] + 1] += 1
    for v in range(n):
        start[v + 1] += start[v]
    pos = start[:-1].copy()
    adj = np.zeros(2 * m, dtype=np.int64)
    for k in range(m):
        adj[pos[er[k]]] = es[k]; pos[er[k]] += 1
        adj[pos[es[k]]] = er[k]; pos[es[k]] += 1
    alive = np.ones(n, dtype=np.bool_)
    stack = np.zeros(n, dtype=np.int64)
    top = 0
    for v in range(n):
        if deg[v] < M:
            alive[v] = False
            stack[top] = v; top += 1
    while top > 0:
        top -= 1
        v = stack[top]
        for p in range(start[v], start[v + 1]):
            w = adj[p]
            if alive[w]:
                deg[w] -= 1
                if deg[w] < M:
                    alive[w] = False
                    stack[top] = w; top += 1
    return alive


def main():
    B = int(sys.argv[1]); orient = sys.argv[2]; M = int(sys.argv[3]); version = sys.argv[4]
    t0 = time.time()
    xs, ys = hilbert(B)
    if orient == 'swap':
        xs, ys = ys, xs
    ii = xs.astype(np.int64); jj = ys.astype(np.int64)
    N = B * B
    vecs = vectors(2 * B - 1)
    gen = 1 if version == 'gen' else 0
    buf = np.zeros(N, dtype=np.int64)
    R = []; D = []; DL = []
    for (q, Y, L) in vecs:
        for d in sorted({q // M, -(-q // M)}):
            if d < 1 or d >= N:
                continue
            delta = q - M * d
            if abs(delta) > M - 1:
                continue
            c = scan(ii, jj, d, Y, L, B, gen, buf)
            if c:
                R.append(buf[:c].copy()); D.append(np.full(c, d)); DL.append(np.full(c, delta))
    r = np.concatenate(R); d = np.concatenate(D); dl = np.concatenate(DL)
    key = (r * 40000 + d) * 16 + (dl + 8)
    _, idx = np.unique(key, return_index=True)
    r = r[idx]; d = d[idx]; dl = dl[idx]; s = r + d
    print(f"B={B} {orient} M={M} {version}: vectors={len(vecs)} constraints={len(r)} build {time.time()-t0:.1f}s")

    # excursions: piece id = number of diagonal cells with rank <= r, minus 1
    diag = (ii == jj)
    piece = np.cumsum(diag) - 1
    cross = np.count_nonzero(piece[r] != piece[s])
    print("constraints joining different excursions:", cross)

    # Lemma B directly: for each diagonal aligned sub-block D of side 2^k, the earlier endpoint
    # of an edge whose later endpoint lies in D must also lie in D.
    viol = 0
    k = 1
    while k <= B:
        bi = ii // k; bj = jj // k
        indiag = (bi == bj)
        blk = np.where(indiag, bi, -1)
        mask = indiag[s]
        # later endpoint s in diagonal block blk[s]; earlier r must be in same block
        viol += np.count_nonzero(mask & (blk[r] != blk[s]) & (r < s))
        k *= 2
    print("constraints entering a diagonal sub-block from an earlier rank:", viol)

    # piece scale: piece starts at diagonal cell (x,x); scale = 2^v2(x+1)
    dcells = np.nonzero(diag)[0]  # ranks of diagonal cells in rank order
    xstart = ii[dcells]
    scale = np.array([((x + 1) & -(x + 1)) for x in xstart])
    print("excursion lengths match (4B'^2+2)/3 for B'<B:",
          all((np.diff(np.append(dcells, N))[scale < B] == (4 * scale[scale < B] ** 2 + 2) // 3)))

    alive = weighted_core(N, r, s, M)
    nc = int(alive.sum())
    print(f"weighted {M}-core size: {nc}")
    if nc:
        pc = piece[alive]
        T = (jj - ii)[alive]
        for p in np.unique(pc):
            sel = pc == p
            x = xstart[p]; sc = scale[p]
            Tp = T[sel]
            # level inside the excursion: side of the off-diagonal Hilbert block containing the label
            idx_alive = np.nonzero(alive)[0][sel]
            lev = []
            for v in idx_alive[:]:
                a, b = ii[v], jj[v]
                kk = 1
                while (a // kk) != (b // kk):
                    kk *= 2
                lev.append(kk // 2)  # side of the off-diagonal child containing v
            lev = np.array(lev)
            levs = {int(u): int(np.count_nonzero(lev == u)) for u in np.unique(lev)}
            print(f"  excursion at diag x={x} scale={sc}{' (tail)' if sc==B else ''}: core labels {sel.sum()}, "
                  f"T in [{Tp.min()},{Tp.max()}], by off-diagonal block side {levs}")
    print(f"total {time.time()-t0:.1f}s")


if __name__ == '__main__':
    main()
