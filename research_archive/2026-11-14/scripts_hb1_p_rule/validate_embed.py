"""Check (1) main-diagonal aligned blocks of H_Q are id- or swap-oriented,
(2) the local block system equals the global candidate constraints
restricted to a mid-strip main-diagonal block (with owner outside it)."""
import numpy as np
from diag_block import hilbert_array
from diag_fast import build

Q = 2048
h = 2 * Q
S, M = 32, 3
H = hilbert_array(Q)
rank = np.empty((Q, Q), dtype=np.int64)
rank[H[:, 0], H[:, 1]] = np.arange(Q * Q)

# (1) orientation lemma for several block sizes
for B in (2, 4, 8, 16, 32, 64, 128):
    base_id = hilbert_array(B)
    kinds = set()
    for I in range(Q // B):
        sub = rank[I * B:(I + 1) * B, I * B:(I + 1) * B]
        lo = sub.min()
        assert sub.max() - lo == B * B - 1
        loc = H[lo:lo + B * B] - I * B
        if np.array_equal(loc, base_id):
            kinds.add("id")
        elif np.array_equal(loc, base_id[:, ::-1]):
            kinds.add("swap")
        else:
            raise SystemExit(f"bad orientation B={B} I={I}")
    print(f"B={B}: all {Q//B} main-diagonal blocks are {sorted(kinds)}")

# (2) embedding check for B=32 at a mid-strip block of each orientation
B = 32
odd_g, even_g = 2 * H[:, 0] + 1, 2 * H[:, 1] + 2
for target in ("id", "swap"):
    loc_id = hilbert_array(B)
    for I in range(24, 46):
        sub = rank[I * B:(I + 1) * B, I * B:(I + 1) * B]
        lo = int(sub.min())
        loc = H[lo:lo + B * B] - I * B
        kind = "id" if np.array_equal(loc, loc_id) else "swap"
        if kind == target:
            break
    n, Eloc = build(B, S, M, target)
    loc_set = set(map(tuple, (Eloc + np.array([lo, lo, 0])).tolist()))
    glob = set()
    for r in range(lo, lo + B * B):
        for s in range(r + 1, lo + B * B):
            d = s - r
            if d > 43:
                break
            for delta in range(1 - M, M):
                X = S * (M * d + delta)
                if X <= 0 or X >= h:
                    continue
                for a, b in ((odd_g[s], even_g[r]), (odd_g[r], even_g[s])):
                    Y = abs(int(b) - int(a))
                    L2 = X * X + Y * Y
                    L = int(np.sqrt(L2))
                    while L * L < L2:
                        L += 1
                    if L * L != L2 or L > h - 1:
                        continue
                    sm = int(a) + int(b)
                    lo_r, hi_r = (sm - L) // 2, (sm + L) // 2
                    if lo_r < 1 or hi_r > h:
                        continue
                    oo, ee = (lo_r, hi_r) if lo_r % 2 else (hi_r, lo_r)
                    oi, oj = (oo - 1) // 2, (ee - 2) // 2
                    if I * B <= oi < (I + 1) * B and I * B <= oj < (I + 1) * B:
                        continue
                    glob.add((r, s, delta))
        if X > h:  # noqa: harmless
            pass
    print(f"{target}: block I={I}, local={len(loc_set)} global={len(glob)} equal={loc_set == glob}")
