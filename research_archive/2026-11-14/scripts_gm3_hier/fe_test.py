"""Forward-extension test: does a given certified solution of the old tail A = [lo, J)
extend to a certified solution of A + W, W = [J, hi)?  (Boundary-list criterion.)
Usage: py -B fe_test.py seg.npz cert.npz key src_lo [limit]
  seg.npz from interface.py; the old values are cert[key][src_lo + (r - lo)].
Steps: verify certification of the old values on A; peel W relative to the fixed A
(a W label counts its distinct certified classes to alive W labels and to A); solve
the relative core with lists; extend by reverse peeling; verify the whole segment.
"""
import sys, time
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
from listsolve import solve

M = 3
segf, certf, key, src_lo = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
limit = int(sys.argv[5]) if len(sys.argv) > 5 else 3_000_000
t0 = time.time()
z = np.load(segf)
E, lo, J, hi = z["E"], int(z["lo"]), int(z["J"]), int(z["hi"])
cert = np.load(certf)[key].astype(np.int64)
y = {}
yo = cert[src_lo:src_lo + (J - lo)]
EA = E[E[:, 1] < J]
viol = ((yo[EA[:, 1] - lo] - yo[EA[:, 0] - lo] - EA[:, 2]) % M == 0).sum()
print(f"{segf} with {key}[{src_lo}:]: old part [{lo},{J}), triples on A {len(EA)}, certified violations on A: {int(viol)}")
assert viol == 0
key3 = np.stack([E[:, 0], E[:, 1], E[:, 2] % M], axis=1)
_, first = np.unique(key3, axis=0, return_index=True)
Ec = E[np.sort(first)][:, :3]
EW = Ec[Ec[:, 0] >= J]                         # inside W
EX = Ec[(Ec[:, 0] < J) & (Ec[:, 1] >= J)]      # crossing (lower end in A)
nW = hi - J
# forbidden residues at W labels from the fixed old values
forb = np.zeros(nW, dtype=np.int64)
for r, u, d in EX.tolist():
    forb[u - J] |= 1 << ((yo[r - lo] + d) % M)
ncl_A = np.array([bin(int(f)).count("1") for f in forb])   # distinct forbidden residues = classes to A (upper bound use)
# relative peeling: classes to A counted as distinct (neighbour, residue) classes
cA = np.zeros(nW, dtype=np.int64)
np.add.at(cA, EX[:, 1] - J, 1)
alive = np.ones(len(EW), dtype=bool)
while True:
    deg = cA + np.bincount(EW[alive, 0] - J, minlength=nW) + np.bincount(EW[alive, 1] - J, minlength=nW)
    bad = deg < M
    kill = alive & (bad[EW[:, 0] - J] | bad[EW[:, 1] - J])
    if not kill.any():
        break
    alive &= ~kill
K = EW[alive]
Kl = np.flatnonzero(deg >= M) + J          # alive labels (some may have no alive W edge)
touch = np.zeros(nW, dtype=bool); touch[EX[:, 1] - J] = True
inK = np.zeros(nW, dtype=bool); inK[Kl - J] = True
print(f"  W: {nW} labels, internal classes {len(EW)}, crossing classes {len(EX)}; relative core {len(Kl)} labels, "
      f"{int((inK & touch).sum())} of them adjacent to A")
# solve the relative core componentwise with lists
sol = {}
status = "SAT"
if len(Kl):
    labs = Kl; a = np.searchsorted(labs, K[:, 0]); b = np.searchsorted(labs, K[:, 1])
    nc, lab = connected_components(coo_matrix((np.ones(len(K)), (a, b)), shape=(len(labs),) * 2), directed=False)
    for c in range(nc):
        V = labs[lab == c]
        Ek = K[(lab[a] == c)]
        dom0 = {int(v): ((1 << M) - 1) & ~int(forb[v - J]) for v in V.tolist()}
        res, s, nodes = solve(V.tolist(), Ek.tolist(), M, dom0, limit)
        nadj = int(touch[V - J].sum())
        if res != "SAT" or nadj:
            print(f"    component {c}: {len(V)} labels, {nadj} adjacent to A: {res} ({nodes} nodes)")
        if res == "SAT":
            sol.update(s)
        else:
            status = res
print(f"  relative core: {status}")
if status == "SAT":
    # reverse-peel extension over all W labels not in the core
    val = -np.ones(nW, dtype=np.int64)
    for v, x in sol.items():
        val[v - J] = x
    # recompute a deletion order (queue peeling) for the non-core labels
    adj = [[] for _ in range(nW)]
    for r, u, d in EW.tolist():
        adj[r - J].append((u - J, d, 1)); adj[u - J].append((r - J, d, -1))
    degl = (cA + np.bincount(EW[:, 0] - J, minlength=nW) + np.bincount(EW[:, 1] - J, minlength=nW)).tolist()
    removed = [False] * nW; order = []
    stack = [v for v in range(nW) if not inK[v] and degl[v] < M]
    while stack:
        v = stack.pop()
        if removed[v]: continue
        removed[v] = True; order.append(v)
        for w, d, sg in adj[v]:
            if not removed[w]:
                degl[w] -= 1
                if not inK[w] and degl[w] < M: stack.append(w)
    assert len(order) + int(inK.sum()) == nW, "peeling did not reach every non-core label"
    for v in reversed(order):
        f = int(forb[v])
        for w, d, sg in adj[v]:
            if val[w] >= 0:
                f |= 1 << (((val[w] - d) if sg == 1 else (val[w] + d)) % M)
        x = 0
        while f >> x & 1: x += 1
        assert x < M
        val[v] = x
    full = np.concatenate([yo, val])
    bad = int(((full[E[:, 1] - lo] - full[E[:, 0] - lo] - E[:, 2]) % M == 0).sum())
    print(f"  extension built: certified violations on the whole segment = {bad}")
print(f"  ({time.time()-t0:.1f}s)")
