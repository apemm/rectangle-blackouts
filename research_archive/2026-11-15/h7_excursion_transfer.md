# The excursion decomposition in design H7

15 November 2026. Problem 001. Continues the gap-mixing notes of 2026-11-14 (continuation_gap_mixing_audit.md, p_excursion_decomposition.md, p_cross_scale_chains.md). Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: the decomposition carries over to design H7 for the three label-only families, P (when sigma M >= 3), Lambda3 and Lambda4: no event crosses a diagonal cut and every event stays within two consecutive links. FW does cross cuts, with an exact integer witness at M = 3, sigma = 1 and h about 5.7e12 to 7.7e12, so the full six-family H7 choice problem does not reduce to finite recurring systems; only the label-only part does. Certificate: every H7 P excursion system of scale <= 1024 has an empty weighted 3-core, for all 28 offsets and both orientations. Not audited yet.

# Result

## Status

partial

## Summary

The excursion decomposition carries over to design H7 for the three label-only families, P (when σM ≥ 3), Λ3 and Λ4: no event crosses a diagonal cut, and every event stays within two consecutive links. FW does cross cuts, and an exact integer witness shows it at M = 3, σ = 1, h ~ 5.7e12–7.7e12. So the full six-family H7 choice problem does not reduce to finite recurring systems. Only the label-only part does. One computed certificate: every H7 P excursion system of scale ≤ 1024 has an empty weighted 3-core, for all 28 offsets c and both orientations.

## Statements

Setting. Design H7, one residue block. A label z = (i_z, j_z) has odd row a0 + 28 i_z and even row b0 + 28 j_z, with D = 28 and c := b0 - a0 odd, |c| <= 27. Put T_z = j_z - i_z. The Hilbert curve is recursion (2) on the padded Q-square, with original ranks kept. Columns are x = x0 + S(M r + xi), where S = 8 D^2 sigma = 6272 sigma, sigma >= 1 is a power of 2 and 0 <= xi < M. An event is a label set J (|J| >= 2) with its geometric conditions. Its span is max rank minus min rank. A cut is the rank of a diagonal cell (x,x), x >= 1. Excursions and links are as in p_excursion_decomposition.md: links have sides 1, 2, ..., B/2, then O2 of side B.

THEOREM 0 (cut theorem for event families; proved). Suppose a family of events in a Hilbert Q-square satisfies two conditions:
- (A'ev) if an event contains a label with |T| <= 2s-1, then its span is <= s^2;
- (Bev) no event contains both a label of an aligned main-diagonal block E and a label of rank < rho(E).
Then no event crosses any cut, every event lies inside one excursion, and every event lies inside one link or two consecutive links. Condition (Phi) implies both (A'ev) and (Bev): T_z^2 >= 4 * span(J) for every label z of every event J.

THEOREM 1 (P transfers to H7; proved for sigma*M >= 3). Every candidate P constraint has the cross-pair Pythagorean form, with no strip test and no owner test. Each such constraint satisfies the following:
- Lemma A'7: if an endpoint has |T| <= 2s-1, then d <= s^2.
- Lemma B7: nothing enters a diagonal block from the left.
- Sign separation: both endpoints have T of the same strict sign.
Hence the H7 P system of a block is the disjoint union of its excursion systems, with no boundary conditions. Every constraint joins the same link or two consecutive links. The proof needs no T1 normal form and no S = 2^e: the case d = 1 follows from Y >= 113.

THEOREM 2 (Lambda3 and Lambda4 transfer; proved for every sigma >= 1, M >= 1, |c| <= 27). Every label-only tilted right angle that is not all of one parity satisfies (Phi), in fact T_z^2 >= 9e6 * span. So does every label-only nonvertical mixed four-support, in both parity cases (b) and (c) and in the degenerate rectangle case, with T_z^2 >= 1.3e7 * span. The proofs use only Hilbert locality, S | X and orthogonality, with no strip test. So Theorem 0 applies to P ∪ Lambda3 ∪ Lambda4. Every label of a Lambda event has |T| >= 3129, so Lambda events occur only in links of side >= 1565.

COROLLARY 3 (reduction of the label-only part; proved).
- Rigid diagonal translation preserves all candidate conditions. So the candidate system of P ∪ Lambda3 ∪ Lambda4 on E_x is a translate of a fixed finite system Pi_B^o(c; sigma, M), with B = B_x and o the orientation of D_x. The final excursion lies in Pi_Q^swap.
- Pi_B^o(c) is a chain W_0 -> ... -> W_{j-1} -> W_j' of first-off-diagonal links, with events only inside a link or between consecutive links.
- If every Pi_B^o(c) with B <= Q is certified-M-solvable, then P ∪ Lambda3 ∪ Lambda4 is solvable in every block at height h. If this holds for all B, it is solvable at every h.
- No boundary conditions arise between excursions.
- (Computed, one implementation) At sigma = 1, M = 3, the weighted 3-core of the candidate P system on the Q = 2048 square is empty for all 28 odd c in [-27, 27] and both top orientations. Lambda is empty at these scales, so every Pi_B^o(c) with B <= 1024 is certified-3-solvable by reverse peeling.

PROPOSITION 4 (the sea families are T-free; proved).
- FW, 6PT and R2s events involve no cross-parity label-label row difference. 6PT-same involves only the hub's own gap.
- An FW event (odd role) has i_f - i_e = Delta in (S^2/(2D)) Z_{>0} = 702464 sigma^2 Z_{>0}. In the even role, j_f - j_e is in 1404928 sigma^2 Z_{>0}.
- The FW rank gap is fixed by e's row alone: d in {floor(|q|/M), ceil(|q|/M)}, with |q| = k|F - a_e|/(2|xi'|).
- A 6PT-same event has i_e = i_f - Delta and j_e' = j_f - Delta, with Delta in 32 sigma Z (224 sigma Z in mixed blocks with s in {L, H}). It also has |j_e - j_e'| and |i_e - i_e'| < 4 sqrt(d_ee'). So e and e' sit next to the diagonal translate f - (Delta, Delta).
- Consequently any FW or 6PT-same event with a label in an excursion of scale B with 2B <= Delta joins two excursions.
- FW is not row-sparse. Every role row with |F - y| > M sigma S^3/4 admits the arithmetic solution (k, xi') = (1, +-1). So R2s-style row relocation cannot remove FW.

PROPOSITION 5 (FW crosses cuts; exact witness, computer-assisted). Take sigma = 1, M = 3, block (a0, b0) = (1, 2) and sea row F = 2007 (profile class g = 6). Then for every h in [5.742e12, 7.69e12] (padded side Q = 2^38), these three labels form an FW candidate event:
- e = (205049396512, 205049396443), rank 40924868087275944369487, in an excursion of scale 2^9;
- f = (205050098976, 205049091641), rank +956897183388, in the O2 link of an excursion of scale 2^20;
- g = the label at rank r_f + 1.
It is the exact pattern (xi_e, xi_f, xi_g) = (1, 2, 0). S0 lies in e's own empty slot. The right angle, W's column and the strip conditions were all verified in exact integers. In total 19 such witnesses were found, at Q = 2^36 and Q = 2^38. One of them joins T_e = -2064 to T_f = +114523, across the diagonal.

CONCLUSION (on the reduction). The full six-family H7 choice problem does not reduce to finite recurring systems. FW events join excursions (Proposition 5). FW and 6PT also depend on absolute rows through m = s - y, so they are not translation-invariant. What holds:
- block problem = (disjoint union over excursions of translates of Pi_B^o(c)) + H_row;
- H_row = FW ∪ 6PT, with R2s removed by the relocation of r2s_relocation_o_h2.md (asymptotic, conditional on (Rel), not audited);
- H_row is a hypergraph of events on 2 to 4 labels, each forbidding one value of its last-placed label (Lemma G). Its cross-excursion events have the exact displacement form of Proposition 4.
The reduction to the recurring family {Pi_B^o(c)} holds in any block and height range where H_row is empty. FW is empty for h <= 6.16e10 M sigma^4, but 6PT-same has no proved emptiness range.

## Proofs

0. NOTATION AND FACTS USED
- (F1) For distinct labels at rank distance d >= 1, the column difference is X = S(Md + delta) with |delta| <= M-1. So |X| >= S(M(d-1)+1) >= S d.
- (F2) Hilbert locality (audited Theorem 1, continuation_hilbert_placement.md): |Delta i|, |Delta j| < 4 sqrt(d). Hence |T_f - T_e| < 8 sqrt(d).
- (F3) Same-parity pair: the row difference is Y_s = D*Delta, with Delta = Delta i (odd role) or Delta j (even role). Then Y_s^2 < 16 D^2 d <= 16 D^2 |X|/S = 2|X|/sigma.
- (F4) Cross pair (odd point of e, even point of g): Y_c = b_g - a_e = c + D U with U = j_g - i_e. Here U - T_e = j_g - j_e and U - T_g = i_g - i_e. The other role is symmetric, with U = j_e - i_g. So |T_z| > (|Y_c| - 27)/D - 4 sqrt(d_eg) for z in {e, g}.
- Hilbert facts, from recursion (2): H_{2q} lists Q1 (the transposed H_q on [0,q)^2), Q2, Q3 (the translate on [q,2q)^2) and Q4. A transpose fixes diagonal blocks. So in both orientations the diagonal children are visited 1st and 3rd. Every aligned diagonal block starts at its lower-left cell, and its first R^2 ranks form the diagonal sub-block of side R. Diagonal cells are visited in increasing order.

1. THEOREM 0
Induction on x. Put s = 2^{v2(x)}, E = [x, x+s)^2 and D' = [x-s, x+s)^2. D' is aligned, and E is its third child, so rho(x,x) = rho(E) = rho(D') + 2s^2 and rho(D') = rho(x-s, x-s). Suppose an event has a label v with rho(v) < rho(x,x) and a label w with rho(w) >= rho(x,x).
- If some label lies in E, this contradicts (Bev).
- Otherwise every later label has rank >= rho(D') + 3s^2.
  - If rho(v) >= rho(D'), then v is in the first two children of D', so |T_v| <= 2s-1, while span >= s^2 + 1. This contradicts (A'ev).
  - If rho(v) < rho(D'), then x - s >= 1 and the event crosses the cut at x - s < x. This contradicts the induction hypothesis. At x = 1, rho(D') = 0, so this case is empty.

Links: an event with labels in links L_a and L_b, a <= b-2, has span >= s_{b-1}^2 + 1. Its label in L_a has |T| <= 2 s_a - 1 <= 2 s_{b-1} - 1, and (A'ev) then gives span <= s_{b-1}^2. Contradiction.

(Phi) => (A'ev): if |T_z| <= 2s-1, then 4 span <= (2s-1)^2 < 4s^2.

(Phi) => (Bev): let w be at offset m in E and v before E. Then span >= m + 1. Let R be the least power of 2 with R^2 >= m+1. Then |T_w| <= R - 1 < 2 sqrt(m+1) <= 2 sqrt(span). (If R = 1, then T_w = 0.) This contradicts (Phi).

2. THEOREM 1 (P). Write kappa = sigma M >= 3. Since Y^2 >= 2X + 1 (L >= X + 1),
 (Y/D)^2 > 2S(M(d-1)+1)/D^2 = 16(kappa(d-1) + sigma) >= 16(3d-2).

Lemma A'7. Suppose |T_z| <= 2s-1 and d >= s^2 + 1. Then |U| < 2s - 1 + 4 sqrt(d), so Y < 27 + D(2s - 1 + 4 sqrt(d)) < D(2s + 4 sqrt(d)). So we would need 4 sqrt(3d-2) - 4 sqrt(d) < 2s. But sqrt(3d-2) - sqrt(d) is increasing, because 9d > 3d - 2. At d = s^2 + 1 it is >= s/2:
- s = 1: 2 - 1.414 = 0.586;
- s >= 2: > 0.732s - 1/(2s) >= s/2.
Contradiction.

Lemma B7. In the notation of section 1, |T_w| < 2 sqrt(d) - 1, so |U| < 6 sqrt(d) - 1 and Y < 6 D sqrt(d). Then 36d > 16(3d-2), which forces d <= 2.
- d = 1: m = 0, T_w = 0 and |U| <= 3, so Y <= 27 + 84 = 111. But Y^2 >= 2S + 1 >= 12545, so Y >= 113.
- d = 2: |T_w| <= 1 and |U| <= 6, so Y <= 195. But Y^2 >= 2S(M+1) + 1 >= 12544(kappa + sigma) + 1 >= 50177, so Y >= 225.

Sign separation. If T_v <= 0 <= T_w, then |U| < 4 sqrt(d).
- d = 1 gives Y <= 111 < 113.
- d >= 2 would need 25088d - 6048 sqrt(d) - 25817 < 0, that is d < 1.31.
Lemmas A'7 and B7 are (A'ev) and (Bev) for two-label events, so Theorem 0 applies.

3. LAMBDA3. V is a point of label e. F is a point of label f with V's parity, f != e. G is a point of label g with the other parity, g != e, since g = e would make the angle axis-aligned. Write (X1, Y1) = F - V and (X2, Y2) = G - V, with X1 X2 = -Y1 Y2, |Y1| >= D and |X2| >= S.
- (F3) gives |X1| > sigma Y1^2/2. So |Y2| = |X1||X2|/|Y1| > sigma S|Y1|/2, and y := |Y2|/D > sigma S/2 >= 3136.
- From Y1^2 < 2|X1|/sigma = 2|Y1||Y2|/(sigma|X2|): |Y1| < 2|Y2|/(sigma|X2|), |X1| < 2Y2^2/(sigma S^2), and |X2| < 2|Y2|/(sigma D).
- So d_ef < 2 D^2 y^2/(sigma S^3) <= 6.36e-9 y^2 and d_eg < 2y/(sigma S) <= y/3136.
- (F4) on (e, g), and (F2) on (e, f): min_z |T_z| > y - 1 - 4 sqrt(y/3136) - 8 * 7.97e-5 y >= 0.99777 y, using sqrt(y) >= 56.
- span <= d_ef + d_eg < 1.081e-7 y^2. Hence T^2 >= 9.2e6 * span.
The case f = g is the same. All labels share the sign of U.

4. LAMBDA4 (side AB, diagonal C Dp). Case (a), all four points of one parity, is impossible (H7 S3(b)). The vertical case is P. Assume X = x_B - x_A != 0, which gives |X| >= S.

(b) Even components (A, B of one parity; C, Dp of the other). The audited argument with alpha = 2/sigma gives Dp - C = (X, -Y) up to order, with X Z0 = -Y(y_C - y_B) and Z0 = x_C - x_A != 0. Put R = |y_C - y_B| (cross).
- R >= S|X|/|Y| > S sqrt(sigma|X|/2), so |X| < 2R^2/(sigma S^2) and R >= 351234.
- |Z0| < R sqrt(2/(sigma S)) and |Y| < 2R/(sigma S).
- Dp - B = (Z0, (y_C - y_B) - Y). So (A, C) and (B, Dp) are cross pairs with |row difference| >= R - |Y| and rank distance <= |Z0|/S < 7.97e-5 rho, where rho = R/D >= 12544.
- span <= (|X| + 2|Z0|)/S < 1.91e-8 rho^2, and every |T| > 0.99928 rho. Hence T^2 >= 5e7 * span.

(c) Odd component (A, B of opposite parity; C with A's parity, Dp with B's parity, after a swap). Put m = x_C - x_A, n = x_Dp - x_B, p = y_C - y_A and q = y_Dp - y_B. Then m, n != 0: m = 0 or n = 0 would force a hypotenuse equal to a leg. Let u = |m| and w = |n|, with u, w >= S, and use (F3): p^2 < 2u/sigma and q^2 < 2w/sigma.
- If m + n = p + q = 0, the four points form a rectangle with diagonals AB and CD. Its two corner triples are Lambda3 events that share e_A and e_B, so section 3 gives T^2 >= 4e6 * span.
- Same sign: u + w = |Y||p+q|/|X| < 2|Y| sqrt((u+w)/sigma)/S, so u + w < 4Y^2/(sigma S^2) and |X| < 2|Y|/sqrt(2 sigma S).
- Opposite sign: the audited identity is |Y| = |Delta|^2 |m+n|/(4|mq - np|), with |Delta|^2 >= (u+w)^2 and |mq - np| < (u+w)^{3/2}/sqrt(sigma). This gives u + w < 16Y^2/(sigma S^2) and |X| < 8Y^2/(sigma S^2).
- Both cases: |Y| >= S^{1.5} sqrt(2 sigma)/4, so y = |Y|/D >= 6272, and span < 7.63e-8 y^2. With (F4) on (A, B) and (F2) on (A, C) and (B, Dp), every |T| > 0.99726 y. Hence T^2 >= 1.3e7 * span.

5. COROLLARY 3. Take two aligned diagonal 2B-blocks of the same orientation at diagonal offset t. They have the same local rank order and contiguous rank intervals. With equal choices, the map z -> z + (t, t) is a rigid motion of every label point: rows move by D t and columns by S M (rank shift). P, Lambda3 and Lambda4 candidate conditions are rigid-motion invariant. Only the strip and bulk tests are not, and the candidate version drops them, which gives a superset. With Theorems 0 to 2 this yields the decomposition and the solvability implication.

Each certified event, in its mod-M version, forbids one class of its last label. So the weighted-core reverse peeling of L9, and T8 of p_cross_scale_chains.md, extend to hyperedges, with the core defined by event counts: a component of the core inside Pi_i is a union of components of K(Pi_i). I give this extension as a sketch only.

Computation: the weighted 3-core is empty in all 56 runs. With the swap runs, the Q = 2048 squares contain translates of P_B^o for every B <= 1024 and both o. By section 3 and 4, Lambda is absent for link side < 1565.

6. PROPOSITION 4
- R2s, FW and PT events use only same-parity label differences and label-to-sea differences m = s - y. In 6PT-same, the only cross quantity is m - m' = b_f - a_f.
- FW: S^2 | X xi = -delta m, with v2(m) = 1 (odd role) or 0 (even role) and v7(m) = 0. So delta is in (S^2/2) Z (odd role) or S^2 Z (even role), and delta > 0 because the row of W, F + delta, lies in [1, h].
- With (k, xi') = (1, +-1): X = +-S|m|/2 is a multiple of S, and the necessary (Hil) bound |X| > M sigma delta^2/2 - (M-1)S reads |m| > M sigma S^3/4 - 2(M-1). So every such row is admissible, and FW is not row-sparse.
- 6PT-same: e pairs with f's odd point and e' with f's even point at the same delta, so i_e = i_f - Delta and j_e' = j_f - Delta. Locality on (e, e') gives the rest.
- Crossing: D_y has i-extent 2B. If 2B <= Delta, then the label shifted by Delta in i lies outside D_y, and E_y is contained in D_y.

7. PROPOSITION 5 (fw_cross_witness.py). The search uses odd role, k = 1, xi' = +-1, q = +-|F - a_e|/2 and labels with |T_e| <= 4096. It is vectorized in numba with split-base ranks. Every hit was re-verified in Python integers:
- the inverse Hilbert map at r_f;
- the slot equation, with choices xi_e = 1, xi_f = 2, xi_g = 0, so x_f - x_e = S q;
- a_f - a_e = delta = S^2/2;
- X xi + delta m = 0, the right angle at A;
- x_g = x_f + xi, with g != f;
- the excursion indices, by binary search over diagonal ranks.
Locality is consistent: Delta^2/(16d) = 0.032. The row range gives the h interval.

8. CONCLUSION. This combines Corollary 3 with Propositions 4 and 5. FW and 6PT depend on m = s - y, so the translation argument of section 5 fails for them.

## External results used

- Hilbert locality max(Delta i^2, Delta j^2) < 16|Delta r| for recursion (2) with ranks not compressed: Theorem 1 of continuation_hilbert_placement.md (audited). Used in every proof.
- Normal forms of Lambda4: the even-component reduction to Dp - C = (X, -Y) with alpha = 2/sigma, and the identity 4X(mq - np) = |Delta|^2 (p+q), from continuation_hilbert_mixed_supports.md and hilbert_angles_mixed_thresholds.md Theorem 2, as confirmed in audit_hilbert_sea_design_h7.md and audit_hilbert_angles_mixed_thresholds.md. Used in section 4.
- Design H7 definitions and Lemmas S3(b), S4 and S6; residual Propositions E and F; Lemma G (hilbert_sea_design_h7.md, audited with fixable gaps; hilbert_residual_families.md, audited). Used for the family definitions in Propositions 4 and 5.
- Excursion and link structure, and the T8/L9/C12 framework, from p_excursion_decomposition.md and p_cross_scale_chains.md (unaudited). I re-derived here the parts I use.
- The R2s relocation of r2s_relocation_o_h2.md (unaudited). Cited, not used in any proof.
- No published theorem was used, and I consulted no web source.

## Checks

Script folder: scripts_gm4_transfer/. Every script ran with py -I, one at a time, each under 60 s and well under 1 GB.

1. h7_p_cuts.py (Q M sigma c [swap]) is my own builder for the H7 candidate P system: Hilbert recursion (2), divisor pairs of Y^2 with 6272 | X, Y = |c + 28U|, both roles. It reports cut crossings, constraints joining non-consecutive links, opposite-sign constraints and the weighted M-core.
- Q = 256 and Q = 1024 (M = 1, 2, 3; c in {-27, 1, 27}), and Q = 2048 (M = 2 with c = 1; M = 3 with all 28 odd c in [-27, 27] and both orientations): 0 cut crossings, 0 non-consecutive links and 0 opposite-sign constraints in every run.
- At M = 3, max d/(min|T| + 0.5)^2 is about 0.041 (proved bound: d <= ((|T|+1)/2)^2).
- At sigma = 1, M = 3, the weighted 3-core is empty in all 56 runs at Q = 2048 (46k to 402k constraints per run). At M = 2 and c = 1 the 2-core has 93 labels.
- Constraint counts satisfy the c <-> -c, id <-> swap symmetry exactly.

2. fw_cross_witness.py (n trials seed F0) runs a self-test of its numba and Python Hilbert maps against the recursion on all 4096 ranks at n = 6.
- n = 38, 10^7 trials, F0 = 2007: 14 hits.
- n = 38, 4*10^6 trials, F0 = 2035: 4 hits.
- n = 36, 4*10^6 trials, F0 = 2007: 1 hit.
- Every hit was re-verified in exact integers (slot equation, right angle, W column, strip) and joins different excursions. The quoted witness has qa mod 3 = 1, so S0 lies in e's own empty slot.

By hand: Theorem 0, Lemmas A'7 and B7 (including the small cases d = 1 and d = 2 and the monotonicity step), sign separation, and every constant in sections 3 and 4.

I only read the repository, ran no git command, left Kagey-Problems untouched, installed nothing, and wrote no report file.

## Gaps

- Nothing here is audited: Theorem 0 (event version), Lemmas A'7 and B7, and the (Phi) proofs for Lambda3 and Lambda4 still need an independent reader. They depend only on audited Hilbert locality, the recursion-(2) facts re-derived above, and the audited normal forms of Lambda4 (the alpha = 2/sigma argument for case (b), and the identity for case (c)).
- Theorem 1 is proved only for sigma*M >= 3. At sigma*M = 2 the constant in Lemma A'7 fails (4(sqrt 2 - 1) < 2). The sanity runs found no crossing at M = 1 and M = 2 for Q <= 2048 (c = 1) and Q <= 1024 (c in {-27, 1, 27}), but that is unproved.
- Only inclusion is proved: each actual excursion system is contained in a translate of the candidate system Pi_B^o(c). An H7 analogue of Corollary A1 (equality in an interior row range) is not proved, so failure of some Pi_B^o(c) would not by itself obstruct the real board.
- The hypergraph extension of T8, L9 and C12 to P ∪ Lambda events is sketched, not written out.
- The weighted-3-core certificate (all 28 values of c, both orientations, Q = 2048, sigma = 1, M = 3) comes from one implementation, mine. Its sanity checks are the c <-> -c, id <-> swap symmetry of the constraint counts and 0 cut crossings. Scales B >= 2048 are untested.
- The FW witness is a candidate-level event (choices realizing it exist) for sea row F = 2007. I did not recompute AP4's choice of F at h in [5.74e12, 7.69e12], so the witness applies exactly only if AP4 selects 2007; the mechanism itself does not depend on F (a second run with F = 2035 also gave 4 hits). It rests on one implementation and inherits H7's unaudited inputs (N1, AP4, Lemmas S4 and S6, Lemma G).
- 6PT (both kinds) and R2s are shown to be T-free, and 6PT-same is shown to cross whenever its hub lies in an excursion with 2B <= Delta. I have no explicit 6PT witness: an event needs two simultaneous Hilbert coincidences.
- The R2s removal relies on r2s_relocation_o_h2.md, which is unaudited, asymptotic only and conditional on (Rel).
- No bounded-M statement about H_row (FW ∪ 6PT) is proved. The full H7 problem therefore stays open even where every Pi_B^o(c) is solvable.

## Missing estimate

The H7 choice problem now splits into two parts.

(1) The recurring label-only systems Pi_B^o(c), for B >= 2048. For B <= 1024 the computation shows they have empty 3-cores at sigma = 1, M = 3. For larger B one needs either a uniform certified-3-solvability theorem for chains of first-off-diagonal links, or DEC plus the two-block systems, exactly as at S = 32.

(2) The row hypergraph H_row = FW ∪ 6PT, which crosses excursions and depends on absolute rows. The cleanest estimate that would remove FW by relocation is a Hilbert row-lag anti-concentration bound. Let N(i0, d, Delta) be the number of j such that the cell at rank r(i0, j) + d has first coordinate i0 + Delta. The bound needed is N(i0, d, Delta) <= Q^{1-eps}, on average over rows i0. For FW, d depends only on the row, so the total number of FW labels would be h^{2-eps+o(1)} and relocation would cost o(h^2). The heuristic value of N is Q/sqrt(d).

6PT-same has heuristically about h^2 log h / S events. Relocation cannot remove it, so a choice argument must absorb it: a local-lemma or greedy bound for a sparse hypergraph across excursions, combined with the shift-closed certified excursion solutions.

## Next steps

- Audit Theorem 0, Lemmas A'7 and B7, and the Lambda3 and Lambda4 (Phi) proofs. They are short and carry the H7 transfer.
- Record in the ledger: P (sigma*M >= 3), Lambda3 and Lambda4 never cross a diagonal cut in H7 and stay within two consecutive links. FW does cross cuts (the witness above). The full six-family H7 problem does not reduce to excursions.
- Extend the H7 P certificate to scale 2048 by building one excursion P_2048^o(c) (about 5.6M labels) per c and orientation, split into runs under 60 s. Then test the weighted 3-core.
- Attack FW by relocation: try to prove the row-lag bound N(i0, d, Delta) <= Q^{1-eps} from the digit structure of Hilbert row ranks. Alternatively, change the design so that slot-column sea points cannot serve as the S0 corner of a PT. The residual note says putting H at slots breaks S1, so a different sea assignment would be needed.
- Use the 6PT-same structure: e and e' lie at the diagonal translate f - (Delta, Delta), with Delta in 32 sigma Z. Look for a 2-adic or 7-adic kill, or a design shift of the diagonal that makes such translates land on padding.
- Write out the hypergraph versions of T8, L9 and C12 for P ∪ Lambda, then rerun the DEC tests on H7 chains once their cores are nonempty.

