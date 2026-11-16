# Stopping point: quadratic-width research

15 November 2026. I paused this round after completing the immediate
certificate checks. I did not obtain an unconditional proof of
`m_h = O(h^2)`. I did not edit the paper, the ledger, or the archive
manifests in this round.

The longer dependency record is [NONSTOP_PROGRESS.md](NONSTOP_PROGRESS.md).
"Reviewed" below means that I checked the statement a second time,
mathematically or by a separate computation, not that it was refereed.

## Analytical results completed

1. **A conditional occupied scaffold with compatible ends.**
   The [constant-sea assembly](continuation_constant_sea_assembly.md)
   and [boundary-clean parameter update](continuation_boundary_clean_v_scaffold_update.md)
   keep the label accounting, full arithmetic occupancy, local
   permutations, interpolation, R2s filtering, and filled quadratic
   collars compatible. Full occupancy removes FW under the stated
   geometric hypotheses. The remaining core exclusions and the external
   positional relocation input are still conditions of the construction.

2. **Stronger arithmetic and interaction bounds.**
   The complete R2s side-owner exception set has size
   `h^(5/6+o(1))`; see the
   [small-variable count](continuation_r2s_small_u_refinement.md).
   The [linear-window proof](continuation_r2s_linear_window.md) gives
   full six-point span at most `h-1` for positive sea-one R2s supports
   under the stated locality condition, and `O(h)` for fixed low or
   reflected high seas. For the sampled scaffold, the reviewed long-six
   incidence bound is `h^(23/12+o(1))`. P-cycle counts have a power
   saving through length five. The general length-six estimate remains
   `h^(2+o(1))`. These are counts, not a theorem that repairs every event
   while preserving occupancy.

3. **Several constructive local repair mechanisms.**
   The [permutation local lemma](continuation_finite_direction_permutation_lll.md)
   handles any fixed finite direction menu with constant-size full
   permutation blocks. The
   [fixed-slope R2s theorem](continuation_r2s_fixed_side_slope_permutations.md)
   also handles the entire horizontal-side half using block side 65,
   or 33 above its shallow exception. These results retain every label
   in the placed blocks; interpolation and other collision families have
   separate requirements.

4. **A negative answer for bounded coloring of the full odd P graph.**
   The [parity-localized partition-regularity argument](continuation_odd_p_localized_partition_regularity.md)
   proves that every finite coloring of the positive odd integers has
   monochromatic distinct `u,v` with
   `u^2 + 4(v-u)^2` a square. Two source-level reviews checked the
   adaptation of Frantzikinakis, Klurman, and Moreira. This rules out a
   uniform bounded palette for that full graph. Its
   [construction transfer limits](continuation_odd_p_transfer_limits.md)
   are explicit: it does not prove a lower bound for unrestricted
   blackouts or rule out the Hilbert private-choice systems.

5. **An exact R2s coloring reduction and partial coloring theorems.**
   [Bounded palettes on the two row graphs](continuation_r2s_row_coloring_reduction.md)
   would give occupied color-product cores of total width `O(h^2)`,
   retaining every label, even if color classes have arbitrary gaps.
   Fixed low seas reduce to the positive sea-one graph with a constant
   extra palette. The
   [bounded-parameter theorem](continuation_r2s_bounded_parameter_bipartite.md)
   proves eventual bipartiteness when both the row increment and the
   smaller norm factor are bounded. The cutoffs can tend to infinity,
   nonquantitatively. Within one rational cube class of their product,
   an elementary threshold is `10^6 B^15`; for one exact product it is
   `10^6 B^9`. The general finiteness step uses Siegel's theorem.
   The separate [small-factor count](continuation_r2s_small_factor_sparsity.md)
   is `h^(1/2+o(1)) B^(5/4)`. Neither result bounds the colors of the
   complete row graph.

6. **A guarded repair that can remove long singleton P edges.**
   The [adjacent-shadow rule](continuation_adjacent_shadow_singleton_repair.md)
   replaces an interval of odd singleton row `A` by even singleton row
   `A-1`. Existing flat even plateaus supply the guard. For a bracketed
   facing-anchor bridge with a literal-good shadow row, at least `7/8`
   of the gap can be converted, up to a constant, without new width or
   lost double labels. The proof includes a genuine long-P example.
   This is a per-bridge result. Unbracketed caps, simultaneous different
   shadow values, and the altered higher-support sampling dependence
   remain outside the conclusion.

## Exact certificates and finite findings

- **Aligned quadratic K4 exclusions.** The
  [alignment note](continuation_odd_scale_alignment_prefix.md) excludes
  all odd rank-step valuations, every valuation through four, and odd
  scale factors congruent to five modulo eight, in the stated common
  quadratic family. The checks include all common outer orientations
  and signed potential bases. The remaining cases start at even
  valuation six, with the stated tournament and residue restrictions.
  A further valuation-six diagonal certificate is saved but has not
  received independent review. None of these exclusions proves general
  private-choice solvability.
- **A faster exact generator.** The
  [Hilbert rank-lag automaton](continuation_rank_lag_generator_audit.md)
  has at most 64 states per digit. Independent generation agrees on
  30 complete systems. This removes the need to scan every rank pair
  when building the finite P systems.
- **Three actual choices work in a large aligned example.** The
  [independent certificate audit](continuation_aligned_private_certificate_audit.md)
  verifies all 1,048,576 choices for side 1024, offset -2048, canonical
  orientation, stride 32. All 2,169,330 candidate events pass the
  actual integer norm check. The assignment violates 148,116 stronger
  modular constraints. The modular problem itself is unresolved;
  its solver run was interrupted at this stopping point and recorded
  as `UNKNOWN_STOPPED_AT_USER_REQUEST`. A side-512 system also has a
  verified modular certificate. These are finite P-only results.
- **Two choices do fail in one aligned candidate system.** A
  [51-edge odd cycle](continuation_aligned_m2_odd_cycle_audit.md)
  gives an independently checked contradiction at side 256, offset
  -512, with two choices. The contradiction does not rely on a solver.
  It is not a full-board or unrestricted threshold obstruction.
- **The alignment hypothesis matters.** An
  [unaligned Hilbert K4](continuation_unaligned_hilbert_k4_certificate.md)
  defeats three private choices. Thus the arbitrary-offset extension
  is false, even though the required aligned problem remains open.
- **Small row-graph cycles are completely understood locally.**
  The [seven known cyclic R2s components](continuation_r2s_closed_cyclic_components.md)
  contain 35 vertices and 35 edges in total. Independent exact neighbor
  enumeration proves they are already complete components of the
  infinite positive sea-one graph. This does not exclude a different,
  more complicated component at larger rows.

## What still blocks the quadratic theorem

1. Prove simultaneous solvability of the required P systems with a
   fixed number of actual choices, or give another placement rule.
   The stronger modular formulation is optional and may obscure the
   freedom available to actual integer choices.
2. Repair every forced singleton and cap while retaining occupancy,
   including unbracketed configurations and interactions between repairs.
   Sparse incidence counts alone do not provide this operation.
3. Exclude the remaining mixed three-cell, mixed four-cell, and short
   parked-six families for the same final filling. Changing the origin
   of a shadow row invalidates any unverified reuse of independent-parity
   sampling estimates.
4. Either prove a bounded coloring theorem for the complete R2s row graph
   or complete the alternative filtered-row/cap route. The partial
   bipartite families and finite cactus evidence do not settle it.
5. Finish the external positional-relocation dependency audit and check
   every interface using one consistent parameter choice. Conditional
   local results cannot yet be assembled into an unconditional board.

The general optimal-size formula at every width, a sharp threshold lower
bound, dominance and insertion for the counting formula, the true sea
entropy order, and the square exponent remain open. This round focused
on the quadratic construction and does not settle those other questions.

I started no further runs after stopping. I terminated the long modular
SAT run; the exact integer certificates and their separate checks are
complete. The solver scripts need the PySAT package in a folder
`local_sat_dependencies` beside them, which is not stored here.
