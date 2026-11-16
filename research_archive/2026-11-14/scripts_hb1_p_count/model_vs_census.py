"""Random-row model for the Hilbert P family, compared with archived census numbers.

Model: for each slot (rank gap d, slot shift delta, role), the cross-parity row
pair (odd row of one label, even row of the other) is replaced by the row pair
of one uniformly random label.  Everything else is exact integer counting.
"""
import math, sys

def pyth_rows(X, h):
    """All (y, L) with y odd (signed), L < h, X^2 + y^2 = L^2."""
    out = []
    hs = (X // 2) ** 2
    for a in range(1, math.isqrt(hs) + 1):
        if hs % a:
            continue
        b = hs // a
        if (a + b) < h and (b - a) % 2:
            out.append((b - a, a + b))
    return out

def model(h, S, M, strip):
    A, K = (h + 1) // 2, h // 2
    labels = A * K
    # p_y[y] = #{(i,j): (2j+2)-(2i+1) = y} / labels, with midpoint data if strip
    total = 0.0
    nslots = 0
    for d in range(1, ((h - 1) // S + M - 1) // M + 1):
        for delta in range(1 - M, M):
            X = S * (M * d + delta)
            if X <= 0 or X >= h:
                continue
            nslots += 1
            for y, L in pyth_rows(X, h):
                for sy in (y, -y):
                    # count labels (i,j) with 2j+1-2i = sy and strip condition
                    t = (sy - 1) // 2  # j - i = t
                    cnt = 0
                    for i in range(A):
                        j = i + t
                        if not (0 <= j < K):
                            continue
                        a, b = 2 * i + 1, 2 * j + 2
                        if strip and not (a + b - L >= 2 and a + b + L <= 2 * h):
                            continue
                        cnt += 1
                    total += 2 * cnt / labels  # two roles
    return total, labels, nslots

if __name__ == "__main__":
    for (h, S, M, strip, obs) in [
        (512, 32, 1, False, 0.16983), (1024, 32, 1, False, 0.20219),
        (2048, 32, 1, False, 0.29655), (2048, 64, 1, False, 0.08160),
        (2048, 32, 3, True, 139237), (2048, 32, 4, True, 173065),
        (4096, 32, 3, True, 695871)]:
        tot, labels, ns = model(h, S, M, strip)
        if M == 1:
            print(h, S, M, "pred mean incidence", round(2 * tot, 5), "obs", obs)
        else:
            print(h, S, M, "pred constraints", round(tot * labels), "obs", obs,
                  "pred mean degree", round(2 * tot, 4))
        sys.stdout.flush()
