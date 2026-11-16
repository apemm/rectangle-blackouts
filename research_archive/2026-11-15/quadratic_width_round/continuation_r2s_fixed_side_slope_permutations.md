# Full permutation blocks avoid a finite R2s side-slope menu

15 November 2026. For a constant row-one sea, a fixed rational slope
of the black side in an R2s support gives a bounded number of
injective maps between candidate core points. The bound is independent
of height. Consequently, sufficiently large fixed Cartesian blocks
have simultaneous full-occupancy permutations avoiding every R2s
support in any prescribed finite side-slope menu.

This is a positive placement statement with an explicit arithmetic
load bound. It has no fixed outside stubs. It does not control the
complete height-dependent slope set, interpolated points, or the
other residual families.

## 1. Geometry and the integer parameter

Use the exact crossed R2s notation
\[
 A=(0,n+1),\quad B=(U,1),\quad
 C=(X,n+1+\delta),\quad D=(X+V,1).
\]
The in-strip common row \(1+\delta/2\) forces \(\delta>0\):
the row difference is a multiple of four, and \(\delta=0\)
would be degenerate. Reflect horizontally so \(U>0\). The equations
are
\[
 TU=n\delta,\qquad
 V^2=U^2-2n\delta-\delta^2,\qquad
 2X=U+T-V.                                           \tag{1}
\]
Assume the candidate core-point family satisfies
\[
                         \delta^2\le2|X|.            \tag{2}
\]
The isolated \((|X|,\delta)=(4,4)\) seam can instead be allowed:
it has no positive-offset R2s realization, by the explicit check in
[the good-row theorem](continuation_multiplicative_r2s_good_rows.md).

Fix coprime positive integers \(p,q\) and impose the black-side
slope
\[
                       U:n=p:q.
\]
Thus \(U=p\ell\) and \(n=q\ell\) for an integer \(\ell\ge1\).
Write
\[
 W=|V|,\qquad e=U-W.
\]
Equation (1) gives \(0<e\le U\), \(T>0\), and \(U>2T\). Also
\[
 (U-T)^2-W^2=T^2+\delta^2>0,
\]
so \(W<U-T\). It follows that both choices of the sign of \(V\)
give
\[
                         0<X<U.                     \tag{3}
\]
In particular \(\delta^2<2p\ell\).

Define the positive integer
\[
                         c=pe-q\delta.
\]
The square equation in (1) is exactly
\[
                         e^2+\delta^2=2\ell c.       \tag{4}
\]
To bound \(c\), observe that
\[
 e={2n\delta+\delta^2\over U+W}
       \le {2q\delta\over p}+2.
\]
Hence
\[
 e^2\le {8q^2\delta^2\over p^2}+8
       <{16q^2\ell\over p}+8,
\]
and (4) yields
\[
 1\le c<C(p,q):=
             \left\lceil p+{8q^2\over p}+4\right\rceil+1.       \tag{5}
\]
The harmless extra integer in this definition avoids endpoint
rounding conventions.

This bound uses the rational direction of the side, rather than a
fixed similarity class of the whole support. For a fixed side slope,
the positive row increment can still grow on the scale \(\sqrt h\).

## 2. Each bounded parameter gives a partial injection

Substitute \(e=(q\delta+c)/p\) into (4):
\[
 (p^2+q^2)\delta^2+2qc\delta+c^2=2\ell cp^2.           \tag{6}
\]
For fixed \(p,q,c\), the left side is strictly increasing for
\(\delta>0\). Thus each \(\ell\) has at most one positive solution
\(\delta\), and that solution increases strictly with \(\ell\).

The target row
\[
                         q\ell+1+\delta(\ell)
\]
therefore increases strictly with the source row \(q\ell+1\).
After choosing the sign of \(V\), equations (1) determine \(X\).
Choosing a horizontal orientation gives the point map
\[
 (x,q\ell+1)\longmapsto
 (x+\sigma X(\ell),q\ell+1+\delta(\ell)),
 \qquad \sigma\in\{-1,1\}.                           \tag{7}
\]
Restrict this map to the integer solutions that pass the actual
profile, sea-column, strip, parity and nondegeneracy conditions.
It is a partial injection on the integer point placements:
the source row determines the target displacement, while the
target row determines the source row uniquely.

For one parity-specific slope \((p,q)\), there are at most
\(4C(p,q)\) such partial injections: two horizontal orientations,
two signs of \(V\), and the integer choices in (5). This safely
overcounts any coincident branches. Every point resource has at
most one outgoing and one incoming neighbor per injection.

## 3. Simultaneous permutations

Each block has \(k^2\) slots and the full Cartesian label set
\[
                 \{(a_i,b_j):1\le i,j\le k\},
\]
with distinct odd rows \(a_i\) and distinct even rows \(b_j\).
All block labels and slots are prescribed. The only variables are
the bijections between them.

Require (2) for every pair of same-parity candidate point resources
that can coexist under these permutations, with the seam exception
allowed as above. It is enough to use the already established
uniform geometry for bounded permutations. No assumptions on the
number or adjacency graph of the blocks are needed.

Let \(\mathcal S\) be a finite list of parity-specific black-side
slopes, and set
\[
                  B=4\sum_{(\rho,p,q)\in\mathcal S}C(p,q).      \tag{8}
\]
Each entry specifies which core parity it concerns. If a slope is
to be controlled for both parities, include both entries.

**Theorem.** If
\[
                              k\ge32B+1,             \tag{9}
\]
there are simultaneous block permutations avoiding every crossed
R2s support whose side slope is in \(\mathcal S\).
Every original label is used exactly once and every block slot is
occupied.

Here is the full canonical-event bound. A point resource consists
of a slot and one candidate row. Exactly \(k\) label-slot assignments
realize it. For each injection in Section 2, forbid every compatible
pair of assignments realizing its two endpoints. Discard impossible
prescriptions, and deduplicate events.

One atomic label-slot assignment has at most \(2Bk\) conflicting
atomic partners: each injection has at most one incoming and one
outgoing point neighbor, and each neighbor is realized by \(k\)
labels. Since (8) already counts the roles, there is no additional
factor of two for the two points of a label.

Put \(N=k^2\). A two-assignment event has probability
\(1/[N(N-1)]\) in one permutation, or \(1/N^2\) in two different
permutations. A fixed permutation resource, either a label or a
slot, participates in \(N\) atomic assignments. Therefore
\[
 \sum_{E\text{ using a fixed resource}}\mathbb P(E)
       \le {2Bk\over k^2-1}=:\rho.                   \tag{10}
\]
The product-permutation negative-dependency coupling is exactly the
one proved in
[the finite-direction theorem](continuation_finite_direction_permutation_lll.md):
force prescribed assignments by swaps. A currently occurring event
using none of the forced labels or slots cannot be destroyed.

Under (9), \(\rho\le1/16\). Give each event local-lemma weight
\(2\mathbb P(E)\). Each event uses at most four resources, so the
sum of neighboring weights is at most \(8\rho\le1/2\). The product
of the complementary weights is therefore at least \(1/2\).
The asymmetric local lemma applies and proves the theorem.

If \(d\) Pythagorean directions are also prescribed, and the uniform
same-parity nonintegral-distance hypothesis of the finite-direction
theorem holds, they contribute at most \(2dk\) additional atomic
partners. The same proof gives the combined sufficient condition
\[
                              k\ge32(B+d)+1.         \tag{11}
\]

## 4. Uniformity and the remaining load question

A bounded permutation block can be given the required geometry by
the fixed stride choice in the finite-direction theorem. Since the
menu and \(k\) are fixed, this changes the width by a fixed factor.
The theorem allows interactions between arbitrary numbers of
variable blocks, rather than fixing all outside labels before
repairing one block.

For example, all primitive side slopes with \(1\le p,q\le H_0\)
can be removed using
\[
                   B=O(H_0^3\log(2H_0)),
\]
by summing (5). Here \(H_0\) is fixed independently of height.
There is no assertion that a bounded real angle interval has only
finitely many relevant rational slopes: their denominators may
grow.

The explicit obstruction in
[the stride note](continuation_r2s_stride_and_permutation_reduction.md)
has side ratio \(U/n=1/w\). Its required denominator grows with the
height. Thus it is consistent with this positive finite-menu
theorem, and it identifies a genuine limitation of a fixed menu.

To extend (9) to every R2s support, one needs a bound on the summed
canonical resource loads for the remaining height-dependent slopes,
or a method other than this sufficient local-lemma criterion.
The arithmetic row count \(h^{5/6+o(1)}\) alone does not supply such
a maximum load bound.

Fixed outside stubs create unary restrictions and are not covered.
Points created by interpolation also require a separate candidate
resource analysis. No avoidance of the other rectangle families
or completed quadratic-width blackout follows from this theorem.

## 5. Reduce the parameter count, and classify the horizontal half

The exact identity \(TU=n\delta\) improves (5). Since
\(T=q\delta/p\) is an integer and \(\gcd(p,q)=1\), write
\[
 \delta=pt,\qquad T=qt,\qquad
 \kappa=e-qt\in\mathbb Z_{>0},\qquad c=p\kappa.
\]
Thus one may replace \(C(p,q)\) everywhere by
\[
 \widetilde C(p,q)=
       \left\lceil1+{8q^2\over p^2}+{4\over p}\right\rceil+1,    \tag{12}
\]
and use
\[
 (p^2+q^2)t^2+2q\kappa t+\kappa^2=2p\ell\kappa.      \tag{13}
\]
The same monotonicity proves the partial-injection assertion.
For all \(p,q\le H_0\), the resulting total budget is
\(B=O(H_0^3)\), since \(\sum_{p\le H_0}p^{-2}=O(1)\).

There is a sharper exact result for all side slopes \(U/n\ge1\)
at once, including arbitrarily large denominators. Set
\[
                         a=X-T,\qquad b=U-X.
\]
Both are positive integers by (3) and \(W<U-T\), and direct
substitution gives
\[
                         4ab=T^2+\delta^2.          \tag{14}
\]
The hypothesis \(U\ge n\) is equivalent to \(T\le\delta\).
Using (2),
\[
 a\ge\delta^2/2-T,\qquad
 b\le {T^2+\delta^2\over2\delta^2-4T}
       \le {\delta\over\delta-2}.                   \tag{15}
\]
Here \(\delta\ge4\), and the denominators are positive.
For \(\delta\ge8\), (15) forces \(b=1\). When \(\delta=4\),
only \(b=1,2\) are possible.

If \(b=1\), (14) and (2) give
\[
                         \delta^2\le T^2+4T.
\]
Both \(T\) and \(\delta\) are even. If \(T\le\delta-2\), the
right side is at most \(\delta^2-4\), a contradiction. Hence
\[
 T=\delta,\quad U=n=X+1,\quad
 X=\delta^2/2+\delta.
\]
Writing \(\delta=4d\), the two core rows and their separation are
\[
 \begin{split}
 y_d&=8d^2+4d+2,\\
 z_d&=8d^2+8d+2,\\
 X_d&=8d^2+4d,
 \qquad d\ge1.
 \end{split}                                                   \tag{16}
\]
If \(b=2\), then \(\delta=4\). Equations (14)--(15), with
\(T\) positive and even, force
\[
                 T=4,\quad a=4,\quad X=8,\quad U=n=10.          \tag{17}
\]
This is the sole additional row pair \(11,15\), at separation
eight. The reconstruction has \(V=-2\) and passes the sea residues.

These calculations classify the whole horizontal half:
there is no R2s support with \(U>n\). At \(U=n\), (16) and
(17), with their two horizontal orientations, are the complete list.
In particular, an odd-profile source row above eleven always has
\(U<n\).

There is a particularly small global permutation budget for this
infinite family. The even row pairs in (16) are disjoint, since
\[
                         y_d<z_d<y_{d+1}.
\]
The exceptional pair (17) is odd. Thus each point resource has at
most two candidate neighbors in its role: the partner row at the
two allowed horizontal displacements. An atomic double assignment
has at most \(4k\) conflicting atomic partners over both roles.
The proof of Section 3 therefore gives:

**Horizontal-half corollary.** Under the same uniform geometry,
\(k\ge65\) permits simultaneous full-occupancy permutations avoiding
every constant-sea R2s support with \(|U|\ge n\), at every height.
If rows eleven and fifteen are absent, \(k\ge33\) suffices.
With \(d_0\) additional Pythagorean directions, replace these
thresholds by \(k\ge65+32d_0\) and \(k\ge33+32d_0\), respectively.

This corollary controls an infinite, height-dependent family.
The remaining R2s side slopes have \(0<|U|/n<1\); their joint
resource load is not bounded here.

Independent written review: all sections passed a separate derivation,
including the integer parameter, monotone partial injections, resource
counts, and the complete product-permutation local-lemma argument.
The complete horizontal-half classification, disjoint row pairs,
exceptional row pair, improved parameter count, and thresholds 65 and
33 also passed review. An exact integer check on
\(n\le300,\delta\le80,U\le500,U\ge n\) recovered precisely the
listed admitted families and verified the full-span inequality.

