# The consolidated board for a menu of strides

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: Theorem N_menu. For every fixed finite menu U of odd u that contains 1, with every 4u^2 + 1 squarefree and the numbers 4u^2 + 1 independent modulo squares, m_h <= C_U h^2 (log h)^(x_|U|) (loglog h)^C, and so m_h <= C_eps h^2 (log h)^(1.3108172 + eps) for every eps > 0. The audits this note labels A* are audit_stride_shape_counts.md, audit_stride_menu_closure_a.md and audit_stride_menu_closure_b.md. (M9), the stride-4u cells first transferred verbatim, is now re-derived at stride 4u by a second reader (audit_menu_m9_a.md, audit_menu_m9_b.md). (M10), the one-line new steps of this note, is audited (audit_menu_m10.md). (M11), the K2/K4 constant sweep at stride 4u that audit_consolidated_board_menu_trace.md asked for, found no failing step (audit_menu_sweep_core.md, audit_menu_sweep_cross.md, audit_menu_sweep_classes.md). The STATUS line after (M11) records how squarefree_menus.md closes the two items the patch left open; that note is audited in audit_squarefree_menus.md, and the final trace is audit_consolidated_board_menu_final_trace.md. NOT PROVED: m_h = O(h^2).

# Result

## Status

partial

## Summary

consolidated_board_menu: for every fixed finite menu U of odd u that contains 1, with every 4u^2 + 1 squarefree and independent modulo squares, m_h <= C_U h^2 (log h)^(x_|U|) (loglog h)^C. Corollary: m_h <= C_eps h^2 (log h)^(1.3108172 + eps). Every input is now audited: (M9) by audit_menu_m9_a.md and audit_menu_m9_b.md, (M10) by audit_menu_m10.md, and the K2/K4 sweep (M11) by audit_menu_sweep_core.md, audit_menu_sweep_cross.md and audit_menu_sweep_classes.md. None of the six found a failing step. Every fix from them, from audit_consolidated_board_menu_trace.md and from the seven earlier audits is applied. The two items the patch left open (the sweep scopes, and u with Delta_u not squarefree) are settled in squarefree_menus.md: the scopes cover every cited note, and Lemma SQ (audited in audit_squarefree_menus.md) lets the corollary use only squarefree menus. NOT PROVED: m_h = O(h^2).

## Statements

consolidated_board_menu. 14 November 2026. Problem 001. Nothing here is in the paper. This note extends consolidated_board_v4.md (Theorem N, a single stride of 4) to a finite menu of strides 4u. Notes are in research_archive/2026-11-13.

STATUS KEY
- P: paper.
- A: audited, with the audit file named.
- A*: audited in audit_stride_shape_counts.md, audit_stride_menu_closure_a.md or audit_stride_menu_closure_b.md.
- VR: transferred verbatim by reading its inputs in a source note. No second reader re-derived it at stride 4u.
- V: verbatim at stride 4u, its inputs read in the source note. Every V cell of section 3 is re-read by a filed audit or is in (M9) [audit_consolidated_board_menu_trace.md].
- N: new in this note, not audited.
- EXT: external result.

NOTATION
- Lambda = log h and ell = loglog h.
- A menu U is a finite nonempty set of odd integers u >= 1, fixed as h grows. |U| is its size. To avoid a clash with the board width m, I never write m for the menu size.
- Delta_u = 4u^2 + 1, and Delta'_u is its squarefree part.
- P_u = max(40, 8u^2 + 4). So P_1 = 40, P_3 = 76, P_5 = 204, P_7 = 396 and P_13 = 1356.
- (IND): no product of the Delta_u over a nonempty subset of U is a square.
- beta_k(a) = ((1 + 3^(a/k))/2)^k - 1, so beta_1(a) = E(a) - 1. x_k = min over a > 0 of (beta_k(a) + 2)/(1 + a), attained at a*_k (stride_menu_heavy_count Theorem X).
- kappa_T^(u) = |D_T^(2u)| is the number of distinct |d| with 0 < |d| < n_T and (4ud)^2 + (2d + T)^2 = L^2 for some 0 < L < h. kappa_T^U = min over u in U of kappa_T^(u).
- a = a*_|U| and B = ceil(Lambda^(x_|U|)).
- L^U is the board (B0)-(B10) in the proof field. It has one chain C_u of stride 4u for each u in U. L^{1} is v4's L***U.

THEOREM N_menu (every input is A or A*; (M9), (M10) and (M11) are audited by the six reports named in (M9)-(M11); the STATUS line records how squarefree_menus.md, audited in audit_squarefree_menus.md, closes the scope check).
Let U be a menu with (IND), 1 in U and every Delta_u squarefree (so Delta'_u = Delta_u), and let h >= h0(U) := max(10^10, h_PNT^U, h_D(U), max over u in U of h_SC(u), 2 max U). Here:
- h_PNT^U is the non-explicit height from the PNT in progressions mod 4 Delta'_u, for each u in U (mod 20 at u = 1);
- h_D(U) is the height of Theorem D-weighted at kappa(U), with the ap Lemma 1-4 heights and Henriot's C0. audit_menu_sweep_classes.md finds every height in ap Lemmas 1-4, Theorem D-weighted and polylog Theorem D (D1)-(D4) stride-free, so U enters at most through kappa(U) (audit_menu_m10.md);
- h_SC(u) is the height of stride_shape_counts.md at u. Theorem M1 holds for all h >= 4, so it adds no height (audit_menu_m10.md).
Then for every m >= M, L^U truncated to columns 1..m is a valid blackout of the h x m grid with m + q_h points, where:
- M <= C_U h^2 (B + Lambda^(beta_|U|(a) + 2) B^(-a) + Lambda^2/B) ell^C1 + C |U| h^2 ell + c0 n_rel tau*(h)^2;
- n_rel = O_U(h^(2 - eps_D) + h^(11/6) log h + h^(9/5 + 2eps)), with eps_D from Theorem D and any small eps > 0.
For odd h, Proposition partial case (c) adds 4 c0 tau*(h)^2 + 6h^2 + 4 = O(h^2).
At a = a*_|U| and B = ceil(Lambda^(x_|U|)):
- m_h <= C_U h^2 (log h)^(x_|U|) (loglog h)^C1.
The bound holds for any a > 0 with exponent (beta_|U|(a) + 2)/(1 + a). So each number below is certified by a single evaluation at the stated a*, not by a minimisation:
- x_1 <= 1.4967430 (v4's theta* is the exact value 1.49674291..., so the decimal 1.4967429 is too small);
- x_2 <= 1.4295235;
- x_3 <= 1.3986921;
- x_4 <= 1.3807492;
- x_5 <= 1.3689531;
- x_6 <= 1.3605886;
- x_7 <= 1.3543412;
- x_8 <= 1.3494942;
- x_9 <= 1.3456226;
- x_10 <= 1.3424580.
Rounding down understates. For example, x_2 = 1.42952342..., so 1.4295234 is too small.
Examples:
- U = {1} is Theorem N of v4.
- U = {1, 3} (Delta = 5, 37) gives exponent 1.4295235.
- U5 = {1, 3, 5, 7, 13} (Delta = 5, 37, 101, 197, 677, all prime) gives 1.3689531.
- The light width grows like the sum over U of P_u/40 times v4's: 2.9 for {1, 3} and 51.8 for U5. The other constants (C(a, U) from Theorem M1, kappa(U) in the Bad_split term, and the |U|-dependent buffer and window terms) depend on U and are not explicit. So the gain is asymptotic only.
- Remark (N), menus without 1. audit_menu_m10.md found no assembly step that uses the u = 1 chain: the u = 1-only items, D3 [T2] and h >= 280, drop out. It did not re-read (M4)-(M9) for a dependence on 1 in U, so the theorem is stated only for menus that contain 1. Nothing is lost: the menus of Lemma SQ (squarefree_menus.md) start at u_1 = 1, and {1, 3} and U5 contain 1.

LEMMA MI (A, audit_menu_m10.md). For every k >= 1 there is a menu of size k with (IND) that contains 1.

COROLLARY M-infinity (its new steps are A, audit_menu_m10.md; it uses Theorem N_menu only at menus with every Delta_u squarefree, which exist for every size by Lemma SQ of squarefree_menus.md, audited in audit_squarefree_menus.md). For every eps > 0 there are C_eps and h_eps with m_h <= C_eps h^2 (log h)^(1.3108172 + eps) for all h >= h_eps.
- x_inf = inf over k of x_k = min over a of (1 + 3^(a/2))/(1 + a), which is at most 1.3108171966 at a = 1.5833613.
- The menu depends on eps but not on h. No statement here lets |U| grow with h.

HYPOTHESES (item | source | status | audit)
(M0) EXT. The PNT in progressions mod 4 Delta'_u (u in U) and mod 20. Jacobi reciprocity (Delta_u = 1 mod 4). Dirichlet's L(1, chi) != 0 for real nonprincipal chi, and Mertens, used inside Theorem M1. v4's (H4): Henriot's corrected Theorem 5 (MPCPS 157 (2014)), tau(n) << n^eps, and the product-form local lemma. The p-condition has density 1/4 because chi_(-4) chi_(Delta'_u) is nonprincipal.
(M1) A. All of v4's inputs (H3): P1-P3, A-1 to A-31, the T1 chain, V3-1 to V3-5, V4-1 and V4-2 | consolidated_board_v4.md | audits as listed in v4 section 2. The u = 1 chain is v4's rigid chain, with one fix: v4 (B8) [G11] reads: per-type density gcd(64, |U'|)/|U'| <= 64/|U'|, with modulus dividing lcm(32, |U'|) (closure Part B audit, issue f, as corrected by audit_consolidated_board_menu_trace.md and audit_menu_m10.md). v4's formula gcd(32, m)/m with m = |U'|/gcd(2, |U'|) equals gcd(64, |U'|)/|U'|; v4's slip is the bound 32/|U'|. The earlier form gcd(64, m)/m <= 64/|U'| is false with v4's m, first at |U'| = 128. In this note the [G11] density is always written in |U'|. Only kappa_FF's constant changes.
(M2) A. Theorem M1, the menu heavy moment: sum over T of (kappa_T^U)^a <= C(a, U) h Lambda^(beta_|U|(a)), so H^U(B/4) <= C 4^a h Lambda^(beta_|U|(a)) B^(-a). It uses (IND) | stride_menu_heavy_count.md section 1, on heavy_light Theorem 1(b) (A-5) and the Kronecker-form stride_menu Lemma 2 (audits_stride_menu_and_gamma.md) | audit_stride_menu_heavy_count.md (correct_with_fixable_gaps; fix applied: Y^2/n = (4 + 1/u^2) h^2/T^2 < 9h^2/T^2).
(M3) A. Theorem X: definition of x_k, strict decrease in k, limit x_inf | stride_menu_heavy_count.md section 4 | audit_stride_menu_heavy_count.md (values reproduced to 7 or more digits; x_7 to x_9 added).
(M4) A. The stride-4u core. It covers:
- Definition L***(u): (B2') and the twisted rule (B5');
- Lemma C (C1)-(C7), U1(a), (b), (d) and U3;
- stride_menu Lemma 4 at s = 4u, SAW Lemma 4(a), (b), and II(-1,-1) with Sigma = 0;
- threshold Proposition 1(b), (c), (d), Lemma L-adic, and BH16 A3;
- the Feo kill, the filler-vertex Foo kill, in-class ll/FF and in-class even-even M2c.
Source: stride_transfer_core.md. Audit: audit_stride_transfer_core.md (correct_with_fixable_gaps). The serious fix is applied: intra-class SLL-Pc triples exist when u | u_V, and they are parked (cells S6 and B3).
(M5) A. Theorem T(u), the cell verdicts | stride_transfer_table.md | audit_stride_transfer_table.md (correct_with_fixable_gaps). The serious fix is applied: the exponent claim of T(c) now rests on (M2) and (M3). The p-range is fixed at P_u.
(M6) A. The placement rule, G_T^(2u) and (B4), R_IV(u) and Lemma IV(u), Theorem F at r = 4u with F2(i), M0, sea_census B1 and B3 at stride 4u, and A3 | stride_transfer_ratio.md | audit_stride_transfer_ratio.md (correct_with_fixable_gaps, all minor).
(M7) A*. Theorems S1-S5, C(u) and U(u): the A4, D8, B7, D17 and D18 shape counts, the label-vertex Foo and FFo cells, and A(ii), A(iii) and Proposition F at stride 4u | stride_shape_counts.md | audit_stride_shape_counts.md (correct_with_fixable_gaps, all minor; fixes SC-1 to SC-7 applied).
(M8) A*. The closure | stride_menu_closure.md. Part A covers Theorem R4, Lemma IV(u), (B8)(u), Theorem FF(u), Lemma FF'(u), [G11], the Feo, Foo and Fee re-derivations, and D1, D2, D3, D7 and D8. Part B covers Lemma DL, the A4 identities, the D1 margins, Theorem K(u) sections 0-6, K7(u), the reconciliation and the assembly. Both audits were audit_stride_menu_closure_a.md and audit_stride_menu_closure_b.md (correct_with_fixable_gaps, all minor; fixes CA-1 to CA-7 and CB-a to CB-h applied).
(M9) A. Re-derived at stride 4u by a second reader: items (a), (b), (d), (e) and (f) in audit_menu_m9_a.md, item (c) in audit_menu_m9_b.md (both correct_with_fixable_gaps, all minor; fixes applied). Each re-derivation rests on the stride-4 audits it cites (A-7, A-13, A-21, A-28, block_sea Theorems 1 and 2, sea_row3 shift invariance, SAW Theorem 1(4'), point_counts Theorem A, N1) and on L1 (A*); those were not audited a second time. The common reason (m9_a): under (B5') slot n sits in column 4n, so the deep columns (0 mod 4) and the sea columns are those of stride 4. The stride changes only the in-class vector (4u Di, 2Di), the true rho0 and the gap, and these cells use the gap only as a lower bound.
- (a) [A, audit_menu_m9_a.md] The Table J1* seam entries and the cell E1/L3 (core audit; closure Part B audit). Under (B6) the seams see only filler columns, whose rows depend on the type and on n - rho0 (mod 4). (Phi) pads the phase, and (B5') gives the true rho0. The filler law at stride 4u in type tau is, slot for slot, the stride-4 filler law of that type for some b_tau, so every seam configuration is already a v4 configuration. Rests on A-13, A-21 and L1 (A*).
- (b) [A, audit_menu_m9_a.md] The internals of sea_row3 Theorem A, and Corollary B in detail (ratio audit; closure Part B audit). Their conditions concern single deep points and rows. The proof uses the stride in only two sentences of 2(iii); at stride 4u they are replaced by the row argument of K4(u) (sea_row3 line), and that case is empty. Rests on A-7 and block_sea Theorems 1 and 2.
- (c) [A, audit_menu_m9_b.md] The cells S0, B4, M7', M9, B8, S11, S12, S13, [V3 cross-type], [R4] and [D-4F], and the cells the trace audit found missing here: C1/L4, D9, D10, D11, E3, E4 and E5. Their inputs are rows, parity, columns mod 4, the filler rows and one-label data. They use (B5') only through rho0 = the true slot residue (u(iota + sigma) - kappa_tau) mod 4, the F2 repair: with the stride-4 formula, label slots sit at offset 2 when u = 3 (mod 4) and iota + sigma is odd, and D9 (V2-6), S12, D11 (ii-a) and SAW Theorem 1(2b), (3), (4') would lose their hypothesis. [V1] and [V2] are not separate cells: [V1] follows from A1, D5, D6 and the FFF exclusion (SAW Theorem 1(3), re-derived in m9_b), and [V2] is the union of the S and T cells. SAW Lemma 3 is removed from this list: no cell and no step of Theorem N_menu uses it (it transfers verbatim anyway). Sanity runs at u = 3, h = 1001 found 0 configurations for B8, D9, S11 and S12, with the controls firing.
- (d) [A, audit_menu_m9_a.md; second check in audit_menu_sweep_classes.md] heavy_diagonals_sharp Proposition 3(a), (b) at stride 4u (ratio audit). It holds word for word: it is a fact about any graph of maximum degree below B/2, and the only stride input is the degree bound for G_T^(2u(T))[tau]. See S-0.
- (e) [A, audit_menu_m9_a.md] The R_FF^+ bound t <= 210 (ratio audit; closure Part A audit). It is a row-only bound: n_y = Di, and fillers lie in [h - 210, h]. The 210 is tight to Table J1*, where max(h - T*) = 186. Rests on Lemma mixedeq and Table J1*.
- (f) [A, audit_menu_m9_a.md] The constants, not the orders, in the averages of Theorem U(u) (closure Part B audit). They are explicit finite constants that depend on u; for fixed u, P_u enters only in the denominator, together with the PNT o(1) terms. n_rel is insensitive to them. Rests on S1-S5 (A*) and point_counts Theorem A.
(M10) A, audit_menu_m10.md (correct_with_fixable_gaps, all minor; fixes applied). The new steps of this note: Lemma MI; step S-0; the U1(c) line (S-2); the Theorem D event line (S-3); the window count; the width arithmetic; and Corollary M-infinity. Each was derived again and holds given (M1)-(M9) and Theorem D-weighted (A-18). The assembly for a general U was checked at assembly level only (no step uses the u = 1 chain), so Theorem N_menu is stated for menus with 1 in U, and general U is a remark (N).

(M11) A. Completeness of the K2 and K4 constant lists at stride 4u (u odd, u >= 3), added at the request of audit_consolidated_board_menu_trace.md. Swept in three parts, each correct_with_fixable_gaps, all minor:
- audit_menu_sweep_core.md: 10 notes (its own text says 11), namely stride_menu, sea_row3_split, deep_layer_sawtooth, deep_layer_bh16, saw_residual_families, three_label_one_filler, low_rows_row3_types, audit_constant_lists (Lemma S1L), consolidated_board (Lemma L-adic, J1*, K1-K4) and consolidated_board_v2 (V2-1 to V2-9);
- audit_menu_sweep_cross.md: 10 notes, among them obstruction_table_completeness, mixed_quadruples_blocks, rigid_layout_cross_block, v3_and_cross_block and uniformity_first_moments;
- audit_menu_sweep_classes.md: 11 notes, among them full_layout_junctions, heavy_diagonals_sharp, heavy_light_split, additive_class_split, truncated_additive_split, ratio_graph_r_iv, polylog_relocation_diluted and ap_hypothesis_henriot.
No step that the board uses fails at stride 4u. Each changed constant holds as written or a fortiori (it enters only as a lower bound: the p range, the gap, J4, the prime counts), or holds by a re-derivation on file (core, table, ratio, shape, closure; the sweeps derived the critical ones again), or belongs to a stride-4 step that the board does not use. The lines the sweeps supply are now in section 4, K4(u).

STATUS of Theorem N_menu (14 November 2026). No hypothesis is open for audit, and no audit on file found a failing step. The two items the patch left open are settled in squarefree_menus.md:
- (i) Scope of (M11): closed. The three sweep scopes (31 notes) cover all 30 notes of the A-list of consolidated_board_v4.md. two_filler_row_lemma.md and threshold_families_random_prime.md are in the scope of audit_menu_sweep_cross.md (its items 4 and 1). The rest of (M1) is stride-free (P1-P3; the T1 chain, through Theorems D, E and N1, the row-defined set S and cells D2 and D3) or re-done in this note (S-3, S-5, S-7, the window count and the width), and (M2)-(M8) are the audited stride notes. This scope check is audited in audit_squarefree_menus.md.
- (ii) u with Delta_u not squarefree: not needed. Lemma SQ of squarefree_menus.md gives, for every m, a menu of m odd u containing 1 with every Delta_u squarefree and the Delta_u independent modulo squares. Corollary M-infinity uses Theorem N_menu only at such menus. Lemma SQ is audited in audit_squarefree_menus.md.
So Theorem N_menu holds, as far as the audits on file certify, for every menu U containing 1 with every Delta_u squarefree and independent modulo squares, such as {1, 3} and U5 = {1, 3, 5, 7, 13}. Corollary M-infinity holds on the same basis, through Lemma SQ, using (M4)-(M9) at every odd u of the chosen menu. Menus containing a u with Delta_u not squarefree are not covered. NOT PROVED: m_h = O(h^2).

The heavy-count audit left the u = 1 subset-chain claim undecided. It is now settled by the closure Part B audit (A*), through V2-1; see S-4.
(V_u) of stride_menu_heavy_count Theorem W is now (M4)-(M9) for each u.
census_stride12.md tested the untwisted rule. census_stride12_twisted.md tested the twisted L***(3) in 45 single-type runs at h = 429 to 1501 and found no unlisted family; cross-class cells are vacuous below about h = 10^4.

NOT PROVED: m_h = O(h^2), and any exponent at or below x_inf by this method. Every exponent below theta* = 1.49674291... (upper bound 1.4967430) stated here rests on the audits named in (M1)-(M11), and stays open exactly as the STATUS line says.

## Proofs

0. WHAT CHANGES FROM v4
- v4 is the case U = {1}. For the u = 1 chain, every v4 statement is used word for word, except the [G11] bound, which reads gcd(64, |U'|)/|U'| <= 64/|U'| [CB-f, audit_menu_m10.md]. v4's proofs use B only through B -> infinity polylogarithmically (K_max = B, rho = 2/B >= Lambda^(-C'), t < 16lB), so B = ceil(Lambda^(x_|U|)) in place of ceil(Lambda^theta*) changes nothing (audit_consolidated_board_menu_trace.md).
- New in L^U:
  - a chain of stride 4u for each u in U \ {1};
  - one admissible pair (l_u, p_u) per chain;
  - each light diagonal sent to its lightest stride;
  - a diagonal heavy only when it is heavy at every stride;
  - one Theorem E instance, one weighted Theorem D group and one Proposition partial instance;
  - one switch z, with every chain a separate J5' window left of z.

1. SPECIFICATION OF L^U

(B0) PARAMETERS
- h >= h0(U) = max(10^10, h_PNT^U, h_D(U), max over u in U of h_SC(u), 2 max U), as in the statement. This gives:
  - h >= 424 (SAW Theorem 1);
  - h >= 280 (two_filler Proposition 4 at u = 1);
  - h >= 148 (Proposition 4 at u >= 3, where the gap is at least 298h);
  - h >= 2u (U1 sizes).
- Lambda, ell, a = a*_|U| and B = ceil(Lambda^(x_|U|)).
- A = ceil(h/2), K = floor(h/2) and W_h = floor((h-1)^2/4) + 1.
- Labels (i, j), s = j - i, T = 2s + 1 and q_h = AK are as in v4.
- Locality: (P3).
- S and the T1-exceptional set are as in v4 (B0). They are defined by rows only, so they do not depend on the stride.

(B1) LIGHT, HEAVY, ASSIGNMENT
- T is light iff kappa_T^U < B/4. It then goes to chain C_u(T), where u(T) is the least u in U with kappa_T^(u) = kappa_T^U: the stride at which T is lightest.
- T is heavy iff kappa_T^(u) >= B/4 for every u in U.
  - Labels of S on heavy T go to the single Theorem E instance (rule 1).
  - Other heavy labels go to Proposition partial (R-d).
- u(T) is a deterministic function of T, so it is fixed before (l_u, p_u) and chi.
- Classes exist only on light diagonals, so heavy labels are never in Bad_split [Z2].

(B2) PRIMES: ONE PAIR PER CHAIN
- L_u = {l prime in (1.04h, 2.08h] : (Delta_u/l) = -1}.
- Pset_u = {p prime in (P_u h, 2 P_u h] : p = 3 (mod 4), (Delta_u/p) = -1}.
- Adm_u = L_u x Pset_u. At u = 1 this is v4's Adm: (5/l) = -1 iff l = +-2 (mod 5), and p = 3 (mod 4) with (5/p) = -1 iff p = 3 or 7 (mod 20).
- #L_u >= (1/2 - o(1)) 1.04h/log h and #Pset_u >= (1/4 - o(1)) P_u h/log h, by (M0).
- gcd(p, 16l) = 1 and gcd(u, 16l) = 1, because l > 2u.
- Chain u takes the deterministic minimiser (l_u, p_u) over Adm_u of Y^(u)(l, p) := sum over tau of sum over F in {A4-I.2, A4-II, B7, D8, D17, D18} of Y_F^(tau,u)(l, p). This is the pointwise bound of Theorem U(u). At u = 1 it is K6-v3 step 1.
- The residue conditions of different chains never interact, so no global prime is needed.
- kappa and b_tau are fixed integers (for example 0) in each chain.
- The p-range is P_u = max(40, 8u^2 + 4) in every chain [TA-2, CO-4]. stride_menu Lemma 4 at s = 4u needs only p > (8u^2 + 4)h, and v4 uses 40 at u = 1.

(B3) TYPES. In each chain there are 512 types tau = (i mod 32, s mod 16), with r0, y_P, tau_T and c_tau as in v4.

(B4) CLASSES
- For light T and type tau, chi_{T,tau} is a uniform random proper B-colouring of G_T^(2u(T))[tau]. This is stride_menu Proposition 1' at sigma = 2u(T) (A-4, valid for any even stride), restricted to the slots i = iota (mod 32).
- The colourings are independent over (T, tau).
- The degree is at most 2|D_T^(2u(T)) ∩ 32Z| <= 2 kappa_T^U < B/2. So Proposition 3(a), (b) give: G_T-independent classes, K_max = B, and P(mono) < 2/B. (Xi1)-(Xi4) hold.

(B5) PLACEMENT IN CHAIN u (the twisted rule (B5'))
- Class k of diagonal s in type tau sits at t = rho_s + 16 l_u k, with rho_s = p_u^(-1)(u s - kappa) (mod 16 l_u) and 0 <= rho_s < 16 l_u.
- Label (i, j) has slot n = u i + p_u t + b_tau. Its odd point is (4n, 2i + 1) and its even point is (4n, 2j + 2), in chain-local columns.
- Hence n = u j - kappa_tau (mod 16 l_u), with kappa_tau = kappa - b_tau. Also rho_tau = u(iota + sigma) - kappa_tau (mod 16) and rho0 = rho_tau mod 4. This is the F2 repair: the stride-4 formula gives the wrong rho0 when u = 3 (mod 4) and iota + sigma is odd.
- t < 16 l_u B.
- At u = 1 this is v4 (B5) word for word.
- Why the twist is needed. Without it, N := u Ds - DM = (u - 1)Ds (mod 16l), and the l-adic kills of A1, A3 (Proposition 1(c)), A5, S8 and Fee lose their proofs. For Fee there is an explicit witness: stride_transfer_table section 4, at h = 2 x 10^7. The table audit checked it exactly at the level of positions and rows. Fatality also needs s0 and s1 to be light and the colour event to occur [TA-8].

(B6) FILLER LAYER. This is v4 (B6) as a function of n, with rho0 from (B5).
- T*_tau >= h - 186, and the fillers lie in [h - 210, h].
- A filler at offset w lies in row y_P + 8(w + c_tau) (mod 64).
- Table J1*, (Phi) and the margins are as in v4.

(B7) DESTINATIONS. v4 (B7) rules 1-5, read per chain.
- R-a, R-b, R-c and R-d are unchanged (rows and T*_tau).
- R-e: the labels touched by an in-class R_IV(u(T)) edge with max(p, q) > h^(1/2)/32, or by an in-class R_FF^oo(u(T)) or R_FF^ee(u(T)) edge with |U'| > h^(1/2)/32.
- R-f: the counted families of chain u at (l_u, p_u): A4 (I.2, and II(1,-1) with Sigma != 0), B7, D8, D10, D11, D17 and D18.
- R-g: E_D.
- The set identity Y = (Bad_split ∩ S) \ D4 is unchanged [Z1].
- Safety: J3 in hitting-set form (V2-1, A-27), Lemma M1 monotonicity (A-16), P2, and the survival of Theorem D's hypotheses under intersection with a fixed set.

(B8) BAD_SPLIT AND THEOREM D
- In each class of chain u, Bad_split is the shallow end of every monochromatic in-class edge of:
  - R_IV(u) with max(p, q) <= h^(1/2)/32 (the q-end);
  - R_FF^oo(u) and R_FF^ee(u) with |U'| <= h^(1/2)/32, in each of the 4 filler rows;
  - R_FF^+: 0 < |Delta i| <= 210 with Delta i = 0 (mod 32), so at most 6 neighbours on each side.
- One weighted Theorem D group:
  - D = all light T, |D| <= h, rho = 2/B;
  - Q_T = the q's of R_IV(u(T)) and R_FF(u(T)), plus q = 1 for R_FF^+ with c_1 <= 12;
  - kappa = max over u in U of (kappa_IV(u) + kappa_FF(u)) + 12, which is finite;
  - Theorem D-weighted allows Q_T to depend on T (closure Part B audit).
- Densities:
  - R_IV(u): q is odd, and {q | v_f} is one class mod 32q, so the density is 1/q (Lemma IV(u), Part A audit).
  - R_FF(u): per type, gcd(64, |U'|)/|U'| <= 64/|U'|, with modulus dividing lcm(32, |U'|) [CA-4; form fixed by audit_menu_m10.md].
  - Every event is a union of O(1) classes of i mod lcm(32, q) <= 32q <= h^(1/2) (ap Lemma 4).

(B9) BUFFERS AND ENDS. Each chain C_u is a copy of v4's (B9) sequence with its own 512 regions:
- row-1 tail | Sea(1,g) | 256 row-1 types | Sea(1,g) | all-g | Sea(3,g) | 256 row-3 types | Sea(3,g) | all-g | Sea(1,g) | row-1 tail.
- Margins: 2W_h + 1 columns of pure SAW*-shift before the first and after the last label column of every region, plus at most 3 slots at each end of the region for (Phi): rule (P9) sets a phase at both ends [audit_menu_m9_a.md].

(B10) GLUING
- Outside the windows the board is beta_z: row 1 at x < z and row h at x >= z.
- The windows:
  - one window per chain, from its first Sea(1,g) to its last, in increasing order of u, all left of z;
  - the WP instance: case (a) inside the row-1 tail for even h; case (c) with switch z for odd h, with U_WP one window;
  - the 2 x 49 WD/WE blocks of Theorem N1, right of z.
- The windows are pairwise at least 2W_h + 1 columns apart. Every block equals beta_z on the 2W_h-neighbourhood of its window; for the case (c) WP block this holds on all of Z outside U_WP.
- There are at most |U| + 99 windows. J5' glues them, and the board is truncated to columns 1..m.

ORDER OF RANDOM CHOICES
1. Light, heavy and u(T) (deterministic).
2. (l_u, p_u) for each chain (deterministic minimisers).
3. chi from the product law (B4), conditioned on the Theorem D event.
4. The WE and WD centre maps, by T2's local lemma, which never uses (l, p).

2. STEPS

S-0 (A: audit_menu_m9_a.md and audit_menu_m10.md, with a second check in audit_menu_sweep_classes.md; this is (M9)(d)). heavy_diagonals_sharp Proposition 3(a), (b) holds for the uniform proper B-colouring of any graph of maximum degree d < B/2: each class is independent, and P(chi(u) = chi(v)) <= 1/(B - d). The only stride input is the degree bound, which holds because G_T^(2u)[tau] joins slots at distances in D_T^(2u) ∩ 32Z.

S-1 Validity of each chain.
- u = 1: v4 Theorem N.
- u >= 3: Theorem K(u) (closure section 6; the Part B audit confirms sections 0-6 at stride 4u). Every (V1)-(V5) violation of a chain region lies in a cell of section 3 marked E, C or W. The labels of C cells leave R_tau: they go to Bad_split (WD), to R-e or R-f (WP), or to E_D (WP).
- K8' holds: label columns are distinct, every double is a label column, and the N1 blocks and Proposition partial are stride-free.
- The Feo, Foo and Fee kills apply inside one region R_tau. Configurations that span regions are excluded by the localisation of Theorem K section 1 [CA-7].
- Uses (M9), now A (audit_menu_m9_a.md, audit_menu_m9_b.md).

S-2 U1 at stride 4u.
- (a) N := u Ds - DM is in 16lZ. Dt = 0 iff the two labels are in one class iff N = 0.
- (b) The slot determines the label, by division: 0 <= u i <= u(A - 1) < p.
- (c) (A, audit_menu_m10.md) t = rho_s + 16lk with 0 <= rho_s < 16l gives (rho_s, k) by division. rho_s gives s, because u is a unit mod 16l and |s| < h < 16l. The core audit left (c) undecided because the core wrote only 'as before'.
- (d) Dx/4 - u Dy/2 = DM for two odd points and -N for two even points.
- Notation [CO-5, TA-5]: N = N_u = Dn_u always means the difference of the class constants, u Ds - DM.

S-3 The pair choice and the Theorem D event (A, audit_menu_m10.md; fix SC-7).
- Y = (Bad_split ∩ S) \ D4 depends only on chi and on deterministic data, because in-class pictures are (l, p)-free. This is U3 at stride 4u (core section 2, A; Theorem U(u), A*).
- Theorem D (i) and (ii) hold with finite kappa (Part A).
- So Theorem D-weighted (A-18) with (D1)-(D3) and Markov gives the Theorem D event with probability at least 1/4 (Theorem D-weighted itself states at least 1/2; any positive bound suffices, audit_menu_m10.md), the same for every family (l_u, p_u)_u. Choosing the pairs before chi is therefore legitimate.
- Theorem U(u) holds pointwise, so X_F <= Y_F^(tau,u)(l_u, p_u) for every chi.

S-4 Subset chains (A*, closure Part B audit; fix CB-g). By V2-1, a chain with label set Y0 and relocation set R is violation-free if F(empty set) is clean and R meets every bad Lambda (|Lambda| <= 7) with Lambda ⊂ Y0. Each cell verdict depends only on the labels of Lambda and their classes, and each count is an upper bound over the realised shapes. Removing diagonals only shrinks Y0 and the set of realised shapes. So a chain that holds only the diagonals assigned to it is valid, with the same counts. This settles the undecided u = 1 item of the heavy-count audit.

S-5 Partition (V3-1 for the menu). First-fit puts every label in exactly one of WE, WP, WD or a chain region. Rules 1 and 3 receive only labels of S. So the doubles carry each parity edge exactly once (J5, K8').

S-6 Gluing.
- J5' is stride-free by its statement (A-13; heavy-count audit).
- Each chain ends in row-1 tails, so it equals beta_z on the 2W_h-neighbourhood of its window.
- No violation meets two chains: its span is at most 2W_h + 1, which is less than the gap.
- The seams inside a chain are v4's seams. Their J1* entries are (M9)(a), now A (audit_menu_m9_a.md).
- [RA-7] This gluing needs each chain to be a valid block. That is S-1.

S-7 Relocation count.
- O(h): R-a, R-b, R-c, D1, D9, the rows outside [5000, h - 5000], and T2's rows (2). These sets are defined by rows, so they are counted once.
- O(h^(3/2)): D4, D10 and the T1-exceptional labels.
- O_u(h^(11/6) log h) per chain: R-e. The Lemma IV(u) tail is h^2 times the sum over be > c h^(1/6) of (1 + log(u be))/be^2, plus h^(5/3). The FF'(u) tail is h^2 W^(-1/3) + h^(5/3).
- At most 512 C_u h^(9/5 + 2eps) per chain: A4, B7, D8, D17 and D18 at (l_u, p_u). Minimising Y^(u) bounds each term only by the total (the V4-2 form). Add D11, which is O(h^(9/5 + eps)) and deterministic.
- E_D <= 4h^(2 - eps_D), from the one group.
- So n_rel = O_U(h^(2 - eps_D) + h^(11/6) log h + h^(9/5 + 2eps)), and c0 n_rel tau*(h)^2 = h^(2 - min(eps_D, 1/6) + o(1)) = o(h^2).
- Relocation moves n labels by Proposition partial in width c0 n tau*(h)^2, so a family that hits O(h^(2 - delta)) labels is harmless.

3. STRIDE-4u OBSTRUCTION TABLE
Format: cell | verdict | stride 4u (V = verbatim, R = re-derived, F->R = fails for the untwisted rule and holds under (B2') and (B5')) | status.
For u = 1 every cell is consolidated_board_v4.md section 3.
For u >= 3:
- 'gap' means the cross-class distance 4(p - u(A - 1)) > 4(P_u - u/2)h + 2u, which is at least 298h + 6 at u = 3 [CO-2].
- 'core', 'table', 'ratio', 'shape' and 'closure' are the five stride notes.

WINDOWS AND CHAIN
- W1 [WP] | W | P2, stride-free | P.
- W2 [WD] and W3 [WE] | W | Theorem N1. Profiles use T only. | A-31; heavy-count audit (Theorem E stride-free).
- W4, a violation meeting two windows | E | J5' with at most |U| + 99 windows | A-13 and V4 audit; S-6 (A, audit_menu_m10.md; assembly in audit_stride_menu_closure_b.md).
- W5, the switch | E | Lemmas chain and rival | P.
- L1, two regions, or a label point with a buffer point | E | margins [F12] and Theorem K(u) section 1 | A* (Part B). This settles the ratio audit's L1 item.
- C2/L2, SAW*-shift gap with sea | E | fillers only; SAW Theorem 1(3), (4'), with h >= 424 | V; A* (DL(a)).
- E1/L3, SAW*-shift with a Sea(r0,g) seam | E | Table J1* with rho0 from (B5) | A (M9)(a), audit_menu_m9_a.md.
- C1/L4, buffers, chains, all-g and tails | E | J2, Lemma sea and V2-2 (rows only) | V; A (M9)(c), audit_menu_m9_b.md.
- E2, junctions | E | J2, J3 (at most 7 columns) and J5' are V. J4 is R: 4(16lp - uA) > 2600h^2 [TA-10] | A (core, table).

LABEL ONLY
- A1, LLL and LLLL right angles | E | F->R.
  - stride_menu Lemma 4 at s = 4u leaves only (E;O,E). Only this conclusion is cited. Lemma 4's statement (placement s(i + pc), its t1 bound and its displayed equation) does not hold verbatim at the board placement 4(u i + p t + b); the residual equation and bounds below are core 4(ii) (audit_menu_sweep_core.md).
  - Then c2((8u^2 + 2)t1 - T0) = 8u t1 N with l | N.
  - 0 < |b'| < (1 + Delta_u/(8u(P_u - u) - Delta_u))(h - 1) < l. At u = 3 this is 1 + 37/1715, below 1.0216h.
  - Status: A (core 3 and 4(ii), table A1, ratio 1(ii)).
- A2, rival pairs | E | V. In class, G_T^(2u) excludes them. Across classes, |t| < 2h < gap | A.
- A3: I.1; II(1,1); II(-1,-1); II(1,-1) with Sigma = 0; 3 or 4 classes | E.
  - MQ Theorem 2 is V. Theorem 1 is R. Theorem 4(a), (b) are R, (c) is F->R ((Delta_u/p) = -1), and (d) is V.
  - Proposition 1(c), II(-1,-1) with Sigma != 0, is F->R: l | N, with the margin below 1.0216h at P_u = 76.
  - II(-1,-1) with Sigma = 0: Delta_u(delta - Ds)^2 = (2u Ds)^2 (mod p).
  - A-24(d) is V. The role kills are re-checked in shape S2.
  - Status: A (core, table, ratio) and A* (shape).
- A4: I.2, and II(1,-1) with Sigma != 0 | C | R.
  - shape S1: U* n2 = 8ua(2N - u Ds) with U* = 2 Delta_u a + T0, and |a| < h/(8u(2P_u - u)).
  - shape S2: X^2 + Y^2 = U2^2(H^2 + 16u^2 Sigma^2), 16u Sigma | H U2, and at most one (l, p) per skeleton [CB-e].
  - Status: A* (shape), A (table).
  - Labels hit: average h^(1+o(1)); at (l_u, p_u) they lie inside 512 C_u h^(9/5 + 2eps); to WP.
- A5, cross-block A2 pairs | E | F->R. Odd points: mod p. Even points: mod l, under the twist | A (core 4(i), table A5).

LABEL AND SEA
- S0 | E | (F1), sea_row3 Theorem A | A (M9)(b), (c): audit_menu_m9_a.md, audit_menu_m9_b.md.
- B1 [S2, S9], X1 and X2 | E.
  - v3 A(i) needs only label columns congruent mod 64, so it is stride-free. v3's mixed-parity line should read c - a = 0 (mod 4); the conclusion stands.
  - Corollary B M2a: delta = u eps (mod 16) with u odd.
  - Status: A (table) and A* (shape re-derived A(i)). The details of Corollary B are A (M9)(b), audit_menu_m9_a.md.
- B2, Pa and Pb with two labels | E | v3 A(i) | A*.
- S6, intra-class Pc, both odd | PARKED, not empty [CO-1].
  - (u Di + DM)a = u_V Di. Dt != 0 is impossible by the mod-p size step. Dt = 0 gives a = u_V/u, so these triples exist iff u | u_V, about 1/u of the odd label rows.
  - G = V + (4ut, 2t), E = V + (u_V/u, -2u_V), and W lies in a shallow column in row r0 + 2t, with 2t = 0 (mod 64).
  - Status: A (core audit, serious fix) and A* (shape S4(c)); table S6.
- S7 | E | R: mod p gives 2ua = f exactly, so DM = 0 | A.
- S8, both even | E | F->R (L-adic): mod l, |2ua - f| < (1 + u/(2P_u - 3u))h, which is 1 + 3/143 at u = 3. Dj = 0 forces a = 0 [TA-9] | A (core 4(iv), table S8).
- S10, SLF-Pc | parked | one label | A* (DL(a)).
- B3, V3 SLL/SLL | E | R (A(iii)): 2u(x_W - 4ut) - (1 - r0) - 8ub = (8u^2 + 2) i_V + 8up t_c, with 0 <= (8u^2 + 2) i_V < 8up. So W determines the triple | A (table) and A* (shape).
- V3 SLL/SLF | E | the W rows are r0 + 2t (2t = 0 mod 64) and r0 + g (v2(g) = 3) | A* (shape, Part B).
- B4 [M0-M3] | E | block_sea Theorem 2, sea_row3 A(iii), Corollary B; odd deep rows congruent mod 8. For M9 and the low part of M0, cite obstruction_table section 3 (same-parity row differences of deep points are 0 mod 8, against |Dy| = 2e in {2, 4}), not the same-class step of sea_row3 2(iii), which is stride-4 specific. For M2, cite Dy = 2Dj in 32Z (stride-free); the BH16 A3 route also holds (core 5(i)) | A (M9)(c), audit_menu_m9_b.md.
- B5, in-class even-even M2c | E | R: empty (R4 would need zeta = -1; core 5(vi)) | A and A*.
- B6, in-class odd-odd M2c, R_IV(u) | C | R.
  - R4: edges (q m, p m), with (al, be) odd and coprime, 0 < al < u be, v2(u be - al) >= 3, F_u = 4(al - 2u be)^2 + be^2, g = gcd(F_u, u be - al) | Delta_u, q = al F_u/g and p = (al F_u + 4be^2(u be - al))/g [CA-1].
  - The table's g_T is a superset (D2). At u = 3 every divisor of 111 occurs as g_T [TA-3]. (349, 749) checks the k = 4 family [TA-4].
  - Status: A (ratio) and A* (Part A).
  - Destination: Bad_split to WD. Heights above h^(1/2)/32 go to WP (R-e), O_u(h^(11/6) log h).
- B7, cross-class M2c | C | R (shape S5): DM = Delta/4 - ue (p-type); N = ue - Delta/4 (l-type) | A* and A | O(h^(9/5 + eps) log h) on average; to WP.
- M7', M9, B8 and S13 | E | rows; (L2), (L3); Lemma rival and J1(e); sea_row3 A(ii); M9 cites obstruction_table section 3, as in B4 | A (M9)(b), (c): audit_menu_m9_a.md, audit_menu_m9_b.md.

LABEL AND FILLER
- D1, S2 near the band | C | DL(a): the S2 witness column at offset 0 is a hole or an R-b label [CB-a] | A* | O(h), in R-b.
- D2, T1 and CE | E/C | one label (SAW Theorem 1(5), Lemma 2; re-read in Part B) | A* | to WP (R-d).
- D3 [T2] | E.
  - u = 1: v4.
  - u >= 3: absent, because the class line has slope 1/(2u) [CO-3].
  - Every in-class 2L2F is D12/D13 (df = 0, same row) or D15 (df != 0). So nothing rests on the unaudited claim that T2 is a point of the cubic [CA-6].
  - Status: A (core audit).
- D4 and D4' [D-1L3F] | C / E | one label; V2-4, S1L, R-b | A* | D4: O(h^(3/2)), in R-d.
- D5: Feo, SAW-S3 and S3-low | E.
  - Feo is R (core 5(ii), closure 4(b)), from (C1)-(C4) only [TA-11: cite core 5(ii), not the table's D5 formula]. The saw (iii-a) V-vertex proof text uses the stride-4 even-row line and is not cited at stride 4u (audit_menu_sweep_core.md).
  - SAW-S3 is V. Q4(a) is R (core 7).
  - Status: A and A*.
- D6 | E.
  - FFe is V.
  - Fee is F->R: 8 alpha(u eta - N) = -d eta. In a class it fails by parity. Across classes, mod l, |8u alpha + d| < 1.021h < l. eta = 0 forces alpha = 0.
  - Foo, filler vertex: R (core 5(iii)).
  - Foo, label vertex: R. Normalise eps = Di/4 and e = (y_V - y_O)/8, so that alpha(4u eps + DM) = -4e eps. Then u alpha + e is odd, hence nonzero; across classes it is divisible by p with |u alpha + e| < p [CA-2].
  - Status: A and A*.
- D7, FFo | parked (hole vertex) / E (label vertex) | for labels not in R-b, the W row is at least T* + 272 >= h + 86. R-b labels are relocated [SC-4] | A*.
- D8, family (d) | C | R (shape S3).
  - x_V2 - x_V1 = 4DM with |x_V2 - x_V1| >= 64p, so the family is empty unless 64p <= 2W_h + 1.
  - Status: A*.
  - Labels hit: average h^(1+o(1)); at (l_u, p_u) inside 512 C_u h^(9/5 + 2eps); to WP.
- D9 | E after R2' | V2-6 (rows), with label slots at offset 0 by the true rho0 of (B5) | V; A (M9)(c), audit_menu_m9_b.md | in R-c.
- S4 and S5 | E | one label | A* (DL(a)). S11 and S12 are A (M9)(c), audit_menu_m9_b.md.
- D10, (e,F) rival pairs | C | saw (i), H0 = 210 | V (re-read in Part B); A (M9)(c), audit_menu_m9_b.md | O(h^(3/2)); to WP.
- D11 | C, deterministic | saw (ii-a,b), point_counts | V (re-read in Part B); A (M9)(c), audit_menu_m9_b.md | O(h^(9/5 + eps)); to WP.
- D12, d > 0 | C | R_FF^+, |Delta i| <= 210 | A (M9)(e), audit_menu_m9_a.md | to WD (q = 1).
- D13, d < 0 | C | R: FF(u) and FF'(u).
  - For t != 0 and gcd(a, b) = 1: (P - 8ut)(P^2 + 4t^2) = 8tY1(P - 4ut), and Y2/Y1 = V_u/U_u at a/b = P/(2t).
  - m = 2u and b = 0 are forced out by the cubic [CA-3]. t > 0 is D12.
  - gcd(U_u, V_u) | 8u Delta_u. The sum of 1/|U'| is finite, the tail is O(W^(-1/3)), and there are O(X^(2/3)) shapes.
  - The converse of F2(i) is restricted to beta in {1, 2}, with filler offsets != 0 (mod 16) [RA-2].
  - Status: A (ratio) and A* (Part A).
  - Destination: WD. |U'| > h^(1/2)/32 goes to WP.
- D14, ll/FF | E.
  - In a class: 256 Delta_u t''^2 = Dmu^2 + 4 Dw^2 is impossible (core 5(iv)).
  - Across classes: two_filler Proposition 4 with |Dx| >= gap, and 4 x 298h > 420^2 for h >= 148 [CB-b, CO-6].
  - FF/ll: via A5.
  - Status: A and A*.
- D15, in-class 2L2F with df != 0 | E | two_filler Corollary 2. Its inputs Dx = 0 (mod 16) and Dy = 0 (mod 32) come from (C1)-(C4) [CA-5] | A* (shape S5).
- D16: F1, F2, F3 with n_y >= 0 | E.
  - F1 is V.
  - F2 is R. If Dy != 0, mod p (or mod l, even-even), 2u n_x + n_y = 0 with |n_x| < h/(4(P_u - u)). If Dy = 0 and the diagonal is a filler pair, |X| <= 10 < p. If Dy = 0 with a label diagonal, the configuration falls in A3/A5 [SC-5, CB-d].
  - F3 with n_y >= 1: |Dx| <= 106h + 2 < gap.
  - Status: A*.
- D17 | C | R (S5): the df = 0 map is stride-free, and the type is p-type with DM = Dx/4 - u Dy/2 | A* | O(h^(9/5 + eps) log h); to WP.
- D18 | C/E | R (S5): l-type, N = -(Dx/4 - u Dy/2) | A* | the same.
- D19 and D20 | E | Lemma 3L1F-a, Lemma N, Theorem Q3 and Lemma Q3; only (L1)-(L3) and (K-a)-(K-d) | A (core) and A* (Part B).
- D21 (Q4) | E or in A3/A4/D10 | R (core 7) [TA-11] | A.
- D22, V3 completeness | E, except D8 and the parked S6 triples.
  - Theorem C(u) holds given v3 Theorem B's case split (block_sea Theorem 1, audited, stride-free), together with A(i), core 4(iv), 5(ii) and 5(iii), and table D6 [SC-3].
  - SLF/SLF in one class: gamma1 gamma2 = u_V g/8 has v2 = 0, against 4 or 2 [SC-1].
  - Status: A*.
- [V1] | E | R: from A1, D5, D6 and SAW Theorem 1(3) (FFF) | A (M9)(c), audit_menu_m9_b.md.
- [V2] | E | the union of the S and T cells | as those cells.
- [V3 cross-type], [R4] and [D-4F] | E | V (rows, parity, one label) | A (M9)(c), audit_menu_m9_b.md.

JUNCTIONS AND EXCEPTIONAL SETS
- E3 and E4 | N1(c), (e) | stride-free | A (M9)(c), audit_menu_m9_b.md.
- E5 | R-a (Corollary B's exceptions i = 0, and in row-3 types also i = 2 and j in {0, 1}; Corollary B's BH16 S1 labels do not occur in the SAW*-shift board), the near band, the low rows and the T1-exceptional labels | rows | A (M9)(c), audit_menu_m9_b.md | O(h^(3/2)); to WP.

OPEN CELLS: none was found by any audit. Every cell is E, C or W; the (M9) cells are now A (audit_menu_m9_a.md, audit_menu_m9_b.md).

4. K4(u): the constants that change at u >= 3 (u = 1: v4 K4)
Status: (M11), swept by audit_menu_sweep_core.md, audit_menu_sweep_cross.md and audit_menu_sweep_classes.md, written [core], [cross] and [classes] below. Tags on the added lines: H = holds as written or a fortiori; R = holds by a re-derivation on file; NU = stride-4 specific, does not transfer, not used by the board.
- p range: P_u = max(40, 8u^2 + 4).
- Phase and lattice (R). Read (K-a) of three_label_one_filler, K1 of consolidated_board, [F1] of consolidated_board_v2, (F1) of low_rows and the BH16 A3 statement through (C1) and core 5(i), with rho_tau = u(iota + sigma) - kappa_tau (mod 16). Their literal stride-4 forms are false whenever (u - 1)(iota + sigma) != 0 (mod 16); the proofs need only one slot residue per region, which (C1) gives. The A3 lattice at stride 4u is u y = 2n + 2u + 2kappa_tau (mod 32), so y = 2u n + 2 + 2u kappa_tau (mod 8), and it still gives delta = u eps (mod 16). [core]
- (L1) of obstruction_table (R): M_c = u sigma - kappa (mod 16) and x0 = 4(u iota + M0 + b_tau) (mod 64). The conclusion, label columns congruent mod 64 and label slots at offset 0, holds; read it through stride_transfer_table (I2). [cross]
- True rho0 (R): Lemma N, S1L (V2-5), V2-6, the SAW* rows and J1* are read with rho0 from (B5). [core]
- gap: 4(P_u - u/2)h + 2u, which replaces 158h. It is at least 298h + 6 at u = 3 and increases with u. Every v4 lower-bound use (A2, sea_row3 6h, F3 106h + 2, Proposition 4) holds a fortiori.
- low_rows (F6), Lemma S and Q4(c) (H): 156h and 131h become 298h and about 273h at u = 3. [core]
- sea_row3 (H): |beta| <= 6h and (H4)'s 2h are compared with the gap. In 2(iii), the stride-4 sentences 'Same class: B - D = (4t, 2t)' and '|beta| <= 6h < 76h' are replaced at stride 4u by the row argument: no same-parity deep pair in one region has row difference 2 or 4 (v4 (B3), (B6)), so the case is empty. [core; audit_menu_m9_a.md]
- V2-8 (H): |p Dt| >= p > u(A - 1). [core]
- stride_menu Lemma 4 (R, conclusion only; see A1): |bracket| < (8u^2 + 4)h < p, and 4(p - u(A - 1)) > h. [core]
- mixed_quadruples Theorem 4, parity step (H): U.w = 16u(p Dt + u k) + 2U2, and |16u(p Dt + u k)| >= 16u(p - uA) > 2h >= |2U2|. [cross]
- J4: 4(16lp - uA) > 2600h^2.
- heavy_diagonals Proposition 4(a) (R): t_c = p^(-1)(u s_c - kappa), with spacing 4(16lp - uA). [classes]
- U1 sizes: |DM| <= h^2/8 + uh/2 + 1 and |N| <= h^2/8 + 1.5uh + 1 < (1.04h)^2 for h >= 2u. So a nonzero value has at most one prime factor in each range.
- V2-7 (H): |N| <= u h/2 + (2W_h + 1)/4 < (1.04h)^2, with Ds = u^(-1) N (mod p). [core]
- uniformity (H): #P >= (P_u/4 - o(1)) h/log h and |DM| <= h^2/8 + uh/2 + 1 < (P_u h)^2. U1(a), (b) and (d) use the twisted forms of S-2. [cross]
- Thin margins, all below 1.04h < l [D1]. These are three separate conditions, all true for every odd u >= 3 (proof below, audit_menu_m10.md; the values also check numerically for u < 400, audit_menu_sweep_cross.md):
  - rigid 2(e): 1 + Delta_u/(8u(P_u - u) - Delta_u), which needs 8u(P_u - u) > 26 Delta_u. It is 1752/1715 at u = 3.
  - L-adic and Fee: 1 + u/(2P_u - 3u), which needs P_u > 14u. It is 1 + 3/143 at u = 3.
  - Proposition 1(c): 1 + Delta_u/(4u(2P_u - 3u) - 1), which needs 25 Delta_u < 4u(2P_u - 3u) - 1. It is 1752/1715 at u = 3.
  Proof for every odd u >= 3 (P_u = 8u^2 + 4, Delta_u = 4u^2 + 1). Rigid 2(e) and Proposition 1(c) both reduce to 64u^3 - 112u^2 + 32u - 26 > 0. This is 790 at u = 3, and its derivative 192u^2 - 224u + 32 is positive for u >= 2. The L-adic and Fee condition is 8u^2 - 14u + 4 > 0, true for u >= 2. At u = 1 the v4 values apply. All three margins fall like 1 + 1/(16u).
  The table's 1.020h, 1.019h and 1.0205h hold only for its 80h range.
- I.2: |a| < h/(8u(2P_u - u)), which is h/3576 at u = 3, and |N| <= (h - 1)^2/(16u) + 1.5uh.
- mixed_quadruples setting (R): replace s P Dc by 4 p Dt and s(P - (A - 1)) by 4(p - u(A - 1)); the bounds are the I.2 and II lines here (table A3/A4, shape S1/S2). The literal bounds read at s = 4u (|a| < 2h/(39 s^2), h/2808 at u = 3) are weaker and stay true. [cross]
- rigid_layout Theorems 1 and 2 (R): 'b | N' becomes b_u | u N_u, with b_u = 2 Delta_u t' - T' and q = u N_u/b_u; 294 becomes 16u(P_u - u) - 2 Delta_u (3430 at u = 3); the margin 1.035h becomes the rigid 2(e) margin above. The board uses only the conclusion of 2(e). [cross]
- v3 (L) and Theorem A (R): lambda = 2y - x becomes lambda_u = 2u y - x, equal to 2u - 4M_c and 4u + 4(u s - M_c). In A(ii), a = u_V becomes a = u_V/u (S6), and the both-odd bound is |a| < h/(4(P_u - u/2)). A(iii) is B3. [core, cross]
- II: |Sigma| < 2h^2/(16u(p - uA)) and |N| <= h^2/(8u) + uh. The triple count per Sigma is the sum over d | N0 of (2h/d + 1)(4hd/N0 + 1) <= tau(N0)(8h^2/N0 + 7h), with N0 = 16u|Sigma| [SC-2]. The source line of stride_shape_counts S2 still reads (2hd/N0 + 1); cite this line instead [audit_menu_m9_a.md].
- Foo, label vertex: |alpha| < h/(16(P_u - u)).
- F2: |n_x| < h/(4(P_u - u)), which is h/292 at u = 3 (h/796, h/1556 and h/5372 at u = 5, 7 and 13). It follows from the direct bound |n_x| <= h^2/gap < h/(4(P_u - u/2)), which is h/298 at u = 3. Either way |2u n_x + n_y| < 2u h/(4(P_u - u)) + h < p (audit_menu_sweep_core.md, audit_menu_sweep_cross.md, audit_menu_m10.md).
- D8: |x_V2 - x_V1| >= 64p.
- R_IV(u): q > al be^2 and 4u be^3/Delta_u < p <= (128u^3/27 + 4u) be^3. At u = 1 this is about 8.74 be^3 < 21 be^3; at u = 3 it is 140 be^3 (the observed maximum is 134).
- V2-3, the R_IV(u) cutoff (R): max(p, q) <= C_u be^3, so an edge above h^(1/2)/32 has be > c_u h^(1/6). [core]
- additive Lemma 4(a) and polylog Lemma IV (R): about u be/4 values of al per be, in place of (be - 1)/4, and S_IV(u) <= (Delta_u/16) sum over be of be^(-2)(1 + log(u be)). [classes]
- ratio_graph Corollary 3 at k = 5 (R): v2(p - q) = 2 + v2(u be - al) >= 5. [classes]
- SAW Lemma 4(a) (R): the residue condition is (Delta_u/p) = -1; 4(b) goes through l. [core]
- R_FF(u): gcd(U_u, V_u) | 8u Delta_u; [G11] per-type density gcd(64, |U'|)/|U'| <= 64/|U'|, modulus dividing lcm(32, |U'|). The sum of 1/|U'| over the shapes at fixed k is at most 2(16u^2 + 1)/|k|^3 + pi/k^2, so S_U(u) <= 4(16u^2 + 1) zeta(3) + 2 pi zeta(2). This corrects the weaker, still summable form in stride_transfer_ratio.md section 4 [classes].
- Lemma FF' (R): the constants 17 and 40 are replaced by FF'(u), with gcd | 8u Delta_u. [core]
- additive Lemma 4(b) (R): 17 = 16 + 1 becomes 16u^2 + 1 (a^2 + b^2 >= k^2/(16u^2 + 1)), and 40H/|U| becomes 8u Delta_u H/|U|. [classes]
- additive Lemma 1 (R): P != 4t becomes P != 4ut, since (P - 8ut)(P^2 + 4t^2) = -16u Delta_u t^3 != 0 at P = 4ut. [classes]
- ll/FF (R): the stride-4 norm 20t^2 becomes 4 Delta_u t^2 (core 5(iv)). [core]
- R_FF^+: |Delta i| <= 210, 6 neighbours on each side, c_1 <= 12. The bound n_y = Di <= 210 is row-only: fillers lie in [h - 210, h], and max(h - T*) = 186 in Table J1* [audit_menu_m9_a.md; core].
- Width per type: 4p · 16lB + 4uA + 2(2W_h + 1) + 24, with at most 3 slots for (Phi) at each end. v4's + 12 has the same slip; it is O(1) per type and changes no bound [audit_menu_m9_a.md].
- Not transferred; not used (NU). Do not cite these at stride 4u:
  - consolidated_board Lemma 3L1F-a (the line (4x, 2x); 5 mu and 5 nu integers). D19 uses Lemma N. [core]
  - deep_layer_sawtooth Proposition 5 (T2, |AB|^2 = 200t^2) and the Corollary 6 range. D3 is absent at u >= 3. [core]
  - sea_row3 2(iii) same-class numerics ((z - 4)^2 - 20, beta = 8). Same-class pairs are empty because Di is in 32Z (core 5(v)). [core]
  - saw (iii-b): the nodal cubic with 4d, (a - 2b) | 5db^2, and its d > 0 finiteness. d > 0 is the R_FF^+ superset; d < 0 is FF(u). [core]
  - saw (iii-a): the V-vertex proof text and the thickness formula N = f'(20f' - T). D5 is core 5(ii). [core]
  - BH16 A4 (it holds with y = 2u n + c (mod 8)) and rule B; stride_menu Derivation 1 (1c). [core]
  - mixed_quadruples Theorem 5 (S2a), cross-block: it fails at large h at every stride (above about h = 596 at u = 3). [cross]
  - heavy_diagonals_sharp Lemma 1 and the lower bound of Theorem 2, and heavy_light Theorem 2(a): these are Q(sqrt 5)-specific. For sharpness at stride 4u, cite stride_menu_heavy_count Theorem LB, proved for |U| <= 5 only. [classes]
  - full_layout_junctions section 0 and its Summary and Gaps lines ('stride 4 only', no sea at stride 12): superseded for strides 4u with u odd by stride_transfer_core.md (Lemma C, Theorem T) and stride_transfer_ratio.md. The remark stands only for strides with v2(sigma) != 1. [classes]
- Stale stride-4 constants, read through this list and never verbatim: full_layout (P6) (20h, 40h] with p = 3, 7 mod 20, J4 40h^2 - 44h and (P4) 128 types; heavy_light Proposition R p <= 40h; polylog Lemma IV g | 5 and al be^2/5; additive Lemma 2 gcd | 40, Lemma 1 |t| <= 86, and Theorem 5's 63 and 86/16; heavy_diagonals Proposition 4(a) untwisted t_c [classes]; the stride_transfer_table values at 80h (1.0205h, h/314, 314h, h/3768, h/1880), superseded by the 76h values here [cross; TA-2].

5. WIDTH AND EXPONENT
- Light regions. Summing over u in U and the 512 types: at most 512 · 4 · 2P_u h · 16 · 2.08h · B (1 + o(1)) per chain, which is 136314.88 (sum over U of P_u) B h^2 (1 + o(1)). P_1 = 40 recovers v4's 5452595.2 B h^2. The factor is 2.9 for {1, 3} and 51.8 for U5.
- Buffers, margins and sea pieces: |U| · O(h^2).
- Window gaps: at most (|U| + 99)(h^2/2 + 3).
- Theorem E. Delta = H^U(B/4) <= C(a, U) 4^a h Lambda^(beta_|U|(a)) B^(-a), by (M2). The cost is C h^2 Lambda^(beta_|U|(a) + 2) B^(-a) ell^C1 + C h^2 ell. Theorem E takes any set of diagonals and uses only label rows and T1/T2 profiles, so it is stride-free.
- Theorem D: one group with rho = 2/B, |D| <= h and finite kappa. The cost is C kappa h^2 Lambda^2 ell^C1/B + C h^2 ell.
- N1 collars and separations: O(h^2 ell).
- Switch, tails and Proposition partial: o(h^2) in case (a). For odd h, case (c) adds 4 c0 tau*(h)^2 + 6h^2 + 4 = O(h^2).
- Total: M <= C_U h^2 (B + Lambda^(beta(a) + 2) B^(-a) + Lambda^2/B) ell^C1 + C |U| h^2 ell + o(h^2).
- Exponent. With B = Lambda^x, the exponent is max(x, beta(a) + 2 - a x, 2 - x). Take x = (beta(a) + 2)/(1 + a). Then the middle term equals x, and 2 - x < 1 < x. At a = a*_|U| this is x_|U|. So M <= C_U h^2 Lambda^(x_|U|) ell^C1.
- Passage to m_h. Every truncation with m >= M has m + q_h points, so f(h, m) >= m + q_h. The paper's upper bound f(h, m) <= m + q_h then gives equality for all m >= M, so m_h <= M.
- The numbers of the theorem statement are single evaluations at the stated a*, in 40-digit arithmetic (expo_point.py). They agree with the note and its audit.

6. LEMMA MI AND COROLLARY M-INFINITY
Lemma MI (A, audit_menu_m10.md). The corollary now uses Lemma SQ of squarefree_menus.md instead, because Lemma MI menus can contain u with Delta_u not squarefree (u = 9).
- Build u_1, ..., u_k inductively. Start with u_1 = 1 (q_1 = Delta_1 = 5), so every menu contains 1. For j >= 2, let D be the largest Delta_(u_i) with i < j, and take a prime q = q_j = 1 (mod 4) with q > D (Dirichlet).
- -1 is a square mod q, so 4u^2 + 1 = 0 (mod q) has a root u0 (from 2u0 = x, where x^2 = -1). Since f(u) = 4u^2 + 1 has f'(u0) = 8u0 != 0 (mod q), exactly one of the q lifts of u0 mod q^2 is a root mod q^2. Take another lift, then make u odd by CRT. So v_q(Delta_(u_k)) = 1, and q divides no earlier Delta_(u_j).
- Independence. Suppose a product over a subset S is a square, and let j = max S. Then v_(q_j) of the product is odd, which is impossible.
- Sanity script menu_mi.py: it gives u = 1, 9, 113643 with q = 5, 13, 337, all independent, and confirms U5 independent.

Corollary M-infinity.
- Theorem X (A): x_k decreases strictly to x_inf = min over a of (1 + 3^(a/2))/(1 + a).
- One evaluation at a = 1.5833613 gives x_inf <= 1.3108171966 < 1.3108172.
- Given eps, choose k with x_k < 1.3108172 + eps/2, and take U_k from the Corollary of Lemma SQ (squarefree_menus.md, audited in audit_squarefree_menus.md), so every Delta_u is squarefree. The corollary uses (M4)-(M9) at every odd u of U_k, which the sweeps and transfer notes state for general odd u >= 3. Theorem N_menu gives m_h <= C_(U_k) h^2 Lambda^(x_k) ell^C1, and ell^C1 <= Lambda^(eps/2) for large h.
- h_eps = max(h0(U_k), the height where ell^C1 <= Lambda^(eps/2)).
- U_k is fixed for fixed eps, so the u-dependence of C_u, h_PNT and kappa(u) is harmless [SC-6]. The Corollary uses (M4)-(M9) at every u in U_k. Take U_k with every Delta_u squarefree (Lemma SQ, squarefree_menus.md), so u such as 9 never occurs.

7. FIX LEDGER (every audit issue on file and supplied)
Heavy count (audit_stride_menu_heavy_count.md):
- HC-1: Y^2/n = (4 + 1/u^2) h^2/T^2. Applied in (M2).
- HC-2: n_T > 0.43h in Lemma L. Lemma L is not used here.
- HC-3: in case A, Lemma L gives kappa >= g/2 for T coprime to u Delta_u, with no designated prime. The falsity remark is deleted. This is lower-bound only.
- HC-4: by Biro (Acta Arith. 107 (2003)), (LB-hyp) holds only for u in {1, 3, 5, 7, 13}, so Theorem LB stops at |U| = 5. Biro is cited by the audit from secondary sources; the claim is not load-bearing.
- HC-5: the subset chain. Settled in S-4.
- HC-6: the 'Lambda^0.128 > 34' remark is dropped. P_u = max(40, 8u^2 + 4).
Core (audit_stride_transfer_core.md):
- CO-1 (serious): the parked intra-class SLL-Pc (S6, B3, D22).
- CO-2: the gap bound.
- CO-3: F4 is deferred into D12/D13, which are now closed by FF(u).
- CO-4: the p-range wording.
- CO-5: the N notation.
- CO-6: two_filler Proposition 4 and the K4(u) list.
Table (audit_stride_transfer_table.md):
- TA-1 (serious): the exponent rests on (M2) and (M3).
- TA-2: one p-range.
- TA-3: g_T at u = 3 can be any divisor of 111.
- TA-4: (349, 749) is a k = 4 edge.
- TA-5: N_u = +Dn_u.
- TA-6: M_c = u sigma - kappa + b_tau (mod 16).
- TA-7: the literal-rule A1 remark reads h >~ 1.2 x 10^5 (not load-bearing).
- TA-8: the witness conditions.
- TA-9: the eta = 0 and Dj = 0 cases.
- TA-10: E2, and Theorem K completeness (now A*).
- TA-11: D5 cites core 5(ii); D21 is R.
Ratio (audit_stride_transfer_ratio.md):
- RA-1: v2(c2) >= 8 (literal rule).
- RA-2: the filler offsets.
- RA-3: the Hensel identity uses Res(f, f') = +-4 disc. At p = 2, f' is odd and the root is unique.
- RA-4: Theorem DC uses truncated Lemma B. DC is not used here.
- RA-5: the Kronecker form suffices.
- RA-6: the Fo/Fo evidence at u >= 3 is constructive only.
- RA-7: gluing is conditional on valid chains (S-1).
- RA-8: the verbatim items go to (M9).
Shape counts (audit_stride_shape_counts.md): SC-1 to SC-7, as cited above.
Closure Part A (audit_stride_menu_closure_a.md): CA-1 to CA-7.
Closure Part B (audit_stride_menu_closure_b.md; its ninth item, the three D1 margin conditions, is applied in K4(u)):
- CB-a: DL(a), with v3 Theorem B. One-label W is never at offset 0.
- CB-b: cross-class ll/FF.
- CB-c: S6-S8 cite table S6, S7 and B3.
- CB-d: F2 with Dy = 0.
- CB-e: at most one (l, p) per skeleton.
- CB-f: v4 [G11].
- CB-g: the statuses are updated, and the subset chain is settled.
- CB-h: |U| in place of m.
Trace (audit_consolidated_board_menu_trace.md):
- TR-1 (serious): the three A* audits are filed; (M7) and (M8) cite them.
- TR-2 (serious): (M11), K2/K4 completeness at stride 4u, is added and swept.
- TR-3: C1/L4, D9, D10, D11, E3, E4 and E5 moved into (M9)(c); status key V added.
- TR-4: h0(U) with h_D(U) and h_SC(u).
- TR-5: F2 is h/292 at u = 3.
- TR-6: theta* = 1.49674291..., upper bound 1.4967430.
- TR-7: [G11] density gcd(64, |U'|)/|U'| <= 64/|U'|.
- TR-8: the C_U growth claim covers only the light width.
- TR-9: the u = 1 chain with B = ceil(Lambda^(x_|U|)) (section 0).
- TR-10: general U kept out of the main statement; menus contain 1.
Menu audits of 14 November (audit_menu_sweep_core.md, audit_menu_sweep_cross.md, audit_menu_sweep_classes.md, audit_menu_m9_a.md, audit_menu_m9_b.md, audit_menu_m10.md), all correct_with_fixable_gaps, all minor:
- the missing K4(u) lines, tagged H, R or NU, and the stale stride-4 constants (section 4);
- A1 cites stride_menu Lemma 4 for its conclusion only; D5 does not cite the saw (iii-a) proof text;
- (Phi) needs up to 3 slots at each end, so + 24 per type;
- [V1] and [V2] are not separate cells; SAW Lemma 3 leaves (M9)(c); B4 and M9 cite rows mod 8; E5 names R-a;
- the (M9)(c) cells use (B5') only through the true rho0;
- the thin margins are proved for every odd u >= 3;
- Lemma MI starts at u_1 = 1, and N_menu is stated for menus that contain 1;
- S-3: Theorem D-weighted gives 1/2; 1/4 is kept;
- the FF'(u) sum bound 2(16u^2 + 1)/|k|^3 + pi/k^2.

## External results used

- PNT in arithmetic progressions mod 4 Delta'_u and mod 20 (non-explicit). It gives #L_u >= (1/2 - o(1)) 1.04h/log h and #Pset_u >= (1/4 - o(1)) P_u h/log h. The joint density 1/4 holds because chi_(-4) chi_(Delta'_u) is nonprincipal.
- Jacobi reciprocity: (Delta_u/q) = (q/Delta_u) for odd q not dividing Delta_u, since Delta_u = 1 mod 4. Textbook.
- Dirichlet: L(1, chi) != 0 for real nonprincipal chi, and Mertens. Used only inside Theorem M1 (audited heavy_light Theorem 1(b)).
- Dirichlet's theorem on primes = 1 mod 4, and Hensel lifting for a simple root. Used in Lemma MI.
- As in v4: Henriot's corrected Theorem 5 (MPCPS 157 (2014) 375-377) through A-18, tau(n) << n^eps, and the product-form local lemma.
- Not used, remark only: Biro, Chowla's conjecture (Acta Arith. 107 (2003)), h(4n^2+1) > 1 for n > 13, as cited by the heavy-count audit from secondary sources.

## Checks

I read these in full: consolidated_board_v4.md; stride_menu_heavy_count.md, stride_transfer_core.md, stride_transfer_table.md, stride_transfer_ratio.md, stride_shape_counts.md and stride_menu_closure.md; and the four audits on file (audit_stride_menu_heavy_count.md, audit_stride_transfer_core.md, audit_stride_transfer_table.md, audit_stride_transfer_ratio.md). I read the head of census_stride12.md. I took the three supplied audits from the target text. I merged every issue by hand into the fix ledger: HC, CO, TA, RA, SC, CA and CB.

Two sanity scripts ran with py -I in my script folder, scripts_menu_board/.
- menu_mi.py. Its first run, with menu size 8, timed out at 60 s, because the Lemma MI numbers grow doubly exponentially and factoring them is slow. I stopped it and reran with size 3, which finished in a few seconds. Lemma MI gave u = 1, 9, 113643 (q = 5, 13, 337), with independence checked by F_2 rank. U5 and {1, 9} are independent. The three thin-margin ratios are below 1.04 for every odd u < 400 at P_u = max(40, 8u^2 + 4); the values at u = 3 are 1.02157, 1.02098 and 1.02157.
- expo_point.py. It evaluates (beta_k(a) + 2)/(1 + a) at the stated a*_k with mpmath at 40 digits, for k = 1 to 10 and k = infinity. The results match the audited table: x_2 = 1.4295234225, x_5 = 1.3689530191 and x_inf <= 1.3108171966.

I did not recompute anything else that is double-sourced. The repository was only read, I ran no git command and I did not use the web.

## Gaps

- (M9) and (M10) are discharged: audit_menu_m9_a.md, audit_menu_m9_b.md and audit_menu_m10.md re-derived every item and found no failing step. The (M9) re-derivations rest on the stride-4 audits they cite, which were not audited a second time.
- (M11), the K2/K4 sweep at stride 4u, found no failing step (audit_menu_sweep_core.md, audit_menu_sweep_cross.md, audit_menu_sweep_classes.md). Their scopes together cover every note cited in (M1)-(M8) (squarefree_menus.md). Lemma SQ, which the Corollary uses, is audited in audit_squarefree_menus.md.
- Several source notes still carry stale stride-4 text (listed in K4(u)). At stride 4u they are cited only through K4(u).
- Menus without 1 are a remark (N): (M4)-(M9) were not re-read for a dependence on 1 in U.
- The three A* audits are filed as audit_stride_shape_counts.md, audit_stride_menu_closure_a.md and audit_stride_menu_closure_b.md.
- The twisted-rule census on file (census_stride12_twisted.md) covers single types at h <= 1501 only. Cross-class cells need h of about 10^4 or more even to fit in one window. The R_FF(u) evidence at u >= 3 is constructive only, because the smallest depth at u = 3 is 21320.
- Constants and h0(U) are not explicit (PNT mod 4 Delta'_u, h_D, Dirichlet character sums in M1). The gain over v4 is asymptotic only. The light-width factor is sum over U of P_u/40: 2.9 for {1, 3} and 51.8 for U5.
- Uniformity in |U| is not proved. Corollary M-infinity uses one fixed menu per eps, and the Lemma SQ menus contain large u.
- The exponent values are single 40-digit evaluations at the stated a*, without interval arithmetic. They are upper bounds because any a > 0 is valid. Rounded values must be rounded up.
- Theorem LB (sharpness of menu-heaviness) is proved only for |U| <= 5 (class number 1, prime Delta; Biro caps it). It is not used here, but it means that x_inf = 1.3108172 is a floor for this method only for those menus. For general menus the floor is not proved.
- NOT PROVED: m_h = O(h^2), and any exponent at or below 1.3108172.

## Missing estimate

None for the near goal or for the menu theorem. Below x_inf = 1.3108172, menu-heaviness at relocation price Lambda^2 is the binding term: B against Lambda^(beta(a)+2) B^(-a). Theorem LB shows that it is sharp for |U| <= 5. To go lower one needs a heavy relocation price below Lambda^2, or a finer heaviness measure than min_u kappa_T^(u). The far goal m_h = O(h^2) is untouched.

## Next steps

- Add ledger rows for Theorem N_menu (menus containing 1, every Delta_u squarefree) and for Corollary M-infinity.
- Fix the stale texts in the source notes listed above (phase formulas, stride_menu Lemma 4 at s = 4u, stride_menu_heavy_count line 59, the S2 triple count), which the board already reads correctly.
- Fix the stale text in the source notes listed in K4(u): three_label (K-a), consolidated_board K1, v2 [F1], BH16 A3, the stride_menu Lemma 4 statement, saw (iii-a), full_layout section 0, the stride_shape_counts S2 count and the stride_transfer_ratio section 4 sum.
- Run a cross-class census of the twisted board L^{1,3} at h of about 10^4 or more, where cross-class cells first fit in one window (census_stride12_twisted.md covers single types at h <= 1501).
- Apply the one-line [G11] fix to consolidated_board_v4.md (B8): keep the density gcd(32, m)/m with v4's m = |U'|/gcd(2, |U'|), which equals gcd(64, |U'|)/|U'|, and change the bound 32/|U'| to 64/|U'|. Also change v4's '+ 12' per type to '+ 24'.
- For the exponent below 1.3108: a heavy relocation price below Lambda^2, or a finer heaviness measure. Splitting a diagonal's residue classes across strides is one candidate.

