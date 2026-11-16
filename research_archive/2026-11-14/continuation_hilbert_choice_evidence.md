# Constant local choices for the Hilbert placement

14 November 2026. The same-parity exclusion in
[the placement note](continuation_hilbert_placement.md) permits
\[
 x_r=32(Mr+\xi_r),\qquad 0\le\xi_r<M.
\]
This note studies the remaining opposite-parity P-rivals. It gives exact
finite certificates and two limitations of possible proof strategies.
It does not prove that a constant \(M\) works for every height.

## 1. The finite constraint system

For ranks \(r<s\), put \(d=s-r\). A constraint
\((r,s,\delta)\) forbids \(\xi_s-\xi_r=\delta\). The corresponding
horizontal gap is \(X=32(Md+\delta)\).

For each of the two opposite-parity pairs, compute its row difference
\(Y\). Include the constraint when \(X^2+Y^2=L^2\) and the vertical
completion rows
\[
 (y_r+y_s-L)/2,\qquad (y_r+y_s+L)/2
\]
both belong to \(\{1,\ldots,h\}\). This is a sufficient exclusion
system. Some included candidates could have their owner at the midpoint
for particular choices of other labels. Excluding every candidate avoids
that extra dependence and guarantees that no actual P-rival survives.

Completeness of the integer enumeration follows from
\[
 a=(L-|Y|)/2,\quad b=(L+|Y|)/2,
 \qquad ab=(X/2)^2.
\]
The integers \(a,b\) have opposite parity. Conversely every such divisor
pair gives \(L=a+b\) and \(|Y|=b-a\). The rank-gap loop is complete
because \(X<L<h\) bounds \(d\).

Give each constraint weight one, including distinct forbidden differences
on the same pair of labels. If this multigraph has weighted degeneracy
less than \(M\), reverse peeling gives a valid assignment: each previously
assigned constraint excludes at most one of the \(M\) choices.

The exact computations are:

| Height | Choices | Constraints | Incident labels | Maximum weighted degree | Weighted degeneracy |
|---:|---:|---:|---:|---:|---:|
| 2048 | 3 | 139237 | 171851 | 8 | 2 |
| 2048 | 4 | 173065 | 184194 | 8 | 3 |
| 4096 | 3 | 695871 | 877697 | 8 | 2 |

Reverse peeling and greedy assignment succeeds without repairs in all
three cases. Every reconstructed constraint is checked against the final
assignment. The script is
[hilbert_finite_choice_search.py](hilbert_finite_choice_search.py), with
certificates in `hilbert_choice3_h2048.json`,
`hilbert_choice4_h2048.json`, and `hilbert_choice3_h4096.json`.
Omitted rank entries have choice zero.

An independent verifier,
[verify_hilbert_choice_certificate.py](verify_hilbert_choice_certificate.py),
reconstructs the coordinates by a different Hilbert algorithm and uses
Euclid's primitive-triangle parametrization instead of the search's
divisor enumeration. It checks the final choices directly at every
potentially relevant rank gap. All three certificates pass. The two
three-choice certificates require 44039730 and 360708252 opposite-parity
pair checks, respectively. Results and certificate hashes are in
`hilbert_choice_independent_verification.json`.

These certify only the P exclusion. The two-choice obstruction remains
valid, and no claim about filler or higher-arity supports follows.

## 2. Translated patches test much larger offsets

Take an aligned, identity-oriented Hilbert square of side \(R\), translated
by \((I,J)\), where \(R\mid I,J\). Put
\(D=2(J-I)+1\), so \(D\equiv1\pmod{2R}\). A local label \((i,j)\)
has odd row \(2(I+i)+1\) and even row \(2(J+j)+2\).

For a local rank pair \(r<s\), every possible Pythagorean row difference
\(Y>0\) gives the candidate offsets
\[
 D=\pm Y-2j_s+2i_r,
 \qquad D=2i_s-2j_r\pm Y.
\]
Factoring \((X/2)^2\) therefore enumerates all offsets without a bound on
the global height. This is a finite enumeration for a fixed patch.
The script
[hilbert_translated_patch_search.py](hilbert_translated_patch_search.py)
groups the constraints by \(D\).

For \(M=3\), \(S=32\), and \(R=16\), all 12942 nonempty offset groups
have weighted degeneracy at most two. At \(R=32\), three of the 58579
groups have weighted degeneracy three. Their offsets are
\(2561,-260863,260865\).

Thus weighted degeneracy below three does not hold for every translated
candidate patch. This is not a three-choice impossibility result. For
example, the displayed core at \(D=2561\) contains only nonzero forbidden
differences and is solved by setting every choice to zero.

All three exceptional cores are in fact three-choice satisfiable. Their
sizes are 10, 4, and 41 vertices, and exact domain propagation with
backtracking finds assignments in 10, 3, and 22 search nodes. The script
[solve_hilbert_patch_cores.py](solve_hilbert_patch_cores.py) checks the
assignments directly against every core constraint. Since every vertex
peeled before each recorded core had weighted degree at most two, each
core assignment extends by reverse greedy assignment. Consequently all
58579 offset groups for this identity-oriented \(32\)-square admit three
choices. This is a finite local certificate, not a statement about
arbitrarily large Hilbert patches or interactions between patches.

A global
counterexample would also require an appropriate Hilbert orientation,
in-strip completion rows, and an owner distinct from every midpoint.

## 3. The unjittered P graph contains a triangle

The actual unjittered graph uses \(x_r=32r\). Here the computation also
checks that the owner column differs from the midpoint column.
At height 2048 it is bipartite, with 94222 edges. At height 4096 it has
481323 edges and contains the following triangle:

| Label | Hilbert rank | Coordinates \((i,j)\) | Black rows |
|---|---:|---|---|
| A | 1331100 | \((187,1549)\) | \(375,3100\) |
| B | 1331133 | \((190,1545)\) | \(381,3092\) |
| C | 1331166 | \((187,1541)\) | \(375,3084\) |

The three exact rival witnesses are:

| Pair | Chosen black rows | \(X,|Y|,L\) | Completion rows | Owner rank |
|---|---|---|---|---:|
| A,B | \(375,3092\) | \(1056,2717,2915\) | \(276,3191\) | 3990830 |
| A,C | \(375,3084\) | \(2112,2709,3435\) | \(12,3447\) | 3952606 |
| B,C | \(3092,375\) | \(1056,2717,2915\) | \(276,3191\) | 3990830 |

Each row satisfies \(X^2+Y^2=L^2\). Every completion lies in the strip.
The owner ranks differ from the respective midpoint ranks
\(1331116.5,1331133,1331149.5\). The corresponding axis rectangle and
tilted rectangle therefore have the same presentation.

The triangle embeds at heights \(4096\cdot2^k\) by repeatedly using the
unrotated third quadrant of the next Hilbert square. Coordinates and
completion rows undergo the same translations, and rank differences
remain unchanged. Thus two colors cannot resolve the fixed Hilbert
P graph for every height.

The script is
[hilbert_fixed_graph_coloring.py](hilbert_fixed_graph_coloring.py).
The separate sparse checker
[check_hilbert_p_triangle.py](check_hilbert_p_triangle.py) verifies the
three base edges and their embeddings at heights 8192 and 16384. It
checks the actual presentations of both rectangles using full-family
membership, rather than only their lengths and completion rows.
The graph census also rejects both simple proposed colorings, rank popcount modulo two
and the pair of coordinate popcounts modulo two, already at height 2048.
This gives no obstruction to an unrestricted bounded palette of at least
three colors, or to the three-choice local placement.
