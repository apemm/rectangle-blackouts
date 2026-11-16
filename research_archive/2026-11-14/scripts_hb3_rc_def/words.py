import itertools, numpy as np
import chain as C
def dob(seq):
    Mx = np.eye(C.G)
    for d in seq: Mx = Mx @ C.P[d]
    return C.dobrushin(Mx)
for L in (5, 7):
    bad = [''.join(map(str, w)) for w in itertools.product(range(4), repeat=L) if dob(w) > 1 - 1e-12]
    print(L, len(bad), bad)
# worst coefficient among words with no run of 0s or 3s longer than 1? and per-length max over words containing >= half middle digits
for L in (6, 8):
    worst = 0
    for w in itertools.product(range(4), repeat=L):
        if sum(1 for d in w if d in (1, 2)) >= L // 2:
            worst = max(worst, dob(w))
    print('L', L, 'max coefficient over words with at least half middle digits:', round(worst, 4))
