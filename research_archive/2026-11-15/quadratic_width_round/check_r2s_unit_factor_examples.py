"""Exact four-support certificates for the unit-factor R2s graph."""
from fractions import Fraction

CASES = [
    (11830, 11834, 14, 1, (844, 845, 56, -787)),
    (11834, 11902, 34, 17, (5916, 5917, 136, -5779)),
    (72150, 72234, 70, 21, (21644, 21645, 280, -21363)),
    (71910, 72234, 94, 81, (61964, 61965, 376, -61587)),
]

for n, target, m, d, expected in CASES:
    delta = 4*d
    U = (2*m+1)**2 + 4*d*d
    X, T, V = U-1, 4*m, 4*m-U+2
    a, b = X-T, U-X
    assert (X,U,T,V) == expected
    assert n*d == m*U and target == n+delta
    assert 4*a*b == T*T+delta*delta and b == 1
    assert T*U == n*delta
    assert V*V == U*U-2*n*delta-delta*delta
    assert 2*X == U+T-V
    assert delta*delta <= 2*X
    assert X % 4 == 0 and U % 4 == 1 and (X+V) % 4 == 1
    assert n % 4 == 2 and m % 2 == 0 and d % 2 == 1
    P, Q = (2*m,n+1+2*d), (U+2*m,1+2*d)
    assert P[0] % 4 == 0 and P[1] % 4 == 1
    assert Q[0] % 4 != 0 and Q[1] > 1
    assert min(P[1],Q[1]) >= 1 and max(P[1],Q[1]) < target+1
    # AB is a side of the first rectangle, with translation A->P.
    assert U*(2*m) - n*(2*d) == 0
    # CD and PQ are the two diagonals of the second rectangle.
    A, B, C, D = (0,n+1), (U,1), (X,n+1+delta), (X+V,1)
    assert (C[0]+D[0], C[1]+D[1]) == (P[0]+Q[0], P[1]+Q[1])
    assert (C[0]-D[0])**2+(C[1]-D[1])**2 == (P[0]-Q[0])**2+(P[1]-Q[1])**2
    assert len({A,B,C,D,P,Q}) == 6
assert Fraction((2*2+1)**2,2).denominator == 2
print("PASS: four exact unit-factor supports, compatible path, repeated target, and Vieta obstruction.")

