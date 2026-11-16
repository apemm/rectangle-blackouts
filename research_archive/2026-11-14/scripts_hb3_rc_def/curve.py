"""Random CGK curves: generation, locality checks, Hilbert comparison."""
import random, sys
import numpy as np
from table import TABLE, GATES, bits

def base_orders(g):
    gin, gout = g
    mids = [c for c in range(4) if c not in (gin, gout)]
    return [(gin, mids[0], mids[1], gout), (gin, mids[1], mids[0], gout)]

def build(n, g, rng, hilbert=False):
    """Return array cells[r] = (x, y) for the 2^n square with gate g."""
    out = []
    def rec(x0, y0, side, gate):
        if side == 1:
            out.append((x0, y0)); return
        s = side // 2
        if side == 2:
            orders = base_orders(gate)
            if hilbert:
                order = [o for o in orders if all(bin(o[k] ^ o[k + 1]).count('1') == 1 for k in range(3))][0]
            else:
                order = rng.choice(orders)
            for c in order:
                cx, cy = bits(c)
                out.append((x0 + cx, y0 + cy))
            return
        R = TABLE[gate]
        if hilbert:
            # Hilbert: image of the canonical refinement under the symmetry; pick the all-A U-shape
            cand = [w for w in R if all((bin(a ^ b).count('1') == 1) for a, b in w[1])]
            w = cand[0]
        else:
            w = rng.choice(R)
        order, cg = w
        for c, gg in zip(order, cg):
            cx, cy = bits(c)
            rec(x0 + cx * s, y0 + cy * s, s, gg)
    rec(0, 0, 1 << n, g)
    return np.array(out, dtype=np.int64)

def check(cells, n, exhaustive_limit=1 << 12, samples=200000, rng=None):
    q = 1 << n
    N = q * q
    # bijection
    flat = cells[:, 0] * q + cells[:, 1]
    assert len(set(flat.tolist())) == N
    # king steps
    st = np.abs(np.diff(cells, axis=0)).max(axis=1)
    assert st.max() == 1 and st.min() == 1, (st.max(), st.min())
    # quadtree: each aligned 4^j block is an aligned square
    for j in range(1, n + 1):
        b = 4 ** j
        blk = cells.reshape(-1, b, 2)
        mn = blk.min(axis=1); mx = blk.max(axis=1)
        assert np.all(mx - mn == (1 << j) - 1)
        assert np.all(mn % (1 << j) == 0)
    # locality max(D^2) < 16 t and Lemma 0
    worst = 0.0
    viol0 = 0
    def test(r, s):
        nonlocal worst, viol0
        t = abs(s - r)
        D = np.abs(cells[s] - cells[r]).max()
        worst = max(worst, D * D / t)
        if D >= 2:
            m = int(D).bit_length() - 1  # 2^m <= D
            if not (t > 4 ** (m - 1)):
                viol0 += 1
    if N <= exhaustive_limit:
        for r in range(N):
            for s in range(r + 1, N):
                test(r, s)
    else:
        rng = rng or random.Random(1)
        for _ in range(samples):
            r = rng.randrange(N)
            # log-uniform gaps
            t = int(2 ** rng.uniform(0, np.log2(N - 1)))
            s = r + t
            if s >= N: s = r - t
            if s < 0 or s == r: continue
            test(r, s)
        # all consecutive-block junction pairs at every level (worst cases)
        for j in range(0, n):
            b = 4 ** j
            for r0 in range(b, N, b):
                for r in (r0 - b, r0 - 1):
                    for s in (r0, r0 + b - 1):
                        if s < N: test(r, s)
    return worst, viol0

if __name__ == '__main__':
    rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 7)
    for n in (2, 3, 4, 5):
        for trial in range(5):
            g = rng.choice(GATES)
            cells = build(n, g, rng)
            w, v = check(cells, n)
            print('n', n, 'gate', g, 'max D^2/t', round(w, 3), 'Lemma0 violations', v)
    for n in (7, 8, 9):
        g = rng.choice(GATES)
        cells = build(n, g, rng)
        w, v = check(cells, n, rng=rng)
        print('n', n, 'gate', g, 'sampled max D^2/t', round(w, 3), 'Lemma0 violations', v)
    # hilbert sanity: compare with recursion (2)
    def hil(q):
        if q == 1: return [(0, 0)]
        p = hil(q // 2); h = q // 2
        return [(y, x) for x, y in p] + [(x, y + h) for x, y in p] + [(x + h, y + h) for x, y in p] + [(q - 1 - y, h - 1 - x) for x, y in p]
    for n in (3, 5, 7):
        a = build(n, (0, 1), rng, hilbert=True)
        b = np.array(hil(1 << n))
        print('hilbert recursion (2) reproduced at n', n, bool(np.all(a == b)))
