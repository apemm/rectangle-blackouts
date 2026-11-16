"""Re-check reported instances from the definitions, independently of the checker and of WinBoard:
blackness from the (B5)/(B6) formulas, Lemma mixedeq for V4, Lemma rival for V5."""
import re, ast, glob, random, os
from v2board import build_type_v2, params, admissible_primes
random.seed(2)
cache = {}
def ctx(h, a, b, mode, graph, f):
    key = (h, a, b, mode, graph)
    if key not in cache:
        P = params(h); ls, ps = admissible_primes(h); l, p = ls[0], ps[0]
        tp, subs, _ = build_type_v2(h, a, b, l, p, mode=mode, graph=graph)
        cache[key] = (P, p, tp, subs)
    return cache[key]
ok = bad = 0
lines = []
for f in glob.glob('log_exact*_split_*.txt'):
    if 'closure' in f or 'rho' in f: continue
    parts = f[:-4].split('_'); mode = parts[1]; h, a, b = map(int, parts[3:6]); graph = f.endswith('_graph.txt')
    for ln in open(f):
        if ln.startswith('VIOL'):
            lines.append((h, a, b, mode, graph, f, ln))
multi = [x for x in lines if ast.literal_eval(re.search(r' labels (\[.*?\]) oob', x[6]).group(1)).__len__() >= 2]
d11 = [x for x in lines if 'D11' in x[6]]
rest = [x for x in lines if 'D10' in x[6]]
sample = multi + random.sample(d11, min(60, len(d11))) + random.sample(rest, 60)
for (h, a, b, mode, graph, f, ln) in sample:
    P, p, tp, subs = ctx(h, a, b, mode, graph, f)
    W = P['W']
    sub = int(ln.split()[2]); sc = subs[sub]
    labs = {i + p * sc['t']: (i, j) for (i, j) in sc['labels']}
    rho0 = next(iter(labs)) % 4; X0 = 4 * min(labs) - 2 * W - 64
    def blk(z):
        X = z[0] + X0; y = z[1]
        if X % 4: return y == tp['r0']
        n = X // 4
        if n in labs: return y in (2 * labs[n][0] + 1, 2 * labs[n][1] + 2)
        return y == tp['Ts'] - 24 + 8 * ((n - rho0) % 4)
    kind = re.search(r'kind (\w+)', ln).group(1)
    data = ast.literal_eval(re.search(r' data (\(.*\))', ln).group(1))
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
    else:
        good = None
    ok += good is True; bad += good is False
    if good is not True: print('NOT OK', good, f, ln[:200])
print('re-checked', ok + bad, 'ok', ok, 'failed', bad, '(multi-label', len(multi), ', D11 sample', min(60, len(d11)), ', D10 sample 60)')
