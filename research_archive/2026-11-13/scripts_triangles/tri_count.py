"""Sanity check for the cross-direction triangle count.
P_h = {(X,y): 0<|y|<h, X != 0, X^2+y^2 a square}  (|X| <= y^2/2 automatically).
Sigma(tau) = #{(z1,z2) in P^2 : z3 = z2 - z1 + (0,tau) in P, and not collinear when tau=0}.
Also: split by whether some edge is 'flat' (|X| >= h^(1+a)).
"""
import sys, time, math
import numpy as np

def pyth_set(h):
    pts = []
    for y in range(1, h):
        y2 = y * y
        for d in range(1, y):
            if y2 % d == 0:
                e = y2 // d
                if (e - d) % 2 == 0:
                    X = (e - d) // 2
                    for sx in (1, -1):
                        for sy in (1, -1):
                            pts.append((sx * X, sy * y))
    return np.array(pts, dtype=np.int64)

def run(h, taus, a=0.25):
    P = pyth_set(h)
    Xmax = int(P[:, 0].max()) + 1
    M = 4 * Xmax + 10
    keys = np.sort((P[:, 0] + 2 * Xmax) * (4 * h) + (P[:, 1] + 2 * h))
    K = h ** (1 + a)
    res = {}
    for tau in taus:
        tot = 0; flat = 0
        for (X1, y1) in P:
            if X1 <= 0:
                continue
            X3 = P[:, 0] - X1
            y3 = P[:, 1] - y1 + tau
            ok = (X3 != 0) & (y3 != 0) & (np.abs(y3) < h)
            if tau == 0:
                ok &= (X1 * P[:, 1] - P[:, 0] * y1) != 0
            idx = np.nonzero(ok)[0]
            if idx.size == 0:
                continue
            k3 = (X3[idx] + 2 * Xmax) * (4 * h) + (y3[idx] + 2 * h)
            pos = np.searchsorted(keys, k3)
            pos[pos >= keys.size] = keys.size - 1
            hit = keys[pos] == k3
            sel = idx[hit]
            tot += sel.size
            if sel.size:
                fl = (abs(X1) >= K) | (np.abs(P[sel, 0]) >= K) | (np.abs(X3[sel]) >= K)
                flat += int(fl.sum())
        res[tau] = (2 * tot, 2 * flat)
    return P.shape[0], res

if __name__ == "__main__":
    t0 = time.time()
    for h in [int(s) for s in sys.argv[1:]]:
        nP, res = run(h, [0, 14, 28 * 3, h // 2])
        L = math.log(h)
        for tau, (tot, flat) in res.items():
            print(f"h={h} |P|={nP} tau={tau} Sigma={tot} flat={flat} mod={tot-flat} "
                  f"Sigma/h={tot/h:.2f} Sigma/(h L^2)={tot/(h*L*L):.3f} |P|^2/Sigma={nP*nP/max(tot,1):.1f}",
                  flush=True)
        print(f"  elapsed {time.time()-t0:.1f}s", flush=True)
