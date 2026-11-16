# Prescribed anchors in mechanical row classes

15 November 2026. A fixed good anchor can be inserted into every mechanical
row class without requiring a prime in that class. The modification
preserves bounded row gaps, the uniform affine approximation, full label
coverage, and the good-cap width budget. A small interpolation extension
handles the resulting bounded physical jumps.

This note does not transfer the new two-parameter triangle estimate to
every folded or cap-constant case.

## 1. Exact complementary occurrence lists

For `theta in [1/3,2/3]`, put

`w_theta(n)=floor((n+1)theta)-floor(n theta)`, for `n>=0`.

The positions of its ones and zeros, indexed from zero, are exactly

`p_i^1=ceil((i+1)/theta)-1`,

`p_i^0=floor(i/(1-theta))`.

The first formula follows by locating the `(i+1)`st increase of
`floor(n theta)`. For the second, the number of zeros before position
`n` is `n-floor(n theta)=ceil(n(1-theta))`.

Both lists are strictly increasing, with gaps at most three, and

`p_i^epsilon=alpha_epsilon i+O(1)`,

uniformly in `theta,i`, where `alpha_1=1/theta` and
`alpha_0=1/(1-theta)`. Both stretch factors lie in `[3/2,3]`.
Uniform sampling of `theta` gives a bounded density for either stretch
factor. Rational endpoints and floor discontinuities cause no issue
for these deterministic formulas.

Restrict the lists to one original finite residue-row interval. Its two
classes partition that interval. Both class sizes are `Theta(h)` in the
intended profile pools. Independent partitions of the odd and even row
pools give four Cartesian class products covering every original label
exactly once.

## 2. Insert a prescribed physical anchor

Choose a good physical anchor in the original row interval before
sampling `theta`. It can be the prime-gap even anchor or the odd anchor
near the appropriate strip edge. If a class does not contain that anchor,
insert it into the increasing class list. If it already occurs, make no
change.

This operation has four useful properties.

1. It preserves strict increase and cannot enlarge the largest gap.
2. Every original occurrence moves by at most one index, so the modified
   list still satisfies `p_i=alpha i+O(1)`, with an absolute uniform error.
3. Every bad physical value has at most one preimage in the modified list.
4. Each missing anchor adds only one virtual coordinate line to a
   Cartesian class product, containing `O(h)` objects.

An injected anchor is marked nongenuine in that class. Any object using
that virtual coordinate is a singleton padding object, never a new
double. The original class pairs still occur exactly once. This marking
prevents duplication of a label whose anchor row belongs genuinely to
the other class.

Only a fixed number of anchors and classes is needed. Their injection
therefore adds `O(h)` virtual objects and does not remove any original
label. It avoids a prime-distribution claim about individual mechanical
classes.

## 3. Folded caps and offset counts

Let `n` dominate all possible class sizes, including inserted anchors.
Choose the fixed padded side and offset range from the folded-anchor
construction using this maximum. They are independent of `theta`, and
the two offset intervals have length `Theta(h)`.

For each realized class, its anchor has an index in that class. Apply
the usual scalar folding map at that index, then the modified increasing
physical-row list. The fold leaves the genuine coordinate interval
unchanged. Its bad-value preimage count is at most three. The physical
list is injective and has Lipschitz constant at most three in row-index
units. Thus the square-root locality constant grows by only a fixed
factor.

Conditionally on any `theta`, at most `3b` offsets make a fixed raw
coordinate land in a prescribed set of `b` bad class values. The cap-area
expectation and its joint averaging with other nonnegative costs retain
their previous orders. The first-good-ancestor construction must still
include doubly bad padding positions.

The strong fixed offset margins put both endpoint neighborhoods at the
prescribed anchors. Inserting the same physical anchor in both classes
therefore preserves the common endpoint row needed by the guarded join.

## 4. Interpolation with bounded original jumps

After applying the occurrence lists, an unchanged Hilbert edge still
changes at most one coordinate, but that coordinate can jump by at most
`J=3` index units. The unit-step occupancy argument must be modified.

Let `B_alpha` be the actual forbidden physical-index set. Construct the
caps using its fixed-radius enlargement `B_alpha^(+D)`, where

`D >= max(J, ceil(C_0 sqrt(2k-1)))`.

Here `C_0` is the coarse physical-index Hölder constant and `k` is the
fixed permutation block size. Choose anchors outside the enlarged set.
Permit only the same cleared genuine-double permutations as before.

On a changed edge, one moved endpoint has distance greater than `D`
from the actual bad set in each coordinate. Its other endpoint is within
`D`, so all interpolated coordinate values are good.

On an unchanged edge, one coordinate is constant. If its value is good
for the actual bad set, it supplies occupancy throughout the edge. If
it is bad, both endpoint pairs must use their other coordinate outside
the enlarged bad set. The changing coordinate moves by at most `J<=D`,
so every intermediate value is good. This proves occupancy without
assuming unit physical gaps.

Use the same mesh `G=8D`, `M=32D^2`. The two geometric estimates in the
permutation-interpolation proof depend only on the adjacent jump bound
`D` and the coarse Hölder constant. They therefore remain unchanged.
All same-parity exclusions, including the isolated-seam qualification,
still hold.

A fine unavailable even option on an unchanged edge forces one coarse
even endpoint into the fixed enlargement of the actual bad set. If both
endpoints avoided that enlargement, the interpolation could not meet a
bad value. Changed edges contribute no such points. Hence the forced-odd
count and the corresponding conditional bad-offset count grow by only
a fixed factor. They must be charged to the enlarged bad set, not only
to coarse endpoints that were already bad before enlargement.

## 5. Probability scope

For a genuine raw coordinate, the physical row remains

`rho+D p_(H(r)-U)(theta)`.

Its monotonicity determines `U` at most once when `theta` and the desired
physical row are fixed. For two coordinates on one common nonconstant
fold branch, their index difference is fixed, and the approximation
`p_i=alpha i+O(1)` still gives the stretch interval used by the proposed
triangle estimate. Inserting a bounded number of anchors changes that
error by only a constant.

An arbitrary pair of different fold branches, or a pair involving a
fixed anchor value, does not automatically have the same stretch
anti-concentration. Those cases require their own argument. The present
result supplies anchor coverage and occupied interpolation; it does
not assert a complete capped six-point estimate or solve the residual
constraints.
