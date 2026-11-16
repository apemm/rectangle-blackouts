"""Sanity check: cross-block even-even A2 (S5) pairs in a Route-L-like region.

Model: one type tau=(iota,sigma); pieces (s, r) with i = r mod Q, r = iota mod 32;
one class per piece (all slots of the piece, g = 1); rule n(c) = kappa_rho mod 16 l
with rho = j-residue mod Q. Route L: kappa_rho random in disjoint windows.
Control: kappa_rho = kappa for all rho (L***-like), where Prop 1(d) predicts 0.
Counts label pairs C, D (even points) in blocks t, t+Dt (|Dt| <= h/320) with
4 delta^2 + eps^2 a square (Lemma A2), and checks the witness slots.
"""
import sys, math, random
import numpy as np

def isprime(n):
    if n < 2: return False
    for q in range(2, int(n**0.5) + 1):
        if n % q == 0: return False
    return True

def run(h, Q, mode, samples, seed):
    rnd = random.Random(seed)
    A = (h + 1) // 2; K = h // 2
    iota, sigma, kap, b = 1, 0, 0, 0
    # primes
    ls = [l for l in range(int(1.04*h)+1, int(2.08*h)+1) if l % 5 in (2, 3) and isprime(l)]
    ps = [p for p in range(40*h+1, 40*h+4000) if p % 20 in (3, 7) and isprime(p)]
    l = rnd.choice(ls); p = rnd.choice(ps)
    M = 16*l
    pinv = pow(p, -1, M)
    # diagonals of the type: s = j - i, s in [-(A-1), K-1], s = sigma mod 16
    S = [s for s in range(-(A-1), K) if s % 16 == sigma % 16]
    rhos = sorted(set((r + s) % Q for s in S for r in range(iota % 32, Q, 32)))
    n = len(rhos)
    if mode == 'L':
        W = int(15.0*h) // n  # window length (integers)
        kap_rho = {}
        for k, rho in enumerate(rhos):
            lo = -int(7.5*h) + k*W
            v = lo + rnd.randrange(W)
            v -= (v - kap) % 16
            kap_rho[rho] = v
    else:
        kap_rho = {rho: kap for rho in rhos}
    # stacks keyed by X = s - kappa_rho
    stacks = {}
    for s in S:
        for r in range(iota % 32, Q, 32):
            rho = (r + s) % Q
            X = s - kap_rho[rho]
            stacks.setdefault(X, []).append((s, r, rho))
    for X in stacks: stacks[X].sort(key=lambda z: z[2])
    keys = list(stacks.keys())
    def centered(v):
        v %= M
        return v - M if v > M//2 else v
    def piece_at(t):
        x = t % M; k = t // M
        X = centered(p*x + b)
        st = stacks.get(X)
        if st is None or k >= len(st): return None
        return st[k]
    def t_of(X, k):
        return (pinv*((X - b) % M)) % M + M*k
    reach = h // 320
    dts = [d for d in range(-reach, reach+1) if d != 0 and d % 16 == 0]
    hits = 0; wit_label = 0; pairs_checked = 0; labels_seen = 0; diffrho = 0
    for _ in range(samples):
        X = rnd.choice(keys); st = stacks[X]; k = rnd.randrange(len(st))
        s, r, rho = st[k]
        t = t_of(X, k)
        iC = np.arange(r, A, Q, dtype=np.int64)
        nC = iC + p*t + b; jC = iC + s
        labels_seen += len(iC)
        for dt in dts:
            pc = piece_at(t + dt)
            if pc is None: continue
            s2, r2, rho2 = pc
            iD = np.arange(r2, A, Q, dtype=np.int64)
            nD = iD + p*(t+dt) + b; jD = iD + s2
            delta = nD[None, :] - nC[:, None]
            eps = jD[None, :] - jC[:, None]
            v = 4*delta*delta + eps*eps
            rt = np.floor(np.sqrt(v.astype(np.float64))).astype(np.int64)
            ok = np.zeros(v.shape, bool)
            for d in (-1, 0, 1):
                rr = rt + d
                ok |= (rr*rr == v)
            ok &= (eps != 0)
            pairs_checked += v.size
            c = int(ok.sum())
            if c:
                hits += c
                if rho2 != rho: diffrho += c
                # witness slots n_{A,B} = (nC + nD -/+ L)/2, L = L'/2
                ci, di = np.nonzero(ok)
                for a_, d_ in zip(ci, di):
                    Lp = int(math.isqrt(int(v[a_, d_]))); L = Lp // 2
                    nA = (int(nC[a_]) + int(nD[d_]) - L) // 2
                    nB = (int(nC[a_]) + int(nD[d_]) + L) // 2
                    for nw in (nA, nB):
                        tw = (nw - b) // p; iw = nw - b - p*tw
                        pw = piece_at(tw) if 0 <= iw < A else None
                        if pw is not None and (iw - pw[1]) % Q == 0:
                            wit_label += 1
    return dict(h=h, Q=Q, mode=mode, l=l, p=p, n_rho=n, samples=samples,
                labels=labels_seen, pairs=pairs_checked, hits=hits,
                diffrho=diffrho, witness_label_cols=wit_label,
                hits_per_label=hits/max(1, labels_seen))

if __name__ == '__main__':
    h = int(sys.argv[1]); Q = int(sys.argv[2]); mode = sys.argv[3]
    samples = int(sys.argv[4]); seed = int(sys.argv[5])
    print(run(h, Q, mode, samples, seed))
