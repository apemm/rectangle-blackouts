"""Search for one FW candidate event of design H7 whose labels lie in different excursions.

Usage: py -I fw_cross_witness.py n trials seed F0
  Q = 2^n (padded side of one block), M = 3, sigma = 1, S = 6272, D = 28, a0 = 1, b0 = 2.
  Odd role, k = 1, xi' = +-1:  delta = S^2/2, Delta = delta/28 = 702464,
  m = F0 - a_e (< 0), slot gap q = -+|m|/2, xi = +-S, X = S q.
  f = label at rank r_e + sign * floor(|q|/M), and the event needs i_f = i_e + Delta.
  g = label at rank r_f + sign (slot of f +- 1).
Hits are re-verified with exact Python integers: Hilbert maps, the right angle at A,
the column of W, and the excursion index (number of diagonal cells of rank <= r).
"""
import sys, time
import numpy as np
import numba as nb

D = 28; S = 6272; M = 3; A0 = 1; B0 = 2


@nb.njit(cache=True)
def fwd(i, j, n, L0):
    hi = 0; lo = 0
    for l in range(n - 1, -1, -1):
        q = 1 << l
        a = 1 if i >= q else 0
        b = 1 if j >= q else 0
        if a == 0 and b == 0:
            dig = 0; i, j = j, i
        elif a == 0 and b == 1:
            dig = 1; j = j - q
        elif a == 1 and b == 1:
            dig = 2; i = i - q; j = j - q
        else:
            dig = 3; i, j = q - 1 - j, 2 * q - 1 - i
        if l >= L0:
            hi = hi * 4 + dig
        else:
            lo = lo * 4 + dig
    return hi, lo


@nb.njit(cache=True)
def inv(hi, lo, n, L0):
    x = 0; y = 0
    for l in range(n):
        if l < L0:
            dig = (lo >> (2 * l)) & 3
        else:
            dig = (hi >> (2 * (l - L0))) & 3
        q = 1 << l
        if dig == 0:
            x, y = y, x
        elif dig == 1:
            y = y + q
        elif dig == 2:
            x = x + q; y = y + q
        else:
            x, y = 2 * q - 1 - y, q - 1 - x
    return x, y


@nb.njit(cache=True)
def search(ie, te, n, L0, F0, Delta, out):
    base = 1 << (2 * L0)
    k = 0
    for t in range(ie.shape[0]):
        i = ie[t]; j = i + te[t]
        if j < 0 or j >= (1 << n):
            continue
        hi, lo = fwd(i, j, n, L0)
        am = A0 + D * i - F0          # |m|, m = F0 - a_e < 0
        qa = am // 2                  # |q| (am is even)
        dd = qa // M
        dhi = dd // base; dlo = dd % base
        for sgn in (-1, 1):
            if sgn == 1:
                l2 = lo + dlo; h2 = hi + dhi
                if l2 >= base:
                    l2 -= base; h2 += 1
            else:
                l2 = lo - dlo; h2 = hi - dhi
                if l2 < 0:
                    l2 += base; h2 -= 1
            if h2 < 0 or h2 >= (1 << (2 * (n - L0))):
                continue
            x, y = inv(h2, l2, n, L0)
            if x == i + Delta:
                if k < out.shape[0]:
                    out[k, 0] = t; out[k, 1] = sgn; out[k, 2] = x; out[k, 3] = y
                k += 1
    return k


def fwd_py(i, j, n):
    r = 0
    for l in range(n - 1, -1, -1):
        q = 1 << l
        a = i >= q; b = j >= q
        if not a and not b:
            dig = 0; i, j = j, i
        elif not a and b:
            dig = 1; j -= q
        elif a and b:
            dig = 2; i -= q; j -= q
        else:
            dig = 3; i, j = q - 1 - j, 2 * q - 1 - i
        r = 4 * r + dig
    return r


def inv_py(r, n):
    x = y = 0
    for l in range(n):
        dig = (r >> (2 * l)) & 3
        q = 1 << l
        if dig == 0:
            x, y = y, x
        elif dig == 1:
            y += q
        elif dig == 2:
            x += q; y += q
        else:
            x, y = 2 * q - 1 - y, q - 1 - x
    return x, y


def excursion_index(r, n):
    """Largest y with rank(y, y) <= r (diagonal ranks increase with y)."""
    lo, hi = 0, (1 << n) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if fwd_py(mid, mid, n) <= r:
            lo = mid
        else:
            hi = mid - 1
    return lo


def selftest():
    import itertools
    n = 6; L0 = 3
    xs = np.zeros(1, dtype=np.int64); ys = np.zeros(1, dtype=np.int64); s = 1
    while s < (1 << n):
        x, y = xs, ys
        xs = np.concatenate([y, x, x + s, 2 * s - 1 - y]); ys = np.concatenate([x, y + s, y + s, s - 1 - x]); s *= 2
    for r in range(len(xs)):
        h, l = fwd(int(xs[r]), int(ys[r]), n, L0)
        assert h * 4 ** L0 + l == r
        assert inv(h, l, n, L0) == (xs[r], ys[r])
        assert fwd_py(int(xs[r]), int(ys[r]), n) == r and inv_py(r, n) == (xs[r], ys[r])
    print("self-test passed (n = 6, all", len(xs), "ranks)")


def main():
    n = int(sys.argv[1]); trials = int(sys.argv[2]); seed = int(sys.argv[3]); F0 = int(sys.argv[4])
    selftest()
    L0 = n // 2
    Q = 1 << n
    delta = S * S // 2; Delta = delta // D
    assert delta % D == 0 and (A0 - F0) % 4 == 2 and (F0 - A0) % 7 != 0
    rng = np.random.default_rng(seed)
    t0 = time.time()
    ie = rng.integers(int(0.55 * Q), int(0.75 * Q), size=trials, dtype=np.int64)
    te = rng.integers(1, 4097, size=trials, dtype=np.int64) * rng.choice(np.array([-1, 1]), size=trials)
    out = np.zeros((100, 4), dtype=np.int64)
    k = search(ie, te, n, L0, F0, Delta, out)
    print(f"n={n} trials={trials} seed={seed} F0={F0}: hits={k}  ({time.time()-t0:.1f}s)")
    for row in out[:min(k, 100)]:
        t, sgn, xf, yf = (int(v) for v in row)
        i_e = int(ie[t]); j_e = i_e + int(te[t])
        r_e = fwd_py(i_e, j_e, n)
        am = A0 + D * i_e - F0; qa = am // 2; dd = qa // M
        r_f = r_e + sgn * dd
        assert inv_py(r_f, n) == (xf, yf)
        # choices realising the slot gap q = sgn * qa and g at slot(f) + sgn
        if sgn == 1:
            xi_f = M - 1; xi_e = M - 1 - (qa - M * dd); r_g = r_f + 1; xi_g = 0
        else:
            xi_f = 0; xi_e = qa - M * dd; r_g = r_f - 1; xi_g = M - 1
        assert 0 <= xi_e < M
        x_e = S * (M * r_e + xi_e); x_f = S * (M * r_f + xi_f); x_g = S * (M * r_g + xi_g)
        X = x_f - x_e; xi = sgn * S
        a_e = A0 + D * i_e; a_f = A0 + D * xf; m = F0 - a_e
        assert X == sgn * S * qa and a_f - a_e == delta
        assert X * xi + delta * m == 0            # right angle at A = (x_e, a_e)
        assert x_g == x_f + xi                     # W = (x_f + xi, F0 + delta) in g's column
        assert x_g != x_f and r_g != r_f
        # locality sanity: Delta^2 < 16 * dd
        ex = [excursion_index(r, n) for r in (r_e, r_f, r_g)]
        i_g, j_g = inv_py(r_g, n)
        print(f"  e=({i_e},{j_e}) T_e={j_e-i_e} r_e={r_e}; f=({xf},{yf}) T_f={yf-xf} r_f={r_f}; "
              f"g=({i_g},{j_g}) r_g={r_g}; rank gap {sgn*dd}; excursion index e,f,g = {ex}; "
              f"Delta^2/(16 d) = {Delta*Delta/(16*dd):.3f}")


if __name__ == '__main__':
    main()
