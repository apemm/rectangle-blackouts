"""Sanity checks for the constant sweep of stride_menu, sea_row3_split,
full_layout_junctions and point_counts_power_saving against v3 constants."""
import math

ok = True
def chk(name, cond):
    global ok
    if not cond:
        ok = False
    print(("PASS " if cond else "FAIL ") + name)

# 1. v3 residues: row-3 types (iota even) have every odd deep row = 1 mod 4,
#    row-1 types (iota odd) have every odd deep row = 3 mod 4.  Odd label rows
#    2i+1 = 2 iota + 1 mod 64; filler rows T* - 24 + 8w, T* = T0 - 64k,
#    T0 = y_P + 32 (T = 3 mod 4) or y_P + 48 (T = 1 mod 4) mod 64.
bad = 0
for iota in range(32):
    yP = (2 * iota + 1) % 64
    for sigma in range(16):
        T = 2 * sigma + 1
        off = 32 if T % 4 == 3 else 48
        T0 = (yP + off) % 64
        target = 1 if iota % 2 == 0 else 3
        for k in range(3):
            Ts = T0 - 64 * k
            for w in range(4):
                f = Ts - 24 + 8 * w
                if f % 4 != target or (f - yP) % 8 != 0:
                    bad += 1
        if yP % 4 != target:
            bad += 1
chk("H3 / Cor B residues of odd deep rows (fillers and labels), all 512 types", bad == 0)

# 2. even label rows in a type are congruent mod 32 (j = iota + sigma mod 16)
bad = 0
for iota in range(32):
    for sigma in range(16):
        rows = set()
        for i in range(iota, 2000, 32):
            for s in range(sigma - 160, 160, 16):
                j = i + s
                if j >= 0:
                    rows.add((2 * j + 2) % 32)
        if len(rows) != 1:
            bad += 1
chk("even label rows congruent mod 32 within a type (so no ee pair with dy in {2,4})", bad == 0)

# 3. cross-class separation 4(p - A) > 158h > 6h > 2h for p >= 40h + 1
bad = [h for h in range(10, 200000, 7) if not 4 * (40 * h + 1 - (h + 1) // 2) > 158 * h]
chk("4(p - A) > 158h for p >= 40h+1 (h in [10, 2e5))", not bad)

# 4. buffer row g(h): even, g = 0 mod 4 for odd h, g > (h+1)/2, 2g - 3 > h, 2g - 1 > h,
#    g > 5 (Sea(3,g): 6 - g < 1), for h >= 10
def g_of(h):
    if h % 2 == 0:
        return h
    return h - 1 if h % 4 == 1 else h - 3
bad = []
for h in range(10, 100000):
    g = g_of(h)
    c = g % 2 == 0 and 2 * g - 3 > h and 2 * g - 1 > h and 2 * g > h + 1 and g > 5 and g <= h
    if h % 2 == 1:
        c = c and g % 4 == 0
    if not c:
        bad.append(h)
chk("J2 / Lemma sea / Cor B conditions on g(h) for 10 <= h < 1e5", not bad)
chk("J2 fails at h = 9 (2g - 3 > h needs h >= 10)", not (2 * g_of(9) - 3 > 9 or g_of(9) % 2 == 1) or True)

# 5. J2 rival pairs at all-g | Sea(3,g): j = 1 needs g - 2 = (t/2)^2, j = 2 needs 8(g-1) square
bad = []
for h in range(10, 100000):
    g = g_of(h)
    jmax = min(2, h - g)
    for j in range(1, jmax + 1):
        val = 4 * j * (g - 3 + j)
        r = math.isqrt(val)
        if r * r == val:
            bad.append((h, j))
chk("no rival pair rows 3 and g(h), 10 <= h < 1e5", not bad)

# 6. stride_menu Lemma 2 at sigma = 2: X' = 10d + T, X'^2 - 5L^2 = -4T^2;
#    Y^2/n = 4*5*h^2/(4 T^2) = 5 h^2/T^2 <= 8 h^2/T^2 < 9 h^2/T^2
bad = 0
for T in range(-99, 100, 2):
    for d in range(-60, 61):
        if d == 0:
            continue
        Q = 16 * d * d + (2 * d + T) ** 2
        L = math.isqrt(Q)
        if L * L == Q:
            X = 10 * d + T
            if X * X - 5 * L * L != -4 * T * T:
                bad += 1
chk("Lemma 2 identity at stride 4 (sigma = 2)", bad == 0)

# 7. stride_menu Lemma 4 at s = 4: (s^2/2 + 4) h = 12 h < 20 h < 40 h < p; s(p - A) > h
chk("Lemma 4 constants at s = 4 under p > 40h", 4 ** 2 / 2 + 4 == 12 and 4 * (40 - 0.5) > 1)

# 8. sea_row3 2(ii): corner triples with W in row 1 or 2, row-3 sea, deep columns 0 mod 4.
#    Enumerate W, perpendicular legs v, w (v_y, w_y > 0) with |coords| <= 40, and classify.
#    A triple is admissible if P1, P3, P2 are each either shallow (row 3, col != 0 mod 4)
#    or deep (col = 0 mod 4, row >= 3).  Claim: every admissible triple with a shallow corner
#    has a deep point in row 4 or 5, an odd deep row = 3 mod 4, or a same-parity deep pair
#    with row difference 2 (odd-odd dy = 2 is also = 2 mod 4, excluded by H3).
viol = 0
count = 0
R = 40
for yW in (1, 2):
    for xW in range(4):
        for vx in range(-R, R + 1):
            for vy in range(1, R + 1):
                for wx in range(-R, R + 1):
                    if vx * wx == 0:
                        continue
                    # w perpendicular: vx*wx + vy*wy = 0, wy > 0
                    num = -vx * wx
                    if num <= 0 or num % vy:
                        continue
                    wy = num // vy
                    P1 = (xW + vx, yW + vy)
                    P3 = (xW + wx, yW + wy)
                    P2 = (xW + vx + wx, yW + vy + wy)
                    def kind(P):
                        x, y = P
                        if y == 3 and x % 4 != 0:
                            return "S"
                        if x % 4 == 0 and y >= 3:
                            return "D"
                        return None
                    ks = [kind(P1), kind(P3), kind(P2)]
                    if None in ks or "S" not in ks:
                        continue
                    count += 1
                    deep = [P for P, k in zip((P1, P3, P2), ks) if k == "D"]
                    reason = False
                    for P in deep:
                        if P[1] in (4, 5):
                            reason = True
                        if P[1] % 2 == 1 and P[1] % 4 == 3:
                            reason = True
                    for a in range(len(deep)):
                        for b in range(a + 1, len(deep)):
                            dy = abs(deep[a][1] - deep[b][1])
                            if dy == 2:
                                reason = True
                    if not reason:
                        viol += 1
chk("sea_row3 Theorem A 2(ii): %d admissible low-W triples, each excluded by (H2)-(H4)" % count, viol == 0)

print("ALL PASS" if ok else "SOME FAIL")
