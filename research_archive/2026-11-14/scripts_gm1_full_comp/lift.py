"""k-th level: P = 2*3^k, a = 2*3^(k-1) or 4*3^(k-1) (mod P), all b mod P, s in {1,2}: any failures?
Also test the candidate closed-form rule xi_r = pi(floor(r/3^(k-1)) mod 3) composed with parity, printed if found."""
import sys, time
src = open("dyadic_period.py").read().split("if __name__")[0]
exec(src)
for k in map(int, sys.argv[1:]):
    P = 2 * 3 ** k; t0 = time.time(); bad = []
    for am in (2 * 3 ** (k - 1), 4 * 3 ** (k - 1)):
        for bm in range(P):
            for s in (1, 2):
                sh = [(am, 0), (bm, s), ((bm + 1) % P, s - 3)]
                seq = solve_mod(P, sh)
                if seq is None or not check(seq, sh): bad.append((am, bm, s))
    print("k", k, "P", P, "failures", bad, "time %.1f" % (time.time() - t0), flush=True)
