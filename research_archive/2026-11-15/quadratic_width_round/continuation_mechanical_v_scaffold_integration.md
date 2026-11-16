# Integration of the independent-arm constant-sea scaffold

15 November 2026. The independent-arm row map preserves the occupied
constant-sea scaffold and gives subquadratic incidence bounds for every
long parked-six family. Its random near-edge anchors also retain the
prime-gap collars and the earlier genuine-source P cleanup.

These are construction ingredients and incidence estimates. They do not
give a simultaneous residual choice, an occupancy-preserving repair of
every counted support, or a proof of a quadratic width threshold.

## 1. Parameters and dependency order

Fix the permitted permutation block size and interpolation constants.
Choose the R2s bad-row superset using the resulting weak locality, then
enlarge it by the fixed interpolation radius. The reviewed row count is

`b=h^(5/6+o(1))`.

The [constant odd sea classification](continuation_constant_odd_sea_core.md)
provides at most eight rectangular residue-row pools, covering all but
O(h) original parity labels. Put those omitted labels in the external
relocation set from the outset. Work first with a low sea; high profiles
are reflected throughout.

Use the fixed choices

`E=h^(23/24)`, `L_*=h^(15/16)`,                       (1)

and let K be any fixed polylogarithmic function. Relocate every original
label incident to the top 2E row window. This costs O(hE) labels.
Sample good parity anchors in the top E window, with a prime difference
from the sea for the even anchor. The
[anchor-pool theorem](continuation_random_top_anchor_pools.md) gives
maximum atoms `h^o(1)/E`, independently of the subsequent row sampling.

The remaining class lists have length Theta(h). Partition them by
complementary central mechanical words. Use independent odd and even
parameters, and an independent left-arm parameter for each class.
Continue each central list to its anchor, but mark all extra coordinates
nongenuine. Insert the common fixed base and sampled anchor when needed.
The [V-map theorem](continuation_independent_arm_v_map.md) proves exact
coverage of the retained original labels, without a prime-in-class
assumption.

Padded square sizes and offset ranges are fixed before sampling, using
the maximum possible arm length. Sample every offset uniformly from a
fixed Theta(h)-length interval. No estimate below uses a parameter-dependent
offset range or conditions on the selected cap configuration.

## 2. Deterministic geometry and width

Each V-map is globally Lipschitz, and each nonanchor bad physical row
has at most two raw preimages. Conditional on arm parameters and anchors,
the bad-cap probability is O(b/h). The first-good-ancestor construction
therefore gives expected cap area

`O(hb log h)=h^(11/6+o(1))`.                          (2)

The selection includes bad padding positions. Its two total virtual
coordinate functions retain square-root locality and always provide
a good option. Default even preference gives

`|J|<=2N b_even`                                     (3)

for the intrinsic forced-odd coarse ranks. Fixed interpolation changes
this by only a constant factor.

The bounded-jump interpolation extension is essential here: mechanical
gaps are at most three, rather than one. Fixed-radius bad-set clearance
makes all intermediate options good on changed edges. On unchanged
edges the constant coordinate supplies occupancy, unless it is bad;
in that case the moving coordinate stays outside the actual bad set.

Only eligible genuine objects are permuted inside fixed-size blocks.
The refined core remains fully occupied. It has at most one point of
each parity per column, and only surviving original labels are doubles.
The reviewed spacing-four geometry excludes nonhorizontal same-parity
integral distances, same-parity right angles, and same-parity mixed
four-supports. Its isolated slope-one seams retain their original
nonintegral-distance and nonadjacency qualifications.

All selected rows remain in their prescribed residue and half-strip
pools and avoid the enlarged R2s bad set. Thus the constant-sea
classification and the same-row R2s exclusion still apply. This is a
deterministic transfer through locality and good rows, not through any
old probability estimate.

The endpoints have the good even anchor row. Extend each arithmetic
profile by the required O(h^2) constant-anchor region. Compile its
residual constraints together with the core, then use
[the guarded collar theorem](continuation_lipschitz_collar_graphs.md).
The near-top anchor still satisfies the two-level inequalities and its
prime gap has square greater than 2h. The adjacent-row and checkerboard
guards reach the universal row-h tail.

There are only a fixed number of profiles and central class products.
Their padded cores, refinements, arithmetic anchor extensions, and
guarded joins have total width O(h^2). The existing external relocation
input, with internal factor `T(h)^2` for `T(h)=h^o(1)`, charges

`[O(hE)+h^(11/6+o(1))] T(h)^2=o(h^2)`                 (4)

apart from its stated quadratic filled-window cost.

## 3. P incidence and genuine-source cleanup

The exceptional-source argument transfers with explicit dependencies.
A fine forced-odd source lies on an unchanged edge and has a coarse
even endpoint in the enlarged bad set. Conditional on both even-arm
parameters and anchors, this restricts the even offset to O(b) values.
Changed edges have both options good and contribute no such source.

For a nonconstant odd source, condition on every other sampled value.
Each prescribed norm height restricts the odd offset to O(1) possibilities
on each arm. Cap ancestors, local origins, and bounded physical shifts
are enumerated before sampling. The nonconstant-source contribution
therefore retains the bound `h b h^o(1)`.

A constant odd source is within E+O(1) of the strip edge. An actual
in-strip P diagonal then has horizontal gap O(sqrt(Eh)). If its target
is nonconstant, the target equation restricts its offset to O(1) values.
If both values are anchors, condition on both physical anchors and use
the divisor bound for their fixed row difference. The original boundary
count consequently becomes

`h b h^o(1)+h^(3/2+o(1)) sqrt(E)
 =h^(95/48+o(1))`.                                  (5)

This is an incidence bound for the specified default forced-odd set.
It is not a bound for arbitrary parity assignments on the virtual union.
Constant-even arithmetic guards add targets, but no new forced-odd
sources. They are included in the O(h^2) rank universe.

For a genuine odd source, its physical row is still exactly the central
occurrence value of its original label, even after a bounded rank move.
Conditional on its arm parameter, a prescribed physical row determines
its offset at most once. Every even target has a nonconstant arm formula
or a fixed anchor. Hence the averaged-divisor small-half-factor argument
still gives

`E I_A <= C h^(3/2) sqrt(A) log^4(2h)`.               (6)

Take

`A=h/[T(h)^4 log^12(2h)]`,

`B=h/[T(h)^2 log^2(2h)]`.                            (7)

The expected source count in (6), and the O(hB) original labels with
own-row gap at most B, each cost O(h^2/log^2 h) after relocation.
Mark them uniformly over the fixed allowed refinement union, and erase
only their odd points. Their even mates keep the columns occupied.

For any remaining actual P from a genuine source, its counterfactual
even mate and the total even locality imply vertical gap
`Y>=B-C sqrt(h)`. The half-factor exceeds A. Therefore its slot gap is
at least

`c sqrt(AB)=c h/[T(h)^3 log^7(2h)]=h^(1-o(1))`.       (8)

The counterfactual coordinate remains legitimate after point erasure;
the argument concerns the original geometric functions, not just the
currently selected mate.

Only after this genuine-source cleanup may a surviving double targeted
by an exceptional odd source be converted by erasing its even point.
Its odd point preserves occupancy. Already-singleton targets remain
constraints, and no object may lose both points. This order does not
solve forced singleton paths or cycles.

## 4. Every long parked-six family has a power saving

All following counts concern the original product sampling law. Fixed
cap ancestors and local refinement patterns are enumerated before
discarding their selection conditions.

For a prescribed nonconstant triangle increment delta, the V-map has
probability `CK/h^2`, on either arm or across the two independent arms.
The raw physical-divisor list therefore has expected size `h^(1+o(1))`.

The weighted partner-distance argument in
[the nonanchor six theorem](continuation_two_arm_nonanchor_six_count.md)
covers all same-parity nonconstant arm pairs and cap depths up to L_*:

`E N_same,nonanchor <= h^(1+o(1)) L_*
                         =h^(31/16+o(1))`.           (9)

An anchor cannot be a long partner, since its available upward room is
at most E, while delta is at least ch/K. For anchor hubs,
[the anchor-hub theorem](continuation_random_anchor_hub_six_count.md)
fixes the actual anchor value in the deterministic divisor list and then
applies the conditional partner sampling estimate. It gives

`E N_same,anchor <= h^(2+o(1)) L_*/E
                      =h^(95/48+o(1))`.              (10)

The large-cap exception has probability

`Pr(max selected cap side>L_*) <= Chb/L_*^2
                                  =h^(-1/24+o(1))`.  (11)

For opposite parities,
[the opposite-parity theorem](continuation_two_arm_opposite_parity_six_count.md)
uses a second-partner divisibility progression and independent parity
parameter families. It includes all cap sizes and anchor hubs:

`E N_opposite <= h^(3+o(1))/E^2=h^(13/12+o(1))`.       (12)

This proof allows coincident hub columns and does not assume their cap
selection events are independent. It multiplies only the prescribed-row
events in the original two parity parameter families.

Joint averaging of (2), (5), (6), and (9)--(12) gives parameters with
no selected cap larger than L_* and total long parked-six incidence

`N_long6 <= h^(95/48+o(1))`.                           (13)

No probability estimate is conditioned on the event in (11). Fixed
constant-anchor arithmetic extensions belong to these counts: their
points are anchor hubs or targets, while long anchor partners are
excluded geometrically.

Keeping the polynomial offset factors permits a stronger counting
window. The independently reviewed
[polynomial-window corollary](continuation_polynomial_long_six_window.md)
retunes E and L_* and gives a positive exponent saving for every span
cutoff `h^(2-kappa)` with fixed `0<kappa<1/42`. This changes the numerical
parameters in (1), rather than claiming that the fixed choices in (1)
already attain every such cutoff. Its incidence-versus-repair limitation
is the same as below.

## 5. What the integration does not prove

The four compiled residual systems are still P, mixed-parity inserted
right triangles, mixed-parity nonvertical inserted mixed-four supports,
and repeated parked triples. Shorter parked-six supports are not counted
by (13).

Even for the long family, (13) is a witness and incidence bound. A
support may use only compulsory singleton points. Relocating a genuine
label while keeping one of its points as a stub can leave that support
intact. Thus a subquadratic count does not establish an
occupancy-preserving repair, and it does not remove the fourth residual
system from the construction problem.

The full-final row-pair graph, genuine-double-only rule, residual
avoidance on anchor extensions, and external relocation/tail hypotheses
remain necessary. If those remaining obligations are met, retained and
relocated doubles partition the original parity labels. Every other
column is a singleton, so the exact black count is `m+q_h`.

No threshold, general optimum, or full quadratic construction is claimed.

Independent dependency review: the complete written integration passed
a separate review of coverage, row-pool preservation, the two distinct
P probability arguments, genuine-source sampling, cleanup order,
long-six scopes, cap-selection independence, and final label accounting.
The displayed construction remains conditional on the explicitly
retained residual-choice and external relocation requirements.
