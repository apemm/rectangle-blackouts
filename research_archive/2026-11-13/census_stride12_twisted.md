# Census of the stride-12 board with the twisted rule

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (computational): 45 single-type censuses of the twisted board L***(3) at h = 429 to 1501 found only listed families that the table does not mark empty (D4, D7 near-band, D10, D11, D12), and nothing unlisted. On the 29 runs that repeat the untwisted census, the output is identical instance by instance, and a short proof explains why: within one subclass the twist only translates the window, so up to h = 9717 a windowed census cannot tell the rules apart. The deep runs at h = 1201 and 1501 contain 29 D12 instances (as predicted) and 4023 parked intra-class SLL-Pc triples matching the corrected audit formula. Cross-class cells are vacuous at these heights.

# Result

## Status

partial

## Summary

I built the twisted board L***(3) at definition level and ran 45 single-type censuses at h = 429 to 1501. Every violation is in a listed family that the table does not mark empty: D4, D7 near-band, D10, D11 and D12. Nothing is UNLISTED. On all 29 runs that repeat the untwisted census, the twisted output is identical instance by instance (3826 = 3826). I prove why: within one subclass the twist only translates the window, so up to h = 9717 a windowed census cannot tell the two rules apart. The new deep runs at h = 1201 and 1501 also have no unlisted family. They contain 29 deep two-label D12 instances (predicted = observed), and 4023 parked intra-class SLL-Pc triples match the corrected audit formula exactly.

## Statements

Scope: Problem 001, the stride-12 board L***(3) built exactly as stride_transfer_core.md defines it.
- (B2'): l is the least prime in (1.04h, 2.08h] with (37/l) = -1. p is the least prime in (76h, 152h] with p = 3 (mod 4) and (37/p) = -1.
- (B5'): rho_s = p^(-1)(3s - kappa) mod 16l, t = rho_s + 16lk, slot n = 3i + pt + b, column 4n, with kappa = b = 0.
- D_T, kappa_T, the heavy threshold B/4, G_T[tau], the colouring law, the removal rules, T*, the fillers and the sea are unchanged from census_stride12 (lstar12.py).

PROVED (short proofs in the proof field):
- (P1) Same classes. For every (h, type, colour mode, rule mode, seed), the twisted and untwisted builds give the same list of subclasses (s, colour, label set). Only the column offset M_c = p t_c differs.
- (P2) Translation invariance. For each subclass c, the census window of c under the twisted rule is the untwisted window shifted by 4 delta_c columns, with delta_c = M_c(tw) - M_c(untw). This holds point for point: the arrays R1 and R2, the tags, the label map and the anchors all agree in window coordinates. So the census of each window gives identical (V1)-(V5) output under both rules.
- (P3) Twisted (S2). Two subclasses of one type have Delta t a nonzero multiple of 16. So their label columns are at least 4(16p - 3(A - 1)) > 4858h apart. This exceeds 2W_h + 1 for every h <= 9717.
  - Corollary: for h <= 9717, the windowed census of L***(3) is the same under the twisted and untwisted rules, label by label. Every difference between the rules lies in cross-class configurations, and those are empty at these heights.
- (P4) Type phase. Every label slot has n = rho_tau = 3(iota + sigma) - kappa_tau (mod 16), with kappa_tau = kappa - b = 0. This differs from census_stride12's 3 iota + sigma by 2 sigma. So rho0 changes by 2 exactly when sigma is odd. The rule (C7) holds: n - 3j is constant mod 16l on each type.
- (P5) Parked intra-class Soo rectangles are exactly the family of audit_stride_transfer_core issue 1. These are rectangles where W is parked and the black corners are one shallow point S and two odd label points of one class. Write G = V + (12t, 2t) with t > 0, t in 32Z, and E = V + (u_V/3, -2u_V) with u_V = (y_V - r0)/2, which is always odd. The vertex is always the lower label V, and the condition is 3 | u_V and r0 + 2t <= h. A vertex at G puts W in row r0 - 2t < 1. A vertex at E fails mod 8.
- (P6) B6 (R_IV(3) at k = 5) is vacuous for h <= 2905. The least k = 5 edge is (1165, 1453), so a fatal pair needs u_D >= 1453 > (h - r0)/2.
- (P7) Deep D12 instances found here have Delta i = 32 or 96 <= 210, so R_FF^+ covers them.

COMPUTED (each py call ran one type, sequentially, under 60 s):
- (C1) 45 runs. Every violation is one of the following:
  - D10: 4981 (2677 near-band; 2304 deep);
  - D7 (FFo) with one label: 664, all near-band;
  - D7 with two labels: 28, all near-band;
  - D4: 264, all near-band;
  - D11: 376 (120 near-band; 256 deep);
  - D12: 52 (23 near-band; 29 deep).
  - There were 0 UNLISTED, 0 V1 and 0 V3, and oob = 0 in every run.
- (C2) The 29 runs that repeat the untwisted census_stride12 runs give identical violation multisets (3826 = 3826). An untwisted control at h = 1201 is also identical (231 = 231).
- (C3) Parked Soo observed = predicted by (P5) in all 45 runs: 4023 = 4023, all with the predicted shape, and none at a V3 point.
- (C4) D12/D13 predicted from the stride-12 cubic equals observed on the 6 deep types where the scan predicts any (1, 4, 4, 7, 12 and 1 quadruples). On all 512 types at h = 1201 and 1501 (stress, exact), the cubic predicts no D13 quadruple.

## Proofs

SETUP
- script folder: scripts_census_u3_twisted/.
- I copied core.py, checker.py, classify.py, lstar.py, lstar12.py, census12.py and verify12.py byte for byte from scripts_census_u3 and checked each with cmp. core.py is also identical to scripts_census/core.py, the validated kernel. I copied the untwisted logs into untw/. The repository was only read, and I ran no git command.
- New scripts:
  - lstar12t.py: the twisted board (B2') and (B5'). It reuses lstar12's diag_graph12, colour and removal, with the same random stream.
  - census12t.py: the census12.py driver with the same windows, anchors, kernel and classifier, plus analysis of every parked W.
  - stats12t.py: structural checks over all 512 types.
  - cmp_tw.py: compares the twisted and untwisted violation multisets after deleting the window origin X0.
  - verify12t.py: verify12.py with the twisted build. It rebuilds blackness from the slot formulas and re-checks Lemma mixedeq (V4), Lemma rival (V5) and the corners and parity (V2).
  - predict12t.py: predict12.py with the twisted build, plus a scan over all types.
  - riv3_min.py: least R_IV(3) edges.
- Primes used, twisted (l, p): (449, 32611) at h = 429; (479, 34319) at 451; (479, 34367) at 452; (757, 53299) at 701; (1277, 91303) at 1201; p = 114143 at 1501. stats12t confirms (37/l) = (l/37) = -1, (37/p) = -1 and p = 3 (mod 4).
- The untwisted primes happen to satisfy (37/.) = -1 at h = 429 and 452, but not at 451 (p), 701 (l) or 1201 (p). By (P2) this does not matter in class.

PROOF OF (P1)
- build_type12t and build_type12 run the same loop over s with the same inputs: the same D_T (diag_graph12), the same heavy test 4 kappa_T >= B, the same vertex list V, the same colour call with the same random stream (seeded by seed, iota, sigma), and the same removal(tp, i, j, mode).
- None of these reads l, p or rho_s. Those enter only through t = rho_s + 16lk.
- So the lists (s, colour, labels, removed) agree. stats12t confirms this on 512 of 512 types at h = 429, 451, 452, 701 and 1201.

PROOF OF (P2)
- Fix a subclass c with label set Lambda. Under rule X, the slot of label (i, j) is n = 3i + M_c^X, with M_c^X = p_X t_c^X.
- Put delta = M^tw - M^untw. Then:
  - n_lo and n_hi both shift by delta;
  - X0 = 4n_lo - 2W - 64 shifts by 4 delta;
  - Wd = 4(n_hi - n_lo) + 4W + 129 does not change;
  - the local label columns 4n - X0 do not change.
- For a local column x, the global columns X^tw = X^untw + 4 delta are equal mod 4, and the slots satisfy n^tw = n^untw + delta.
- rho0 is the slot of a label mod 4, so it shifts by delta mod 4 and (n - rho0) mod 4 does not change.
- In WinBoard, R1 depends only on X mod 4, r0, T* and (n - rho0) mod 4. The label rows depend on (i, j). tag() depends on X mod 4, on membership of n in the label set (which shifts with n), and on (n - rho0) mod 4.
- So R1, R2, rows(), tag(), islabelcol() and label_of() agree in local coordinates. checker.census and the classifier see only these.
- census12t.py and census12.py build the same anchors in local coordinates, so the output is identical.
- Observed: identical multisets on all 29 + 1 compared runs.

PROOF OF (P3)
- Reduce mod 16. rho_s = p^(-1)(3s - kappa) mod 16l, and 16 | 16l, so rho_s = p^(-1)(3s - kappa) mod 16. Also 16lk = 0 (mod 16).
- Inside a type, 16 | Delta s, so Delta t = 0 (mod 16).
- Delta t != 0:
  - if Delta s != 0: 3 is a unit mod 16l (l > 3 is prime), and 0 < |Delta s| < h < 16l, so rho_s differ, and t = rho_s (mod 16l);
  - if Delta s = 0: Delta t = 16l Delta k != 0.
- So the label columns are at least 4(16p - 3(A - 1)) >= 4(16(76h + 1) - 1.5h) > 4858h apart.
- 2W_h + 1 <= (h - 1)^2/2 + 3 < 4858h for h <= 9717. This is the arithmetic of census_stride12 (S2).
- stats12t: Delta t = 0 (mod 16) in every case. The least gaps are 2.30e7, 2.42e7, 2.64e7, 2.39e7 and 3.51e7 columns at h = 429, 451, 452, 701 and 1201, against 2W_h + 1 = 91595, 101253, 101703, 245003 and 720003.
- Different types sit in separate regions with (B9) margins. This is inherited from L***U and not re-checked.

PROOF OF (P4)
- p t = 3s - kappa (mod 16l), so n = 3i + 3s - kappa + b = 3j - kappa_tau (mod 16l). This is (C7).
- With i = iota (mod 32) and s = sigma (mod 16), n = 3(iota + sigma) - kappa_tau (mod 16).
- Untwisted: n = 3i + s - kappa + b, which gives 3 iota + sigma. The difference is 2 sigma (mod 16).
- stats12t, over all 512 types:
  - mod-16 failures: 0;
  - slot collisions: 0;
  - (n - 3j) mod 16l takes 1 value per type under the twist, and 20 to 71 values under the untwisted rule;
  - (n_tw - n_untw) mod 4 is 0 for every label with sigma even and 2 for every label with sigma odd.
- census12t reads rho0 from the true slot, as (B6) requires.

PROOF OF (P5)
- In a single-class window, a shallow column (X mod 4 != 0) has one black point, in row r0. So S = E has y_E = r0.
- Let V and G be the two odd label points, with y_G > y_V. Then G - V = (12t, 2t) with t = Delta i in 32Z and t > 0.
- r0 = 1 iff iota is odd, and i = iota (mod 32). So u_V = (2i + 1 - r0)/2 is i or i - 1, which is odd.
- Vertex at V: (E - V).(12t, 2t) = 0 with E - V = (e, -2u_V) gives 12te = 4tu_V, so e = u_V/3, which needs 3 | u_V. Then W = G + E - V has row r0 + 2t and column offset 12t + e, which is odd. So W is white and in the same parity as its column's only black row, which makes it parked. It needs r0 + 2t <= h.
- Vertex at G: the same computation gives row(W) = r0 - 2t < 1.
- Vertex at E: write alpha = x_E - x_V. The condition is alpha(12t - alpha) = 4u_V u_G with u_G = u_V + t.
  - alpha odd: the left side is odd and the right side is even. Impossible.
  - alpha = 0 (mod 4): E is in a deep column, not shallow.
  - alpha = 2alpha': alpha' and 6t - alpha' are the roots of z^2 - 6tz + u_V u_G. Its discriminant is 4(9t^2 - u_V u_G), with u_V u_G = u_V^2 + u_V t = 1 (mod 8). So the square 9t^2 - u_V u_G would be 7 (mod 8). Impossible.
- So the parked in-class Soo rectangles are exactly the pairs counted.
- census12t checks the shape of every observed one: 4023 of 4023 pass, observed equals predicted per run, and 0 lie at a V3 point. This is a computational check of the corrected Theorem A(ii) and (iii) at stride 12.

PROOF OF (P6)
- By sea_census_rigid B4 and stride_transfer_ratio Theorem R4 (audited), two odd label points of one class form a fatal M2c iff their u-values form an edge (qm, pm), m odd, with u_D <= (h - r0)/2.
- At u = 3 and k = 5: (al, be) odd and coprime, 0 < al < 3be, v2(3be - al) >= 3, F = 4(al - 6be)^2 + be^2, g = gcd(F, 3be - al), q = al F/g and p = (al F + 4(3be - al)be^2)/g.
- Lemma IV(u) gives p >= 12be^3/37, which exceeds 1453 for be >= 17.
- riv3_min.py enumerates be <= 59. The least edges are (1165, 1453), then (14987, 15787). At k = 3, (101, 109) is the least edge, but v4 uses k = 5.
- So u_D >= 1453 > (h - r0)/2 for h <= 2905.

PROOF OF (P7)
- The deep D12 instances (from predict12t) have t = 96 with Y1 = 915 (Fe) at h = 1201 and 1501, and t = 32 with Y1 = 1313 (Fe) at h = 1501.
- 96 <= 210 and 32 <= 210, which is the R_FF^+ bound (census_stride12 S4: t <= h - Y <= 210).

RUNS (twisted; s = stress, b = board, r = relaxed, e = exact)
- h = 429:
  - (1,1)s/r: D4 26, D10 48;
  - (0,1)s/r: D4 24, D10 40;
  - (2,0)s/r: D7 76 (6 with nL = 2), D10 125;
  - (6,0)s/r and (6,0)b/r: D7 43, D10 124;
  - (7,7)s/r: D7 26, D4 26, D10 161, D12 6;
  - (7,7)b/r: the same without D12.
- h = 451:
  - (1,1)s/r: D7 51, D11 48, D4 24, D10 175;
  - (0,1)s/r: D7 25, D4 24, D10 84;
  - (12,0)s/r: D7 76, D10 150;
  - (12,0)b/r: D7 70, D10 150.
- h = 452: (7,7)s/r: D7 14, D4 28, D10 77.
- h = 701:
  - b/e: (1,1) D10 5, (0,0) 7, (5,7) 6, (8,3) 2, (14,0) 0, (10,0) 0;
  - b/e with reloc701.txt: all 0;
  - s/e: (1,1) 5, (0,0) 7, (5,7) 6 (all D10);
  - (1,1)s/r: D7 21, D4 42, D10 195;
  - (0,0)s/r: D11 36, D10 176;
  - (14,0)s/r: D7 73, D11 36, D10 360;
  - (18,7)s/r: D7 148 (16 with nL = 2), D4 44, D10 539, D12 17.
- Every one of these 29 runs is identical to its untwisted log (cmp_tw).
- h = 1201, s/e (new; deep multi-label classes of 1 to 9 labels):
  - D10 only: (7,7) 51, (18,7) 140, (1,1) 58, (0,0) 41, (2,0) 125, (5,7) 59, (8,3) 16;
  - (6,0): D11 88, D10 125;
  - (8,6): D11 84, D12 4, D10 143;
  - (12,6): D12 4, D10 143;
  - (4,6): D12 1, D10 95.
- h = 1201, b/e: (8,6) D11 84, D10 143; (7,7) D10 51.
- h = 1501 (in chunks of at most 37 s; classes of 1 to 13 labels):
  - (2,6)s/e: D12 7, D10 380;
  - (7,7)s/e: D12 12, D10 304;
  - (2,6)b/e: D12 1, D10 380.
- verify12t re-checked every logged instance from the formulas: 6365 of 6365 pass.
- The longest call ran about 39 s internally, and memory stayed small (windows of at most about 2.3 million columns).

FAMILY VERDICTS AGAINST THE TABLE (consolidated_board_v4 section 3, stride_transfer_table)
- D4: C. Near-band only.
- D7 (FFo, label vertex): E only beyond the band (X >= 234 < 320). Every instance, including the 28 two-label ones with W in a label column, is within T* - 320, so R-b removes it. At exact h = 1201 and 1501 there are 0.
- D10: C, O(h^(3/2)), WP.
- D11: C, WP.
- D12: C, to WD via R_FF^+.
- No instance falls in a cell that the table marks E. All 50 + 2254 deep D10 instances and all 256 deep D11 instances are one-label C cells.

## External results used

- No web sources. I used only Euler's criterion and quadratic reciprocity for (37/q), and I checked numerically that (37/l) = (l/37).

## Checks

Every logged instance (6365) was re-verified from the slot and filler formulas against Lemma mixedeq, Lemma rival and the parity conditions, with 0 failures. All 29 runs that repeat the untwisted census are identical as multisets, and so is an untwisted control at h = 1201. D12/D13 predicted from the cubic equals observed on 6 deep types. Parked SLL-Pc observed equals predicted (4023 = 4023). Structural checks over all 512 types at 5 heights: same classes as the untwisted build, 0 slot collisions, 0 mod-16 failures, a single (n - 3j) value mod 16l per type, Delta t = 0 (mod 16), and gaps far above 2W_h + 1. oob = 0 and UNLISTED = 0 in every run. Every py call ran one at a time, under 60 s and well under 1 GB.

## Gaps

- Cross-class cells are not tested. A4, A5, B7, D8, D16, D17 and D18, the cross-class parts of A1, A2, A3 (I.1, type II, Proposition 1(c)), S7/S8, D6 Fee/Foo, D14 (two_filler Proposition 4) and Q3 are vacuous for h <= 9717 under both rules (P3). The twisted rule's purpose, l | Dn_u, which restores the l-adic kills, is invisible to every windowed census at computable heights, so this census cannot confirm or refute it. The Fee witness against the untwisted rule needs h = 2*10^7.
- Vacuous or not realised at the tested heights: in-class A2 (G_T[tau] has no edges for h <= 4097, census_stride12 S3); B6/R_IV(3) for h <= 2905 (P6); D13 (no type realises the cubic at h = 1201 or 1501, which is computed, not proved); D3/T2 (absent at stride 4u); in-class A1 (stride_menu Lemma 4). In-class D14, D15, D19, D20, B5 and A3 have no instance; they are proved empty in the notes, and here they are only observed empty. So the deep two-label test covers D12 only.
- Inherited and not re-checked: the window convention (every configuration within 2W_h + 64 of a label column; the separation of types by the (B9) margins), and the classifier's family names.
- The type phase changes by 2 whenever sigma is odd. The SAW*-shift gap, the seams, J1* and the (Phi) junctions at region boundaries were not re-run. I rely on census_stride12 (S7) and census (C2)/(C3), which cover all four phases.
- Not applied: R-d, R-e and (B8) Bad_split. R-f was applied only through reloc701.txt. Heavy diagonals (Theorem E side) are not placed. I used one seed, kappa = b = 0, and the least admissible (l, p). Stress classes (whole residue classes) are valid but atypical outcomes of the colouring law, and they are not supersets of board pictures, because vacated slots become fillers.
- Parked mixed-parity S-label-label triples (Soe) were not analysed. None were observed parked, and none were fatal.
- The deep runs cover only 13 types at h = 1201 and 3 type-runs at h = 1501, out of 512 types per height. The D12/D13 scan covers all 512 types, but only for that one family.

## Missing estimate

This census does not bear on the near goal or the far goal, and it removes no hypothesis of Theorem N. What it shows: up to h = 9717, the twisted board L***(3) and the untwisted board have the same in-class content, exactly (P2, P3). The in-class content at h <= 1501 holds no family outside D4, D7 near-band, D10, D11 and D12. The parked SLL-Pc family flagged by the core audit has exactly the corrected shape and count. The twist matters only through cross-class configurations, and no windowed census can reach those below h of about 9717.

## Next steps

- Test the twist where it acts: at h > 9717, run a family-targeted search (like fee_untwisted2.py) for A5, (E;O,E) and Fee across adjacent subclasses (Delta t = 16), with sparse windows. Expect 0 under (B2') and (B5'), by the l-adic and p-adic proofs.
- The first height where B6 (R_IV(3), k = 5) can occur is h >= 2907. A deep census near h = 3001 with census_large's FastWinBoard would give the first definition-level test of in-class R_IV(3) on the board. Run it on the types where u_D = 1453 m falls on a label residue.
- Add (P5) to the stride-4u notes as the explicit statement of the corrected v3 Theorem A(ii) at u = 3. It counts the in-class parked Soo family, and the vertex-at-E case dies mod 8.
- Record (P2): within one subclass the placement rule is a pure translation. Any in-class lemma of L***U at stride 4u is therefore independent of the choice of rho_s, so only the cross-class lemmas need the twisted rule.

