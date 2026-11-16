"""DEC at the junction J_11 (blocks W_9 -> W_10 -> W_11, sides 512, 1024, 2048), cand, S=32, M=3.
Usage: py -B dec11.py build g attach w      -> win_<g>_<attach>_<w>.npz (all window triples)
       py -B dec11.py core  g attach w      -> components of the certified 3-core of the window
g: orientation of the diagonal block E of side 2048 whose tail W_0..W_10 is extended.
attach O4: E = C3(F), F of side 4096 and orientation g, new block W_11 = O4(F), J_11 = 3*2048^2.
attach O2: E = C1(P), P of side 4096 and orientation g o swap, new block O2(P), J_11 = 2048^2.
Window = [J_11 - 1024^2 - 512^2, J_11 + w): W_9, W_10 and the first w ranks of the new block.
The certified core of the window system lies inside the certified core of the whole chain
(cores are monotone under subsystems), so a window-core component that holds a label of W_9
and a label of the new block refutes DEC at J_11.
"""
import sys, time
import numpy as np
from common import hilbert_array, legs, window_triples, certified_classes, core, M

stage, g, attach, w = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
N = 2048
J11 = 3 * N * N if attach == "O4" else N * N
J10 = J11 - (N // 2) ** 2
J9 = J10 - (N // 4) ** 2
lo, hi = J9, J11 + w
tag = f"win_{g}_{attach}_{w}"
t0 = time.time()


def geometry():
    h = g if attach == "O4" else ("swap" if g == "id" else "id")
    xy = hilbert_array(2 * N)
    if h == "swap":
        xy = xy[:, ::-1].copy()
    # geometry checks: E occupies [J11 - N^2, J11) as a diagonal block; W_10, W_9 are its
    # last two first-off-diagonal tail blocks; the new block is first-off-diagonal of side N.
    def box(a, b):
        x, y = xy[a:b, 0], xy[a:b, 1]
        return int(x.min()), int(x.max()), int(y.min()), int(y.max())
    E0 = J11 - N * N
    ex = box(E0, J11)
    assert ex[1] - ex[0] == N - 1 and ex[3] - ex[2] == N - 1 and ex[0] == ex[2], ex
    for (a, b, s) in [(J9, J10, N // 4), (J10, J11, N // 2), (J11, J11 + N * N, N)]:
        bx = box(a, b)
        assert bx[1] - bx[0] == s - 1 and bx[3] - bx[2] == s - 1, (a, bx)
        off = abs(bx[0] - bx[2])
        assert off == s, ("not first-off-diagonal", a, bx)
    T = xy[:, 1].astype(np.int64) - xy[:, 0]
    sg = [int(np.sign(T[a:b]).min()) * int(np.sign(T[a:b]).max()) for a, b in [(J9, J10), (J10, J11), (J11, J11 + N * N)]]
    assert all(s == 1 for s in sg), sg               # each block lies in one open half
    assert np.sign(T[J9]) == np.sign(T[J10]) == np.sign(T[J11])
    xw = xy[lo:hi].astype(np.int64)
    return (2 * xw[:, 0] + 1), (2 * xw[:, 1] + 2), T[lo:hi]


if stage == "build":
    odd, even, T = geometry()
    print(f"geometry ok; window [{lo},{hi}) size {hi-lo}; T sign {int(np.sign(T[0]))}  ({time.time()-t0:.1f}s)", flush=True)
    P = legs(4 * N - 1)
    print(f"legs: {len(P)} gaps  ({time.time()-t0:.1f}s)", flush=True)
    E = window_triples(odd, even, 0, hi - lo, P)
    print(f"triples {len(E)}  ({time.time()-t0:.1f}s)", flush=True)
    np.savez_compressed(tag + ".npz", E=E.astype(np.int32), T=T.astype(np.int32), lo=lo, hi=hi, J9=J9, J10=J10, J11=J11)
    print(f"saved {tag}.npz  ({time.time()-t0:.1f}s)")

elif stage == "core":
    from scipy.sparse import coo_matrix
    from scipy.sparse.csgraph import connected_components
    z = np.load(tag + ".npz")
    E = z["E"].astype(np.int64); n = hi - lo
    a9, a10, a11 = J9 - lo, J10 - lo, J11 - lo
    C = certified_classes(E)
    K = core(n, C)
    labs = np.unique(K[:, :2])
    print(f"window core: {len(labs)} labels, {len(K)} classes  ({time.time()-t0:.1f}s)", flush=True)
    ia = np.searchsorted(labs, K[:, 0]); ib = np.searchsorted(labs, K[:, 1])
    nc, lab = connected_components(coo_matrix((np.ones(len(K)), (ia, ib)), shape=(len(labs),) * 2), directed=False)
    sizes = np.bincount(lab)
    n9 = np.bincount(lab, weights=(labs < a10)); n10 = np.bincount(lab, weights=(labs >= a10) & (labs < a11))
    n11 = np.bincount(lab, weights=(labs >= a11))
    order = np.argsort(-sizes)
    print(f"components {nc}; largest (size: W_9 / W_10 / new):")
    for c in order[:8]:
        print(f"   {sizes[c]}: {int(n9[c])} / {int(n10[c])} / {int(n11[c])}")
    span = [c for c in range(nc) if n9[c] > 0 and n11[c] > 0]
    print(f"components holding a W_9 label and a new-block label: {len(span)}")
    if span:
        c = max(span, key=lambda c: sizes[c])
        sel = lab == c
        Kc = K[sel[ia]]
        np.savez_compressed(f"cert_{g}_{attach}_{w}.npz", labels=(labs[sel] + lo).astype(np.int64),
                            classes=(Kc + [lo, lo, 0]).astype(np.int64), J9=J9, J10=J10, J11=J11, g=g, attach=attach)
        print(f"  saved certificate component of {sizes[c]} labels, {len(Kc)} classes")
    print(f"done  ({time.time()-t0:.1f}s)")
