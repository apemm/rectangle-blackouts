# Sanity check of Lemma 5.1: edges spanned by a neighbourhood in G_T are at most 6|D_T| + R_T.
# Also prints how many diagonals are triangle-free.
import sys, math
from math import gcd
from collections import defaultdict

def build(h):
    S = defaultdict(set)
    u = 2
    while u * u + 1 < h:
        for v in range(1, u):
            if (u - v) % 2 == 0 or gcd(u, v) != 1: continue
            L0 = u * u + v * v
            if L0 >= h: break
            d0 = u * v // 2; b0 = u * u - v * v
            g = 1
            while g * L0 < h:
                for sd in (g * d0, -g * d0):
                    for sb in (g * b0, -g * b0):
                        S[sb - 2 * sd].add(sd)
                g += 2
        u += 1
    return S

def main(h):
    S = build(h)
    A = (h + 1) // 2; K = h // 2
    ndiag = 0; tri_free = 0; viol = 0
    sum_k = 0; sum_R = 0; sum_tau = 0; sum_kl = 0.0
    worst = None
    for s in range(-(A - 1), K):
        T = 2 * s + 1
        lo = max(0, -s); hi = min(A, K - s)
        n = hi - lo
        if n <= 0: continue
        ndiag += 1
        ST = S.get(T, set())
        D = sorted({abs(d) for d in ST if abs(d) < n})
        k = len(D); sum_k += k
        sum_kl += k / math.log(2 + k)
        Dset = set(D)
        # R_T
        na = nb = 0
        for a in ST:
            for b in ST:
                c = a + b
                if c in ST and 5 * c != -T: na += 1
                if -c in ST: nb += 1
        R = 6 * na + 2 * nb; sum_R += R
        # tau_T: unordered pairs {x,y} in +-D, x != y, |x-y| in D
        pm = D + [-x for x in D]
        tau = 0
        for i in range(len(pm)):
            for j in range(i + 1, len(pm)):
                if abs(pm[i] - pm[j]) in Dset: tau += 1
        sum_tau += tau
        if tau == 0: tri_free += 1
        if tau > 6 * k + R:
            viol += 1
        if worst is None or tau > worst[0]: worst = (tau, T, k, R)
    print(f"h={h}: diagonals={ndiag} sum k={sum_k} ({sum_k/h:.3f} h), sum R={sum_R} ({sum_R/h:.3f} h), "
          f"sum tau={sum_tau} ({sum_tau/h:.3f} h), triangle-free diagonals={tri_free} ({tri_free/ndiag:.3f}), "
          f"violations of tau<=6k+R: {viol}, worst (tau,T,k,R)={worst}, "
          f"sum k/log(2+k) = {sum_kl:.0f} = {sum_kl/h:.3f} h")

for a in sys.argv[1:]:
    main(int(a))
