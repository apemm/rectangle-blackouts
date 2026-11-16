"""Common pieces for the H7 block census (P and R2s candidate systems).

Block (mixed by default): odd label rows a = 17 mod 28, even label rows
b = 8 mod 28 (zero-residue block: b = 24 mod 28).  Bottom indexing:
a_i = 17 + 28 i, b_j = BRES + 28 j (i, j >= 0, rows in [1, h]); the Hilbert
square side Q is the least power of two >= max(#odd rows, #even rows);
labels are the pairs (i, j) whose two rows lie in the bulk [lo, h - lo]
(subset with the original ranks).  Label e sits at column
x_e = S (M r_e + xi_e), S = 6272 (sigma = 1).  Sea rows (mixed block):
L = 3, F = 2015, H = largest row <= h that is 18 mod 28.  Sea type of a
column x (relative to the label columns, which are 0 mod 7):
F if 7 | x, L if x mod 7 in {3,5,6}, H if x mod 7 in {1,2,4}.
Hilbert curve: the standard low-bit rotation curve (same as pgraph.py).
"""
import numpy as np
from numba import njit

S = 6272


@njit(cache=True)
def d2xy(q, t):
    x = 0
    y = 0
    s = 1
    while s < q:
        rx = (t // 2) & 1
        ry = (t ^ rx) & 1
        if ry == 0:
            if rx == 1:
                x = s - 1 - x
                y = s - 1 - y
            x, y = y, x
        x += s * rx
        y += s * ry
        t //= 4
        s *= 2
    return x, y


@njit(cache=True)
def xy2d(q, x, y):
    d = 0
    s = q // 2
    while s > 0:
        rx = 1 if (x & s) > 0 else 0
        ry = 1 if (y & s) > 0 else 0
        d += s * s * ((3 * rx) ^ ry)
        if ry == 0:
            if rx == 1:
                x = q - 1 - x
                y = q - 1 - y
            x, y = y, x
        s //= 2
    return d


def block(h, lo, bres=8, ares=17):
    """Return a dict describing one residue block at height h."""
    nA = (h - ares) // 28 + 1          # odd rows 17 + 28 i <= h
    nK = (h - bres) // 28 + 1
    Q = 1
    while Q < max(nA, nK):
        Q *= 2
    # bulk index ranges
    iA0 = max(0, -(-(lo - ares) // 28))
    iA1 = (h - lo - ares) // 28
    jK0 = max(0, -(-(lo - bres) // 28))
    jK1 = (h - lo - bres) // 28
    Hrow = max(x for x in range(h - 800, h + 1) if x % 28 == 18)
    return {"h": h, "lo": lo, "ares": ares, "bres": bres, "Q": Q,
            "iA0": iA0, "iA1": iA1, "jK0": jK0, "jK1": jK1,
            "L": 3, "F": 2015, "H": Hrow,
            "labels": (iA1 - iA0 + 1) * (jK1 - jK0 + 1)}


def check_curve(q=64):
    n = q * q
    seen = set()
    for t in range(n):
        x, y = d2xy(q, t)
        assert xy2d(q, x, y) == t
        seen.add((x, y))
    assert len(seen) == n
    # locality bound max(dx^2, dy^2) < 16 |dt| (audited Placement Thm)
    for t in range(0, n, 7):
        x, y = d2xy(q, t)
        for dt in (1, 2, 3, 5, 17, 100):
            if t + dt < n:
                x2, y2 = d2xy(q, t + dt)
                assert max((x2 - x) ** 2, (y2 - y) ** 2) < 16 * dt
    return True


if __name__ == "__main__":
    print(check_curve(64), check_curve(128))
    print(block(250000, 100000))
