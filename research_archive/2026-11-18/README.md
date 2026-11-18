# November 18 research results

The full quadratic threshold and a structural size formula below threshold remain open. This folder contains new working notes. The drafts they cite under `papers/extremal/drafts` are not stored in the repository yet. The previously reported full-board bound in the [stride-menu draft](../../papers/extremal/drafts/upper_bound/part1_theorem.tex) still applies.

## Full-strip bounds and counting

For all sufficiently large heights and every width, \(f(h,m)\ge m+c\min(m,h^2)/(\log h)^{1/3}\). At widths \(m\ge h^2(\log h)^{(\log3)/2+\varepsilon}\), a globally valid filled board carries \(q_h-o(h^2)\) doubles. Both arguments use the deterministic stride-four chain. [Proof at every width](global_partial_size_bound.md) and [near-equality proof](global_near_equality.md)

A separate construction puts all \(q_h\) doubles in \(O_\varepsilon(h^2)\) columns and certifies every window of span \(h/(\log h)^{\sqrt3-1+\varepsilon}\). Its stride depends on the prime divisors of the diagonal. A matching lower bound gives the actual short-distance count at a single stride. A four-point mixed collision of span at most 5h/3 persists for a positive fraction of labels under every fixed menu of padded constant-row trials. [Explicit obstruction](constant_row_trial_obstruction.md). [Window theorem](multistride_constant_row_windows.md), [constant-row geometry](random_constant_row_windows.md), [quantitative divisor spacing](quantitative_divisor_window.md), and [single-stride lower bound](short_diagonal_distance_mass.md)

A modular shear reduces the true vertical-rival graph on each diagonal to a single universal distance graph of chromatic number three. The resulting double placement uses \(O(h^2)\) columns. Trying to impose the binary alignment used by the angle proofs on those same shears loses a positive proportion of the labels. [Three-color theorem](modular_shear_packing.md) and [alignment obstruction](modular_shear_binary_alignment.md)

At height 127 the finite certificate gives \(m_{127}\le498166\). All four filled windows and all three joins passed geometric replay. With \(t=m-498166\ge0\), four insertion sites give \(a_{127}(m)\ge2^t\binom{t+3}{3}\). [Board, verifier, and counting proof](capped_filled_threshold_127.md)

For \(p>200HM\) prime, one can explicitly choose a residue-line support on the \(pH\)-by-\(pM\) grid whose full size enumerator is \(Z_{H,M}(t)^p\) for \(H,M\ge4\). This gives clean filled modules for all parity labels whose difference is divisible by a sufficiently large prescribed prime. [Counting lift and its scope](prime_fiber_counting_lift.md)


## Filled boards and new construction results

At height 127 all 4,032 parity labels fit in one filled, extendible board of width 1,507,048. Thus \(f(127,m)=m+4032\) for every \(m\) at least that large. The construction also gives \(2^t\binom{t+27}{27}\) different maximum blackouts at width \(1{,}507{,}048+t\). All 27 windows passed an independent geometric replay. [Board and verification](filled_threshold_127.md)

For arbitrary heights the [separated-row tile theorem](separated_row_tiles.md) partitions all labels into fully filled, individually valid blocks of quadratic total width. They can be joined at quadratic total width while excluding every tilted triple or nonvertical mixed support contained in a single parity of rows and every horizontal mixed chord. Two-parity triples, nonhorizontal mixed supports, and vertical rivals across the joins remain open. [Proof for the joined board](hilbert_two_strip_joins.md)

The [dyadic matching proof](dyadic_matching_blocks.md) removes all tilted triangles and nonvertical mixed supports from a sparse matching block. At height 32,768 three colors suffice for every one of the 16,384 vertical-rival graphs tested. A separate lower bound proves that the mean degeneracy for a common permutation eventually grows at least as \(\log h\), so uniformly bounded degeneracy cannot certify those colorings. [Proof and computational checks](matching_core_budget.md)

Two further constructions place all labels at quadratic width while excluding vertical rivals. One uses [modular blocks for each signed gap](modular_gap_blocks.md). The other uses [a shared random set of slots and a matching](pooled_star_packing.md). The [star geometry](star_sea_reduction.md) rules out several families of sea obstructions under its alignment hypotheses. A [partition-regularity argument](affine_star_menus.md) proves that a finite menu of affine star slopes and a bounded number of bands loses a positive fraction of the leaves of a central star.

At height 13 a proof-checked exclusion of runs of 20 doubles yields \(m_{13}\ge44\). An independent unsatisfiability computation excluding runs of 14 yields \(m_{13}\ge45\). These tests allow arbitrary balanced row partitions. [Height-13 bounds and verification records](saturation_at_thirteen.md)

The [window amplification theorem](window_amplification.md) shows that one width-\(H+1\) counterexample at height \(H\ge4\) forces \(\liminf_{h\to\infty}W(h)/h\ge1+1/H\) for balanced windows. The [collar locality bound](linear_collar_locality.md) and the [prime-profile seam](descending_prime_collar.md) give two different settings where additional cells can be joined with local control.

## Vertical rivals with every label column divisible by four

[The interleaving proof](ternary_interleaving.md) reduces all row scales to three-coloring one ordinary Hilbert graph. A separate Euclidean-triple enumeration checked all 16,117,764 edges at dyadic side 4096, and all smaller dyadic sides passed too. The finite conclusion covers every height through 24,569, with the integral-distance test imposed even when the hypotenuse exceeds the strip height. [The largest check](ternary_graph_96_4096.json) gives the coloring digest and edge count. [The placement checker](check_ternary_placement.py) also tested the actual reconstructed columns at heights 4, 5, 8, 13, 27, 53, 81 and 101, including all 6,499,950 cross-role distances at height 101.

[The multiprime extension](bounded_palette_transfer.md) weakens the sufficient all-height hypothesis. Any fixed chromatic bound on the same normalized graph at \(Q=96\) would give \(O(h^2)\) width for these vertical-rival constraints. Sizes of the palette, modulus and implied width constant can be large. A second reader checked the recursive gap, terminal congruences and width sum. Bounded chromatic number remains open.

[The right-angle note](triangles_after_interleaving.md) gives a height-127 tilted rectangle whose three label corners force a presentation collision for every sea in the first placement. It proves a stride condition eliminating the whole adjacent-rank family, exhibits the rank-four obstruction at height 383, and shows how every fiber can be translated independently in \(h+1\) ways at total \(O(h^2)\) cost. Explicit translations now remove every tilted label triangle in the tested cores at heights 127, 383, 511, 769 and 1,025. [Repaired sparse cores and certificates](repaired_sparse_cores.md)

## The original bounded-choice Hilbert question

The [two-problems draft](../2026-11-15/two_problems/two_problems.tex) allows \(S,M\) to be chosen independently of side. In Problem 1 take \(S=1,M=96\), and use only offsets \(c_r\in\{0,1,2,3\}\), so the physical column is \(96r+c_r\). If offsets differ, the horizontal leg is nonzero modulo four. For odd vertical leg \(Y\), the squared norm is \(2\) or \(5\bmod8\), hence is not a square. Equal offsets reduce to the ordinary zero-offset graph, joining either ordered pair for which the original draft's norm is a square at horizontal distance \(96|r-t|\). A proper four-coloring is therefore sufficient.

At side 2048 this graph had an empty 4-core. Reverse elimination gave a four-coloring of all 4,194,304 cells. An independent Euclidean-triple enumerator and direct rank scan found 4,960,930 edges over 2,082 candidate lags, with zero monochromatic pairs. See [the certificate check](unit_stride_check_2048_96.json), [the coloring](unit_stride_2048_96.npz), and [the independent verifier](check_unit_stride.py). This is a finite answer for the clean model. Its offsets use all four residues modulo four, which motivated the separate construction above.

For the draft's \(S=32,M=3\) parameters, the exact star-elimination test left 3,205,437 vertices at side 2048. [The numerical record](star_side2048.json) reports the residual. It does not decide satisfiability at that size.

## Windows, size and counting

[The window note](windows.md) supplies a width-\(h\) construction at every odd height from five on, completing the known lower direction \(W(h)\ge h\) for all \(h\ge4\). It also checks the earlier hidden-rectangle proof, which restores the stronger lower inequality in the current threshold draft. A second reader checked the construction, and direct diagonal enumeration found no violating rectangle at any odd height from 5 through 31. The upper direction \(W(h)\le h\) remains open above the certified range.

[The finite-grid formula](finite_grid_formula.md) gives both the maximum size and its multiplicity for every finite grid by inclusion-exclusion. It agrees with direct presentation enumeration on nine small grids. Evaluating it can take exponential space and time. The structural questions about arbitrary subthreshold widths and the dominant counting component remain.

For the large-width counting problem the [residue-class spectral theorem](../2026-11-09/full_problem_push/unconditional_residue_asymptotics.md) already gives an unconditional algorithmic asymptotic. The [seven-row counterexample](../2026-11-09/full_problem_push/parity_partition_dominance_counterexample.md) rules out universal ordinary-parity dominance. A general simplification must allow a different maximizing partition.
