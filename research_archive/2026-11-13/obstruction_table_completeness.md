# Completeness of the obstruction table for L***

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: Theorem K. Under K8, every violation of (V1) to (V5) in L*** falls in a cell of Table T that is impossible, counted or inside a certified window, and no cell is open. A third proof of Q3 (by x^2 + y^2 = 0 mod 4^k) and a proof of Q4 by inspection are included. Not audited yet.

# Result

## Status

proved

## Summary

The family table for L*** is complete. Q3 (three labels + one filler) and Q4 (low corners in row-3 types) are closed by proofs given here, and no OPEN cell remains. All of this still needs an audit.

## Statements

THEOREM K (completeness of the obstruction table for L***; proved here, not audited, conditional on the cited results).

Let h >= h0 and let L*** be the board of consolidated_board.md (B1)-(B10), truncated to columns 1..m. Assume K8: every parity edge occurs exactly once as a double, and every column is a singleton or a double. Then every violation of (V1)-(V5) of block_sea_classification.md falls in at least one cell of Table T below. By the criterion, a violation is the same thing as a pair of distinct rectangles with equal presentations. Every cell is of one of three kinds:
- (E) impossible, by a cited result or by a proof given here;
- (C) a counted family whose labels go to Proposition partial or to Theorem D blocks;
- (W) internal to a window certified by a cited theorem.

No cell is OPEN. In particular:
- LEMMA Q3 (new; proved here). No mixed quadruple in a light region R_tau consists of three label points and one filler. This holds for both parity patterns {F,o,o,o} and {F,o,e,e}, every role of F and every class pattern. It closes table rows D19 and D20 (Q3), and it supersedes Lemma 3L1F-a.
- LEMMA Q4 (proved here by inspection of the cited arguments). In row-3 types, no obstruction with W, p or q in rows 1-2 lies outside the cells that already cover it. This closes D21 (Q4).
- Q2 (row D15) is empty by two_filler_row_lemma Corollary 2 (not audited). Q1 (rows D17 and D18) reduces to the N_h count O(h^(9/5+eps)) by two_filler Theorem 3 (not audited) and point_counts Theorem A (audited).

NOT CLAIMED: the internal validity of the Proposition partial, Theorem D and Theorem E windows (cited); any audit; m_h = O(h^2). The near-goal bound still depends on (AP) and on the audits of the cited unaudited notes, listed in Gaps.

## Proofs

Status labels: A = audited (with fixable gaps), N = proved but not audited, P = paper, H = proved here (not audited).

0. THE OBSTRUCTION KINDS
Under K8, the criterion (V1)-(V5) is equivalent to validity (block_sea section 0, A). Axis-aligned rectangles enter in only three ways:
- two axis-aligned rectangles: excluded, because each parity edge is a double exactly once (a 4- or 6-cycle in G_S is impossible);
- an axis-aligned and a tilted rectangle sharing a white corner W: this is the parking rule (V2);
- a mixed pair with a vertical side: this gives a rival pair (V5), by the paper's reduction lemma.
Compress with an axis-aligned R3 would need two doubles on the same row pair, which K8 excludes. So the kinds are:
- V1: a fully black tilted rectangle;
- V2: a fatal triple;
- V3: two parked triples at one W;
- V4: a black mixed quadruple, with nonvertical side, from Lemma mixedeq;
- V5: a rival pair.

1. LOCALIZATION (H, from cited facts)
(a) Every object of V1-V5, including V3 pairs and the column of W, lies in 2W_h+1 consecutive columns. For V3: both rectangles have span at most W_h and contain W.
(b) The windows are: the light chain (row-1 tail | buffers and regions | row-1 tail), the Proposition partial instance, the Theorem D blocks and the Theorem E blocks. They are separated by more than 2W_h (B10). So J5 (A) puts every violation inside one window together with its constant tail. The switch chain is a chain, and Lemma rival forbids rows 1 and h (P).
(c) In the light chain:
- every label column is followed by at least 2W_h+1 columns of pure SAW* (margin, B9), and regions are separated by Sea(r0,g) pieces of width 2W_h+1;
- so no violation contains points of two regions, or a label point together with a buffer point;
- a violation without a label point is a pure SAW* violation (row C2), a seam violation (J1*, H; audit U1 owed), or a buffer violation (J2, A).
(d) Inside R_tau:
- two classes of one diagonal have Dt in 16lZ \ {0}, so they are at least 64lp - 2h > 2600h^2 columns apart (J4 with modulus 16l);
- classes of different diagonals have distinct residues rho_s mod 16l (16l > h > |Ds|);
- so the label points of one violation lie in a single class, or in classes with distinct t_c. Then |Dx| >= 4p - 2h > 158h.

2. CONGRUENCES IN R_tau (H)
Here i = iota (mod 32), s = sigma (mod 16) and T_c = 2sigma+1 (mod 32). The rule p t_c = s_c - kappa (mod 16l) gives M_c = M0 (mod 16).
- (L1) Every label column satisfies x = x0 := 4(iota+M0) (mod 64), and the label slots are at offset 0.
- (L2) Odd label points satisfy P - P' in 64Z^2, since (4(32a+16b), 64a) = 64(2a+b, a). Their rows are y = y_P := 2iota+1 (mod 64).
- (L3) Even label points satisfy E - E' in 64Z x 32Z, which is contained in 32Z^2, and E - P is in (0, T_tau) + 64Z x 32Z. Also y_E = y_P + T_c (mod 64), where T_c is fixed only mod 32.
- (Phi) A filler at offset o has row T* - 24 + 8o, and y_F - y_P = 8(o+c) (mod 64), with c = 1 (T = 3 mod 4) or c = 3 (T = 1 mod 4). This holds after the 64k shift. So y_F - y_P is = 0 (mod 8), is = 8 (mod 16) iff o is even, is never = 0 (mod 64), and is = 32 (mod 64) only at an odd offset (a base).
- (N2) If x^2 + y^2 = 0 (mod 4^k), then x = y = 0 (mod 2^k). Induction on k: squares mod 4 are 0 or 1.
- Row ranges: fillers lie in rows [h-210, h], and kept labels lie below T* - 320. In row-3 types, i = 0, i = 2 and j in {0,1} are relocated, so odd label rows are >= 9 and = 1 (mod 4), and even rows are >= 6.

3. SHALLOW CELLS
- block_sea Theorems 1 and 2 (A) give at most one shallow corner per triple, and the shallow sets M2a, M2c and M1C only. For r0 = 3 this uses sea_row3 Theorem A (A), whose hypotheses (H1)-(H3) hold by section 2.
- Every same-parity row difference of deep points in R_tau is a multiple of 8: odd-odd by (L2) and (Phi), even-even = 0 (mod 32) by (L3). The low M2c of sea_row3 (iii) needs |Dy| = 2e in {2,4}, so it is EMPTY (H).
- A rival pair with a row-3 shallow point C needs j <= 2 and t != 0 (mod 4). For t odd, t^2 is odd against 0 (mod 4). For t = 2 (mod 4), j = 1 needs c' even and odd at once, and j = 2 needs 2(c'-1) odd. Impossible (H).

4. DEEP CORNER TRIPLES, AND V1 TO V3
- Theorem B (A) together with Lemma L-adic lists every deep right triple. The only ones that exist are FFo with an offset-0 hole as vertex. Their fourth corner W lies at offset o2 != 0, in a filler column with an odd row, so the triple is parked.
- FFo with a label vertex has W above row h (X >= 234, K4).
- V1 (H): a fully black tilted rectangle has no shallow corner (Theorem 1). Any 3 of its 4 deep corners form a right triple whose fourth corner is black. By the list, the 4L case is excluded by Theorem C, and the cases with F plus two labels by Fee, Feo and Foo. In the case F, F plus a label, the fourth corner is white or outside the grid. FFF does not occur. So V1 is empty.
- V3: a triple with a shallow corner has W in a shallow column, and an all-deep triple has W in a deep column, so mixed pairs are impossible. The remaining pairs are covered by Theorem C (A).

5. DEEP MIXED QUADRUPLES
- The row equation 2n_y = y_C + y_D - y_A - y_B forces an even number of even points, because fillers are odd. So only these compositions occur: 4L; {F,o,o,o} and {F,o,e,e} (3L1F); {L,L',F,F} with L, L' of the same parity; {o,F,F,F}; and 4F.
- 3L1F is handled by Lemma Q3. The other compositions are covered by the cited rows (Table T).

6. RIVAL PAIRS
- A rival pair needs different parities, so only (o,e) and (e,F) occur.
- Cross-class (o,e): t^2 = 4j(d+j) < 4h^2 gives |t| < 2h < 158h, which is impossible (H).
- (e,F) is counted by saw (i), with H0 = 210.

7. PROOF OF LEMMA Q3 (H)
Setup:
- Parity leaves {F,o,o,o} and {F,o,e,e'}.
- Let L be the label paired with F, on the side or on the diagonal, and let {L', L''} be the other pair. Lemma mixedeq gives |F - L| = |L'' - L'|.

Case 1: L' and L'' have the same parity. Then L is odd, by the parity count.
- By (L2) and (L3), L'' - L' is in 32Z^2, so |F - L|^2 = 0 (mod 4^5).
- By (N2), F - L is in 32Z^2.
- So (x_F - x_L)/4 = 0 (mod 8), and F is at offset 0, a hole, with y_F = y_L = y_P (mod 32).
- But by (Phi), offset 0 has y_F - y_P = 8 (mod 16). Contradiction.
This case covers all of {F,o,o,o}, and {F,o,e,e'} when F is paired with o, in every role and every class pattern.

Case 2: {L', L''} = {o, e'} and L = e. Then T_L = T_e' (mod 32).

2a. F on the side: A = F, B = e, C = o, D = e'.
- Put U = B - A, V = D - C and W0 = C + D - 2B. Since 2n = W0 + U and n.U = 0, we get W0.U = -|V|^2 and |U| = |V|.
- By section 2: W0_x = 0 (mod 64), W0_y = T_D - 2T_B = -T_D (mod 64), V_x = 0 (mod 64), V_y = T_D (mod 64), and U_x = 0 (mod 4).
- Mod 64 this gives U_y = T_D, so y_F = y_B - U_y = y_P + T_B - T_D (mod 64). This is y_P, which (Phi) excludes, or y_P + 32.
- In the second case F is a base at an odd offset, and that offset is -U_x/4 (mod 4). So v2(U_x) = 2 and U_x^2 = 16 (mod 128).
- But U_y = V_y (mod 64) gives U_y^2 = V_y^2 (mod 128), and |U|^2 = |V|^2 with V_x^2 = 0 (mod 4096) gives U_x^2 = 0 (mod 128). Contradiction.

2b. F on the diagonal: D = F, C = e', side {A = o, B = e}.
- U = B - A has U_x = 0 (mod 64) and U_y = T_b (mod 64), which is odd.
- Write n = t e0 with e0 = (-U_y, U_x)/g, g odd, t != 0.
- F = A + B - C + 2n lies in a deep column, so n_x is even, and F's offset is n_x/2 (mod 4). Also v2(n_x) = v2(t) and v2(n_y) >= v2(t) + 6 >= 7.
- So y_F = y_P + T_b - T_c (mod 64). The value y_P is excluded.
- If y_F = y_P + 32, then the offset is odd, so v2(t) = 1.
- The condition |W1 + 2t e0| = |U| with W1 = A + B - 2C reads 4t^2|e0|^2 + 4t(W1.e0) + (|W1|^2 - |U|^2) = 0.
- The 2-adic valuations of the three terms are exactly 4 (|e0|^2 odd), at least 9 (v2(W1.e0) >= 6, since W1_x and U_x are = 0 mod 64), and at least 7 (from W1_y - U_y = -2T_c and W1_y + U_y = 2(T_b - T_c) = 0 mod 64). Contradiction.

Only (L1)-(L3) and (Phi) are used. No sizes, no p and no l are needed. QED

8. PROOF OF LEMMA Q4 (H, by inspection)
Shallow-point families with a low corner are handled by sea_row3 Theorem A (A) and section 3. For the deep-only families, each cited argument uses p and q only through p, q in Z x [1,h], in the forms |n_y| <= h-1, y_q <= h or q above the grid, or not at all. The shift of sea_row3 2(i) is never used. Read item by item:
- mixed_quadruples Theorems 1 to 4 and the random-prime conventions (|n2| <= h-1);
- two_filler Lemma 1 and Corollary 2 (no rows), Proposition 4 (it derives its lower bound from y_p + y_q, a sum of filler rows), and Theorem 3 (Q < 3h);
- saw (iii-b), where 2d <= h - y_F, and the R_FF edges of additive Lemma 1, which are defined by shapes alone and are all removed by Theorem IV and Theorem D;
- v3 Propositions F1-F3 (|n_y| <= h, n_y <= h - f1);
- SAW Theorem 1(4'): here all four points lie in rows [T*-24, T*], so p and q lie in rows >= T* - 36;
- SAW Theorem 1(6): upper bounds only (audit);
- Lemma Q3: no rows;
- the (e,F) rival count, which runs over every j with lo - j >= 1;
- deep corner triples: Proposition E (A), with no W in rows 1-2.

9. TABLE T (cell: verdict; source; status; labels hit)

WINDOWS
- WP, Proposition partial (case (a) for even h inside the row-1 tail; case (c) for odd h with the global z): W; paper; P.
- WD, Theorem D blocks: W; polylog Theorem D, weighted form; A, with (AP) proved in ap_hypothesis_henriot (N); ends E4 N.
- WE, Theorem E blocks: W; t1 Theorem E; A.
- X, a violation meeting two windows: E; J5 and the separation of (B10); A.
- SW, row 1 left of z, row h right of z: E; chain and Lemma rival; P.

LIGHT CHAIN
- L1, two regions, or a label point with a buffer point: E; section 1(c); H.
- L2, pure SAW* with sea: E; SAW Theorem 1(3),(4') with the shift; A for SAW*, H for the shift (row C2).
- L3, SAW* with Sea(r0,g) at a seam: E; J1*; H (U1).
- L4, buffer pieces and seams, and tails: E; J2 and Lemma sea; A and P.

CORNER TRIPLES WITH A SHALLOW CORNER (W in a shallow column)
- S0, two shallow corners: E; (F1) and sea_row3 Theorem A; A.
- S1, E is the vertex, with ee (Pa): E; v3 A(i); A.
- S2, E is the vertex, with oo or oe, any classes (Pb, X1): E; v3 A(i); A.
- S3, E is the vertex, with o and a base (Pb): E after relocation; y_L <= 205, R2'; N, constants K4 H; O(h).
- S4, E is the vertex, with eF or with a hole: E; parity and rows mod 8 (block_sea Theorem 1, Theorem B); A.
- S5, E is the vertex, FF: E; W row > h for h >= 424; A and U8.
- S6, E is an end, with V, G odd in one class (Pc): parked; v3 A(ii); A.
- S7, E is an end, V, G odd in different classes: E; v3 A(ii) mod p; A.
- S8, E is an end, V, G even: E; v3 A(ii) with Lemma L-adic(i); A and H.
- S9, E is an end, mixed parity (X2 shape): E; parity and rows; A.
- S10, E is an end, V odd and G a hole (SLF-Pc): parked; Theorem B; A. With G a base: E (a = 0 mod 4); A.
- S11, E is an end, filler vertex and label end: E; W below row 1; A and K4.
- S12, E is an end, FF: E; SAW Theorem 1(3); A.
- S13, row-3 types with W in rows 1-2: E; sea_row3 Theorem A(ii); A.

DEEP CORNER TRIPLES (W in a deep column)
- T1, LLL, any classes, including both points of one label: E; rigid Theorem C and Proposition 1(b); A.
- T2, Fee, Feo, Foo (every vertex): E; Theorem B, the SAW* kill, Proposition E, R1, and L-adic(ii); A and H.
- T3, FFe: E; A. FFo with a label vertex: E; X >= 234; H. FFo with a filler vertex: parked only; Theorem B; A.
- T4, FFF: E; A.
- T5, row-3 types with W in rows 1-2: E; Proposition E; A.

V1, V2 AND V3
- V1: E; section 4; H.
- V2, fatal triples: E; S0-T5.
- V3: SLL/SLL E (A(iii)); SLL/SLF E (W rows); SLF/SLF in one class E; SLF/SLF across classes with equal i is family (d), C, Proposition D, A, h^(1+o(1)) labels, and empty for h < 2560 (64p > 2W_h); FFo/FFo E (Theorem C); a shallow-W triple with a deep-W triple E (the columns differ; H).

MIXED QUADRUPLES WITH A SHALLOW POINT
- M0, shallow set {C,D}, three shallow points, one shallow point on the side, or four: E; Theorem 2, and sea_row3 A(iii) for low corners; A.
- M1, M2a with diagonal oo, oF or FF: E; odd deep rows are all congruent mod 8; A.
- M2, M2a with diagonal ee, any classes: E; Corollary B (nu >= 2; Dn(c) = 0 mod 16l); A.
- M3, M1C: E; D would need row 1 (mod 4) (row-1 types) or 3 (mod 4) (row-3 types); A.
- M4, M2c with oo in one class: C; R_IV, then Theorem IV and Lemma IV, with Bad_split sent to Theorem D; N and AP; large heights O(h^(11/6)).
- M5, M2c with oo or ee across classes: C; Proposition 5 and point_counts Corollary B; A; O(h^(9/5+eps)).
- M6, M2c with ee in one class: E; B3(C1); A.
- M7, M2c with B odd and D a filler: C; saw (ii-a,b) and point_counts Theorem A; A; O(h^(9/5+eps)). With the filler shallower than the label: E by rows (H).
- M8, M2c with FF: E; SAW Theorem 1(4'); A. Mixed-parity pairs: E by parity.
- M9, row-3 types with p or q in rows 1-2: E; section 3; H.

DEEP MIXED QUADRUPLES
- D-4L, four labels: E for I.1, II(1,1), II(-1,-1) and II(1,-1) with Sigma = 0, and for three or four classes (mixed_quadruples Theorems 1, 2, 4; Proposition 1(c); A). C for I.2 and for II(1,-1) with Sigma != 0 (random-prime Theorems 2 and 3; A; B h^(1+o(1))).
- D-3L1F, {F,o,o,o} and {F,o,e,e} (all roles and classes): E; Lemma Q3; H. Other compositions: E by parity.
- D-2L2F, ll/FF and FF/ll in one class: E; saw (iii-b); A.
- ll/FF across classes: E; two_filler Proposition 4; N. With the shift: fillers lie in rows >= h-210, so |Dy| <= 420, and 4·158h > 420^2 for h >= 280, with |n_y Dy| <= 24h < 158h; H.
- FF/ll across classes: E; v3 F1, and S5 by Lemma 4(a) and Proposition 1(d); A.
- Mixed sides with df != 0, any classes: E; two_filler Lemma 1 and Corollary 2; N.
- Mixed sides with df = 0 in one class: C; d > 0 has finitely many shapes (R_FF^+); d < 0 goes to Theorem IV with Lemma FF' and then Theorem D; A, N, H and AP.
- Mixed sides with df = 0 across classes: E for n_y >= 1 (|Dx| < 106h + 2; v3 F3 and K4; A and H) and for n_y = 0 (A); C for n_y <= -1 (N_e = N_h, O(h^(9/5+eps)); two_filler Theorem 3 (N) and point_counts Theorem A (A)). The even-even version is the same, by Theorem 3(b).
- {o,e,F,F}: E by parity.
- D-1L3F, label on the diagonal: S2 near band (Theorem 1(2b)), T1 and CE (Theorem 1(5)), O(sqrt h) per diagonal (Theorem 1(6)); A, with a cutoff of 156 rows below the filler row, covered by T* - 320; C, O(h^(3/2)).
- D-1L3F, label on the side: E (q is above the grid); A. {e,F,F,F}: E by parity.
- D-4F: E; SAW Theorem 1(4'); A.

RIVAL PAIRS
- R1, any rival pair with a shallow point: E; Lemma rival and section 3; P and H.
- R2, (o,e) in one class: E; Theorem C; A. Across classes: E by size (|t| < 2h < 158h); H.
- R3, (e,F): C; saw (i) with H0 = 210; A; O(h^(3/2)).
- R4, (o,F), (o,o), (e,e), (F,F): E by parity.

LOW CORNERS (Q4): E; Lemma Q4; H.
JUNCTIONS: E1 (J1*, H); E2 (J2-J5, A); E3 (Theorem E ends, A); E4 (Theorem D ends, N).

OPEN CELLS: none.

## External results used

- None outside the repository. Lemma Q3 uses only the elementary fact that x^2 + y^2 = 0 (mod 4^k) implies x = y = 0 (mod 2^k). Repository inputs are cited per cell in Table T: the paper's Lemmas mixedeq, rival, reduction, sea and chain and Proposition partial; block_sea Theorems 1-2 and the criterion; sea_row3 Theorem A; v3_and_cross_block Theorems A-C and Propositions D-F; saw_residual (i), (ii) and (iii); deep_layer_sawtooth Theorem 1; mixed_quadruples Theorems 1-4; threshold_families Proposition 1 and Theorems 2, 3 and 5; two_filler_row_lemma; point_counts Theorem A and Corollary B; polylog Theorem D; t1 Theorem E; full_layout J1-J5; consolidated K1-K8.

## Checks

Scripts are in scripts_completeness/. They ran with py, one at a time, each in under 5 s.
- foee_mod64.py and run2.py: an exact solver for mixed quadruples made of three label points and one free point F. The model is a region with i = iota (mod 32), M = M0 (mod 16) and T = T0 (mod 32), several classes with different T and M, and no grid or prime constraints.
  - It solves the line-and-circle equations (F on the side) and the t-quadratic (F on the diagonal).
  - Every solution was asserted from Lemma mixedeq: n.U = 0 and |U| = |V|.
  - Result: 3113 solutions with F in a deep column and an odd row, over both parity patterns, every role, and one-class and cross-class patterns. Every one has y_F = y_P (mod 64), so none could be a filler. This agrees with Case 1 and with the T-difference-0 branch of Case 2.
- mixedpar.py: a targeted search for Case 2 (F paired with an even label). It found 127 solutions over three runs, all in branch 2a with T difference 0 mod 64 and residue 0. It found no T-difference-32 instance and no branch-2b instance.
- By hand:
  - Lemma Q3 in full, including the identity W0.U = -|V|^2 and the valuations in 2a and 2b;
  - the lattice facts (L1)-(L3);
  - the filler residues (Phi) under the 64k shift;
  - Proposition 4 constants with fillers in rows >= h-210;
  - the localization distances (margins, J4 with 16l, |Dx| > 158h);
  - the low-M2c and row-3 rival-pair one-liners.
- The repository was only read.

## Gaps

- Nothing here is audited. Lemma Q3 (2-adic casework, Case 2 in particular) and Lemma Q4 (an inspection of the cited arguments) need a second reader. So do the one-line H items: the low M2c, rival pairs with a row-3 shallow point, cross-class (o,e) rival pairs, V1 from the triple list, Proposition 4 with the shifted filler rows (h >= 280), and the localization in section 1.
- Completeness is relative to criterion (V1)-(V5). That needs K8 (each parity edge exactly once, every column a singleton or a double), which is an unaudited step of consolidated_board.md.
- Many cells close only through unaudited inputs: two_filler_row_lemma (Lemma 1, Corollary 2, Theorem 3, Proposition 4); consolidated J1*, Lemma L-adic, Lemma FF' and the K4 constants; R2'; deep_layer_bh16 A1 and A3; the proof of (AP) in ap_hypothesis_henriot.md; the Theorem D block ends (E4).
- Lemma Q4 rests on my reading of the notes. SAW Theorem 1(6) and rigid Theorem C were checked only through their statements and their audits, not line by line.
- Numerical sanity checks are small and use no grid bounds or prime structure. In the Case 2 branches with T difference 32 mod 64, my search found no instance at all, so those branches are tested only by the proof.
- No definition-level census of L*** at true spacing (p > 40h) was run. Cross-class configurations are out of reach below h of about 1300.
- The windows WP, WD and WE are cited as violation-free. I did not reclassify their internal obstructions.

## Missing estimate

None for completeness. Under the cited results, every cell of the obstruction table is impossible, counted at O(h^(2-delta)) labels or removed by a colouring, or certified as a window. What the near goal still needs is outside the table: the audits (Lemmas Q3 and Q4 here, two_filler_row_lemma, J1*, L-adic, FF', K4, K8, deep_layer_bh16 A1 and A3, the Theorem D ends) and the audit of (AP).

## Next steps

- Audit Lemma Q3 first (about one page). It closes D19 and D20 for every class pattern, using only the mod-64 lattice (L1)-(L3) and the filler residues (Phi).
- Audit Lemma Q4 by re-reading each deep-only proof in the list of section 8 for any use of y_p, y_q >= 3.
- Update consolidated_board.md section 4: D15, D19 and D20 become EMPTY; D21 is closed; D17 and D18 become counted at O(h^(9/5+eps)); add the missing explicit cells M1 (M2a with an oF diagonal), M7 (filler shallower), M9 (low M2c), R2 (cross-class oe rival pairs) and the V3 cross-type cell.
- Audit two_filler_row_lemma (Lemma 1, Proposition 4 with the shifted constants, and the Theorem 3 map to E0(Q)), since D15-D18 rest on it.
- Run one definition-level census of a single L*** region type with the shifted T* at h of about 450 to 650, as a test of the single-class cells. Cross-class cells need h above about 1300 and stay proof-only.

