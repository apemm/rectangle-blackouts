"""Board L*** of consolidated_board.md (B1)-(B10): parameters, region types, classes, windows."""
import math, random, os
from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    for q in range(2, isqrt(n) + 1):
        if n % q == 0:
            return False
    return True


def params(h):
    A = (h + 1) // 2; K = h // 2
    W = (h - 1) ** 2 // 4 + 1
    Lam = math.log(h)
    B = math.ceil(Lam ** 1.5)
    return dict(h=h, A=A, K=K, W=W, B=B)


def admissible_primes(h):
    ls = [l for l in range(int(1.04 * h) + 1, int(2.08 * h) + 1) if l % 5 in (2, 3) and is_prime(l) and l > 1.04 * h]
    ps = [p for p in range(40 * h + 1, 80 * h + 1) if p % 20 in (3, 7) and is_prime(p)]
    return ls, ps


def g_of(h):
    if h % 2 == 0:
        return h
    return h - 1 if h % 4 == 1 else h - 3


# Table J1* shifts (consolidated_board.md (B6), TABLE J1*)
def k_shift(h, r0, D0):
    if h % 2 == 0:
        return 0
    if h % 4 == 1:
        return 0 if r0 == 1 else {40: 1, 48: 1, 56: 2}.get(D0, 0)
    return {24: 1, 32: 1, 40: 1, 48: 1}.get(D0, 0) if r0 == 1 else {42: 1, 50: 1, 58: 2}.get(D0, 0)


# Table J1* bad pairs (o, kappa) of the k = 0 rows
def j1star_bad(h, r0, D):
    if h % 2 == 0:
        return []
    if h % 4 == 1:
        if r0 == 1:
            return []
        tab = {0: (1, 2), 4: (3, 1), 8: (2, 2), 12: (0, 3), 16: (3, 2), 20: (1, 3), 28: (2, 3), 36: (3, 3)}
        return [tab[D]] if D in tab else []
    if r0 == 1:
        tab = {4: (2, 3), 12: (3, 3)}
        return [tab[D]] if D in tab else []
    tab = {2: (1, 2), 6: (3, 1), 10: (2, 2), 14: (0, 3), 18: (3, 2), 22: (1, 3), 30: (2, 3), 38: (3, 3)}
    return [tab[D]] if D in tab else []


def type_params(h, iota, sigma):
    r0 = 1 if iota % 2 else 3
    yP = (2 * iota + 1) % 64
    Tmod4 = (2 * sigma + 1) % 4
    add = 32 if Tmod4 == 3 else 48
    T0 = max(y for y in range(1, h + 1) if (y - yP - add) % 64 == 0)
    D0 = h - T0
    k = k_shift(h, r0, D0)
    Ts = T0 - 64 * k
    return dict(iota=iota, sigma=sigma, r0=r0, yP=yP, T0=T0, D0=D0, k=k, Ts=Ts,
                frows=[Ts - 24 + 8 * o for o in range(4)])


def diag_graph(h, s):
    """I_T, D_T, k_T for stride 4 (stride_menu.md Derivation 2, sigma = 2)."""
    A = (h + 1) // 2; K = h // 2
    T = 2 * s + 1
    I = [i for i in range(A) if 0 <= i + s < K]
    n = len(I)
    D = set()
    for d in range(-n + 1, n):
        if d == 0:
            continue
        v = 16 * d * d + (2 * d + T) ** 2
        L = isqrt(v)
        if L * L == v and 0 < L < h:
            D.add(abs(d))
    return I, sorted(D)


def greedy(I, D):
    col = {}
    Iset = set(I)
    for i in I:
        used = set(col[i - d] for d in D if (i - d) in col)
        c = 0
        while c in used:
            c += 1
        col[i] = c
    return col


def build_type(h, iota, sigma, l, p, kappa=0, b=0, seed=1, mode='relaxed'):
    """Return the type's subclasses: list of dict(s, T, k, t, labels=[(i,j)], removed=[(i,j,why)])."""
    P = params(h); B = P['B']
    tp = type_params(h, iota, sigma)
    rng = random.Random(seed * 1000003 + iota * 101 + sigma)
    mod = 16 * l
    pinv = pow(p, -1, mod)
    subs = []
    heavy = []
    for s in range(-P['A'] + 1, P['K']):
        if (s - sigma) % 16:
            continue
        I, D = diag_graph(h, s)
        if not I:
            continue
        kT = len(D)
        T = 2 * s + 1
        if kT >= B:
            heavy.append((T, kT))
            continue
        col = greedy(I, D)
        cT = max(col.values()) + 1
        KT = B // cT
        if os.environ.get('NOSPLIT'):
            KT = 1
        rho = (pinv * (s - kappa)) % mod
        groups = {}
        for i in I:
            if i % 32 != iota:
                continue
            psi = rng.randrange(KT)
            groups.setdefault((col[i], psi), []).append(i)
        for k, key in enumerate(sorted(groups)):
            t = rho + mod * k
            labs = []; rem = []
            for i in groups[key]:
                j = i + s
                why = removal(h, tp, i, j, mode)
                if why:
                    rem.append((i, j, why))
                else:
                    labs.append((i, j))
            subs.append(dict(s=s, T=T, kT=kT, cT=cT, KT=KT, key=key, k=k, t=t, labels=labs, removed=rem,
                             slots=[i + p * t + b for i in groups[key]]))
    return tp, subs, heavy


_REL = None
def removal(h, tp, i, j, mode):
    global _REL
    why = []
    if mode == 'exact2':
        if _REL is None:
            _REL = set(tuple(map(int, ln.split())) for ln in open(os.environ['RELOC']) if ln.strip())
        if (tp['iota'], tp['sigma'], i, j) in _REL:
            why.append('D10/D11 relocated')
        mode = 'exact'
    if i == 0:
        why.append('i0')
    if tp['r0'] == 3 and (i == 2 or j in (0, 1)):
        why.append('row3')
    if mode == 'exact':
        if max(2 * i + 1, 2 * j + 2) >= tp['Ts'] - 320:
            why.append('nearband320')
        if 2 * i + 1 <= 300:
            why.append("R2'")
    return why


def filler_row(tp, n, rho0):
    return tp['Ts'] - 24 + 8 * ((n - rho0) % 4)
