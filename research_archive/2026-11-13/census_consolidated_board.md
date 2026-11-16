# Definition-level census of the consolidated board

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (computational): at h = 429 and 451 (all 512 types) and h = 701, every violation of a validated (V1) to (V5) checker matches a family of the table, and Table J1* holds exactly at the seams. Two short proofs: blocks never interact for h <= 5117, and no light label survives (B7) for h <= 652. Finding: (B7) omits D11 (one label plus filler M2c), which leaves 176 bad labels at h = 701; the fix is to add D11 to the relocation list.

# Result

## Status

partial

## Summary

Definition-level census of L*** at h = 429 and 451 (all 512 types), plus h = 701: every violation matches a table family, and Table J1* holds exactly at the seams. At h <= 652 no light label survives (B7), and for h <= 5117 two blocks never interact. (B7) omits D11.

## Statements

These are computational facts plus two short proved observations. Nothing here proves the near goal.

(O1) PROVED: at true spacing, blocks never interact for h <= 5117. Take two distinct subclasses of one region type. Their positions differ by Dt with 16 | Dt and Dt != 0. So their label columns are at least 64p - 4(A-1) > 2558h apart, which exceeds 2W_h + 1 for every h <= 5117. Labels of different types sit in different regions, which margins and buffers separate by more than 2W_h + 1. So for h <= 5117 no obstruction and no V3 pair holds labels of two blocks. The cross-class families (A4, A5, B7, D16 to D18, and cross-class D20/Q3) are empty at these heights, for every admissible (l, p), kappa and b_tau.

(O2) PROVED, plus an exact count: for h <= 621 the (B7) rules (near band, an endpoint row >= T* - 320; R2', 2i+1 <= 300) remove every light label. Enumerating all 512 types shows that this persists up to h = 652. The first height with a surviving light label is h = 653 (82 labels). At h = 701, 3586 light labels survive.

(C1) COMPUTED, after validation: the checker is a definition-level (V1)-(V5) finder. It enumerates by divisors over the set of occupied rows, anchored at one point. On random boards it agrees exactly with a naive search over all rectangles and mixed pairs, kind by kind. On random equality boards, "some (V1)-(V5) violation" agrees with "two rectangles share a presentation".

(C2) COMPUTED: the pure SAW*-shift gap with its row-1 or row-3 sea has no tilted rectangle with 3 or more black corners, no mixed quadruple and no rival pair. This holds for every (r0, T*) that occurs at h = 429, 451 and 701 (32 cases each, including all k = 1 and k = 2 shifts). The check is complete, because the pattern is periodic.

(C3) COMPUTED: the seam census SAW*-shift | Sea(r0, g) matches Table J1* together with the phase rule (Phi) exactly, in all 389 jobs at h = 429 and 451 (both ends, all four phases in the cases with a bad pair or a shift). The only seam violations are the predicted filler/row-g rival pairs (o, kappa, j). The unshifted controls fail at every phase, with kappa = 4 (j = 1) in row-3 types and kappa = 6 (j = 3) in row-1 types at h = 3 (mod 4). At h = 701, all 64 seams at the board's phases are clean. The buffer pieces, the chain seams and the switch row-1 | row-h are clean at h = 429, 451 and 701.

(C4) COMPUTED: a label-centric census of every subclass of all 512 types at h = 429 and at h = 451. In the relaxed mode only i = 0 and the row-3 rules are applied, so 45370 and 50178 light labels are kept. Every violation falls in D10, D7 (FFo with a label vertex, W in the label column), D4, D11, D12 or D13. None falls in a family that the table claims is empty, and none matches no family. There is no 3L1F (Q3), no D15, no D21/Q4 configuration, and no label-only or label+sea violation.

(C5) COMPUTED: at h = 701 in exact mode, with the (B7) rules applied, all 344 types with survivors hold 3586 labels. Only D10 (895 labels) and D11 (176 labels) occur. After those 1020 labels are removed, the remaining 2566 labels give zero violations (J3 closure, checked at definition level).

FINDING: (B7) lists 'D9, D10, B7, A4, D20' but not D11 (one label + filler M2c). Section 3 counts the D11 labels under '[M2c]', but as written the board keeps 176 labels at h = 701 that sit in black D11 quadruples. (B7) needs D11 added.

## Proofs

SETUP. Script folder: scripts_census/. The repository was only read. Every script ran with py, one at a time, each under 60 s.

1. THE CHECKER (core.py, checker.py)
A board window is a set of columns, each holding at most 2 black rows. R is the set of occupied rows: sea row r0, the 4 filler rows, row g in seams, and the label rows. Every enumeration is complete for the stated anchor.
- Rectangles with 3 or more black corners that contain a black point P:
  - P is the vertex: for rows yF, yG in R, the side vectors (a, yF - yP) and (c, yG - yP) satisfy ac = -(yF - yP)(yG - yP), so (a, c) runs over the signed divisor pairs.
  - P is adjacent to a black vertex V: the same equation with V's row in R.
  - Every rectangle whose W row is outside 1..h is discarded.
- Rectangles with white corner W and three black corners: the same enumeration from W, used for V2 with W in a double column and for V3.
- Black mixed quadruples with P = A or P = C (by the A<->B and C<->D symmetry, this covers every support that contains P):
  - The rows fix u_y, w_y and n_y = (y_C + y_D - y_A - y_B)/2.
  - If Q = w_y^2 - u_y^2 != 0, then (u_x - w_x)(u_x + w_x) = Q gives finitely many (u_x, w_x), and n_x = -n_y u_y/u_x must be an integer.
  - If Q = 0, then w = (-u_x, u_y) or (u_x, -u_y), and u_x runs over the divisors of n_y u_y.
  - The checks are: A, B, C, D black; p, q in rows 1..h; D - C != +-(B - A); u_x != 0. A vertical AB is the rival-pair case.
- Rival pairs: rows c < c' with c' - c odd, and 4j(c' - c + j) = t^2 with c - j >= 1 and c' + j <= h.
- Parking: W is parked iff every black point of its column has W's parity. V3 means at least 2 parked rectangles at one W.
- Points outside the window are counted as oob. oob was 0 in every census run.
Validation (validate.py):
- Kind-level set equality of V1, V2, parked-W V3, V4 and V5 against a naive search over all rectangles and all mixed pairs of the grid. Random boards had h 4 to 7 and m 5 to 14: 300 + 40 + 30 + 60 + 80 + 60 boards. A further 127 boards had h 9 to 12 with 3 to 6 occupied rows. All sets were equal. The naive totals were, for example, [84, 844, 42, 507, 103].
- Validity agreement on random equality boards (every parity edge as a distinct double, h = 4 and 5): 30000 + 3000 + 3000 + 2000 + 2000 boards. Agreement was 100%; 77 of the first 30000 were valid.
- I re-ran the validation after each kernel change: the required-row pruning, and the batched and row-masked W enumeration.
- verify_instances.py re-checked reported instances from scratch, by rebuilding the window and testing the equations of Lemma mixedeq and Lemma rival and the corner and parity conditions. It checked 400 random h = 701 instances, all 352 D11 instances at h = 701, all 26 D13 instances at h = 429 and 200 random h = 429 instances, with 0 failures.

2. THE BOARD (lstar.py), as in consolidated_board.md (B1)-(B10)
- A = ceil(h/2), K = floor(h/2), W_h = floor((h-1)^2/4) + 1, B = ceil((ln h)^1.5): 15 at h = 429, 16 at h = 451, 17 at h = 701.
- Primes: the least admissible l in (1.04h, 2.08h] with l = +-2 (mod 5), and the least admissible p in (40h, 80h] with p = 3 or 7 (mod 20). That gives (l, p) = (457, 17167), (487, 18043) and (733, 28087).
- Types: tau = (iota, sigma), with r0 = 1 for iota odd and r0 = 3 for iota even, and y_P = 2iota + 1 (mod 64). T0 is the largest y <= h with y = y_P + 32 (T = 3 mod 4) or y_P + 48 (T = 1 mod 4) (mod 64). D0 = h - T0, k from Table J1*, and T* = T0 - 64k.
- Fillers: deep slot n gets row T* - 24 + 8((n - rho0) mod 4). Shallow columns get (x, r0). Removed labels leave fillers (holes).
- Classes:
  - D_T = {|d| : 16d^2 + (2d + T)^2 = L^2, 0 < L < h, |d| < n_T} (stride_menu.md, Derivation 2), and kappa_T = |D_T|. No diagonal was heavy at h = 429, 451 or 701, so the Theorem E side is empty there.
  - Greedy colouring of G_T in increasing i, then restriction to i = iota (mod 32), then a split into floor(B/c_T) subclasses by iid uniform psi (seed 1).
  - Subclass k of diagonal s sits at t = rho_s + 16lk, with rho_s = p^(-1)(s - kappa) mod 16l, kappa = b_tau = 0, and label slot n = i + pt.
- Subclass sizes over all types: at h = 429, sizes 1/2/3/4/5 occur 34499/4755/432/15/1 times; at h = 451, 39061/4922/381/30/2 times.
- Modes:
  - relaxed: remove only i = 0, and i = 2 or j in {0, 1} in row-3 types.
  - exact: also remove the near band (an endpoint row >= T* - 320) and R2' (2i+1 <= 300).
  - exact2: exact, and also remove the labels that the h = 701 census put in D10 or D11 (the relocation rule).

3. (O1), PROOF. Within a type every s is sigma (mod 16). t_c = p^(-1)(s_c - kappa) (mod 16l), and p is odd, so Dt = p^(-1) Ds = 0 (mod 16). Dt != 0:
- on one diagonal, the k differ;
- on different diagonals, 0 < |Ds| < h < 16l, so the residues mod 16l differ.
So |Dt| >= 16, and the label-column distance is at least 4(16p) - 4(A-1) > 2560h - 2h. Since 2W_h + 1 <= (h-1)^2/2 + 3, this exceeds 2W_h + 1 while h <= 5117 (the first failure of 64 * 40h - 4A > 2W_h + 1 is h = 5118). Different types lie in different regions, separated by more than 2W_h + 1 columns ((B9): pure margins plus a Sea(r0, g) piece of width 2W_h + 1). Every obstruction and every V3 pair lies in 2W_h + 1 consecutive columns. Numerically, over all 512 types, the least gap between subclasses was 7.69e6 columns at h = 429 and 1.15e6 at h = 451, against 2W_h + 1 = 91595 and 101253.
(O2), PROOF. A survivor needs 2i+1 >= 301 and 2i+1 <= T* - 321 <= h - 321, so h >= 622. The enumeration over all 512 types gives 0 survivors for every h <= 652, and 82 at h = 653.

4. PURE GAP (pure_gap.py). The pattern is 16-periodic. The anchors were all 16 black points of one period, with a margin of 2W_h + 64. Results:
- 32 distinct (r0, T*) at each of h = 429, 451 and 701, including T* = 245, 317 and 325 (row-3 types at h = 429, k = 2 and k = 1) and the k = 1 row-1 types at h = 451. All have zero violations and zero rectangles with 3 or more black corners (so zero parked triples).
- Positive controls at h = 429: T* lowered to 150, 200 or 230 (so T* - 24 <= (h+1)/2) gives 78 to 99 V3 collisions among parked FFS triples. Random period-16 filler rows give 206 violations.

5. SEAMS (seam_batch.py, seam_jobs.txt, seam_report.py; logs seam_*.log and s701_*.log)
- The window is the seam +-(4W_h + 160). The anchors were every SAW* filler within 2W_h + 16 of the seam, which covers every violation that contains a filler and a row-g point. The enumeration was restricted to combinations that contain row g. Because the pure gap has no parked rectangle, V3 coverage holds.
- Jobs at h = 429 (g = 428):
  - all 16 row-3 D0 values, both ends, all 4 phases;
  - k = 0 controls for D0 = 40, 48 and 56;
  - row-1 D0 = 2, 14, 30, 46 and 62, all phases.
- Jobs at h = 451 (g = 448):
  - all 16 row-1 and all 16 row-3 D0 values;
  - all 4 phases at the bad-pair and shifted cases, and phase 0 elsewhere;
  - k = 0 controls for row-1 D0 = 24, 32, 40, 48 and row-3 D0 = 42, 50, 58.
- Results:
  - 389 jobs, oob 0, and no non-rival seam violation.
  - The bad phases and the observed (o, kappa, j) equal the prediction of Table J1* with (Phi) in every job. For example, h = 429 row-3 D0 = 0 has (1,2,1), with bad right phases {2,3} and bad left phases {0,1}. h = 451 row-1 D0 = 4 has (2,3,3).
  - Every k = 1 or k = 2 shift is clean at every phase.
  - Unshifted controls: (0,4,1), (1,4,1) and (2,4,1) at h = 429 D0 = 40, 48, 56; (0..3, 6, 3) at h = 451 row-1 D0 = 24 to 48; (0..2, 4, 1) at h = 451 row-3 D0 = 42, 50, 58. All fail at every phase.
- At h = 701, all 64 (r0, D0, end) seams at the board's phases ((Phi) for the k = 0 bad rows, phase 0 otherwise) are clean.
- j2.py checked the pieces row-1 tail, Sea(1,g), all-g, Sea(3,g) and row-h tail, and the seams tail1|Sea1, Sea1|allg, allg|Sea3, Sea3|allg, allg|Sea1, Sea1|tail1 and tail1|tailh, at 4 seam phases each. All are clean at h = 429, 451 and 701. Control: h = 39 with g = h - 1 gives 9 rival pairs at the allg|Sea3 seams (the failure J2 predicts).

6. CLASS WINDOWS (census_class.py, census_multi.py, classify.py; logs cls_*.log)
- Each subclass with kept labels gets its own window: its label columns +-(2W_h + 64). By (O1), no other label lies within reach.
- Anchors: every label point, and every white point of a label column.
- Labels removed from a window leave the filler pattern, so obstructions with no label point and no W in a label column are pure-gap obstructions (section 4: none).
- The classifier maps each violation to a row of table section 4 by kind, by the tags of its points (S sea, F filler with its offset, o, e, g) and by the shallow pattern. D12/D13 is decided by homogeneous filler rows and the sign of d. Q4/D21 is flagged when, in a row-3 type, there is no shallow black point and p, q or W lies in rows 1-2. Unmatched cases are tagged UNLISTED.
- Results, relaxed mode, all 512 types at h = 429 (45370 labels):
  - D10 (even label + filler rival pair): 49216 pairs, 25879 labels. The label point lies from 203 rows above to 383 rows below the lowest filler row.
  - D7 (FFo, label vertex, W white in the label column): 10216, with the label at most 152 rows below the lowest filler row. This fits 'empty under X >= 234'.
  - D4 (FF/Fo, Theorem 1(6)): 6816. The label point is always exactly 8 rows below the lowest filler, that is row T* - 32.
  - D11 (So/FS, one label + filler M2c): 4666, with the label 24 to 344 rows below the lowest filler.
  - D11 (FS/So): 1064, with labels only 40 to 120 rows above the lowest filler, so near band only.
  - D12 (d > 0): 137 Fo/Fo and 4 Fe/Fe.
  - D13 (d < 0, Fe/Fe): 26.
- Results, relaxed mode, all 512 types at h = 451 (50178 labels): the same families, with 56928, 12544, 7168, 5160 + 898, 148 + 5 and 23 instances.
- Over all logs: 0 UNLISTED; 0 instances of A1 to A5, B1 to B8, D1, D5, D6, D8, D9, D14, D15 or D19 to D22; no V1 and no V3.
- Unsplit-class stress (K_T = 1, 16 types at h = 429): the same families, with D12 at 39.
- Exact mode at h = 701, all 344 types with survivors (3586 labels): D10, 1457 pairs on 895 labels; D11 So/FS, 352 quadruples on 176 labels (label odd rows 307 and 309, label 344 rows below the lowest filler). Nothing else.
- exact2 at h = 701, with those 1020 labels relocated: 2566 labels and zero violations.
- Positive control (control_class.py): 16 consecutive labels on one diagonal at stride 1, which breaks the offset-0 rule, give 252 violations, including A2 rival pairs at distances in D_T.

7. FINDINGS ON THE SPECIFICATION
- (B7) omits D11. At h = 701 it matters: 176 surviving labels are in black D11 quadruples. The fix is to add D11 to (B7)'s list, in line with the '[M2c]' term of section 3.
- D10 is 'harmless' only asymptotically. It hits 57% of the light labels at h = 429 and 451, and 895 of 3586 survivors at h = 701. Its rival pairs reach even rows as low as 8 (j = 1, d + 1 a square).
- At the heights the target names, the census tests the pure parts, the junctions and the near-band families, not deep survivors: by (O2) the board has no light label there. The h = 701 run is the only test with true survivors, and its subclasses hold one label each.

## External results used

- None used beyond elementary facts (divisor enumeration, trial-division primality). No web sources were consulted.

## Checks

Validation: kind-level set equality against a naive all-rectangles and all-mixed-pairs search on about 700 random boards (h 4 to 12). Validity agreement with naive presentation collisions on about 40000 random equality boards. Re-run after every kernel change. Re-verification from scratch of 978 reported instances. Positive controls: the pure gap with low T*, random filler rows, J2 at h = 39 with g = h - 1, bad seam phases, and a stride-1 label control. oob = 0 in every census. Runs, all under 60 s each, logs in the script folder:
- pure_gap.py: h = 429, 451, 701 (96 cases);
- seam_batch.py: 389 jobs at h = 429 and 451, 64 at h = 701;
- j2.py: h = 429, 451, 701, plus the j2g.py control;
- census_class.py / census_multi.py: relaxed at all 512 types at h = 429 and 451, unsplit on 16 types at h = 429, exact on all 344 h = 701 types with survivors, and exact2 after relocation.
Scripts: core.py, checker.py, validate.py, lstar.py, classify.py, pure_gap.py, seam_batch.py, seam_report.py, j2.py, j2g.py, census_class.py, census_multi.py, cls_batch.sh, cls_list.sh, cls_report.py, refine.py, verify_instances.py, control_class.py, all in scripts_census/.

## Gaps

- The near goal is not addressed by proof. Q1 to Q5, (AP) and the audits U1 to U8 remain open. This is a finite census.
- The target asked for 2 or 3 interacting blocks. That is impossible in L*** for h <= 5117 (O1), so no cross-class family (A4, A5, B7, D16 to D18, cross-class Q3) was or could be exercised. Their status matters only above h of about 5100.
- At h <= 652 the exact board has no light labels (O2). So the census at h = 429 and 451 is either label-free (exact) or a near-band census (relaxed). The only survivor test is h = 701, which is outside the requested range [424, 520] and has subclasses of size 1, so no two-label family can occur there.
- Subclasses are tiny at these heights (86% hold 1 label, at most 5), so the evidence against Q3 (3L1F), D15 and D21/Q4 is weak. Large classes appear only at much larger h.
- Only one psi seed, one (l, p) pair per height (the least admissible) and kappa = b_tau = 0 were used. By (O1), (l, p), kappa and b_tau do not affect in-class content at these heights, but psi does.
- Not built or checked: Proposition partial windows, Theorem D blocks (E4), Theorem E blocks (none needed: no heavy diagonals at h = 429, 451 or 701), J5 gluing, the global 'every parity edge exactly once' condition, and truncation to columns 1..m.
- Windows use the strip reading (columns unbounded), which the audit says is the stronger form for the 'if' direction. The grid reading was used only in validation.
- Family names come from my classifier: it uses point tags, the shallow pattern and filler-row equality. The D2/D7 and D12/D13 assignments follow the table's wording, not a re-derivation of each theorem's hypotheses.
- The seam census used the required-row (g) pruning. It is complete for violations that contain a filler and a row-g point, and it relies on the pure-gap result (no parked rectangle) for V3 coverage. The pure buffer was checked separately (J2).

## Missing estimate

This census proves nothing about the missing estimates. It shows that Q1 and the cross-class part of Q3 only matter for h > 5117, and that Q3 in-class, Q2 and Q4 produce no instance at h = 429 and 451 in any subclass of L***. Those subclasses hold at most 5 labels, so this is weak evidence. The near goal still needs Q1 to Q5 and (AP).

## Next steps

- Amend (B7) to relocate D11 (one label + filler M2c) explicitly, and say in section 3 that the [M2c] term includes D11.
- Add (O1) to consolidated_board.md: for h <= 5117 no two blocks interact, so every cross-class family is asymptotic only. Add (O2): no light label survives (B7) for h <= 652.
- To test two-label and three-label families against survivors, run the exact census at h of about 1500 to 3000. The kernel cost depends on the occupied rows, not on W_h, so this should be feasible in a few runs per type. Subclasses there hold about h/(64B) labels.
- Use the checker as the definition-level seam audit U1 (Lemma J1*): the census reproduces Table J1* and (Phi) exactly at h = 429 and 451. An auditor can re-run seam_batch.py at any h.
- Run the same census on the Theorem D and Proposition partial windows (E4) once their layouts are fixed.
- Quantify D10 at moderate h. It removes a majority of light labels at h of about 450 and 25% of survivors at h = 701, so the constant in O(h^(3/2)) is large.

