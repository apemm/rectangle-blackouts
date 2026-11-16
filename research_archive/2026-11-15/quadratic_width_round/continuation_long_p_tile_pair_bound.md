# Long P has at most two arithmetic types per tile-pair role

15 November 2026. Three integer Pythagorean triples in a fixed-size
box cannot occur arbitrarily far from the origin unless they lie on
one ruling of the cone. For physical four-square tiles, the stride
excludes that ruling. Consequently every sufficiently long pair of
tiles has at most two candidate vectors per opposite-parity role.

This bounds the number of arithmetic relation types between two
tiles. It does not bound the number of neighboring tiles, or solve
the permutation constraints simultaneously.

Independent review checked the Cramer bounds, the identically-zero
polynomial case, and the proportionality exclusion. The arithmetic
two-type conclusion passed without corrections.

## 1. A quantitative bounded-box lemma for the cone

Write
\[
 Q(x,y,z)=x^2+y^2-z^2,
\qquad
 \langle u,v\rangle=u_xv_x+u_yv_y-u_zv_z.
\]
Let \(p_0,p_1,p_2\in\mathbb Z^3\) be three distinct points of
\(Q=0\). Suppose every coordinate of both
\(v_i=p_i-p_0\), \(i=1,2\), has absolute value at most
an integer \(R\ge1\). Then either the three points are
proportional, or every coordinate of \(p_0\) has absolute value
at most \(100R^8\).

First suppose \(v_1,v_2\) are linearly dependent. The polynomial
\(Q(p_0+t v_1)\) has three distinct zeros, so it vanishes
identically. Thus \(Q(v_1)=0\) and
\(\langle p_0,v_1\rangle=0\). Two nonzero null vectors in
signature \((2,1)\) that are orthogonal are proportional. This
follows directly from equality in Cauchy--Schwarz on their first two
coordinates. The three points are therefore proportional. Cases
involving the zero vector give the same conclusion directly.

Now suppose \(v_1,v_2\) are independent. The cone equations imply
\[
 \langle p_0,v_i\rangle=-Q(v_i)/2,\qquad i=1,2.
\tag{1}
\]
The right sides are integers, with absolute value at most \(2R^2\).
Choose a nonzero two-column minor \(\Delta\) of this rank-two
linear system, and let \(t\) be the remaining coordinate. Cramer's
rule writes every solution as
\[
 p(t)=\frac{a+bt}{\Delta},
\tag{2}
\]
where \(a,b\) are integer vectors. One coordinate of \(a\) is
zero, the corresponding coordinate of \(b\) is \(\Delta\),
and
\[
 1\le|\Delta|\le2R^2,
 \qquad |a_j|\le4R^3,
 \qquad |b_j|\le2R^2.
\]
Substitution in \(Q(p(t))=0\) gives an integer polynomial
\[
 A t^2+B t+C=0
\]
with
\[
 |A|\le12R^4,\qquad |B|\le32R^5,
 \qquad |C|\le32R^6.
\tag{3}
\]

The polynomial cannot vanish identically. If it did, \(a,b\)
would be orthogonal null vectors and therefore proportional. Equation
(1), applied for every \(t\), would then give
\(Q(v_i)=0\) and \(\langle b,v_i\rangle=0\). Both
\(v_i\) would be proportional to \(b\), a contradiction.

If \(A\ne0\), the elementary polynomial root bound gives
\[
 |t|\le1+\max(|B/A|,|C/A|)\le1+32R^6.
\]
The linear case has the same bound. Equation (2) consequently gives
\[
 |p_j|\le4R^3+2R^2(1+32R^6)
 \le70R^8<100R^8.
\]
This proves the lemma. The large constant is sufficient here; no
optimization is needed for a fixed-stride asymptotic construction.

## 2. Application to two four-square tiles

Each tile contains the sixteen row-pair labels in an aligned
\(4\times4\) physical index square, with within-tile row step
\(D\). Each tile occupies sixteen consecutive arithmetic columns
of stride \(S\). Its labels may be permuted arbitrarily.

Fix two distinct tiles and one role: the odd row from the first tile
and the even row from the second, or the reverse. Every candidate
vector has positive horizontal component
\[
 X=S q
\]
and odd positive vertical magnitude \(Y\), with
\(X^2+Y^2=L^2\), \(L\in\mathbb Z\). Across all possibilities
for this fixed role,
\[
 |\Delta X|\le30S,\qquad |\Delta Y|\le6D.
\tag{4}
\]
The absolute value in the definition of \(Y\) does not increase
the second bound. By the reverse triangle inequality,
\[
 |\Delta L|\le\sqrt{(\Delta X)^2+(\Delta Y)^2}
 \le30S+6D.
\]
Set \(R=30S+6D\). If three distinct candidate vectors occur
and one has
\[
 X>100R^8,
\tag{5}
\]
the cone lemma makes the triples proportional.

Assume also
\[
 S>18D^2.
\tag{6}
\]
Proportionality is impossible here. The difference of two distinct
proportional integer triples is itself a null vector. Its horizontal
component is a nonzero multiple of \(S\), and its vertical
component is nonzero with absolute value at most \(6D\). Therefore
\[
 0<(\Delta Y)^2\le36D^2<2S\le2|\Delta X|.
\]
Its squared Euclidean length lies strictly between the consecutive
squares \((\Delta X)^2\) and \((|\Delta X|+1)^2\), contrary
to integrality of \(\Delta L\).

Thus a tile-pair role whose candidate horizontal components satisfy
(5) has at most two distinct Pythagorean vectors. The two roles
together have at most four. Conditions (4) depend only on the size
of each tile, not on the distance between their coordinate origins.
The result therefore also applies to the packed good-row scaffold,
provided each retained tile has four genuinely consecutive physical
rows from each residue list.

## 3. Consequence after short-P exclusion

For fixed \(S,D\) satisfying (6), the threshold
\(100(30S+6D)^8/S\) for the slot gap is an absolute constant.
Any scaffold that excludes P through a slot-gap cutoff tending to
infinity eventually meets it. All remaining tile pairs then have
at most two arithmetic types per role.

For one vector \((Sq,Y)\), the slot relation is a partial matching
between the two sixteen-slot blocks. Its row relation is one fixed
cross-index difference, or both signs if both are available. These
are bounded-size relations, but a tile can still meet many other
tiles. Establishing a simultaneous permutation rule remains the
essential gap. The lemma also says nothing about three-label angles
or higher mixed supports.
