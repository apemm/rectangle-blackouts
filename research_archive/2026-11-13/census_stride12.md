# Definition-level census of the stride-12 board

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (computational): the stride-12 board was built at definition level on 13 region types at h = 429, 451, 452 and 701, with the type phase adjusted to 3 iota + sigma - kappa + b (mod 16). All 3826 violations fall in families that the obstruction table already handles at stride 4 (D10, D11, D4, D7, D12). None is unlisted, and none is a deep instance of a cell the table marks empty. The homogeneous two-label two-filler cubic at stride s is derived, so R_FF^+ still covers D12. Blocks never interact below h = 9717.

# Result

## Status

partial

## Summary

I ran the stride-12 board L***(3) at definition level on 13 region types at h = 429, 451, 452 and 701, and nothing was flagged. All 3826 (V1)-(V5) violations fall in table families that hold in L***U: D10, D11, D4, D7 and D12. All are near-band except 50 deep D10 rival pairs. None is UNLISTED, and none is a deep instance of a cell the table marks empty. One adjustment was needed: the type phase becomes rho_tau = 3 iota + sigma - kappa + b (mod 16). I also proved that the homogeneous 2L2F cubic at stride s is (delta - 2st)(delta^2 + 4t^2) = 8tY1(delta - st). So R_FF^+ (|Delta i| <= 210) still covers D12, and D13 becomes the ratio graph of U_12, V_12. The colouring has no effect below h = 4097, and blocks never interact below h = 9717.

## Statements

Nothing in this result proves the near goal or the far goal. It has two parts: definition-level computations on L***(3), and seven short proved statements.

DEFINITION OF L***(3) (as built). It is L***U of consolidated_board_v4 (B0)-(B7), with these changes:
- slot n = 3i + pt + b, in column 4n;
- p is the least prime > 76h with p = 3 or 7 (mod 20) (stride_menu Lemma 4 at s = 12);
- D_T = {|d| : 0 < |d| < n_T, 144d^2 + (2d+T)^2 = L^2, 0 < L < h} (sigma = 6, Delta = 37), with kappa_T = |D_T|;
- T is heavy if kappa_T >= B/4, with B = ceil(Lambda^theta*);
- G_T[tau] is the distance graph on the slots i = iota (mod 32);
- the classes are the colour classes of a uniform proper B-colouring of G_T[tau], sampled exactly by rejection;
- colour k sits at t = rho_s + 16lk, with rho_s = p^(-1)(s - kappa) (mod 16l) and kappa = b = 0;
- l, the types, T*, the SAW*-shift fillers and the shallow sea are unchanged.

ADJUSTMENT. Only the [F1] phase changes, to rho_tau := 3 iota + sigma - kappa + b (mod 16), with rho0 = rho_tau mod 4. The mod-16l form of the slot changes from n = j - kappa_tau (mod 16l) to n = 3i + s - kappa + b (mod 16l). Only the cross-class lemmas use that form, and nothing in this census tests them (see S2).

PROVED (short proofs in the proof field):
- (S1) Every label slot of R_tau has n = rho_tau (mod 16), so labels sit at filler offset 0. The slot map is injective on each type.
- (S2) Two subclasses of one type are more than 2W_h + 1 columns apart for every h <= 9717. So the cross-class families (A4, A5, B7, D8, D16-D18, cross-class Q3) are empty at the tested heights.
- (S3) For every odd u and every h <= 4097, G_T[tau] has no edge at stride 4u. So at these heights every partition of a residue class into at most B parts is a proper colouring, and in-class A2 is empty whatever the colouring.
- (S4) THE STRIDE-s CUBIC. Take a homogeneous two-label, two-filler mixed quadruple inside a class of stride s: side {L1, F1}, diagonal {L2, F2}, L2 - L1 = (st, 2t), and F1, F2 in one row Y at depths Y1 and Y2 = Y1 - 2t. Put delta = a - c, where a = x(F1) - x(L1) and c = x(F2) - x(L2). Then:
  - a = (delta^2 + 4t^2)/(4(delta - st)), Y1 = a(delta - 2st)/(2t), and equivalently (delta - 2st)(delta^2 + 4t^2) = 8tY1(delta - st);
  - n = ((2st - delta)/2, t);
  - Y2/Y1 = V_s/U_s at a/b = delta/(2t), with U_s = (a - sb)(a^2 + b^2) and V_s = a^3 - s a^2 b - 3ab^2 + s b^3. At s = 4 this is additive_class_split Lemma 1;
  - for coprime (a, b), gcd(U_s, V_s) divides 2s(s^2 + 4), which is 3552 at s = 12;
  - D12 (t > 0) needs t <= h - Y <= 210 at every stride, so R_FF^+ (0 < |Delta i| <= 210) covers D12 at stride 12 unchanged.
- (S5) The type congruences for (S4): Fo needs Y1 = 8(o + c_tau) (mod 64), and Fe needs Y1 = 8(o + c_tau) - T (mod 64), where o = (a/4) mod 4.
- (S6) census_large (P1) holds verbatim at stride 12: under (B7) and (B8), a final subclass keeps at most floor((h - 623)/448) + 1 labels. The proof uses only Delta i = 0 (mod 32) and R_FF^+ at 210.
- (S7) The pure SAW*-shift gap, the seams, the buffers and the J2 pieces hold no label. Their content depends only on (r0, T*), the phase and g, and stride 12 leaves the set of (r0, T*) unchanged. So census (C2) and (C3) apply verbatim.

COMPUTED (one type per run, each under 60 s, with the validated kernel; the full list is in the proof field):
- (C1) In every run, every violation that contains a label point or has W in a label column is one of the following. The first number counts violations, and nL is the number of labels involved:
  - D10, (e, F) rival pairs: 2727 (2677 near-band, 50 deep);
  - D7, FFo with a label vertex: 692 (664 with nL = 1, 28 with nL = 2), all near-band;
  - D4, Theorem 1(6): 264, all near-band;
  - D11, M2c with one label and a filler: 120, all near-band;
  - D12, homogeneous Fe/Fe with d > 0: 23, all near-band, with Delta i = 32 or 128.
  There were 0 UNLISTED, 0 V1, 0 V3, and none of A1-A5, B1-B8, D1, D5, D6, D8, D9, D13-D22. oob was 0 everywhere.
- (C2) The 28 two-label D7 instances are one shape and its mirror: legs (-24, 168) and (1176, 168), with W at (1152, 336) in the column of a second label of the class (Delta i = 96). This is the D7 cell (FFo, label vertex, W in a label column), and its vertex lies 168 rows from a filler row, so R-b removes it.
- (C3) A shape enumeration with depth bound H (no board). At stride 12, D13 (t < 0) has no shape with depth <= 871 and 7 shapes up to 3000; at stride 4 it has 10, 29 and 67 shapes up to 700, 1500 and 3000, starting at depth 175. At stride 12, D12 has 9, 18 and 27 shapes up to 700, 1500 and 3000. No stride-12 Fo shape with depth <= 3000 meets the Fo congruence of (S5) (computed, not proved).
- (C4) Predicted equals observed. For 7 types, the set of D12/D13 quadruples predicted from (S4), (S5) and the board formulas equals the census set exactly (6, 0, 0, 0, 0, 17 and 0 quadruples).
- (C5) At h = 701 under the exact rules, 3263 labels survive, all in singleton classes of the board law. In 6 types, the only family is D10 (20 labels). After those labels are relocated, 0 violations remain in the 4 types that had survivors.
- (C6) Heavy diagonals (kappa_T >= B/4): 26 at stride 12 at each of h = 429, 451 and 701, against 60, 62 and 84 at stride 4.

## Proofs

SETUP
- Script folder: scripts_census_u3/.
- I copied core.py, checker.py, classify.py, lstar.py and validate.py byte for byte from scripts_census (checked with cmp), so the numba cache never lands in the repository. The repository was only read.
- New scripts: lstar12.py (the board), census12.py (the driver), stats12.py, cmp_s4.py, shapes12.py, shapes_count.py, predict12.py, verify12.py, ctrl12.py. Logs are log12_<h>_<iota>_<sigma>_<colour>_<rules>.txt.
- Windows, anchors and the classifier are exactly those of census_class.py. Each subclass with kept labels gets the window [4 n_lo - 2W_h - 64, 4 n_hi + 2W_h + 64]. The anchors are every label point and every white point of a label column. By (S2), no other label is within reach.
- Colour modes:
  - board: the v4 law at stride 12;
  - stress: greedy colouring of G_T[tau]. Because G_T[tau] has no edges (S3), each stress class is a whole residue class. That is a proper colouring with positive probability under the law, so it is an atypical board outcome, not an outside one.
- Rule modes:
  - relaxed: R-a only;
  - exact: R-a, R-b (T* - 320, plus the T* - 444 extension when k = 2) and R-c (2i + 1 <= 300).
- R-d (T1-exceptional) is not applied: at h <= 701 it would remove every label. R-e, R-f and (B8) are applied only through the census (relocation in C5).

RUNS (one type per py call, sequential, each under 60 s; the largest internal time was 32.6 s; nL is the number of labels involved; "near-band" means removed by R-b or R-c):
- h = 429, stress, relaxed:
  - (1,1): D4 26, D10 48;
  - (0,1): D4 24, D10 40;
  - (6,0) (k = 1): D7 43, D10 124;
  - (2,0) (k = 2): D7 70 + 6 (nL = 2), D10 125;
  - (7,7): D7 26, D4 26, D10 161, D12 6.
- h = 429, board, relaxed: (6,0) and (7,7) give the same one-label families. The D12 pairs were split by the random colouring.
- h = 451, stress, relaxed:
  - (1,1) (k = 1): D7 51, D11 48, D4 24, D10 175;
  - (0,1): D7 25, D4 24, D10 84;
  - (12,0) (k = 2): D7 70 + 6, D10 150.
- h = 451, board, relaxed: (12,0) gives D7 70 and D10 150.
- h = 452 (even), stress, relaxed: (7,7) gives D7 14, D4 28 and D10 77.
- h = 701, board, exact:
  - (1,1): D10 5;
  - (0,0): D10 7;
  - (5,7): D10 6;
  - (8,3): D10 2;
  - (14,0) and (10,0): no survivors.
  With reloc701.txt (20 labels relocated), the 4 types with survivors have 0 violations.
- h = 701, stress, exact: the same as board exact for (1,1), (0,0) and (5,7). Those classes have no pairs, because the survivors have i in about [150, 176].
- h = 701, stress, relaxed:
  - (1,1): 697 pairs and 1474 triples; D7 21, D4 42, D10 190 + 5 deep;
  - (0,0): D11 36, D10 169 + 7 deep;
  - (14,0): D7 73, D11 36, D10 360;
  - (18,7): 770 pairs and 1650 triples; D7 132 + 16, D4 44, D10 539, D12 17.

CHECKS
- verify12.py rebuilt blackness from the (B5)/(B6) formulas, not from WinBoard. It re-checked all 3826 instances against Lemma mixedeq (V4), Lemma rival (V5) and the corner and parity conditions (V2): 3826 of 3826 passed.
- Cross-check against stride 4 (cmp_s4.py). I ran the original census_class.py (NOSPLIT) on (1,1) at h = 429. On the 43 labels common to both boards, the per-label multiset of one-label (kind, family) entries is identical. The 7 labels found only at stride 4 lie on T = 3 and T = 99, which are heavy at stride 12.
- Positive control (ctrl12.py): I put consecutive slots of one diagonal in one stride-12 class, which breaks G_T independence and the mod-32 rule.
  - s = -99 (D_T = {4}), 12 slots: 8 A2 pairs, all at slot distance 4 (8 = 12 - 4).
  - s = -165 (D_T = {3, 11, 15}), 20 slots: A2 at distances 3, 11 and 15 with counts 17, 9 and 5 (each equals 20 - d).
  So the pipeline detects stride-12 label geometry. My first control attempt (24 slots, run through census12) hit the 60 s timeout and was discarded.
- stats12.py over all 512 types at h = 429, 451 and 701: 0 mod-16 failures, 0 slot collisions, 0 edges of G_T[tau], and least subclass gaps of 3.3e7, 1.1e7 and 1.4e7 columns against 2W_h + 1 of 91595, 101253 and 245003.
- Class sizes under the board law at h = 429: 32815 classes of size 1, 3623 of size 2, 274 of size 3 and 19 of size 4. Stress classes reach 7 labels at h = 429 and 11 at h = 701.
- At h = 429 and 451, exact mode keeps 0 labels, as in census (O2).

PROOF OF (S1)
- Since pt = s - kappa (mod 16l), n = 3i + s - kappa + b (mod 16l).
- Because i = iota (mod 32), 3i = 3 iota (mod 96). Because s = sigma (mod 16), n = rho_tau (mod 16).
- Injectivity: distinct (s, k) give distinct t, because 0 < |Delta s| < h < 16l and the rho_s are residues mod 16l. Inside one t, n determines i. For Delta t != 0, |p Delta t| >= p > 76h > 3A > |3 Delta i|.

PROOF OF (S2)
- Within a type, Delta t = p^(-1) Delta s (mod 16l) with 16 | Delta s, so Delta t is a nonzero multiple of 16.
- So two label columns of different subclasses are at least 64p - 12(A - 1) >= 64(76h + 1) - 6h > 4858h apart.
- Also 2W_h + 1 <= (h - 1)^2/2 + 3, which is < 4858h for h <= 9717. At h = 9717: 47,200,331 < 47,205,186.
- Different types sit in separated regions ((B9) margins), as in L***U.

PROOF OF (S3)
- An edge needs d in D_T with 32 | d, so (4ud)^2 + Y^2 = L^2 with Y = |2d + T| odd and L odd.
- Write L - Y = 2 alpha and L + Y = 2 beta. Then alpha beta = (2ud)^2, and alpha + beta = L is odd.
- So alpha and beta have opposite parity, and one of them carries the whole 2-part of (2ud)^2, which is 2^(2(1 + v2(d))) >= 2^12.
- Hence L = alpha + beta >= 4097, which L < h <= 4097 rules out.

PROOF OF (S4)
- Put A = L1 = (0, y1), B = F1 = (a, Y), C = L2 = (st, y1 + 2t) and D = F2 = (st + c, Y).
- Then u = (a, Y1) and w = (c, Y2), and 2n = C + D - A - B = (2st + c - a, 2t).
- |u| = |w| gives delta(2a - delta) = 4t^2 - 4tY1.
- n . u = 0 gives a delta = 2t(sa + Y1).
- Eliminating Y1 gives 4a(delta - st) = delta^2 + 4t^2. Then Y1 = a(delta - 2st)/(2t).
- Put m = delta/(2t). Then Y1 = t(m^2 + 1)(m - s)/(2m - s), which gives the forms U_s and V_s. At s = 4 they are U and V of Lemma 1.
- Content:
  - U_s - V_s = 2b^2(2a - sb), and gcd(U_s, b) = 1, so gcd(U_s, V_s) divides 2 gcd(U_s, 2a - sb);
  - gcd(a - sb, 2a - sb) = gcd(s, a);
  - 4(a^2 + b^2) = (2a - sb)(2a + sb) + (s^2 + 4)b^2 with gcd(a^2 + b^2, b) = 1, so gcd(a^2 + b^2, 2a - sb) divides s^2 + 4;
  - so gcd(U_s, V_s) divides 2s(s^2 + 4).
- D12 bound: q = F1 + n lies in row Y + t <= h. Fillers lie in [h - 210, h] ((B6)), so t <= 210 when t > 0.
- shapes12.py checked every enumerated solution against the mixedeq equations with explicit points.
- The (C3) enumeration restricts delta to |delta| <= max(4s|t|, sqrt(20|t|H)). This is complete: if |delta| >= 4s|t|, then |delta - 2st| >= |delta|/2 and |delta - st| <= 5|delta|/4, so |Y1| >= delta^2/(20|t|).

PROOF OF (S5)
- With i = iota (mod 32), the odd row is 2i + 1 = y_P (mod 64), and the even row is y_P + T (mod 64).
- A filler at offset o lies in row y_P + 8(o + c_tau) (mod 64) ((B6)).
- The offset of F1 is (n1 + a/4 - rho0) mod 4 = (a/4) mod 4, because n1 = rho0 (mod 4).

PROOF OF (S6): the same as census_large (P1) section 6. It uses R-b, R-c, Delta i = 0 (mod 32) and R_FF^+ at 210, none of which depends on the stride.

PROOF OF (S7): by inspection of WinBoard and (B6). Away from labels, every column is a function of (X mod 4, (n - rho0) mod 4, r0, T*) and of the seam data. type_params does not use the stride. The seam census covered all four phases wherever (Phi) chooses one.

PREDICTIONS MADE BEFORE THE RUNS
- (7,7) at h = 429: Fe/Fe D12 with t = 32 and Y1 = 305, labels at j = 30 and 62 on T = 47 (mod 64), and q in row 399. Observed: exactly 6, at i1 = 7, 39, 71, 103, 135 and 167.
- (18,7) at h = 701: both shapes, (32, 305) and (128, 425). Observed: 17 = 17.

## Checks

Every reported instance (3826) was re-checked from the board formulas against Lemma mixedeq, Lemma rival and the parity conditions, and all passed. One-label families match the stride-4 census label by label on 43 common labels. A positive control detects A2 at exactly the stride-12 distances D_T. D12/D13 sets predicted from the stride-12 cubic equal the census sets on 7 types, including two predictions made before the runs. The shape enumerator reproduces additive_class_split Lemma 1 at s = 4. Structural statistics over all 512 types at three heights show 0 slot collisions and 0 mod-16 failures, and every subclass gap exceeds 2W_h + 1. oob was 0 in every run, and every py call ran sequentially under 60 s and well under 1 GB. One control call hit the 60 s timeout and was discarded. Scripts and logs are in scripts_census_u3/.

## Gaps

- The in-class content of L***(3) is tested only on near-band labels and on singleton survivors. At h <= 652 no label survives the exact rules (S7 and O2), and at h = 701 each mod-32 class holds at most one survivor. By (S6), deep multi-label survivors need h >= 1071. The stride-12 two-label cells (D12, D13, D14, D15, B6, A3) have not been tested on deep labels.
- The stress classes (whole residue classes) are valid but atypical outcomes of the board law. The board-law runs give classes of 1 to 4 labels. I used one psi seed, the least admissible (l, p), and kappa = b = 0.
- Cross-class families are empty for h <= 9717 (S2), so this census says nothing about them. They depend on the changed mod-16l form n = 3i + s - kappa + b (mod 16l). threshold_families Propositions 1(a)-(d), Theorems 2 and 3, uniformity U1, two_filler Theorem 3, D17 and D18 are not re-derived at stride 12. Using rho_s = p^(-1)(3s - kappa), which gives n = 3j + const (mod 16l), is an open design choice.
- Not re-derived at s = 12: the stride-dependent K4 lines that the census only samples. These are v3_and_cross_block Theorem B (FFo label vertex X >= 234, Foo |alpha| < h/632), rigid Theorem C (A1), mixed_quadruples Theorems 1-4 (A3), sea_census_rigid B4 and ratio_graph (R_IV, B6), and Lemma FF'/Theorem IV/(AP) for the stride-12 forms U_12, V_12 at cutoff h^(1/2)/32.
- Not run: pure gap and seams (covered by argument S7, not recomputed), Theorem D/E blocks, Proposition partial, J5 gluing, truncation, R-d, and the faithful (B8) Bad_split. R-f is applied only through census-driven relocation (D10 at h = 701).
- The 'no Fo shape' observation at stride 12 (C3) is computed to depth 3000, not proved.
- The family names come from classify.py, unchanged. I re-derived only the D12/D13 shapes (S4, C4) and the D7 two-label shape (C2).
- Record-keeping: census_consolidated_board says 'no diagonal was heavy' at h = 429, 451 and 701. That used the old threshold kappa_T >= B. Under v4 (B1) (kappa_T >= B/4), stride 4 has 60, 62 and 84 heavy diagonals there, so its claim that the Theorem E side is empty is false for v4. The label sets it tested are supersets of v4's light labels.

## Missing estimate

This census does not bear on the near goal. It removes no hypothesis of Theorem N, and it proves no menu exponent x_m. What it shows: within one class and at h <= 701, moving from stride 4 to stride 12 brings in no new obstruction family. The stride enters the in-class cells only through the constant s of the 2L2F cubic (S4) and through where W lands (C2). For the menu board, two things remain:
- the stride-12 re-derivation of the in-class lemmas listed in gaps item 4, and the cross-class lemmas under the new mod-16l slot form;
- a deep census at h of about 1500 to 2500, where survivor classes hold 2 to 5 labels.

## Next steps

- Re-derive, at s = 12, the four in-class proofs that carry a stride constant: v3_and_cross_block Theorem B (FFo X >= 234, Foo), mixed_quadruples Theorems 1-4 (they already carry s), rigid Theorem C, and the R_IV characterisation of sea_census_rigid B4. Then restate Lemma FF', Theorem IV and the (B8) R_FF cutoff with U_12, V_12 and content dividing 3552 (S4).
- Fix the mod-16l placement for stride 12: either n = 3i + s + const or n = 3j + const (rho_s = p^(-1)(3s - kappa)). Then re-derive threshold_families Proposition 1, Theorems 2 and 3, and uniformity U1 at stride 12. These matter only above h = 9717 (S2).
- Run the faithful stride-12 census at h = 1501 to 2501 on 10 types, with (B8) using R_FF^+ at 210 and R_FF from U_12, V_12. This is the first height where deep multi-label survivors exist (S6). Copy census_large's FastWinBoard so the windows fit in memory.
- Record the S3 lemma in the board note: for h <= 4097, G_T[tau] has no edges at every stride 4u, so the colouring law is vacuous at every computable census height below that.
- Correct census_consolidated_board's 'no diagonal was heavy' to the v4 threshold B/4: 60, 62 and 84 heavy diagonals at stride 4 at h = 429, 451 and 701, against 26 at stride 12.

