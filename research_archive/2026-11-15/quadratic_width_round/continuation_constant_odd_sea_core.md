# Constant odd seas recover a four-family core reduction

15 November 2026. Independently reviewed in full. This note classifies a proposed core with one constant
odd sea row. It does not prove the residual systems satisfiable or give
end collars. Its purpose is to remove the extra parked-triangle families
that obstruct the two-row profiles.

## 1. Low and high profiles

Choose an odd sea row \(s\). Put a black point at row \(s\) in every
column not divisible by four. All inserted points have columns divisible
by four. In one profile require
\[
 a\equiv s+2\pmod4
 \quad\text{for odd inserted rows},\qquad
 b\equiv\beta\pmod4
 \quad\text{for even inserted rows},                     \tag{1}
\]
where \(\beta\) is one fixed even residue. Use either of these regimes:

* **Low sea:** \(s\in\{1,3\}\), every inserted row exceeds \(2s\),
  and every odd inserted row satisfies \(a>(h+s)/2\).
* **High sea:** \(s\in[h-3,h]\) is odd, every inserted row satisfies
  \(r<2s-h\), and every odd inserted row satisfies \(a<(s+1)/2\).

The inequalities are strict to avoid boundary cases. Every inserted
column has at most one point of each parity; only actual retained labels
may be doubles. Their opposite-parity row pairs are distinct.

There are at most eight such profiles covering all but \(O(h)\) labels
of the complete parity-pair graph. For each odd residue, use its prescribed
low sea for odd rows above \(h/2+2\), and an odd high sea with the required
residue for odd rows below \(h/2-2\). Split even rows by their two residues
modulo four and keep, for example, \(8\le b\le h-8\). The excluded odd
middle band and even end bands have bounded numbers of rows. Each retained
profile is a rectangular product of row intervals in fixed step-four
residue classes, with bounded aspect ratio for large \(h\).

## 2. Zero- and one-inserted-point safety

The constant-row sea has no nondegenerate three-black right triangle,
hidden rectangle, or repeated presentation. Its black pairs are horizontal;
equal midpoint and length determine a diagonal pair, while any competing
side presentation would degenerate.

For an inserted point and a sea point, the distance is never integral.
If the inserted row is odd, its vertical difference from \(s\) is
\(2\pmod4\). At an odd sea column the squared distance is \(5\pmod8\);
at a \(2\pmod4\) sea column it is \(8\pmod{16}\). If the inserted
row is even, the vertical difference is odd. The corresponding residues
are \(2\pmod4\) and \(5\pmod8\).

A right triangle with one inserted point and two sea points must have
its right angle at the inserted point, since a sea-vertex angle would
require another black point in that sea column. Its fourth row is
\(2s-r\), outside the strip in either regime above. A triangle with
both points of one double and a sea point is impossible: the vertical
label leg cannot be perpendicular to a sea leg, and at the sea point
both label rows lie strictly on the same side of \(s\).

Two-white collisions with exactly one inserted point are also impossible.
If both black pairs play the same role, unequal row sums or differences
exclude them. In the mixed case, the inserted/sea distance is nonintegral,
whereas the sea/sea distance is an integer.

## 3. All sea-mediated triangles are parked label-vertex triangles

Consider one odd label point, one even label point, and one sea point.
At a label vertex, the inserted leg has horizontal difference divisible
by four and odd vertical difference. The sea vertical difference has
valuation one at the odd label and valuation zero at the even label.
The two terms in the orthogonality equation therefore have unequal
2-adic valuations.

At an odd sea column, the horizontal product is \(1\pmod4\);
the vertical product is \(2\pmod4\), so the dot product is nonzero.
At a \(2\pmod4\) sea column the horizontal product is zero modulo
four and the vertical product is two. Thus opposite-parity endpoints
never form a sea-mediated right triangle.

At a sea vertex with two even labels, the fixed even residue makes the
vertical product \(1\pmod4\). The horizontal product is one or zero
modulo four, so the dot product cannot vanish. With two odd labels, the
vertical product is zero modulo four. An odd sea column is again excluded.
A \(2\pmod4\) sea column is the sole remaining possibility, but its
completion has row \(a_1+a_2-s\), outside the strip by the odd-row
half-strip restriction.

Hence every admitted tilted triple involving sea points has exactly two
same-parity inserted points, with its right angle at an inserted point.
Write
\[
 A=(x,y),\quad C=A+(X,\delta),\quad B=(x+\xi,s).
\]
Then
\[
 X\in4\mathbb Z,\quad \delta\in4\mathbb Z,\qquad
 X\xi=-\delta(s-y),\qquad W=B+(X,\delta).                 \tag{2}
\]
Here \(\delta\ne0\), since \(\xi\ne0\). The completion column has
the same nonzero residue modulo four as \(B\). Its row \(s+\delta\)
differs from the sea row and has the same row parity. Thus \(W\) is
white, is safely parked against axis singleton presentations, and never
falls in an arithmetic hole. This argument does not require all inserted
slots to be occupied.

The one-even/two-sea and sea-vertex/two-label six-point families from the
two-row profiles are absent. Repeated completions between two triples
of (2) remain.

## 4. Mixed four-point supports

For this section, assume every nonhorizontal same-parity inserted pair
has nonintegral Euclidean length. The
[spacing-four refinement](continuation_step_four_refinement.md) provides
this, including its isolated slope-one seams.

Modulo sixteen, inserted pair lengths satisfy
\[
 OO,EE:0,\qquad OE:1\text{ or }9.
\]
The inserted/sea lengths satisfy
\[
\begin{array}{c|cc}
 &\text{odd sea column}&\text{sea column }2\pmod4\\ \hline
 O&5\text{ or }13&8\\
 E&2\text{ or }10&5\text{ or }13 .
\end{array}                                             \tag{3}
\]
These residues exclude every mixed support with three inserted points
and one sea point, in all parity assignments. The one-inserted/three-sea
case was excluded in Section 2.

For two inserted and two sea points, integrality of the common white
corners requires the total black row sum to be even. The inserted points
must therefore have the same parity. If the inserted pair forms a whole
black side or diagonal, the other black pair is horizontal. The
nonintegral-distance hypothesis forces the inserted pair to be horizontal
as well, which makes the alternative presentation degenerate.

Only crossed pairs remain, each joining an inserted point to a sea point.
Table (3) forces the two sea columns to have the same parity. Therefore
every such support is a same-sea-row crossed support with same-parity
inserted endpoints and same-parity sea columns.

This last column condition is important: the constant sea occupies both
column parities, but its possible crossed supports can be counted
separately in the odd-column and \(2\pmod4\) subclasses. The geometric
and divisor argument of
[the spacing-four R2s transfer](continuation_step_four_r2s_transfer.md)
then applies to each subclass. Low seas have \(s\le3\). For high seas,
reflect rows by \(r\mapsto h+1-r\); the reflected sea is at most four,
and the count does not require that its row be odd. It follows, under
that lemma's refined locality hypotheses, that
\[
 \#\{\text{possible side-owner rows}\}=h^{5/6+o(1)}.       \tag{4}
\]
This bad-row superset can be selected before the cap offsets.

## 5. Conditional collision criterion

Assume the distinct genuine-double rule, the geometric hypotheses of
Sections 1–4, and exclusion of the following positive-support families:

1. in-strip opposite-parity P diagonals, with the full final parity-pair
   graph supplying their owners when necessity is asserted;
2. tilted right angles on three inserted points;
3. nonvertical-side mixed four-inserted-point supports;
4. the crossed same-sea supports from Section 4;
5. two distinct triples of (2) with the same completion and six distinct
   black points.

Then the core and its constant sea have no identifying collision.
After the bad-row exclusion (4), the four remaining families are the
usual P, all-inserted three-corner, all-inserted mixed four-point, and
parked six-point families. This is a new proof for this sea; it is not
an automatic transfer of the old H7 completeness claim.

To check completeness, hidden tilted rectangles with sea points would
contain a triple from (2) with its fourth corner white; all-inserted
hidden rectangles contain an excluded three-corner support. Two-white
same-kind collisions force a hidden black rectangle. Mixed two-white
collisions are covered by Section 4 and the all-inserted entries.
A vertical inserted black side is the P case.

Two singleton presentations sharing an additional black corner reduce
to the same four-point symmetric-difference supports. Without a shared
black corner, their six black points are distinct. Any surviving tilted
singleton comes from (2), because all other tilted triples were excluded.
It cannot match an axis singleton: its column contains only the sea
point of the same row parity.

The axis subsystem is identifying because actual doubles are distinct
opposite-parity row pairs. Its row-pair graph is simple and bipartite,
which gives the stated axis uniqueness; singleton columns add no
row-pair edge.
Three common white corners determine a rectangle.

The spacing-four cone lemma also excludes all-one-parity inserted mixed
supports, and its seam argument excludes all-one-parity inserted right
triangles. Thus the corresponding residual entries may be restricted
to supports using both inserted parities.

## 6. Conditional quadratic scaffold, not a finished construction

The eight rectangular row pools have step-four coordinates. A separately
applicable good-cap construction, using (4) and the relevant endpoint
restrictions as bad rows, supplies good total coordinate options with
bounded adjacent increments. The spacing-four refinement then fills every
column divisible by four at a fixed width factor, retaining each genuine
double once and using singletons elsewhere. Its own exceptional-label
budget is \(h^{11/6+o(1)}\), in addition to the \(O(h)\) boundary and
middle-band labels from Section 1.

This is only a conditional scaffold. External relocation must preserve
the full final parity-pair graph and must be separated from every core
under a proved joining argument. The four residual systems in Section 5
must still be solved on the selected options. In particular, neither
uniform P cleanup nor a choice among cap palettes is supplied here.

No filled collar between the core and another profile is proved. Filling
a previously empty arithmetic column by the sea row introduces new black
points and is not justified by the one-label theorem. A unit-slope ramp
and its constant-repeat refinement actually fail the
[explicit staircase mixed-support tests](continuation_constant_sea_staircase_obstruction.md).
The quadratic width accounting
does not establish validity without these remaining steps.

