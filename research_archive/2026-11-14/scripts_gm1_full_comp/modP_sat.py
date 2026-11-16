"""For period P: which (a mod P != 0, b mod P, s) M=3 two-gap systems have NO solution on Z/P? (pysat)"""
import sys
src = open("dyadic_period.py").read().split("if __name__")[0]
exec(src)
for P in map(int, sys.argv[1:]):
    bad = []
    for am in range(1, P):
        for bm in range(P):
            for s in (1, 2):
                sh = [(am, 0), (bm, s), ((bm + 1) % P, s - 3)]
                seq = solve_mod(P, sh)
                if seq is None or not check(seq, sh): bad.append((am, bm, s))
    print("P", P, "unsolvable with a mod P != 0:", len(bad), bad[:12])
