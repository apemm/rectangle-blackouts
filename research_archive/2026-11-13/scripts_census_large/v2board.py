"""consolidated_board_v2 (B0)-(B7) on top of the validated lstar.py: same classes and placement,
v2 removal rules R-a, R-b (with the k = 2 extension, odd row >= T* - 444), R-c.
Census-driven relocation of the counted families is done by the driver."""
import os
import lstar
from lstar import params, admissible_primes, type_params
from functools import lru_cache

@lru_cache(maxsize=None)
def diag_graph(h, s):
    return lstar.diag_graph(h, s)

@lru_cache(maxsize=None)
def _greedy(h, s):
    I, D = diag_graph(h, s)
    return lstar.greedy(I, D)


EXT444 = os.environ.get('NOEXT444') is None   # set NOEXT444=1 to test Lemma S1L without the extension


def removal_v2(h, tp, i, j, mode):
    why = []
    if i == 0:
        why.append('R-a i0')
    if tp['r0'] == 3 and (i == 2 or j in (0, 1)):
        why.append('R-a row3')
    if mode in ('exact', 'exactS1L'):
        if max(2 * i + 1, 2 * j + 2) >= tp['Ts'] - 320:
            why.append('R-b 320')
        if mode == 'exact' and tp['k'] == 2 and 2 * i + 1 >= tp['Ts'] - 444:
            why.append('R-b 444')
        if 2 * i + 1 <= 300:
            why.append('R-c')
    return why


def build_type_v2(h, iota, sigma, l, p, seed=1, mode='exact', nosplit=False, reloc=None, graph=False):
    """As lstar.build_type (same rng sequence, same groups, same placement), v2 removal rules.
    reloc: set of (i, j) of this type to relocate in addition."""
    P = params(h); B = P['B']
    tp = type_params(h, iota, sigma)
    import random
    rng = random.Random(seed * 1000003 + iota * 101 + sigma)
    mod = 16 * l
    pinv = pow(p, -1, mod)
    subs = []; heavy = []
    for s in range(-P['A'] + 1, P['K']):
        if (s - sigma) % 16:
            continue
        I, D = diag_graph(h, s)
        if not I:
            continue
        kT = len(D); T = 2 * s + 1
        if kT >= B:
            heavy.append((T, kT)); continue
        col = _greedy(h, s)
        cT = max(col.values()) + 1
        KT = 1 if nosplit else B // cT
        rho = (pinv * (s - 0)) % mod
        groups = {}
        for i in I:
            if i % 32 != iota:
                continue
            psi = rng.randrange(B // cT)   # draw as lstar does, so the rng stream is identical
            if nosplit:
                psi = 0
            groups.setdefault((0, 0) if os.environ.get('NOCOLOUR') else (col[i], psi), []).append(i)
        for k, key in enumerate(sorted(groups)):
            t = rho + mod * k
            labs = []; rem = []
            gr = {}
            if graph:
                from bsplit import graph_reloc
                gr = graph_reloc(h, tp, [(i, i + s) for i in groups[key]])
            for i in groups[key]:
                j = i + s
                why = removal_v2(h, tp, i, j, mode) + gr.get((i, j), [])
                if reloc and (i, j) in reloc:
                    why.append('census-relocated')
                (rem if why else labs).append((i, j, why) if why else (i, j))
            subs.append(dict(s=s, T=T, kT=kT, cT=cT, KT=KT, key=key, k=k, t=t, labels=labs, removed=rem))
    return tp, subs, heavy
