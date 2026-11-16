def maxclique_list(d):
    s = set(d)
    adj = {a: {b for b in d if b != a and abs(a - b) in s} for a in d}
    best = [[]]
    def bk(R, P):
        if len(R) + len(P) <= len(best[0]): return
        if not P:
            best[0] = R[:]; return
        for v in sorted(P):
            if len(R) + len(P) <= len(best[0]): return
            bk(R + [v], P & adj[v]); P = P - {v}
    bk([], set(d)); return sorted(best[0])
