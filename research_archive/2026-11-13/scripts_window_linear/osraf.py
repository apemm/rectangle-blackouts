"""Largest width of a 'one-sided' window: two points per column, distinct
K_{A,B} edges, and no tilted right angle V,X,Y with X and Y strictly on the
same horizontal side of V (no condition on rows of the fourth corner).
usage: py osraf.py h Kmax [A]
"""
import sys, time

def run(h, Kmax, A, tl):
    B = [y for y in range(1, h + 1) if y not in A]
    E = [(a, b) for a in A for b in B]
    pts = []
    used = [False] * len(E)
    best = [0, None]
    t0 = time.time()

    def ok_new(N):
        nx, ny = N
        # N rightmost.  (a) N is vertex, X,Y left of N.
        L = pts
        n = len(L)
        for i in range(n):
            X = L[i]
            if X[0] == nx: continue
            ux, uy = X[0] - nx, X[1] - ny
            if uy == 0: continue
            for j in range(i + 1, n):
                Y = L[j]
                if Y[0] == nx: continue
                vx, vy = Y[0] - nx, Y[1] - ny
                if vy == 0: continue
                if ux * vx + uy * vy == 0:
                    return False
        # (b) N is a leg end, vertex V left of N, other leg end Y with x_Y > x_V
        for V in L:
            if V[0] == nx: continue
            ux, uy = nx - V[0], ny - V[1]
            if uy == 0: continue
            for Y in L:
                if Y is V or Y[0] <= V[0]: continue
                vx, vy = Y[0] - V[0], Y[1] - V[1]
                if vy == 0: continue
                if ux * vx + uy * vy == 0:
                    return False
        return True

    def dfs(x):
        if time.time() - t0 > tl:
            raise TimeoutError
        if x - 1 > best[0]:
            best[0] = x - 1; best[1] = [(p[1]) for p in pts]
        if x > Kmax:
            return True
        for j, (a, b) in enumerate(E):
            if used[j]: continue
            p1, p2 = (x, a), (x, b)
            if not ok_new(p1): continue
            pts.append(p1)
            if ok_new(p2):
                pts.append(p2); used[j] = True
                if dfs(x + 1): return True
                used[j] = False; pts.pop()
            pts.pop()
        return False
    try:
        r = dfs(1)
        status = 'complete' if not r else 'reached Kmax'
    except TimeoutError:
        status = 'timeout'
    return best[0], status, best[1]

if __name__ == '__main__':
    h = int(sys.argv[1]); Kmax = int(sys.argv[2])
    A = [int(v) for v in sys.argv[3].split(',')] if len(sys.argv) > 3 else list(range(1, h + 1, 2))
    b, st, s = run(h, Kmax, A, 55)
    print(f"h={h} A={A} best width found={b} ({st}) rows={s}")
