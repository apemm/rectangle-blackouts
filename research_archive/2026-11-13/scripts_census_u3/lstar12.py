"""Board L***(u) at u = 3 (stride 12): L***U of consolidated_board_v4.md with slot n = 3 i + p t + b
(column 4n) and p > 76h (stride_menu Lemma 4, s = 12).  Everything else as in v4 (B0)-(B7):
 - types tau = (i mod 32, s mod 16), r0, y_P, T0, D0, k (Table J1*), T* and fillers: lstar.type_params
   (unchanged: they do not depend on the stride);
 - D_T at stride 12: {|d| : 0 < |d| < n_T, 144 d^2 + (2d + T)^2 = L^2, 0 < L < h}  (stride_menu
   Derivation 2, sigma = 6);  kappa_T = |D_T|;  heavy iff kappa_T >= B/4 (v4 (B1));
 - G_T[tau]: slots i of T with i = iota (mod 32), i ~ i' iff |i - i'| in D_T;
 - colouring law (B4): uniform random proper B-colouring of G_T[tau] (exact, by rejection sampling);
   colour k sits at t = rho_s + 16 l k, rho_s = p^(-1)(s - kappa) mod 16 l (B5), kappa = b = 0.
Colour modes: 'board' (the law above), 'stress' (greedy colouring of G_T[tau], fewest classes:
 not the board, stresses the in-class cells), 'nocolour' (one class per (T, tau), ignores G_T:
 positive control, not the board).
Removal modes: 'relaxed' = R-a only; 'exact' = R-a, R-b (with the k = 2 extension), R-c."""
import math, random, os
from math import isqrt
from lstar import is_prime, type_params

THETA = 1.4967429
U = 3          # slot multiplier: stride 4U = 12


def params(h):
    A = (h + 1) // 2; K = h // 2
    W = (h - 1) ** 2 // 4 + 1
    B = math.ceil(math.log(h) ** THETA)
    return dict(h=h, A=A, K=K, W=W, B=B)


def primes12(h):
    l = next(l for l in range(int(1.04 * h) + 1, int(2.08 * h) + 1) if l % 5 in (2, 3) and is_prime(l) and l > 1.04 * h)
    pmin = (8 * U * U + 4) * h          # 76 h
    p = next(p for p in range(pmin + 1, 2 * pmin + 1) if p % 20 in (3, 7) and is_prime(p))
    return l, p


from functools import lru_cache


@lru_cache(maxsize=None)
def diag_graph12(h, s):
    A = (h + 1) // 2; K = h // 2
    T = 2 * s + 1
    I = [i for i in range(A) if 0 <= i + s < K]
    n = len(I)
    D = set()
    ss = (4 * U) ** 2
    for d in range(-n + 1, n):
        if d == 0:
            continue
        v = ss * d * d + (2 * d + T) ** 2
        L = isqrt(v)
        if L * L == v and 0 < L < h:
            D.add(abs(d))
    return I, sorted(D)


def colour(V, D, B, mode, rng):
    """Return dict vertex -> colour for the graph on V with distance set D."""
    Ds = set(D)
    E = [(a, b) for x, a in enumerate(V) for b in V[x + 1:] if abs(a - b) in Ds]
    if mode == 'nocolour':
        return {v: 0 for v in V}, E
    if mode == 'stress':
        col = {}
        for v in V:
            used = {col[w] for w in col if abs(v - w) in Ds}
            c = 0
            while c in used:
                c += 1
            col[v] = c
        return col, E
    # uniform proper B-colouring, exact by rejection
    for _ in range(100000):
        col = {v: rng.randrange(B) for v in V}
        if all(col[a] != col[b] for a, b in E):
            return col, E
    raise RuntimeError('rejection sampling failed')


def removal(tp, i, j, mode):
    why = []
    if i == 0:
        why.append('R-a')
    if tp['r0'] == 3 and (i == 2 or j in (0, 1)):
        why.append('R-a(row3)')
    if mode == 'exact':
        if max(2 * i + 1, 2 * j + 2) >= tp['Ts'] - 320:
            why.append('R-b')
        if tp['k'] == 2 and 2 * i + 1 >= tp['Ts'] - 444:
            why.append('R-b(444)')
        if 2 * i + 1 <= 300:
            why.append('R-c')
    return why


def build_type12(h, iota, sigma, cmode='board', rmode='relaxed', seed=1, kappa=0, b=0, reloc=None):
    P = params(h); B = P['B']
    l, p = primes12(h)
    tp = type_params(h, iota, sigma)
    rng = random.Random(seed * 1000003 + iota * 101 + sigma)
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
        if os.environ.get('CONSEC'):          # positive control only: consecutive slots, all residues
            V = I[:int(os.environ['CONSEC'])]
        if not V:
            continue
        if 4 * kT >= B:            # heavy: kappa_T >= B/4
            heavy.append((T, kT, len(V)))
            continue
        col, E = colour(V, D, B, cmode, rng)
        nedges += len(E)
        rho = (pinv * (s - kappa)) % mod
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
    return dict(P=P, l=l, p=p, tp=tp, subs=subs, heavy=heavy, nedges=nedges)


def slot(i, t, p, b=0):
    return U * i + p * t + b
