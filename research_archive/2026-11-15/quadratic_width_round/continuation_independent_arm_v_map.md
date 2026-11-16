# An occupied cap core with independent monotone arms

15 November 2026. Independent left and central mechanical arms replace
the two correlated reflected branches of the earlier fold. Cropping a
sublinear top window makes the two arms meet a common random near-top
anchor. The construction preserves all genuine labels outside that
crop, bounded row gaps, cap locality, and occupied spacing-four cores.

This is a conditional scaffold, not a solution of its residual systems.
The construction still requires the stated external relocation input
and avoidance of the compiled P, inserted-three, inserted-four, and
parked-six supports on the enlarged cores and anchor extensions.

## 1. Coverage before sampling

Work in one low constant-odd-sea profile, with sea row s. Its allowed
odd and even row pools are fixed residue classes in fixed intervals of
length Theta(h). Take `E=h^(23/24)`. Remove every original label incident
to a row above `h-2E`. There are O(hE) such labels. Under a relocation
factor `T(h)=h^o(1)`, their internal relocation cost is

`O(hE T(h)^2)=h^(47/24+o(1))=o(h^2)`.                (1)

Every remaining row pool still has length Theta(h). The low profile's
odd upper-half condition is unchanged. High profiles use the vertical
reflection of the whole construction.

For each parity, choose a good random anchor A from its fixed residue
class in `[h-E,h-2]`. The even anchor also satisfies that A-s is prime.
[The reviewed anchor-pool lemma](continuation_random_top_anchor_pools.md)
gives maximum atom `h^o(1)/E`. The bad-row sets, including any fixed-radius
enlargement used for interpolation, are fixed before this sampling.

Choose a fixed base row rho in the bottom of the original residue pool.
Write physical rows as `rho+D j`, with fixed D. The base need not itself
be good: its possible bad value is treated by the ordinary cap procedure.
It is common to the two arms of this parity.

Partition the retained genuine residue indices by the complementary
mechanical lists of a parameter theta_C in `[1/3,2/3]`. Independent odd
and even partitions give four Cartesian class products. They cover every
retained original label exactly once.

For each central class, continue its same mechanical sequence beyond the
genuine cutoff to A. Insert the base index zero and the anchor index when
absent. Both insertions change occurrence indices by O(1). Mark injected
indices nongenuine unless they were already genuine in that class.
Every continuation above the genuine cutoff is also nongenuine.

For its left arm, use a fresh independent mechanical parameter theta_L.
One of its occurrence lists suffices; no genuine coverage is assigned to
the left arm. Insert the same base and anchor. All its occurrences are
nongenuine. The two central complementary classes can share theta_C;
the left parameters can be sampled separately. There are only a fixed
number of class products.

## 2. The scalar V-map

Let g_C and g_L be the resulting increasing physical lists, beginning
at rho and ending at A. Extend each constantly at A after its last index.
They have gaps at most 3D and satisfy, before clamping,

`g_b(j)=rho+D alpha_b j+O(1)`, `3/2<=alpha_b<=3`,      (2)

uniformly in the anchor and mechanical parameters. Both stretch factors
have bounded density, and the two arms are independent conditional on A.
Define

`F_U(k)=g_C(k-U)` for `k>=U`,

`F_U(k)=g_L(U-k)` for `k<U`.                         (3)

The arms agree at zero because both begin at rho. Hence F_U is globally
3D-Lipschitz in its integer argument, even across the turning point.
Every nonanchor physical value has at most two preimages, one on each
strictly increasing arm.

Choose a fixed n_* bounding every possible arm length. It is Theta(h)
and independent of all sampled parameters. Take a dyadic padded side
`8n_*<=N<16n_*`, and independently sample each parity's offset from

`2n_*<=U<=N-3n_*`.                                  (4)

The interval has length Theta(h). Coordinates within n_* of either raw
boundary map to A. In particular, both endpoint corner neighborhoods
are constant at the chosen anchors.

Genuine labels occur only in the central Cartesian products at their
original physical rows. Left-arm points, upper continuation points,
injected coordinates, and all other padding are singleton objects.
They never introduce an additional genuine double label.

## 3. Caps, occupancy, and fixed-size refinements

Condition on both arm parameters and A. A fixed raw coordinate takes a
bad value for at most 2b choices of U, where b is the number of bad
physical rows. The anchor is good, so its constant plateau contributes
no bad offsets. Thus every potential bad-cap event has probability
`O(b/h)`.

Apply the same first-good-ancestor construction to every doubly bad raw
position, including padding. The root cap is good because its common
endpoint coordinate has value A. The expected selected area remains
`O(hb log h)`. Each total virtual coordinate retains the square-root
locality bound: on its own-parity caps replace it by the common endpoint
value, and leave it unchanged elsewhere. Every rank has a good option.

Prefer even at every nondouble rank when its option is good. The forced
odd set is contained in the positions with a bad raw even value, so

`|J|<=2N b_even`.                                    (5)

The first and last large corner blocks are constant at their good
anchors. Select the even option there. Constant-even anchor extensions
therefore preserve locality and provide the endpoint states used by
the reviewed guarded join.

Adjacent raw Hilbert positions change at most one coordinate. After the
V-map that coordinate changes by at most 3D. Caps preserve the same
one-coordinate property at unpermuted edges. The bounded-jump extension
in [the anchor-insertion note](continuation_mechanical_anchor_insertion.md)
therefore applies: enlarge the bad set by a fixed radius, move only
cleared genuine objects within fixed-size blocks, and use the sparse
spacing-four interpolation. Changed edges have good intermediate options.
On unchanged edges, either the constant coordinate is good or the moving
coordinate stays clear of the actual bad set.

All constants depend only on the fixed refinement parameters. This
retains occupied columns, same-parity square-root locality, nonintegral
nonhorizontal same-parity distances, and the isolated-seam qualification.
The bad-row filter is chosen using these final fixed constants, before
sampling. Its cardinality remains `h^(5/6+o(1))`.

## 4. Two prescribed nonconstant row values

For the same arm, subtracting (2) eliminates U. The argument in
[the triangle sampling lemma](continuation_mechanical_triangle_sampling.md)
gives, for fixed indices k_1,k_2 and physical targets,

`Pr(two prescribed values | A)
 <= C/[h(1+|k_1-k_2|)]`.                             (6)

For opposite arms, U lies between the two indices. Their arm distances
sum to `d=|k_1-k_2|`. Split the event according to which distance is at
least d/2. Condition on the other arm's slope. Its prescribed row allows
O(1) offsets U by (2); this includes distance zero, where the index fixes
U. For each such U, the independent long-arm slope lies in an interval
of length O(1/d). Its density is bounded. Averaging proves (6) across
the independent arms as well.

Bounded row perturbations are permitted throughout: they enlarge only
the fixed strip width and the constant number of admissible offsets.
The proof never assumes independent rounding errors. Ancestor indices
are deterministic candidates; selected-cap conditions can be discarded.

Global Lipschitz continuity implies that a physical difference at least
`ch/K` needs an index difference at least `c' h/K`. Therefore a
prescribed parked triangle with a prescribed nonzero increment delta
has probability

`C K/h^2`,                                          (7)

uniformly over any nonconstant arm pair. Summing over its divisor-many
possible increments gives `h^(-2+o(1))` for polylogarithmic K.

Fixed anchors do not satisfy (6) as nonconstant rows. Long anchor
partners are excluded because their room above is at most E=o(h/K).
[The random-anchor hub count](continuation_random_anchor_hub_six_count.md)
handles anchor hubs using their atom bound and (6).

## 5. Width accounting and remaining dependencies

There are only a fixed number of profiles and class products. Each
padded square and fixed refinement has O(h^2) columns. Their constant
number of guarded joins also has O(h^2) width. The top-window crop and
the cap-relocated labels have subquadratic internal relocation cost
under the existing external input.

After each removed genuine label is restored exactly once externally,
and every other core or padding column contains exactly one selected
point, the final count has the usual exact excess: one extra point for
each original parity pair. Adding singleton guards changes width and
black count equally.

The deterministic constant-sea classification applies to the selected
objects under its original hypotheses. Its remaining four systems must
be compiled on the complete virtual-option family, including constant
anchor extensions and every allowed refinement. Old probability bounds
are not inherited merely by changing the row map. The explicit estimate
(6), the bad-preimage bound, and separately reviewed transfer arguments
are the available inputs.

In particular, no singleton parity assignment, full parked-six repair,
or complete O(h^2) construction is asserted here. The external relocation
and guarded-join hypotheses remain separate from the scalar-map proof.

Independent review: the complete written construction passed a separate
review of genuine coverage, injected-coordinate marking, fixed sampling
ranges, common-base Lipschitz continuity, the two-preimage bound,
enlarged-bad-set interpolation, and conditional independence of the arms.
The residual avoidance and external relocation requirements remain open
inputs, as stated.
