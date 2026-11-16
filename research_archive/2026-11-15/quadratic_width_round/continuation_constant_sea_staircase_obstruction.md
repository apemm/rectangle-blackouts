# Constant-repeat staircase collars fail in a constant sea

15 November 2026. A constant odd sea does not admit the natural staircase
collar that decreases its odd inserted row by four after every fixed
number of spacing-four slots. Explicit mixed four-supports obstruct both
one-slot steps and every longer plateau. The latter includes plateau
lengths that grow with height.

This rules out that collar template. It does not rule out nonuniform
ramps, alternating parity choices, additional row options, or a different
sea near the boundary.

## 1. Model and collision test

Fix an odd sea row \(L\). At every column not divisible by four, place
the sea point at row \(L\). At columns divisible by four, the proposed
collar has one odd point of row \(L+2\pmod4\). Its row decreases by
four after each block of \(M\) consecutive inserted slots. Here \(M\)
is any positive integer, and the descent ends at row \(L+2\).

All coordinates below are written relative to sea row zero; add \(L\)
to every row. Horizontal translations by multiples of four preserve the
template. Each certificate must lie inside the board, including the two
displayed corners. This is automatic in a sufficiently long interior
portion of the indicated ramp.

For a mixed certificate, let \(A,B\) be the black side, \(C,D\) the
black diagonal, and let \(t\) satisfy
\[
 (B-A)\cdot t=0,\quad |B-A|=|D-C|,\quad
 (C+D)/2=(A+B)/2+t.
 \tag{1}
\]
Then \(P=A+t,Q=B+t\) form the common displayed pair. The rectangle
with black side \(AB\) and the rectangle with black diagonal \(CD\)
have symmetric difference exactly \(\{A,B,C,D\}\). Thus their visible
presentations agree whenever these four points are black. Additional
black points cannot repair this collision on the same board.

## 2. Every plateau length at least two

Place the seam from relative row 14 to relative row 10 between columns
\(-4\) and zero. If \(M\ge2\), the two black core points
\[
 A=(0,10),\qquad C=(-8,14)
\]
are present. The ordinary columns contain
\[
 B=(-10,0),\qquad D=(-6,0).
\]
Take
\[
 t=(-2,2),\qquad P=(-2,12),\qquad Q=(-12,2).
 \tag{2}
\]
The exact checks are
\[
 B-A=(-10,-10),\qquad D-C=(2,-14),
\]
\[
 |B-A|^2=|D-C|^2=200,
 \qquad (B-A)\cdot t=20-20=0.
\]
Both diagonal midpoints equal \((-7,7)\), so (1) holds.

The point \(P\) is in an ordinary column whose black row is zero,
not 12. The point \(Q\) is in an earlier core column, whose monotone
ramp row is at least 14, not two. Thus both common points are genuinely
white in this collar. All certificate rows lie between zero and 14.

The horizontal interval \([-12,0]\) must be present. For a staircase
beginning at relative row at least 18 and descending through 14 and 10,
this interval lies inside the ramp for every \(M\ge2\). A shorter ramp
can still contain the certificate if its adjacent core supplies that
interval. The contradiction is independent of how large \(M\) is.

## 3. One slot per level

For \(M=1\), the inserted points lie on a line of slope \(-1\).
Translate a portion of it to \(y=50-x\). Use
\[
 A=(0,50),\qquad C=(-36,86),
\]
and the sea points
\[
 B=(-75,0),\qquad D=(-63,0).
\]
Now set
\[
 t=(-12,18),\qquad P=(-12,68),\qquad Q=(-87,18).
 \tag{3}
\]
Here
\[
 B-A=(-75,-50),\qquad D-C=(-27,-86),
\]
\[
 |B-A|^2=|D-C|^2=8125,
 \qquad (B-A)\cdot t=900-900=0.
\]
Both diagonal midpoints equal \((-99/2,43)\). The core point in
\(P\)'s column has row 62, not 68. The point \(Q\) is in an odd sea
column and has row 18, not zero. Thus both displayed corners are white.

The certificate fits whenever the constant sea and ramp cover
\([-87,0]\), and the height is at least \(L+86\). In particular, a
one-slot staircase descending from relative row at least 138 to relative
row two contains the entire certificate, including its displayed columns.
This explicit interval condition avoids assuming an unprovided sea
extension beyond a short ramp's finite end.

## 4. Consequence and limits

A constant-repeat staircase from a sufficiently high row down to
\(L+2\) fails for every \(M\ge1\). Taking \(M\) proportional to
height, which would give an \(O(h^2)\)-wide slow ramp, does not avoid
the norm-200 seam obstruction.

The argument is local and uses no axis owners or global row-pair graph.
The positive-support identity in Section 1 also makes it independent
of additional even points elsewhere in the proposed collar.

A nonuniform ramp can avoid the particular norm-200 certificate by
shortening the row-14 plateau to one slot. That does not prove such a
ramp works: it still needs to exclude all mixed supports and repeated
triangle completions. No impossibility claim is made for that broader
adaptive problem.

Independent review: both exact certificates passed a separate check of
their norms, perpendicular translations, midpoint equalities, residue
classes, and actual common white points.
