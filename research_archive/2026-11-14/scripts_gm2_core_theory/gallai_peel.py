"""Gallai (DP-Brooks) peeling of the certified problem on the weighted M-core of G_B^o.

Certified problem = DP-colouring with M colours: constraint (r,u,delta) is the matching
y_u = y_r + delta (mod M) between the colour sets of r and u.  Parallel constraints with the
same residue are one matching; distinct residues give multiplicity.

Peeling rules (assignment is in reverse peeling order):
 (a) remove v with deg(v) < M;
 (b) remove a whole component C of G[{v : deg(v) = M}] if some block of C is not K_n^k or C_n^k
     (Bernshteyn-Kostochka-Pron 2017, Theorem 9: then C is colourable from every cover with
     |L(v)| >= deg_C(v), and |L(v)| >= M - deg_R(v) = deg_C(v) for the residual lists).
Usage: py -B gallai_peel.py B S M orient
"""
import sys
from collections import defaultdict
import networkx as nx
import cert_core as cc


def is_gdp_block(Gm, nodes, mult):
    nodes = list(nodes)
    n = len(nodes)
    ks = set()
    ecount = 0
    for i in range(n):
        for j in range(i + 1, n):
            m = mult.get(frozenset((nodes[i], nodes[j])), 0)
            if m:
                ks.add(m)
                ecount += 1
    if len(ks) != 1:
        return False
    if ecount == n * (n - 1) // 2:
        return True  # K_n^k (includes K_2^k)
    if ecount == n and all(Gm.degree(v) == 2 for v in nodes):
        return True  # C_n^k  (simple-graph degrees inside the block)
    return False


def main():
    B, S, M, orient = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    trip, x, y = cc.build(B, S, M, orient)
    keys = list(trip)
    K = cc.peel(keys, M, lambda r, u, dl, side: (u, dl) if side == 0 else (r, dl))
    EK = [k for k in keys if k[0] in K and k[1] in K]
    cls = defaultdict(set)
    for (r, u, dl) in EK:
        cls[frozenset((r, u))].add(dl % M if True else None)  # residue of y_u - y_r (oriented r<u)
    mult = {e: len(s) for e, s in cls.items()}
    nb = defaultdict(set)
    for e in mult:
        a, b = tuple(e)
        nb[a].add(b); nb[b].add(a)
    alive = set(K)
    deg = {v: sum(mult[frozenset((v, w))] for w in nb[v]) for v in alive}
    print(f"B={B} S={S} M={M} {orient}: |K|={len(K)}, |E(K)|={len(EK)}, multi-pairs {sum(1 for m in mult.values() if m > 1)}")

    def remove(v):
        alive.discard(v)
        for w in nb[v]:
            if w in alive:
                deg[w] -= mult[frozenset((v, w))]

    rounds = 0; pieces = []
    while True:
        rounds += 1
        changed = False
        stack = [v for v in alive if deg[v] < M]
        while stack:
            v = stack.pop()
            if v not in alive:
                continue
            remove(v); changed = True
            for w in nb[v]:
                if w in alive and deg[w] < M:
                    stack.append(w)
        VM = [v for v in alive if deg[v] == M]
        Gm = nx.Graph()
        Gm.add_nodes_from(VM)
        sv = set(VM)
        for v in VM:
            for w in nb[v]:
                if w in sv:
                    Gm.add_edge(v, w)
        peeled_any = False
        for comp in list(nx.connected_components(Gm)):
            H = Gm.subgraph(comp)
            ok_gdp = True
            if H.number_of_edges() == 0:
                ok_gdp = True  # single vertex: K_1, a GDP-tree
            else:
                for blk in nx.biconnected_components(H):
                    if not is_gdp_block(H.subgraph(blk), blk, mult):
                        ok_gdp = False
                        break
            if not ok_gdp:
                pieces.append(len(comp))
                for v in comp:
                    remove(v)
                peeled_any = True
        if not changed and not peeled_any:
            break
    print(f" rounds {rounds}; Gallai pieces peeled {len(pieces)}, sizes (largest 10) {sorted(pieces)[-10:]}")
    print(f" residual Gallai core: {len(alive)} labels")
    if alive:
        ds = defaultdict(int)
        for v in alive:
            ds[deg[v]] += 1
        print("  residual degree distribution", sorted(ds.items()))


if __name__ == "__main__":
    main()
