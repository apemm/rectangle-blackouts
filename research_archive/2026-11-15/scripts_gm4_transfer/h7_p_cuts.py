"""Sanity check: excursion cuts for the H7 profile P system (cand version).

Usage: py -I h7_p_cuts.py Q M sigma c
Labels are all cells (i, j) of the Q-square, odd row a0 + 28 i, even row b0 + 28 j,
c = b0 - a0 (odd, |c| <= 27).  Columns x = S (M r + xi), S = 6272 sigma.
A cand constraint (r, r+d, delta): a cross pair with Y = |c + 28 U| and
(S q)^2 + Y^2 = L^2, q = M d + delta, |delta| <= M - 1.  No strip test, no owner test.
Reports: number of constraints, constraints across a diagonal-cell cut, constraints
joining non-consecutive links of one excursion, opposite-sign constraints.
"""
import sys, time
import numpy as np
import numba as nb

D = 28


def hilbert(q):
    xs = np.zeros(1, dtype=np.int64)
    ys = np.zeros(1, dtype=np.int64)
    n = 1
    while n < q:
        x, y = xs, ys
        xs = np.concatenate([y, x, x + n, 2 * n - 1 - y])
        ys = np.concatenate([x, y + n, y + n, n - 1 - x])
        n *= 2
    return xs, ys


@nb.njit(cache=True)
def vectors(ymax, S):
    out = np.zeros((200000, 2), dtype=np.int64)
    k = 0
    for Y in range(1, ymax + 1, 2):
        Y2 = Y * Y
        for u in range(1, Y, 2):
            if Y2 % u == 0:
                w = Y2 // u
                X = (w - u) // 2
                if X % S == 0:
                    out[k, 0] = X // S
                    out[k, 1] = Y
                    k += 1
    return out[:k]


@nb.njit(cache=True)
def scan(ii, jj, d, yv, c, out_r):
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
            Y = c + D * (je - io)
            if Y < 0:
                Y = -Y
            if Y == yv:
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
    start = np.zeros(n + 1, dtype=np.int64)
    for k in range(m):
        deg[er[k]] += 1; deg[es[k]] += 1
        start[er[k] + 1] += 1; start[es[k] + 1] += 1
    for v in range(n):
        start[v + 1] += start[v]
    pos = start[:-1].copy()
    adj = np.zeros(2 * m, dtype=np.int64)
    for k in range(m):
        adj[pos[er[k]]] = es[k]; pos[er[k]] += 1
        adj[pos[es[k]]] = er[k]; pos[es[k]] += 1
    alive = np.ones(n, dtype=np.bool_)
    stack = np.zeros(n, dtype=np.int64); top = 0
    for v in range(n):
        if deg[v] < M:
            alive[v] = False; stack[top] = v; top += 1
    while top > 0:
        top -= 1; v = stack[top]
        for p in range(start[v], start[v + 1]):
            w = adj[p]
            if alive[w]:
                deg[w] -= 1
                if deg[w] < M:
                    alive[w] = False; stack[top] = w; top += 1
    return alive


def main():
    Q = int(sys.argv[1]); M = int(sys.argv[2]); sigma = int(sys.argv[3]); c = int(sys.argv[4])
    S = 6272 * sigma
    t0 = time.time()
    ii, jj = hilbert(Q)
    if len(sys.argv) > 5 and sys.argv[5] == "swap":
        ii, jj = jj, ii
    N = Q * Q
    vecs = vectors(abs(c) + D * Q, S)
    buf = np.zeros(N, dtype=np.int64)
    R = []; DD = []; DL = []
    for (q, Y) in vecs:
        for d in sorted({q // M, -(-q // M)}):
            if d < 1 or d >= N:
                continue
            delta = q - M * d
            if abs(delta) > M - 1:
                continue
            k = scan(ii, jj, d, Y, c, buf)
            if k:
                R.append(buf[:k].copy()); DD.append(np.full(k, d)); DL.append(np.full(k, delta))
    if not R:
        print(f"Q={Q} M={M} sigma={sigma} c={c}: vectors={len(vecs)} constraints=0")
        return
    r = np.concatenate(R); d = np.concatenate(DD); dl = np.concatenate(DL)
    key = (r * (N + 1) + d) * 64 + (dl + 32)
    _, idx = np.unique(key, return_index=True)
    r = r[idx]; d = d[idx]; s = r + d
    diag = (ii == jj)
    piece = np.cumsum(diag) - 1
    cross = int(np.count_nonzero(piece[r] != piece[s]))
    # link index inside an excursion: offset 0 is the diagonal cell, then links of
    # sizes 1, 4, 16, ... (staircase) and finally O2; link of offset o >= 1 is the
    # least a with 1 + (4^a - 1)/3 > o - ... computed from cumulative sizes.
    starts = np.flatnonzero(diag)
    off = np.arange(N) - starts[piece]
    # cumulative boundaries 1, 2, 6, 22, 86, ... : link a covers [1 + (4^a-1)/3, 1 + (4^(a+1)-1)/3)
    link = np.zeros(N, dtype=np.int64)
    a = 0
    while True:
        lo = 1 + (4 ** a - 1) // 3
        if lo >= N:
            break
        link[off >= lo] = a
        a += 1
    same = piece[r] == piece[s]
    far_links = int(np.count_nonzero(same & (np.abs(link[r] - link[s]) >= 2)))
    T = jj - ii
    opp = int(np.count_nonzero(T[r] * T[s] <= 0))
    mint = int(np.min(np.minimum(np.abs(T[r]), np.abs(T[s]))))
    ratio = float(np.max(d / (np.minimum(np.abs(T[r]), np.abs(T[s])) + 0.5) ** 2))
    print(f"Q={Q} M={M} sigma={sigma} c={c}: vectors={len(vecs)} constraints={len(r)} "
          f"cut-crossing={cross} non-consecutive-links={far_links} opposite-sign={opp} "
          f"min|T|={mint} max d/(min|T|+.5)^2={ratio:.4f} time={time.time()-t0:.1f}s")
    alive = weighted_core(N, r, s, M)
    print(f"   weighted {M}-core: {int(alive.sum())} labels")


if __name__ == '__main__':
    main()
