import sys, time
from seam import run, saw_rows

def grule(h):
    if h % 2 == 0:
        return h
    return h - 1 if h % 4 == 1 else h - 3

def bad_pairs(h, g, r1):
    # predicted (offset o, kappa) rival pairs filler-row-g, with offset o -> row T*-24+8o
    rows, Ts = saw_rows(h, r1)
    res = []
    for o, c in enumerate(rows):
        lo, hi = (c, g) if c < g else (g, c)
        for j in range(1, min(lo - 1, h - hi) + 1):
            v = 4 * j * (hi - lo + j)
            t = int(round(v ** 0.5))
            if t > 0 and t * t == v and t % 4 == 0:
                res.append((o, t // 4, j))
    return res

def rule_phase(o, kap, side):
    # our phase convention: slot n0-1-k (left side R) has offset (phase-1-k) mod 4.
    # right end (side R): last kap slots must avoid offset o -> phase = o+kap+1
    # left end (side L): first kap slots (offsets phase..phase+kap-1) avoid o -> phase = o+1
    return (o + kap + 1) % 4 if side == 'R' else (o + 1) % 4

if __name__ == '__main__':
    hs = [int(a) for a in sys.argv[1].split(',')]
    mode = sys.argv[2]  # 'rule' or 'all'
    t0 = time.time()
    for h in hs:
        g = grule(h)
        for r1 in ([3, 7, 11, 15, 1, 5, 9, 13]):
            r0 = 1 if r1 % 4 == 3 else 3
            bp = bad_pairs(h, g, r1)
            for side in ['R', 'L']:
                if mode == 'rule':
                    phases = [rule_phase(bp[0][0], bp[0][1], side)] if bp else [0]
                else:
                    phases = [0, 1, 2, 3]
                for ph in phases:
                    res = run(h, r0, r1, g, ph, side, verbose=False)
                    flag = '' if res == (0, 0, 0, 0) else '  <-- NONZERO'
                    print(f"h={h} g={g} r0={r0} r1={r1:2d} side={side} phase={ph} bad={bp} (fatal,V3,MQ,RIV)={res}{flag}", flush=True)
                    if time.time() - t0 > 50:
                        print('time limit'); sys.exit()
