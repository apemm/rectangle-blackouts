"""Mod-7 + row-parity sieve of support roles in the Hilbert period-seven block.

Normalized residues (T2 Section 1): label columns 0; odd label row 0;
even label row 5 (mixed block) or 0 (zero-residue block).
Sea: L row 0, columns {3,5,6}; F row 3, column 0; H row 1, columns {1,2,4}.
Physical parity: O odd, E even, L odd, F odd, H even.
Prints, for corner triples (vertex + two ends) and for mixed quadruples
(side A,B | diagonal C,D), the type patterns that have a mod-7 solution
compatible with the row-parity constraints, restricted to patterns that
use at least one label point.
"""
import itertools, json, sys

N = [3, 5, 6]; Q = [1, 2, 4]

def types(block):
    eres = 5 if block == 'mixed' else 0
    return {
        'O': ([0], 0, 1), 'E': ([0], eres, 0),
        'L': (N, 0, 1), 'F': ([0], 3, 1), 'H': (Q, 1, 0),
    }

def pts(T, name):
    cols, r, par = T[name]
    return [((c, r), par) for c in cols]

def triples(block):
    T = types(block); out = []
    names = list(T)
    for v in names:
        for p1, p2 in itertools.combinations_with_replacement(names, 2):
            if not any(n in 'OE' for n in (v, p1, p2)):
                continue
            ok = []
            for (V, pv) in pts(T, v):
                for (P1, q1) in pts(T, p1):
                    for (P2, q2) in pts(T, p2):
                        a = ((P1[0]-V[0]) % 7, (P1[1]-V[1]) % 7)
                        b = ((P2[0]-V[0]) % 7, (P2[1]-V[1]) % 7)
                        if (a[0]*b[0] + a[1]*b[1]) % 7 == 0:
                            W = ((P1[0]+P2[0]-V[0]) % 7, (P1[1]+P2[1]-V[1]) % 7)
                            wpar = (q1 + q2 - pv) % 2
                            ok.append((V, P1, P2, W, wpar))
            if ok:
                out.append((v, p1, p2, len(ok), sorted(set((w, wp) for *_, w, wp in ok))))
    return out

def quads(block):
    T = types(block); out = []
    names = list(T)
    pairs = list(itertools.combinations_with_replacement(names, 2))
    for s in pairs:
        for d in pairs:
            if not any(n in 'OE' for n in s + d):
                continue
            ok = 0
            for (A, pa) in pts(T, s[0]):
                for (B, pb) in pts(T, s[1]):
                    for (C, pc) in pts(T, d[0]):
                        for (D, pd) in pts(T, d[1]):
                            if (pa + pb - pc - pd) % 2:
                                continue  # row sums must agree mod 2
                            U = ((B[0]-A[0]) % 7, (B[1]-A[1]) % 7)
                            Vv = ((D[0]-C[0]) % 7, (D[1]-C[1]) % 7)
                            n2 = lambda w: (w[0]*w[0] + w[1]*w[1]) % 7
                            if n2(U) != n2(Vv):
                                continue
                            Tt = ((C[0]+D[0]-A[0]-B[0]) % 7, (C[1]+D[1]-A[1]-B[1]) % 7)
                            if (U[0]*Tt[0] + U[1]*Tt[1]) % 7:
                                continue
                            ok += 1
            if ok:
                out.append((s, d, ok))
    return out

res = {}
for block in ('mixed', 'zero'):
    tr = triples(block); qu = quads(block)
    res[block] = {'triples': [(v, p1, p2, n, w) for v, p1, p2, n, w in tr],
                  'quads': [(s, d, n) for s, d, n in qu]}
    print('BLOCK', block)
    print(' corner triples surviving (vertex | ends | #sol | W residues,parity):')
    for v, p1, p2, n, w in tr:
        print('  ', v, '|', p1, p2, '|', n, '|', w)
    print(' mixed quadruples surviving (side | diagonal | #sol):')
    for s, d, n in qu:
        print('  ', ''.join(s), '|', ''.join(d), '|', n)
json.dump(res, open(sys.argv[1], 'w'), indent=0, default=str) if len(sys.argv) > 1 else None
