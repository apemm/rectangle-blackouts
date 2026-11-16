"""Probe: the eight-bit and twelve-bit register tests for t=6, antidiagonal branch."""
import sys
from itertools import product
import check_hilbert_diagonal_t6_alignment_independent as M

PAIRS = [(i, j) for i in range(4) for j in range(i + 1, 4)]


def roles(mask):
    return [(j, i) if mask >> k & 1 else (i, j) for k, (i, j) in enumerate(PAIRS)]


def template(R):
    verts = [(k, i) for k in 'xy' for i in range(4)]
    pot, comp = {}, {}
    groups = []
    for v0 in verts:
        if v0 in pot:
            continue
        pot[v0] = 0; group = [v0]; todo = [v0]
        while todo:
            v = todo.pop()
            for u, w in R:
                d = (w - u) ** 2
                if v == ('x', u) and ('y', w) not in pot:
                    pot['y', w] = pot[v] - d; group.append(('y', w)); todo.append(('y', w))
                if v == ('y', w) and ('x', u) not in pot:
                    pot['x', u] = pot[v] + d; group.append(('x', u)); todo.append(('x', u))
        groups.append(group)
    for u, w in R:
        assert pot['y', w] == pot['x', u] - (w - u) ** 2
    assert sorted(map(len, groups)) == [2, 6]
    base = {}
    for g in groups:
        low = min(pot[v] for v in g)
        for v in g:
            pot[v] -= low
            base[v] = ('AB' if len(g) == 6 else 'ZW')[v[0] == 'y']
    return pot, base


def run(mask, theta, J, j=3):
    M.COEFF, M.BASE = template(roles(mask))
    rswap = (1, 1)
    cosets = {frozenset((g, M.mul(g, rswap))) for g in M.SYMS}
    Cmod = 1 << max(0, J - j - 1)
    states = {(*o, *([0] * 11), 0, 0) for c in cosets for o in product(sorted(c), repeat=4)}
    for depth in range(1, 8 + 3 * j):
        states = {n for s in states for n in M.step(s, 0, first=(depth == 1), registers=(Cmod, 1 << J), depth=depth)}
    groups = {}
    for s in states:
        C, D = s[15:]
        b = 9 * D * D * pow((C << (j + 1)) + theta, -1, 1 << J) % (1 << J)
        groups.setdefault(b, set()).add(s[:15])
    alive = 0; term = 0
    for b, cur in groups.items():
        for bit in range(J):
            cur = {n for s in cur for n in M.step(s, (b >> bit) & 1)}
            term += sum(M.terminal(s) for s in cur)
            if not cur:
                break
        alive += len(cur)
    return len(states), len(groups), alive, term


if __name__ == '__main__':
    J = int(sys.argv[1])
    for mask in (13, 17):
        for theta in (15, 11, 7, 3, -1, -5, -9, -13):
            print(mask, theta, run(mask, theta, J), flush=True)
