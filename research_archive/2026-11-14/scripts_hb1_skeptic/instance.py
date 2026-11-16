from check_binary_angle import chi
S, L, F = 1568, 1, 1005
alpha, blo, bup = 13441, 13504, 13518
def row(x): r = x % 7; return 'hole' if r == 0 else (L if chi(r) == -1 else 'H')
for order in ((blo, bup), (bup, blo)):      # (b of left label e, b of right label f)
    be, bf = order
    for q in range(1, 6):
        X = S * q; out = []
        Y1, Y2 = bf - alpha, be - alpha
        n1 = Y1 * (alpha - L)
        if n1 % X == 0:
            u = n1 // X; E = (u, L); W = (X + u, L + Y1)
            if row(E[0]) == L and row(W[0]) == L: out.append(('opt1 V=(0,%d) Q=(%d,%d)' % (alpha, X, bf), E, W))
        n4 = -Y2 * (alpha - L)
        if n4 % X == 0:
            u = n4 // X; E = (X + u, L); W = (u, L + Y2)
            if row(E[0]) == L and row(W[0]) == L: out.append(('opt4 V=(%d,%d) Q=(0,%d)' % (X, alpha, be), E, W))
        print('b_e=%d b_f=%d q=%d' % (be, bf, q), out)
