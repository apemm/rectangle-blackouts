# Menus with squarefree discriminants, and the scope of the menu sweeps

14 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: two short items that close the STATUS line of consolidated_board_menu.md, up to one audit of Lemma SQ.
- Lemma SQ: for every m there is a menu U of m odd u, containing 1, with every 4u^2 + 1 squarefree and the numbers 4u^2 + 1 independent modulo squares. So Corollary M-infinity needs Theorem N_menu only at menus whose discriminants are squarefree, and STATUS (ii) of the menu board (u with 4u^2 + 1 not squarefree, such as u = 9) is not needed.
- Scope check: the three sweeps at stride 4u cover every note that consolidated_board_v4.md cites as an input. This closes STATUS (i).

Audited in audit_squarefree_menus.md (correct with fixable gaps, all minor; fixes applied below). NOT PROVED: m_h = O(h^2).

# Lemma SQ

## Statement

LEMMA SQ. Let P be a finite set of primes. There is an odd u >= 1 such that 4u^2 + 1 is squarefree and has a prime factor q not in P.

COROLLARY. For every m >= 1 there is a menu U = {u_1 = 1, u_2, ..., u_m} of odd u with every Delta_u = 4u^2 + 1 squarefree and the Delta_u multiplicatively independent modulo squares.

## Proof

Fix a prime q with q = 1 (mod 4) and q not in P. Such q exist: every prime factor of 4(N!)^2 + 1 is = 1 (mod 4) and exceeds N. Since -1 is a square modulo q and 2 is invertible, there is r with 4r^2 + 1 = 0 (mod q). The derivative 8r is a unit modulo q (q is odd, and r is not 0 because 4 * 0 + 1 = 1), so by Hensel's lemma r lifts to exactly one root r' of 4x^2 + 1 modulo q^2. Choose a residue c modulo 2q^2 with c odd, c = r (mod q) and c != r' (mod q^2). Every u = c (mod 2q^2) then has u odd and q exactly dividing 4u^2 + 1. Since u is odd, 4u^2 + 1 = 5 (mod 8), so 2 does not divide it.

Let A(X) be the set of u <= X with u = c (mod 2q^2). Then |A(X)| >= X/(2q^2) - 1. A number u in A(X) fails to give a squarefree 4u^2 + 1 only if l^2 divides 4u^2 + 1 for some prime l other than 2 and q. Such an l satisfies l^2 <= 4X^2 + 1, so l <= 3X. For an odd prime l, the congruence 4x^2 + 1 = 0 (mod l^2) has at most two solutions, because the unit group modulo l^2 is cyclic and -1/4 has at most two square roots there. By the Chinese remainder theorem the u in A(X) with l^2 | 4u^2 + 1 lie in at most two classes modulo 2q^2 l^2, so there are at most 2(X/(2q^2 l^2) + 1) of them. Summing over primes l with 3 <= l <= 3X and l != q:

  #{u in A(X) : 4u^2 + 1 not squarefree} <= (X/q^2) * sum over odd primes l of 1/l^2 + 2 pi(3X) <= 0.2023 X/q^2 + O(X/log X).

Here the sum of 1/p^2 over all primes is 0.4522..., so the sum over odd primes is below 0.2023. Hence at least (1/2 - 0.2023) X/q^2 - O(X/log X) > 0 elements of A(X) have 4u^2 + 1 squarefree once X is large. Any such u proves the lemma, with the prime factor q.

Corollary. Start with u_1 = 1 (Delta = 5). Given u_1, ..., u_k, apply the lemma with P the set of primes dividing Delta_(u_1) ... Delta_(u_k). The new Delta_(u_(k+1)) is squarefree and divisible exactly once by a prime q that divides no earlier Delta. A product over a nonempty subset of the Delta_(u_j) is a square only if each prime occurs to an even power; if the subset contains u_(k+1), the prime q occurs exactly once, and otherwise the induction hypothesis applies. So the family stays independent modulo squares.

## Explicit menus

A greedy search over odd u (sanity script, under a second) gives the menu 1, 3, 5, 7, 11, 13, 15, 17, 21, 23, 25, 27, with Delta = 5, 37, 101, 197, 5 * 97, 677, 17 * 53, 13 * 89, 5 * 353, 29 * 73, 41 * 61, 2917: all squarefree and independent modulo squares. The non-squarefree values skipped below 27 are u = 9 (325 = 5^2 * 13) and u = 19 (1445 = 5 * 17^2). So explicit squarefree menus exist for every m <= 12, and Lemma SQ gives them for every m.

## Consequence for Corollary M-infinity

For eps > 0, choose m with x_m < x_inf + eps (stride_menu_heavy_count.md Theorem X, audited), and take a squarefree menu U of size m containing 1 from the Corollary. Theorem N_menu at U gives m_h <= C_U h^2 (log h)^(x_m) (loglog h)^C, which is at most C_eps h^2 (log h)^(1.3108172 + eps). This uses (M4) to (M9) at every odd u of the chosen menu; the sweeps and transfer notes state them for general odd u >= 3, and the thin margins are proved for every odd u (audit_menu_m10.md). So Corollary M-infinity uses Theorem N_menu only at squarefree menus, which is the case STATUS (ii) of consolidated_board_menu.md leaves untouched.

# Scope of the three sweeps (STATUS (i))

consolidated_board_v4.md cites 30 notes in its A-list (section 2). Each is in the scope of one of the three sweeps at stride 4u:
- audit_menu_sweep_core.md: stride_menu, sea_row3_split, deep_layer_sawtooth, deep_layer_bh16, saw_residual_families, three_label_one_filler, low_rows_row3_types, audit_constant_lists, consolidated_board, consolidated_board_v2.
- audit_menu_sweep_cross.md: threshold_families_random_prime, mixed_quadruples_blocks, v3_and_cross_block, two_filler_row_lemma, point_counts_power_saving, rigid_layout_cross_block, block_sea_classification, sea_census_rigid, obstruction_table_completeness, uniformity_first_moments. Its table has its own sections for threshold_families_random_prime (item 1) and two_filler_row_lemma (item 4).
- audit_menu_sweep_classes.md: ratio_graph_r_iv, additive_class_split, truncated_additive_split, degree_capped_colouring, heavy_light_split, heavy_diagonals_sharp, polylog_relocation_diluted, ap_hypothesis_henriot, full_layout_junctions, block_layout_n1, t1_cost_decomposition.

The remaining inputs of (M1) are stride-free:
- the paper's P1 to P3;
- the T1 chain, which enters through Theorems D, E and N1 (stride-free by audit_menu_sweep_classes.md), through the row-defined set S (menu (B0); audit_menu_m9_b.md E5), and through cells D2 (A*, closure part B) and D3 (absent at u >= 3).
- V3-1 to V3-5, V4-1 and V4-2 are not stride-free: their stride-4u forms are S-3, S-5, S-7, the window count and the width arithmetic of the menu board, which rest on (M7), (M8) and (M10).

The inputs (M2) to (M8) are the stride notes themselves, each written at stride 4u and audited.

The stride-4u forms that audit_menu_sweep_core.md left undecided rest on notes in the other two scopes or on audited stride notes:
- two_filler Proposition 4, v3 Theorems B and C, and threshold Proposition 1(c): audit_menu_sweep_cross.md;
- FF(u), FF'(u) and Lemma IV(u): stride_transfer_ratio.md and stride_menu_closure.md part A, both audited;
- the A4 shape counts: stride_shape_counts.md, audited.

So the three scopes cover the 30 A-list notes (31 notes in all: the core sweep names 10, though its text says 11). The rest of (M1) is stride-free or re-done in the menu board, and (M2) to (M8) are the audited stride notes. So STATUS (i) is closed.
