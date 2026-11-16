"""Exact check of the dense barrier (Barrier 2) for the Lambda3 candidate hypergraph.
Labels P_p, g_p (p < m).  Slots sigma(P_p) = s0 + p a, sigma(g_p) = sigma(P_p) + M.
P_p = (i0 - p M K, j0 - p M K), g_p = (i0 - p M K + 1, j0 - p M K), 2(j0-i0)+1 = a.
Claim: every pair satisfies Lemma 0 (and (1)), every ordered (p,q), p != q, is a
tilted cross-parity right angle (V = odd pt of P_p, F = odd pt of P_q, G = even pt
of g_p) with fourth corner in the strip; every label has degree >= m-1."""
import sys, json, math
import numpy as np

def run(S, M, a, h):
    K = S * S // 2
    assert a % 2 == 1 and math.gcd(a, M) == 1
    # largest m with (n M K + 1)^2 < 4 (n a / M - 2) for all 1 <= n <= m-1
    m = 2
    while True:
        n = m  # test adding one more point
        if (n * M * K + 1) ** 2 < 4 * (n * a / M - 2):
            m += 1
        else:
            break
    i0 = (m - 1) * M * K
    j0 = i0 + (a - 1) // 2
    h = max(h, 2 * j0 + 2)
    s0 = 0
    p = np.arange(m, dtype=np.int64)
    sP = s0 + p * a
    sg = sP + M
    slots = np.concatenate([sP, sg])
    rank = slots // M
    I = np.concatenate([i0 - p * M * K, i0 - p * M * K + 1])
    J = np.concatenate([j0 - p * M * K, j0 - p * M * K])
    n = 2 * m
    assert len(set(rank.tolist())) == n
    assert len(set(zip(I.tolist(), J.tolist()))) == n
    # pairwise locality
    ok0 = True; ok1 = True
    for k in range(n):
        t = np.abs(rank - rank[k]); sel = t > 0
        for Dc in (np.abs(I - I[k]), np.abs(J - J[k])):
            D = Dc[sel]; tt = t[sel]
            big = D >= 2
            mu = np.floor(np.log2(np.maximum(D, 1))).astype(np.int64)
            ok0 &= bool(np.all(~big | (tt > 4.0 ** (mu - 1))))
            ok1 &= bool(np.all(D * D < 16 * tt))
    # right angles
    X = S * slots
    odd = 2 * I + 1
    even = 2 * J + 2
    P_, Q_ = np.meshgrid(p, p, indexing='ij')
    msk = P_ != Q_
    P_, Q_ = P_[msk], Q_[msk]
    Vx, Vy = X[P_], odd[P_]
    Fx, Fy = X[Q_], odd[Q_]
    Gx, Gy = X[m + P_], even[m + P_]
    dot = (Fx - Vx) * (Gx - Vx) + (Fy - Vy) * (Gy - Vy)
    tilted = (Fx != Vx) & (Gx != Vx) & (Fy != Vy) & (Gy != Vy)
    Wy = Fy + Gy - Vy
    instrip = (Wy >= 1) & (Wy <= h) & (Vy >= 1) & (Fy >= 1) & (Gy <= h)
    ev = int(np.sum((dot == 0) & tilted & instrip))
    # normal-form a of Theorem 1 and its threshold
    return dict(S=S, M=M, a=a, h=h, m=m, labels=n, lemma0_all_pairs=ok0,
                hilbert1_all_pairs=ok1, events=ev, expected=m * (m - 1),
                min_degree=int(m - 1), weighted_density=round(3 * ev / n, 2),
                pred_16a_over_M3S4=round(16 * a / (M ** 3 * S ** 4), 1),
                a_over_MS4_16=round(a / (M * S ** 4 / 16), 1))

out = []
for (S, M, a, h) in [(8, 1, 200001, 200400), (8, 2, 200001, 200400), (8, 3, 200003, 200400), (16, 1, 2000001, 2000200)]:
    out.append(run(S, M, a, h))
print(json.dumps(out, indent=1))
