# One-parity dyadic caps can consume the whole square

15 November 2026. Restricting the good-cap repair to odd caps does not give
a subquadratic relocation bound, even with a single bad odd row. The first
admissible ancestor can be the root on a positive proportion of offsets.
This concerns that particular repair rule, not arbitrary good-row extensions.
The target here is an everywhere-good odd option: every bad-odd leaf is
covered, even if its even option is already good. Covering only doubly-bad
leaves would not have that stronger target.

Let the standard Hilbert order on a square of side \(N=2n\) start at
\((0,0)\) and end at \((N-1,0)\). Swap its two coordinates, so the root
has common first coordinate zero. Call the first coordinate odd and the
second coordinate even. A nontrivial dyadic node is eligible for an odd
cap only if its two endpoints have equal first coordinate.

For each \(1\le k<n\), consider the cell
\[
 (k,n-1).                                                   \tag{1}
\]
It lies in the root's first child, where the swapped global Hilbert curve
is the unmodified standard curve on the lower-left \(n\)-square.
Its second coordinate is the top coordinate of that child. At every
subsequent scale it lies in one of the two middle children, numbered 1
and 2. Both middle children preserve the local orientation. Hence every
nontrivial proper ancestor of (1) has its common endpoint coordinate in
the second coordinate. None admits an odd cap. The root is the first
eligible odd-cap ancestor.

Suppose the clipped odd coordinate at (1) is bad, while the root's clipped
value is good, as it is in the padded construction. Its leaf cannot be
filled by its own odd value. Ascending through odd-cap ancestors therefore
selects the root. Inclusion-maximal selection then replaces all \(N^2\)
slots, including all genuine labels, by one odd cap.

The loss also occurs on average over the existing offset distribution.
Let the genuine first-coordinate interval have length \(m\), with
\(4m\le N<8m\), and fix one interior bad index \(j\in[1,m-2]\),
with every other odd index good. This bad value is unchanged by clipping;
a bad boundary value that clips to a good endpoint would not suffice.
The raw bad coordinate is \(k=U+j\), where
\(U\in\{1,\ldots,N-m-1\}\) is uniform. At least
\(N/2-m\ge N/4\) of these offsets give \(1\le k<N/2\).
For each, (1) forces selection of the root. Thus the expected selected
area is \(\Omega(N^2)\), even when the bad-row count is one.

The ordinary two-parity cap argument does not have this problem: it can
stop at an intervening good even cap. Nor does this obstruction rule out
non-dyadic caps, movable barriers, or a construction that erases additional
good points according to a different geometric rule. It does rule out
obtaining an everywhere-good odd virtual option by the naive modification
"skip every even-cap ancestor."

The companion checker verifies the complete ancestor chain for every
\(1\le k<N/2\), at powers of two \(4\le N\le1024\), using independent
rank-to-coordinate and coordinate-to-rank routines. This is a check of the
recursive proof, not a substitute for it.

The written recursion was independently reviewed on 15 November 2026.
The review clarified the everywhere-good target and the interior bad-index
condition in the averaging argument; both are included above.
