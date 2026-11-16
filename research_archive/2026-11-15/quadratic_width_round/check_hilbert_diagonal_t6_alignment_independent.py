"""Independent rerun of the eight-bit certificate for the t=6 diagonal branch.

Nothing is imported from the other checkers. The Hilbert transitions are built
from point symmetries of the unit square and tested against the classical
iterative coordinate-to-rank routine. The template is rebuilt from the six
selected roles of mask 13.
"""
from itertools import product
from pathlib import Path
import json

# --- Hilbert transitions from symmetries -----------------------------------
# A symmetry is (swap, flip): first swap the coordinates if swap, then
# replace (x, y) by (1-x, 1-y) if flip. The two operations commute.
SYMS = [(s, f) for f in (0, 1) for s in (0, 1)]


def act(g, p):
    x, y = p
    if g[0]:
        x, y = y, x
    if g[1]:
        x, y = 1 - x, 1 - y
    return x, y


def mul(g, h):
    return (g[0] ^ h[0], g[1] ^ h[1])


BASE_ORDER = [(0, 0), (0, 1), (1, 1), (1, 0)]
CHILD = [(1, 0), (0, 0), (0, 0), (1, 1)]  # swap, identity, identity, reflected swap

# top-down: (parent, digit) -> (quadrant, child)
DOWN = {(g, k): (act(g, BASE_ORDER[k]), mul(g, CHILD[k])) for g in SYMS for k in range(4)}
# bottom-up: (child, quadrant) -> (parent, digit)
UP = {}
for (g, k), (quad, child) in DOWN.items():
    assert (child, quad) not in UP
    UP[child, quad] = (g, k)
assert len(UP) == 16


def rank_table(g, n, x, y):
    d = 0
    for level in range(n - 1, -1, -1):
        quad = ((x >> level) & 1, (y >> level) & 1)
        k = next(k for k in range(4) if DOWN[g, k][0] == quad)
        d = 4 * d + k
        g = DOWN[g, k][1]
    return d


def rank_classical(n, x, y):
    side = 1 << n
    d = 0
    s = side // 2
    while s > 0:
        rx = int((x & s) > 0)
        ry = int((y & s) > 0)
        d += s * s * ((3 * rx) ^ ry)
        if ry == 0:
            if rx == 1:
                x, y = side - 1 - x, side - 1 - y
            x, y = y, x
        s //= 2
    return d


def test_hilbert():
    n = 5
    side = 1 << n
    for g in SYMS:
        ranks = {(x, y): rank_table(g, n, x, y) for x in range(side) for y in range(side)}
        assert sorted(ranks.values()) == list(range(side * side))
        inverse = {d: p for p, d in ranks.items()}
        for d in range(side * side - 1):
            (x0, y0), (x1, y1) = inverse[d], inverse[d + 1]
            assert abs(x0 - x1) + abs(y0 - y1) == 1
    # one of the four orientations is the classical curve
    assert any(all(rank_table(g, n, x, y) == rank_classical(n, x, y)
                   for x in range(side) for y in range(side)) for g in SYMS)


# --- The template of mask 13 -----------------------------------------------
ROLES = [(1, 0), (0, 2), (3, 0), (2, 1), (1, 3), (2, 3)]  # source -> target


def template():
    # y_target - x_source = C - c (target - source)^2. Vertices ('x', u), ('y', v).
    pot = {('x', 1): 0}
    changed = True
    while changed:
        changed = False
        for u, v in ROLES:
            w = (v - u) ** 2
            if ('x', u) in pot and ('y', v) not in pot:
                pot['y', v] = pot['x', u] - w
                changed = True
            if ('y', v) in pot and ('x', u) not in pot:
                pot['x', u] = pot['y', v] + w
                changed = True
    big = set(pot)
    assert len(big) == 6
    for u, v in ROLES:
        if ('x', u) in big:
            assert pot['y', v] == pot['x', u] - (v - u) ** 2
    rest = [(kind, i) for kind in 'xy' for i in range(4) if (kind, i) not in big]
    assert len(rest) == 2
    (xs,), (ys,) = [[i for kind, i in rest if kind == k] for k in 'xy']
    assert (xs, ys) in ROLES
    small = {('x', xs): 0, ('y', ys): -(ys - xs) ** 2}
    for group in (pot, small):
        low = min(group.values())
        for key in group:
            group[key] -= low
    coeff = {**pot, **small}
    base = {key: ('A' if key[0] == 'x' else 'B') for key in pot}
    base.update({key: ('Z' if key[0] == 'x' else 'W') for key in small})
    spread = max(coeff[k] for k in pot if k[0] == 'x') - min(coeff[k] for k in pot if k[0] == 'x')
    return coeff, base, spread


COEFF, BASE, SPREAD = template()
KEYS = [(kind, i) for i in range(4) for kind in 'xy']  # x0, y0, x1, y1, ...
NAMES = 'ABZW'


def step(state, scale_bit, first=False, registers=None, depth=None):
    """One coordinate level. state = (orient x4, cr, c1, c2, carries x8[, C, D])."""
    orient = state[:4]
    cr, c1, c2 = state[4:7]
    carries = state[7:15]
    out = set()
    for bits in product((0, 1), repeat=4):
        low = dict(zip(NAMES, bits))
        rel = low['A'] + low['W'] - low['B'] - low['Z'] + cr
        if rel % 2:
            continue
        values = [low[BASE[key]] + COEFF[key] * scale_bit + carries[n] for n, key in enumerate(KEYS)]
        ups = [UP[orient[i], (values[2 * i] % 2, values[2 * i + 1] % 2)] for i in range(4)]
        q = [u[1] for u in ups]
        if first and (q[1] - q[0]) % 2 == 0:
            continue
        f = q[0] - 2 * q[1] + q[2] + c1
        g = q[1] - 2 * q[2] + q[3] + c2
        if f % 4 or g % 4:
            continue
        new = (*(u[0] for u in ups), rel // 2, f // 4, g // 4, *(v // 2 for v in values))
        if registers is not None:
            C, D = state[15:]
            C = (C + (low['B'] - low['A']) * (1 << (depth - 1))) % registers[0]
            D = (D + (q[1] - q[0]) * (1 << (2 * (depth - 1)))) % registers[1]
            new += (C, D)
        out.add(new)
    return out


def terminal(state):
    if len(set(state[:4])) != 1 or state[5] or state[6]:
        return False
    shift = {}
    for n, key in enumerate(KEYS):
        if shift.setdefault(BASE[key], state[7 + n]) != state[7 + n]:
            return False
    return state[4] == shift['A'] + shift['W'] - shift['B'] - shift['Z']


def audit():
    test_hilbert()
    assert SPREAD >= 3
    j = 3
    zero_levels = 7 + 3 * j  # c' = 2^16 b
    swap = (1, 0)
    cosets = {frozenset((g, mul(g, swap))) for g in SYMS}
    states = {(*o, *([0] * 11), 0, 0) for coset in cosets for o in product(sorted(coset), repeat=4)}
    for depth in range(1, zero_levels + 1):
        states = {n for s in states for n in step(s, 0, first=(depth == 1), registers=(16, 256), depth=depth)}
        assert all(not any(s[7:15]) for s in states)
    seed_count = len(states)
    groups = {}
    for s in states:
        C, D = s[15:]
        b = 9 * D * D * pow(16 * C + 1, -1, 256) % 256
        groups.setdefault(b, set()).add(s[:15])
    report = []
    for b, current in sorted(groups.items()):
        sizes = [len(current)]
        for bit in range(8):
            current = {n for s in current for n in step(s, (b >> bit) & 1)}
            assert not any(terminal(s) for s in current), (b, bit)
            sizes.append(len(current))
        assert not current, b
        report.append(dict(b_mod256=b, level_sizes=sizes))
    return dict(status='PASS', seed_states=seed_count, groups=report,
                residues_mod8=sorted({g['b_mod256'] % 8 for g in report}))


if __name__ == '__main__':
    result = audit()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(result['status'], result['seed_states'], len(result['groups']), result['residues_mod8'])
