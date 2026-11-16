"""Numba build of the main-diagonal block P system (same family as diag_core)."""
import sys
import numpy as np
import numba as nb
from diag_block import hilbert_array, legs_by_X
from diag_core import core, solve
from collections import defaultdict


@nb.njit(cache=True)
def kernel(odd, even, B, M, qs, offs, Ys, Ls, out):
    n = odd.shape[0]
    cnt = 0
    look = np.zeros(4 * B + 8, dtype=np.int64)
    for t in range(qs.shape[0]):
        q = qs[t]
        for k in range(offs[t], offs[t + 1]):
            look[Ys[k]] = Ls[k]
        d1 = q // M
        d2 = -((-q) // M)
        for dd in range(2):
            d = d1 if dd == 0 else d2
            if dd == 1 and d2 == d1:
                continue
            delta = q - M * d
            if d < 1 or d >= n or abs(delta) > M - 1:
                continue
            for r in range(n - d):
                for role in range(2):
                    if role == 0:
                        a = odd[r + d]; b = even[r]
                    else:
                        a = odd[r]; b = even[r + d]
                    y = b - a
                    if y < 0:
                        y = -y
                    L = look[y]
                    if L == 0:
                        continue
                    s = a + b
                    lo = (s - L) // 2
                    hi = (s + L) // 2
                    if lo % 2 == 1:
                        oo = lo; ee = hi
                    else:
                        oo = hi; ee = lo
                    oi = (oo - 1) // 2
                    oj = (ee - 2) // 2
                    if oi >= 0 and oi < B and oj >= 0 and oj < B:
                        continue
                    if cnt < out.shape[0]:
                        out[cnt, 0] = r
                        out[cnt, 1] = r + d
                        out[cnt, 2] = delta
                    cnt += 1
        for k in range(offs[t], offs[t + 1]):
            look[Ys[k]] = 0
    return cnt


def build(B, S, M, orient):
    xy = hilbert_array(B)
    if orient == "swap":
        xy = xy[:, ::-1]
    odd = (2 * xy[:, 0] + 1).astype(np.int64)
    even = (2 * xy[:, 1] + 2).astype(np.int64)
    legs = legs_by_X(2 * B + 1, S)
    qs, offs, Ys, Ls = [], [0], [], []
    for X in sorted(legs):
        qs.append(X // S)
        for Y, L in legs[X].items():
            Ys.append(Y); Ls.append(L)
        offs.append(len(Ys))
    out = np.zeros((6_000_000, 3), dtype=np.int64)
    cnt = kernel(odd, even, B, M, np.array(qs, dtype=np.int64), np.array(offs, dtype=np.int64),
                 np.array(Ys, dtype=np.int64), np.array(Ls, dtype=np.int64), out)
    assert cnt <= out.shape[0]
    E = np.unique(out[:cnt], axis=0)
    return B * B, E


if __name__ == "__main__":
    B, S, M, orient = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    n, E = build(B, S, M, orient)
    Ec = core(n, E, M)
    cv = len(np.unique(Ec[:, :2])) if len(Ec) else 0
    print(f"B={B} S={S} M={M} {orient}: constraints={len(E)} avgdeg={2*len(E)/n:.4f} "
          f"{M}-core: vertices={cv} constraints={len(Ec)}")
    for k in range(M + 1, M + 4):
        Ek = core(n, E, k)
        print(f"  {k}-core constraints={len(Ek)} vertices={len(np.unique(Ek[:, :2])) if len(Ek) else 0}")
    if len(sys.argv) > 5 and len(Ec):
        parent = {}
        def find(x):
            while parent.setdefault(x, x) != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for a, b, _ in Ec:
            parent[find(int(a))] = find(int(b))
        comps = defaultdict(list)
        for row in Ec:
            comps[find(int(row[0]))].append(row)
        print(f"  core components: {len(comps)}, max constraints={max(len(c) for c in comps.values())}")
        for key, rows in sorted(comps.items(), key=lambda kv: -len(kv[1])):
            res, nodes, _ = solve(np.array(rows), M, limit=300000)
            print(f"  component {len(rows)} constraints: result={res} nodes={nodes}")
