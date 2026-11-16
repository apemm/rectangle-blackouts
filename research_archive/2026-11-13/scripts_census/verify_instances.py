"""Re-check reported instances from scratch: rebuild the subclass window and test the defining
equations directly (Lemma mixedeq for V4; Lemma rival for V5; corners and parity for V2)."""
import sys, re, glob, random
from math import isqrt
from lstar import params, admissible_primes, build_type
from classify import WinBoard
random.seed(1)
def board_for(h, a, b, mode, sub):
    P = params(h); W = P['W']; ls, ps = admissible_primes(h); l, p = ls[0], ps[0]
    tp, subs, heavy = build_type(h, a, b, l, p, seed=1, mode=mode)
    sc = subs[sub]; labs = {i + p * sc['t']: (i, j) for (i, j) in sc['labels']}
    rho0 = next(iter(labs)) % 4; n_lo, n_hi = min(labs), max(labs)
    X0 = 4 * n_lo - 2 * W - 64; Wd = 4 * (n_hi - n_lo) + 4 * W + 129
    return WinBoard(h, X0, Wd, tp, rho0, labels=labs)
ok = bad = 0
for pat, mode, kmax in ((sys.argv[1], sys.argv[2], int(sys.argv[3])),):
    lines = []
    for f in glob.glob(pat):
        h, a, b = map(int, f.split('_')[2:5])
        for ln in open(f):
            if ln.startswith('VIOL') and (len(sys.argv) < 5 or sys.argv[4] in ln):
                lines.append((h, a, b, ln))
    random.shuffle(lines)
    for h, a, b, ln in lines[:kmax]:
        sub = int(ln.split()[2]); kind = re.search(r'kind (\w+)', ln).group(1)
        data = eval(re.search(r'data (\(.*\))', ln).group(1))
        bd = board_for(h, a, b, mode, sub)
        blk = lambda z: bool(bd.black(*z))
        if kind == 'V4':
            A, B, C, D, p, q = data
            n = (p[0] - A[0], p[1] - A[1]); u = (B[0] - A[0], B[1] - A[1])
            good = (q == (B[0] + n[0], B[1] + n[1]) and n != (0, 0) and n[0] * u[0] + n[1] * u[1] == 0
                    and C[0] + D[0] == A[0] + B[0] + 2 * n[0] and C[1] + D[1] == A[1] + B[1] + 2 * n[1]
                    and (D[0]-C[0])**2 + (D[1]-C[1])**2 == u[0]**2 + u[1]**2
                    and (D[0]-C[0], D[1]-C[1]) not in (u, (-u[0], -u[1])) and u[0] != 0
                    and all(1 <= z[1] <= h for z in (A, B, C, D, p, q)) and all(blk(z) for z in (A, B, C, D)))
        elif kind == 'V5':
            C = (data[0], data[1]); D = (data[2], data[3]); j = data[4]
            t = D[0] - C[0]; lo, hi = sorted((C[1], D[1]))
            good = (blk(C) and blk(D) and (hi - lo) % 2 == 1 and t != 0 and 4 * j * (hi - lo + j) == t * t and lo - j >= 1 and hi + j <= h)
        elif kind == 'V2':
            Q, W_ = data
            V, F, Wc, G = Q
            good = ((F[0]-V[0])*(G[0]-V[0]) + (F[1]-V[1])*(G[1]-V[1]) == 0 and Wc == (F[0]+G[0]-V[0], F[1]+G[1]-V[1])
                    and sum(blk(z) for z in Q) == 3 and not blk(W_) and any((r - W_[1]) % 2 for r in bd.colrows(W_[0]))
                    and all(1 <= z[1] <= h for z in Q))
        else:
            good = None
        ok += bool(good); bad += (good is False)
        if good is False: print('FAILED', ln[:200])
print('re-checked', ok + bad, 'ok', ok, 'failed', bad)
