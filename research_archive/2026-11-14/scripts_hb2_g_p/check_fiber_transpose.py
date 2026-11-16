import numpy as np, sys, math

def hilbert(q):
    # recursion (2) of continuation_hilbert_placement.md
    pts = np.zeros((1, 2), dtype=np.int64)
    s = 1
    while s < q:
        x = pts[:, 0]; y = pts[:, 1]
        a = np.stack([y, x], 1)
        b = np.stack([x, y + s], 1)
        c = np.stack([x + s, y + s], 1)
        d = np.stack([2 * s - 1 - y, s - 1 - x], 1)
        pts = np.concatenate([a, b, c, d])
        s *= 2
    return pts

q = 256
H = hilbert(q)
N = q * q
# locality check (1) on a sample
rng = np.random.default_rng(1)
for _ in range(20000):
    r, s = rng.integers(0, N, 2)
    if r == s: continue
    assert max((H[r] - H[s]) ** 2) < 16 * abs(int(r) - int(s))

# Lemma F: max over intervals [a, a+D) of max fiber of one coordinate, ratio to sqrt(D)
worst = 0.0
for D in [1, 2, 3, 5, 8, 16, 31, 64, 100, 256, 1000, 1024, 4096, 5000, 16384]:
    w = 0.0
    starts = rng.integers(0, N - D, 300)
    for a in list(starts) + [0, 1, N // 4 - D // 2 if N // 4 > D else 0]:
        seg = H[a:a + D]
        for c in (0, 1):
            cnt = np.bincount(seg[:, c] - seg[:, c].min()).max()
            w = max(w, cnt / math.sqrt(D))
    worst = max(worst, w)
    print("D", D, "max fiber/sqrt(D)", round(w, 3))
print("overall worst ratio", worst)

# Transposition identity: for each aligned block of length 4q'^2 (q'=2^m), ranks in first quarter,
# j_{r+q'^2} - i_r and j_r - i_{r+q'^2} constant
bad = 0
for m in range(0, 7):
    qq = 2 ** m
    L = 4 * qq * qq
    for B0 in range(0, N, L):
        r = np.arange(B0, B0 + qq * qq)
        f = r + qq * qq
        v1 = H[f, 1] - H[r, 0]
        v2 = H[r, 1] - H[f, 0]
        if len(set(v1.tolist())) != 1 or len(set(v2.tolist())) != 1:
            bad += 1
        # offset relative to block origin
        O = H[B0:B0 + L].min(0)
        c1 = v1[0] - (O[1] - O[0]); c2 = v2[0] - (O[1] - O[0])
        assert c1 in (0, qq, -qq) and c2 in (0, qq, -qq), (m, c1, c2)
print("transposition identity failures:", bad)

# per-diagonal fiber at d = 4^m over the whole square vs mean
for m in range(2, 7):
    d = 4 ** m
    r = np.arange(0, N - d)
    t = H[r + d, 1] - H[r, 0]
    cnt = np.bincount(t - t.min())
    print("d", d, "max fiber", cnt.max(), "mean nonzero fiber", round(cnt[cnt > 0].mean(), 1),
          "ratio max/(q*sqrt d)", round(cnt.max() / (q * math.sqrt(d)), 3))
