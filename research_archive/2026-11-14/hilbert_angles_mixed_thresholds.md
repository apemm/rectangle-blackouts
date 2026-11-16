# Right angles and mixed supports at smaller stride

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: with M private choices at stride S = 2^e, every surviving cross-parity label right angle has the form F - V = lambda(Sa, S^2 b), G - V = c(-Sb, a) with |a| > M S^4/16, so none exists once M S^4 >= 16(h - 1), four times better than the bound on file. Mixed supports with even components and mixed parity vanish under the same condition, odd-component ones once sqrt(M) S^4 >= 128 sqrt(2) (h - 1), and all-one-parity ones once S >= 16. A barrier configuration shows locality and divisibility alone allow about 2h/S^4 angles at one label, so these tools stop at S of order h^(1/4). Audited in audit_hilbert_angles_mixed_thresholds.md (correct with fixable gaps).

# Result

## Status

partial

## Summary

At stride S = 2^e and M private choices, every surviving cross-parity label right angle has the form F-V = λ(Sa, S²b), G-V = c(-Sb, a), with |a| > MS^4/16. So all such angles vanish once MS^4 >= 16(h-1), four times better than the 64h on file. The other cases: mixed even-component supports with mixed parity vanish under the same condition, odd-component ones once √M·S^4 >= 128√2·(h-1), and all-one-parity ones once S >= 16. Below these thresholds survivors exist, but no proof works at polylog S with bounded M. Arithmetic counts give polynomial per-label bounds. A barrier configuration shows locality plus divisibility alone allow about 2h/S^4 angles at one label, so these tools stop at S ~ h^{1/4}, width O(h^{9/4}). A census at S=8 shows few actual survivors, and local search clears them with M = 2 or 3.

## Statements

Setting. Hilbert ranks r_e on the padded q-square (recursion of continuation_hilbert_placement.md). Columns x_e = S(M r_e + xi_e), 0 <= xi_e < M, S = 2^e. Slot = M r + xi. Each label (i, j) has black points (x_e, 2i+1) and (x_e, 2j+2). K = S²/2.

LEMMA 0 (dyadic locality; PROVED). If two ranks differ by t >= 1 and one coordinate differs by |D| >= 2^m with m >= 1, then t > 4^(m-1). This is sharp in the sense used below. The bound D² < 16t on file gives only t > 4^(m-2) when |D| = 2^m.

THEOREM 1 (cross-parity label right angles; PROVED). Take S = 2^e >= 8 and any M >= 1 with any choices. Every tilted right angle among label points has a vertex V, an endpoint F of V's parity, and an endpoint G of the other parity. It can be written uniquely as
  F = V + λ(S a, S² b),  G = V + c(-S b, a),
with λ >= 1, a and c odd, b != 0, and gcd(a, b) = 1. Let t be the rank distance between the labels of V and F. Then:
 (i) |ac| <= h-1;
 (ii) t >= (S^4/16)·4^floor(log2(λ|b|)) + 1, and λ|a| >= M(t-1)+1;
 (iii) hence |a| > (MS^4/16)·4^floor(log2(λ|b|))/λ >= MS^4/16, and |a| > (MS^4/64)λb²;
 (iv) consequently no such angle exists when M S^4 >= 16(h-1);
 (v) near-far structure: G lies within |x2| = |bc| < 64(h-1)/(M S^4 λ|b|) slots of V, while F lies λ|a| > MS^4/16 slots away;
 (vi) the two-label case (F and G in one column) has a | c and |G_y - V_y| >= a². It is excluded when M²S^8 >= 256(h-1).
Same-parity angles (S >= 8) and angles whose two endpoints both have the opposite parity (parity argument) are impossible, as in Theorem 2 of the placement note.

THEOREM 2 (nonvertical mixed four-supports; PROVED). Black side A,B with X = B_x - A_x != 0, and black diagonal C,D.
 (a) Even vertical components, all four points of one parity: impossible for S >= 16 at any h. The proof on file needs S² >= 2(64/S)², so S = 8 is not covered.
 (b) Even components with AB and CD of different parities. Then R2 is axis-aligned and the data parametrize as X = S g a, Y = S² g b, Z0 = -S b c, c_row - b_row = a c, with a and c odd and gcd(a, b) = 1. Here |a| > MS^4/16, so these vanish when MS^4 >= 16(h-1). The near pairs are (A,C) and (B,D) at slot distance < 64(h-1)/(MS^4).
 (c) Odd vertical component, with C - A = (m,p) and D - B = (n,q). Equivalently C = A + T - E and D = B + T + E with T ⊥ U and E ⊥ (E+U), where E ∉ {0, -U}. For m, n of the same sign, |Y| > √M·S^4/(64√2), and the side AB is a near pair: |X|/S < 64√2·h/(√M·S^4). For opposite signs, |Y| > √M·S^4/(128√2). All vanish when √M·S^4 >= 128√2·(h-1).
 The vertical case is exactly the P-rival family, as on file.
COROLLARY. With M = 1, take S = the least power of two >= max{32, (182(h-1))^{1/4}}. This S excludes all label-only tilted right angles and all nonvertical label mixed supports, in width < S·q² = O(h^{9/4}). The constant improves on (1024h)^{1/4}. Because width scales with SM while the thresholds scale with S^4·M or S^4·√M, M = 1 is optimal for these thresholds.

PROPOSITION 3 (arithmetic incidence counts; PROVED). Let N_V(e), N_G(e) and N_F(e) count candidate right-angle events (all choice vectors) in which label e is the vertex, the near endpoint and the far endpoint. Put W = floor(64(h-1)/(MS^4)). Then
  N_V(e), N_G(e) <= 256(h-1)(1 + ln W)/S^4,   N_F(e) <= 384(h-1)²/S^4,
and all are 0 when MS^4 >= 16(h-1). Family (b) obeys the same bounds. For family (c), the count of (T, E) per side is <= (2h/|X'| + 1)·4τ(X²+Y²), with X' = X/gcd(X,Y). These counts are polynomial in h for MS^4 << h.

PROPOSITION 4 (barrier; PROVED). Take S >= 8, M = 1 and h >= S^4. There is a configuration of floor(2h/S^4) + 2 labels, given by prescribed ranks and coordinates, in which every pair satisfies the dyadic locality of Lemma 0. One label of it is the vertex of at least floor(2h/S^4) distinct in-strip tilted right angles. So no argument that uses only locality among the constraint's own points, column divisibility and arithmetic counts can bound the per-label incidence by o(h/S^4).

LEMMA 5 (local lemma for private choices; PROVED). Let the events be any family of label-only constraints, each a label set J with 2 <= |J| <= 4 and a forbidden choice vector, and let M >= 2. For each label z put mu_z = sum over events containing z of M^-|J|. If mu_z <= 1/16 for every z, then some choice avoids all events.

NOT PROVED: any exclusion at S = O(1) or S = (log h)^c with bounded M. Conjecture, heuristic only: the expected right-angle incidence per label is about C·log²(16h/(MS^4))/(M²S²). With a max-equals-mean hypothesis, Lemma 5 would then give S ~ log h with M = 2, or S fixed with M ~ log h, that is width h² log h for this part.

## Proofs

LEMMA 0. Let 4^k be the least power of 4 that is >= t. As in the placement note, the two ranks lie in one aligned block of length 4^k or in two consecutive ones. These are one square of side 2^k or two edge-adjacent squares, so every coordinate difference is <= 2^(k+1) - 1. If |D| >= 2^m, then 2^m < 2^(k+1), so m <= k. When k >= 1, 4^(k-1) < t by minimality, so t > 4^(k-1) >= 4^(m-1). If k = 0, then t = 1 and |D| <= 1, which contradicts m >= 1.

THEOREM 1. First the parity cases. A same-parity segment has (Δy)² < 64t <= 64|Δx|/S, because the slot distance is >= t. With |Δx| >= S, its slope is < 8/S <= 1, so two such segments cannot be perpendicular. If both endpoints have parity opposite to the vertex, then X1X2 is even and Y1Y2 is odd, so the dot product is odd. V and F cannot share a column, because they would be the same point. If G shares V's column, then Y1 = 0 and the angle is axis-aligned. So the leg (X1,Y1) = F - V has the same parity and the leg (X2,Y2) = G - V has the opposite parity, with Y2 odd and X1, X2, Y1 nonzero.
Write X1 = S x1 and X2 = S x2. Orthogonality gives S² x1 x2 = -Y1 Y2. Since S is a power of two and Y2 is odd, S² divides Y1. Write Y1 = S² y1, so x1 x2 = -y1 Y2. Let λ = gcd(x1, y1) > 0, x1 = λa and y1 = λb, with gcd(a,b) = 1. Then a x2 = -b Y2, so a | Y2. Write Y2 = ac; then x2 = -bc. Y2 odd forces a and c odd. This gives the stated form, and uniqueness follows because λ, a, b, c are recovered from F - V and Y2.
(i) holds because both rows lie in [1,h].
(ii) The coordinate difference of V and F is D = Y1/2 = 2^(2e-1) λ b. So |D| >= 2^m with m = 2e - 1 + floor(log2(λ|b|)). Lemma 0 gives t > 4^(m-1) = (S^4/16)·4^floor(log2(λ|b|)). The slot difference is x1 = M(r_f - r_v) + (xi_f - xi_v), so |x1| = λ|a| >= Mt - (M-1).
(iii) Combine (ii) with t - 1 >= (S^4/16)·4^floor(log2 n), where n = λ|b|. For λ in [2^j, 2^(j+1)), 4^floor(log2 n) >= 4^j >= λ, so |a| > MS^4/16. Also 4^floor(log2 n) > n²/4, so |a| > (MS^4/64)λb².
(iv) |G_y - V_y| = |ac| >= |a| > MS^4/16 >= h - 1 is a contradiction.
(v) |x2| = |b||c| <= |b|(h-1)/|a| < 64(h-1)/(MS^4 λ|b|).
(vi) Here x1 = x2, so λa = -bc. gcd(a,b) = 1 gives a | c, so |ac| >= a² > (MS^4/16)².

THEOREM 2. Write α = 64/S. Every same-parity pair satisfies (Δy)² < 64t <= α|Δx| for any M, since the slot distance is >= t.
(a) This is the argument on file, which needs S² > 2α², that is S^4 > 8192. That holds for S >= 16.
(b) Even case: equal norms and |X²-Z²| >= S(X+Z) > α·max(X,Z) > |Y² - W²| (using S >= α) force X = Z and W = -Y. Then XZ0 + Y(c-b) = 0, as on file. Put X = Sx and Z0 = Sz. If z = 0, then Y(c-b) = 0, which is impossible because Y != 0 and c - b is odd. So S²xz = -Y(c-b) with c - b odd, which gives S² | Y. The factorization is the same as in Theorem 1: x = ga, y = gb, c - b = ac, z = -bc. Lemma 0 on the same-parity pair (A,B) with |Y/2| = 2^(2e-1)·g|b| gives t_AB > (S^4/16)·4^floor(log2(g|b|)). Then g|a| >= M(t_AB - 1) + 1, so |a| > MS^4/16 exactly as in (iii). Also |c - b| >= |a| and |c - b| <= h - 1. The slot bound on z follows as in (v).
(c) Odd case, with Y odd and p, q even. As on file, S² | p+q != 0 and m + n != 0. Write u = |m|/S and w = |n|/S for slot distances. Then t <= u gives p² < 64u and q² < 64w. Because max(|p|,|q|) >= S²/2, Lemma 0 with |D| >= 2^(2e-2) gives t > S^4/64 for that pair, so u + w >= M·S^4/64 + 1.
 Same sign: |Y| = |X||m+n|/|p+q| >= S²(u+w)/(8(√u + √w)) >= S²√(u+w)/(8√2) > √M·S^4/(64√2). Also |X| = |Y||p+q|/(S(u+w)) < 8√2·h/(S√(u+w)), which gives the near-pair bound.
 Opposite signs: identity (12) on file, |Y| = ((n-m)² + (q-p)²)|m+n| / (4|mq-np|), with |m+n| >= S, |n-m| = S(u+w), and |mq - np| < 8S√(uw)(√u + √w). Using √(uw) <= (u+w)/2 and √u + √w <= √(2(u+w)), this gives |Y| > S²√(u+w)/(16√2) > √M·S^4/(128√2).
 The T/E form: C + D = A + B + 2T, and |D - C|² = |U + 2E|² = |U|² is equivalent to E·(E+U) = 0. The excluded values E = 0 and E = -U give D - C = ±U.
 The corollary follows by combining (iv), (a), (b) and (c) at M = 1, with 128√2 < 182.

PROPOSITION 3. Vertex role: an event is fixed by (xi_v, x2, λ ≠ 0). G is the owner of slot σ_v + x2, which fixes Y2, γ = gcd(Y2, x2), a = Y2/γ and b = -x2/γ. By (iii), |λ| < 64|a|/(MS^4 b²) <= 64(h-1)γ/(MS^4 x2²), and by (v), |x2| <= W. Then Σ_x2 γ/x2² <= Σ_{|x2|<=W} 1/|x2| <= 2(1 + ln W). With M values of xi_v, this gives N_V <= 256(h-1)(1 + ln W)/S^4. The near role is symmetric, with V at slot σ_g - x2.
Far role: an event is fixed by (xi_f, λ, a). V is the owner of slot σ_f - λa. The coordinate difference of V and F then fixes b, and c ranges over at most 3(h-1)/|a| odd values. With |λ| < 64|a|/(MS^4) and at most h - 1 odd a with |a| < h, N_F <= M·Σ_a (128|a|/(MS^4))·3(h-1)/|a| <= 384(h-1)²/S^4.
Family (c): for a fixed side, T = k(-Y, X)/gcd(X,Y) with |k|·|X'| <= 2h. E is a lattice point on the circle |2E + U| = |U|, and there are at most r_2(|U|²) <= 4τ(|U|²) of them.

PROPOSITION 4. Put K = S²/2. Choose an odd a with h/4 <= a <= h/2 and set Λ = floor(8a/S^4) >= floor(2h/S^4).
 Label v: rank 0, coordinates (i0, j0) with i0 = ΛK and j0 = i0 + (a-1)/2.
 Label g: rank 1, coordinates (i0 + 1, j0).
 Labels f_λ, λ = 1..Λ: rank λa, coordinates (i0 - λK, j0).
 Check: V = (0, 2i0+1), G = (S, 2j0+2) = V + (S, a), and F_λ = V + λ(Sa, -S²). Then (F_λ - V)·(G - V) = λ(S²a - S²a) = 0. The row of F_λ is >= 1, and the rows of G and of W_λ = F_λ + G - V are <= ΛS² + 1 + a <= h/16 + 1 + h/2 <= h.
 Locality: every j-difference is 0. The i-differences are λK at rank distance λa, |λ - μ|K at rank distance |λ - μ|a, λK + 1 at rank distance λa - 1, and 1 at rank distance 1. Each satisfies |D| < 2√t, which implies |D| <= 2^(k+1) - 1. For example, λK² <= 2a gives λK <= √(2λa), and √(2λa) + 1 < 2√(λa - 1) once λa > 10.
 So the dyadic locality holds for every pair, and v is the vertex of Λ tilted in-strip right angles. Here M = 1, so slots equal ranks.

LEMMA 5. Choose the xi_z independently and uniformly. Events whose label sets are disjoint are mutually independent, so the dependency graph joins two events when their label sets meet. Put x_A = 2P(A) = 2M^-|J_A|, which is <= 1/2. Then Σ_{B~A} x_B <= Σ_{z ∈ J_A} 2mu_z <= 8/16 = 1/2, so Π_{B~A}(1 - x_B) >= 1 - Σ x_B >= 1/2 and x_A Π_{B~A}(1 - x_B) >= P(A). The asymmetric local lemma then gives positive probability that no event occurs.

CHECKS (sanity only). The scripts are in the script folder below. The exact enumerator built on the Theorem 1 parametrization matches a brute-force direction-hash search on every cross-parity angle: 549/549 (h=32, S=2), 49/49 (h=32, S=2, M=2), 23/23 (h=40, S=2, M=3) and 23/23 (h=64, S=4). Census at S = 8:
 - Actual angles, M = 1: 0 at h=128 and 256; 84 at h=512 (max incidence 2); 4179 at h=1024 (mean 0.048, max 5); 53398 at h=2048 (mean 0.153, max 8).
 - Actual angles, M = 2: 0 at h=512, 47 at h=1024, 2131 at h=2048. M = 4 at h=2048: 30.
 These zeros match (iv) exactly: none whenever MS^4 >= 16(h-1). The smallest observed ratio |a|/(MS^4/16) is 1.34. At h=2048 and M=1, 95% of angles have x2 = 1, 98% have |b| = 1, and λ <= 5. These are the near-far structure of (v).
 - Highest-incidence labels are in the far role. Each one is shared by about 7 vertices clustered at rank offset about ±K² = ±S^4/4 from it, a block-alignment effect.
 - Candidate events with all choices at h=2048: M=2: 34983 events, max 10 per label, max mu = 1.25. M=3: max mu = 0.41. M=4: max mu = 0.20. All exceed the 1/16 of Lemma 5.
 - Rank-order greedy fails (41 and 27 unresolved labels for M = 2 and 3). Local search reaches 0 violations in 177 and 47 steps.
 - The mixed brute force (validated on the Holder collision) finds no nonvertical mixed supports in the actual placement for S=4 (h <= 32) or S=8 (h <= 48). At S=2 it finds 28 and 62, all within the Theorem 2 bounds.
Scripts: scripts_hb1_angles_mixed/angles.py, .../cand.py, .../greedy.py, .../shape.py, .../maxlab.py, .../mixed_brute.py and .../mtest.py, all in the same folder.

## External results used

- Asymmetric Lovász local lemma: suppose events A_i have a dependency graph in which each A_i is mutually independent of its non-neighbours, and there are x_i in [0,1) with P(A_i) <= x_i·Π_{j~i}(1 - x_j). Then with positive probability no A_i occurs. This is standard, and I did not look it up.
- Weierstrass product inequality: Π(1 - x_j) >= 1 - Σ x_j for x_j in [0,1].
- r_2(n) <= 4τ(n), the number of representations as a sum of two squares.

## Checks

Exact enumerator for cross-parity angles against brute force: all four test sizes match exactly, including choices M = 2 and 3. Threshold (iv) matches every zero in the census at S = 8: h = 256 with M = 1, h = 512 with M = 2, and h = 1024 with M = 3 (candidates included). The observed minimum of |a|/(MS^4/16) is 1.34 > 1. The mixed brute force reproduces the Holder collision. At S = 2, every mixed support found satisfies the Theorem 2 bounds, with minimum ratios 56.6, 79.2 and 7.0 for the same-sign, opposite-sign and mixed-parity even cases. All scripts ran under 60 seconds and 1 GB, using numpy and the Hilbert recursion of the placement note.

## Gaps

- No exclusion of cross-parity right angles or mixed supports at S = O(1) or S = (log h)^c with bounded M is proved. The only proved exclusions are the thresholds MS^4 >= 16(h-1), √M·S^4 >= 128√2·(h-1) and S >= 16, which force S ~ h^{1/4}.
- Arithmetic counts give only polynomial per-label bounds (N_V, N_G <= 256(h-1)(1+ln W)/S^4 and N_F <= 384(h-1)²/S^4). Combined with Lemma 5, they need M³S^4 >> h², which gives no width gain over the threshold theorem.
- Proposition 4 shows the missing input is a property of the actual Hilbert order that goes beyond pairwise dyadic locality. One example is anti-concentration of the i-coordinate along rank progressions r_v + λa, uniformly in v. I have no proof of any such property.
- The heuristic incidence C·log²(16h/(MS^4))/(M²S²) for right angles uses a random-coordinate model. Its fitted constant ranges from 0.8 to 2.3 in the census. The census also shows max/mean ratios near 100, driven by far-role hubs at rank offset ±S^4/4. So a max-equals-mean hypothesis is doubtful at small h.
- For family (c), only inequality thresholds and a crude count are given. I have not computed the heuristic incidence. The census of the actual placement covers only S <= 8 and h <= 48, which is too small to be informative.
- For S = 8, the all-one-parity even-component mixed case is not excluded. The z = -1 configurations are not ruled out by the inequalities. The full placement needs S >= 32 anyway.
- Parked corners are not used. With M >= 2, a right angle whose fourth corner falls in an empty sea column with the right filler parity is allowed by (V2). The count above treats every in-strip angle as forbidden, so it overcounts. This needs the filler design of gap 3.
- Interaction with the P family (gap 1) and with sea or filler supports (gap 3) is not addressed. Lemma 5 would have to absorb every family at once, with sum of mu_z <= 1/16.
- The period-seven profile version, with v2(S) = 5 and row step 14, was only sketched. It follows the same steps, with a right-angle threshold around |Y2| > 1.1·10^7 at M = 1. It is not written in full.

## Missing estimate

The missing bound is a uniform per-label estimate. For every label z, the expected number mu_z of right-angle and mixed events containing z, over uniform private choices, must be at most 1/16, with S = (log h)^c and M bounded, or with S constant and M = O(log h). The vertex role needs a Hilbert anti-concentration statement of roughly this form. For every label v, every odd a with MS^4/16 < |a| < h and every b, the number of λ <= 64|a|/(MS^4b²) for which the label at slot σ_v + λa has coordinate difference exactly λKb from v must be o(1) on average over the M² choice pairs. The far role needs the same statement summed over the vertices clustered near rank offset ±S^4/4, where the census shows hubs. Proposition 4 shows this cannot follow from locality alone.

## Next steps

- Test the hub structure: rerun the census at fixed S = 8 for M = 1 and 2 at h = 4096 with an iterative numpy Hilbert map, and check whether the maximum far-role incidence grows like h/S^4 (as in the barrier) or like a power of log h. The h=2048 data show max 8 to 13, roughly doubling per doubling of h.
- Prove a block-alignment lemma for the far role. Hubs occur at rank offset ~ ±K² with Δi = ±K, which forces equal orientation of the two K-blocks. Bound the number of vertices sharing one far label by the number of v in a rank window of length O(h/S^4) whose local i-coordinate matches f's, which is probably O(√(h/S^4)).
- Try a choice rule that breaks block alignment: choose xi_e from the orientation of the label's K-block, so that slot offsets ~ MK² never pair equal-orientation blocks. The orientation-only obstruction note does not rule out combining this with the M-slot shift.
- Use parked corners with M >= 2: leave the fourth-corner column of each dominant near-far angle empty and give it the right filler parity. This turns the constraint into a sea-design condition, and it must be checked against V3.
- Compute the heuristic and actual incidence for the odd-component mixed case at S = 8 and 16 with a T/E enumerator (sides with |Y| > √M·S^4/(128√2), lattice points E on the Thales circle), to see whether its order is below that of right angles.
- Once any family has a per-label bound, combine it additively in Lemma 5 with the P-family bounds of continuation_hilbert_local_factor_budget.md, which needs the sum of mu_z <= 1/16 over all families.

