"""Two +-1 walks f0, f1 (parity classes), distinct unordered pairs, OSRAF and/or N-window.
Max width by DFS (branching <= 4).  usage: py twowalk.py h mode   (mode: osraf | nwin)"""
import sys, time
h = int(sys.argv[1]); mode = sys.argv[2]
pts = []; best = [0, None]; t0 = time.time()
def bad_new(N, K=None):
    nx, ny = N
    L = pts
    for i, V in enumerate(L):
        for j, X in enumerate(L):
            if X is V: continue
            # right angle at V with legs X and N
            u = (X[0]-V[0], X[1]-V[1]); v = (nx-V[0], ny-V[1])
            if u[0]*v[0] + u[1]*v[1] == 0 and u[0] and u[1] and v[0] and v[1]:
                if mode == 'osraf':
                    if u[0]*v[0] > 0: return True
                else:
                    F = (X[0]+nx-V[0], X[1]+ny-V[1])
                    if 1 <= F[1] <= h and F[0] >= 1 and (F[0] <= Kmax): return True
        # right angle at N with legs V and X (V,X earlier)
    for i, V in enumerate(L):
        for X in L[i+1:]:
            u = (V[0]-nx, V[1]-ny); v = (X[0]-nx, X[1]-ny)
            if u[0]*v[0] + u[1]*v[1] == 0 and u[0] and u[1] and v[0] and v[1]:
                if mode == 'osraf':
                    if u[0]*v[0] > 0: return True
                else:
                    F = (V[0]+X[0]-nx, V[1]+X[1]-ny)
                    if 1 <= F[1] <= h and F[0] >= 1 and F[0] <= Kmax: return True
    return False
Kmax = 10**9 if mode == 'osraf' else int(sys.argv[3])
def dfs(x, f0, f1, used):
    if time.time() - t0 > 55: raise TimeoutError
    if x - 1 > best[0]: best[0] = x - 1; best[1] = [(p[1]) for p in pts]
    if x > Kmax: return True
    for a in (f0 - 1, f0 + 1):
        for b in (f1 - 1, f1 + 1):
            if not (1 <= a <= h and 1 <= b <= h): continue
            key = (min(a, b), max(a, b))
            if key in used: continue
            p1 = (x, a); p2 = (x, b)
            if bad_new(p1): continue
            pts.append(p1)
            if not bad_new(p2):
                pts.append(p2); used.add(key)
                if dfs(x + 1, a, b, used): return True
                used.discard(key); pts.pop()
            pts.pop()
    return False
try:
    for a in range(1, h + 1):
        for b in range(1, h + 1):
            if (a + b) % 2 == 0 or a > b and False: continue
            if a % 2 != 1: continue        # class 0 = odd row at x=1
            pts.clear(); pts.extend([(1, a), (1, b)])
            dfs(2, a, b, {(min(a, b), max(a, b))})
    st = 'complete'
except TimeoutError:
    st = 'timeout'
print(f"h={h} mode={mode} best={best[0]} ({st}) rows={best[1]}")
