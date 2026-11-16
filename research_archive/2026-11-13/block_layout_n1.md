# The block layout of Theorems D and E (N-1)

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: Theorem N1. Amend rule 2 of (B7) so that only the non-exceptional labels of Bad_split go to Theorem D. Then the Theorem D and Theorem E blocks place each received parity edge exactly once as a double and end in constant row-h tails. The audit of consolidated_board_v2.md found the same amendment independently. The proof cites only audited inputs. Definition-level E and D blocks at h = 111, 112 and 129, glued across the switch, show no violation, far below the constants of T1. Theorem N also needs h0 >= 10^10. Not audited yet.

# Result

## Status

proved

## Summary

N-1 (K8'(b) and E4) holds for L*** once (B7) rule 2 is amended to Bad_split ∩ S. The proof uses an explicit T1 block layout and cites only audited inputs. Definition-level E and D blocks at h = 111, 112 and 129, glued across the switch z, show 0 violations.

## Statements

THEOREM N1 (block layout; proved here, NOT audited; conditional on the audited inputs I1 to I4 below).

Notation. D := 2W_h + 1. A profile is pi = (L, F, H, g) as in filled_mod7_profile_cover.md (1)-(3), (7)-(9). Its sea is s_pi(x) = F if 7 | x, L if chi_7(x) = -1, and H if chi_7(x) = 1. S is the set of labels that are not T1-exceptional. pi(e) is a fixed profile map on S, for example the least L in {1..14} with L = a_e (mod 7) and g = (b_e - a_e)/5 (mod 7), with g = 1 when that is 0. v_pi is T1's weight, and a class is a dyadic class (v <= Lambda^3) or a coarse group (W_k, W_{k+1}], with W_0 = Lambda^3 and W_{k+1} = W_k^(4/3).

Inputs (all audited):
- I1 is the T1 profile theorem (filled_mod7 Sections 1-6 and its independent audit). It covers: the sea; one-label substitution at any period-zero column, with no tilted rectangle having 3 or more black corners and at most one label; and the hole-choice property (each period-zero column may hold F or H).
- I2 is the existence of injective centre maps avoiding every bad event E_J (|J| = 2, 3, 4, coincidence events included). This comes from compatible_profile_threshold Sections 3-4, T1 (8), Theorem E (E4)-(E5) and Theorem D (D4). The events E_J do not depend on the sea pattern: the other points need only lie in sea rows.
- I3 is the paper: 2W_h+1 locality, Lemma chain, Lemma rival, and the parity step of Lemma sea.
- I4 is J5 of full_layout_junctions.md.

Instances. There is one Theorem E instance, which receives R_E = heavy-diagonal labels in S. There is one Theorem D instance per dyadic group j of c_T, which receives R_j = (Bad_split ∩ S ∩ D_j) minus E_{D,j}.

BLOCK LAYOUT (BL):
- BL1. R_{I,pi} = {e in R_I : pi(e) = pi} is partitioned into classes c of profile pi. Each class has a slot count N_c >= |c| and an injective centre map X_c : c -> {0..N_c - 1} from I2.
- BL2. The core of c is the interval K_c = [x_c, x_c + 7N_c - 1] with 7 | x_c. Column x_c + 7 X_c(e) holds exactly the two points (a_e, b_e). Every other column x of K_c holds the single point s_pi(x), so unchosen slots keep F.
- BL3. Consecutive cores of one block are separated by at least D columns holding s_pi.
- BL4. The right collar is, in order away from the core:
  - P: D columns of s_pi;
  - Phi: D columns of s_pi with F replaced by H at the columns divisible by 7;
  - C_H, C_{H+1}, ..., C_{h-1}: D columns each, of constant rows H, H+1, ..., h-1;
  - then row h.
  The left collar is the mirror image.
- BL5. The block B_{I,pi} is: row h on (-inf, a) | left collar | cores and separations | right collar | row h on (b, inf). Its window is U = [a, b].
- BL6. Every D or E window lies right of the switch z, at least D columns from z and from every other window (of any kind), with row h in between.

CLAIMS:
- (a) Every column of B_{I,pi} is a singleton or a double. The doubles are exactly the label columns. The double at x_c + 7X_c(e) has rows {a_e, b_e}, the parity edge of e.
- (b) The map e -> column is injective. So B_{I,pi} carries each edge of R_{I,pi} exactly once, and the instance carries each edge of R_I exactly once (K8'(b)).
- (c) B_{I,pi} is constant row h outside U (E4).
- (d) B_{I,pi}, read as a configuration of the strip with infinite row-h tails, has no (V1)-(V5) violation.
- (e) J5 glues every D and E window to its neighbours, z included.
- (f) With the amended rule 2' of (B7), K8' holds for L***: every column is a singleton or a double, the doubles carry pairwise distinct parity edges, and every parity edge occurs.

AMENDMENT (needed). (B7) rule 2 must read: 'the label is in Bad_split ∩ S (not T1-exceptional) and not in E_D: it goes to Theorem D'. Without this, a shallow R_IV end with odd row below 5000 is outside T1's bulk rows and is sent to a Theorem D block that cannot place it. Such ends exist: the smallest R_IV edge has u = 349, which is odd row about 699. The labels in Bad_split minus S fall to rule 3 (R-d), so J3 closure is unchanged.

LEMMA RL (restriction; proved here, conditional on I1 and I2). If X_c avoids every E_J with J ⊆ c, then for every c' ⊆ c the restricted configuration (the labels of c' placed, the other slots F) has no violation. So a Theorem D block may also be made by deleting labels from a placement of S (Lemma M1 read literally), or by removing E_D after placement, without re-running the local lemma.

## Proofs

0. WHAT N-1 NEEDS. consolidated_board_v2 (iii) and V2-8: every D and E block places each received parity edge exactly once as a double, every other column is a singleton, and both ends are constant row-h tails, so that J5 glues the block. polylog's R(Y) is defined as exactly such a block. So N-1 says that Theorem D's and Theorem E's constructions realise R(Y). The layout BL is read off T1 (filled_mod7 Sections 3-6, compatible Sections 4-5, two_moment Section 3) and Theorem E (E5): a fully filled period-7 profile, labels at designated period-zero slots, unused slots keeping F, O(ell) class blocks separated by periodic sea, and the Section 6 collars. Theorem D and Lemma M1 use the same construction with their own N_w, or with S's.

1. CLAIM (a). The intervals of BL5 are disjoint: row-h tails, the stages of the two collars, cores, and separations. Each column gets its content from exactly one rule.
- The rules s_pi, the Phi rule, constant C_y and row h each put exactly one point in the column.
- The label rule of BL2 applies only at x_c + 7X_c(e), which lies in K_c, and puts the two points a_e (odd) and b_e (even). They are distinct, so the column is a double, and {a_e, b_e} is a parity edge. The F of that slot is not kept (filled_mod7 Section 1).
So the doubles are exactly the label columns.

2. CLAIM (b).
- Inside one class the column x_c + 7X_c(e) is injective in e, because X_c is injective: the coincidence events are part of I2.
  - compatible Section 4: 'coincident centers are forbidden separately'.
  - Theorem D (D4): the coincidence term is covered by 2 rho n_w <= N_w / C0.
- Different classes have disjoint cores (BL3).
- So e -> column is injective on R_{I,pi}, and by (a) its image is the set of doubles of B_{I,pi}.
- pi is a function on S and the classes partition R_{I,pi}: dyadic classes below Lambda^3 and coarse groups above it, with consecutive endpoints. So every e in R_I lies in exactly one class of exactly one block.
- The blocks of an instance have disjoint column ranges (BL6). So the instance's doubles carry R_I, each edge once.

3. CLAIM (c). This is BL5 directly: outside U every column is the single point (x, h).

4. LEMMA TR (two sea rows of opposite parity). Let y0 < y1 have opposite parity with 2y0 - y1 < 1 and 2y1 - y0 > h, and suppose 4j(y1 - y0 + j) is not a square for 1 <= j <= min(y0 - 1, h - y1). Then no configuration inside rows {y0, y1} contains a corner triple, a mixed quadruple or a rival pair.
Proof:
- Corner triples: as in the paper's Lemma sea. Two corners in one row are opposite (F3), so the fourth corner is in row 2y0 - y1 or 2y1 - y0, outside [1, h].
- Mixed quadruples: Lemma sea's parity argument, which uses only that y0 + y1 is odd.
- Rival pairs: Lemma rival needs exactly the excluded square.
- With no tilted rectangle having 3 black corners, there is no V1, V2 or V3 violation either.
For (y0, y1) = (L, H), the conditions follow from T1:
- 2H - L > h, because H - L > H - F > 2(h - H) >= h - H, by (9).
- 2L - H < 1, because H > F + 2(L - 1) >= 3L - 2, by (9).
- The squares are excluded by (7), since min(L - 1, h - H) <= L - 1.
For adjacent rows (y, y+1), each a contiguous interval of columns, the points form a monotone chain: use Lemma chain, after reflecting x -> -x for the left collar. A rival pair would need j(j+1) to be a square, and j^2 < j(j+1) < (j+1)^2.

5. LEMMA C (the label-free block B0 is clean). B0 is B with every slot holding F. Its stages, left to right, are: row h, C_{h-1}, ..., C_H, Phi, the periodic region (P, cores, separations, P), Phi, C_H, ..., row h.
- Every stage other than the periodic region has length >= D.
- A violation Q (V3 pairs included) lies in D consecutive columns, so its column span is at most D - 1. Q therefore cannot contain a whole stage of length >= D together with a column on each side, and it meets at most two consecutive stages.
- Periodic region with Phi: this is s_pi with some F replaced by H, which is clean by the hole-choice property (I1, Section 6, audited).
- Phi with C_H: only rows L and H appear, so Lemma TR applies.
- C_y with C_{y+1}, or C_{h-1} with row h: adjacent rows, so Lemma TR applies.

6. CLAIM (d). Let Q be a violation of B. It has at most 7 columns, and a 'point' of Q includes W.
- Suppose Q has a point in some core K_c. Then Q lies in K_c^+ = K_c widened by D - 1 on both sides. By BL3 and BL4 (P and the separations have length >= D), every non-label column of K_c^+ holds s_pi, and its only label columns are those of c. So B agrees on K_c^+ with C_c, the infinite periodic sea with class c substituted, and Q is a violation of C_c. But C_c is violation-free (I1 + I2).
  - compatible Section 4: every forbidden support has 0 labels (the sea), 1 label (one-label substitution at any period-zero column with F elsewhere) or at least 2 labels (E_J avoided).
  - T1's list excludes every tilted rectangle with 3 or more black corners, so no V2 or V3 can arise. A rival pair or mixed quadruple with at least 2 labels is in G_J.
- Otherwise Q avoids every core, and B agrees with B0 on Q's columns, which contradicts Lemma C.

7. CLAIM (e). J5 needs two things: each window with its constant tail is violation-free, which is (d) with (c); and windows are separated from each other and from z by more than 2W_h columns, which is BL6. The rest of J5's proof applies unchanged: outside the windows, row 1 for x < z and row h for x >= z form a chain, and Lemma rival excludes rows 1 and h.

8. CLAIM (f).
- Under rules 1, 2', 3, 4 the destinations partition the labels. Each label takes the first rule that fits, and rule 4 is the default.
- Rule 1 and rule 2' receive only labels of S (both use T1), and the heavy and light diagonals are disjoint.
- The groups D_j partition the light diagonals.
- E_{D,j} and Bad_split minus S go to Proposition partial (R-g, R-d).
- Each destination places each received label once as a double, with singletons elsewhere: the light regions by V2-8, partial by P2, and D/E blocks by (a) and (b).
- The windows are disjoint, and (i, j) -> {2i+1, 2j+2} is a bijection from labels onto parity edges. So K8' holds.
- Truncation keeps every double, since all doubles lie in columns <= M.
Check of the K6 order: R_j depends only on the classes, psi and S, not on (l, p), because Bad_split is defined from the types and fillers. So the D blocks are fixed before (l, p) is drawn.

9. LEMMA RL. Take a violation of the restricted configuration, and let J ⊆ c' be the labels with a point (or W) in their column.
- |J| = 0: the sea.
- |J| = 1: one-label substitution (I1).
- |J| >= 2: every other point lies in a sea row, so the geometry is counted in G_J, which ignores the periodic pattern. Then E_J occurs for X_c restricted to J, which X_c avoided.
- If W lies in a label column whose label has no black corner, the rectangle's black corners use J' with |J'| >= 2 (killed by E_{J'}), or |J'| <= 1 (no such rectangle exists by I1).

10. DEFINITION-LEVEL CHECK (sanity only; scripts in the script folder).
Method:
- The validated checker (core.py and checker.py, copied unchanged) runs over windows [a, a + 2D) with stride D, which contain every obstruction.
- Label windows are checked twice. First, anchored at label points and at every white cell of the label columns. Second, with the label columns emptied and every point anchored, discarding records whose W lies in a label column. Together these find every record.
- Profiles satisfy (1), (2), (7), (8) and (9). Label rows satisfy (4) and (6), plus the vertical-rival filter (10) restricted to the cases where Lemma rival can apply (opposite parity, j <= min(lower - 1, h - upper)). The literal (10) leaves almost no rows at these h.
- Classes are split at the median of v. Centres are drawn at random among N slots, and labels in any record are resampled until clean. Strict mode also resamples parked rectangles that have a label corner.
- Segment lengths are D.

Results at h = 112, profile (3, 9, 110, 2), D = 6163:
- The 108 candidate labels: 0 one-label records, and 0 parked triangles.
- The empty block (sea, both collars and tails): 0 records.
- E block: whole diagonals T = -7, 7, 21 (23 labels), two classes with N = 330 and 360, strict mode. Random first placements had records (for example 6 V2), and resampling took 28 and 11 rounds.
- D block: |S| = 18 on T = 3, 35, -21. Y is a Bernoulli(1/2) subset with 7 labels; one label goes to E_D and 6 are placed in N = 30|S| = 540 slots, leaving 1201 unused slots holding F.
- Layout: row 1 (D) | z | E block | D block | row h. Width 150371, 24 windows, records V1-V5 all 0.
- Bookkeeping: 29 doubles, all distinct, equal to E plus (Y minus E_D). E_D is not placed. Every other column is a singleton. Both blocks start and end in row h.

Results at the other heights:

| h | Profile | Labels | Blocks | Width | Records |
| --- | --- | --- | --- | --- | --- |
| 129 | (3, 15, 126, 4) | 117 | E with 26 labels; D with 21 placed from \|S\| = 33 | 241857 | 0 |
| 111 | (4, 20, 105, 3) | 18 | Small E and D blocks | 238806 | 0 |

At h = 129 the doubles are exactly the received labels. At h = 111, L is even and the staircase C_105, ..., C_110 has 6 steps.

Controls:
- Wrong-residue labels gave a one-label record in 56 of 60 cases.
- Two independently placed classes interleaved with no separation gave 9 records (26 in strict mode).
- Restricting clean classes to random halves gave 0 records in 20 trials, both modes, consistent with Lemma RL.
- Each run took under 20 seconds.

## External results used

- Paper (rectangle-blackouts, papers/extremal/sections/sec5_threshold.tex): 2W_h+1 locality, Lemma rival, Lemma sea (its parity step), Lemma chain, Proposition partial (a) and (c). sec2_prelim.tex: Lemma mixedeq and Lemma criterion.
- filled_mod7_profile_cover.md (2026-11-09, independently audited): profiles (1)-(3), the filters (7)-(10), one-label substitution, and the Section 6 collars with the hole-choice property.
- compatible_profile_threshold.md Sections 3-4 and two_moment_threshold_refinement.md (8): bad events, the placement local lemma and the coincidence events.
- t1_cost_decomposition.md Theorem E (E4)-(E5) and polylog_relocation_diluted.md Theorem D (D4) and Lemma M1 (audited A9/A10): the slot counts N_w and the existence of placements.
- full_layout_junctions.md J5 (audited A9).

## Checks

I read these in full: consolidated_board_v2.md; polylog_relocation_diluted.md (Lemma M1, Theorem D and D1-D4, Theorem IV); t1_cost_decomposition.md (Theorem E, E1-E5) and its audit (Theorem E, the tail fix); full_layout_junctions.md (J1-J5); two_moment_threshold_refinement.md, filled_mod7_profile_cover.md and compatible_profile_threshold.md; the paper's sec5 (locality, Lemmas rival, sea and chain, Proposition partial (a) and (c)) and sec2 (Lemma mixedeq, Lemma criterion). I read by grep: the E4 and K8 items of the audits of polylog, junctions, constant lists and table completeness, and the collar lines of filled_mod7_independent_audit.

By hand I checked:
- the two-row inequalities 2H - L > h and 2L - H < 1 from (9), and the rival range of (7);
- the stage-crossing argument (span <= D - 1 against stages of length >= D);
- injectivity, the partition by profile and class, and the coincidence terms in compatible Section 4 and D4;
- that R_j does not depend on (l, p), which fits the K6 order;
- the failure of the unamended rule 2, through the smallest R_IV edge (u = 349).

Scripts, one at a time with py, each under 20 s and well under 1 GB, all in the script folder:
- blib.py: profiles, layout and windowed checker;
- search_prof.py;
- run1_onelabel.py: one-label and empty-block checks;
- diag1.py and diag2.py: parked count and slot-count trials;
- run3_eblock.py: E block, switch and bookkeeping;
- run4_global.py: E and D blocks, switch and bookkeeping;
- run5_controls.py;
- run6_param.py: h = 129 and h = 111.

The rectangle-blackouts repository was only read, no git command was run, and no report file was written.

## Gaps

- Not audited: Theorem N1, Lemmas TR, C and RL, and the amendment of (B7) rule 2 still need a second-reader audit.
- N1 cites I1 to I4 and does not re-derive them: the T1 profile theorem with its hole-choice collar property, the existence of centre maps from T1 (8), compatible Section 4 and Theorems E and D, the paper's lemmas, and J5. Two facts are read from compatible Section 3, not re-proved: the bad events E_J ignore the sea pattern, and T1 excludes every tilted rectangle with 3 or more black corners and at most one label. Lemma RL and the step 'C_c has no (V1)-(V5) violation' rest on them.
- The amendment to (B7) rule 2 (Bad_split ∩ S) is not in consolidated_board_v2. Without it N-1 fails: shallow R_IV ends with rows below T1's bulk (5000) would be sent to Theorem D blocks.
- h0 must also be at least T1's profile range (filled_mod7 Section 3 assumes h >= 10^10). The hypothesis list states h0 >= 424. Theorem N is non-explicit anyway, but the list should be corrected.
- The definition-level check runs far below T1's constants: h near 110 against h >= 10^10, F of about 9-20 against F in [1000, 3743], bulk rows set by (6) only, collar segments of length 2W_h+1 against 2h^2, a vertical-rival filter restricted to the Lemma rival cases instead of the literal (10), resampling instead of the local lemma, and a median class split instead of dyadic classes. It tests the layout rules and the junctions, not T1's constants or N_w bounds.
- No Proposition partial window (case (a) or (c)) was built next to the D and E blocks. That junction rests on J5 and the paper.
- N-3 (K6 uniformity), the V2 steps other than V2-8(b), and the completeness of the K2 and K4 lists are untouched. Theorem N stays conditional on them.

## Missing estimate

None for N-1. No counting estimate is involved: N-1 is a layout fact, proved from the explicit layout BL and the audited existence of class placements. What remains is an audit of this note and folding rule 2' (Bad_split ∩ S) and h0 >= 10^10 into the board.

## Next steps

- Have a second reader audit Theorem N1 (claims a-f), Lemmas TR, C and RL, and the rule 2' amendment. Each step is short and elementary.
- Fold into consolidated_board v3: rule 2' 'Bad_split ∩ S, not in E_D -> Theorem D'; h0 >= max(10^10, ...) in Theorem N; N-1 moved from CIT to N (this note) pending audit; E4 and W2 cells cite N1(c)-(e).
- Optionally build a definition-level Proposition partial window (case (a) for even h, case (c) for odd h) next to the D and E blocks, to test the remaining J5 junction at definition level.
- Turn to N-3 (K6 uniformity), now the main unaudited hypothesis of Theorem N, together with the audit of the V2 steps and of the K2 and K4 lists.
- Scripts: scripts_blocks/blib.py, run1_onelabel.py, run3_eblock.py, run4_global.py, run5_controls.py and run6_param.py, all in that folder, with the copied core.py and checker.py.

