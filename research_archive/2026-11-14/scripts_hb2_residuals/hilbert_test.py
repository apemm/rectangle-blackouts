"""Check Hilbert maps: pt_census xy2d versus the textbook pair; bijection,
inverse, and locality max(dx^2, dy^2) < 16|dr|."""
def xy2d_pt(n, x, y):
    d = 0; s = n // 2
    while s > 0:
        rx = 1 if (x & s) else 0; ry = 1 if (y & s) else 0
        d += s * s * ((3 * rx) ^ ry)
        if ry == 0:
            if rx == 1: x = s - 1 - x; y = s - 1 - y
            x, y = y, x
        s //= 2
    return d
def xy2d(n, x, y):
    d = 0; s = n // 2
    while s > 0:
        rx = 1 if (x & s) else 0; ry = 1 if (y & s) else 0
        d += s * s * ((3 * rx) ^ ry)
        if ry == 0:
            if rx == 1: x = n - 1 - x; y = n - 1 - y
            x, y = y, x
        s //= 2
    return d
def d2xy(n, d):
    x = y = 0; s = 1; t = d
    while s < n:
        rx = 1 & (t // 2); ry = 1 & (t ^ rx)
        if ry == 0:
            if rx == 1: x = s - 1 - x; y = s - 1 - y
            x, y = y, x
        x += s * rx; y += s * ry
        t //= 4; s *= 2
    return x, y
for n in (16, 64):
    pts = [d2xy(n, d) for d in range(n * n)]
    print(n, 'd2xy bijective', len(set(pts)) == n * n,
          'xy2d inverts', all(xy2d(n, *pts[d]) == d for d in range(n * n)),
          'pt version agrees', all(xy2d_pt(n, *pts[d]) == d for d in range(n * n)))
    bad = 0
    for r in range(n * n):
        for t in range(r + 1, n * n):
            dx = pts[t][0] - pts[r][0]; dy = pts[t][1] - pts[r][1]
            if max(dx * dx, dy * dy) >= 16 * (t - r): bad += 1
    print(n, 'locality violations', bad)
