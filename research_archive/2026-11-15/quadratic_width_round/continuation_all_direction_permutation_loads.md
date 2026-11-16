# The exact all-direction permutation load and a fixed-stub obstruction

15 November 2026. The finite-direction permutation theorem has an
all-direction version under a local resource-load condition. The condition
also exposes a separate obstruction: fixed even stubs can rule out every
permutation of an arbitrarily large fixed Cartesian block, using only
long, large-factor P pairs. The specified obstruction edges form a
matching on potential point resources. Eliminating short P cycles does
not remove them.

Neither statement proves that the sampled scaffold satisfies the needed
load condition. The obstruction is a partial geometric configuration,
not an embedding into the sampled cap construction.

## 1. An all-direction load criterion

Use the full Cartesian permutation blocks of
[the finite-direction theorem](continuation_finite_direction_permutation_lll.md).
Each block has n=k^2 labels and n slots. An atomic assignment specifies
one label at one slot. A permutation resource is one label or one slot
of one block.

Form all compatible two-assignment canonical events that create an
actual P pair, in any direction. Events may be internal to a block or
join two blocks. Fixed outside points also generate unary events that
forbid one assignment. Deduplicate both families. For each resource R,
define

\[
 \Lambda_R=\sum_{E\text{ using }R}\Pr(E).
 \tag{1}
\]

The probabilities are 1/n for unary events, 1/[n(n-1)] for two assignments
in the same block, and 1/n^2 for assignments in distinct blocks.

**Load criterion.** If every resource satisfies

\[
                         \Lambda_R\le 1/16,
 \tag{2}
\]

there are simultaneous block permutations avoiding all these P events.
Every label is used once and every slot remains occupied.

Indeed, join canonical events that share a label or slot resource.
The product-permutation forcing coupling in the cited theorem makes
this a negative dependency graph. Put x_E=2Pr(E). An event uses at most
four resources, so its neighboring x-mass is at most8/16=1/2. Therefore

\[
 x_E\prod_{F\sim E}(1-x_F)
 \ge2\Pr(E)\left(1-\sum_{F\sim E}x_F\right)
 \ge\Pr(E).
\]

The local lemma applies. No direction count, block-degree bound, or
cycle assumption enters this implication.

Here is a sufficient condition phrased directly in terms of the potential
point resources (slot, odd row) and (slot, even row). First prune some
atomic assignments, and suppose each label and each slot loses at most
u of its n assignments. Among the retained point resources, suppose
each has at most D actual P partners of the opposite parity. This count
is over all directions and all blocks. Each opposite point resource can
be realized by at most k labels, so one retained atomic assignment has
at most2kD atomic partners. It follows that

\[
 \Lambda_R\le {u\over k^2}+{2kD\over k^2-1}.
 \tag{3}
\]

Thus a fixed D and sufficiently large fixed k solve the retained
all-direction problem, provided the pruning and fixed-boundary unary
loads also fit (3). A bound on the average number of P pairs alone does
not imply the per-label and per-slot inequalities in (3).

The missing probabilistic statement for this route is now precise:
produce a fixed k, a fixed D, and a sampled row realization for which
all but an affordable exceptional collection of blocks admit pruning
with u/k^2+2kD/(k^2-1)<=1/16, including all fixed singleton boundaries.
Neither the existing fixed-palette theorem nor the central short-cycle
estimates establish this statement. The interpolation points still need
their own canonical-event description before (1) can include them.

## 2. A matching of fixed-stub P constraints can forbid every state

Fix k>=2. Choose an integer stride S divisible by8 such that

\[
 S>\max\{16k,72(k-1)^2\}.
 \tag{4}
\]

Let t tend to infinity through t=1 mod4, and put

\[
 h=12t,\qquad b=10t,\qquad
 a_i=7t-12i,\qquad b_j=10t+4j
 \quad(0\le i,j<k).
 \tag{5}
\]

Place the k^2 Cartesian labels (a_i,b_j), in arbitrary order, at the
slots

\[
                     x_s=S s,\quad 0\le s<k^2.
 \tag{6}
\]

A common horizontal translation can make all columns positive. The
odd rows are3 mod4, the even rows are2 mod4, and every a_i exceeds h/2
once t is large in terms of k. For every pair (s,i), add the fixed even
stub

\[
                    E_{s,i}=(x_s+4(t+4i),b).
 \tag{7}
\]

These fixed columns lie on the fine4Z lattice. They are not asserted
to lie on the coarse S lattice. That distinction is necessary: an odd
multiple of the3--4--5 triangle has horizontal leg with2-adic valuation2.

All the stub columns are distinct. Equality of two columns in (7)
would give S(s-s')=16(i'-i); (4) forces i=i' and then s=s'. For large t
they also lie outside the central slot interval.

Suppose a permutation puts odd row a_i at slot x_s. Set v=t+4i. Its
odd point and the fixed stub E_{s,i} have displacement

\[
                         (4v,3v),\qquad L=5v.
 \tag{8}
\]

Their alternative vertical pair has column x_s+2v and rows

\[
                         b-4v=6t-16i,
 \qquad                    b+v=11t+4i.
 \tag{9}
\]

Both rows are in[1,h] for sufficiently large t. The column is2 mod4.
If the nonarithmetic columns carry the constant sea row1, both cells
in (9) are white. In a full-parity-owner construction, their odd/even
row pair has an owner elsewhere; it cannot be owned at this sea column.
The tilted rectangle from (8)--(9) and that axis rectangle then have
the same white set. This is the usual genuine P obstruction.

Consequently every central slot, under every permutation, creates at
least one actual P conflict with its prescribed fixed stub. No choice
of the k^2! block permutations helps.

The selected necessary constraints pair each potential odd point
(x_s,a_i) with its distinct fixed stub E_{s,i}. This specified point
resource graph is a matching. Additional P pairs might exist, but
are unnecessary. A proof that removes only cycles cannot remove this
matching obstruction.

In fact, for sufficiently large t the protected points have no additional
nonhorizontal integral pairs. To check an odd central point against a
stub E_{s',i'}, write its displacement as

\[
 (4t+C,3t+D),\qquad C=S(s'-s)+16i',\quad D=12i.
 \tag{10}
\]

There are only finitely many C,D. If its length is an integer, that
length is5t+z with z in a fixed finite integer set. Squaring gives

\[
 t(8C+6D-10z)+(C^2+D^2-z^2)=0.
 \tag{11}
\]

For sufficiently large t, both coefficients must vanish. Substituting
z=(4C+3D)/5 into the constant term gives(3C-4D)^2/25=0.
Thus C=16i, and (4) forces s'=s,i'=i. A central odd/even pair has
bounded horizontal separation and vertical separation3t+O(k), so its
nonzero squared horizontal separation eventually lies below the gap
between consecutive squares of its vertical separation. It cannot have
integer length. All remaining protected nonhorizontal pairs have the
same parity and are excluded by Section3.

Accordingly, after any central permutation, the actual nonhorizontal
integral-distance graph on the protected points consists of k^2
disjoint edges and isolated unused stubs. This statement omits the
separately supplied remote owners. The obstruction does not need a
cycle even before deleting any of these protected edges.

## 3. The obstruction respects the basic scale exclusions

For fixed k and S, both the P horizontal leg4v and the smaller
half-factor(L-3v)/2=v are Theta(h). Thus a cutoff h^(1-o(1)) on the
horizontal rank gap, or any sublinear smaller-factor cutoff, does not
remove these specified pairs merely by size. This is an assertion
about their own sizes, not survival under the full union of every
row-exception band.

The partial potential configuration also has uniform same-parity
nonhorizontal integral-distance exclusion over all central block
permutations. Between central odd resources the squared row difference
is at most144(k-1)^2<2S. Between central even resources it is smaller.
All fixed even stubs have the same row. A central even point differs
from a stub by at most4(k-1), while their horizontal separation tends
to infinity with t. Therefore, whenever the row difference is nonzero,

\[
                         (\Delta y)^2<2|\Delta x|
 \tag{12}
\]

for every compatible same-parity pair. Its squared distance lies
strictly between consecutive integer squares. This verifies the
uniform geometric hypothesis used in the permutation theorem for
the protected points.

It does not specify a Hölder-compatible filling of every omitted fine
column, nor does it place the remote axis owners, test every other
support family, or realize the points as a sampled Hilbert cap.
Those are deliberately outside this local boundary obstruction.

The conclusion is limited but useful: full Cartesian permutation
freedom, long P gaps, large half-factors, and same-parity geometry do
not supply the unary part of (2). Fixed singleton choices must be
included in the solvability argument, not attached after the genuine
permutations are chosen.

## Review status

The full written note passed an independent review of the canonical
probabilities, resource loads, product-permutation local lemma, stub
distinctness, actual P alternatives, matching-only norm graph, and
uniform same-parity exclusion. The fine4Z/coarse-S distinction and the
absence of a sampled/full-filling claim were checked separately.
