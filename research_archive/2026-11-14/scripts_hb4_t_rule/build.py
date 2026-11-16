"""Build the in-strip P candidate system (archive definition) with factor data.
Outputs an npz with arrays r, s, delta, a (smaller half-factor), Y, role, and
label coordinates per rank. Sanity tool only."""
import sys, math
import numpy as np

def hilbert_array(q):
    xy = np.zeros((1, 2), dtype=np.int64); n = 1
    while n < q:
        b = n * n
        nxt = np.empty((4 * b, 2), dtype=np.int64)
        nxt[:b] = xy[:, ::-1]
        nxt[b:2 * b] = xy + (0, n)
        nxt[2 * b:3 * b] = xy + (n, n)
        nxt[3 * b:, 0] = 2 * n - 1 - xy[:, 1]
        nxt[3 * b:, 1] = n - 1 - xy[:, 0]
        xy = nxt; n *= 2
    return xy

def divisors_of_square(N):
    f = {}; m = N; p = 2
    while p * p <= m:
        while m % p == 0:
            f[p] = f.get(p, 0) + 1; m //= p
        p += 1
    if m > 1: f[m] = f.get(m, 0) + 1
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** k for d in ds for k in range(2 * e + 1)]
    return ds

def legs(X, h):
    """odd y>0 with X^2+y^2=L^2, L<=h-1 ; returns {y:(L,a)}"""
    N = X // 2; out = {}
    for a in divisors_of_square(N):
        b = N * N // a
        if a < b and (b - a) % 2 == 1 and a + b <= h - 1:
            out[b - a] = (a + b, a)
    return out

def build(h, M, S):
    A, K = (h + 1) // 2, h // 2
    q = 1 << (max(A, K) - 1).bit_length()
    xy = hilbert_array(q)
    active = (xy[:, 0] < A) & (xy[:, 1] < K)
    odd, even = 2 * xy[:, 0] + 1, 2 * xy[:, 1] + 2
    R, Sx, D, AF, YY, RO = [], [], [], [], [], []
    for d in range(1, ((h - 1) // S + M - 1) // M + 1):
        for delta in range(1 - M, M):
            gq = M * d + delta
            if gq <= 0: continue
            X = S * gq
            if X >= h: continue
            ys = legs(X, h)
            if not ys: continue
            hyp = np.zeros(2 * q + 2, dtype=np.int64); fac = np.zeros(2 * q + 2, dtype=np.int64)
            for y, (L, a) in ys.items():
                if y < len(hyp): hyp[y] = L; fac[y] = a
            for role, (r1, r2) in enumerate(((odd[:-d], even[d:]), (even[:-d], odd[d:]))):
                y = np.abs(r2 - r1)
                L = hyp[y]; ssum = r1 + r2
                hit = (L > 0) & (ssum - L >= 2) & (ssum + L <= 2 * h) & active[:-d] & active[d:]
                idx = np.nonzero(hit)[0]
                R.append(idx); Sx.append(idx + d); D.append(np.full(len(idx), delta))
                AF.append(fac[y[idx]]); YY.append(y[idx]); RO.append(np.full(len(idx), role))
    cat = lambda z: np.concatenate(z) if z else np.zeros(0, dtype=np.int64)
    return dict(r=cat(R), s=cat(Sx), delta=cat(D), a=cat(AF), Y=cat(YY), role=cat(RO),
                i=xy[:, 0], j=xy[:, 1], active=active, h=h, M=M, S=S)

if __name__ == "__main__":
    h, M, S = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    out = build(h, M, S)
    np.savez_compressed(sys.argv[4], **out)
    print("constraint rows", len(out["r"]),
          "distinct triples", len(set(zip(out["r"].tolist(), out["s"].tolist(), out["delta"].tolist()))))
