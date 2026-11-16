# lambda_T = -min_theta sum_{d in D_T} cos(2 pi d theta) on the richest diagonals (FFT grid + Taylor error bound)
import sys, numpy as np
from math import pi, log
from common import all_D, nT
h = int(sys.argv[1]); top = int(sys.argv[2])
D = all_D(h)
ks = sorted(D, key=lambda T: -len(D[T]))[:top]
print("h", h, "ln h %.2f" % log(h), "sum k", sum(len(v) for v in D.values()))
for T in ks:
    d = np.array(D[T]); k = len(d); dmax = d.max()
    N = 1 << int(np.ceil(np.log2(64 * dmax)))
    a = np.zeros(N); a[d] = 1.0
    P = np.fft.rfft(a).real  # sum cos(2 pi d j / N)
    lam_grid = -P.min()
    err = pi**2 * k * dmax**2 / (2 * N**2)
    lam = lam_grid + err
    print("T %7d n %6d k %4d lam %.2f lam/k %.3f  Hoffman chi >= %.2f  k/ln h %.2f k/ln k %.2f" %
          (T, nT(h, T), k, lam, lam / k, k / (6.66 * lam), k / log(h), k / log(k)))
