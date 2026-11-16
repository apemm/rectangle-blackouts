"""Refinement table for corner-gated king quadtree curves (CGK curves).

Corner / child index: c = cx + 2*cy, cx, cy in {0,1}.
Gate = (in_corner, out_corner), in != out.
A refinement of a node with gate g (child side s >= 2) is
  (order of the 4 children, gate of each child) with
  first child = child containing the in corner, its in gate = that corner,
  last child = child containing the out corner, its out gate = that corner,
  child gates have in != out,
  junction rule between consecutive children c1 -> c2 (scale invariant king adjacency):
    for each axis a: if p1a != p2a then out1_a = p2a and in2_a = p1a,
                      else out1_a = in2_a.
"""
import itertools, json, sys

def bits(c):
    return (c & 1, c >> 1)

GATES = [(a, b) for a in range(4) for b in range(4) if a != b]

def junction_ok(p1, o1, p2, i2):
    P1, P2, O1, I2 = bits(p1), bits(p2), bits(o1), bits(i2)
    if p1 == p2:
        return False
    for a in range(2):
        if P1[a] != P2[a]:
            if not (O1[a] == P2[a] and I2[a] == P1[a]):
                return False
        else:
            if O1[a] != I2[a]:
                return False
    return True

def refinements(g):
    gin, gout = g
    res = []
    mids = [c for c in range(4) if c not in (gin, gout)]
    for mid in itertools.permutations(mids):
        order = (gin,) + mid + (gout,)
        for cg in itertools.product(GATES, repeat=4):
            if cg[0][0] != gin or cg[3][1] != gout:
                continue
            ok = all(junction_ok(order[k], cg[k][1], order[k + 1], cg[k + 1][0]) for k in range(3))
            if ok:
                res.append((order, cg))
    return res

TABLE = {g: refinements(g) for g in GATES}

def gate_type(g):
    a, b = g
    return 'A' if bin(a ^ b).count('1') == 1 else 'D'

if __name__ == '__main__':
    out = {}
    for g in GATES:
        R = TABLE[g]
        out[str(g)] = len(R)
        print(g, gate_type(g), len(R))
        for order, cg in R:
            print('   order', order, 'child gates', cg, [gate_type(x) for x in cg])
    # Hilbert check: gate (0,1): in BL corner 0, out BR corner 1
    hil = ((0, 2, 3, 1), ((0, 2), (0, 1), (0, 1), (3, 1)))
    print('Hilbert refinement in table:', hil in TABLE[(0, 1)])
    print('all nonempty:', all(len(TABLE[g]) > 0 for g in GATES))
