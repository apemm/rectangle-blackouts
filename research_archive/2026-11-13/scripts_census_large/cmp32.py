"""Compare the census with the int64 divisor table (validated) and the int32 table, window by window."""
import sys, time
import checker, core
from v2board import build_type_v2, params, admissible_primes
from classify import WinBoard, run
import importlib.util
spec = importlib.util.spec_from_file_location('cv', 'census_v2.py')
h, a, b, nmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
from census_v2_tables import divisor_table32
P = params(h); W = P['W']; ls, ps = admissible_primes(h); l, p = ls[0], ps[0]
tp, subs, _ = build_type_v2(h, a, b, l, p, mode='exact')
T64 = core.divisor_table(h * h); T32 = divisor_table32(h * h)
nw = 0; same = 0; nv = 0; t0 = time.time()
for sc in subs:
    if not sc['labels'] or nw >= nmax or time.time() - t0 > 40: continue
    labs = {i + p * sc['t']: (i, j) for (i, j) in sc['labels']}
    rho0 = next(iter(labs)) % 4; X0 = 4 * min(labs) - 2 * W - 64; Wd = 4 * (max(labs) - min(labs)) + 4 * W + 129
    bd = WinBoard(h, X0, Wd, tp, rho0, labels=labs)
    anc = []; wan = []
    for n, (i, j) in labs.items():
        x = 4 * n - X0; anc += [(x, 2 * i + 1), (x, 2 * j + 2)]
        wan += [(x, y) for y in range(1, h + 1) if y not in (2 * i + 1, 2 * j + 2)]
    res = []
    for T in (T64, T32):
        checker._DIV.clear(); checker._DIV[h * h] = T
        out, oob = run(bd, anc, wan)
        res.append(sorted((k, f, str(d)) for (k, f, _, d) in out))
    nw += 1; same += res[0] == res[1]; nv += len(res[0])
print('windows', nw, 'identical', same, 'violations', nv)
