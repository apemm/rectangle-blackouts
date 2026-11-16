# Sparse bad rows do not permit a universal two-parity locality repair

15 November 2026. A universal constant-factor extension theorem for the
proposed singleton-stub repair is false, even for a bijective Hilbert order.
The obstruction uses only \(O(B)\) bad rows inside a much larger ambient
strip. Every good original black point is retained, while the repair may
add arbitrary good-row points of either parity. Full occupancy still forces
an unbounded loss in the square-root locality constant.

This is a limitation of a general repair theorem based on bad-row cardinality.
It does not assert that the actual arithmetic R2s bad-row sets have the form
used here. Deleting additional good original points, or changing the label
order, is also outside the obstruction.

## 1. A precise extension problem

An injective order of row-pair labels gives two integer functions
\(f_0,g_0\) on a consecutive rank interval. Assume each obeys
\[
 |f_0(r)-f_0(s)|,\ |g_0(r)-g_0(s)|\le C_0\sqrt{|r-s|}.       \tag{1}
\]
Choose good value sets \(F,G\). Retain every original first-coordinate
point with \(f_0(r)\in F\), and every original second-coordinate point
with \(g_0(r)\in G\). A repair consists of partial functions \(f,g\)
with these properties:

1. They retain all those original good values at their original ranks.
2. Their values belong to \(F\) and \(G\), respectively.
3. Every rank belongs to at least one of their domains.
4. Each partial function satisfies (1), on its own domain, with a proposed
   constant \(C\) in place of \(C_0\).

Both parities may be present at a repaired rank. Values not used by the
original order may also be used. These freedoms do not remove the example.

Physical parity rows \(a_0+Df\), \(b_0+Dg\), for fixed even \(D\),
are obtained by a common scaling and translation. The locality constants
are multiplied by \(D\); the obstruction is unchanged.

## 2. An injective Hilbert block

Let \(A\ge2\) and \(B=A^2\) be powers of two. Take the usual Hilbert
order of all \(B^2\) points in \([0,B-1]^2\). Its coordinate functions
have \(C_0=4\), and consecutive coordinate values change by at most one.
Choose the coordinate orientation so that \(g_0(0)=0\). The order also
visits a point with \(g_0=B-1\).

Inside the block, declare the first-coordinate multiples of \(A\) good,
and declare only second-coordinate values 0 and \(B-1\) good. All values
outside the block's coordinate interval may remain good. In normalized
integer coordinates, one can take
\[
 F=(\mathbb Z\setminus[0,B-1])\cup
       \{0,A,2A,\ldots,B-A\},
\qquad
 G=\mathbb Z\setminus[1,B-2].                               \tag{2}
\]
There are fewer than \(B\) bad values in each parity. Distinct retained
first-coordinate levels inside the block lie in different components of
the graph on \(F\) that connects values of distance less than \(A\).
Allowing all outside values therefore cannot connect two such levels by
steps smaller than \(A\).

An interval containing \(N\) distinct original labels cannot have
first-coordinate span at most \(2A\) unless
\[
 N\le(2A+1)(4\sqrt N+1)\le15A\sqrt N,
 \quad\text{hence}\quad N\le225A^2.                         \tag{3}
\]
The first inequality counts the possible integer row pairs, using
injectivity and (1) for the second coordinate.

Consequently, every rank interval with more than \(225A^2\) labels has
first-coordinate span greater than \(2A\). Since the Hilbert path changes
that coordinate by at most one, it visits two distinct multiples of \(A\)
within that interval. Both corresponding first-parity points are retained.

## 3. A forced empty interval gives the contradiction

Suppose a repair exists with \(C<A\). If its second parity were absent
throughout a rank interval with more than \(225A^2\) points, its first
parity would have to be present at every rank there. Section 2 supplies two
retained first-coordinate levels in different components of \(F\).
Some two consecutive ranks would therefore have first-coordinate values
differing by at least \(A\), contrary to their Hölder bound with \(C<A\).

Thus every consecutive pair of ranks in the repaired second-parity domain
has distance at most
\[
 225A^2+1.                                                   \tag{4}
\]
The second parity retains one value 0 and a later value \(B-1\). Every
allowed second value is either at most 0 or at least \(B-1\). Along its
ordered domain there is therefore a consecutive pair that crosses this
gap. Equations (1) and (4) force
\[
 (B-1)^2\le C^2(225A^2+1).                                  \tag{5}
\]
Hence every repair satisfies
\[
 C\ge\min\left(A,\frac{B-1}{\sqrt{225A^2+1}}\right)
   =\frac{B-1}{\sqrt{225B+1}}
   =\Omega(\sqrt B).                                        \tag{6}
\]
The equality uses \(B=A^2\); the second displayed quantity is less than
\(A\). The original constant was the absolute value 4.

## 4. Embedding in a full label order and in triangular orders

A dyadically aligned \(B\times B\) square is a contiguous Hilbert block
inside any sufficiently large dyadic ambient square. The restriction to
that block is a Hilbert order up to a coordinate symmetry. Choose the bad
row sets after that symmetry and translate (2) to its physical row ranges.
All other rows remain good. Additional retained points outside the block
only impose more constraints; they cannot invalidate the argument inside it.

Thus the example is compatible with a genuine complete, injective label
grid. For any fixed \(\beta>0\), the ambient height can be chosen so large
that the \(O(B)\) bad rows are \(O(h^\beta)\). For example, taking the
ambient side proportional to \(B^2\) gives \(O(\sqrt h)\) bad rows but
forces a locality constant of order at least \(h^{1/4}\).

The same argument applies to the unfiltered triangular order in
[`continuation_hole_free_rectangles_and_triangles.md`](continuation_hole_free_rectangles_and_triangles.md).
Use \(T_B\) and physical index coordinates \((f_0,g_0)=(u,u+v)\),
up to translations. They are injective, have locality constant 7, and both
coordinates change by at most one on each step. One visits second-coordinate
values 0 and \(B-1\). The analogue of (3) is
\[
 N\le(2A+1)(7\sqrt N+1)\le24A\sqrt N,
\]
so \(225\) is replaced by \(576\). Taking the same good sets again forces
\(C=\Omega(\sqrt B)\). Hence changing from the square order to this
triangular order does not make a cardinality-only stub-extension theorem true.

## 5. What remains possible

The failed assertion was a universal constant-factor extension retaining
every good original point. This example leaves several narrower routes open:

- the arithmetic R2s exceptional rows may have structure absent from (2);
- a repair may relocate some additional good points;
- a fresh label ordering may avoid the forced retained transitions;
- a construction may tolerate a quantified locality loss and charge it
  against a different width budget.

No obstruction to the unrestricted quadratic-width problem is claimed.
The Hilbert-block proof and its constants were checked independently by a
second reader before this note was written.
