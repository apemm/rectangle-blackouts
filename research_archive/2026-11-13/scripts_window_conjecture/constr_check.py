"""Definition-level check of the two width-h windows of the note, for h = 4..40:
odd h: A = {1,3,...,h-2}; columns {1,h-1}, {h-j,h-j+1} (j=2..h-1), {1,h}.
even h: parity; columns {i,i+1} (i=1..h-1), {1,h}.
Checks: pairs distinct edges of K_{A,B}, |A| = floor(h/2), and no three points of P that are
three corners of a tilted rectangle whose fourth corner lies in the h x h grid (all triples)."""
import itertools
def window(h):
    if h % 2:
        A = set(range(1, h - 1, 2))
        cols = [(1, h - 1)] + [(h - j, h - j + 1) for j in range(2, h)] + [(1, h)]
    else:
        A = set(range(1, h + 1, 2))
        cols = [(i, i + 1) for i in range(1, h)] + [(1, h)]
    return A, cols
def check(h):
    A, cols = window(h)
    assert len(A) == h // 2 and len(cols) == h and len(set(cols)) == h
    assert all((a in A) != (b in A) for a, b in cols)
    P = [(x + 1, r) for x, c in enumerate(cols) for r in c]
    bad = 0
    for V, X, Y in itertools.permutations(P, 3):
        if X >= Y: continue
        u = (X[0] - V[0], X[1] - V[1]); v = (Y[0] - V[0], Y[1] - V[1])
        if u[0] * v[0] + u[1] * v[1] or u[0] == 0 or u[1] == 0: continue
        F = (X[0] + Y[0] - V[0], X[1] + Y[1] - V[1])
        if 1 <= F[0] <= h and 1 <= F[1] <= h: bad += 1
    return bad
print({h: check(h) for h in range(4, 41)})
