# Low corners in row-3 types (Q4)

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: in a light region of L***, no deep-only corner triple has its white corner in rows 1 or 2, and every deep-only mixed quadruple with p or q in rows 1 or 2 has four label points, so the existing label-only counts cover it. A 2-adic norm lemma, found independently of three_label_one_filler.md, also closes Q3. Not audited yet.

# Result

## Status

proved

## Summary

Q4 is closed under the cited inputs. Rows 1 and 2 never hold the white corner W of a deep-only corner triple. Every deep-only mixed quadruple with p or q in rows 1-2 is label-only, and A3/A4 already count those in the true strip. A new 2-adic norm lemma also empties every 3-label 1-filler quadruple, so Q3 closes as well. None of this is audited.

## Statements

SCOPE AND HYPOTHESES. This covers one light region R_tau of L*** (consolidated_board.md B3-B7), including its SAW*-shift margins, with h >= 424. Type tau = (iota = i mod 32, sigma = s mod 16), y_P = 2iota+1, T0 = 2sigma+1, c = 1 if T = 3 (mod 4) and c = 3 if T = 1 (mod 4). I use these facts of L***:
 (F1) Every label point lies in a column 4n with n = rho0 (mod 4) (K1). Every other deep column 4n holds one filler, in row f_o = T*_tau - 24 + 8o, with o = (n - rho0) mod 4 (B6). Relocated label slots become offset-0 holes.
 (F2) Odd label rows are y_P (mod 64), because i = iota (mod 32).
 (F3) Even label rows are y_P + T0 (mod 32), because j = iota + sigma (mod 16).
 (F4) f_o = y_P + 8(o + c) (mod 64), because T*_tau = T0_tau (mod 64) and the 64k shift keeps this.
 (F5) Row ranges, from B7 and K4. Every label point is in a row <= Lambda := T*_tau - 321 (near band). Every filler is in [Phi, Phi + 24] with Phi = T*_tau - 24 >= h - 210. Odd label rows are >= 301 (R2'). Label rows are >= 2, and >= 6 in row-3 types; rows 1 and 2 are empty in row-3 types.
 (F6) Label points of different classes are at least 4(p - A) > 156h columns apart (p > 40h; distinct classes have distinct t_c). Within one class, two points of the same parity differ by (4t, 2t) with t = 0 (mod 32).
'Deep-only' means every black point of the obstruction is a label point or a filler. Deep-only obstructions do not depend on the sea row, so everything below holds in row-1 types as well. Row-3 types are the case asked about.

LEMMA N (3-label 1-filler norm lemma; proved here). Let F be a filler and L, L', L'' label points, with y_L + y_F = y_L' + y_L'' (mod 2). Then |F - L|^2 != |L'' - L'|^2. Hence no mixed quadruple, in any arrangement, inside a class or across classes, has a support made of three label points and one filler. This settles D19, D20 and Q3 entirely and supersedes Lemma 3L1F-a.

LEMMA LR (low pair point; proved here). Let {A,B,C,D} be a deep-only mixed quadruple (side AB, diagonal CD, p = A+n, q = B+n), named so that y_p <= 2. Then y_C + y_D <= y_B - y_A + 4, and the support is one of:
 (L) four label points;
 (M-ii) A and B fillers, with C and D even label points in rows <= 26;
 (M-i) B a filler, one of C or D a filler, and A and the other diagonal point even label points whose rows sum to at most 28;
 (M-iii) B a filler and A, C, D label points.

LEMMA S (proved here). (M-i) and (M-ii) are empty. Inside a class this follows from (F6). Across classes it is a size argument with no congruence.

THEOREM Q4 (proved, conditional on the inputs listed under Proof, part 6; not audited). In R_tau:
 (a) No deep-only corner triple has its fourth corner W in row 1 or 2.
 (b) No V3 pair has W in row 1 or 2. In row-3 types this also needs sea_row3 Theorem A(ii).
 (c) A deep-only rival pair with p in row 1 or 2 is either {even label point, filler}, or {odd, even} label points of one class. The first kind is inside the set that saw_residual (i) counts with H0 = 210 (O(h^(3/2)) labels, relocated as D10). The second kind is excluded by G_T-independence.
 (d) A deep-only mixed quadruple with p or q in row 1 or 2 has four label points. Those quadruples belong to A3 (empty) or A4 (B h^(1+o(1)) labels in expectation). Both analyses use the true strip [1,h], so they already include them. No low quadruple contains a filler.
 (e) No deep-only count used by L*** assumes p, q >= 3 (or W >= 3). The sea-involving counts that use shifted coordinates in row-3 types (y - r0 with r0 = 3) are valid exactly for obstructions whose non-black corners lie in rows >= 3. The complement is sea_row3 Theorem A(ii)-(iv) (audited), whose hypotheses (H1)-(H3) hold in L***. In L*** no two deep points even differ by 2 or 4 rows, so the M2c-low and e = 2 branches are empty outright.
CONSEQUENCE. Remove D21 (Q4) and D20 (Q3) from the open list of Theorem N, and remove their J3-Bad sets from B7. D19 becomes a corollary of Lemma N.
NOT PROVED: anything outside light regions (junctions J1*, Theorem D/E blocks, Proposition partial regions), Q1, Q5, (AP), the owed audits U1-U8, or m_h = O(h^2).

## Proofs

0. NOTATION. For a mixed quadruple, Lemma mixedeq (sec2_prelim.tex, read) gives n != 0, n.(B-A) = 0, C + D = A + B + 2n and |D-C| = |B-A|, with D-C != +-(B-A). The paper's Definition obstruction requires p = A+n and q = B+n in rows 1..h, and AB not vertical. Write U = B - A = (X1, Y1) and V = D - C = (X2, Y2). Rows give 2n_y = y_C + y_D - y_A - y_B. A label column holds exactly its two label points, so a filler is never in a label column.

1. LEMMA N.
Residues. Take a label L and a filler F at offset o. By (F1), x_F - x_L = 4o (mod 16). By (F2)-(F4), f - y_L = 8(o+c) (mod 64) if L is odd, and f - y_L = 8(o+c) - T0 (mod 32) if L is even. For two label points L' and L'', x difference = 0 (mod 16), and the row difference is 0 (mod 64) for odd-odd, 0 (mod 32) for even-even, and T0 (mod 32) up to sign for odd-even. Fillers have odd rows. So L odd forces L' and L'' to have the same parity, and L even forces them to have mixed parity.
Write a = x_F - x_L, Y1 = f - y_L, and for the label pair b = x difference, Y = row difference.
Case L odd (partner pair of the same parity). Here b^2 + Y^2 = 0 (mod 256), because 16 | b and 16 | Y. Then:
 - o odd: a^2 = 16 (mod 128) and 16 | Y1, so a^2 + Y1^2 = 16 (mod 128).
 - o = 2: a = 8·odd and Y1 = 8·odd, so a^2 + Y1^2 = 64 + 64 = 128 (mod 512).
 - o = 0: 16 | a and Y1 = 8c = 8·odd (mod 16), so a^2 + Y1^2 = 64 (mod 256).
 None of these is 0 (mod 256).
Case L even (partner pair {O, E'} odd-even). Put Y = y_O - y_E' and kappa = Y1 - Y = (f - y_O) + (y_E' - y_L). Then kappa = 8(o+c) (mod 32), and the norm equation is a^2 - b^2 = Y^2 - Y1^2 = kappa^2 - 2 kappa Y1, with Y1 odd.
 - o even: o + c is odd, so v2(kappa) = 3 and v2(kappa^2 - 2 kappa Y1) = 4. But v2(a^2 - b^2) = 6 for o = 2. For o = 0 it is >= 8, and a^2 = b^2 is impossible since the right side is nonzero.
 - o odd: v2(a^2 - b^2) = 4, because a^2 = 16 (mod 128) and b^2 = 0 (mod 256). If v2(kappa) = 4, the right side has v2 = 5. If v2(kappa) >= 5, or kappa = 0, the right side has v2 >= 6 or is 0.
Every case fails. In a 3-label 1-filler quadruple, the pair holding F has a label as the other point, and the parity condition is the row-sum parity from C + D = A + B + 2n. QED.
Why earlier notes missed it: Lemma 3L1F-a used filler rows mod 64 only. The kill comes from coupling the filler's column offset o (4o mod 16) with its row 8(o+c) (mod 64). The control check below confirms that removing this coupling brings solutions back.

2. LEMMA LR. y_p = y_A + n_y = (y_A - y_B + y_C + y_D)/2 <= 2 gives (★): y_C + y_D <= y_B - y_A + 4. By (F5), Phi - Lambda = 297.
 - B a label. The right side of (★) is <= Lambda + 2. A filler among C, D gives y_C + y_D >= Phi + 2 > Lambda + 2. If A is a filler, the right side is <= Lambda - Phi + 4 < 0. So the support is (L).
 - B and A fillers. y_B - y_A <= 24, so y_C + y_D <= 28. Fillers are >= h - 210 > 28, so C and D are labels with rows <= 26, hence even (odd rows are >= 301). This is (M-ii).
 - B a filler and A a label. The right side of (★) is <= h + 2. Two fillers on the diagonal give y_C + y_D >= 2Phi >= 2h - 420 > h + 2, since h >= 424. With one diagonal filler D, (★) reads y_A + y_C <= y_B - y_D + 4 <= 28, so A and C are even labels. This is (M-i). With no diagonal filler, the support is (M-iii).
 The case y_q <= 2 is the same with A and B exchanged.

3. LEMMA S.
(M-ii).
 - C and D in one class: their rows differ by 2t with t = 0 (mod 32), so they cannot both lie in rows <= 26 unless C = D.
 - Different classes: |X2| >= 156h and |Y1|, |Y2| <= 24. Then ||X1| - |X2|| <= 576/(|X1| + |X2|) < 1, so |X1| = |X2| and Y1^2 = Y2^2. Next, n_x X1 = -n_y Y1 with |n_y Y1| <= 24h < |X1|, so n_x = 0. Here |n_y| >= Phi - 14 > 0, so Y1 = 0 = Y2, and V = +-U, which mixedeq excludes.
(M-i).
 - In one class: impossible, as above.
 - Different classes, with D = x_C - x_A and |D| >= 156h: |n_y| = |(y_C - y_A) + (y_D - y_B)|/2 <= 24 and |Y1| <= h.
 - X1 != 0 (B is not in a label column). Y1 is odd, so n_y = 0 would give n_x X1 = 0 and then n = 0. So n_x != 0, and |X1| <= |n_x X1| = |n_y Y1| <= 24h.
 - Then |X2|^2 = X1^2 + Y1^2 - Y2^2 <= (24h)^2 + h^2.
 - But 2n_x = 2D + X2 - X1, so |n_x| >= 131h, and |n_x X1| >= 131h > 24h. Contradiction.
 No congruence is used in the cross-class cases, so R1 is not needed.

4. THEOREM Q4.
(a) Let V be the black corner opposite W, with ends E and G. Then y_W = y_E + y_G - y_V <= 2 means y_V >= y_E + y_G - 2.
 - V a label: a filler end gives y_E + y_G >= Phi + 2 > Lambda + 2 >= y_V + 2. So the triple is LLL, which rigid Theorem C (audited) excludes; it is row-free.
 - V a filler with two filler ends: y_E + y_G >= 2Phi > h + 2.
 - V a filler with ends {F', even label in a row <= 26}: this is FFe with a filler vertex. Its right angle gives 2 alpha beta = -d1 e2 with beta = e2 (mod 4), which has no solution (v3 Theorem B; re-derived; row-free).
 - V a filler with two label ends. Fee is excluded by parity. Feo is the SAW* V-vertex kill (saw_residual (iii-a), audited). Foo: re-derived. alpha1 alpha2 = -4 e1 e2 forces o_V = 2. Under R1, (2alpha1 + D)^2 = D^2 - 16 e1 e2 with 16 | D gives w^2 + e1 e2 = 2 (mod 8) against (D/4)^2 = 0 (mod 16).
 All of these arguments are row-free.
(b) A V3 pair needs two parked triples sharing W. By (a), no deep-only triple has W in rows 1-2. In row-3 types, sea_row3 Theorem A(ii) (audited) excludes triples with a shallow corner there, under (H1)-(H3). These hold in L***:
 - (H1): rows 1-2 are empty.
 - (H2): j = 1 and i = 2 are relocated, and fillers are high.
 - (H3): odd label rows are 1 (mod 4) for even iota, and fillers are y_P (mod 8).
(c) By Lemma rival, the two points of a rival pair have different parities, with p at row c - j >= 1 and q at row c' + j <= h.
 - Deep pairs of different parity: {even label, filler}, or {odd label, even label}.
 - The first kind is in the count of saw_residual (i). That count uses only hi + j <= h, which gives j <= H0 = 210, and lo - j >= 1. So the low-p ones are already relocated (D10).
 - For the second kind, t^2 = 4j(d+j) < 9h^2 gives |t| < 3h < 156h, so both points lie in one class, and G_T-independence excludes them. The rigid note defines this through Lemma rival on the strip [1,h].
(d) By Lemma LR, the support is (L), (M-i), (M-ii) or (M-iii). Lemma S empties (M-i) and (M-ii), and Lemma N empties (M-iii).
 Case (L) is treated in absolute rows:
 - mixed_quadruples_blocks Theorem 1 uses |n2| <= h - 1 from rows in [1,h];
 - Theorems 2 to 4 there use no row bound;
 - random_prime Theorems 2 and 3 count with |n2| < h and translation families of at most A, so their counts are upper bounds over [1,h].
 So low-p label-only quadruples are already in A3 and A4.
(e) Count review. I checked every deep-only family in the table of section 4 of the board:
 - A1, A2, A3, A4, A5: rows free, or the strip [1,h].
 - C2: four fillers cannot have a low pair point, by Lemma LR.
 - D2, D3, D4, D14: row-free, or top boundary only (SAW Theorem 1(6) uses q > h).
 - D5, D6: row-free.
 - D7: FFo has W in row y_L + 8o2 >= 309, or needs W <= h.
 - D10: as in (c).
 - D12, D13: the (iii-b) scaling uses 'lowest point >= 1'. By Lemma LR and Lemma S, no homogeneous instance has a low pair point at all.
 - D15: two_filler Lemma 1, row-free.
 - D16 to D18: F1 is size; F3 with n_y >= 1 uses q <= h; F3 with n_y <= -1 and Theorem 3 of two_filler are superset counts with Q < 3h.
 - D19, D20: Lemma N.
 None uses p, q >= 3.
 The sea-involving families in row-3 types (M2c, R_IV, N_h, SLF-Pc, Pb) use u = y - 3. This shift is valid for obstructions with every non-black corner in rows >= 3. The low complement is Theorem A(ii)-(iv), whose low branches need a deep pair with row difference 2 or 4. In L*** none exists:
 - odd-odd differences are 0 (mod 64), even-even 0 (mod 32), and odd-even differences are odd;
 - a label and a filler differ by >= 297 rows;
 - two fillers differ by a multiple of 8.

5. CHECKS (scripts in my script folder; each run with py, one at a time, under 60 s; the repository was only read).
 - norm_residue.py: exhaustive residue check of Lemma N mod 1024, over c in {1,3}, every odd T0 mod 32 consistent with c, o in 0..3, and the three parity patterns. Result: 0 solvable cases. Control with the column offset decoupled (filler column 0 mod 16): 32 solvable cases.
 - norm_geom.py: synthetic regions at h = 400 (six types, random label rows obeying (F1)-(F4), fillers in every non-label deep column) with full mixedeq verification of every candidate. Result: 0 three-label one-filler quadruples. Control with filler rows decoupled from offsets: 18.
 - lowp_classify.py: random deep sets with the L*** row ranges and no congruences, h = 900, 10 seeds, listing every quadruple with a pair point in row <= 2. Only the shapes FF|LL (labels in rows 2 and 10 or 18) and LF|FL (even labels in rows 2 and 18) appeared, as Lemma LR predicts. Their row differences (8, 16) violate (F6) and the mod-32 rule, so the real layout kills them.
 These are sanity checks of the algebra, not of a full L*** board.

6. INPUTS USED (status). Audited:
 - block_sea and sea_row3 Theorem A (with the audit's fixes);
 - rigid Theorem C and G_T;
 - SAW Theorem 1;
 - saw_residual (i) and (iii-a);
 - mixed_quadruples Theorems 1-4;
 - random_prime Theorems 2-3.
 Audited with fixable gaps: v3 Theorem B (FFe, Fee, Foo with a filler vertex under R1). Not audited: two_filler Lemma 1, used only in the count review, not in the new lemmas. Lemma N and Lemma S need only (F1)-(F6).

## External results used

- None beyond the repository. I used the paper's Lemma mixedeq, Lemma rival and Definition obstruction (sec2_prelim.tex, sec5_threshold.tex, read directly), and the audited notes listed in Proof part 6. No web sources were used.

## Checks

Analytic work first; three scripts, one at a time, each under 60 s, in scripts_low_rows/:
- norm_residue.py: exhaustive mod-1024 residue check of Lemma N. 0 solvable cases; the decoupled control gives 32.
- norm_geom.py: synthetic congruence-respecting regions at h = 400, with every candidate verified against Lemma mixedeq. 0 three-label one-filler quadruples; the control without the row-offset coupling gives 18.
- lowp_classify.py: random sets with the L*** row ranges and no congruences, at h = 900. Every quadruple with a pair point in row <= 2 had the shape Lemma LR predicts (FF|LL and LF|FL, with low even labels).
I read the paper's Lemma mixedeq, Lemma rival and the obstruction definition, plus these notes: sea_row3_split.md, audit_sea_row3_split.md, v3_and_cross_block.md, consolidated_board.md, deep_layer_sawtooth.md, saw_residual_families.md, two_filler_row_lemma.md and mixed_quadruples_blocks.md. I grepped threshold_families_random_prime.md and rigid_layout_cross_block.md for every row or strip condition.

## Gaps

- Nothing here is audited. Lemma N (the 2-adic norm lemma) and Lemma LR are new, and Lemma N is the critical one. It is short; an auditor should re-derive the four residue cases and check facts (F1)-(F4) against B5 and B6 of consolidated_board.md, in particular that every label point of a region has slot n = rho0 (mod 4) region-wide.
- Lemma N assumes the coupling (F1)/(F4) holds in every deep non-label column within 2W_h + 1 columns of a label. I did not check that the end phases of Table J1* (at region seams) keep the filler offset rule o = (n - rho0) mod 4. If an end phase re-phases the sawtooth, Lemma N must be re-checked within one obstruction width of the seam.
- Scope: light regions of L*** and their SAW*-shift margins only. The junction obstructions (J1*, audit U1 owed), the Theorem D and E blocks, and the Proposition partial regions are not covered here. Their low-row cases depend on their own constructions.
- Part (a) uses v3 Theorem B (audited with fixable gaps) for the filler-vertex triples FFe and Foo, the latter needing R1, which the board adopts. Part (c) relies on G_T being defined through Lemma rival on the true strip [1,h], as the rigid note states; I did not re-read the G_T definition in stride_menu.md.
- Part (d) treats label-only low quadruples as already counted in A3 and A4. That count is a first moment over (l,p), proved for p in (20h, 40h]; K3 of the board asserts that it carries over to (40h, 80h]. I did not re-check K3.
- Constants: h >= 424, the near-band cutoff T* - 320 and R2' (2i+1 <= 300) are used as stated in B7 and K4. Lemma LR's case 'two diagonal fillers' needs 2h - 420 > h + 2.
- Computations are small sanity checks: an exhaustive residue check mod 1024, which fully covers the congruence step of Lemma N, plus synthetic geometric tests at h = 400 and h = 900. No full L*** census was run.

## Missing estimate

None for Q4. With Lemma N, Q3 needs no estimate either: the family is empty. For the near goal the open items are now Q1 (only the parts that two_filler_row_lemma.md did not settle), Q5/(AP), and the audits U1-U8, plus an audit of Lemma N and Lemma LR here.

## Next steps

- Audit Lemma N first. It is one page of residues and it removes Q3 (D19, D20) and the board's J3-Bad sets for Q3. Re-derive the four cases, and confirm (F1)-(F4) from B5 and B6, especially the region-wide label slot residue rho0 and the coupling of filler offset and row.
- Check that the Table J1* end phases keep the offset rule within 2W_h + 1 columns of every label. If they do not, re-run Lemma N near seams.
- Update consolidated_board.md: section 4 rows D19-D21 become 'empty (Lemma N, Lemma LR/S, Theorem Q4)'; delete Q3 and Q4 from the Gaps; drop the Q3/Q4 J3-Bad sets from B7; replace U6 (Lemma 3L1F-a) by the audit of Lemma N.
- Record in the ledger the L***-specific fact used in part (e): no two deep points differ by 2 or 4 rows. It makes the M2c-low and e = 2 branches of sea_row3 Theorem A empty in L***.
- Run one definition-level census of a row-3 type of L*** at h of about 700 to 1000 (true exclusions, SAW*-shift fillers) restricted to obstructions with a non-black corner in rows 1-2, as an end-to-end confirmation.

