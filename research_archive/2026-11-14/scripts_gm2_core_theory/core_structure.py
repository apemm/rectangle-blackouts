"""Structure of the weighted M-core K of G_B^o: factors, signs, diagonals, gains, parallels.
Usage: py -B core_structure.py B S M orient"""
import sys
from collections import defaultdict, Counter
import numpy as np
import cert_core as cc


def build_full(B, S, M, orient):
    """Like cc.build but keeps (q, Y, a, role) for each triple (owner outside block)."""
    xy = cc.hilbert_array(B)
    if orient == "swap":
        xy = xy[:, ::-1].copy()
    x, y = xy[:, 0], xy[:, 1]
    odd, even = 2 * x + 1, 2 * y + 2
    Ymax = 2 * B - 1
    legs = defaultdict(dict)
    for Y in range(1, Ymax + 1, 2):
        Y2 = Y * Y
        for u in range(1, Y, 2):
            if Y2 % u:
                continue
            w = Y2 // u
            X, L = (w - u) // 2, (w + u) // 2
            if X > 0 and X % S == 0:
                legs[X][Y] = L
    info = defaultdict(set)
    N = B * B
    for X, ys in legs.items():
        q = X // S
        hyp = np.zeros(Ymax + 2, dtype=np.int64)
        for Y, L in ys.items():
            hyp[Y] = L
        for d in {q // M, -(-q // M)} - {0}:
            delta = q - M * d
            if abs(delta) > M - 1 or d >= N:
                continue
            for role, (r1, r2) in enumerate(((odd[:-d], even[d:]), (even[:-d], odd[d:]))):
                sgn = (r2 - r1)
                yy = np.abs(sgn)
                ok = yy <= Ymax
                yc = np.where(ok, yy, 0)
                L = np.where(ok, hyp[yc], 0)
                idx = np.nonzero(L > 0)[0]
                if not len(idx):
                    continue
                Lh = L[idx]
                s1 = r1[idx] + r2[idx]
                c1, c2 = (s1 - Lh) // 2, (s1 + Lh) // 2
                co = np.where(c1 % 2 == 1, c1, c2)
                ce = np.where(c1 % 2 == 1, c2, c1)
                ins = (co >= 1) & (ce >= 2) & ((co - 1) // 2 < B) & ((ce - 2) // 2 < B)
                for k in np.nonzero(~ins)[0].tolist():
                    rr = int(idx[k])
                    Y = int(yc[rr])
                    Lv = int(L[rr])
                    a = (Lv - Y) // 2
                    eta = 1 if sgn[rr] > 0 else -1
                    info[(rr, rr + d, delta)].add((q, Y, a, eta, role))
    return info, x, y


def main():
    B, S, M, orient = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    info, x, y = build_full(B, S, M, orient)
    keys = list(info)
    K = cc.peel(keys, M, lambda r, u, dl, side: (u, dl) if side == 0 else (r, dl))
    EK = [k for k in keys if k[0] in K and k[1] in K]
    T = (y - x)
    print(f"B={B} {orient}: |K|={len(K)} |E(K)|={len(EK)}")
    # witnesses per triple
    print(" witnesses per triple:", Counter(len(info[k]) for k in EK).most_common(5))
    # parallel constraints per unordered pair
    pair = defaultdict(set)
    for (r, u, dl) in EK:
        pair[(r, u)].add(dl)
    print(" pairs:", len(pair), " multiplicity:", sorted(Counter(len(v) for v in pair.values()).items()))
    print(" residue sets of multi-pairs:", Counter(tuple(sorted({d % M for d in v})) for v in pair.values() if len(v) > 1).most_common(6))
    # per-label degree, distinct gaps, distinct factors
    deg = Counter(); gaps = defaultdict(set); facs = defaultdict(set); vecs = defaultdict(set)
    for k in EK:
        r, u, dl = k
        for (q, Y, a, eta, role) in info[k]:
            for v in (r, u):
                gaps[v].add(q); facs[v].add(a); vecs[v].add((q, Y))
        deg[r] += 1; deg[u] += 1
    print(" degree dist:", sorted(Counter(deg.values()).items()))
    print(" distinct gaps per label:", sorted(Counter(len(gaps[v]) for v in K).items()))
    print(" distinct factors per label:", sorted(Counter(len(facs[v]) for v in K).items()))
    allvec = Counter()
    for k in EK:
        for (q, Y, a, eta, role) in info[k]:
            allvec[(q, Y, a)] += 1
    print(" distinct vectors (q,Y) in K:", len(allvec), " top:", allvec.most_common(8))
    fa = Counter()
    for (q, Y, a), c in allvec.items():
        fa[a] += c
    print(" factor mass (a: edges) top:", fa.most_common(12))
    # near-isosceles: L = X+1  <=> a = (Y-1)^2/4
    iso = sum(c for (q, Y, a), c in allvec.items() if 4 * a == (Y - 1) ** 2)
    print(" edges from near-isosceles vectors (L = X+1):", iso, "of", sum(allvec.values()))
    # gain-0 subgraph: components and bipartiteness
    adj0 = defaultdict(list)
    for (r, u, dl) in EK:
        if dl % M == 0:
            adj0[r].append(u); adj0[u].append(r)
    col = {}; nonbip = 0; ncomp = 0; sizes = []
    for s in adj0:
        if s in col:
            continue
        ncomp += 1; col[s] = 0; st = [s]; sz = 0; bad = False
        while st:
            v = st.pop(); sz += 1
            for w in adj0[v]:
                if w not in col:
                    col[w] = 1 - col[v]; st.append(w)
                elif col[w] == col[v]:
                    bad = True
        sizes.append(sz); nonbip += bad
    print(" gain-0 subgraph: comps", ncomp, "non-bipartite", nonbip, "largest", sorted(sizes)[-3:])
    # T range of K and rank range
    Ts = [int(T[v]) for v in K]
    print(" T range in K:", min(Ts), max(Ts), " |T| quartiles:", np.percentile(np.abs(Ts), [25, 50, 75, 100]).tolist())
    # Lemma C check: nonzero gain only with 3 | Y (when 3 | M)
    if M % 3 == 0:
        bad = sum(1 for k in EK for (q, Y, a, eta, role) in info[k] if k[2] % 3 != 0 and Y % 3 != 0)
        print(" Lemma C violations (delta != 0 mod 3 with 3 not | Y):", bad)


if __name__ == "__main__":
    main()
