# Coarse affine sections with a fine rank progression

15 November 2026. This note gives the exact composition of a coarse
Hilbert row-section bound and a fine progression bound. It identifies
the remaining counting issue rather than asserting a subquadratic
same-parity six-point estimate.

## 1. Tile decomposition

Let \(N,R\) be powers of two with \(R\mid N\), and put
\(Q=N/R\), \(B=R^2\). In the standard Hilbert order, a rank block
\([BJ,BJ+B)\) is one aligned spatial \(R\times R\) tile. Its tile
coordinates are \(H_Q(J)\). The order within that tile is a rotated or
reflected Hilbert order.

Fix a coordinate role \(\alpha\), two raw coordinate rows \(y_1,y_2\),
an integer progression \(p_1\equiv z\pmod d\), and an affine relation
\[
 a p_2-bp_1=c,\qquad ab\ne0.
 \tag{1}
\]
Write \(p_i=BJ_i+e_i\), where \(0\le e_i<B\). Then
\[
 aJ_2-bJ_1=(c-ae_2+be_1)/B.
 \tag{2}
\]
The integer on the left belongs to an interval of length at most
\(|a|+|b|\). Thus only \(O(|a|+|b|+1)\) coarse translations occur.
This bound is independent of the size and sign of \(c\).

If the rows share their coarse row,
\[
 \lfloor y_1/R\rfloor=\lfloor y_2/R\rfloor=Y,
 \tag{3}
\]
both \(J_i\) belong to the coordinate-\(\alpha\) section of row \(Y\)
in \(H_Q\). Define
\[
 A_Q(a,b;Y)=
 \max_{c'\in\mathbb Z}
 \#\{(J_1,J_2):H_Q(J_i)_\alpha=Y,\
                         aJ_2-bJ_1=c'\}.
 \tag{4}
\]
For each admissible coarse pair, the first partner lies in one fixed
row of one \(R\times R\) tile and one residue class modulo \(d\).
The local version of the
[row-progression packing lemma](continuation_hilbert_row_visit_energy.md)
gives at most
\[
 C(R/\sqrt d+1)
 \tag{5}
\]
choices. Tile rotations and reflections only change the coordinate
role and its sign. The first partner determines the second partner
through (1), so this factor is not squared.

Consequently the number of fine pairs is at most
\[
 C(|a|+|b|+1)A_Q(a,b;Y)(R/\sqrt d+1).
 \tag{6}
\]
The statement also holds for unequal coarse rows, with the corresponding
two-row version of (4). The common-row hypothesis is useful because the
existing carry-automaton estimates use common row bits.

## 2. Application to a fixed hub and increment

For a raw same-parity parked pair, fix the hub, increment, and sea
offsets. The exact reduction gives a relation of form (1), with
\(|a|+|b|=O(K)\), and a progression modulus
\(d\ge ch/K^2\). Here \(N=\Theta(h)\).

The
[dyadic boundary counting split](continuation_raw_six_grid_boundary_count.md)
removes, by counting rather than by changing the construction, the
exceptional cases where the two partner rows fail (3). For
\(R\asymp h^\varepsilon\), with fixed \(\varepsilon>1/2\), its expected
exceptional contribution is \(h^{5/2-\varepsilon+o(1)}=o(h^2)\).

Suppose, for the relevant slopes and rows, a uniform estimate
\[
 A_Q(a,b;Y)\le C_K Q^{1-\eta}
 \tag{7}
\]
is available. Equation (6) then improves the uniform partner count
for a fixed hub and increment to
\[
 C_K h^{1/2-\eta(1-\varepsilon)}.
 \tag{8}
\]
The coefficients may be reduced by their common divisor before using
the carry automaton. Negative slopes can be treated by rank reversal,
provided the resulting coordinate-complement state is retained.

## 3. Accounting limit and joint target

There are \(O(h^2)\) hubs and \(O(h)\) increments before arithmetic
tests. A same-parity pair fixes only one random offset, giving an
\(O(1/h)\) probability. Summing (8) directly therefore gives
\[
 C_K h^{5/2-\eta(1-\varepsilon)},
 \tag{9}
\]
not \(h^{2-\eta(1-\varepsilon)}\).

The earlier \(h^{2+o(1)}\) estimate uses an averaged divisor-energy
argument. The
[partner-first improvement](continuation_partner_first_six_reduction.md)
instead uses a bounded number of increments per close-row partner pair.
Neither argument shows that its accepted configurations distribute
uniformly among the coarse affine pairs in (4).

Thus (6) is a valid composition theorem and (8) is a uniform local
improvement. A global power saving still needs a weighted version that
couples the coarse affine restriction with the increment divisibility
or with the partner-first hub test. Multiplying a section deficit into
an unrelated upper bound would not establish that result.

The theorem concerns raw coordinates, or a prescribed common affine
fold branch. Cap-constant sections are not injective row sections and
are outside its scope.

Independent review: the complete written composition and its exponent
accounting passed a separate review.
