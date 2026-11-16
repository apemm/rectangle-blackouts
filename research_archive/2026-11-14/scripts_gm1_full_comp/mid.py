import sys, itertools
sys.argv = ["x", "0"]
src = open("dyadic_period.py").read().split("amax =")[0].replace('if __name__ != "__main__": raise SystemExit', '')
exec(src)
al = 3; H = 8; P = 16
for s in (1, 2):
    for beta in range(1, P - 1):
        sh = [(H, 0), (beta, s), (beta + 1, s - 3)]
        seq = solve_mod(P, sh)
        print("s", s, "beta", beta, "".join(map(str, seq)) if seq else None)
