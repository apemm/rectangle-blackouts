"""Count e in (0, Q/2) with a factorization e(Q-e) = t1*t2 and (t1+t2) | e(Q-2e)  (M2c label-filler core).
Usage: py m2c_count.py Q1,Q2,...   prints counts, plus the solutions (e, t1, t2, n1, X=t1-n1, Y=t2-n1)."""
import sys
from math import isqrt
import numpy as np
from numba import njit

@njit(cache=True)
def divs(n, out):
    k = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            out[k] = d; k += 1
        d += 1
    return k

@njit(cache=True)
def run(Q):
    res = []
    buf = np.zeros(4096, dtype=np.int64)
    for e in range(1, (Q + 1) // 2):
        if 2 * e >= Q:
            break
        P = e * (Q - e)
        M = e * (Q - 2 * e)
        # divisors t1 <= sqrt(P): t1 = a*b with a | e, b | Q-e is enough to enumerate via trial over divisors of e and Q-e
        ke = divs(e, buf)
        de = buf[:ke].copy()
        # all divisors of e: de and e//de
        alle = np.concatenate((de, e // de))
        kf = divs(Q - e, buf)
        df = buf[:kf].copy()
        allf = np.concatenate((df, (Q - e) // df))
        seen = set()
        for a in alle:
            for b in allf:
                t1 = a * b
                if t1 * t1 > P or P % t1:
                    continue
                if t1 in seen:
                    continue
                seen.add(t1)
                t2 = P // t1
                k = t1 + t2
                if M % k == 0:
                    n1 = M // k
                    res.append((e, t1, t2, n1, t1 - n1, t2 - n1))
    return res

for Q in [int(a) for a in sys.argv[1].split(',')]:
    r = run(Q)
    es = sorted(set(x[0] for x in r))
    print('Q', Q, 'solutions', len(r), 'distinct e', len(es))
    if len(sys.argv) > 2:
        for x in r[:40]:
            print('  e=%d t1=%d t2=%d n1=%d X=%d Y=%d  e/Q=%.3f' % (x + (x[0] / Q,)))
