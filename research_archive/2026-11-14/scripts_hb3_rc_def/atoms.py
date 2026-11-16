"""Translation atoms (Lemma H3) and transposition fibers (Theorem B(iv)) on Hilbert vs random CGK curves, q = 256."""
import random
import numpy as np
from curve import build

n = 8; q = 1 << n; N = q * q
rng = random.Random(5)
curves = {'hilbert': build(n, (0, 1), rng, hilbert=True)}
for k in range(3):
    curves['random%d' % k] = build(n, (0, 1), rng)

print('Translation atom: max over v in {(+-2^k,0),(0,+-2^k)} of fraction of r with H(r+4^k)-H(r)=v (Hilbert proof: >= 1/16 for one sign)')
for name, H in curves.items():
    row = []
    for k in range(0, 7):
        d = 4 ** k
        D = H[d:] - H[:-d]
        best = 0
        for v in ((1 << k, 0), (-(1 << k), 0), (0, 1 << k), (0, -(1 << k))):
            best = max(best, int(np.sum((D[:, 0] == v[0]) & (D[:, 1] == v[1]))))
        row.append(round(best / N, 4))
    print('  %-8s' % name, row)

print('Transposition fiber: max_t #{r: j_{r+d} - i_r = t} / (q sqrt d), d = 4^m (Hilbert proof: >= 1/8)')
for name, H in curves.items():
    row = []
    for m in range(1, 7):
        d = 4 ** m
        t = H[d:, 1] - H[:-d, 0]
        vals, cnt = np.unique(t, return_counts=True)
        row.append(round(cnt.max() / (q * np.sqrt(d)), 3))
    print('  %-8s' % name, row)
print('reference for random curves (expectation bound per fixed t, up to constants): 2^m * 0.664^m / 2^m =', [round(0.6644 ** m * 2 ** m / 2 ** m, 3) for m in range(1, 7)])
