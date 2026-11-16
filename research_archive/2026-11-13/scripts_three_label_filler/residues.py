# Norm classes of difference vectors in one L*** region, over all residues.
def v2(n):
    if n == 0: return 99
    k = 0
    while n % 2 == 0: n //= 2; k += 1
    return k
MOD = 1 << 14
bad = 0
for c in (1, 3):
    for w in range(4):
        vals = set()
        for a in range(w, 256, 4):            # nu_F - nu_L = w (mod 4)
            for k in range(16):
                b = 8*(w+c) + 64*k            # f - y_o = 8(w+c) (mod 64)
                vals.add(v2(16*a*a + b*b))
        print("F-o  c=%d w=%d  v2 in" % (c, w), sorted(vals))
        for T0 in range(1, 32, 2):
            r = set()
            for a in range(w, 64, 4):
                for k in range(8):
                    b = 8*(w+c) - T0 + 32*k   # f - y_e = 8(w+c) - T0 (mod 32)
                    r.add((16*a*a + b*b - T0*T0) % 32)
            if r != {16}: bad += 1
# o-e, o-o, e-e
r = set(); s = set(); t = set()
for T0 in range(1, 32, 2):
    for d in range(0, 256, 16):
        for k in range(8):
            r.add(((4*d)**2 + (T0 + 32*k)**2 - T0*T0) % 32)
for d in range(0, 256, 16):
    for k in range(8):
        s.add(min(v2((4*d)**2 + (64*k)**2), 99)); t.add(min(v2((4*d)**2 + (32*k)**2), 99))
print("F-e minus T0^2 mod 32 always 16:", bad == 0)
print("o-e minus T0^2 mod 32:", r)
print("o-o min v2:", min(s), " e-e min v2:", min(t))
