# An unbounded repair cost for an adjacent-row checkerboard sea

15 November 2026. This addresses one proposed replacement for the local
H7 backgrounds. It is a necessary repair bound for this specific sea,
not a width lower bound or an obstruction to other backgrounds.

Independent review: the triangle family, the two-per-column incidence
bound, and the finite-board interpretation were checked separately and
passed.

Fix an odd integer \(r\). In every odd column put a black point in row
\(r\), and in every even column put one in row \(r+1\). At an odd
column \(x_0\), retain a black label point

\[
 A=(x_0,u),\qquad u=r+d,\qquad d\equiv3\pmod4,
 \quad d>1. \tag{1}
\]

This is the wrong checkerboard class. It satisfies the suggested
alignment \(u-(r+1)\equiv2\pmod4\). The other point of the label can,
for example, be in row \(r+2\), also satisfying its proposed alignment.
Assume the full final parity row-pair graph is present. Thus every
three-black tilted rectangle must have its white completion parked in a
column containing black points only of the completion's parity.

## 1. Explicit fatal triangles

Put

\[
 N=\frac{d(d-1)}2.
\]

This is odd. For every positive divisor \(a\mid N\) and every
\(\epsilon\in\{1,-1\}\), define

\[
 B_{a,\epsilon}=(x_0+2\epsilon a,r),\qquad
 C_{a,\epsilon}=(x_0-\epsilon N/a,r+1).
\]

Both are black points of the original sea. Their displacements from
\(A\) have dot product

\[
 (2\epsilon a)(-\epsilon N/a)+(-d)(1-d)
 =-2N+d(d-1)=0. \tag{2}
\]

The fourth corner is

\[
 W_{a,\epsilon}
 =\left(x_0+\epsilon(2a-N/a),\ r+1-d\right). \tag{3}
\]

Its column is even and its row is odd. The original black point in that
column is in the even row \(r+1\), so this is a fatal, unparked triangle
whenever \(r+1-d\ge1\). The three black columns and the completion
column are all distinct: the horizontal legs are nonzero, and equality
of the two other black columns would equate an even and an odd offset.

For example, \(r=5,d=3,x_0=1\) gives the black points
\((1,8),(3,5),(-2,6)\), with completion \((0,3)\).

All of these triangles fit in the horizontal interval
\([x_0-2N,x_0+2N]\). Their rows fit in \([1,r+d]\) when \(r\ge d\).
Thus the obstruction is finite and survives restriction to a board
containing this interval.

## 2. At least \(\tau(N)\) other columns must change

There are \(2\tau(N)\) triangles in (2). Their sea columns are all
distinct: the \(B\)-offsets are distinct nonzero even integers and the
\(C\)-offsets are distinct odd integers.

Their completion columns are also all distinct. For a fixed sign,
\(2a-N/a\) is strictly increasing in \(a\). An equality between
opposite signs would give

\[
 2a-N/a=-(2b-N/b),
 \qquad 2ab=N,
\]

which is impossible because \(N\) is odd.

Consequently a column other than \(x_0\) occurs in at most one sea
pair \(\{B_{a,\epsilon},C_{a,\epsilon}\}\), and in at most one
completion column. It can affect at most two of the displayed triangles.

Any valid repair that keeps \(A\) must change at least one of these
three columns for each triangle. If its two sea corners and completion
column remain unchanged, it is still an unparked three-black rectangle.
This remains necessary even when the repair changes a column to a
double, since a double cannot park a white corner. Adding black at the
completion itself instead makes the tilted rectangle fully black.

It follows that any such repair must alter at least

\[
 \frac{2\tau(N)}2=\tau(N) \tag{4}
\]

columns other than the retained label column. Arbitrary new collisions
caused by the repair are irrelevant to this necessary lower bound.

## 3. The bound is unbounded under the proposed alignment

Take \(d=3^{2k+1}\), \(r=d\), and \(h=2d\). Then all the triangles
fit vertically, their completion row is one, and

\[
 \tau\!\left(\frac{d(d-1)}2\right)\ge\tau(d)=2k+2.
\]

Thus no absolute number of background-column patches per inserted label
can repair this adjacent-row sea uniformly over heights. Along this
explicit sequence the necessary number of patches is \(\Omega(\log h)\).

This does not rule out shared repairs across many labels, a different
sea chosen jointly with the labels, or an overall quadratic-width
construction. It rejects the narrower proposal that the unchanged
adjacent-row sea can always be made safe by a bounded number of local
patches for each label.
