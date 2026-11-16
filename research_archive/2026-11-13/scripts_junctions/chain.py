# Seams between two pure pieces (one point per column). Reports obstructions touching both pieces,
# and also all obstructions (pieces themselves). Usage: py chain.py h pieceL pieceR
# piece syntax: row1 | rowh | rowg | sea1 | sea3 | saw<r1>p<phase>
import sys
import numpy as np
from seam import Wh, triples, mixed, rivals, reps_table, saw_rows

def piece_row(name, x, h, g):
    if name == 'row1':
        return 1
    if name == 'rowh':
        return h
    if name == 'rowg':
        return g
    if name in ('sea1', 'sea3'):
        r0 = 1 if name == 'sea1' else 3
        return g if x % 4 == 0 else r0
    raise ValueError(name)

def run_pair(h, g, L, R, verbose=True):
    W = Wh(h)
    m = 4 * (2 * W + 8)
    z0 = (m // 2) // 4 * 4
    row = np.zeros(m, dtype=np.int64); kind = np.zeros(m, dtype=np.int64)
    for x in range(m):
        nm = L if x < z0 else R
        row[x] = piece_row(nm, x, h, g); kind[x] = 0 if x < z0 else 1
    out = np.zeros((2000000, 8), dtype=np.int64)
    c = triples(row, h, m, W, out); tri = out[:min(c, out.shape[0])]
    rs, ra, rb = reps_table(h, W)
    out2 = np.zeros((2000000, 8), dtype=np.int64)
    c2 = mixed(row, h, m, W, rs, ra, rb, out2); mq = out2[:min(c2, out2.shape[0])]
    out3 = np.zeros((200000, 4), dtype=np.int64)
    c3 = rivals(row, h, m, W, out3); rv = out3[:min(c3, out3.shape[0])]
    fatal = 0; park = {}
    for t in tri:
        xv, yv, xp, yp, xq, yq, xf, yf = [int(v) for v in t]
        if row[xf] == yf or (row[xf] - yf) % 2 != 0:
            fatal += 1
        else:
            park.setdefault((xf, yf), []).append(1)
    v3 = sum(1 for l in park.values() if len(l) > 1)
    res = (fatal, sum(len(l) for l in park.values()), v3, c2, c3)
    if verbose:
        print(f"h={h} g={g} {L}|{R}: (fatal, parked, V3, MQ, RIV) = {res}")
        for r in rv[:3]:
            print('   rival', tuple(int(v) for v in r))
    return res

if __name__ == '__main__':
    h, g = int(sys.argv[1]), int(sys.argv[2])
    for pair in sys.argv[3:]:
        L, R = pair.split('|')
        run_pair(h, g, L, R)
