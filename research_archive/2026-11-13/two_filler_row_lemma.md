# Two-label quadruples with fillers in different rows

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: a 2-adic lemma shows that every two-label, two-filler quadruple with fillers in different rows is empty, inside a class and across blocks. So the count N_e(h) reduces to the N_h surface (O(h^(9/5+eps))), the inhomogeneous family of additive_class_split.md is empty, and side-two-label quadruples with a filler diagonal are empty. Not audited yet.

# Result

## Status

proved

## Summary

A 2-adic lemma shows that every two-label, two-filler quadruple whose fillers sit in different rows is empty, inside a class and across blocks, for both parities. The open counts collapse. N_e(h) is the N_h surface, so N_e << h^(9/5+eps) by point_counts Theorem A (or h^(52/27+eps) by Heath-Brown). The Prop 9 family is empty. Side-two-labels quadruples with a filler diagonal are empty by a size argument. Nothing here is audited.

## Statements

Setting. One region R_tau of L** with the SAW* layer (and the SAW layer where stated). The congruences used are:
- (C1) Odd label points of the region have rows y = r (mod 64) in SAW*. In SAW this holds mod 32 inside one class.
- (C2) Label points sit in columns 4n with n = n0 (mod 4). A filler in column 4n_F has offset o = n_F - n0 (mod 4) and row f_o = T* - 24 + 8o, with T* >= h - 63.
- (C3) For an odd label point y_L, f_o - y_L = 8 (mod 16) when o is even, and = 0 (mod 16) when o is odd. In SAW* this follows from f_o - y_L = 8(o + c) (mod 64) with c in {1, 3}. Even label points have even rows and fillers have odd rows, so f_o - y_E is odd.
- (C4) For even label points across classes, R1 (s fixed mod 16 per region type) gives Dy = 0 (mod 32). Inside one class, Dy = 2t with t = 0 (mod 16), in SAW and in SAW*.

Notation. Take a quadruple of Lemma mixedeq (sec2_prelim.tex) with side {A, B} = {L1, F1} and diagonal {C, D} = {L2, F2}. Write:
- U = F1 - L1 = (X1, Y1), Dv = L2 - L1 = (Dx, Dy), and df = f1 - f2 = 8(o1 - o2);
- n = (n_x, n_y), Z = Dv - n, W' = U - Z.

LEMMA 1 (2-adic offset lemma; proved, not audited). If L1 and L2 are both odd and Dy = 0 (mod 32), or both even and Dy = 0 (mod 32), then o1 = o2, that is df = 0. This holds for any Dx = 0 (mod 16), any sign of n_y, inside a class or across blocks.

COROLLARY 2 (Prop 9 of additive_class_split.md; proved, conditional on (C1) to (C3)). In SAW and in SAW*, for odd-odd and even-even quadruples inside one class line, the inhomogeneous within-class two-label, two-filler family (delta_F in {±8, ±16, ±24}) is EMPTY. The count #{(t, s)} of Prop 9 is a superset count without the congruences. Under the real congruences it is 0.

THEOREM 3 (N_e of v3_and_cross_block.md Prop F3; proved, conditional on point_counts Theorem A, which is unaudited).
(a) Odd-odd (SAW*, L**, no R1 needed): the F3 branches with df != 0 are EMPTY. With df = 0, the map (y_L1, Dy, f, k, w) -> (Q, e, n1, X, Y) = (A' + 2N', N', k, Dx - 2k, W'_x - k), with A' = f - y_L1 and N' = -n_y, sends every n_y <= -1 tuple with |Dx| >= 78h to an E0(Q) witness of point_counts_power_saving.md. Explicitly: XY = e^2 + n1^2, n1(X + Y + 2n1) = e(Q - 2e), X, Y >= 1, and Q < 3h. The map is at most 4-to-1 per filler row. Also Dx = Delta, the M2c quantity: the df = 0 surface M A' (w - k) = k(w^2 + M^2) is the N_h surface e w u2 = n1(e^2 + (n1 + w)^2) under (e, n1, w, u2) = (N', k, w - k, A').
Hence N_e(h) <<_eps h^(o(1)) sum over Q < 3h of |E0(Q)| <<_eps h^(9/5+eps). Then E_p[labels hit] = O(h^(9/5+eps)), which is harmless under the relocation rule.
Independent cross-check, resting on Heath-Brown, Ann. Math. 155 (2002), as read from the abstract: every real line of that cubic surface lies in M k (w - k)(...) = 0, so N_e << h^(52/27+eps).
(b) Even-even analogue of the n_y <= -1 branch (L**, SAW*, R1): df != 0 is EMPTY by Lemma 1, and df = 0 obeys the same bound O(h^(9/5+eps)).

PROPOSITION 4 (side two labels with two fillers on the diagonal; proved, no congruences used). Take two label points of different classes, of any parities, with |Dx| >= 74h, as the side. Take two fillers in rows >= h - 87 as the diagonal. For h >= 103 no such mixed quadruple exists. In particular the even-even side-two-labels quadruples left open in v3 are EMPTY, and this gives a second proof of F2 for filler diagonals.

Numerics suggested about h^0.5 for Prop 9 and h^(1+o(1)) for N_e. Those were superset counts without the congruences. They do not survive the layout congruences (Prop 9) or they coincide with N_h (N_e, df = 0).

## Proofs

0. EQUATIONS (from Lemma mixedeq; re-derived as in v3 F3)
- Lemma mixedeq gives n != 0, n.(B - A) = 0, C + D = A + B + 2n, |D - C| = |B - A| and D - C != ±(B - A).
- With V = F2 - L2 we have V = U + 2n - 2Dv = U - 2Z. Then |V| = |U| is equivalent to Z.(U - Z) = 0.
- So the quadruple is equivalent to the two equations
 (E1) n_x X1 + n_y Y1 = 0;
 (E2) Z_x W'_x + Z_y W'_y = 0, with Z = Dv - n and W' = U - Z;
 together with 2n = Dv + V - U.
- Rows: 2n_y = Dy - df. Columns: by (C2), x_L2 = x_L1 (mod 16) and x_Fi - x_Li = 4 o_i (mod 16). Hence 2n_x = Dx + (x_F2 - x_L2) - (x_F1 - x_L1) = 4(o2 - o1) (mod 16), and therefore
 (N) n_x = 2(o2 - o1) (mod 8), X1 = 4 o1 (mod 16), Dx = 0 (mod 16).

1. PROOF OF LEMMA 1. Suppose df != 0, so o1 != o2.
1a. Valuations of n_y and n_x.
- Dy = 0 (mod 32) and |df/2| is in {4, 8, 12}, so v2(n_y) = v2(df) - 1. This is 2 when o1 - o2 is odd and 3 when o1 - o2 = ±2.
- By (N), v2(n_x) is 1 or 2 in the same two cases. In particular n_x != 0.
- X1 != 0 and Y1 != 0, otherwise (E1) forces n = 0.
1b. Even labels.
- Y1 is odd by (C3). (E1) gives v2(n_x) + v2(X1) = v2(n_y).
- By (N), v2(X1) >= 2.
- Case o1 - o2 odd: 1 + v2(X1) = 2, so v2(X1) = 1. Contradiction.
- Case o1 - o2 = ±2: 2 + v2(X1) = 3, so v2(X1) = 1. Contradiction.
1c. Odd labels, first step.
- By (C3), v2(Y1) = 3 if o1 is even and v2(Y1) >= 4 if o1 is odd.
- (E1) gives v2(n_x) + v2(X1) = v2(n_y) + v2(Y1). In both cases this means v2(X1) = 1 + v2(Y1) >= 4.
- So X1 = 0 (mod 16). By (N) this forces o1 = 0, and then v2(Y1) = 3.
- So o2 is in {1, 3} with df = -8 o2, or o2 = 2 with df = -16.
1d. Odd labels, (E2).
- Z_x = Dx - n_x = -n_x (mod 16) and W'_x = X1 - Z_x = n_x (mod 16). Hence v2(Z_x W'_x) = 2 v2(n_x), which is 2 (o2 odd) or 4 (o2 = 2).
- Z_y = (Dy + df)/2 = df/2 (mod 16).
- If o2 is odd: v2(Z_y) = 2, and v2(W'_y) = v2(Y1 - Z_y) = 2, because v2(Y1) = 3. So v2(Z_y W'_y) = 4, which is not 2.
- If o2 = 2: Z_y = -8 = 8 (mod 16), and Y1 = 8 (mod 16) because o1 = 0 is a hole. So W'_y = 0 (mod 16) and v2(Z_y W'_y) >= 7, which is not 4.
- All factors are nonzero, since their valuations are finite. So (E2) fails in every case. QED.
Inputs used: (C1) gives Dy = 0 (mod 32) for odd points, inside a class in SAW (t = 0 mod 16) and region-wide in SAW* (mod 64). (C4) gives it for even points.

2. PROOF OF COROLLARY 2. A within-class quadruple has Dv = (4t, 2t). In SAW, t = 0 (mod 16), so Dy = 0 (mod 32) and Dx = 0 (mod 64). The same holds in SAW* with t = 0 (mod 32). Even points of one class differ by the same vector (4t, 2t). Lemma 1 then gives delta_F = -df = 0. Prop 9's family is exactly the case delta_F != 0, so it is empty.

3. PROOF OF THEOREM 3.
3a. Branches with df != 0. The F3 hypotheses give Dy = 0 (mod 64) for odd points in one SAW* region, because i is fixed mod 32 region-wide; T* is tied to y_P mod 64 per region type. For even points they give Dy = 0 (mod 32) under R1, because T2 - T1 = 2Ds with Ds = 0 (mod 16). Lemma 1 applies to every branch.
3b. Branch df = 0, n_y <= -1.
- Put N' = -n_y >= 1 and Y1 = A' = f - y_L1 >= 1. Use the mirror symmetry x -> -x to take X1 > 0. Then n_x = k > 0, by (E1): k X1 = N' A'.
- In F3 notation, Z_x and W'_x are the roots of z^2 - X1 z + N'(N' + A') = 0. Both are positive, and Dx = Z_x + k.
- Put X = Z_x - k and Y = W'_x - k. Then:
 XY = N'(N' + A') - k X1 + k^2 = N'^2 + k^2;
 k(X + Y + 2k) = k X1 = N' A'.
- Size: X1 >= 2 sqrt(N'(N' + A')) > 2N', so k = N' A'/X1 < A'/2 < h/2. If X and Y were negative, then Dx < 2k < h, which contradicts |Dx| >= 78h (or 74h for even points). So X, Y >= 1.
- With e = N', n1 = k and Q = A' + 2N' < 3h, this is an E0(Q) witness, and e < Q/2.
- Recovery: (e, Q, n1) fixes N', A' and k. The roots {X, Y} are fixed by L = e(Q - 2e)/n1 and W = ±sqrt(L^2 - 4e(Q - e)). There are 2 orderings and 2 mirrors. Also n1 divides e(Q - 2e), which leaves h^(o(1)) choices. The row f takes at most 88 values.
- Hence N_e << h^(o(1)) sum over Q < 3h of |E0(Q)| << h^(9/5+eps), by Theorem A.
- The identity Dx = Delta = M A'/k - j, with j = w - k, follows from the surface equation: k(M^2 + w^2) = M A' j. The algebraic substitution was verified by hand.
3c. Cross-check through Heath-Brown. The df = 0 surface S0: M A'(w - k) = k(w^2 + M^2) is absolutely irreducible, because it is linear in A' with coprime coefficients. Its singular points are (0:0:0:1) and (0:1:0:0), both double points, so S0 is not a cone. On a real line of S0 with M(w - k) != 0, the polynomial M(w - k) must divide k(w^2 + M^2) in R[s, t]. That forces w to be proportional to M, then w = 0. So every real line lies in {M = 0} ∪ {k = 0} ∪ {w = k} ∪ {w = 0}, where every tuple of the count is excluded. Points off lines number << B^(52/27+eps), and summing over the scalings lambda gives h^(52/27+eps).

4. PROOF OF PROPOSITION 4. Let the side be {L1, L2} with S = (Dx, Dy), and the diagonal be fillers {F, F'}, with rows >= T* - 24 >= h - 87.
- Rows: y_F + y_F' = y_p + y_q, where p = L1 + n and q = L2 + n are in the grid. So y_p, y_q >= 2(h - 87) - h = h - 174, and |Dy| = |y_q - y_p| <= 174.
- Lengths: F' - F = (Delta', 8e) with |e| <= 3. Then (Delta' - Dx)(Delta' + Dx) = Dy^2 - 64e^2, whose absolute value is at most 174^2. With |Dx| >= 74h and Delta' = Dx (mod 4), any |Delta'| != |Dx| gives a left side of absolute value at least 4 · 74h > 174^2 for h >= 103. So |Delta'| = |Dx| and |Dy| = 8|e|.
- Then n_x Dx = -n_y Dy with |n_y Dy| <= 24h < |Dx|, so n_x = 0. Then n_y Dy = 0.
- n_y = 0 gives n = 0, which is excluded. Dy = 0 gives e = 0 and F' - F = ±(L2 - L1), which mixedeq excludes. QED.

## External results used

- Heath-Brown, The density of rational points on curves and surfaces, Ann. of Math. 155 (2002): O(B^(52/27+eps)) points off lines on a projective surface of degree >= 3. Used only for the secondary cross-check in Theorem 3, as quoted from the abstract in point_counts_power_saving.md. Not re-read.
- Repository inputs: point_counts_power_saving.md Theorem A (|E0(Q)| << Q^(4/5+eps); unaudited); paper Lemma mixedeq (sec2_prelim.tex, read); v3_and_cross_block.md (L), (S) and F3 setup (unaudited); saw_residual_families.md SAW* definition (unaudited); deep_layer_sawtooth.md row structure of SAW.

## Checks

Scripts are in scripts_remaining_counts/. Each was run with py, one at a time, each under 60 s. One chain that ran past the time limit was stopped and rerun smaller.
- f3_class_general.py builds the 4 points and checks Lemma mixedeq directly, including D - C != ±(B - A).
  - It reproduces the hand instance of saw_residual (iii-b) at h = 1281 (L1 = (644, 323), shifted).
  - Inside a class, SAW and SAW*, odd and even, h = 3000 and 4000, residues r in {1, 3, 9, 17, 41}, T in {33, 35}: every solution has df = 0. There were 0 solutions with df != 0.
- f3_check2.py is the same check without congruences (control, h = 400). It finds solutions for every df in {0, ±8, ±16, ±24} (33 to 118 each). With congruences only df = 0 remains.
- f3_cross_general.py is the cross-class version.
  - Control without congruences: odd at h = 300 gives df != 0 counts 2 to 38; even at h = 250 gives 8 and 3.
  - With congruences (odd, h = 1500, |DM| <= 60; even under R1, |DM| <= 48): only df = 0 survives (5 and 3 for odd, 0 for even).
- ne_count.py counts the df = 0 F3 solutions with Dx >= 78H and A <= H: 28, 168, 695 and 2622 at H = 1e4, 2e4, 4e4 and 8e4. The first three are exactly the point_counts census of N_h^+.
- map_to_e0.py checks all 695 df = 0 solutions at H = 4e4 as E0(Q) witnesses: 0 failures.
- ne_search.py and kappa_stats.py show the congruence-free df != 0 solutions (now irrelevant). Their kappa = e'/gcd(e', k) is >= sqrt(M) always, so the point_counts p-adic lemma does NOT transfer to df != 0. Lemma 1 bypasses this.
- inhom.py reproduces Prop 9's superset count (603 at h = 3000, delta_F = 16).

## Gaps

- Nothing here is audited. Lemma 1 is a page of 2-adic casework and should be rederived first, especially the step v2(W'_y) in the o2 = 2 case and the column relation n_x = 2(o2 - o1) (mod 8).
- Lemma 1 rests on layout congruences taken from unaudited notes. These are (C1) i fixed mod 32 region-wide in SAW* (mod 16 inside a class in SAW), (C2) label slots at offset 0 with filler row T* - 24 + 8 * offset, (C3) the filler-minus-label row valuations, and (C4) R1 for even cross-block pairs. Without R1, even-even cross-block F3 with df != 0 is NOT killed, because Dy is only 0 (mod 8) there.
- The df = 0 bound O(h^(9/5+eps)) is only as good as point_counts_power_saving.md Theorem A, which is unaudited. The Heath-Brown cross-check rests on the theorem as stated in the journal abstract. I did not open the paper to check the hypotheses.
- Theorem 3 inherits the upstream reduction E_p[#labels] = O(N_e log h) of v3 Prop F3 (unaudited). The F3 claim that the n_y >= 1 branch has |Dx| < 45h is not needed for df != 0 (Lemma 1 covers every branch). For df = 0 that branch is still taken from v3.
- Proposition 4 covers only side two labels with a diagonal of two fillers, which is family (e). Side two labels with a label-filler or label-label diagonal is not treated here.
- Numerical checks are small: the within-class direct mixedeq checker at h <= 4000 over a few residues, and the cross-class checker at h = 1500 with |DM| <= 60. They test the algebra and the congruence kill, not the full layout.
- The rows of the R_FF homogeneous (df = 0, within-class) family and the cross-block df = 0 family remain. The first is thick (additive_class_split). The second is now O(h^(9/5+eps)).

## Missing estimate

None for the three requested counts, under the stated congruences and Theorem A. N_e(h) << h^(9/5+eps). The even-even F3 analogue is empty for df != 0 under R1 and O(h^(9/5+eps)) for df = 0. Even-even side-two-labels quadruples with filler diagonal are empty. The Prop 9 inhomogeneous family is empty. The one open point is the even-even cross-block df != 0 branch if R1 is dropped.

## Next steps

- Audit Lemma 1 (about 1 page), then Proposition 4 (a few lines). Together they close Prop 9, F2 and F3 for df != 0, and the even-even side quadruples.
- Audit the df = 0 to E0(Q) map in Theorem 3 (5 lines), then audit point_counts Theorem A. One audited Theorem A then covers cross-class M2c, label-filler M2c and N_e at once.
- Update the notes: additive_class_split.md Prop 9 becomes empty under the congruences; v3_and_cross_block.md F3 needs N_e only for df = 0, which equals N_h; F2 gets the 174-row proof; record R1 as needed for even-even cross-block.
- Check whether Proposition 4's 174-row argument also settles side two labels with a label-filler diagonal. That needs the row of the diagonal label, which is not near the top, so a new argument is needed.

