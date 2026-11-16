# Locally valid graph backgrounds for a collar

15 November 2026. Every integer 1-Lipschitz graph is identifying internally.
Its tilted one-white completions are parked at points of the same row
parity. Checkerboard graphs and arbitrary adjacent-row mixtures also have
no opposite-parity integral distance. A separate two-level construction
connects a low sea to a high constant row when their difference is a
suitable odd prime.

These are background lemmas. A complete collar must still separate these
pieces from the non-background core by the required locality guards and
match its endpoint rows. No global collar or quadratic threshold is claimed
without those conditions.

## 1. A cone lemma for mixed presentations

Rotate coordinates by putting \(U=x+y\), \(V=x-y\). Scaling all squared
lengths by two does not affect rectangles. A graph
\[
 \{(x,f(x)):x\in I\cap\mathbb Z\},\qquad
 |f(x)-f(x')|\le |x-x'|,                                  \tag{1}
\]
is a chain under the coordinatewise order in \((U,V)\).

Four distinct points of such a chain cannot form the black support of a
mixed side/diagonal presentation. Indeed, orient each of the two black
pairs increasingly along the chain. Their vectors have nonnegative
coordinates and equal lengths. The displacement between their midpoints
must be perpendicular to the black side vector.

If one pair interval contains the other, its vector dominates the other's
coordinatewise. Equal lengths force equal vectors and identical endpoints.
If the intervals are disjoint, the midpoint displacement has positive dot
product with either nonzero pair vector.

For the remaining interlacing order \(A\le C\le B\le D\), write
\(p=C-A\), \(q=B-C\), \(r=D-B\), all coordinatewise nonnegative.
The pair vectors are \(p+q\), \(q+r\), and twice the midpoint
displacement is \(p+r\). If its dot product with \(q+r\) vanishes,
then \(r=0\), and equal lengths imply \(p=0\). The same argument
with the pairs reversed treats perpendicularity to \(p+q\). Either case
duplicates the pairs. Thus no nondegenerate mixed support exists.

## 2. Right triangles have unique completions

Let three chain points be ordered \(A\le B\le C\). A right angle
cannot occur at \(A\) or \(C\), since the two nonzero leg vectors
there have the same coordinate signs and are comparable. At \(B\),
orthogonality forces each coordinate product to vanish. One leg is
horizontal and the other vertical in \((U,V)\). In the original
coordinates these are slopes \(+1\) and \(-1\).

Thus a black right triangle is exactly three corners of an axis rectangle
in the rotated coordinates. Its fourth corner is incomparable to the turn
corner and so cannot also belong to the chain. There is no fully black
rectangle.

For a fixed missing corner \(W=(u,v)\), at most one such triple belongs
to the chain. Consider first a triple whose turn is northwest of \(W\).
It consists of
\[
 (p,v),\quad(p,q),\quad(u,q),\qquad p<u, q>v.             \tag{2}
\]
Two different values of \(p\) would make the earlier turn incomparable
to the later point at height \(v\). Two different values of \(q\)
similarly create incomparable points at first coordinate \(u\).
Hence both are unique. A second triple of the southeast orientation also
creates an incomparable pair with (2). This proves uniqueness.

Three common rectangle vertices determine the rectangle. Two-white
collisions of the same kind force a fully black rectangle; mixed ones
were excluded in Section 1. The absence of hidden rectangles and repeated
one-white completions therefore proves internal identifying validity of
(1), on any integer strip in which its black points lie.

## 3. Parking and the two convenient P-free cases

The preceding statement also gives a direct parking rule when every
integer column of the interval is occupied. Suppose the right-angle vertex
is \((x_0,y_0)\), and the other two vertices are
\[
 (x_0-a,y_0+\epsilon a),\quad
 (x_0+b,y_0+\epsilon b),
 \qquad a,b>0,\quad\epsilon\in\{1,-1\}.
\]
The completion has column \(x_0+b-a\), between the two endpoints.
Equality in (1) forces the graph to follow the corresponding slope-one
arm throughout each of the two intervals. At the completion column the
existing graph row is \(y_0+\epsilon|b-a|\), whereas the completion
row is \(y_0+\epsilon(a+b)\). Their difference is
\(2\epsilon\min(a,b)\). In particular they have the same row parity.

Consequently a tilted one-white presentation from this graph cannot
coincide with an axis presentation whose double pairs opposite row
parities, even if its owner is elsewhere in the board.

Two useful subclasses also exclude every nonhorizontal opposite-parity
integral distance:

* A checkerboard graph, where \(x+f(x)\) has fixed parity. Opposite row
  parity then forces both coordinate differences odd, and their squared
  length is \(2\pmod4\).
* Any graph using only adjacent integer rows \(B,B+1\). Its nonhorizontal
  squared distances are \(X^2+1\), strictly between consecutive squares
  for every nonzero integer \(X\).

Thus arbitrary mixtures of two adjacent rows, and checkerboard walks with
steps \(+1\) or \(-1\), supply internally valid backgrounds with neither
unparked tilted completions nor the ordinary opposite-parity P rival.
An arbitrary 1-Lipschitz graph need not have the latter P property.

## 4. A low-to-high two-level connector

Let \(L\) be odd and \(B\) even, with
\[
 2L<B\le h,\qquad 2B-L>h.                               \tag{3}
\]
At each integer column, choose exactly one of rows \(L,B\), in any
pattern. This background is internally identifying.

A nondegenerate right triangle must have two vertices on one level and
its right angle on the other. Its completion row is either \(2L-B<1\)
or \(2B-L>h\). A right angle at an endpoint of the horizontal black
pair would require a second black point in that same column. Thus there
are no in-strip one-white presentations and no hidden rectangles.

For a mixed two-white presentation, consider the two black pairs. If one
is horizontal and one crosses the levels, the horizontal common pair
would have a half-integer row: their midpoint row parities are incompatible
because \(B-L\) is odd. If both pairs cross the levels, equal norms
force equal absolute horizontal gaps. Their midpoints have the same row,
and perpendicularity to a nonvertical crossed side forces coincident
midpoints, yielding the degenerate presentation. If both are horizontal,
equal length and the midpoint condition likewise identify the common pair
with one of the supposed black pairs. This exhausts the mixed cases.

Suppose in addition that
\[
 p=B-L\text{ is prime},\qquad p^2>2h.                     \tag{4}
\]
Any nonhorizontal integral distance between these rows solves
\(X^2+p^2=Z^2\). Since \(p\) is odd prime and \(X>0\), factorization
of \((Z-X)(Z+X)=p^2\) gives
\(Z=(p^2+1)/2>h\). Hence there is no actual in-strip P rival, regardless
of remote axis owners. Primality is only used for this last conclusion;
internal identifying validity used (3) and opposite row parity.

## 5. What these lemmas provide for a collar

The two-level connector may end in a constant \(B\) segment. A mixture
of \(B,B+1\) can then introduce an adjacent-row zigzag. A checkerboard
walk can rise to the top adjacent-row zigzag, and another adjacent-row
mixture can end in the constant row \(h\). The endpoint checkerboard
phase can be chosen by the parity of the starting column.

Each individual piece has the internal and remote-axis properties proved
above. Their union still requires a joining argument: points in different
pieces can form tilted supports. Locality guards of sufficient width,
agreement on the overlap, and a compatible constant-row endpoint of the
main core are separate hypotheses, not consequences of this note. Existence
of a good even \(B\) satisfying (3)--(4) also belongs to that integration.

## 6. A complete guarded join, conditional on the core residuals

Use the established local criterion V1--V5 with
\[
 D_*=2W_h+1,\qquad G=4\lceil D_*/4\rceil.                \tag{5}
\]
Every local violation has column span at most \(D_*-1\), including a
repeated completion and its completion column. The full final parity-pair
graph represents any remote axis owner; that owner's column is not included
in this local span. This is the same locality input used in
[the H7 dependency audit](continuation_cap_h7_dependency_audit.md), Section 7.

Assume a finite low constant-odd-sea core has the prescribed high even
anchor \(B\) at its two endpoint inserted columns. In its right extension,
put the same anchor at every inserted column \(0\pmod4\), with sea row
\(L\) at all other columns. Retain this profile for \(G\) columns.
Make the analogous extension to the left. The hypotheses on the core are:

1. The constant-sea geometric and good-row hypotheses hold on the core
   together with these inserted-anchor extensions.
2. Its four residual systems are absent on that enlarged point set:
   P, inserted three-corner supports, nonvertical inserted mixed supports,
   and repeated parked triples. The remote-owner convention is the one
   stated above.
3. The endpoint anchor satisfies (3)--(4). Actual doubles are distinct
   opposite-parity pairs; all new extension columns are singletons.

The first two hypotheses are assertions about the enlarged core, not just
the original finite core. Constant extension preserves the same-parity
bound when its endpoint value agrees, but its new P and higher-order
supports still belong to the required residual exclusion. The folded
anchor construction in
[continuation_folded_anchor_caps.md](continuation_folded_anchor_caps.md)
supplies suitable endpoint values; it does not by itself settle these
residuals.

Beyond the right profile extension, append these stages:

* \(G\) columns all at row \(B\);
* \(G\) columns alternating between \(B\) and \(B+1\);
* a checkerboard walk with increments \(+1\), rising from its current
  row to \(h\), then continuing in the alternating rows \(h-1,h\);
* at least \(G\) columns of that top alternating pattern;
* a constant row-\(h\) tail.

The walk from the low to high alternating patterns has length at most
\(h+1\). Choose the first low alternating value to agree with the desired
checkerboard phase. The ascent and its following top pattern then have
the same phase automatically. Reverse the horizontal order for the left
collar. For sufficiently large heights the anchor interval guarantees
\(B+1\le h\).

Here is the full joining check. A local pattern meeting the original core
cannot reach beyond its profile extension; it is excluded by the enlarged
core hypotheses. A pattern meeting the transition from that profile to
constant \(B\) uses only rows \(L,B\), so Section 4 applies. One meeting
the next transition uses only \(B,B+1\), so Section 3 applies. The low
alternating guard separates that transition from the ascent. All patterns
within the low zigzag, ascent, and high zigzag lie in one checkerboard
1-Lipschitz graph. The top alternating guard separates the ascent from
the final transition, which uses only \(h-1,h\). No span-\((D_*-1)\)
pattern crosses an entire \(G\)-column guard. These comparisons exclude
all local V1--V5 patterns, including repeated singleton completions and
the locally encoded remote-owner cases.

Each collar has width at most \(4G+h+O(1)=O(h^2)\), besides an arbitrary
constant-row tail. The tails allow complete windows to be separated by
at least \(D_*\) constant row-\(h\) columns, as in the existing joining
lemma. Every collar column is a singleton, so the number of doubles and
the exact excess count are unchanged.

For a high constant-odd-sea core, reflect Section 4 vertically: choose a
low even anchor \(B\) with the reflected prime-gap and outside-completion
conditions. The high-sea/anchor transition is its reflected two-level
background. A vertical reflection may interchange the absolute row
parities; Section 4 only needs the two levels to have opposite parity,
so its proof still applies. From constant \(B\) onward, use the same adjacent-row bridge
and upward checkerboard walk to row \(h\). Thus both low- and high-sea
cores have the same final background, conditional on their enlarged
residual exclusions.

If valid filled relocation windows with row-\(h\) tails are supplied,
they can be joined to these cores with the stated guards. Distinct retained
and relocated pairs then give exactly one double for each parity label and
one black point in every other column, hence \(m+q_h\) black points.
The present theorem closes the collar step under its core and relocation
hypotheses. It does not supply the missing simultaneous choice theorem
for the four core residual systems.

## Review and exact checks

Sections 1--5 passed an independent written geometric review on 15 November
2026. The separate checker
[check_lipschitz_collar_graphs.py](check_lipschitz_collar_graphs.py)
enumerates all lattice rectangles through equal-center, equal-length
diagonal pairs. It checked 11,279 complete 1-Lipschitz graphs on the
\(5\times5\), \(6\times7\), and \(4\times9\) grids: identifying
validity and parking passed throughout. The checkerboard and adjacent-row
P claims passed as well. The checker also found a P event for a general
1-Lipschitz graph, confirming the stated scope distinction. Exact output
is saved in [check_lipschitz_collar_graphs.json](check_lipschitz_collar_graphs.json).
Section 6 also passed an independent written joining review. The review
checked the completion-column span, guard comparisons, checkerboard phase,
left reflection, width count, and the explicit enlarged-core hypotheses.
The complete note subsequently passed a second independent written review,
including the local V1--V5 convention for remote axis owners. No further
correction was needed.
