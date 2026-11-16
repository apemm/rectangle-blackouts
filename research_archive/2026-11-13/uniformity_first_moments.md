# Uniformity of the first-moment bounds (N-3)

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: Theorem U. Each random-prime first-moment bound of the board (A4, B7, D8, D17 and D18) holds for every fixed class structure, psi, kappa and b_tau, and the factor B in A4 and D8 drops out. D11 is deterministic. So Theorem N of consolidated_board_v2.md no longer needs hypothesis N-3, and the exponent is unchanged. Lemma U3 assumes that the Theorem D blocks do not use (l, p), which block_layout_n1.md supports. Not audited yet.

# Result

## Status

proved

## Summary

N-3 (K6 uniformity) holds. Each random-prime first-moment bound (A4, B7, D8, D17, D18) holds for every fixed class structure, psi, kappa and b_tau. The factor B in A4 and D8 drops out. D11 is deterministic. Theorem N loses hypothesis N-3 and keeps its exponent. Not audited.

## Statements

SETTING. Fix h >= h0 and one region type tau = (iota, sigma) of L***. Adm is the set of admissible pairs (l, p) of (B2), with #L >= (1/2 - o(1)) 1.04h/log h and #P >= (10 - o(1)) h/log h (non-explicit PNT in progressions).

A CLASS DATUM Xi is any assignment of the light labels of type tau to subclasses that satisfies:
 (Xi1) every light label lies in exactly one subclass;
 (Xi2) every subclass lies inside one diagonal s;
 (Xi3) the subclasses of one (s, tau) carry pairwise distinct indices k in Z_{>=0};
 (Xi4) every subclass is independent in G_T. This is used only by the deterministic exclusions, for example b != 0 in I.2. It is not used by any count.
The board's classes followed by any outcome of psi form a class datum. Xi does not depend on (l, p).

Positions follow (B5): label (i, j) of subclass (s, k) sits at slot n = i + p t + b, with t = rho_s + 16 l k and p rho_s = s - kappa (mod 16l), 0 <= rho_s < 16l. Here kappa and b = b_tau are arbitrary integers. X_F(Xi, kappa, b; l, p) is the number of labels hit by family F, in the F(Lambda) sense of V2-1.

THEOREM U (proved here, not audited). For every class datum Xi and all integers kappa and b, with E the average over (l, p) uniform on Adm:
 (A4, I.2) E X <= 4A h^(2+o(1)) / (#L #P) = h^(1+o(1)).
 (A4, II(1,-1) with Sigma != 0) E X <= h^(1+o(1)).
 (B7, cross-class M2c, oo and ee) E X <= C h N_h^int / min(#L, #P) = O(h^(9/5+eps) log h).
 (D8, v3 family (d)) E X <= 2h * h^(1+o(1)) / #P = h^(1+o(1)).
 (D17, cross-class F3, odd-odd, df = 0, n_y <= -1) E X <= 2h * 512 N_e / #P = O(h^(9/5+eps) log h).
 (D18, the even-even analogue) E X <= 4h * 512 N^ee / #L = O(h^(9/5+eps) log h).
The right-hand sides depend only on h. They do not depend on Xi (so not on the class structure or on psi), on kappa, or on b. Hence, for the classes and the psi already fixed, some (l, p) in Adm has X_A4 + X_B7 + X_D8 + X_D17 + X_D18 <= C h^(9/5+2eps). This is just min <= average, so Markov is not needed.

LEMMA U3 (proved, not audited). Every configuration F(Lambda) whose labels Lambda lie in one subclass is a translate, by a multiple of 4 columns, of a picture that does not depend on (l, p). So Bad_split, the graphs R_IV, R_FF^oo, R_FF^ee and R_FF^+, the event of Theorem D, the sets E_D and the R-e set do not depend on (l, p).

COROLLARY (K6). The order "classes (deterministic), then psi in the intersection of the Theorem D events, then (l, p)" is legitimate. N-3 is no longer a hypothesis of Theorem N; it becomes an N-status result (proved, not audited).

Corrections to v2:
 (1) In V2-9, A4 and D8 become h^(1+o(1)) instead of B h^(1+o(1)).
 (2) D11 is a deterministic bound, valid for every (l, p) and every Xi. It does not belong in the Markov sum (K6 item 3).
 (3) Step 3 of K6 can read "choose (l, p) minimising the sum".
None of these changes the exponent of Theorem N or its n_rel.

## Proofs

0. WHAT HAS TO BE SHOWN
Theorem N picks (l, p) after the classes and psi. That is legitimate when two things hold:
 (i) for every fixed outcome of the earlier choices, the average over Adm of the relocated-family count is at most a bound that depends only on h;
 (ii) nothing chosen earlier depends on (l, p).
Item (ii) is Lemma U3, together with the remark that G_T, the type restriction and psi are defined without (l, p). Item (i) is Theorem U.

The proof has three steps:
 - Lemma U1 lists the position facts that hold for every Xi and every (l, p).
 - Lemma U2 is one counting template.
 - Section 3 checks each family against the template. For each family it lists the places where the original proof touches the class structure and shows that only (Xi1) to (Xi3) enter.

1. LEMMA U1 (position facts, for every Xi, kappa, b and admissible (l, p))
Let L1 and L2 be labels of R_tau in subclasses c1 = (s1, k1) and c2 = (s2, k2). Write Dt = t2 - t1, Ds = s2 - s1, Di = i2 - i1, DM = p Dt and Dn = Ds - p Dt.
 (a) Dn = 0 (mod 16l). Moreover Dt = 0 iff c1 = c2 iff Dn = 0.
 (b) A slot holds at most one label. If a point P (a column and a row) is the odd or even point of some label of R_tau, that label is determined by P, (l, p), kappa, b and Xi.
 (c) Given a subclass c1 and an integer D, at most one subclass c2 has t_{c2} = t_{c1} + D.
 (d) Write Dx and Dy for the column and row differences of two points. If both points are odd: Dx/4 - Dy/2 = DM. If both are even: Dx/4 - Dy/2 = -Dn.

Proof.
 (a) By definition p t = s - kappa (mod 16l), so p Dt = Ds (mod 16l).
  - If Dt = 0, then Ds = 0 (mod 16l). The s-range of a type has fewer than h < 16l values, so Ds = 0. Then 16l(k2 - k1) = 0, so c1 = c2.
  - If Dn = 0, then Ds = p Dt with |Ds| < h < p, so Dt = 0.
  - The converses are immediate.
 (b) Write n - b = i + p t with 0 <= i < A < p. The division algorithm gives (i, t) uniquely.
  - Then rho_s = t mod 16l and k = floor(t/16l).
  - s -> rho_s = p^(-1)(s - kappa) mod 16l is injective on fewer than 16l consecutive integers, so s is unique.
  - So the slot can hold only the label (i, i + s), and only if that label lies in subclass (s, k).
  - For a point, the column gives the slot, so the label is unique; the row then has to match its odd or its even row.
 (c) t_{c2} determines (s2, k2), as in (b).
 (d) Odd points: Dx = 4(Di + p Dt) and Dy = 2Di. Even points: Dy = 2(Di + Ds). Compute.
Only (Xi1), (Xi2) and (Xi3) are used.
Sanity script u1_check.py: random Xi, random admissible (l, p), random kappa and b, h in {101, 160, 257, 400}, 12 runs of 20000 pairs each. Result: 0 failures of (a), (b) and (d).

Two arithmetic facts are used below:
 - Every point of a violation lies in 2W_h + 1 consecutive columns (P3). So for two points of one configuration, |Dx| <= 2W_h <= h^2/2 + 2 and |Dy| < h.
 - Hence |DM|, |Dn| <= h^2/8 + h. That is below (1.04h)^2 and below (40h)^2. A nonzero integer below (1.04h)^2 has at most one prime factor in (1.04h, 2.08h]. A nonzero integer below (40h)^2 has at most one prime factor in (40h, 80h].

2. LEMMA U2 (counting template)
Let F be a family of configurations in R_tau. Each configuration has a label set Lambda with |Lambda| <= lam. Assume there is a set Sigma (the shapes), which depends only on h and tau, with three properties.
 (S1) Every configuration realised at (l, p) has a shape sigma in Sigma.
 (S2) sigma determines a nonzero integer Delta(sigma) and one of two things:
  - [p-type] Delta = DM between two of its points in distinct subclasses, for every realisation at every (l, p);
  - [l-type] Delta = Dn between two such points;
  - [both] sigma determines DM and Dn.
 (S3) There is a free index phi in a set of size at most Phi. Given (sigma, phi), some point P0 of the configuration (the anchor) is the odd or even point of a label determined by (sigma, phi) alone. Every other support point is P0 plus a vector that depends only on (sigma, l, p).
Then, for every Xi, kappa and b, the sum over (l, p) in Adm of X_F is at most:
 - lam Phi |Sigma| #L in the p-type case;
 - lam Phi |Sigma| #P in the l-type case;
 - lam Phi |Sigma| in the both case.
So E X_F <= lam Phi |Sigma| / #P, / #L or / (#L #P) respectively.

Proof.
 - Realisability. By (S2), realisation at (l, p) needs p | Delta, or 16l | Delta, or both, and Delta is nonzero and below the thresholds of section 1. So for a p-type shape the realising pairs lie in L x {p0}, for an l-type shape in {l0} x P, and in the both case there is at most one pair.
 - Uniqueness. Fix (sigma, phi, l, p). The anchor label L0 is fixed by (sigma, phi). Its subclass is Xi(L0), which does not depend on (l, p). So its slot, and hence P0, are fixed. Every other support point is P0 plus a fixed vector. By U1(b), every label point among them belongs to at most one label. Fillers and sea points are fixed by position: in F(Lambda), every non-label slot is a filler of the sawtooth row, margins included. So at most one configuration exists.
 - Summing over sigma, phi and the realising pairs gives the bound.
The proof uses Xi only through the map L0 -> Xi(L0) and U1. So the bound holds uniformly in Xi.

3. THE FAMILIES
For each family below: the shape set Sigma, its type, the anchor and free index, and the places where the source proof uses classes.

3.1 A4 (I.2): threshold_families Theorem 2, in the form of the audit.
 - Shape: sigma = (skeleton (a, T0, T', b), n2). By the audit, |Sigma| <= Sum_a 4 tau(N_a) Sum_T0 (h gcd(a, T0)/(4|a|) + 1) = h^(2+o(1)). This count is layout-free.
 - Type: both. N = Dn = (Ds + U n2/(8a))/2, with Ds fixed by (T0, T'), and DM = Ds - N. Also 0 < |N| < h^2/14 and 0 < |DM| < h + h^2/14.
 - Anchor: A, the odd point of slot i0 on diagonal T0 (mixed_quadruples Theorem 3). Free index phi = i0, so Phi <= A. The label of A is (i0, i0 + s0), and it is unique.
 - Other points: B is the even point of slot i0 + a in the same subclass. C is the odd point of slot iC in the subclass at t + Dt, where Dt = DM/p and iC - i0 is fixed by E2. D is the even point of slot iC + b. Each is P0 plus a vector fixed by (sigma, l, p).
 - Bound: E <= 4A h^(2+o(1)) log^2 h/(c h^2) = h^(1+o(1)).
 - Where classes enter the source: "at most B' class pairs per realised tuple, and per class pair a translation family of at most A quadruples". This bound is already uniform: it uses only (Xi3), through at most B subclasses per (T, tau), and U1(c), which fixes c' from (c, Dt). The template sharpens it. Each i0 fixes the T0-label, and (Xi1) puts that label in one subclass, so the B' factor overcounts. The exclusion b = 0 uses (Xi4). Subclasses inherit independence in G_T, so the exclusion holds for every Xi.

3.2 A4 (type II with Sigma != 0): threshold_families Theorem 3.
 - Shape: the skeleton (Sigma, Dd, H, De, U2). Its count is h^(2+o(1)), by the conic identity, r_2 and the triple count. The count is layout-free.
 - The skeleton recovers (d, d', eta, eta') and hence T0, T' and Dj, and so the vectors g = C - A and g' = D - B. U = (4(Dj - Dn), 2Dj + T0) is fixed through Dn.
 - Type: both. Dn = Dj + U2(Sigma - Ds)/(8 Sigma) is fixed and nonzero, and DM = Ds - Dn with |DM| <= 0.13h^2 + h/2.
 - Anchor: A, with phi = iA, so Phi <= A. Then B = A + U, C = A + g and D = B + g'.
 - Bound: E <= h^(1+o(1)).
 - Classes enter the source in the same two places as in 3.1, and the same remarks apply.

3.3 B7 (cross-class M2c): threshold_families Proposition 5 (audited form), Corollary B for N_h^int.
 - Shape: the M2c tuple (n1, w, e, u2), with n1 | e u2, together with r0 (2 values). So |Sigma| <= 2 N_h^int << h^(9/5+eps).
 - The shape fixes the rows of B and D and Delta = x_D - x_B, so it fixes the vector D - B. The shallow points A and C sit at fixed offsets.
 - Odd-odd is p-type: DM = Delta/4 - (y_D - y_B)/2 by U1(d). DM is nonzero because the classes differ (U1(a)).
 - Even-even is l-type: Dn = -(Delta/4 - (y_D - y_B)/2). Mixed parity is vacuous (audit).
 - Anchor: B. Its row fixes i_B (odd) or j_B (even). Free index phi = s_B, so Phi <= h.
 - Bound: E <= 2 * 2h * N_h^int / min(#L, #P) = O(h^(9/5+eps) log h).
 - Where classes enter the source:
  - odd-odd: "j_B free, s_D forced by the rigid rule". This is U1(c) and U1(b).
  - even-even: "Ds forced mod p, s_B free".
  Both use only (Xi1) and U1. Under U1(b) the even-even step simplifies: D's point determines D's label, so the step "Ds is forced mod p" is not needed.

3.4 D8 (v3 family (d)): v3 Proposition D.
 - Shape: (u, hole row, gamma1, gamma2), with gamma_k | N = ug/2. So |Sigma| <= h * max tau^2 = h^(1+o(1)), and the count is layout-free.
 - The shape fixes x_V2 - x_V1 = (e1 - e2)(4G - R) with y_V2 = y_V1. It also fixes the hole vectors G_k - V_k and W.
 - Type: p-type. DM = (x_V2 - x_V1)/4 is nonzero (different classes) and below 0.63h^2.
 - Anchor: V1. Its row fixes i. Free index phi = s1, so Phi <= h.
 - Bound: E <= 2h * h^(1+o(1)) / #P = h^(1+o(1)). The source states this bound without B.
 - Where classes enter the source: "c1 is any class holding a label with that i, and c2 is fixed by Dm". These are (Xi1) and U1(c).
 - Under the board's 512 types, which build in R1, realised pairs need |x_V2 - x_V1| >= 64p (audit). This changes nothing in the upper bound.

3.5 D17 (two_filler Theorem 3(a) with the v3 F3 reduction).
 - Shape: (y_L1, Dy, f, k, w), with f a filler row of the type (at most 106 values).
 - The df != 0 branches and the n_y >= 1 branch are empty for every (l, p) and every Xi. They use only:
  - Dx = 0 (mod 64) and Dy = 0 (mod 64), from the type and [F1];
  - |Dx| <= 106h + 2 < 158h.
 - The df = 0 shapes map at most 4-to-1 per filler row into E0(Q) witnesses with Q < 3h. So |Sigma| <= 512 * 4 * 106 * h^(o(1)) * Sum_{Q<3h} |E0(Q)| << h^(9/5+eps). The factor 512 is the sum over types, since f depends on the type.
 - The shape fixes Dv = L2 - L1 and the filler vectors.
 - Type: p-type. DM = Dx/4 - Dy/2 is nonzero.
 - Anchor: L1, with free index s1, so Phi <= h.
 - Bound: E <= 2h * |Sigma| / #P = O(h^(9/5+eps) log h).
 - Where classes enter the source: "labels per shape at most h/8; a shape fixes DM". These are (Xi1) and U1(b).

3.6 D18 (two_filler Theorem 3(b) with V2-7).
 - Shape: as in 3.5, with even L1. Lemma 1 kills df != 0 (Dy = 0 mod 32 because s is fixed mod 16). The df = 0 shapes are O(h^(9/5+eps)) through the parity-free E0 map.
 - Type: l-type. Dn = -(Dx/4 - Dy/2) is nonzero, and |Dn| < h^2/16 + h/2 + 1 < (1.04h)^2.
 - Anchor: L1. Its row fixes j1. Free index s1, so i1 = j1 - s1 and Phi <= 2h.
 - Bound: E <= 2 * 2h * |Sigma| / #L = O(h^(9/5+eps) log h).
 - Where classes enter V2-7:
  - "L1 is unique and its class does not depend on (l, p)". This is (Xi1): Xi is fixed before (l, p).
  - "Given p, Ds = Dn (mod p), so L2 is unique". U1(b) replaces this step: L2's point determines L2.

3.7 The other cells of (B7)
 - D11 (label-filler M2c) is deterministic. By saw_residual (ii-b) and point_counts Corollary C(2), a label with odd row y_B is hit only if, for one of the O(1) filler rows, e = (Q - u2)/2 lies in E(Q) contained in E0(Q). The filler offsets are slot offsets mod 4, fixed by [F1]. So the hit set depends only on rows and the type. It is the same for every (l, p) and every Xi, and it has at most (h/2) * Sum |E0(Q)| = O(h^(9/5+eps)) labels.
 - D10 (rows; saw (i)), D4 (Theorem 1(6)), D1, R-a, R-b, R-c and R-d are row-defined or diagonal-defined. They are independent of (l, p) and of Xi.
 - R-e: the labels touched by large-height R_IV and R_FF edges are bounded through Lemma IV over all label pairs of a (T, tau). That is a superset of the in-subclass edges, so the bound holds for every Xi. It is (l, p)-free by U3.
 - The E-cells that the families rely on hold for every admissible (l, p) and every Xi. They use only the residues of l and p, the size of p, [F1], and (Xi4) for in-class independence. These cells are: Proposition 1(b) to (d), the II roles other than (1,-1), Lemma 1, and the F3 n_y >= 1 branch.

4. LEMMA U3: (l, p)-INDEPENDENCE OF THE EARLIER CHOICES
Take two labels of one subclass. They have Dt = 0 and a common s. So their points differ by (4Di, 2Di) (odd-odd), by (4Di, 2Di) (even-even), or by (4Di, 2(Di + s) + 1) (odd point to even point). None of these involves (l, p).
 - Every label slot is congruent to rho_tau mod 16 [F1]. So the filler at relative slot w has offset w mod 4, and its row T*_tau - 24 + 8(w mod 4) does not depend on (l, p). The margins continue the same sawtooth, and (Phi) does not re-phase it.
 - Shallow columns are those not divisible by 4. A translation by 4(p t + b) preserves them.
 - In F(Lambda) with Lambda inside one subclass, every slot outside Lambda is a filler.
So an in-subclass configuration is a translate of an (l, p)-free picture. The following are therefore (l, p)-free:
 - the R_IV and R_FF edges (in-subclass M2c and two-filler shapes);
 - Bad_split, which consists of the shallow ends of monochromatic small-height edges;
 - the hypotheses of Theorem D (P(f in Y) through psi only, independence across T);
 - its event and E_D, since the D blocks are profile blocks right of z that do not use (l, p);
 - the R-e set.
G_T (Lemma rival inside a diagonal), the type restriction and psi are defined without (l, p).

5. ASSEMBLY
 - The classes are deterministic.
 - Choose psi in the intersection of the Theorem D events. Its probability is positive by the polylog audit, and U3 shows the events do not involve (l, p).
 - With Xi now fixed, Theorem U gives Sum over Adm of X <= #Adm * C h^(9/5+2eps). So some (l, p) has X <= C h^(9/5+2eps).
 - For that (l, p), the width bound of the light regions (t < 16l(B+1)) holds, as it does for every admissible pair. Every deterministic E-cell holds, by 3.7.
So K6 holds as stated, without probabilistic independence between psi and (l, p).

6. EFFECT ON THEOREM N
 - N-3 is now an N-status result (Theorem U and Lemma U3; proved, not audited).
 - In V2-9, replace "B h^(1+o(1)): A4, D8 (Markov)" by "h^(1+o(1)): A4, D8". Move D11 to the deterministic terms.
 - n_rel = O(h^(2 - eps_D) log B + h^(11/6) log h + h^(9/5+eps) + h^(3/2) + h). The term B h^(1+o(1)) becomes h^(1+o(1)).
 - The bound M <= C h^2 (log h)^(3/2) (loglog h)^C1 is unchanged. Theorem N stays conditional on N-1 (K8'(b) and E4), the V2 steps, and the completeness of the K2 and K4 lists.

## External results used

- Prime number theorem in arithmetic progressions mod 5 and mod 20 (non-explicit), for #L >= c h/log h and #P >= c h/log h.
- tau(n) << n^eps and r_2(n) <= 4 tau(n), through the cited shape counts.
- No new external theorem. The shape counts are taken from audited notes: threshold_families (A9), point_counts Theorem A and Corollary B for N_h^int (A9), and two_filler Theorem 3 (A10).

## Checks

I read these in full:
 - consolidated_board_v2.md;
 - threshold_families_random_prime.md and its audit;
 - v3_and_cross_block.md and its audit;
 - two_filler_row_lemma.md and its audit;
 - point_counts_power_saving.md and its audit;
 - polylog_relocation_diluted.md, Theorem D through Theorem IV.
I read the following only as far as needed:
 - the I.2 statement of mixed_quadruples_blocks.md Theorem 3 (A is the odd point of slot i0 in c0; iC - i0 fixed by E2; b fixed by the skeleton);
 - saw_residual (ii-b) for D11;
 - the AR remark of t1_cost_decomposition.md (not used in L***).
By hand, I derived:
 - U1(a) to (d);
 - the size thresholds for one-prime realisation;
 - the template U2;
 - the per-family shape type, anchor and free index;
 - the (l, p)-independence of in-subclass configurations (Lemma U3).
One script ran in my script folder, u1_check.py, with py -I in a few seconds. It drew random class data, random admissible (l, p), random kappa and b, at h in {101, 160, 257, 400}, 12 runs of 20000 label pairs each. It tested U1(a), the slot injectivity U1(b), and U1(d). Result: 0 failures. The repository was only read, and no git command was run.

## Gaps

- Theorem U and Lemma U3 are proved here and have not been audited. The template (Lemma U2) and its check against each family need a second reader. The most important points are the I.2 and II anchors (the skeleton plus Dt fixes every relative vector) and the l-type versus p-type classification of B7, D17 and D18.
- Theorem U rests on the shape counts and on the realisation arguments of the source notes: the I.2 and II skeleton counts, N_h^int, the E0(Q) map, and the Proposition D shapes. Those are audited (A9 and A10), but for p in (20h, 40h]. I re-checked only the thresholds that realisation uses: |N|, |Dn| < (1.04h)^2 and |DM| < (40h)^2. I did not re-derive the counts themselves.
- Uniformity is proved for the five random-prime families of (B7) R-f, and D11 is shown deterministic. A random-prime family missing from Theorem K's list would not be covered. Completeness of the table is A-25's job.
- Lemma U3 assumes that the Theorem D blocks do not use (l, p). The notes support this (profile blocks right of z), but no definition-level D block exists, which is N-1.
- The sanity script u1_check.py checks only the position facts of Lemma U1, on small synthetic regions. It does not test any family count.
- h0 is not explicit (PNT in progressions mod 5 and mod 20). The o(1) and eps exponents come from divisor bounds.

## Missing estimate

None for N-3. Theorem U gives every random-prime first moment with a bound that depends only on h. The total over A4, B7, D8, D17 and D18 is O(h^(9/5+2eps)), uniformly in the class structure, psi, kappa and b_tau.

## Next steps

- Have Lemmas U1 to U3 and section 3 audited, about two pages. Re-derive the I.2 and II anchor-and-vector claims from mixed_quadruples Theorem 3 and from threshold_families Theorem 3.
- Update consolidated_board_v2:
   - move N-3 out of the hypothesis list (status N);
   - in K6, replace Markov by 'min <= average' and drop D11 from the sum;
   - in V2-9, change A4 and D8 to h^(1+o(1));
   - replace the V2-7 step 'Ds forced mod p' with U1(b).
- Add one line to each of the source notes (threshold_families Theorems 2, 3 and Proposition 5, v3 Proposition D, two_filler Theorem 3): the bound holds for every class datum Xi with (Xi1) to (Xi3), and the B' factor is not needed.
- Turn to the remaining hypothesis of Theorem N, N-1 (K8'(b) and E4). In particular, confirm at definition level that the Theorem D and E blocks do not use (l, p), which Lemma U3 assumes.

