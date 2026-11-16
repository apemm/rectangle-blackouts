"""Board L***(3) with the TWISTED rule of stride_transfer_core.md (B2'), (B5').
Differences from lstar12.py (the untwisted census board):
 (B2') l = least prime in (1.04h, 2.08h] with (37/l) = -1;
       p = least prime in (76h, 152h] with p = 3 (mod 4) and (37/p) = -1;
 (B5') rho_s = p^(-1)(3 s - kappa) mod 16 l, class k at t = rho_s + 16 l k, slot n = 3 i + p t + b, column 4n.
Everything else (types, D_T at stride 12, heavy threshold B/4, G_T[tau], colouring law, removal rules,
T*, fillers, sea) is imported unchanged from lstar12.py / lstar.py.
kappa = b = 0 by default, so kappa_tau = kappa - b = 0 and rho_tau = 3(iota + sigma) (mod 16)."""
import os, random
from lstar import is_prime, type_params
from lstar12 import params, diag_graph12, colour, removal, U

DELTA = 4 * U * U + 1      # 37
PU = 8 * U * U + 4         # 76


def legendre(a, q):
    """Euler's criterion; q an odd prime not dividing a."""
    r = pow(a % q, (q - 1) // 2, q)
    return -1 if r == q - 1 else r


def primes12t(h):
    l = next(l for l in range(int(1.04 * h) + 1, int(2.08 * h) + 1)
             if l > 1.04 * h and is_prime(l) and legendre(DELTA, l) == -1)
    p = next(p for p in range(PU * h + 1, 2 * PU * h + 1)
             if p % 4 == 3 and is_prime(p) and legendre(DELTA, p) == -1)
    return l, p


def build_type12t(h, iota, sigma, cmode='board', rmode='relaxed', seed=1, kappa=0, b=0, reloc=None):
    P = params(h); B = P['B']
    l, p = primes12t(h)
    tp = type_params(h, iota, sigma)
    rng = random.Random(seed * 1000003 + iota * 101 + sigma)     # same stream as lstar12.build_type12
    mod = 16 * l
    pinv = pow(p, -1, mod)
    subs = []; heavy = []; nedges = 0
    for s in range(-P['A'] + 1, P['K']):
        if (s - sigma) % 16:
            continue
        I, D = diag_graph12(h, s)
        if not I:
            continue
        T = 2 * s + 1
        kT = len(D)
        V = [i for i in I if i % 32 == iota]
        if not V:
            continue
        if 4 * kT >= B:
            heavy.append((T, kT, len(V)))
            continue
        col, E = colour(V, D, B, cmode, rng)
        nedges += len(E)
        rho = (pinv * (U * s - kappa)) % mod          # (B5') u-twist
        groups = {}
        for i in V:
            groups.setdefault(col[i], []).append(i)
        for c in sorted(groups):
            t = rho + mod * c
            labs = []; rem = []
            for i in groups[c]:
                j = i + s
                why = removal(tp, i, j, rmode)
                if reloc is not None and (iota, sigma, i, j) in reloc:
                    why.append('relocated')
                (rem.append((i, j, why)) if why else labs.append((i, j)))
            subs.append(dict(s=s, T=T, kT=kT, D=D, colour=c, t=t, labels=labs, removed=rem, E=E))
    return dict(P=P, l=l, p=p, tp=tp, subs=subs, heavy=heavy, nedges=nedges, b=b, kappa=kappa)


def slot(i, t, p, b=0):
    return U * i + p * t + b
