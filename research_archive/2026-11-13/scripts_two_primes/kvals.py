# K_l(M) = min N^t over N >= 3, t >= 1 with M * ceil(2l/N)^t < l^t  (per-level digit lemma cost)
import math
def K(l, M):
    best = None
    for t in range(1, 40):
        for N in range(3, 4*M + 2*l + 5):
            b = -(-2*l // N)
            if M * b**t < l**t:
                v = N**t
                if best is None or v < best[0]: best = (v, N, t)
                break  # smallest N for this t
    return best
for l in (11, 19, 29):
    print("l", l, [(M, K(l, M)) for M in (4, 12, 20, 28, 44, 84, 164, 324, 804, 1604)])
# compare with uniform bound 6 M^2.29 and with (E)'s factor (2l+1)^ceil(log_l(M+1))
for M in (12, 84, 804, 8004, 80004):
    print(M, "K_11", K(11, M)[0], "K_19", K(19, M)[0], "6M^2.29", round(6*M**2.29), "ratio log K_19/log M", round(math.log(K(19, M)[0])/math.log(M), 3))
