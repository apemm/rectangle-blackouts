# Census of the consolidated board at h = 1501 to 2501

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (computational): on 10 region types at h = 1501, 2003 and 2501, every violation among true survivors is a one-label family D10 or D11, and none remains after relocation. Two-label families appear only in the superset runs, and each is an R_FF edge that (B8) or R-e removes. Short proof (P1): under (B8) a light subclass keeps at most floor((h - 623)/448) + 1 labels, so four-label survivors need h >= 1967 and stay rare. A real test of the in-class multi-label cells needs h of about 4000 or more.

# Result

## Status

partial

## Summary

I ran a census of L*** (consolidated_board_v2) at h = 1501, 2003 and 2501 on 10 region types (row-1 and row-3; k = 0, 1 and 2). I found no flags. True survivors show only the one-label families D10 and D11, and zero violations remain once those labels are relocated. The two-label families D12 and D13 appear only in the superset run, and every instance is an R_FF edge that (B8) or R-e removes. Short proof: under (B8), a final subclass keeps at most floor((h-623)/448)+1 labels. So true in-class survivors stay sparse (at most 3 per subclass were seen), and no 4-label survivor occurs at these heights.

## Statements

These are computational facts from a finite census, plus three short proved observations. Nothing here proves the near goal or Theorem N.

SETTING. Board: consolidated_board_v2 (B0)-(B8), with the least admissible (l, p), kappa = b_tau = 0, psi seed 1, and strip windows as in census_consolidated_board.md.
- h = 1501 (h = 1 mod 4; B = 20, l = 1567, p = 60083):
  - (29,7): row-1, k = 0, T* = 1499.
  - (28,7): row-3, k = 0, T* = 1497.
  - (10,15): row-3, k = 1, T* = 1397.
  - (26,6): row-3, k = 2, T* = 1317.
- h = 2003 (h = 3 mod 4; B = 21, l = 2087, p = 80147):
  - (23,13): row-1, k = 0, T* = 1999.
  - (22,13): row-3, k = 0, T* = 1997.
  - (13,13): row-1, k = 1, T* = 1915.
  - (28,13): row-3, k = 2, T* = 1817.
- h = 2501 (B = 22, l = 2617, p = 100043):
  - (7,13): row-1, k = 0, T* = 2479.
  - (22,13): row-3, k = 2, T* = 2317.
- No diagonal was heavy at any of these heights.

Four label sets per type:
- SUPERSET: R-a, R-b (320, plus the 444 extension for k = 2) and R-c.
- FAITHFUL: SUPERSET, then (B8) Bad_split and R-e by definition, then census-driven R-f (D4, D10, D11) and a closure run.
- S1L: SUPERSET without the 444 extension, k = 2 types only.
- STRESS: unsplit classes (K_T = 1), and one run with no G_T colouring. These are not the board.

(R1) COMPUTED: NO FLAGS. In every run, every (V1)-(V5) violation that contains a label point, or has W in a label column, falls in a counted (C) cell: D10, D11, D12 or D13. oob was 0 throughout.
- None falls in a cell the table marks E: A1, A2, A3 (D-4L in one class), B1-B5, B6 in one class, D1, D2/D6/D7, D4, D4' (D-1L3F with the label on the side), D5, D6, D14, D15 (D-2L2F in one class), D19, D20 (3L1F), V3 (family (d) or any other), SLF.
- None is UNLISTED, and there is no D21 tag.

(R2) COMPUTED: TRUE SURVIVORS. FAITHFUL board, 10 types, 6259 labels after (B8) and R-e.
- The only violations are 3166 D10 rival pairs and 196 D11 M2c quadruples. All are single-label.
- I relocated those 1866 labels to Proposition partial.
- The closure run on the remaining 4393 labels gives 0 violations in all 10 types.

(R3) COMPUTED: IN-CLASS COVERAGE. Every window is searched completely, so every k-subset of a window is tested.
| Label set | Labels | Pairs | Triples | Quadruples |
|---|---|---|---|---|
| SUPERSET, split classes, 9 types | 7826 | 3421 | 1613 | 1180 |
| S1L | 1234 | 433 | 188 | 153 |
| STRESS (classes up to 17 labels) | 2202 | 7465 | 20327 | 44920 |
| FAITHFUL | 6259 | 622 | 32 | 0 |
| FAITHFUL closure | 4393 | 328 | 14 | 0 |
- Two-label violations occurred only in the SUPERSET and S1L runs: 7 D12 (Fo/Fo, d > 0) and 1 D13 (Fe/Fe, d < 0).
- Each of the 8 is an R_FF^oo or R_FF^ee ratio edge, and each D12 is also an R_FF^+ edge (|Delta i| = 64 <= 210). So FAITHFUL removes all 8, and no two-label violation occurs in FAITHFUL.
- No R_IV edge occurs inside any subclass, so B6 never fires.

(R4) COMPUTED: THE D12/D13 SHAPES. The 7 D12 instances span 4 types and 3 heights, and all have one shape:
- t = 64, filler row Y = T* - 24, depths (Y1, Y2) = (520, 392) = 8 (65, 49);
- R_FF shape (a, b) = (3, 2), with U = -65, V = -49 and P = X1 - X2 = 3t.
The D13 instance has t = -96 and depths 3 (679, 743), with |U'| = 679 < |V'|. Both fit additive_class_split Lemma 1 exactly.

(R5) COMPUTED: LEMMA S1L TEST. In the k = 2 types without the 444 extension (62 extra labels at h = 1501, 94 at h = 2003), there is no D-1L3F side configuration (D4'), and nothing new except D10 and the D12 shape above.

(R6) COMPUTED: PURE GAP. The pure SAW*-shift gap with its sea has 0 violations for all 32 distinct (r0, T*) values at each of h = 1501, 2003 and 2501. This covers every type tested.

(P1) PROVED: SURVIVOR SUBCLASSES ARE SPARSE. Under (B7) and (B8), a final subclass keeps at most floor((h - 623)/448) + 1 labels in its light region. So a surviving subclass with k labels needs h >= 623 + 448(k - 1): 1071 for k = 2, 1519 for k = 3, 1967 for k = 4.

(P2) PROVED: WHERE THE GRAPH EDGES GO AT THESE HEIGHTS.
- For h < 1.2 * 10^7, every R_IV edge goes to R-e (WP), not to Theorem D.
- For h < 4096, the Theorem D part of R_FF^oo and R_FF^ee is empty (shape enumeration computed at h = 1501, 2003 and 2501).
- So at the tested heights, Theorem D receives only R_FF^+ shallow ends.

(P3) PROVED: in-class windows are complete at these heights. For h <= 5117, no two subclasses lie within 2W_h + 1 columns of each other. This is (O1) of census_consolidated_board, which I re-checked at h = 2501. So no cross-class family can occur, and per-subclass windows see all in-class content.

## Proofs

SCRIPTS (all in the script folder scripts_census_large/).
- core.py, checker.py, classify.py, lstar.py, validate.py and pure_gap.py are byte-identical copies of research_archive/2026-11-13/scripts_census (checked with cmp). They were copied so that the numba cache is never written into the repository.
- New files: v2board.py, bsplit.py, fastboard.py, census_v2.py, census_v2_tables.py, analyze.py, verify_v2.py, cmp32.py, pg.py, stats.py, runtype.sh and batch.sh.
- Logs: log_<mode>_<split|nosplit>_<h>_<iota>_<sigma>[_closure][_graph|_rho1|_rho2|_nocolour].txt, an_*.txt, anc_*.txt and pg_*.txt.
- Every py call was one run under 60 s (TL 35-45 s per chunk, resumed from NEXT). Peak memory at h = 2501 was 876 MB. The repository was only read.

1. BOARD (v2board.py)
- v2board.py reuses lstar.type_params, diag_graph and greedy unchanged, with the same per-type rng stream, groups, sorted subclass order and placement t = rho_s + 16 l k.
- Removal rules follow v2 (B7):
  - R-a: i = 0, plus i = 2 or j in {0, 1} in row-3 types.
  - R-b: an endpoint row >= T* - 320, plus 2i+1 >= T* - 444 when k_tau = 2.
  - R-c: 2i+1 <= 300.
- Slots satisfy n = i + p t. Following [F1], the filler phase is rho0 = (first label slot) mod 4, which is constant on R_tau because n = iota + sigma - kappa (mod 16).

2. (B8) AND R-e BY DEFINITION (bsplit.py; FAITHFUL mode only)
- Edges are computed on all labels of the final subclass, before R-a to R-c, because rule 2 precedes rule 3. This removes only more labels.
- R_FF^+: every pair with 0 < |Delta i| <= 210. The shallow end (larger i) goes to Theorem D.
- R_IV: odd u-values u = (2i+1-r0)/2 with {u, u'} = {q m, p m}, m odd, for lambda = (al, be) odd, coprime, 0 < al < be, be < 400, using q and p of sea_census_rigid B4.
  - The cap be < 400 suffices: q >= F/5 >= be^2/5 and q <= h.
  - Both labels go to R-e, because max(p, q) >= 109 > h^(1/2)/32.
- R_FF^oo and R_FF^ee: for each filler row Y_o and each parity, take depths Y1, Y2 > 0, reduce them by their gcd, and test them against the set of (|U'|, |V'|) with U V > 0, over coprime (a, b), b > 0, a^2 + b^2 <= 40h.
  - Completeness: Y1 = mu|U'| <= h, gcd(U, V) | 40 (Lemma 2) and a^2 + b^2 <= |U| when U != 0. So every relevant shape is listed.
  - Rule: if |U'| <= h^(1/2)/32, the L1 end goes to Theorem D; otherwise both labels go to R-e.
- Removal counts per type are in each log header. For example, (7,13) at h = 2501 had 763 R_FF^+ labels, 375 + 34 R-e R_FF labels, 0 R_IV labels and 0 B8-R_FF labels.

3. CENSUS (census_v2.py)
- Windows and anchors are exactly those of census_class.py: the label columns +- (2W_h + 64); every label point; every white point of a label column.
- Classification is by classify.run and the validated kernel, unchanged.
- Two engineering changes, each checked:
  - (a) FastWinBoard slices a 16-periodic template instead of calling np.where on 2W_h-wide arrays. Its R1, R2 and rows() were asserted equal to WinBoard on all 39 windows of one 8 s run at h = 1501, and on the first 3 windows of every run at h <= 2003.
  - (b) The int32 divisor list. cmp32.py ran 142 windows of (10,15) at h = 1501 with the int64 table and the int32 table and got identical violation lists (134 violations).
- verify_v2.py rebuilt each board from the (B5)/(B6) formulas, not from WinBoard. It re-checked all 8 multi-label instances, 60 random D11 instances and 60 random D10 instances against Lemma mixedeq or Lemma rival, with corners and row bounds: 128 of 128 passed.

4. VERDICT MAP (analyze.py)
- C cells: D10, D11, D4 (label on the diagonal), B6, D12 and D13. Everything else found in a one-class window is FLAG.
- B6 instances would be checked against the R_IV definition; none occurred.
- The 8 two-label instances were tested against bsplit.graph_reloc. Each is an R_FF ratio edge, and the D12 instances are also R_FF^+ edges. So 0 of 8 are missed by (B8) and R-e.

5. POSITIVE CONTROLS. Breaking [F1] by shifting rho0 shows the pipeline sees in-class filler families.
- RHOSHIFT = 1 on (29,7) at h = 1501 gives 2133 D1 instances (correctly FLAGGED, deep labels), 74 D11, 6 two-label D13 and 126 D10.
- RHOSHIFT = 2 gives 1036 D4 and 140 D10.
- The NOCOLOUR control (no G_T colouring, one class per diagonal) produced nothing new: only the same 84 D10. So it is NOT a positive control. Restricting to i = iota (mod 32) already removes the label-label rival pairs among these labels.

6. PROOF OF (P1)
- R-c gives 2i+1 >= 301, so i >= 150.
- R-b gives 2i+1 < T* - 320. T* = T0 - 64k is odd, because T0 = y_P + 32 or y_P + 48 (mod 64) with y_P odd. So 2i+1 <= T* - 322 and i <= (T* - 323)/2 <= (h - 323)/2.
- Survivors therefore have i in an interval of length at most (h - 623)/2.
- Two labels of one final subclass lie on one diagonal and in one type, so Delta i is a nonzero multiple of 32.
- If |Delta i| <= 210, they form an R_FF^+ edge, which is monochromatic since they share the subclass. By (B8) the shallow end is in Bad_split, and rule 2 of (B7) sends it to Theorem D, or to Proposition partial if it is in E_D. Either way it is not a survivor.
- So survivors are pairwise at least 224 = 7 * 32 apart in i, and their number is at most floor((h - 623)/448) + 1. QED.
- Observed maxima: 2 at h = 1501, 3 at h = 2003 and 3 at h = 2501, against bounds of 2, 4 and 5.

7. PROOF OF (P2)
- R_IV: q_lambda = al F/g with F = 4(al - 2be)^2 + be^2 and g in {1, 5}. The smallest q is 109, at (al, be) = (1, 3): F = 109, g = gcd(109, 2) = 1. So max(p, q) >= 109 > h^(1/2)/32 whenever h < 109^2 * 1024 = 12,166,144, and R-e applies.
- R_FF: h < 4096 gives h^(1/2)/32 < 2, so the Theorem D part needs |U'| = 1.
  - In the complete shape list at h = 1501, 2003 and 2501, the only shape with |U'| = 1 has |V'| = 1.
  - That shape forces Y1 = Y2. But Y2 = Y1 - 2t with t = Delta i != 0. So it never fires.
  - The removal-reason counts confirm 0 B8-R_FF labels in all 10 types.

8. PROOF OF (P3)
- Two subclasses of one type have Dt = p^(-1) Ds (mod 16 l) with 16 | Ds, so Dt is a nonzero multiple of 16.
- Their label columns are therefore at least 64p - 4(A - 1) > 2560h - 2h apart. This exceeds 2W_h + 1 <= (h - 1)^2/2 + 3 for every h <= 5117.
- At h = 2501: 64 * 100043 = 6.40e6 against 2W_h + 1 = 3.13e6.
- Different types sit in different regions, separated by the (B9) margins.

9. RUNS, per type (kept labels / violations)
| h | Type | SUPERSET | FAITHFUL | Relocated | Closure |
|---|---|---|---|---|---|
| 1501 | (29,7) | 518 / 84 D10 | 357 / 55 D10 | 36 | 321 labels, 0 |
| 1501 | (28,7) | 518 / 98 D10 | 330 / 57 D10 | 32 | 298, 0 |
| 1501 | (10,15) | 408 / 300 D10, 68 D11, 3 D12 | 286 / 203 D10, 58 D11 | 122 | 164, 0 |
| 1501 | (26,6) | 279 / 306 D10 | 189 / 207 D10 | 111 | 78, 0 |
| 2003 | (23,13) | 1166 / 242 D10 | 773 / 159 D10 | 118 | 655, 0 |
| 2003 | (22,13) | 1166 / 242 D10 | 801 / 170 D10 | 123 | 678, 0 |
| 2003 | (13,13) | 1000 / 680 D10, 200 D11, 2 D12 | 659 / 447 D10, 138 D11 | 316 | 343, 0 |
| 2003 | (28,13) | 799 / 833 D10 | 524 / 530 D10 | 248 | 276, 0 |
| 2501 | (7,13) | 1972 / 493 D10, 1 D13 | 1294 / 318 D10 | 248 | 1046, 0 |
| 2501 | (22,13) | not run | 1046 / 1020 D10 | 512 | 534, 0 |

Further runs:
- S1L: (26,6) at h = 1501 gives 341 labels and 374 D10. (28,13) at h = 2003 gives 893 labels, 931 D10 and 2 D12.
- STRESS, unsplit: (29,7) at h = 1501 gives 84 D10. (23,13) at h = 2003 gives 242 D10. The no-colouring run of (29,7) at h = 1501 gives 84 D10.
- An earlier closure run without (B8) at h = 1501 (types (29,7), (28,7), (26,6), relocating the SUPERSET D10 labels) gives 0 violations on 462, 462 and 117 labels.

## External results used

- None. No web sources were used. Only the notes in research_archive/2026-11-13 (census_consolidated_board.md, consolidated_board_v2.md, sea_census_rigid.md B4, additive_class_split.md Lemmas 1 and 2, deep_layer_sawtooth.md Theorem 1, v3_and_cross_block.md Theorem C, threshold_families_random_prime.md) and the scripts_census code were read.

## Checks

How each part of the census was checked:
- The validated kernel files were copied byte-identically (cmp) into the script folder.
- FastWinBoard was asserted equal to WinBoard (R1, R2 and rows) on 39 windows, plus 3 windows of every run at h <= 2003.
- The int32 and int64 divisor tables gave identical violation lists on 142 windows (134 violations).
- 128 of 128 reported instances (all 8 multi-label, 60 D11, 60 D10) were re-verified from the (B5)/(B6) formulas and Lemmas mixedeq and rival.
- All 8 two-label instances are edges of my R_FF or R_FF^+ graphs. Their shapes were checked by hand against Lemma 1: (3,2) with mu = 8 and t = 64 for D12; ratio 679:743 with mu = 3 and t = -96 for D13.
- The pure gap is clean for 96 (r0, T*) cases.
- Positive controls: RHOSHIFT = 1 and 2 (detected); NOCOLOUR (not positive).
- oob = 0 and no FAIL in every log.
- Every py call ran under 60 s, peak memory was under 0.9 GB, and runs were strictly sequential.
- (P1), (P2) and (P3) are proved in the proof field.

## Gaps

- The census covers 10 of 512 region types at three odd heights (1501, 2003 and 2501). No even h was tested, and row-1 k = 1 was tested only at h = 2003. All runs used one (l, p) (the least admissible pair), one psi seed, and kappa = b_tau = 0. By (O1), (l, p), kappa and b_tau do not change in-class content at these heights, but psi does.
- True survivors are sparse in their subclasses (P1): FAITHFUL runs held only 622 in-class pairs, 32 triples and no quadruples. So D-4L in one class, and most of D-3L1F, were tested only against SUPERSET and STRESS label sets. Those sets contain labels the board relocates, so they stress the E cells but are not the board. A 4-label survivor subclass needs h >= 1967 and was not seen at h = 2003 or 2501. A real test needs h of about 4000 or more, beyond the 1 GB divisor table of the current kernel.
- The (B8) and R-e graphs are my own implementation, from sea_census_rigid B4 (R_IV) and additive_class_split Lemma 1 (R_FF). I computed edges on the full final subclass before R-a to R-c, which is my reading of the priority rule. Lemma 1 itself is not audited. For R_FF^+ I took 'shallow end' to mean the larger i.
- R-d was not implemented as a criterion: there were no heavy diagonals, so no T1-exceptional labels; D4 was census-driven and never occurred. D8 is cross-class and therefore vacuous here (P3). R-f was applied by census only (D10, D11), not by the defining criteria of saw (i) and (ii).
- The NOCOLOUR control was not positive. Only the RHOSHIFT controls (breaking [F1]) showed that in-class filler families, including the two-label D13, are detected at these heights. No positive control produced an in-class label-label family (A2, A3, B6, D14, D15, D20) at these heights.
- Not re-run at these heights: seams (Table J1*), buffers, J2 pieces, Theorem D and Theorem E blocks (N-1, E4), Proposition partial windows and truncation. Pure-gap V3 coverage relies on pure_gap.py, which anchors black points only, as in the earlier census.
- Family names come from classify.py (point tags, shallow pattern, filler-row equality). I re-derived only the D12 and D13 shapes (R4) and the R_FF and R_FF^+ edge membership of the 8 two-label instances.

## Missing estimate

This census proves nothing about the missing estimates (N-1 and N-3). It is evidence only for the in-class E cells of the merged table in the 10 tested types at h = 1501, 2003 and 2501. What it does show:
- At these heights, the in-class C cells that actually fire are D10, D11, D12 and D13.
- D12 and D13 are exactly R_FF edges.
- D10 is a large constant-factor cost: it relocates 10% to 49% of FAITHFUL labels per type, and 49% (512 of 1046) in the k = 2 type at h = 2501.
- The R_FF^+ part of Bad_split takes about 30% to 40% of the labels that pass R-a to R-c.

## Next steps

- Add (P1) to consolidated_board_v2's remarks. Under (B8), with R_FF^+ range 210, a light subclass holds at most floor((h-623)/448)+1 survivors. So the in-class multi-label cells (D-4L, 3L1F) cannot meet true survivors below h of about 1500 (3 labels) or 1970 (4 labels), and rarely do at h of about 2500.
- To test D-4L and 3L1F against true survivors, reach h of about 4000 to 6000. This needs a kernel without the full h^2 divisor table: factor on the fly, or keep a table of small divisors only. (O1) still makes windows per-subclass up to h = 5117.
- Run the FAITHFUL pipeline (batch.sh) over all 512 types at h = 1501, in about 2 runs per type, and at one even height. Add a second psi seed and a second (l, p) for a few types.
- Look for a genuine positive control for the in-class label-label cells. For example, drop the i mod 32 type restriction (use i mod 16), or place two G_T-adjacent labels in one class. This would show that A2, A3, D14, D15 and D20 are detected at large h.
- Record that at h < 4096, Theorem D receives only R_FF^+ shallow ends, and every R_IV and R_FF ratio edge goes to R-e (P2). This makes the definition-level Theorem D block test of N-1 simpler at moderate h.

