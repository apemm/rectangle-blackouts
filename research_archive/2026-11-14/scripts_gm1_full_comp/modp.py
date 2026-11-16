"""Solvability of the M=3 two-gap system on Z/P as a function of (a mod P, b mod P, s)."""
import sys, itertools
def ok(seq, sh):
    P = len(seq); return all(seq[(k + a) % P] - seq[k] != d for a, d in sh for k in range(P))
for P in map(int, sys.argv[1:]):
    seqs = list(itertools.product(range(3), repeat=P))
    bad = []
    for am in range(P):
        for bm in range(P):
            for s in (1, 2):
                sh = [(am, 0), (bm, s), ((bm + 1) % P, s - 3)]
                if not any(ok(q, sh) for q in seqs): bad.append((am, bm, s))
    print("P", P, "unsolvable (a mod P, b mod P, s) with a mod P != 0:", [t for t in bad if t[0] != 0])
