# Hilbert prefix extrema belong to the ancestor-face menu

15 November 2026. A coordinate extremum of a traversal prefix is an
ancestor face. Thus the running-record candidates in a multi-anchor
cap menu are bounded shifts of the same face grids used in the earlier
cap incidence estimates.

This restores the face-grid counting input. It does not make two
independently projected coordinates the paired corner of one node.
The separate target-first packing argument in
[the rank-dependent P-pair note](continuation_rank_dependent_cap_p_pairs.md)
addresses that issue without requiring a paired corner.

## 1. Prefix maximum and minimum

Let a recursive traversal visit every aligned dyadic square contiguously,
and visit its four child quadrants one at a time in any order. Within
each child the traversal has the same recursive property, with arbitrary
coordinate isometries. Fix a node Q, a rank r in Q, and one coordinate.
Consider the maximum coordinate among the points of Q visited from
its entry through r.

That maximum is a coordinate face of some ancestor R of r contained
in Q. A leaf counts as an ancestor. The corresponding assertion holds
for the minimum.

Here is an induction. Let C be the child of Q containing r.
A completed child has as its coordinate projection either the lower
half or the upper half of Q's projection. Its maximum is the upper
face of that half.

If C is in the lower half and some completed child is in the upper
half, the prefix maximum is Q's upper face. If a completed child is
in the same half as C, its maximum is C's upper face; this dominates
the entire incomplete prefix in C. If C is in the upper half and
every completed child is in the lower half, each of their coordinates
is below the current point, so the maximum is determined inside C.
If there is no completed child, the same is true. Recurse in C in
the remaining cases.

All cases return either Q's face, C's face, or an ancestor face supplied
by the induction inside C. Reversing the chosen coordinate proves
the minimum statement.

The proof does not require one particular Hilbert quadrant order.
It only uses the consecutive full-child property and the two coordinate
halves of an axis-aligned square.

## 2. Multi-anchor records have deterministic face origins

In a selected cap Q, the opposite coordinate starts at one face and
ends at the other. Its running first-hit record is a prefix maximum
or minimum, depending on that orientation.

Suppose every bad raw run in the relevant coordinate interval has
length at most G. The good raw levels bracketing that record are
within G+1 of it. The copied intermediate-anchor values at rank r
therefore have raw-coordinate origins

    c_R+e,    R an ancestor of r contained in Q,
    c_R a face in the relevant coordinate,
    |e|<=G+1.                                             (1)

The appended exit return uses a face of Q itself. Include the original
common-coordinate cap face and the unchanged raw leaf value in (1).

If the selected Q is unknown before sampling, it is enough to enumerate
all ancestors R of r. There are O((G+1)log N) possible coordinate
origins. Any cap-trigger witness can still enumerate Q separately.
The value menu itself does not require a quadratic number of depth
choices.

For the hybrid construction, old-fill caps keep their old forms and
the other caps use (1). Their union is covered by the same enumeration.

## 3. Shifted face-grid mass

Work on a complete side-N square. Fix a dyadic side a, a coordinate
role, a lower or upper face, and an integer shift e. Enumerate every
side-a node R and every rank lying in R, assigning the coordinate
origin c_R+e to that rank. Let M_(a,e)(c) count these assignments.

Its support is one translated a-grid, and

    M_(a,e)(c)<=Na,    sum_c M_(a,e)(c)<=N^2.              (2)

Indeed, fixing the chosen coordinate face leaves N/a possible nodes
in the other coordinate, each contributing a^2 ranks. Values outside
the valid raw coordinate domain can be omitted. Two face signs change
the constants only.

For arbitrary shifts e,f, any W>=0, and dyadic sides a,b, (2) gives

    sum_(|c-d|<=W) M_(a,e)(c) M_(b,f)(d)
       <= C N^3 (W+min(a,b)).                            (3)

For example assume a<=b. For each d, its W-neighborhood meets at
most O(W/a+1) points of the translated a-grid, each with mass at
most Na. Multiply the resulting O(N(W+a)) bound by the total b-mass
N^2. No alignment between the two shifted grids is needed.

On a raw domain of diameter O(N), dyadic summation also gives

    sum_(c,d) M_(a,e)(c) M_(b,f)(d)/(1+|c-d|)
       <= C N^3 (min(a,b)+log(2N)).                      (4)

The unit-distance range uses (3) at W=1. At each larger dyadic
distance W, its contribution is at most C N^3(1+min(a,b)/W).
Summing proves (4).

These are the original cap grid-mass estimates, uniformly in the
shifts. A union over t chosen shifts costs at most O((G+1)^t).
A union over depths retains its previous logarithmic factors.

## 4. Counting scope

If every selected cap has side at most L_*, each ancestor R in (1)
also has side at most L_*. Actual copied anchors remain inside Q,
even if the shifted candidate face lies outside the smaller R.
The realized partial locality and the two-row sampling kernels remain
separate inputs.

Consequently, a long-six argument whose cap inputs are the deterministic
face menu, (2)--(4), the side bound L_*, and the realized locality can
use the multi-anchor menu after the explicit shift union. With
G=h^o(1), any fixed-arity shift cost remains h^o(1). Selection and
eligibility conditions must be discarded only after this deterministic
menu has been formed.

This does not automatically transfer the paired-corner bidirectional-P
argument. A virtual coordinate copied from a face of Q and its other
coordinate copied from a face of a proper descendant R need not form
an entry or exit corner of either node. The
[rank-dependent target-pair theorem](continuation_rank_dependent_cap_p_pairs.md)
supplies the needed different argument: sum genuine source cells
separately for each target before summing target ranks. It restores
the bidirectional-P bound with the explicit per-target menu factor.

Likewise, no all-length reachability bound or P-valid filling follows
from the mass estimates. They resolve the running-record provenance
issue for the stated counting inputs.

Independent review: the full prefix-face induction, deterministic menu,
shifted point masses, near-pair sum, and reciprocal sum passed a separate
written review. The distinct role of the P-pair argument is retained.

