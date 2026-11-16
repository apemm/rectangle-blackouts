# Random king-continuous quadtree curve (RQC). Sanity tools only.
import itertools, random
import numpy as np

CORN = [(0,0),(1,0),(1,1),(0,1)]          # local corners / quadrants
TYPES = [(a,w) for a in CORN for w in CORN if a != w]   # 12 types

def pts(q):  # corner points (3x3 grid) of quadrant q
    return {(q[0]+cx, q[1]+cy) for (cx,cy) in CORN}

def configs(tau, child_side):
    """All (prob, order, child_types) for a node of type tau whose children have side child_side."""
    a, w = tau
    mids = [q for q in CORN if q != a and q != w]
    out = []
    for mo in (mids, mids[::-1]):
        order = [a, mo[0], mo[1], w]
        if child_side == 1:
            out.append((0.5, order, [None]*4))
            continue
        P0 = (2*a[0], 2*a[1]); P4 = (2*w[0], 2*w[1])
        S1 = pts(order[0]) & pts(order[1]); S2 = pts(order[1]) & pts(order[2]); S3 = pts(order[2]) & pts(order[3])
        trip = [(p1,p2,p3) for p1 in S1 for p2 in S2 for p3 in S3 if p1 != p2 and p2 != p3]
        for (p1,p2,p3) in trip:
            P = [P0,p1,p2,p3,P4]
            ct = []
            for t in range(4):
                q = order[t]
                ent = (P[t][0]-q[0], P[t][1]-q[1]); ex = (P[t+1][0]-q[0], P[t+1][1]-q[1])
                assert ent in CORN and ex in CORN and ent != ex
                ct.append((ent, ex))
            out.append((0.5/len(trip), order, ct))
    return out

def sample_curve(n, rng, root=((0,0),(1,0))):
    """Return array H of shape (4^n, 2): cell at each rank, side 2^n."""
    def rec(x0, y0, k, tau, outl):
        if k == 0:
            outl.append((x0, y0)); return
        s = 1 << (k-1)
        cf = configs(tau, s)
        u = rng.random(); acc = 0.0
        for (p, order, ct) in cf:
            acc += p
            if u <= acc: break
        for t in range(4):
            q = order[t]
            rec(x0 + q[0]*s, y0 + q[1]*s, k-1, ct[t] if ct[t] is not None else ((0,0),(1,0)), outl)
    outl = []
    rec(0, 0, n, root, outl)
    return np.array(outl, dtype=np.int64)

if __name__ == "__main__":
    import sys
    rng = random.Random(1)
    for n in (4, 6):
        for trial in range(3):
            H = sample_curve(n, rng)
            N = len(H)
            assert len({tuple(c) for c in H}) == N
            step = np.abs(np.diff(H, axis=0)).max()
            # locality (1) and Lemma 0 on all pairs
            worst = 0.0; bad0 = 0
            for r in range(N):
                d = np.abs(H[r+1:] - H[r]).max(axis=1)
                t = np.arange(1, N - r)
                worst = max(worst, float((d**2 / t).max()) if len(t) else 0)
                # Lemma 0: |D| >= 2^m => t > 4^(m-1)
                m = np.floor(np.log2(np.maximum(d, 1))).astype(int)
                bad0 += int(((d >= 2) & (t <= 4.0**(m-1))).sum())
            print(n, trial, "max king step", step, "max D^2/t", round(worst, 3), "Lemma0 violations", bad0)
