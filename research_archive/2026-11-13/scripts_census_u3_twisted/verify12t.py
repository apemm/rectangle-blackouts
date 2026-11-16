"""Re-check reported stride-12 instances from scratch.  Blackness is computed from the (B5)/(B6) formulas
(slot n = 3 i + p t, column 4n; filler row T* - 24 + 8((n - rho0) mod 4); shallow row r0), not from WinBoard.
Then the defining equations are tested: Lemma mixedeq (V4), Lemma rival (V5), corners and parity (V2).
usage: py verify12.py 'logglob' kmax"""
import sys, re, glob, random, os
from lstar12t import build_type12t as build_type12, slot
random.seed(2)
cache = {}
def black_fn(h, io, sg, cmode, rmode, sub, reloc):
    key = (h, io, sg, cmode, rmode, reloc)
    if key not in cache:
        rl = set(tuple(map(int, l.split())) for l in open('reloc701.txt')) if reloc else None
        cache[key] = build_type12(h, io, sg, cmode, rmode, reloc=rl)
    R = cache[key]; p = R['p']; tp = R['tp']; sc = R['subs'][sub]
    labs = {slot(i, sc['t'], p): (i, j) for (i, j) in sc['labels']}
    rho0 = next(iter(labs)) % 4
    def black(X, y):
        if X % 4:
            return y == tp['r0']
        n = X // 4
        if n in labs:
            i, j = labs[n]; return y in (2 * i + 1, 2 * j + 2)
        return y == tp['Ts'] - 24 + 8 * ((n - rho0) % 4)
    def colrows(X):
        if X % 4: return [tp['r0']]
        n = X // 4
        if n in labs: i, j = labs[n]; return [2 * i + 1, 2 * j + 2]
        return [tp['Ts'] - 24 + 8 * ((n - rho0) % 4)]
    return black, colrows
ok = bad = 0
lines = []
for f in glob.glob(sys.argv[1]):
    parts = f[:-4].split('_')
    h, io, sg, cmode, rmode = int(parts[1]), int(parts[2]), int(parts[3]), parts[4], parts[5]
    reloc = f.endswith('_reloc.txt')
    for ln in open(f):
        if ln.startswith('VIOL'):
            lines.append((h, io, sg, cmode, rmode, reloc, ln))
random.shuffle(lines)
for h, io, sg, cmode, rmode, reloc, ln in lines[:int(sys.argv[2])]:
    sub = int(ln.split()[2]); kind = re.search(r'kind (\w+)', ln).group(1)
    X0 = int(re.search(r' X0 (-?\d+)', ln).group(1))
    data = eval(re.search(r'data (\(.*\))', ln).group(1))
    black, colrows = black_fn(h, io, sg, cmode, rmode, sub, reloc)
    G = lambda z: (z[0] + X0, z[1])
    blk = lambda z: black(*G(z))
    if kind == 'V4':
        A, B, C, D, pp, q = data
        n = (pp[0] - A[0], pp[1] - A[1]); u = (B[0] - A[0], B[1] - A[1])
        good = (q == (B[0] + n[0], B[1] + n[1]) and n != (0, 0) and n[0] * u[0] + n[1] * u[1] == 0
                and C[0] + D[0] == A[0] + B[0] + 2 * n[0] and C[1] + D[1] == A[1] + B[1] + 2 * n[1]
                and (D[0]-C[0])**2 + (D[1]-C[1])**2 == u[0]**2 + u[1]**2
                and (D[0]-C[0], D[1]-C[1]) not in (u, (-u[0], -u[1])) and u[0] != 0
                and all(1 <= z[1] <= h for z in (A, B, C, D, pp, q)) and all(blk(z) for z in (A, B, C, D)))
    elif kind == 'V5':
        C = (data[0], data[1]); D = (data[2], data[3]); j = data[4]
        t = D[0] - C[0]; lo, hi = sorted((C[1], D[1]))
        good = (blk(C) and blk(D) and (hi - lo) % 2 == 1 and t != 0 and 4 * j * (hi - lo + j) == t * t and lo - j >= 1 and hi + j <= h)
    elif kind == 'V2':
        Q, W_ = data
        V, F, Wc, Gp = Q
        good = ((F[0]-V[0])*(Gp[0]-V[0]) + (F[1]-V[1])*(Gp[1]-V[1]) == 0 and Wc == (F[0]+Gp[0]-V[0], F[1]+Gp[1]-V[1])
                and sum(blk(z) for z in Q) == 3 and not blk(W_) and any((r - W_[1]) % 2 for r in colrows(G(W_)[0]))
                and all(1 <= z[1] <= h for z in Q))
    else:
        good = None
    ok += bool(good); bad += (good is False)
    if good is False: print('FAILED', ln[:200])
print('re-checked', ok + bad, 'ok', ok, 'failed', bad, 'of', len(lines), 'lines')
