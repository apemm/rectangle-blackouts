# A period-four sea with two odd levels

15 November 2026. A sea can use both odd rows \(s,s+4\) without
introducing a new bulk support family, provided its height is fixed on
each nonzero column residue modulo four. This preserves the constant-sea
classification. It does not separate the two sea corners of one
parked-six witness.

This is a bulk statement. It supplies no new collar or relocation theorem.

## 1. Profile and core assumptions

Fix an odd row \(s\). For each \(j\in\{1,2,3\}\), choose
\(\epsilon_j\in\{0,1\}\). At every column \(x\equiv j\pmod4\),
place the sea point
\[
 (x,s_j),\qquad s_j=s+4\epsilon_j.
 \tag{1}
\]
Core points have columns divisible by four. Odd core rows satisfy
\(a\equiv s+2\pmod4\), and even core rows belong to one fixed even
residue modulo four. Require all core rows to exceed \(2(s+4)\), and
require odd core rows to satisfy
\[
 a>(h+s+4)/2.
 \tag{2}
\]
These are the low-sea hypotheses. Reflection gives the corresponding
high-sea version.

Assume the reviewed same-parity core exclusions: no nonhorizontal
same-parity integral distance, no same-parity right triangle, and no
same-parity side/diagonal mixed support. The spacing-four mesh supplies
these conditions.

## 2. The sea alone is valid

A sea-only right triangle would use both levels. Two vertices would
share one level. If its right angle were at one of those vertices, the
other leg would require two sea points in one column, which is
impossible. Otherwise the right vertex is on the other level. The two
horizontal leg lengths on opposite sides are positive integers \(u,v\)
with
\[
 uv=16.
 \tag{3}
\]
At least one of \(u,v\) is divisible by four. Its endpoint shares the
right vertex's column residue but would have to occupy the other sea
level. This contradicts (1).

There is no sea-only hidden rectangle. Four rectangle vertices on two
horizontal levels would form an axis-aligned rectangle, requiring two
black points in each of two columns.

For completeness, consider a mixed four support, represented by a black
side \(A,B\), a black diagonal \(C,D\), equal lengths, and an integral
translation between their midpoints perpendicular to \(B-A\).
If both pairs cross the two levels, their horizontal gaps have the same
absolute value. Their midpoint heights agree, so perpendicularity forces
the midpoint translation to vanish. This is degenerate. A vertical
black side is unavailable because each column has one sea point.

If both pairs are horizontal, their lengths agree and their midpoint
columns agree. Their endpoint columns therefore coincide, again
requiring two black sea points in a column unless the pairs coincide.

In the remaining case, a horizontal length \(n\) and a crossing pair
with nonzero horizontal gap \(x\) satisfy
\[
 n^2-x^2=16.
 \tag{4}
\]
The only positive solution with \(x\ne0\) is \(n=5,|x|=3\).
If the crossing pair is the side, perpendicularity requires a horizontal
midpoint shift of magnitude \(8/3\), impossible for these integer
endpoints. If the horizontal pair is the side, both midpoint columns
agree. The four columns are a translate of
\(\{0,1,4,5\}\). A point of the crossing pair shares a residue with a
side endpoint but has the other height, contradicting (1).

The usual positive-support classification now excludes a collision of
two rectangle presentations on the sea alone. Four-support collisions
have just been excluded. A six-support collision contains a three-black
right triangle, and a disjoint eight-support collision contains a hidden
rectangle.

## 3. Triangles involving the core

Every core-to-sea distance is nonintegral. For an odd core row, its
squared norm modulo sixteen is in \(\{5,13\}\) at an odd sea column,
and is \(8\) at a \(2\bmod4\) sea column. For an even core row, these
sets are respectively \(\{2,10\}\) and \(\{5,13\}\).

For one core point and two sea points, a right angle at the core has
completion row
\[
 s_i+s_j-a\le2(s+4)-a<1.
 \tag{5}
\]
At a sea vertex \(B=(b,s_i)\), let the other sea point be
\((b+d,s_j)\), and write the core point as \((b+x,a)\). Then
\[
 xd+(a-s_i)(s_j-s_i)=0.
 \tag{6}
\]
If the sea heights agree, a nondegenerate right angle would require
\(x=0\), which would put the core point in a sea column.

If they differ, \(s_j-s_i=\pm4\). When \(b\) is odd, \(x\) is odd,
so (6) forces \(d\equiv0\pmod4\). The sea heights must then agree
by (1), a contradiction. When \(b\equiv2\pmod4\), \(x\equiv2\pmod4\).
For an even core row, (6) forces \(d\equiv2\pmod4\), putting the
second sea point in a core column. For an odd core row,
\(a-s_i\equiv2\pmod4\), and (6) forces \(d\equiv0\pmod4\).
Both possibilities are impossible.

With two core points and one sea point, the usual modulo-four dot
product excludes opposite-parity core points at every possible right
vertex. At a sea right vertex, two even core points are also excluded
modulo four. Two odd core points would have completion row
\[
 a_1+a_2-s_i>h
 \tag{7}
\]
by (2). Thus the only remaining triangle type is the existing parked
triangle with two same-parity core points and its right vertex at a core
point.

## 4. Mixed four supports

Three core points and one sea point are excluded by the same parity and
norm table as in the constant-sea classification. For one core point
and three sea points, total row parity first forces the core point to
be odd. Its core-to-sea squared norm is a nonsquare residue modulo
sixteen. A sea-to-sea squared norm is a square residue modulo sixteen,
since its vertical difference is zero or four. Equal norms are
impossible.

For two core and two sea points, total row parity forces the core
points to have the same parity. If the two core points are paired
together, equality of norms forces the sea columns to agree modulo
four. Their heights then agree. A nonhorizontal core pair has
nonintegral length, while the sea pair has integral length. A horizontal
core pair would force coincident core and sea endpoint columns.

It remains to consider crossed core-to-sea pairs. Their squared norms
force the sea columns to have the same parity. If both are \(2\bmod4\),
their sea heights already agree.

Suppose both are odd. Normalize the four black points as
\[
 A=(0,a),\quad B=(x,a+m),\quad
 C=(X,a+\delta),\quad D=(X+z,a+m+e),
 \tag{8}
\]
where \(A,C\) are core points, \(A,B\) form the side, and \(C,D\)
form the diagonal. Here
\[
 X,\delta,e\equiv0\pmod4,\qquad x,z\ \hbox{odd}.
 \]
Perpendicularity of the side and midpoint translation gives
\[
 x(2X+z-x)+m(\delta+e)=0.
 \tag{9}
\]
Reducing modulo four yields \(z-x\equiv0\pmod4\).
The two sea columns \(x,X+z\) therefore have the same residue, hence
the same height.

Every surviving two-core/two-sea mixed support consequently uses a
single sea row and a single sea-column residue. Apply the existing
\(h^{5/6+o(1)}\) same-row bad-row estimate separately to the three
residues. The fixed union does not change its order.

After this deletion, the residual bulk families are the same four
families as for the constant sea. No new support family has been
discarded merely because the sea has two odd levels.

## 5. What this variation can change

In a parked triangle, write the completion column as \(w\), the long
core-leg displacement as \(X\), and the sea column as \(w-X\).
Since both core columns are divisible by four, \(X\equiv0\pmod4\).
The sea point therefore has residue \(w\bmod4\).

Both triangles of a common-completion six support use this same residue.
Under (1), both sea points still have exactly the same height \(s_j\).
The profile offers three fixed choices of sea level, one for each
completion residue. It does not independently perturb the two sea
corners within a six-point witness.

Allowing the height to vary within one residue would break this last
identity, but it would also invalidate the exclusions in Sections 2--4.
Those new supports need a separate analysis. No such within-residue
variation is asserted to be valid here.

## 6. Within-residue switches necessarily create a new triangle type

There is a precise limitation to preserving the old triangle
classification. Suppose the two-level sea is periodic, with period a
multiple of four, and is nonconstant on one nonzero residue \(j\).
Its sequence on that residue has both an upward and a downward adjacent
transition. Write one such transition as
\[
 B=(b,s_i),\qquad C=(b+4,s_i+4\epsilon),
 \qquad \epsilon\in\{-1,1\}.
 \tag{10}
\]
For a possible core row \(a\), set
\[
 A=(b-\epsilon(a-s_i),a).
 \tag{11}
\]
Then \((A-B)\cdot(C-B)=0\). The completion is
\[
 W=(A_x+4,a+4\epsilon).
 \tag{12}
\]
The core-column condition is exactly
\[
 a\equiv s+\epsilon j\pmod4.
 \tag{13}
\]

For odd \(j\), the two transition directions in (13) give the two even
row classes. Hence one direction accommodates the chosen even core
class. For \(j=2\), either direction accommodates the allowed odd class
\(s+2\bmod4\). For sufficiently large \(h\), choose \(a\) in the
corresponding bulk range, away from the last four rows. Then all four
vertices are in the strip. Periodicity translates the transition to
place the potential core point within any sufficiently long bulk
interval, with \(O(h)\) horizontal margins retained for all four points.

Thus every periodic within-residue variation admits a one-core/two-sea
triangle with an in-strip completion. This is a potential support:
it does not assert that a particular chosen Hilbert core contains
the point \(A\), or that this triangle alone causes a presentation
collision. It shows that eliminating this entire triangle family for
all eligible core points forces the sea to be constant on each residue.

Independent review: the full written proof passed a separate review of
the sea-only mixed cases, triangle valuations, norm table, same-residue
mixed reduction, and the within-residue transition construction.
