# The consolidated board, version 4

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: consolidated_board_v3.md with every fix from the trace audit, the patches audit and the four constant sweeps applied, and a complete K4 list by note. Theorem N still gives theta* = 1.4967429. No sweep found a failing step. The sweeps cited here as Sweeps A, B and C are audit_constant_sweep_a.md, _b.md and _c.md. Status (patched 14 November 2026): no open mathematical item for Theorem N. Sweep T, the constant sweep of the (H1-T) notes (T6, T7/T8 and the two inputs of T3), found no failing step. The V4 audit found V4-1 and V4-2 correct. Their minor fixes and those of audit_consolidated_board_v4_diff.md are applied below. Sweep T is audit_constant_sweep_t.md and the V4 audit is audit_consolidated_board_v4_steps.md. The patch has a second reading in audit_consolidated_board_v4_patch.md (correct; record-keeping fixes applied), and the T1 chain is read end to end in audit_t1_chain_end_to_end.md. NOT PROVED: m_h = O(h^2).

# Result

## Status

partial

## Summary

consolidated_board_v4: v3 with every fix from the trace audit, the patches audit, the constant sweep and Sweeps A-C applied, plus a complete K4 list by note. Theorem N still gives exponent theta* = 1.4967429. No sweep found a failing step. No open item remains: Sweep T (the (H1-T) constant sweep) and the V4 audit found no failing step. Their reports are audit_constant_sweep_t.md and audit_consolidated_board_v4_steps.md. NOT PROVED: m_h = O(h^2).

## Statements

THEOREM N (v4; CONDITIONAL only on the audited inputs (H3) and the external results (H4); no open hypothesis). consolidated_board_v4, 14 November 2026. Problem 001. It replaces consolidated_board_v3.md. Notes are in research_archive/2026-11-13 unless a path says otherwise.

STATUS (14 November 2026). Nothing mathematical is open for Theorem N. (H1) and (H2) are closed, and no audit or sweep on record found a failing step. The 14 November edits that apply Sweep T (audit_constant_sweep_t.md), the V4 audit (audit_consolidated_board_v4_steps.md) and audit_consolidated_board_v4_diff.md have a second reading in audit_consolidated_board_v4_patch.md, which found them correct. The T1 chain is read end to end in audit_t1_chain_end_to_end.md (and earlier in 2026-11-09/AUDIT_threshold_upper_bound.md). Standing caveat: h0 is not explicit.

NOTATION
- Lambda = log h, ell = loglog h, E(a) = (1 + 3^a)/2.
- theta* = min over a > 0 of (E(a) + 1)/(1 + a) = 1.4967429, attained at a* = 0.9124154.
- B = ceil(Lambda^theta*).
- L***U is the board (B0)-(B10) in the proof field. It is v3's board with the v4 fixes. The colouring law is the same as in v3: the uniform random proper B-colouring of heavy_diagonals_sharp Proposition 3.

STATEMENT
Let h >= h0 := max(10^10, h_PNT, h_D).
- 10^10 is T1's profile range (filled_mod7 Section 3).
- h_PNT is the non-explicit height from the PNT in progressions mod 5 and mod 20.
- h_D is the non-explicit height of Theorem D (D1)-(D3). In v4 it also covers the non-explicit heights of ap_hypothesis_henriot Lemmas 1-4, including Henriot's C0 in C0 h^(eta/4) <= h^(eta) - 1 [Z24].

Assume the inputs (H3) and (H4) below ((H1) and (H2) are closed). Then for every m >= M, L***U truncated to columns 1..m is a valid blackout of the h x m grid with m + q_h points, where
 M <= C h^2 (B + Lambda^(E(a)+1) B^(-a) + Lambda^2/B) ell^C1 + C h^2 ell + c0 n_rel tau*(h)^2,
 n_rel = O(h^(2-eps_D) + h^(11/6) log h + h^(9/5+2eps)).
Here eps_D > 0 is the exponent of Theorem D and eps > 0 is arbitrary. For odd h, the extra width 4c0 tau*(h)^2 + 6h^2 + 4 of Proposition partial case (c) is O(h^2) and is absorbed in C h^2 ell (section 5). At a = a* and B = ceil(Lambda^theta*), this gives
 m_h <= C h^2 (log h)^theta* (loglog h)^C1, with theta* = 1.4967429 < 1.49675.
That is the near goal h^2 (log h)^(2-c) with c = 0.5032571 > 0.50325, and it beats T1 (C h^2 log^2 h (loglog h)^C). Do not round theta* to 1.4967, which understates it. The bound sum over light T of c_T = O(h) is no longer needed.

HYPOTHESES (each item gives its source note and audit file)

(H1) Completeness of the constant lists K2/K4. CLOSED, including the residual item (H1-T).
- CLOSED for every note listed in v3 proof section 2. Sources:
  - audit_constant_lists_sweep.md, which read most notes in full.
  - Sweep A (audit_constant_sweep_a.md): stride_menu, sea_row3_split, full_layout_junctions, point_counts_power_saving.
  - Sweep B (audit_constant_sweep_b.md): ap_hypothesis_henriot, ratio_graph_r_iv, block_sea_classification, rigid_layout_cross_block, sea_census_rigid.
  - Sweep C (audit_constant_sweep_c.md): t1_cost_decomposition, obstruction_table_completeness, two_moment_threshold_refinement, compatible_profile_threshold, plus filled_mod7_profile_cover and safe_triangle_pair_first_moment read in full.
  - Together these cover all 13 notes that audit_constant_lists_sweep.md had read only in part. No sweep found a failing step.
  - The complete K4 list is in proof section 4.
- (H1-T) CLOSED by Sweep T (the (H1-T) constant sweep, 14 November 2026; verdict correct_with_fixable_gaps; audit_constant_sweep_t.md): the T1-chain sub-inputs. The patches audit added these notes to the chain:
  - T6 sharper_polylogarithmic_threshold.md (2) (audit: sharper_polylogarithmic_threshold_independent_audit.md);
  - T7/T8 polylogarithmic_threshold.md and near_quadratic_threshold.md (audit: near_quadratic_independent_audit.md);
  - T3's inputs binary_boundary_one_label_separability.md Section 2 and mod7_inset_profile_cover.md Section 1 (audit: mod7_profile_independent_audit.md). All of these are in research_archive/2026-11-09.
  Each is audited for its own content. The question was only whether any of their steps uses a constant that the board changes: collars 2W -> 2W_h + 1, Lambda = 1 + log h -> log h, and W_0 = (log h)^3, with T1's rows, F, H and h0 unchanged. Sweep T read all five notes in full and found no failing step. T8's W is the board's W_h, and every collar in T7 and T8 (2W or 2W_h) is at most 2W_h + 1. The Lambda and ell changes affect constants only (K4 (h)). W_0 occurs in none of the five notes. The rows of R-d and T3's levels put both central rows strictly between the two sea levels, which is all that binary_boundary Section 2 needs, and mod7_inset Section 1 uses no sizes. T6 (2) is used at s = 2 only. The margins 4986, 4805 and 1257 are T3's own steps (filled_mod7 (9) and Section 4, Sweep C), not mod7_inset line 144. Sweep T's minor fixes are applied in section 2 (T-3', T-6, T-7/T-8) and K4 (h).

(H2) Steps with no second reader. NONE OPEN.
- The former (H2a) items, the N1 patches [G12]-[G16] and [G2], are discharged by audit_consolidated_board_v3_patches.md.
- The former (H2b) items, V3-1 to V3-5, are discharged by the same audit, with its minor fixes applied here [Z1]-[Z9].
- Theorem U (A-30) is audited in audit_uniformity_first_moments.md, and Theorem N1 (A-31) in audit_block_layout_n1.md.
- v4 adds two one-line steps, V4-1 and V4-2. Both are audited in the V4 audit (audit_consolidated_board_v4_steps.md; verdict correct_with_fixable_gaps), which found both correct. Neither is a new argument:
  - V4-1: the window separations required by (B10). This is a construction choice, and the only claim it makes is an O(h^2) width count. The V4 audit counts at most 100 windows and 100 gaps of 2W_h + 1 columns, so at most 50h^2 + 300 columns, and confirms that J5 applies with z inside the case (c) window (J5' in (B10)).
  - V4-2: A4 and D8 are counted in the O(h^(9/5+2eps)) term at the chosen (l, p), not at h^(1+o(1)). The V4 audit confirms it: Theorem U gives X_F <= Y_F^tau(l, p) for every chi, and every term is nonnegative, so X_A4 + X_D8 <= Y(l*, p*) <= 512 C h^(9/5+2eps). Nothing downstream needs A4 or D8 at h^(1+o(1)).

(H3) Audited inputs (proof section 2 gives each statement and file):
- P1-P3 (paper);
- A-1 to A-31, as corrected in their audits and in the sweeps;
- the T1 chain (CLAIM_LEDGER section A): T1, T2, T3 with its two inputs, T4, T6 and T7/T8. Each is audited link by link, and the chain is read end to end in audit_t1_chain_end_to_end.md and 2026-11-09/AUDIT_threshold_upper_bound.md. T7 and T9 are not needed by T1.
- T9 is not used, because h >= 10^10. T8's positional lemma for exceptional labels is replaced by P2. C1 (hidden_rectangles; self-checked only) is not used: validity goes through A-1 (V1)-(V5) and P1.

(H4) External results:
- Henriot, corrected Theorem 5 (MPCPS 157 (2014) 375-377), through A-18 and T6 (2);
- the PNT in progressions mod 5 and mod 20;
- quadratic reciprocity;
- tau(n) << n^eps;
- the product-form (asymmetric) local lemma (T2 Section 7, Theorem D (D4), Theorem E (E4)) [Z4].

No longer hypotheses (as in v3): N-1 (now Theorem N1); N-3 (now Theorem U); N-4 (the V2 steps, audited); (AP) and Q1 to Q5, with (AP) = Q5 at A-18/A-19, Q1 and Q2 at A-20, Q3 at A-23 and Q4 at A-24.
OPEN HYPOTHESES: none. (H1-T) is closed by Sweep T, and V4-1 and V4-2 by the V4 audit. No sweep or audit found a failing step, so no cell or step is held open for failure.
NOT PROVED: m_h = O(h^2), and any exponent below theta*.

## Proofs

consolidated_board_v4. It replaces consolidated_board_v3.md.

STATUS KEY
- P: paper.
- A9, A10, A11, A12: audited in rounds 9-12 (audit file named).
- R12+A: proved in round 12 and audited in round 13.
- SW: covered by a constant sweep. The sweeps are audit_constant_lists_sweep.md and Sweeps A, B and C (audit_constant_sweep_a.md, audit_constant_sweep_b.md and audit_constant_sweep_c.md). Sweep T is the (H1-T) sweep, audit_constant_sweep_t.md.
- N: proved, not audited.
- V3: a step of v3, audited in audit_consolidated_board_v3_patches.md.
- V4: a step written here. V4-1 and V4-2 are audited in the V4 audit, audit_consolidated_board_v4_steps.md.
- CIT: citation only.
Tags: v2 fixes keep [F1]-[F26], v3 fixes keep [G1]-[G20], and the new v4 fixes are [Z1]-[Z37] (fix ledger, section 7).

==================================================
0. COLOURING LAW (unchanged from v3)
==================================================
I keep (P3): for each light diagonal T and type tau, the uniform random proper B-colouring of G_T[tau] (heavy_diagonals_sharp Proposition 3, A-28). The alternative (TS) (truncated_additive_split, A-29) gives the same exponent only asymptotically. It is not adopted.

Theorem DC (degree_capped_colouring.md, audited against v2; restatement against v3 owed) and the relocation-price notes are not part of Theorem N. They appear only in remark (R-X).

==================================================
1. SPECIFICATION OF L***U
==================================================

(B0) PARAMETERS
- h >= h0 = max(10^10, h_PNT, h_D) [G1, Z24]. This implies h >= 424 (SAW Theorem 1, Pb, low_rows) and h >= 280 (two_filler Proposition 4).
- Lambda = log h, ell = loglog h, a = a*, B = ceil(Lambda^theta*). Stride 4 only.
- A = ceil(h/2), K = floor(h/2), W_h = floor((h-1)^2/4) + 1.
- Labels:
  - A label is (i, j) with 0 <= i < A and 0 <= j < K.
  - Its odd point is in row 2i + 1 and its even point in row 2j + 2, in one column (a double).
  - s = j - i and T = 2s + 1. There are q_h = AK labels.
- Locality (P3): every violation lies in 2W_h + 1 consecutive columns.
- S is the set of labels that are not T1-exceptional. The T1-exceptional set contains:
  - every label with a row outside [5000, h - 5000];
  - T1's O(h^(3/2)) exceptional labels (T3/T4);
  - T2's rows (2), r = s + t - u [G2]. There are O(1) such rows per profile. They are not vacuous, since 2F - L lies in [1987, 7485], so they hold O(h) labels.

(B1) HEAVY DIAGONALS [G3]
- kappa_T = |D_T|, with D_T as in stride_menu.
- T is heavy if kappa_T >= B/4, and light otherwise.
- Labels of S on heavy diagonals go to the single Theorem E instance (rule 1). Other heavy labels go to Proposition partial (R-d).
- Heavy labels are never in Bad_split, because classes exist only on light diagonals [Z2].

(B2) PRIMES [G4]
- l is prime in (1.04h, 2.08h] with l = +-2 (mod 5).
- p is prime in (40h, 80h] with p = 3 or 7 (mod 20). This gives p = 3 (mod 4) and p = +-2 (mod 5).
- Adm is the set of such pairs:
  - #L >= (1/2 - o(1)) 1.04h/log h and #P >= (10 - o(1)) h/log h;
  - gcd(p, 16l) = 1 (K3).
- K6-v3 step 1: (l, p) minimises Y(l, p) := sum over tau of sum over F in {A4-I.2, A4-II, B7, D8, D17, D18} of Y_F^tau(l, p), the pointwise bound of Theorem U.
- Optional refinement [Z3]: minimise instead the normalised sum Y' := sum over (tau, F) with Ybar_F^tau > 0 of Y_F^tau/Ybar_F^tau, where Ybar is the average over Adm. A term with Ybar = 0 vanishes at every pair.
  - min Y' <= 6 · 512 = 3072, so each Y_F^tau <= 3072 Ybar_F^tau, and A4 and D8 stay at h^(1+o(1)).
  - v4 does not need this. V4-2 counts A4 and D8 inside the total.
- kappa (global) and b_tau (per type) are arbitrary fixed integers, for example 0.

(B3) REGION TYPES (unchanged)
- tau = (iota, sigma) = (i mod 32, s mod 16), giving 512 types.
- r0 = 1 if iota is odd, and 3 if iota is even.
- y_P := 2 iota + 1 (mod 64), and [F2] tau_T := 2 sigma + 1 (mod 32).
- c_tau = 1 if T = 3 (mod 4), and 3 if T = 1 (mod 4).

(B4) CLASSES (v3 law, unchanged) [G5]
- For each light T and type tau, chi_{T,tau} is a uniformly random proper B-colouring of G_T[tau]:
  - G_T is the graph of stride_menu Proposition 1' (A-4);
  - G_T[tau] is G_T restricted to the slots of T with i = iota (mod 32);
  - the colourings are independent over (T, tau).
- The classes are the colour classes, and colour k has index k in {0, ..., B-1}.
- The degree in G_T[tau] is at most 2|D_T ∩ 32Z| <= 2 kappa_T < B/2, so proper B-colourings exist.
- Properties (Proposition 3 (a), (b); A-28):
  - every class lies in one (T, tau) and is G_T-independent;
  - K_max = B;
  - P(chi(u) = chi(v)) <= 1/(B - 2 kappa_T) < 2/B for distinct slots u, v of one (T, tau).
- (Xi1)-(Xi4) of uniformity_first_moments hold.
- The compatibility list of Proposition 3 cites threshold Proposition 1(a),(b) (the 16l rule) in place of heavy_light Proposition R [Z15]. Proposition R assumes p <= 40h, and only its lower bound p > 20h was ever used.
- Compatibility: no downstream step uses the greedy order or K_T. The only use of c_T was Theorem IV's dyadic group cost, which is replaced by the single group of (B8). This was checked by the text searches of heavy_diagonals_sharp and of its audit (J6, threshold_families, polylog Theorem IV/D).

(B5) PLACEMENT (rule L*_l, unchanged)
- Class k of diagonal s in type tau sits at t = rho_s + 16lk, with rho_s = p^(-1)(s - kappa) (mod 16l) and 0 <= rho_s < 16l.
- Label (i, j) of that class sits at slot n = i + pt + b_tau, in column 4n.
- [F1]:
  - rho_tau := iota + sigma - kappa + b_tau (mod 16), rho0 := rho_tau mod 4, kappa_tau := kappa - b_tau;
  - every label slot of R_tau has n = rho_tau (mod 16), and n(c) = kappa_tau (mod 16l).
- Since k <= B - 1, t < 16lB [G6].

(B6) FILLER LAYER (SAW*-shift, unchanged)
- T0_tau is the largest y <= h with y = y_P + 32 (if T = 3 mod 4) or y_P + 48 (if T = 1 mod 4), mod 64.
- D0 = h - T0_tau, in [0, 63]. T*_tau = T0_tau - 64 k_tau, with k_tau from Table J1*.
- Every deep column 4n of R_tau, margins included, that holds no label gets exactly one point, in row T*_tau - 24 + 8((n - rho0) mod 4).
- Shallow columns x != 0 (mod 4) hold (x, r0).
- Consequences:
  - T* >= h - 186, and fillers lie in [h - 210, h];
  - a filler at offset w lies in row y_P + 8(w + c_tau) (mod 64);
  - a hole has offset 0 and sits in row T* - 24;
  - every filler row is congruent to y_P mod 8. So every odd deep row is 1 mod 4 in row-3 types and 3 mod 4 in row-1 types. Sweep A checked all 512 types for k = 0, 1, 2, and this replaces the BH16-filler hypothesis of sea_row3 Corollary B [Z21].
- (Phi) adds at most 3 slots of the same sawtooth, more than 2W_h + 1 columns from every label.
TABLE J1* (unchanged; A-21, audit_consolidated_board.md). Entries are (o, kappa, j):
- h even, and row-1 types with h = 1 (mod 4): k = 0, no bad pair.
- h = 1 (mod 4), row-3 types:
  - k = 0 bad pairs (1,2,1) at D0 = 0, (3,1,1) at 4, (2,2,1) at 8, (0,3,1) at 12, (3,2,1) at 16, (1,3,1) at 20, (2,3,1) at 28 and (3,3,1) at 36;
  - k = 1 at D0 = 40 and 48; k = 2 at D0 = 56.
- h = 3 (mod 4), row-1 types: (2,3,3) at D0 = 4 and (3,3,3) at 12; k = 1 at D0 = 24, 32, 40 and 48.
- h = 3 (mod 4), row-3 types: the first list shifted by 2 (D0 = 2, 6, ..., 38); k = 1 at D0 = 42 and 50; k = 2 at D0 = 58.
- Every k = 0 row has a clean phase under (Phi), and every shifted row is clean at every phase. The shift is needed in 10 of the 64 odd-h cases [F17].

(B7) DESTINATIONS (first rule that fits) [G7; V3-1 with Z1]
1. A label on a heavy diagonal that lies in S goes to Theorem E (WE).
2. A label that meets R-a, R-b, R-c or R-d goes to Proposition partial (WP). These sets are deterministic and free of chi and of (l, p).
3. A label in Bad_split that is not in E_D goes to Theorem D (WD). A label of Bad_split in E_D goes to WP (R-g).
4. A label that meets R-e or R-f goes to WP.
5. Otherwise the label stays in its light region R_tau.
Set identity [Z1]:
- R-a ∪ R-b ∪ R-c ⊆ S^c ⊆ R-d = S^c ∪ D4, because:
  - R-a has rows 1, 2, 4 and 5;
  - R-c has 2i + 1 <= 300;
  - R-b has a row >= T* - 320 >= h - 506, or an odd row >= T* - 444 >= h - 630, both above h - 5000.
- So Y := Bad_split \ (R-a ∪ R-b ∪ R-c ∪ R-d) = (Bad_split ∩ S) \ D4.
- Rule 3 places Y \ E_D, and the N1 instance is R_D := Y \ E_D.
Criteria:
- R-a: i = 0. In row-3 types also i = 2, and j in {0, 1}.
- R-b: an endpoint row >= T*_tau - 320. In types with k_tau = 2, also an odd row >= T*_tau - 444 [F8]. This is O(h) labels: at most 2 odd label rows per type in the 124-row window, and at most 16 types [G8].
- R-c: 2i + 1 <= 300 (R2').
- R-d: every T1-exceptional label (heavy ones included), and every SAW Theorem 1(6) label (D4).
- R-e: the labels touched by an in-class R_IV edge with max(p_lambda, q_lambda) > h^(1/2)/32, or by an in-class R_FF^oo or R_FF^ee edge with |U'| > h^(1/2)/32.
- R-f: the counted families A4 (I.2, and II(1,-1) with Sigma != 0), B7, D8, D10, D11, D17 and D18.
- R-g: E_D, with |E_D| <= 4h^(2-eps_D).
Safety:
- J3 in hitting-set form (V2-1, A-27);
- Lemma M1 monotonicity (A-16);
- P2 accepts any edge set;
- Theorem D's two hypotheses survive intersecting with a fixed set.

(B8) BAD_SPLIT AND THEOREM D [G9]
- In each class, Bad_split is the shallow end of every monochromatic in-class edge of:
  - R_IV with max(p_lambda, q_lambda) <= h^(1/2)/32 (the q-end);
  - R_FF^oo and R_FF^ee with |U'| <= h^(1/2)/32, in each of the 4 filler rows;
  - R_FF^+, every pair with 0 < |Delta i| <= 210 [G10]. Since Delta i = 0 (mod 32) and 6 · 32 = 192 <= 210 < 224, there are at most 6 neighbours on each side.
- One weighted Theorem D group: D = {all light T}, |D| <= h, rho = 2/B >= Lambda^(-C'). It receives Y and places Y \ E_D.
- Hypotheses, in polylog_relocation_diluted's numbering [Z9]:
  - Theorem D (i), the independence hypothesis: Y ∩ T is a function of (chi_{T,tau}) over tau, so it is independent across T.
  - Theorem D (ii), the marginal hypothesis: P(f in Y) <= P(f in Bad_split) <= (2/B) times the sum over q in Q_T of c_q 1[q | u_f or q | delta'(f)]. This holds because, given the rest of the colouring, the colour of the designated end is uniform on more than B/2 colours.
  - c_q is counted with multiplicity [F14].
  - delta'(f) is affine in i within a type (ap Lemma 4).
- [G11] For R_IV, q is odd. For R_FF, the per-diagonal density is gcd(32, m)/m <= 32/|U'|. So kappa_FF <= 32 kappa_IV-type, and both are finite. R_FF^+ has q = 1 with c_1 <= 12.
- [F3, V2-3] Each event is a union of O(1) residue classes of i modulo lcm(32, q) <= 32q <= h^(1/2), which is inside ap Lemma 4 and Theorem D-weighted.
- The Theorem D event has probability >= 1/4 at every (l, p), by (D1)-(D3) and Markov (patches audit G.3).

(B9) BUFFERS AND ENDS (unchanged)
- Buffer row g(h) = h for h even, h - 1 for h = 1 (mod 4), and h - 3 for h = 3 (mod 4) (V2-2).
- Pieces Sea(r0, g) and all-g are each 2W_h + 1 wide, in the order of (P8): row-1 tail | Sea(1,g) | 256 row-1 types | Sea(1,g) | all-g | Sea(3,g) | 256 row-3 types | Sea(3,g) | all-g | Sea(1,g) | row-1 tail.
- Margins [F12]: 2W_h + 1 columns of pure SAW*-shift before the first and after the last label column, plus at most 3 slots for (Phi).
- End phases follow Table J1* and (P9).

(B10) GLUING [Z18; V4-1]
- Outside the windows the board is beta_z: row 1 at x < z and row h at x >= z. For even h, z is outside every window. For odd h, z is the switch of the case (c) WP block.
- Windows:
  - every WD and WE window lies right of z;
  - the WP instance is case (a) for even h, inside the row-1 tail, and case (c) for odd h, with switch z;
  - the rigid-chain window runs from the first Sea(1,g) to the last Sea(1,g).
- NEW (J5's hypothesis):
  - the rigid-chain window, the WP window and every WD/WE window are pairwise at least 2W_h + 1 columns apart;
  - every block B_k is a configuration on Z with no (V1)-(V5) violation that equals beta_z on the 2W_h-neighbourhood of its window U_k (for the case (c) WP block, on all of Z outside U_WP). For the rigid chain, the case (a) WP block and the WD/WE blocks, this needs U_k at least 2W_h + 1 columns from z, on the side given by their tails. For odd h, the WP block is Proposition partial (c) with its own switch taken as z. It equals beta_z outside U_WP := [s_1 - 2W_h, s_4 + N_4 - 1 + 2W_h], and the paper proves it obstruction-free on all of Z, so z lies inside U_WP. U_WP is one window; U_1, ..., U_4 are not separate J5 windows.
- Gluing is by J5 (A-13) in the form J5': windows pairwise more than 2W_h columns apart, and every block equal to beta_z on the 2W_h-neighbourhood of its window. J5's proof gives J5' word for word. full_layout_junctions line 145 already reads case (c) this way ('Case (c) supplies its own z, which is the global z'), and the J5 audit accepted that reading (V4 audit). The board is truncated to columns 1..m.
- V4-1: there are at most 2 · 49 + 2 windows, so the added gaps cost O(h^2) columns (section 5). Audited (V4 audit): at most 100 windows and 100 gaps, so at most 50h^2 + 300 columns.

BLOCK LAYOUT OF WD AND WE (Theorem N1, patched; A-31 and audit_consolidated_board_v3_patches.md)
- Profiles pi = (L, F, H, g) as in filled_mod7 (1)-(3), (7)-(9). Sea: s_pi(x) = F if 7 | x, L if chi_7(x) = -1, and H if chi_7(x) = 1.
- [G12 with Z6] The profile map is T2 Section 1's:
  - L is the unique odd L in [1, 14] with L = a_e (mod 7);
  - a mixed-residue label has g = (b - a)/5 (mod 7);
  - a zero-residue label gets a fixed nonzero g, for example g = 1, and goes to a separate zero-residue block;
  - since b - a = T, the zero-residue labels are exactly those on diagonals with 7 | T, so the block type is a function of the diagonal and uses neither chi nor (l, p).
- There are 42 mixed and 7 zero-residue profiles, so 49 blocks per instance.
- [G13 with Z32] Classes inside a block:
  - the dyadic classes (2^(k-1), min(2^k, Lambda^3)] of v_pi, then coarse groups (W_k, W_{k+1}] with W_0 = (log h)^3 and W_{k+1} = W_k^(4/3);
  - Theorem E uses Lambda = 1 + log h and W >= Lambda^3. The ratio between the two is at most (1 + 1/log h)^3 <= 1.14 at h = 10^10, and (E5) needs only W >= c Lambda^3, so the change affects constants only.
- BL1: each class c has N_c >= |c| slots and an injective centre map X_c that avoids T2's events, with T2's slot counts (T1 (8), (E4)-(E5), (D4)). T2's counts apply to both block types (T2 (3), (10)).
- BL2: the core is K_c = [x_c, x_c + 7N_c - 1] with 7 | x_c. Column x_c + 7X_c(e) holds the two points of e, and every other column x holds s_pi(x).
- BL3: consecutive cores are separated by at least 2W_h + 1 columns of s_pi.
- BL4: right collar P (2W_h + 1 columns of s_pi), then Phi (2W_h + 1 columns, with H at multiples of 7), then C_H, ..., C_{h-1} (2W_h + 1 columns each), then row h. The left collar is the mirror image. There are at most 197 stages.
- BL5: row h | left collar | cores and separations | right collar | row h, with window U = [a, b].
- BL6: as in (B10).

ORDER OF RANDOM CHOICES (K6-v3, unchanged)
1. (l, p) is the deterministic minimiser over Adm (B2).
2. chi is drawn from the product law (B4), conditioned on the Theorem D event. The two hypotheses hold at every (l, p).
3. The WE and WD centre maps come from T2's local lemma and never use (l, p).
Theorem U holds pointwise, so X_F <= Y_F^tau(l, p) for every chi. No Markov step is needed for the U bound.

==================================================
1b. STEPS AND CITED THEOREMS
==================================================
V3-1 (audited, with [Z1], [Z2]): first-fit gives a partition. Rules 1 and 3 receive only labels of S, and Y = (Bad_split ∩ S) \ D4. Removing a deterministic set keeps Theorem D (i) and (ii). J3 needs only that Bad_split ∪ R-e ∪ R-f leave R_tau, whichever window receives them.

V3-2 (audited; fixes from audit_uniformity_first_moments.md, re-derived in audit_consolidated_board_v3_trace.md) [Z11]:
- Pointwise bound: X_F(Xi, kappa, b; l, p) <= Y_F^tau(l, p) := lam_F Phi_F #{sigma in Sigma_F^tau realisable at (l, p)}.
- Averages over Adm:
  - A4 I.2 and A4 II: h^(1+o(1));
  - B7: O(h^(9/5+eps) log h);
  - D8: h^(1+o(1));
  - D17: 2h|Sigma_tau|/#P, with |Sigma_tau| <= 4 · 4 · h^(o(1)) · sum over Q < 3h of |E0(Q)| [G17];
  - D18: 4h|Sigma_tau|/#L.
  - min over Adm of Y <= average <= 512 · C h^(9/5+2eps).
- U1: |DM| <= |Dx|/4 + |Di| and |Dn| <= |DM| + |Ds|, both below h^2/8 + 3h/2 < (1.04h)^2 = 1.0816h^2 < (40h)^2. So each nonzero difference has at most one prime factor in each range.
- D18 constant: h^2/8 + h/2 + 1.
- B7: r0 is fixed by the type, so the factor 2 goes.
- [G18]: shape counts move from (20h, 40h] to (40h, 80h] by superset.
- D11 is deterministic, with O(h^(9/5+eps)) labels.
- [G19]: in V2-7, L2's point determines L2 (U1(b)).
- Lemma U3 is used only for in-subclass objects.
- Law coverage: Theorem U covers every (l, p)-free law with (Xi1)-(Xi3), including the uniform proper B-colouring of (B4) (U audit). (Xi4) is used only by the deterministic exclusions (for example b != 0 in I.2), and (B4) gives it.

V3-3 (audited): N1 runs as one Theorem E instance (R_E = heavy labels in S) and one Theorem D instance (R_D = Y \ E_D). Claims (a)-(f) are per block. Claim (b) uses only that the classes partition R_{I,pi,type}.

V3-4 with V4-2 (n_rel) [Z3]:
- O(h): R-a; R-b with the k = 2 extension; R-c; D1; D9; rows outside [5000, h - 5000]; T2's rows (2).
- O(h^(3/2)): D4; D10 (constant about 5.4e4); T1's exceptional labels.
- O(h^(9/5+2eps)): A4, B7, D8, D17 and D18, at the chosen (l, p), as the sum Y; plus D11, which is deterministic and not part of Y, with O(h^(9/5+eps)) labels. V4-2: A4 and D8 are counted here, because minimising the sum bounds each term only by the total. Their average is h^(1+o(1)).
- O(h^(11/6) log h): R-e, bounded over all pairs, so for every chi.
- E_D: <= 4h^(2-eps_D). The patches audit's count adds O(ell) h^(1+8eps), which is dominated.
- So n_rel = O(h^(2-eps_D) + h^(11/6) log h + h^(9/5+2eps)), since 9/5 + 2eps < 11/6 for small eps. Then c0 n_rel tau*(h)^2 = h^(2 - min(eps_D, 1/6) + o(1)) = o(h^2).

V3-5 (audited) with V4-1 (audited in the V4 audit): width, section 5.

CITED THEOREMS (statements as audited)
- Theorem N1 (block_layout_n1.md; A-31, audit_block_layout_n1.md; patches re-read in audit_consolidated_board_v3_patches.md). Every WD/WE block satisfies:
  - (a) every column is a singleton or a double, and the doubles are the label columns;
  - (b) the label-to-column map is injective;
  - (c) the block is constant row h outside its window;
  - (d) with row-h tails there is no (V1)-(V5) violation;
  - (e) J5 glues it;
  - (f) K8'.
- [G14 with Z5, Z6] The argument for claim (d) runs in a block whose centre maps avoid T2's events. The sea alone has none (filled_mod7 Section 3), one label has none (Section 4), and with two or more labels every non-allowed triangle is an event.
  - The only three-black tilted rectangles are T2's allowed triangles: a high-sea root and two mixed-residue labels.
  - By T2 Section 2 (column residue 5, row residue 4) and (4) (parity), W lies in a low-sea column, holds s_pi = L inside K_c^+, and has L's parity. So the triangle is parked (V2).
  - No two allowed triangles on the same two labels share W.
  - Two allowed triangles at one W that share a black corner have a 4-cell black symmetric difference. It is a mixed quadruple (a T2 four-cell event) or a fully black rectangle, which would contain a forbidden triple. Either way the placement avoids it.
  - Every other V3 pair is a six-cell event on 3 or 4 labels (T2 (15)-(17)).
- [G15] E_J depends only on X_c restricted to J and on s_pi with F at every other period-zero column. So deleting labels never unparks a triangle.
- [G16] Lemma TR': adjacent rows form a chain, and j(j+1) is never a square. Lemma TR covers Phi | C_H. Lemma C is unchanged.
- Theorem U (A-30; audit_uniformity_first_moments.md): V3-2.
- heavy_diagonals_sharp Proposition 3 (A-28, audit_heavy_diagonals_sharp.md).
- heavy_light Theorem 1(b) (A-5, audit_heavy_light_split.md): H_d(B/4) <= C_a 4^a h Lambda^(E(a)-1) B^(-a).
- Theorem E (t1_cost_decomposition (E1)-(E5), A-6, audit_t1_cost_decomposition.md): cost C(Delta h Lambda^2 ell^C1 + h^2 ell). Lemma AP, AR, Theorem B, Propositions C/D, Corollary F and Remark G are not used. If Lemma AP were ever adopted, it would need h0 >= 1.3e13 and R-d widened to rows outside [2e5, h - 2e5] [Z33].
- Weighted Theorem D (polylog_relocation_diluted, A-16; ap_hypothesis_henriot Theorem D-weighted, A-18, audit_ap_hypothesis_henriot.md): cost C(rho kappa |D| h Lambda^2 ell^C1 + h^2 ell), with |E_D| <= 4h^(2-eps_D). The note's statement line 'h^(2-eps)' should read 4h^(2-eps) [Z22].
- V2-1 to V2-9 and Lemma S1L (A-27).

==================================================
2. HYPOTHESIS AND DEPENDENCY LIST
(input | source | statement used | status | audit file)
==================================================
PAPER
- P1 | sec2_prelim.tex, sec5_threshold.tex | Lemmas mixedeq, reduction, rival, sea, chain, diff and criterion, and the girth lemmas | P.
- P2 | sec5_threshold.tex | Proposition partial (a), (c): n edges in width c0 n tau*(h)^2 | P.
- P3 | sec5_threshold.tex | locality 2W_h + 1 | P.

T1 CHAIN (research_archive/2026-11-09; CLAIM_LEDGER section A) [Z4]
- T-1 | two_moment_threshold_refinement.md | slot counts (8) | THM-EXT; two_moment_threshold_independent_audit.md; SW (Sweep C).
- T-2 | full_problem_push/safe_triangle_pair_first_moment.md | Section 1 map, Section 2 allowed triangles, (2), (3), (4), (10), (14)-(17), Section 7 local lemma | THM-EXT; safe_triangle_first_moment_independent_audit.md, safe_triangle_pair_third_audit.md; SW (Sweep C, all).
- T-3 | filled_mod7_profile_cover.md | profiles, one-label substitution, hole-choice collars, h >= 10^10 | THM; filled_mod7_independent_audit.md; SW (Sweep C, all).
- T-3' | binary_boundary_one_label_separability.md (Section 2), mod7_inset_profile_cover.md (Section 1) | inputs of T3 | audited; mod7_profile_independent_audit.md; SW (Sweep T). mod7_inset Sections 2-4 are not used: their margins 41/82 and h >= 1000 are for its own 18 profiles only.
- T-4 | compatible_profile_threshold.md | exceptional roles, O(h^(3/2)) exceptional set, (5) for higher arity | THM-EXT; compatible_profile_threshold_independent_audit.md; SW (Sweep C).
- T-6 | sharper_polylogarithmic_threshold.md (2) | two-factor divisor moment (T4, (E3)), used at s = 2 only | audited; sharper_polylogarithmic_threshold_independent_audit.md; SW (Sweep T). For s < 1 the exponent is max(3^s - 1, 2(2^s - 1)) = 2(2^s - 1), so (2) with beta(s) = 3^s - 1 must not be cited at s = a*. a* enters through heavy_light Theorem 1(b), which does not cite T6.
- T-7/T-8 | polylogarithmic_threshold.md, near_quadratic_threshold.md | used: the black-support classification (T8 introduction, Section 4), the LLL arithmetic (T8 Section 3, arity <= 4, which T2's six-cell events meet) and W = W_h; not used: T8 Sections 1-2 (counts with T), Section 5 (cover) and Section 6 (small heights), and T7 Sections 1-6 | audited; near_quadratic_independent_audit.md; SW (Sweep T).
- Not used: T9 (small heights; h >= 10^10); T8's positional lemma (replaced by P2); C1 (validity goes through A-1 and P1); joint_height_width_counting.md.
- End-to-end reading: audit_t1_chain_end_to_end.md, and earlier 2026-11-09/AUDIT_threshold_upper_bound.md.

AUDITED INPUTS (with the sweep that closed (H1) for each)
- A-1 | block_sea_classification | criterion (V1)-(V5); Theorems 1, 2 | A9, audits_rigid_mixed_sea.md | SW (Sweep B, all).
- A-2 | rigid_layout_cross_block | Theorem C, Proposition R, Theorem 2(e) | A9, audits_rigid_mixed_sea.md | SW (Sweep B). Theorems 4(a) and 5 are not adopted: the 2-adic rule is replaced by K2 and threshold Proposition 1(b) [Z26].
- A-3 | mixed_quadruples_blocks | Theorems 1-4 | A9, audits_rigid_mixed_sea.md | SW (constant sweep).
- A-4 | stride_menu | Proposition 1' (G_T), Lemmas 2-4 | A9, audits_stride_menu_and_gamma.md | SW (Sweep A, both derivations).
- A-5 | heavy_light_split | Theorem 1(b) | A9, audit_heavy_light_split.md | SW.
- A-6 | t1_cost_decomposition | Theorem E (E1)-(E5) | A9, audit_t1_cost_decomposition.md | SW (Sweep C, all).
- A-7 | sea_row3_split | Theorem A ((H1)-(H4)), Corollary B (Proposition C not used; explanatory) | A9, audit_sea_row3_split.md | SW (Sweep A). Corollary B is read with the SAW*-shift fillers (B6) and the mod-16 rule of K2 for M2a [Z21]. Proof 2(ii), case e = 2, should read: 'in every split P2 lies in row 5 and is deep, which (H2) excludes' [Z20].
- A-8 | sea_census_rigid | B1-B4 | A9, audit_sea_census_rigid.md | SW (Sweep B). The in-class parts of B3 and all of B4 hold for any k >= 3 without (Hnu). v4 uses k = 5: R_IV^(5) for odd-odd pairs and the empty set for even-even pairs [Z27].
- A-9 | deep_layer_sawtooth | SAW Theorem 1 (1)-(6), Lemmas 2-4, Proposition 5 | A9, audit_deep_layer_sawtooth.md | SW.
- A-10 | ratio_graph_r_iv | Lemma 2, Corollary 3, Theorem 4 | A9, audit_ratio_graph_r_iv.md | SW (Sweep B). Corollary 3(b) is certified for R_IV^(3) and R_IV^(4) only. For R_IV^(5), bipartiteness is undecided. The upper bound does not use it. Theorem 1's computer certificate is not cited [Z25].
- A-11 | threshold_families_random_prime | L*_l; Propositions 1(a)-(d); Theorems 2, 3; Proposition 5 | A9, audit_threshold_families_random_prime.md | SW.
- A-12 | saw_residual_families | SAW*; Feo kill; (i); (ii-a,b); (iii-b) | A9, audit_saw_residual_families.md | SW.
- A-13 | full_layout_junctions | J1-J5, (P7)-(P9) | A9, audit_full_layout_junctions.md | SW (Sweep A). J3 is read as 'label columns (black points, W, p and q)', and |Lambda| <= 7 stays [Z19]. J5 is used in the form J5' of (B10): each block equals beta_z on the 2W_h-neighbourhood of its window. For the case (c) WP block, which contains z, this holds by construction (V4 audit; full_layout_junctions line 145).
- A-14 | point_counts_power_saving | Theorem A, Corollaries B, C (Theorem D rests on Heath-Brown; cross-check only, not used) | A9, audit_point_counts_power_saving.md | SW (Sweep A).
- A-15 | v3_and_cross_block | Theorems A-C, Propositions D-F | A9, audit_v3_and_cross_block.md | SW.
- A-16 | polylog_relocation_diluted | Lemma M1; Theorem D; Lemma IV | A9, audit_polylog_relocation_diluted.md | SW.
- A-17 | additive_class_split | Lemmas 1, 2, 4 | A9, audit_additive_class_split.md | SW.
- A-18/A-19 | ap_hypothesis_henriot | Lemmas 1-4, (AP) = Q5, Theorem D-weighted | A10, audit_ap_hypothesis_henriot.md | SW (Sweep B). Fixes:
  - Lemma 1 needs I ⊂ [-A0 h, A0 h], with I extended to length h by positivity. Every v4 use has I ⊂ [0, A).
  - Lemma 3(a): 'mod 16' reads 'mod 32 (v4 types)'. The bounded modulus m0 divides 224, and q' <= 7h^(1/2) <= h^(1-eta) [Z23, Z24].
- A-20 | two_filler_row_lemma | Lemma 1, Corollary 2, Theorem 3(a), 3(b) shapes, Proposition 4 | A10, audit_two_filler_row_lemma.md | SW.
- A-21 | consolidated_board | Lemma J1*, Table J1*, Lemma L-adic, Lemma FF', Lemma 3L1F-a, K1-K4 | A10, audit_consolidated_board.md | SW.
- A-22 | deep_layer_bh16 | A1-A3, A5 | A10, audit_deep_layer_bh16.md | SW.
- A-23 | three_label_one_filler | Lemma N, Theorem Q3 | A11, audit_three_label_one_filler.md | SW.
- A-24 | low_rows_row3_types | Lemmas LR, S, N; Q4 (a), (c), (d), (e), and (b) for row-3 types | A11, audit_low_rows_row3_types.md | SW.
- A-25 | obstruction_table_completeness | Theorem K, Lemma Q3, sections 0-6 | A11, audit_obstruction_table_completeness.md | SW (Sweep C, all). Theorem K is stated for L***. Its constant uses are relative to T* and to the mod-16l rule, so they carry over. Table T is read through the merged table of section 3 [Z30]. Lemma Q4 is not used.
- A-26 | constant lists | K2 grep, K4, R2' sufficiency | A11, audit_constant_lists.md; superseded as a method by the sweeps.
- A-27 | consolidated_board_v2 | V2-1 to V2-9, Lemma S1L | A12, audit_consolidated_board_v2.md.
- A-28 | heavy_diagonals_sharp | Lemma 1, Theorem 2, Propositions 3 and 4(a), (b) | A12, audit_heavy_diagonals_sharp.md.
- A-29 | truncated_additive_split | NOT USED (no v4 remark cites Proposition O) | A12, audit_truncated_additive_split.md.
- A-30 | uniformity_first_moments | Lemmas U1, U2, Theorem U (pointwise), Lemma U3 (in-subclass) | R12+A, audit_uniformity_first_moments.md [Z8].
- A-31 | block_layout_n1 | Theorem N1, Lemmas TR, TR', C, RL | R12+A, audit_block_layout_n1.md; patches audited in audit_consolidated_board_v3_patches.md [Z8].
- V3-1 to V3-5 | consolidated_board_v3 | section 1b | V3, audit_consolidated_board_v3_patches.md; dependency trace audit_consolidated_board_v3_trace.md.
- V4-1, V4-2 | this note | (B10) separations; A4/D8 counted in the 9/5 term | V4; audited in the V4 audit (audit_consolidated_board_v4_steps.md; verdict correct_with_fixable_gaps). One line each; no new argument.

EXTERNAL: Henriot's corrected Theorem 5 (through A-18 and T6 (2); its audit read the erratum); the PNT mod 5 and mod 20; quadratic reciprocity; tau(n) << n^eps; the product-form local lemma. For the sharpness remark only: the fundamental lemma of sieve theory (dimension 1/2) and Mertens' theorem (theorem numbers not checked).

NOT AUDITED, NOT LOAD-BEARING: census_large_heights (P1)-(P3), (R1)-(R6); census_consolidated_board; pair_families_dp_colouring. relocation_price_floor, degree_capped_colouring, relocation_price_exponent (audit_relocation_price_exponent.md) and higher_arity_true_counts (audit_higher_arity_true_counts.md; its Proposition 5 has a serious gap that the headline does not use) are audited but not used by Theorem N.

==================================================
3. MERGED OBSTRUCTION TABLE
(cell | verdict | source | status | labels hit, destination)
E = impossible; C = counted and relocated; W = internal to a certified window. Table T names are in brackets. Table T's own counts are superseded by this table [Z30].
==================================================
WINDOWS AND CHAIN
- W1 [WP] | W | P2 | P.
- W2 [WD] | W | N1 (a)-(e) with [G12]-[G16], [Z5], [Z6] | R12+A, patches audit.
- W3 [WE] | W | same | R12+A.
- W4 [X] a violation meeting two windows | E | J5 in the form J5' of (B10) [Z18, Z36] | A9, V4-1 (width only).
- W5 [SW] the switch | E | Lemmas chain and rival | P.
- L1 two regions, or a label point with a buffer point | E | table section 1(c), [F12] | A11.
- C2/L2 SAW*-shift gap with sea | E | SAW Theorem 1 (3), (4'); census (C2), (R6) | A9, A10. Covers T4 (FFF) and M8 [audit_v2 issue 4]. Needs h >= 424.
- E1/L3 SAW*-shift with a Sea(r0,g) seam | E | J1*; census (C3) | A10.
- C1/L4 buffers, chains, all-g, tails | E | J2 (h >= 10, g even, g = 0 mod 4 for odd h), Lemma sea, V2-2 | A9, A12.

LABEL ONLY
- A1 [T1] LLL and LLLL right angles | E | rigid Theorem C, Proposition 1(b) | A9 | 0.
- A2 [R2] (o,e) rival pairs | E | in class: (Xi4) and Theorem C; across classes |t| < 2h < 158h | A9, A11 | 0.
- A3 [D-4L] I.1, II(1,1), II(-1,-1), II(1,-1) with Sigma = 0, and 3- or 4-class quadruples | E | mixed_quadruples Theorems 1, 2, 4; Proposition 1(c); A-24(d) | A9 | 0.
- A4 [D-4L] I.2, and II(1,-1) with Sigma != 0 | C | threshold Theorems 2, 3; Theorem U | A9, R12+A | inside O(h^(9/5+2eps)) at the chosen (l, p), with average h^(1+o(1)) [Z3]; to WP.
- A5 cross-block A2 pairs | E | Lemma 4(a), Proposition 1(d) | A9 | 0.

LABEL AND SEA
- S0 two shallow corners | E | (F1), sea_row3 Theorem A | A9 | 0.
- B1 [S2, S9] X1, X2 | E | block_sea Theorem 1; sea_row3 A, Corollary B (SAW*-shift reading); v3 A(i) | A9 | 0.
- B2 [S1, S2] Pa, and Pb with two labels | E | v3 A(i) | A9 | 0.
- [S6-S8] E as an end | E | v3 A(ii); L-adic (i) | A9, A10.
- [S10] SLF-Pc parked; with G a base E (a = 0 mod 4) | A9 [audit_v2 issue 4].
- B3 [V3 SLL/SLL] | E | v3 A(iii) | A9 | 0.
- B4 [M0-M3] | E | block_sea Theorem 2; sea_row3 A(iii), Corollary B; odd deep rows congruent mod 8 (Sweep A: 512 types, k = 0, 1, 2) | A9 | 0.
- B5 [M6] in-class ee M2c | E | B3 (C1) | A9 | 0.
- B6 [M4] in-class oo M2c (R_IV) | C | B4, Theorem IV, Lemma IV, (AP), (B4) law | A9, A10, A12 | Bad_split to WD; heights > h^(1/2)/32 to WP (R-e), O(h^(11/6) log h).
- B7 [M5] cross-class M2c | C | Proposition 5, Corollary B, Theorem U | A9, R12+A | O(h^(9/5+2eps)); WP.
- M7' [M7] M2c with the filler shallower | E | rows | A11.
- M9 low M2c, row-3 types | E | (L2), (L3) | A11.
- B8 [R1] rival pair with a shallow point | E | Lemma rival, J1(e) | P, A11 | 0.
- [S13] row-3 types, W in rows 1-2 | E | sea_row3 A(ii) | A9.

LABEL AND FILLER
- D1 S2 near band | C | Theorem 1(2b) | A9 | O(h); in R-b.
- D2 T1 and CE | E/C | Theorem 1(5), Lemma 2 | A9 | to WP (R-d).
- D3 T2 | E | Proposition 5, i mod 32 | A9 | 0.
- D4 [D-1L3F diagonal] | C | Theorem 1(6), cutoff y_D - 156 >= T* - 180 | A9 | O(h^(3/2)); WP (R-d).
- D4' [D-1L3F side] | E | V2-4 with the R-b extension, Lemma S1L | A12 [audit_v2 issue 3]. Table T's row holds only under R-b with the k = 2 extension [Z28] | 0.
- D5 [T2, T5] Feo, SAW-S3, SAW-S3-low | E | SAW* kill, v3 Proposition E, Q4(a) | A9, A11 | 0.
- D6 FFe, Fee, Foo | E | v3 Theorem B, L-adic (ii) | A9, A10 | 0.
- D7 FFo | parked (hole vertex) / E (label vertex, X = 320 >= 234) | A9, A10 | 0.
- D8 [V3 cross-class] family (d) | C | Proposition D; Theorem U | A9, R12+A | inside O(h^(9/5+2eps)), average h^(1+o(1)) [Z3]; WP. Empty for h <= 5117 [Z29].
- D9 [S3] Pb, odd label and base filler | E after R2' | V2-6 | A12 | inside R-c.
- [S4, S5, S11, S12] | E | A9, A10.
- D10 [R3] (e,F) rival pairs | C | saw (i), H0 = 210 | A9, A11 | O(h^(3/2)); WP.
- D11 [M7] M2c, one label and a filler | C, deterministic | saw (ii-a,b), point_counts Theorem A, Corollary C(2) | A9, R12+A | O(h^(9/5+eps)); WP.
- D12 homogeneous Fo/Fo, Fe/Fe with d > 0 | C | R_FF^+ with |Delta i| <= 210 | A9, A11 | WD (q = 1).
- D13 the same with d < 0 | C | saw (iii-b), Theorem IV, Lemma FF', (AP), [G11] | A9, A10, A12 | WD; |U'| > h^(1/2)/32 to WP.
- D14 [D-2L2F] | E | parity; saw (iii-b); two_filler Proposition 4 (h >= 280); v3 F1, S5 | A9, A10 | 0.
- D15 in-class 2L2F with df != 0 | E | two_filler Corollary 2 | A10 | 0.
- D16 cross-block F1, F2, F3 with n_y >= 0 | E | v3 Proposition F; two_filler Lemma 1 | A9, A10 | 0.
- D17 cross-class F3, n_y <= -1, odd-odd, df = 0 | C | two_filler Theorem 3(a); point_counts Theorem A; Theorem U | A10, R12+A | O(h^(9/5+2eps)); WP.
- D18 the even-even analogue | C/E | Theorem 3(b) shapes, V2-7 with [G19], Proposition 4; Theorem U | A10, A12, R12+A | O(h^(9/5+2eps)); WP.
- D19 {F,o,o,o} | E | Lemma 3L1F-a; Lemma N | A10, A11 | 0.
- D20 [D-3L1F] | E | Theorem Q3; Lemma N; Lemma Q3; needs [F1] | A11 | 0.
- D21 row-3 deep-only with p, q or W in rows 1-2 | E or inside A3/A4/D10 | Q4 (a), (c)-(e) | A11.
- D22 V3 completeness | E except D8 | v3 Theorem C; table section 4 | A9, A11 [audit_v2 issue 5: 'h < 2560' reads 'h <= 5117'].
- [V1], [V2], [V3 cross-type], [R4], [D-4F] | E | as in v3 | A9, A11.

JUNCTIONS AND EXCEPTIONAL SETS
- E2: J2-J5 | A9, with (B10) [Z18].
- E3, E4: Theorem E and D ends | N1(c), (e) | R12+A.
- E5: Corollary B exceptions, near band, low rows, T1-exceptional (with T2 rows (2)) | O(h^(3/2)); WP.

OPEN CELLS: none. Theorem K (A11) lists obstruction kinds. Its list does not depend on the destination order, and it uses the class law only through (Xi4) and K_max = B [Z10]. The in-class E cells use only (Xi4), at most B classes per (T, tau), and the mod-16l rule.

==================================================
4. THE K-LISTS
==================================================
- K1: [F1].
- K2: complete for every note of section 2. The (H1-T) notes contain no 2-adic rule (no 2^nu, mod 8/16/32 or stride use). The sweeps cross-checked every 2^nu, (Hnu) and 2^r use. Each one is either K2-listed or in a part v4 does not use:
  - SAW 4(b) -> threshold Proposition 1(d);
  - sea_census B1 -> Proposition 1(c)/4(c);
  - rigid Theorem C and Proposition R -> Proposition 1(b);
  - v3 A(ii) and Fee -> L-adic;
  - BH16 A3 and Feo -> mod 16 with constant kappa_tau;
  - J4 and the widths -> 16l;
  - sea_row3 M2a -> mod 16.
  - Not used: sea_census thresholds and L(k) settings, t1 AR regions/Lemma AP/Proposition C, rigid Theorems 4(a) and 5, BH16 rule B.
- K3: admissible-pair count (A10).
- K5: buffer rows by J1* and J2.
- K6: K6-v3, with the optional normalised minimiser [Z3].
- K7: Theorem IV weights: R_IV by Lemma IV, with large-lambda count p < 21 be^3 [F15]; R_FF by Lemma FF' with [G11]; R_FF^+ with q = 1; cutoff h^(1/2)/32.
- K8': Theorem N1(f), as patched.
- K9: LAD not adopted. K10: additive Theorem 5 not adopted.

K4, COMPLETE. Format: note | step | constant: needed -> v4 value | margin | source of check. H = holds as written or a fortiori; R = holds by a K2/K4 replacement. No entry fails.

(a) v4-specific constants [Z13]:
- heavy_diagonals_sharp Proposition 3(a),(b) | heavy threshold B/4 -> degree <= 2kappa_T < B/2, P(mono) <= 1/(B - 2kappa_T) < 2/B | factor 2 | H; constant sweep (checked for B <= 200).
- width | K_max = B, t < 16lB | exact | H.
- Theorem D | rho = 2/B >= Lambda^(-C') | polylog | H.
- ap Lemma 4 / Theorem D-weighted | cutoff h^(1/2)/32, so the modulus lcm(32, q) <= 32q <= h^(1/2) | exact by design | H.
- R_FF^+ | 6 neighbours on each side: 192 <= 210 < 224 | exact | H.
- Theorem D | one group, |D| <= h | H.
- U1 | h^2/8 + 3h/2 < (1.04h)^2 | ratio 1.0816/0.125 | H.
(b) l-range uses [Z12]. These are the thin margins.
- threshold Proposition 1(c) | |5Sigma - S| < 5h/152 + h = 1.033h < l | 1.033h vs 1.04h: THIN | H.
- Lemma L-adic (i) (also v3 A(ii), both even) | |2a - f| < h/35 + h = 1.029h < l, with |a| < h/70 from |Dn| > 39h | 1.029h vs 1.04h: THIN | H.
- rigid Theorem 2(e) | under v4 spacing (|DM| >= p > 40h), l > (1 + 10/614)(h - 1), and (1 + 10/614)(h - 1) < 1.0163h, about 1.016h (Sweep B). The earlier sweep recorded 1.035h | 1.016h vs 1.04h. Sweep B script: max |b|/(h - 1) = 1.0125 at h = 801 and 1.0063 at h = 1601 | H.
- U1, threshold Theorems 2-3, V2-7 | a nonzero integer below (1.04h)^2 has at most one prime factor in (1.04h, 2.08h] | H.
- obstruction_table 1(d) | 16l > h | 16.6h | H.
(c) Filler window and near band (deep_layer_sawtooth, saw_residual, J1*):
- fillers in [h - 210, h], T* >= h - 186 | D <= 63/114/{184,186} for k = 0/1/2 | H.
- SAW Theorem 1 hypothesis | T* - 24 > (h + 3)/2 -> h >= 424 | h0 = 10^10 | H.
- Theorem 1(3) Pb, two fillers | 2(h - 210) - 3 >= h + 1 iff h >= 424 | H.
- Theorem 1(3) Pc and 1(4') | relative heights only | H.
- Theorem 1(6) diagonal | y_D - 156 >= T* - 180 > T* - 321 | 141 rows | H.
- Theorem 1(6) side (D-1L3F) | y_L < T* - 72 - 2D: D <= 114 needs T* - 300 (kept rows <= T* - 321, margin 21 rows); D in {184, 186} needs T* - 440/T* - 444, supplied exactly by the R-b extension | R (V2-4, S1L).
- SAW Lemma 4(a) | p = +-2 mod 5, |Di| < h/2 < 40h | H.
- SAW Proposition 5 | i mod 16 -> mod 32 | H.
- SAW* | T* >= h - 63, H0 <= 87 -> h - 186, 210 | R.
- saw (i) | j <= H0 = 210; (2/3)(H0 + 1)^(3/2), about 5.4e4 h^(3/2) | R (D10).
- saw (ii-a,b) | residues mod 64; 4 filler rows per type, Q <= h | H.
- saw (iii-a) | lattice mod 2^(nu+1) -> mod 16 | R (K2).
- saw (iii-b) | d = 0 mod 8 -> 0 mod 16; d > 0: |Delta i| <= 210 | R.
- J1 -> J1* | g > (h + 1)/2, 2g - 3 > h, T* - 24 > 5, row differences 8m with |m| <= 3, j <= 3 | H.
- Lemma J1* | h - c <= 87 -> <= 210, table for k = 0..3 | H.
(d) Cross-class distances (v3_and_cross_block, two_filler, threshold, uniformity):
- (N) gap > 76h -> > 158h; |Dx| >= 4(p - A) > 158h | H.
- A(ii) both odd | |a| < h/158, |2a - f| < 3h < p | H.
- A(iii) | 5h/2 < 160h | H.
- Theorem B Pb, one label | y_L <= 205 < 300 | 95 rows | R (V2-6).
- Pc, filler vertex | g <= -297 (g < -296) vs -104 | R.
- FFo, label vertex | X >= 234, 320 used | 86 | R.
- Foo, label vertex | |alpha| < h/632 (stated h/600) | H.
- Foo, filler vertex | DM = 0 mod 16 | H.
- Theorem C | 2t = 0 mod 32, |beta| < 3h/8 < p - h/2 | H.
- Proposition D | a difference < 2.5h^2 has at most one prime factor in (40h, 80h] | H.
- Proposition E | W row >= 309 vs 178 | R.
- F1 | |delta| >= 39h vs 19h | R.
- F2 | |n_x| < h/158 | R.
- F3, n_y >= 1 | |Dx| <= 106h + 2 < 158h | R.
- F3, n_y <= -1 | superset of 158h ([G18]) | H.
- two_filler (C2) | f_o = T* - 24 + 8o | R.
- two_filler Lemma 1, Corollary 2 | 2-adic, df in {+-8, +-16, +-24} | H.
- two_filler Theorem 3 | 158h, k < h/2, Q < 3h, 4 filler rows per type | R.
- two_filler Proposition 4 | 4 · 158h > 420^2 iff h >= 280 | R.
- threshold Proposition 1(a) | width with 80h | H.
- threshold Proposition 1(b) | N != 0 since |DM| >= p > |Ds| | H.
- threshold Proposition 1(d) | |eps| < K < l, (5/l) = -1 | H.
- threshold Theorem 2 | |a| < h/312, |N| < h^2/14 < (1.04h)^2, |Ds - N| < (40h)^2 | H.
- threshold Theorem 3 | |Sigma| < h/152, |Dn| <= h/2 + h^2/8 | H.
- threshold Proposition 5 | |Delta| >= 158h superset, |DM| < h^2/8 | H.
- uniformity 3.4 | |dx| >= 64p | H.
- uniformity 3.5 | 4 filler rows per type ('106 values' is stale) | H.
- uniformity 3.6 | |Dn| < h^2/8 + h/2 + 1 | H.
- uniformity PNT counts | shares 2/4, 2/8 | H.
- J4, obstruction_table 1(d), heavy Proposition 4(a) | 64lp - 4(A - 1) > 2600h^2 | factor 2662.4 | H.
- D8 / D22 / (O1) | 64p > 2W_h + 1 through h = 5118 (5122 without the 4(A-1) slack) | v4 uses h <= 5117 | H.
(e) Low rows (low_rows_row3_types) [Z14]:
- Lemma LR | Phi - Lambda = 297; fillers > 28; 2h - 420 > h + 2 | H.
- Lemma S | |X2| >= 156h with |Y| <= 24; |n_x| >= 131h; |n_y| >= Phi - 14 | H.
- Q4(c) | j <= 210, |t| < 3h < 156h | H.
- (F5) | rows <= T* - 321; odd rows >= 301; rows 1-2 empty in row-3 types | H.
- Q4 (unused) | T* - 36 >= h - 222 > 2 | H.
(f) Sweep A notes [Z21]:
- sea_row3 (H1)-(H4) | rows >= 3; fillers > 5; odd deep rows: 1 mod 4 (row-3 types) and 3 mod 4 (row-1 types) under SAW*-shift; (H4) window 2h < 158h; ee differences = 0 mod 32 | H.
- sea_row3 2(iii) | |beta| <= 6h < 158h | H.
- sea_row3 Corollary B M2a | nu >= 2 -> mod-16 rule | R (K2).
- sea_row3 junctions | T* - 128 -> T* - 320; (20h, 40h] -> (40h, 80h], lower bounds only | H.
- J2 | h >= 10, g even, g = 0 mod 4 for odd h, 2g - 3 > h, g > (h + 1)/2 | H.
- J3 | at most 7 columns (V3 pair 3 + 3 + 1; mixed quadruple <= 6; rival pair <= 4) | H.
- J5 | in the form J5' ((B10)): windows pairwise > 2W_h apart; every block equals beta_z on the 2W_h-neighbourhood of its window, which for the rigid chain, case (a) WP and WD/WE needs > 2W_h from z, and for the case (c) WP block holds by construction with z inside U_WP | R ((B10) [Z18]; V4 audit).
- stride_menu Lemma 2 at sigma = 2 | Y^2/n = 5h^2/T^2 < (3h/T)^2 | H.
- stride_menu Lemma 4 | p > max(20h, (s^2/2 + 4)h) and p > 12h; s(p - A) > h; |bracket| < 12h < p | H.
- stride_menu Proposition 1' | no constants (any even stride) | H.
- point_counts | Q < 3h (D17), Q < 2h, Q <= h (D11); per-Q bound covers all; N_h^int is integral (Corollary B) | H.
(g) Sweep B notes:
- ap Lemma 1 | interval <= A0 h, I ⊂ [-A0 h, A0 h], q <= h^(1-eta), non-explicit C0 | H, folded into h_D [Z24].
- ap Lemma 3(a) | m0 | 224, q' <= 224 · h^(1/2)/32 = 7h^(1/2) | H [Z23].
- ap Lemma 4, Theorem D-weighted | q <= h^(1/2) via 32q; |E| <= 4h^(2-eps) | H [Z22].
- ratio_graph Theorem 4, Corollary 5 | a >= 4, in class a >= 5; Corollary 3 at k = 5: v2(p - q) = 2 + v2(be - al) >= 5 | H.
- block_sea criterion | h, m >= 4; Proposition 3: sea row > (h + 1)/2 (g > (h + 1)/2) | H.
- rigid Theorem 2 | |M_c - M_c'| >= p > 40h | H.
- rigid Part 3 | |bracket| <= 18A + 2K + 1 < P; gap > 36h | H.
- rigid no-right-angle steps | p > 10h, blocks > 78h apart (v4 > 158h), slope > 36 | H.
- sea_census B3(i) | a = v2(Delta i) >= 5 excludes a = 3 | H.
- sea_census B3(ii), B4 | any k >= 3, k = 5 | H [Z27].
- sea_census B1 | |Sigma| < h/152; (-1,-1) case via Proposition 1(c) | H/R.
- sea_census minimum heights (h >= 363, h >= 1499) | first-edge thresholds, not hypotheses | H.
- mixed_quadruples Setting | p > max(20h, 12h) | H.
- mixed_quadruples Theorem 1 | |dx| > 19sh, |2n1| < h/(9s) | H.
- mixed_quadruples Theorem 3 | |a| < 2h/(39s^2) | H.
- mixed_quadruples Theorem 4 | |k| < A < p; |M| < 5h < p; 12h < p; p = 3 mod 4 and +-2 mod 5 (from 3, 7 mod 20) | H.
(h) Sweep C notes:
- t1 Theorem E | Lambda = 1 + log h, W >= c Lambda^3 against W_0 = (log h)^3 (ratio <= 1.14); separation 2W_h, with 2W_h + 1 used | H [Z32].
- t1 Lemma AP | NOT USED (would need h >= 1.27e13) | n/a [Z33].
- filled_mod7 Section 6 | collars 2W (W = h^2) -> 2W_h + 1, by P3; at most 195 switches (h - H <= 195) | H [Z31].
- filled_mod7 rows | h >= 10^10; H in [h - 195, h]; F in [1000, 3743]; central rows [5000, h - 5000]; E_h = O(sqrt h) | H (R-d).
- T2 | (2) rows, (3), (10), (14)-(17); Phi residues, (L1)-(L3), mod-7 residues size-free | H.
- obstruction_table Table T | D-1L3F side (see (c)); family (d) 5117; stale counts M4, M5, M7, D-4L, D17 superseded by section 3 | R [Z28-Z30].
- two_moment, compatible | Lambda^3, O(h^(3/2)), h >= 10^10 | H.
- filled_mod7 (9) and Section 4 (T3's margins, Sweep C) | r - L >= 4986 > 390, H - r >= 4805 > 26, r - F >= 1257 > 390 | H. These are not mod7_inset line 144, which is in mod7_inset Section 3 (Sweep T).
- mod7_inset Sections 2-4 | not used: their margins 41/82 and h >= 1000 are for its own 18 profiles only (for T3's margins up to 195, 82 > 2 · 195 fails) | n/a (Sweep T).
- T6 (2) | Henriot size threshold ('sufficiently large h', delta = 1/3) absorbed into C_s on the finite range by tau(n) <= 2 sqrt(n); not part of h0 | H (Sweep T).
- T6 (2), T7 | Lambda = 1 + log h -> log h (ratio <= 1.0435), ell = 1 + loglog 3h -> loglog h (ratio <= 1.334) at h >= 10^10, both decreasing in h; constants only | H (Sweep T).
- T7, T8 | every collar 2W or 2W_h is <= 2W_h + 1; T8's W is W_h, and its union span 2W is P3 | H (Sweep T).
- binary_boundary Section 2 | inset levels (L, H) or (F, H) in place of 1 and h; needs both central rows strictly between the two sea levels, given by R-d ([5000, h - 5000]) and T3's levels (L <= 14, F in [1000, 3743], H in [h - 195, h]) | H (Sweep T).
(i) Other inputs:
- heavy_light Theorem 1(b) | h >= 4, any B >= 1, applied at B/4 | H.
- polylog Lemma IV | tail at h^(1/2)/32: be > c h^(1/6), O(h^(11/6) log h) | H.
- polylog Theorem IV | dyadic groups replaced by one group | H.
- additive_class_split Lemma 1 | H0 87 -> 210 | R.
- additive_class_split Lemmas 2, 4 | constant-free | H.
- consolidated_board Lemma FF' | cutoff /32, modulus lcm(32, m), 2d <= 210 | H.
- BH16 A3 | constant kappa_tau mod 16l | R (K2).
- BH16 A5 | H0 = 210, |dx| <= 2 sqrt(H0(h + H0)) | R.
- three_label_one_filler Lemma N | residues only | H.
- heavy_diagonals_sharp Lemma 1 | h >= 6, |T| < sqrt(5)h/18 | H.
- block_layout_n1 | 7 | x_c; L odd in [1, 14]; 2W_h + 1 stages; ends with odd row < 5000 go to R-d | H.
- V2-1 to V2-8 | 7 columns; j <= 2; 32q <= h^(1/2); T* - 300/444; b0 odd; y_F >= h - 202, 205 <= 300; (1.04h)^2; |pDt| >= p > |Di| | H.
- P1 Lemma rival, P3 locality | re-read | H.
(j) Stale constants in note statements (the K4 line is the authority) [Z17]:
- v3_and_cross_block: T* >= h - 63, T* - 128, Pb 90/82, n_y <= 87, 78h/74h, (20h, 40h].
- deep_layer_sawtooth Theorem 1(6): '80 rows'.
- saw_residual: h - 63, H0 87.
- additive_class_split: 86, 63.
- two_filler: h - 87, 74h, 78h, '88 values'.
- threshold: 40h in the width, (20h)^2, 320|Dt|.
- uniformity 3.5: '106'.
- heavy_light Proposition R: p <= 40h.
- rigid Theorems 4(a), 5 and sea_census L(k): (20h, 40h] and the 2-adic rule.
- Table T: 2560 -> 5117.

==================================================
5. WIDTH AND EXPONENT
==================================================
- Light regions: per type 4p · 16lB + 4A + 2(2W_h + 1) + 12. Over 512 types this is at most 512 · 4 · 80h · 16 · 2.08h · B (1 + o(1)) = 5452595.2 B h^2.
- Buffers, margins and sea pieces: about 3 · 512 pieces of width O(h^2), so O(h^2).
- Window separations (V4-1): at most 100 gaps of 2W_h + 1, so O(h^2).
- Theorem E: Delta = H_d(B/4) <= C_a 4^a h Lambda^(E(a)-1) B^(-a), with 4^(a*) = 3.5427. Cost C h^2 Lambda^(E(a)+1) B^(-a) ell^C1 + C h^2 ell.
- Theorem D (one group, rho = 2/B, |D| <= h, kappa finite): C h^2 Lambda^2 ell^C1/B + C h^2 ell.
- N1 collars and separations: 2 instances × 49 blocks × (at most 197 stages + O(ell) separations), each of width O(h^2), so O(h^2 ell).
- Switch and tails: O(h^2). Proposition partial: c0 n_rel tau*(h)^2 = o(h^2) in case (a). For odd h, case (c) has width c0 (n_rel + 4) tau*(h)^2 + 6h^2 + 4, and the extra 4c0 tau*(h)^2 + 6h^2 + 4 is O(h^2) (V4 audit).
- Total: M <= C h^2 (B + Lambda^(E(a)+1) B^(-a) + Lambda^2/B) ell^C1 + C h^2 ell + o(h^2).
Exponent:
- With B = Lambda^x, the exponent is max(x, E(a) + 1 - ax, 2 - x).
- At a* = 0.9124154 and x = theta* = (E(a*) + 1)/(1 + a*) = 1.4967429, with E(a*) = 1.8623941:
  - the middle term is theta*(1 + a*) - a* theta* = theta*;
  - the last term is 2 - theta* = 0.5032571 < x.
- Legendre duality: min over a of (E(a) + 1 - ax) = 2 - phi(x), and min over x of max(x, 2 - phi(x)) = theta*, the root of x = 2 - phi(x).
- So M <= C h^2 (log h)^theta* (loglog h)^C1. A truncation with m >= M columns has m + q_h points, so f(h, m) >= m + q_h, and with the paper's upper bound f(h, m) <= m + q_h this gives m_h <= M.
- The v4 changes add only O(h^2) and do not touch the exponent. These numbers were computed by three independent scripts on file (expo_v3.py, expo.py/expo2.py in the trace, mod7_t2_check.py in the patches audit), which agree. I did not recompute them.

==================================================
6. REMARKS (not load-bearing)
==================================================
- (R-P1) Census (N): under (B7)/(B8), a class keeps at most floor((h - 623)/448) + 1 labels in its region.
- (R-P2) (N), corrected [Z16]:
  - min max(p, q) over R_IV^(3) is > 109, and R_IV^(5) is a subgraph, so for h < 1.2e7 every R_IV edge goes to R-e;
  - for h < 4096 Theorem D receives only R_FF^+ ends;
  - for h <= 5117 no two classes of a type are within 2W_h + 1 columns.
- (R-C) The census (v2 board, 10 types, h = 1501, 2003, 2501) found no flags. The (B4) law, even h, J1* seams, WD/WE blocks at T1 constants and the WP junctions are untested.
- (R-F) Method floor (relocation_price_floor Theorem R, audit_relocation_price_floor.md): in class P with separated blocks (each flanked by c'h^2 columns of plain periodic sea, charged to the block), every relocation costs at least c Lambda^2 per label. Without the separation clause the floor is unproved for blocks narrower than h^(1+c).
- (R-X) Where the exponent might move. All of the following is conditional, and nothing in it is used above:
  - relocation_price_exponent (audited, audit_relocation_price_exponent.md): a heavy price h Lambda^bE gives theta_E(bE), the root of x + phi(x) = bE, with exponent 1 at bE = 1.135;
  - Theorem DC (audited against v2; restatement against v3 owed) removes Bad_split;
  - higher_arity_true_counts (audited, audit_higher_arity_true_counts.md): the higher-arity part costs about Lambda per label;
  - pair_families_dp_colouring (NOT AUDITED): cross-direction triangle sparsity is unproved, and R1, R2 are unanalysed;
  - the random-greedy pair price of about Lambda is a HEURISTIC only.
  - None of this lowers theta* in Theorem N.

==================================================
7. FIX LEDGER (v4)
==================================================
- Z1 V3-1 identity Y = (Bad_split ∩ S) \ D4 (trace issue 4; patches issue 1).
- Z2 heavy labels never in Bad_split (patches issue 1).
- Z3 A4 and D8 counted in the 9/5 term; normalised minimiser optional (patches issue 2).
- Z4 T1 chain completed with T3's inputs, T6, T7/T8; T9 and C1 not used; local lemma moved to EXTERNAL (trace issue 3; patches issue 3).
- Z5 [G14] wording (patches issue 4).
- Z6 g fixed in zero-residue blocks; [G14] prefix; 7 | T observation (patches issue 5).
- Z7 renumbering of the audit_v2 issues: 1 (B7); 2 R_FF density [G11]; 3 D4' status; 4 names, S10, T4/M8; 5 Table T 5117; 6 status sentence; 7 A-26 statuses [G20]; 8 V2-4 count [G8]; 9 Delta i [G10]; 10 N-1/N-3, now Theorems N1 and U (trace issue 5; patches issue 6).
- Z8 A-30/A-31 cite their audit files; (H2) discharged (trace issue 1; patches issue 7).
- Z9 Theorem D hypotheses in polylog's numbering (trace issue 6).
- Z10 Theorem K sentence (trace issue 7).
- Z11 V3-2 fix sources (trace issue 8).
- Z12 l-range K4 line; rigid 2(e) at about 1.016h (sweep issue 1; Sweep B).
- Z13 v4-constants K4 line (sweep issue 2).
- Z14 low_rows K4 line (sweep issue 3).
- Z15 Proposition R -> threshold Proposition 1(a),(b) (sweep issue 4).
- Z16 (R-P2) wording (sweep issue 5).
- Z17 stale-constant list (sweep issue 6).
- Z18 (B10) J5 separations (Sweep A issue 1).
- Z19 J3 columns (Sweep A issue 2).
- Z20 sea_row3 2(ii) (Sweep A issue 3).
- Z21 Sweep A K4 lines and the SAW*-shift reading of Corollary B (Sweep A issue 4).
- Z22 Theorem D-weighted 4h^(2-eps) (Sweep B issue 1).
- Z23 ap Lemma 3(a) mod 32 (Sweep B issue 2).
- Z24 ap Lemma 1 location; h_D (Sweep B issue 3).
- Z25 A-10 Corollary 3(b) scope (Sweep B issue 4).
- Z26 rigid Theorems 4(a), 5 not adopted (Sweep B issue 5).
- Z27 sea_census k >= 3 (Sweep B issue 6).
- Z28 D-1L3F side pointer (Sweep C issue 1).
- Z29 5117 (Sweep C issue 2).
- Z30 Table T read through section 3 (Sweep C issues 3, 7).
- Z31 collars 2W -> 2W_h + 1 (Sweep C issue 4).
- Z32 Lambda normalisation (Sweep C issue 5).
- Z33 Lemma AP not used (Sweep C issue 6).
- Z34 sub-inputs not swept -> (H1-T) (Sweep C issue 8).
- Z35 Sweep T: (H1-T) closed; K4 (h) lines for filled_mod7 (9)/Section 4, mod7_inset Sections 2-4, T6 (2) and T7/T8; rows T-3', T-6, T-7/T-8.
- Z36 V4 audit: V4-1 and V4-2 audited; (B10) background wording and J5'; A-13 and K4 (f) J5 lines; case (c) width in section 5 and the statement.
- Z37 diff audit: D11 not in Y; A-14 Theorem D and A-7 Proposition C not used; A-29 NOT USED; A-7 2(ii) case e = 2; (R-F) separation clause; Theorem DC restatement owed; 1.016h; [1987, 7485]; v3 sentences restored (eps_D, eps and c_T in the statement; the 'No longer hypotheses' mapping; (B4) compatibility; V3-2 B7 factor 2, D17 average and law coverage).
- Editorial, no audit asked for it: v4 rewrote v3's (R-X) table and deleted v3's (R-T) remark (consolidated_board_v3.md section 5). Neither is load-bearing.

## External results used

- Henriot, corrected Theorem 5, Math. Proc. Camb. Phil. Soc. 157 (2014) 375-377, used through ap_hypothesis_henriot Lemma 1. Its audit read the erratum, and I did not re-read it.
- Prime number theorem in arithmetic progressions mod 5 and mod 20 (non-explicit), for the admissible pairs (l, p).
- Quadratic reciprocity.
- tau(n) << n^eps.
- The product-form (asymmetric) Lovasz local lemma (T2 Section 7, Theorem D (D4), Theorem E (E4)).
- Sharpness remark only: the fundamental lemma of sieve theory in dimension 1/2 and Mertens' theorem for primes = +-1 mod 5 (theorem numbers not checked).

## Checks

I read consolidated_board_v3.md in full, plus audit_consolidated_board_v3_trace.md, audit_consolidated_board_v3_patches.md and audit_constant_lists_sweep.md. I also read CLAIM_LEDGER.md section A and its T-rows for the names of the T1-chain notes and their audits, and I listed the folder to confirm that audit_uniformity_first_moments.md and audit_block_layout_n1.md are on file and that Sweeps A-C had no files yet (they are filed since; see Gaps). Then I merged every issue from the three audits and the three sweeps into v4 by hand, tagged each one Z1-Z34, and kept the v3 colouring law unchanged.

One design choice: for the A4/D8 slip I took the simpler fix, which moves both terms into the O(h^(9/5+2eps)) line. This adds no new argument. The normalised minimiser stays as an option.

I ran no script. The exponent and width numbers come from three independent scripts already on file, and the margins quoted come from the sweeps. The repository was only read, I ran no git command, I did not use the web, and I wrote no files.

## Gaps

- (H1-T) is closed by Sweep T: no failing step, five minor fixes applied (Z35). Sweep T relied on the audits on file for content and did not re-read Henriot's paper. Its report is audit_constant_sweep_t.md.
- Sweeps A, B and C are filed as audit_constant_sweep_a.md, audit_constant_sweep_b.md and audit_constant_sweep_c.md.
- V4-1 (the window separations of (B10)) and V4-2 (counting A4 and D8 in the O(h^(9/5+2eps)) term) are audited in the V4 audit: both correct, four minor fixes applied (Z36). Its report is audit_consolidated_board_v4_steps.md.
- Two thin margins against the lower end of the l range: threshold Proposition 1(c) needs 1.033h and Lemma L-adic (i) needs 1.029h, against l > 1.04h. Both hold, but any lowering of the l range would break them.
- The T1 chain is read end to end in audit_t1_chain_end_to_end.md (no error found) and earlier in 2026-11-09/AUDIT_threshold_upper_bound.md.
- h0 = max(10^10, h_PNT, h_D) is not explicit. h_D now includes Henriot's C0 from ap Lemma 1.
- ratio_graph Corollary 3(b) is not certified for R_IV^(5). It is not used by the upper bound.
- The census evidence (R-C) tested the v2 board, not the (B4) law. No WD/WE block was built at T1 constants, and no WP junction was built at definition level.
- Not addressed: m_h = O(h^2), and any exponent below theta* = 1.4967429.

## Missing estimate

None for the near goal. The certification work is done. Below theta*, the binding term is the heavy-light trade-off B against Lambda^(E(a)+1) B^(-a). In class P, the method floor (relocation_price_floor, audited) blocks it at price Lambda^2.

## Next steps

- Have one reader check the 14 November edits.
- Optionally adopt the normalised minimiser Y' in K6 step 1 to keep A4 and D8 at h^(1+o(1)). This is cosmetic, since n_rel does not change.
- For the exponent below theta*: see stride_menu_heavy_count.md and the stride-transfer notes (a menu of strides 4u); every route to a relocation price below Lambda^2 has failed with a proof (congruence_slot_lists.md, hypothesis_w_false.md).

