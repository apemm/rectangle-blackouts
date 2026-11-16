# A smaller-height board needs an ambient-aware embedding theorem

15 November 2026. Ordinary identifying validity does not survive insertion
into a taller strip with the full parity-pair owner graph. The failure can
occur under a height expansion arbitrarily close to one. A row-band
localization lemma separates this obstruction from the remaining local
triangle and mixed-support checks.

## 1. A filled background that fails after a small height expansion

Fix an even integer \(m\ge2\) and an odd positive integer \(t\).
Set
\[
 k=(m^2-1)t+1,\qquad H=(m^2+1)t+1,\qquad X=2mt.          \tag{1}
\]
In a height-\(k\) strip, put exactly one black point in each column,
using only rows 1 and \(k\). Include \((0,1)\) and \((X,k)\).
The other choices between the two levels are arbitrary.

This is an internally identifying filled background. The two levels
have opposite parity. Every three-black tilted rectangle would complete
at row \(2-k<1\) or \(2k-1>k\). In a mixed four-support, a crossed
row pair and horizontal row pair have incompatible midpoint parity;
two crossed pairs or two horizontal pairs give the degenerate equal-pair
case. This is the two-level lemma in
[continuation_lipschitz_collar_graphs.md](continuation_lipschitz_collar_graphs.md),
Section 4. Any nonhorizontal integral distance between the levels has
hypotenuse greater than their row span \(k-1\), so there is no actual
in-strip P rival either.

Translate this board upward by \(t\), into the height-\(H\) strip.
The two protected black points become
\[
 (0,t+1),\qquad (2mt,m^2t+1).
\]
Their vector is the Pythagorean triple
\[
 (2mt,(m^2-1)t,(m^2+1)t).                                \tag{2}
\]
The alternative vertical diagonal has column \(mt\) and rows exactly
\(1,H\). Those corners lie outside the embedded black row band and
are white. If the full parity-pair graph is supplied, a remote owner of
the opposite-parity pair \((1,H)\) creates the axis rival. Its owner
cannot occur at the common column \(mt\), where the embedded board
already has its prescribed singleton. Thus the embedded filled background
is not safe in the full ambient board.

As \(t\) grows, the expansion ratio tends to
\[
 \frac Hk\longrightarrow\frac{m^2+1}{m^2-1}.
\]
Choosing a large fixed even \(m\) makes this arbitrarily close to one.
Therefore no general lemma can embed an arbitrary smaller-height valid
board into even a slightly taller strip merely by translating it.
This counterexample has singleton columns; it does not rule out an
ambient-robust special family of smaller boards or a construction that
changes the filler while embedding.

## 2. Which local witnesses can leave a row band?

Suppose every local black point lies in a row interval \([A,A+w]\).
For a three-black right triangle, the fourth row is a signed sum of its
three rows, with two plus signs and one minus sign. It lies in
\[
 [A-w,A+2w].                                             \tag{3}
\]
This includes completions shared by two such triples.

For a mixed side/diagonal four-support entirely in the band, let \(P,Q\)
be the black side and \(R,S\) the black diagonal. The common white rows
are
\[
 \frac{p_y-q_y+r_y+s_y}{2},\qquad
 \frac{q_y-p_y+r_y+s_y}{2}.
\]
Both lie in
\[
 [A-w/2,A+3w/2].                                         \tag{4}
\]
Thus every all-local triangle, repeated completion, or mixed witness is
already visible in a strip of width \(3w\) around the original band.
This statement concerns the geometric witness; parking against a remote
axis owner must still be checked using the actual point in its completion
column and the full ambient parity graph.

The vertical P alternative is different. It is determined by only two
local black points and a remote owner. If their row gap is \(Y\le w\)
and their horizontal distance is \(X\), its vertical span is an integer
\(Z\) with \(X^2+Y^2=Z^2\). For nonzero \(Y\), integrality gives
\[
 2X+1\le Y^2\le w^2,
 \qquad X\le(w^2-1)/2,
 \qquad Z\le(w^2+1)/2.                                  \tag{5}
\]
The last inequality follows either from the norm or from
\((Z-X)(Z+X)=Y^2\). Consequently a quadratic-size vertical buffer
detects every possible P from the band, independent of the ambient height.
A linear-size buffer does not: (1)--(2) already refute plain local validity,
and choosing the factor-one triple with \(Y=w\) can put its alternate
span at order \(w^2\).

## 3. The induction statement that would actually be needed

To handle the own-gap band \(|b-a|\le c h\) by recursion, the input
cannot simply be "a valid board at height \(c h\)." It needs an
ambient-aware guarantee. One sufficient version would provide, for each
embedded row interval, the following properties:

* all local triangle, repeated-completion, and mixed checks remain valid
  on the expanded interval (3), with correct ambient parking;
* every integral opposite-parity pair whose alternative corners lie
  anywhere in the final height-\(h\) strip is excluded;
* the embedding keeps every required column occupied, covers each required
  double pair once, and has joins compatible with the other intervals.

The second condition is stronger than validity on the expanded
\(3c h\)-row interval when that interval is smaller than the ambient
strip. The first condition alone does not control the remote-owner
counterexample in Section 1. Conversely, these observations do not prove
that an \(O(c h^2)\) band construction is impossible. They identify the
additional invariant a recursive construction must preserve.

## Review status

The counterexample and all band-localization calculations passed an
independent written review. The full ambient owner condition and the
distinction from an ambient-robust special construction remain explicit.
