"""Definition-level checks.  rows list = flattened column pairs.
Reports: distinct pairs, one-sided right angles (OSRAF violations),
tilted rectangles of the h x K grid with >=3 corners (N-window violations)."""
import sys, itertools
def check(h, rows, A):
    cols = [tuple(sorted(rows[2*i:2*i+2])) for i in range(len(rows)//2)]
    K = len(cols)
    P = [(x+1, y) for x, c in enumerate(cols) for y in c]
    S = set(P)
    edges_ok = len(set(cols)) == K and all((c[0] in A) != (c[1] in A) for c in cols)
    one_sided = 0; nwin = 0
    for V in P:
        for X, Y in itertools.combinations([Q for Q in P if Q != V], 2):
            u = (X[0]-V[0], X[1]-V[1]); v = (Y[0]-V[0], Y[1]-V[1])
            if u[0]*v[0] + u[1]*v[1] != 0: continue
            if u[0] == 0 or u[1] == 0 or v[0] == 0 or v[1] == 0: continue
            if u[0]*v[0] > 0: one_sided += 1
            F = (X[0]+Y[0]-V[0], X[1]+Y[1]-V[1])
            if 1 <= F[0] <= K and 1 <= F[1] <= h: nwin += 1
    return K, edges_ok, one_sided, nwin
if __name__ == '__main__':
    tests = [
        (8, [3,2,3,4,5,2,1,6,7,2,3,8,7,4,5,6,7,6], [1,3,5,7]),
        (10, [1,2,3,2,1,4,5,2,1,6,7,2,1,8,9,2,1,10], [1,3,5,7,9]),
        (12, [1,2,3,2,1,12,5,2,1,6,7,2,3,12,9,2,3,6,11,12,5,12,11,2], [1,3,5,7,9,11]),
        (6, [1,2,2,3,3,4,4,5,5,6,1,6], [1,3,5]),   # cyclic staircase: N-window, not OSRAF
    ]
    for h, rows, A in tests:
        print(h, check(h, rows, A))
