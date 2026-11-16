"""Window kernel: all cand triples (r, r+d, delta) with lo <= r < r+d < hi."""
import numpy as np
import numba as nb


@nb.njit(cache=True)
def kern(odd, even, M, lo, hi, qs, offs, Ys, Ls, out, Ymax):
    look = np.zeros(Ymax + 8, dtype=np.int64)
    cnt = 0
    for t in range(qs.shape[0]):
        q = qs[t]
        for k in range(offs[t], offs[t + 1]):
            look[Ys[k]] = Ls[k]
        for dd in range(2):
            d = q // M if dd == 0 else (q + M - 1) // M
            if dd == 1 and d == q // M:
                continue
            delta = q - M * d
            if d < 1 or d >= hi - lo:
                continue
            for r in range(lo, hi - d):
                for role in range(2):
                    if role == 0:
                        a = odd[r]; b = even[r + d]
                    else:
                        a = odd[r + d]; b = even[r]
                    y = b - a
                    if y < 0:
                        y = -y
                    if look[y] == 0:
                        continue
                    if cnt < out.shape[0]:
                        out[cnt, 0] = r; out[cnt, 1] = r + d; out[cnt, 2] = delta
                    cnt += 1
        for k in range(offs[t], offs[t + 1]):
            look[Ys[k]] = 0
    return cnt
