# Quadratic-threshold research, 15 November 2026

This folder contains my round toward `m_h = O(h^2)`, which I paused on
15 November 2026. The concise summary is
[STOPPING_POINT.md](STOPPING_POINT.md).
No complete quadratic-width blackout is proved. The notes separate proved
local statements, independently reviewed reductions, finite checks, and the
remaining construction hypotheses. The external positional relocation
and the four residual core exclusions remain explicit inputs. Filled
collars for the current conditional scaffold have passed review.

## Current constructive reduction

The latest compatible parameter statement is
[the boundary-clean V update](continuation_boundary_clean_v_scaffold_update.md),
based on [the multiscale V integration](continuation_multiscale_v_integration.md).
It combines complementary bounded-gap row classes, independent outward
padding arms, and independently sampled near-boundary good anchors with
the constant-sea core. Its assembly has passed independent review.
Every original label is retained or charged to a quantified subquadratic
relocation set. Full occupancy, bounded local permutations, interpolation,
R2s exclusion, and filled quadratic collars remain compatible.

For this model, the following incidence estimates have passed review.
They do not assert an occupancy-preserving repair.

* All long six-point families, including same-parity and opposite-parity
  cases, caps, opposite padding arms, and anchor hubs, have expected count
  `h^(23/12+o(1))` under the improved offset law and anchor choice. See
  [the compatible parameter update](continuation_boundary_clean_v_scaffold_update.md)
  and the underlying
  [nonanchor count](continuation_two_arm_nonanchor_six_count.md),
  [the anchor count](continuation_random_anchor_hub_six_count.md), and
  [the opposite-parity count](continuation_two_arm_opposite_parity_six_count.md).
* [The improved polynomial window estimate](continuation_residue_cap_incidence_improvement.md)
  retains a power saving for supports of span greater than `h^(2-kappa)`,
  for every fixed `kappa < 1/21`, after retuning the parameters.
  This is an incidence estimate, not a deterministic interaction window.
* Bidirectional P templates incident to genuine central sources have
  expected count `h^(3/2+o(1))`, including the permitted noncentral target
  forms. The multiscale integration checks the two-row estimate needed
  for this transfer.
* [Height-first cycle counting](continuation_height_first_five_cycle_bound.md)
  gives expected genuine central P-cycle counts `h^(5/3+o(1))` for
  length three, `h^(11/6+o(1))` for length four, and `h^(15/8+o(1))`
  for length five. All directions and repeated raw coordinates are
  included. The complete proof has passed independent written review.
  It strengthens the earlier three- and four-cycle estimates. Its input is
  [the minimum-product tree estimate](continuation_mixed_path_tree_probability.md).
* [The full cycle-space height bound](continuation_cycle_height_cycle_space_volume.md)
  uses alternating-sum constraints between coordinate clusters. Its
  lattice-volume proof has passed independent review. For length six,
  it removes the K(2,3) loss but still yields only `h^(2+o(1))` overall.
  Three separated pairs of near-coincident edge-coordinate points form
  the remaining critical threshold pattern.
* [Hilbert cross-rank order](continuation_hilbert_cross_rank_order.md)
  proves that no nontrivial square submatrix of the inverse Hilbert rank
  has equal multisets of row and column sums. Its stable version excludes
  the exact pairwise horizontal-cancellation branch of the three-pair
  six-cycle pattern after a quantified sparse boundary deletion. Other
  norm representations remain. The complete proof passed review, and
  an independent checker verified 558,558 finite comparisons.
* [The permutation local lemma](continuation_finite_direction_permutation_lll.md)
  solves all P constraints among placed Cartesian blocks for any fixed
  palette of d directions, with block side at least `32d+1`. The proof
  has passed independent review. Growing palettes, fixed boundary lists,
  interpolation, and the other support families have separate conditions.
* [Dirty-cap path counting](continuation_growing_dirty_cap_paths.md)
  covers all lengths through `floor(sqrt(loglog h))` simultaneously.
  Paths containing a retained genuine double are anchor-free and have
  total expected incidence `h^(11/6+o(1))`. For all cap paths, including
  anchor-only cases, the alternative anchor choice `E=h^(17/18)` gives
  `h^(35/18+o(1))`. These reviewed prefix counts do not control full
  reachability or prove consistent singleton choices.
  [Explicit constant bookkeeping](continuation_loglog_dirty_path_bound.md)
  extends the nonanchor estimate through `floor(loglog(h)/72)`, with
  total expected incidence `h^(15/8+o(1))`. Its written proof has
  independent review. This remains a prefix incidence bound.

[The residue restriction](continuation_cap_boundary_residue_offsets.md)
makes every cap node of side at least `L=O(b)` good, where
`b=h^(5/6+o(1))`. It preserves at least half the offsets in each parity,
so every old nonnegative expectation grows by at most a fixed factor.
Every selected cap now has side at most L. With anchor window `E=h^(11/12)`,
the sampled top crop costs `h^(23/12+o(1))` labels. Keeping a dirty-child
witness improves all cap-incident P to `h^(15/8+o(1))` or less, and
covers the initial intrinsic odd stubs. See
[the dirty-child estimate](continuation_dirty_child_cap_p_incidence.md).
These statements retain the original singleton filling. The optional
[boundary-clean movable-cap menu](continuation_boundary_clean_movable_caps.md)
has separately reviewed geometry, area, long-six, cap-P, and
[bidirectional-P transfers](continuation_corner_menu_bidirectional_p.md).
Its actual choice and repair theorem remains open. Older parameter
choices remain valid separate results.

The principal open step is a choice or repair theorem that preserves
every occupied column. A sparse incidence set does not establish it.
Forced singleton paths, longer P systems, all-inserted three- and
four-point supports, and shorter six-point supports remain. In particular,
[the opposite-cap cost calculation](continuation_opposite_cap_cost_boundary.md)
only gives `h^(2+o(1))` weighted repair cost. Its bad boundary strip is in
the current point's coordinate, not the opposite coordinate.

### Good-row arithmetic and forced intervals

[The multiplicative good-row theorem](continuation_multiplicative_r2s_good_rows.md)
proves that a positive sea distance with no prime factor `1 mod4`
cannot support a positive-offset R2s collision. Adding the congruence
`n=1 mod3` removes every negative-offset case for seas at distance at
most four from the strip edge. The proof uses a valuation descent and
the strict inequality `delta^2<2U`. It has an independent derivation.
If A is generated by primes `7 mod12`, both A and 22A are fully good
distance families. Their short-interval consequences and the fixed
row-residue restriction now have separately reviewed proofs:
[the semigroup moment bound](continuation_full_good_semigroup_gap_bounds.md)
and [the residue-class adaptation](continuation_semigroup_residue_gap_tail.md).
Each required literal R2s-good row family has gap moments of every
fixed order below `3/2`. This yields squared bad-run energy
`O(h^(4/3+eta))` for every fixed positive eta, rather than `O(h)`.

[Balanced anchor planting](continuation_balanced_good_anchor_planting.md)
puts a deterministic good family into both sampled row classes.
Disjoint local bit swaps change every prefix count by at most one,
so the fixed-width sampling strips survive. The full proof has review.
[Literal-filter separation](continuation_actual_good_anchor_separation.md)
keeps the actual R2s set for caps and anchors, while reserving its
buffer enlargement for movable-double eligibility. Boundary-clean caps
also give safe bounded-jump interpolation on unchanged edges. This
proof has review. It introduces off-cap forced fine singletons, with
a deterministic near-bad nonanchor witness. Those sources must be
included explicitly in probability estimates. No gap theorem for the
buffered filter is needed or asserted.

[Good-pair interval filling](continuation_good_pair_interval_filling.md)
retains every both-good original label and fills all removed intervals
without additional good-label deletion. The partial same-parity locality
constant grows by at most a fixed factor. The tradeoff is adaptive
endpoint provenance, for which the old sampling kernels do not apply.

[The two-corner propagation obstruction](continuation_movable_cap_p_propagation.md)
shows why movable barriers alone need not cut P implications: a long
barrier can force the entire cap to its common parity. The separate
[multi-anchor menu](continuation_multi_anchor_cap_menu.md) introduces
intermediate good rows and a reachability criterion. Its geometry and
global `O(hb)` forced-width charge have passed review. The
[two-tier threshold](continuation_two_tier_anchor_gaps.md) retains a
subpolynomial candidate menu while paying the stated variable relocation
tariff for long-gap labels. These parameter claims also passed review.
None of these fillings proves simultaneous
P avoidance or a safe erasure theorem.

[The fine-grid multi-anchor construction](continuation_fine_multi_anchor_compatibility.md)
now has independent review, including occupied interpolation and the
spacing-four exclusions. Its coordinate records have
[ancestor-face provenance](continuation_hilbert_prefix_face_menu.md), so
short-gap candidate rows belong to explicit shifted face grids.
[Target-first cap-pair counting](continuation_rank_dependent_cap_p_pairs.md)
allows rank-dependent coordinate pairs and retains the
`h^(3/2+o(1))` bidirectional-P estimate for a subpolynomial menu.
The dirty-child cap-P and long-six estimates also transfer with
subpolynomial overhead. The additional forced-width charge is bounded
by the cap area and the original bad-row charge. These results complete
the geometric and counting audit of this optional menu. They do not
prove its simultaneous choice criterion.

### Earlier compatible scaffold

The current combined result is
[the constant-sea assembly](continuation_constant_sea_assembly.md), with
independent dependency review.
At most eight row pools cover all but `O(h)` parity labels. They use one
constant odd sea row and dense spacing-four cores. Folded padding supplies
prescribed prime-gap endpoint anchors; separated interpolation retains
bounded permutations of genuine good doubles. Filled collars have total
width `O(h^2)` and end at constant row h.

This settles the filler classification, occupancy, endpoint compatibility,
and collar obligations for this conditional scaffold. The four residual
core families must still be avoided simultaneously, and the stated
external relocation input must be supplied. No unconditional quadratic
threshold follows yet.

The previous H7 reduction starts with
[continuation_random_good_caps.md](continuation_random_good_caps.md),
then uses [random-offset factor cleanup](continuation_random_offset_factor_cleanup.md)
and [singleton P incidence](continuation_cap_stub_p_incidence.md).
It constructs occupied arithmetic cores with
good rows, a uniform same-parity square-root locality bound, and the exact
double-label accounting. It removes R2s and FW, subject to their cited
geometric classification and external join inputs.

There are two kinds of remaining actual P sources:

1. An explicitly bounded set of odd-only singleton ranks. They cannot be
   emptied by the odd-point erasure rule.
2. Genuine doubles whose P events have large half-factor and slot gap
   `q >= h^(1-o(1))` after the additional sparse erasures.

The refined R2s exceptional-row bound is `h^(5/6+o(1))`.
The cap construction relocates `h^(11/6+o(1))` labels. Actual P incidence
from intrinsically odd singleton sources is at most `h^(23/12+o(1))`
for a jointly selected pair of offsets. Erasing the even points of genuine
double targets and relocating those pairs leaves only their interactions
with already-even singletons in this exceptional source class.

The label-only families Lambda3 and Lambda4, and the shared-completion
family 6PT, also remain. They must be checked on the actual capped point
set, including its added singleton points. A bound on the singleton count
does not bound their incident P events or supply a valid repair.

For cap area alone, the offset choice separates into two one-dimensional
weighted bad-row sums. The combined incidence estimates require joint
averaging; separate area minimization does not prove those estimates.
Fixed-size permutations of the resulting objects
preserve the construction properties after a fixed stride adjustment.

The constant-sea assembly retains these P exponents after folded padding
and separated interpolation, as checked in its dependency audit. Its
intrinsic forced singleton paths and the three higher support families
remain open.

## Proofs supporting the reduction

* [Odd-point erasure](continuation_odd_stub_exception_repair.md) keeps the
  even point in every exceptional double column and relocates its pair.
  Rectangle collisions are monotone under this erasure, arithmetic
  occupancy survives, and relocation restores the exact excess.
* [Divisibility cleanup](continuation_divisibility_factor_cleanup.md)
  improves the exceptional-label count to
  `O(h^(7/4) A^(3/4) log(2A))`. Writing `a = u v^2` with squarefree `u`
  forces `u v | (S/2) q`. The resulting cutoff is `A = h^(1/3-o(1))`.
* [Good caps](continuation_random_good_caps.md) repair arbitrary bad row
  sets of total size `b` at a cost of `O(h b log h)` relocated labels.
  Clamping fills padding, and selected Hilbert intervals are filled at a
  good common endpoint row. The same-parity locality constant is preserved.
* [Averaged R2s divisibility](continuation_r2s_averaged_divisibility.md)
  sharpens the prior exceptional-row count by retaining the divisor sum
  before averaging. The [small-U refinement](continuation_r2s_small_u_refinement.md)
  gives the independently reviewed exponent `5/6`.
* The H7 dependency audit
  checks the point-level classification for occupied singleton/double cores.
  It justifies the reduction to P, Lambda3, Lambda4, and 6PT under the
  stated external relocation and collar inputs.
* [Virtual cap palettes](continuation_virtual_cap_palettes.md) provide two
  good-row options except at a sparse forced set, with uniform locality.
  [Movable barriers](continuation_movable_forced_barriers.md) further shrink
  the forced set and give a weighted direct-edge hitting criterion.
  Its hypothesis and the exclusion of longer forced paths remain open.

The cap algorithm has an independent exact finite checker:
[check_random_good_caps.py](check_random_good_caps.py), with
[saved output](check_random_good_caps.json). It passed 30 arbitrary-good-set
cases and 678,909 locality comparisons, including the cap-area inequality,
occupancy, odd-only count, and excess accounting. It does not test complete
blackout validity.

## Other positive results from this round

* [Equal-height P two-cycles](continuation_equal_height_p_two_cycles.md),
  with separate review,
  involve at most `h^(3/2+o(1))` genuine endpoints for suitable offsets.
  Unequal hypotenuses and the remaining singleton choices are not covered.
* [The partner-first six-point reduction](continuation_partner_first_six_reduction.md)
  removes the maximal-divisor factor from the raw same-parity expectation.
  Its bound is still quadratic, `O(h^2 K^(5/2))`, for sea offsets bounded
  by `K`. It also proves uniqueness of the increment on a fixed final
  isolated-jump mesh. That deterministic statement gives no extra random
  offset probability.
* [The Hilbert carry automaton](continuation_hilbert_affine_carry_automaton.md),
  with independent review,
  gives exact sublinear row-intersection bounds for several slopes.
  Slope five has a linear-sized exceptional row, but an averaged exponent
  `log_2(56)/3 < 2`. The joint progression/energy estimate remains open.
* [Raw dyadic boundaries](continuation_raw_six_grid_boundary_count.md)
  contribute `h^(7/4+o(1))` expected long same-parity six-point witnesses
  at dyadic side `h^(3/4)`. This partitions the count; it does not add a
  physical bad-row deletion to the cap construction.

* [Constant-odd-sea cores](continuation_constant_odd_sea_core.md) recover the
  four-family classification without the additional parked triangles of
  the two-low-row profiles.
* [Folded anchors](continuation_folded_anchor_caps.md) preserve all genuine
  labels while fixing both endpoint even rows. They retain the cap-area
  and exceptional-source incidence bounds.
* [Permutation interpolation](continuation_permuted_step_four_interpolation.md)
  preserves occupancy, good options, and same-parity exclusions at dense
  spacing four, with constants independent of height.
* [Lipschitz collar backgrounds](continuation_lipschitz_collar_graphs.md)
  give the complete guarded quadratic-width join under the enlarged core
  residual hypotheses. The independent geometric checker passed 11,279
  complete 1-Lipschitz graphs; those are finite checks of the background
  lemmas, not complete blackout computations.

* [Hole-free orders](continuation_hole_free_rectangles_and_triangles.md)
  give uniform locality for arbitrary near-square rectangles and diagonal
  triangles, including bounded-gap filtered row lists.
* [The occupied triangular scaffold](continuation_common_index_occupied_scaffold.md)
  removes all short P gaps through `h^(1/2-o(1))` within the quadratic
  relocation budget. It remains a useful separate construction.
* [Sixteen-slot local repair](continuation_sixteen_block_local_repair.md)
  solves the stated internal P systems. Its H7 version has the explicitly
  limited residue scope in that note. It does not solve cross-tile P.
* [Role-sensitive Hall extension](continuation_role_sensitive_hall_extension.md)
  gives sufficient type budgets, including prescribed placements. No
  global ordering meeting those budgets has been proved.
* [The long-P tile-pair bound](continuation_long_p_tile_pair_bound.md)
  limits sufficiently long interactions to two vectors per role between
  fixed-size physical tiles. It does not bound the number of neighboring
  tiles.
* [Random physical-pack partitions](continuation_random_pack_partitions.md)
  preserve locality and give a spacing anti-concentration estimate. A
  joint constraint estimate is still needed.

## Audited obstructions and their scope

* [Fixed-direction private slots](continuation_single_direction_p_matching.md)
  reduce to an exact path-matching criterion, but a path example defeats
  every fixed private-slot count. A separate
  [three-direction cycle](continuation_three_direction_p_cycle.md) uses
  long P edges and distinct labels. Neither is an actual Hilbert embedding,
  so the Hilbert choice problem remains open.
* [Ambient band embeddings](continuation_ambient_band_embedding.md)
  can acquire a P rival after an arbitrarily small fixed-factor height
  expansion. Recursive treatment of small own gaps needs an ambient-safe
  invariant, not just validity in a smaller strip.

* [Repeated even-row six-supports](continuation_repeated_even_row_six.md)
  obstruct fixed local repetition in the two-low-row profiles. A finite
  profile menu cannot remove every fixed set of such gaps, by CRT. This
  is why the assembled candidate uses one constant sea row instead.
* [Constant-repeat staircase collars](continuation_constant_sea_staircase_obstruction.md)
  fail at every plateau length. The successful guarded collar uses
  prime-gap and Lipschitz backgrounds with separate overlap checks.

* [Odd-P partition regularity](continuation_odd_p_localized_partition_regularity.md),
  with independent source audit:
  every finite coloring of the positive odd integers has monochromatic
  `u < v` with `u^2 + 4(v-u)^2` a square. Thus the full odd P graph has
  unbounded chromatic number. This is a new parity-localized adaptation
  of published concentration and correlation theorems, independently
  reviewed but not refereed. It gives neither a quantitative height bound
  nor a lower bound on the general blackout threshold.

* [Four-slot obstruction](continuation_four_block_obstruction.md): a
  genuine P rival survives every permutation of an explicit full 2-by-2
  tile. Four slots do not suffice uniformly.
* [Two-anchor obstruction](continuation_residual_two_anchor_obstruction.md):
  individually extendable boundary choices need not extend jointly,
  even after the earlier multiple-leg deletion.
* [Two-parity extension obstruction](continuation_two_parity_extension_obstruction.md):
  sparse bad-row cardinality alone does not permit a uniform locality
  repair while retaining every original good point. Good caps avoid this
  hypothesis by relocating a quantified set of additional good labels.
* [Translated-patch density](continuation_translated_patch_density.md),
  [recursive embedding](continuation_dense_patch_recursive_embedding.md),
  and [sparse-filter transfer](continuation_sparse_filter_density_transfer.md)
  show that some admissible deterministic layouts have logarithmic
  potential P degeneracy. This rules out a universal constant-degree
  argument for those layouts. It does not prove permutation
  unsatisfiability, and it does not cover positive-density random
  partitions.

The [long-support anchor theorem](continuation_long_support_local_anchors.md)
gives close cross-parity pairs for long Lambda3 and Lambda4 supports.
For 6PT, the nearby core points can have the same parity when the sea
offsets differ. Explicit supports of span `Theta(h^2)` show why locality
alone cannot give a smaller universal interaction window.
[Hilbert row-visit energy](continuation_hilbert_row_visit_energy.md) bounds
long 6PT with four raw-coordinate endpoints and opposite-parity pairs by
`h^(3/2+o(1))` in expectation. Cap-constant points and same-parity pairs
are outside that result.

The additional private-slot filler obstruction notes distinguish a
long-gap counterexample from survival of the entire small-factor endpoint
deletion rule. The latter is not proved merely by making the displayed
edge's own factor large.

## Work still needed

Three further reviewed limitations guide the current placement work.
[All-direction permutation loads](continuation_all_direction_permutation_loads.md)
give an exact sufficient local-lemma criterion, but fixed singleton
stubs can defeat every permutation of a fixed Cartesian block even
when their protected conflict graph is a matching.
[The endpoint obstruction](continuation_hilbert_endpoint_p_obstruction.md)
shows that hierarchical orientations alone cannot remove every P pair
from a protected Hilbert square. Its stated affine examples also survive
sparse literal filters and clean caps.
[The raw deletion obstruction](continuation_raw_p_deletion_obstruction.md)
shows that a power-saving expected deletion budget cannot remove all
initial P edges in the specified phase-augmented sampling model.
None of these is a lower bound for the general threshold.

The next placement freedom under investigation is a varying column
clock. Pauses of length proportional to the side of a dyadic Hilbert
node have total width `O(h^2)` over all nodes. However, the reviewed
[cut-pause obstruction](continuation_pause_cut_obstruction.md) defeats
every pause length if the guard repeats only its endpoint row options.
Simultaneous interior changes or additional guard rows are still open.

The original private-choice problem has two further positive results.
Complete offset verification
proves internal certified three-choice solvability for Hilbert tiles of
sides 4, 8, and 16 at stride 32, for every integer row offset. The
independent side-16 check covers 215,640 nonempty offsets and 4,290,580
constraints. [Weighted peeling](continuation_private_tile_gain_core_structure.md)
handles every side-4 and side-8 system, and every side-16 system except
six cores. A compact certificate records only their 198 colors. Its
independent search-free checker extends them and verifies every event.
This is a finite computational theorem, not an all-size statement.
[Larger offset-window checks](continuation_larger_private_tile_windows.md)
also pass at sides 32 and 64. Their independent search-free verification
covers 20,202 offsets and 10,987,571 constraints. These are finite windows.
[The large-offset Beatty theorem](continuation_large_offset_beatty_solvability.md)
gives an analytic infinite regime: for sufficiently large side s,
`|2T+1|-2(s-1) >= (3s^2-1)^2/4` implies certified three-choice
solvability. Its exact square-root gap classes and simultaneous phase
argument have passed two independent reviews. The proof uses only the
coordinate range and rank count, and therefore applies to any ordering
of the tile. Neither result supplies the private slots' occupied filler
or solves the interacting large canonical pieces.

[The larger-palette extension](continuation_palette_size_thin_regime.md)
proves the sufficient cutoff `Y_min >= (M s^2-1)^2/(M-1)^2`
for fixed dyadic stride and fixed `M >= 3`. A sufficiently large fixed
palette therefore handles every fixed coefficient above `1/2` in
`|T|/s^4`. [Quantitative phase bounds](continuation_approximate_gap_menu_beatty.md)
also permit a factor menu growing through `loglog s`, under the explicit
odd-normalized-multiplier hypothesis. Both proofs have independent
review. Actual arbitrary-order
[four-label](continuation_arbitrary_order_four_label_obstruction.md) and
[five-label](continuation_arbitrary_order_five_label_obstruction.md)
collisions prevent unrestricted extensions of these arguments. Their
embedding into canonical Hilbert orders is a separate question.

That distinction is now necessary. An
[exact unaligned Hilbert K4](continuation_unaligned_hilbert_k4_certificate.md)
defeats every three-choice assignment at side 8192 and one explicit
integer offset. Its four labels, all six norms, all 81 assignments,
and owner presentations have independent verification. Its offset is
not aligned, so it does not refute the four canonical systems per scale.
[Hilbert rank congruences](continuation_hilbert_quadratic_clique_exclusions.md)
exclude the earlier displayed arbitrary-order templates. The stronger
[aligned dyadic K4 exclusion](continuation_aligned_dyadic_quadratic_k4_exclusion.md)
covers all rank-step valuations and all tournament orientations when the
quadratic coordinate scale is a power of two. Its finite-state proof and
complete state certificate passed independent review. The
[odd-scale alignment extension](continuation_odd_scale_alignment_prefix.md)
also excludes every odd scale factor at step valuations 0 through 4,
every odd step valuation, and every odd scale factor congruent to 5
modulo 8. Its signed terminal checks include every common outer
orientation. The remaining common quadratic family has even step
valuation at least 6 and odd scale factor congruent to 1, 3, or 7
modulo 8. General non-clique obstructions remain open.

The rank-lag digit automaton
enumerates exact Hilbert rank pairs with at most 64 states per digit.
Its independent audit agrees on 30 complete systems. This enabled
search-free checks of two larger private-choice certificates:
side 512 at offset -1024 is certified modular-three-solvable; side 1024
at offset -2048 is integer-three-solvable, with every one of 2,169,330
candidate events checked after extending to all 1,048,576 labels.
The latter assignment violates 148,116 modular constraints, demonstrating
the extra restriction in that sufficient model. The modular side-1024
solver run was stopped without a conclusion. An independently checked
51-edge odd cycle excludes
two integer choices in one smaller aligned candidate system. These are
finite P-only statements, not complete-board results.

For filler repair, the reviewed
[guarded third-row move](continuation_third_row_p_repair.md) removes a
single incoming norm fiber while preserving occupancy and label counts.
[The growing-palette analysis](continuation_growing_row_palette_obstruction.md)
also gives two positive estimates. One long-gap fiber forbids at most
two profile rows in a sufficiently short interval. A fixed direction
`(u,v)` forbids at most `2K/|v|+O(sqrt(K))` choices in a K-row palette,
under the stated square-root source locality. The same note gives a
fully occupied two-direction obstruction to uniform availability from
locality alone. Actual source provenance or coupled changes are needed.

The actual slow interpolation now supplies such a positive provenance
result for two directions. [The slow-palette theorem](continuation_two_direction_slow_palette.md)
leaves at least `K/40-40` norm-safe choices against directions `(4,3)`
and `(12,5)`, uniformly in the compatible cap choices. For `K >= 6400`,
at least `K/160` choices are literal-good except at `O(b+K)` window
starts. An already selected opposite-parity guard permits a real
singleton retuning. Guard creation and the other directions remain open.
[The residue-cover extension](continuation_residue_cover_slow_palette.md)
gives a positive criterion for fixed direction menus and an exact slow
background obstruction when that criterion vanishes. Four directions
already supply such an obstruction. These proofs have independent review.

A return to constant shallow fillers also fails uniformly:
[the mixed-support template](continuation_even_slot_filler_mixed_obstruction.md)
uses one same-parity deep label point and three prescribed sea/filler
points. Its scope requires those arithmetic slots to be unused.
It does not exclude placement that deliberately occupies those slots,
or a varying filler rule.

The [complete row-two one-label classification](continuation_row_two_filler_one_label_classification.md)
identifies the exact remaining mixed family and the shallow exception.
Its written proof and finite presentation checks have independent review.
The adaptive fixed-even-palette obstruction in the preceding note also
allows genuine source doubles separated by more than h columns.

For the constant sea, the
[R2s linear-window theorem](continuation_r2s_linear_window.md) proves that
every crossed R2s support has full six-point span at most h-1 for sea
row one, under the stated same-parity locality condition. Fixed low or
reflected high seas have an O(h) window with a sea-dependent constant.
The [short-distance theorem](continuation_r2s_short_distance_exclusion.md)
also gives a sharp cubic lower bound on core-column separation, so
fixed-width bulk permutation blocks have no internal R2s supports.
Both proofs have independent review.

[Fixed-side-slope permutation avoidance](continuation_r2s_fixed_side_slope_permutations.md)
gives explicit constant resource loads for a finite slope menu. It also
classifies and handles the entire horizontal-side half without a finite
slope assumption: only one disjoint infinite row-pair family and one
shallow exception survive. Cartesian block side 65 suffices for that
whole family, or side 33 above the exception. This retains full occupancy
and every label at the placed block points. Interpolation and the other
support families remain separate. The steeper-side row-pair graph is
under investigation as a possible bounded-coloring replacement for
bad-row deletion.

The [row-coloring reduction](continuation_r2s_row_coloring_reduction.md)
now gives the exact implication: bounded palettes on the two row graphs
produce occupied color-product cores in O(h^2) total width, retaining
every original label. Color classes may have arbitrary gaps. This uses
endpoint interval filling and still creates singletons, so it does not
remove their P obligations. The row-one graph has explicit triangles and
outdegree-six vertices. Enumeration through row distance 262144 finds
degeneracy two, but no uniform coloring theorem is proved. Fixed low
seas reduce to translated copies of this graph plus a constant periodic
palette for negative offsets. This extension has independent review.

An analytic restriction on replication is also available:
[a common cubic row family](continuation_r2s_cubic_row_family.md) with
fixed offsets and polynomial support witnesses is bipartite, with every
edge crossing one common threshold. It cannot contain an increasing
path of length two. The corrected depressed-cubic proof has independent
review. Arbitrary integral supports, nonpolynomial recurrences, and
height-dependent offsets are outside this theorem.

The [bounded-parameter theorem](continuation_r2s_bounded_parameter_bipartite.md)
extends this restriction to arbitrary integral witnesses. For every
fixed bound on the row increment and the smaller factor, the row graph
is bipartite above a finite threshold. Siegel's theorem supplies the
finiteness step. The cutoffs can grow with height, but their growth is
not quantified for the full parameter union. Within one rational cube
class of factor-times-increment, an elementary proof gives the explicit
threshold 10^6 B^15; for one exact product it gives 10^6 B^9. Both the
arithmetic and the construction transfer have independent review.

The [unit-factor family](continuation_r2s_unit_factor_structure.md)
has an exact two-parameter description. It contains compatible
increasing two-edge paths and repeated incoming targets, so neither
property can prove that family is a forest. Its global coloring remains
open.

The [adjacent shadow repair](continuation_adjacent_shadow_singleton_repair.md)
gives a guarded occupancy-preserving move for odd-only singleton gaps.
Existing flat even plateaus permit replacing a central interval of odd
row A by even row A-1. A bracketed facing-anchor bridge permits conversion
of at least 7/8 of its gap, up to a constant. The strengthened guard can
remove long P edges and has independent review. Literal goodness,
bracketing, interactions between separate repairs, and the changed
provenance of higher-support events remain explicit requirements.

Arbitrary local repairs still need boundary hypotheses. An
[actual Hilbert domino obstruction](continuation_r2s_hilbert_domino_obstruction.md)
survives all pair swaps in a full profile. The broader
[stride and permutation reduction](continuation_r2s_stride_and_permutation_reduction.md)
provides both a fixed-boundary obstruction and an exact forbidden-row
matching criterion. These statements have independent review and do not
exclude a global coupled construction.

The immediate targets are a repair for P incident to odd-only singleton
sources, uniform solvability of the remaining long-P systems, and control
of Lambda3, Lambda4, and 6PT for the actual filled cores. Any completed
construction also needs a final dependency audit of the cited relocation
and collar inputs. No result in this folder settles the exact optimal
blackout size or its counting formula for all grids.

All files in this folder are research material. The paper, the ledger, and
the archive manifests are unchanged by this round.
