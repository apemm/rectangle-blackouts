# Assembly of the constant-sea quadratic scaffold

15 November 2026. The complete integration passed a separate
dependency review.
The cited local proofs have independent reviews. The simultaneous choice
of the four residual families remains open. This is not a proof of
`m_h=O(h^2)`.

## 1. What the assembled construction supplies

For all sufficiently large heights, there are at most eight rectangular
row pools covering all but `O(h)` parity labels. In each pool, a constant
odd sea occupies columns outside `0 mod4`. The occupied arithmetic core
has these properties:

* Every column is occupied, with one or two black points. Only retained
  original labels are doubles, each exactly once.
* All actual rows satisfy the prescribed residue, half-strip, and bulk
  restrictions. The R2s side-owner rows are excluded.
* Nonhorizontal same-parity integral distances, same-parity right
  triangles, and same-parity mixed four-supports are absent.
* A fixed-size block may permute its eligible genuine doubles. Fine
  interpolation preserves the preceding properties and full occupancy.
* Both endpoints are good even anchor rows whose difference from the sea
  is an odd prime. Filled collars of width `O(h^2)` reach constant row-h
  tails, under the same residual exclusion on the guarded core.

The core widths, the number of profiles, and the collar widths have
quadratic total cost. Relocating the row/cap exceptions costs
`h^(11/6+o(1))` labels before any additional P cleanup. The existing
positional relocation input charges a subpolynomial factor per exception,
plus a quadratic filled-window cost.

## 2. Dependency order

First choose a fixed permitted permutation block size `k`. The constants
in the interpolation mesh and its locality bound depend on `k`, not on
height. Define the R2s bad-row superset for that weak locality, then
enlarge it by the fixed interpolation radius. It still has
`h^(5/6+o(1))` rows. Include the bounded bulk and central exclusions.

The [constant-sea core theorem](continuation_constant_odd_sea_core.md)
provides the eight row pools and exact geometric classification. The
[R2s transfer](continuation_step_four_r2s_transfer.md) supplies the
bad-row exponent, including isolated fine-mesh slope-one seams.

Choose a good prime-gap even anchor in the required fixed residue class.
The fixed-modulus prime count supplies `Theta(h/log h)` candidates;
the enlarged bad-row set removes fewer. Choose the odd anchor near the
appropriate strip edge. Use
[folded anchors](continuation_folded_anchor_caps.md), with independent
row offsets in a padded Hilbert square. The genuine rectangle is
unchanged. Every raw bad coordinate has at most three offset preimages,
so the good-cap area remains `O(h b log h)`.

Use total virtual cap functions and prefer an even singleton whenever
possible. Permute only eligible genuine objects and use
[the separated interpolation mesh](continuation_permuted_step_four_interpolation.md).
Its forbidden-set buffer makes both interpolated options good on changed
edges. On unchanged edges, only the old two endpoint options occur.
Every fine rank therefore has a good option, and the intrinsic odd-only
count stays within a fixed multiple of the coarse count.

The [spacing-four geometry](continuation_step_four_refinement.md), together
with its permutation extension, excludes all same-parity internal
supports needed by the core classification. In particular, the isolated
`(4,4)` seams have nonintegral length and cannot combine into a black
right angle. The stronger cone lemma excludes all same-parity mixed
supports without relying on a strict norm-gap inequality at those seams.

Finally append the prime-gap, adjacent-row, and checkerboard-path collars
from [the guarded joining theorem](continuation_lipschitz_collar_graphs.md).
Its guards have the full established local-pattern span, including the
completion column. Any additional constant-anchor arithmetic points
belong to the enlarged core's residual constraint set. This last condition
must not be omitted when solving the core.

## 3. P cleanup that is compatible with this assembly

The folded-coordinate incidence proof treats an exceptional odd source
as follows. An affine source retains its own independent odd-row offset;
unavailability of its even option restricts the even offset to a bad-row
set. If the odd source is an anchor, that anchor is within `O(b+1)` of a
strip edge, and the in-strip norm condition restricts its horizontal gap.
The even anchor need not be near a strip edge. This gives the reviewed
`h^(23/12+o(1))` incidence bound before any erasure-only repair.

For the refined permutation union, candidate values are bounded integer
shifts of boundedly many coarse raw/cap candidates. Changed edges have
both options good and add no intrinsic odd sources. An unchanged forced
source has a bad coarse even endpoint, with only a constant number of
endpoint and branch choices. Anchored odd candidates remain a bounded
distance from the same strip edge. Thus the affine-offset and boundary
arguments have the same exponents. The integration review checked this
specific transfer; a generic finite-union claim alone would not
justify a theorem using other Hilbert properties.

The genuine-source small-half-factor count uses its affine odd offset
and an affine or anchored even target. Applying the same sparse cleanup
therefore leaves genuine-source actual P gaps at least `h^(1-o(1))`.
Its own-row-gap comparison uses the counterfactual even coordinate of the
genuine object, which remains available in the geometric proof after
one of its actual points is erased.

Erasing the odd point of a marked double leaves its even point. Erasing
an even target of an exceptional odd source leaves its odd point. Both
operations preserve occupancy and only remove positive supports. They
cannot be performed on a singleton if that would empty its column, and
they cannot erase both points of one object. A consistent order is to
perform the genuine-source cleanup first, then convert only surviving
doubles targeted by exceptional odd sources. The already-singleton
targets remain explicit constraints.

The positional relocation theorem remains an external input. It must
place every relocated pair exactly once, with filled row-h tails. Once
the residual choices are valid, the retained and relocated doubles then
partition all parity labels, and the resulting board has `m+q_h` black
points.

## 4. The unsolved choice theorem

The construction still has to avoid simultaneously, on its ACTUAL
selected and guarded point set:

1. Opposite-parity in-strip P diagonals, including forced singleton paths.
2. Three-inserted-point tilted right triangles using both parities.
3. Nonvertical mixed four-inserted-point supports using both parities.
4. Two parked label-vertex triples sharing a white completion.

The fourth family includes both equal and distinct sea offsets. Its
same-parity distinct-offset raw-coordinate case already leads to the
unresolved Hilbert row-section correlation. Neither a small incidence
bound nor a long P gap supplies a simultaneous solution.

The constant-sea classification removes the additional one-label/two-sea
and sea-vertex triangle families that obstructed the two-low-row profiles.
The folded anchors and guarded joins resolve the filler and endpoint
compatibility for this conditional scaffold. They do not solve these
four core constraints. No threshold lower bound, all-width optimum, or
general counting formula follows from the assembly alone.
