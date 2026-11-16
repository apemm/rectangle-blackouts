# Synthesis: what the Hilbert route gives now

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: no new full board; the best proved bound is still the menu bound (log h)^(1.3108172 + eps). Unconditional: a label scaffold (no sea) of width h^(57/23 + o(1)) and a 2-adic sea lemma (U3). Conditional: an O(h^2) reduction to six families under the H7 reduction; with uniform strides a degeneracy proof heuristically needs S M of order (log h)^2, which gains nothing; a multilevel diagonal tiling would give width O(h^2 log h), exponent 1, conditional on audits of the H7 inputs and a per-tile degeneracy hypothesis (G). Seven open steps are listed in order of value. Not audited yet.

# Result

## Status

partial

## Summary

No new full board. The route gives one new unconditional label scaffold, of width h^(57/23+o(1)). It also gives a conditional O(h^2) reduction to six families. Three conflicts between the routes are resolved. (a) The mod-4 rows of design H7 kill the skeptic's F1 family outright, so that obstruction does not bind. (b) p_count's Hypothesis H cannot hold uniformly in h, because labels with |b-a| near h^(2/3) have P degree about (log h)^2/S, against log h/S on average. (c) So with uniform strides, a degeneracy proof heuristically needs SM of order (log h)^2, that is b = 2, which gains nothing. A multilevel diagonal tiling would bring this down to b = 1 (width h^2 log h), conditional on named steps.

## Statements

Notation. Full-grid placement: x_e = S(M r_e + xi_e), with S = 2^e and labels in an n-square, n <= h, so width <= S M h^2. H7 placement (sea route): 196 residue blocks mod 28, S = 6272 sigma, width 6272 sigma M (h+28)^2 + O(h^2).

(i) UNCONDITIONAL

U0 (unchanged). There is no new full board. The best proved bound is still the menu bound m_h <= C_eps h^2 (log h)^(1.3108172+eps).

U1 (on file, audited). Fix S >= 32. The same-parity exclusion holds for every M and every choice. Choosing M by (14) of the local factor budget note excludes the whole P family. That M is ceil(64 D_h + (4096 D_h^2 (h-1)/S)^(1/3)) + 1 = (h/S)^(1/3) h^(o(1)), so at fixed S the width is h^(7/3+o(1)).

U2 (new combination; scaffold, not a board). Take M from (14), and S the least power of two that is at least 32 and satisfies both M S^4 >= 16(h-1) and sqrt(M) S^4 >= 128 sqrt(2) (h-1). Then the full-grid label set has none of the following: same-parity integral distances, P constraints (all of them, by increasing-rank greedy), tilted label right angles (angles_mixed Theorem 1), or nonvertical label mixed four-supports (angles_mixed Theorem 2 (a)-(c)). This holds at S = h^(5/23+o(1)), M = h^(6/23+o(1)), and width h^(57/23+o(1)), about h^2.478. The angle and mixed exclusions hold for every choice vector, so the greedy for P is unaffected. The exponent is the optimum of the linear program min s+m subject to m >= (1-s)/3, m + 4s >= 1 and m/2 + 4s >= 1, attained at s = 5/23, m = 6/23. The first constraint is slack against the third. Without the mixed constraint the optimum would be 5/11 at s = 2/11, and taking M = 1 with S ~ h^(1/4) gives 1/2. This scaffold has no sea, and its exponent is far above the menu, so its value is low.

U3 (new, elementary; 2-adic sea lemma). Suppose a block has its odd label rows all congruent to alpha (mod 4), its even label rows all congruent to beta (mod 4), and its core sea rows satisfying L ≡ F ≡ alpha+2 and H ≡ beta+2 (mod 4). Suppose also that every label and slot column is congruent mod 4 (4 | S). Then no two label points V, Q of opposite row parity form a right angle, at any vertex, with any point E in a core sea row (any column, hole or slot column included). This also holds when V and Q are the two points of one label. The H7 design (d = 28, Lemma AP4 congruences) meets these hypotheses. So the skeptic's F1 family, and every configuration of two opposite-parity label points plus one sea point, is empty in H7 for every M and every choice. The existence of the aligned profiles is Lemma AP4, which is unaudited.

U4 (re-verified, from angles_mixed). Lemma 0 holds: |Delta coordinate| >= 2^m forces rank distance t > 4^(m-1). So does Theorem 1: every cross-parity label right angle has |a| > M S^4/16 with |ac| <= h-1, and none exists once M S^4 >= 16(h-1). Theorem 2 and Propositions 3-4 were not re-derived.

(ii) CONDITIONAL FULL-BOARD WIDTHS

C1 (O(h^2) reduction). Assume (A) the H7 reduction: Lemma AP4, N1 with a Hilbert core, and Lemmas S1-S6 with Theorem H7, all audited. Assume (B) that at sigma = 1 and some constant M, every block has a choice vector avoiding (P), (Lambda3), (Lambda4), (R2s), (FW) and (6PT). Then m_h <= 6272 M (h+28)^2 + C h^2 = O(h^2).

C2 (degeneracy form). Assume (A). Let K(sigma, h) bound the weighted hyper-degeneracy of the union of all six families' candidate events. Each event is charged to a label that occurs in it as a placed point, never only through an "unused slot = F" role. Then M = K+1 works, and the width is 6272 sigma (K+1)(h+28)^2 + O(h^2). The heuristic incidences give K ≍ (log h)^2/sigma, coming from P in the near-diagonal band (see the proof field). So this route gives at best sigma M ≍ (log h)^2, that is b = 2. That is worse than the menu: with uniform strides, counting arguments cannot beat 1.3108.

C3 (p_count's H). If D_{S,M}(h) <= c0 + c1 mu_hat held uniformly, it would give width h^2 log h. That hypothesis is inconsistent with the band heuristic, so I discard it as a target.

C4 (multilevel diagonal tiling; best conditional, b = 1). In each residue block of side n_b, put level k = 0..K-1 with K = ceil(log2 log h). Level k holds the labels with n_b 2^(-k-1) <= |j-i| < n_b 2^(-k), placed in the 3*2^k aligned squares of side n_b 2^(-k) on and next to the main diagonal. The final level K holds the labels with |j-i| < n_b/log h. Each square is its own Hilbert core in its own window, with constant stride S_k = 6272 * 2^ceil(log2(k+1)) * sigma0 and S_K of order sigma0 log h. Every audited per-core theorem applies to each tile unchanged: square, constant power-of-two-times-6272 stride, subsets with the original ranks. Assume (A), and assume (G) that each tile's weighted hyper-degeneracy is at most c0 + c1 (k+1) log h / S_k, and at the final level at most c0 + c1 (log h)^2/S_K. Then sigma0 = C log h with M = c0 + 2 gives a valid board of width O(h^2 log h). The core width sums to at most about 30 * 6272 sigma0 M (h+28)^2. The roughly 1200 log h windows add at most about 600 h^2 log h columns of gaps (2W_h + 1 <= h^2/2 + 3), plus O(h^2) collars per window. Hypothesis (G) matches the heuristic for P. It is unknown for R2s, FW and 6PT.

(iii) OPEN STEPS, in order of value

1. Audit the H7 inputs: AP4 (rerun verify_filled_mod7_profiles with the mod-28 and mod-4 conditions), N1 with the Hilbert core, S1-S6, and U3. Every board statement rests on these.
2. Run a census of the actual H7 block systems (S = 6272, row step 28) for P and R2s. All P data so far are for the full-grid S = 32 placement, which is not a board design.
3. Prove (G) for P. The missing input is an equidistribution lemma for Hilbert partner offsets (p_rule), used through the induced-average criterion (8), not max degree, because divisor-rich offsets make the max degree large. With step 1, this gives b = 1.
4. Find the heuristic incidence and band behaviour of R2s. It could bind like P.
5. Prove an anti-concentration lemma for Lambda3/Lambda4 (angles_mixed missing estimate). Heuristically these are cheap at S >= 6272.
6. Get per-label bounds for FW and 6PT over all occupancy states.
7. For O(h^2): a structural bounded-M theorem for P. The mean degree grows like log h/S, so no counting argument can reach it.

## Proofs

1. Widths. Full grid: rows 2i+1, 2j+2 <= h give i, j < h/2. Padding to a power of two n <= h gives ranks < n^2 <= h^2, so the width is < S M h^2. H7: each block has Q <= 2(h/28+1), so Q^2 <= 4(h+28)^2/784. Over 196 blocks the total rank space is <= (h+28)^2, which matches the sea route's 6272 sigma M (h+28)^2. The same-parity condition at d = 28 is (28 Delta)^2 < 784 * 16 t <= 2 S t, which holds since S >= 6272 = 8 * 28^2.

2. U2. From (13)-(14) of the local factor budget note, with Q = (h-1)/S: the earlier-constraint count is <= 16 D_h sqrt(Q/M) + 18 D_h < M. So M ≍ D_h^(2/3) (h/S)^(1/3), with D_h = h^(o(1)). angles_mixed Theorem 1(iv) needs M S^4 >= 16(h-1). Theorem 2(b) needs the same, 2(c) needs sqrt(M) S^4 >= 128 sqrt(2)(h-1), and 2(a) needs S >= 16. Put S = h^s and M = h^m. The binding pair is m = (1-s)/3 and m/2 + 4s = 1, which give 23 s = 5, so s = 5/23 and m = 6/23. Check: m + 4s = 26/23 >= 1. The total is s + m = 11/23, so the width is h^(2+11/23+o(1)) = h^(57/23+o(1)). Rounding S up to a power of two costs a factor of 2. The exclusions in Theorems 1 and 2 hold for every choice vector, so they are compatible with the greedy for P.

3. Re-verification of Theorem 1. G - V = (X2, Y2) has Y2 odd and S | X2. Write it as g times a primitive vector. Then g is odd, so S divides the primitive x-part: G - V = c(-S b, a) with a and c odd. Perpendicularity makes F - V a multiple of (a, S b). S | x_F - x_V and a odd force the multiplier to be a multiple of S, so F - V = lambda(S a, S^2 b). The vertical part lambda S^2 |b| equals 2|Delta| for a label coordinate Delta. Lemma 0 then gives t > 4^floor(log2(lambda|b|)) S^4/16. Lemma 0 itself holds because a coordinate gap >= 2^m means the block indices at side 2^(m-1) differ by >= 2. A Hilbert segment between the two points then contains a whole block of 4^(m-1) cells. The horizontal part gives lambda|a| >= M(t-1)+1. And 4^floor(log2 x) >= lambda for x = lambda|b| >= lambda: check lambda = 1, 2, 3 directly, and for lambda >= 4 use (lambda/2)^2 >= lambda. So |a| > M S^4/16, and |a| <= |ac| <= h-1. The same calculation in a profile with row step d gives v2(Delta) >= 2e - v2(d), hence |Y2| >= S^2 M 4^(e-1)/(16 d). At d = 28 and S = 6272 sigma this is about 3.6e8 sigma^4 M, which reproduces the sea route's Lambda3 threshold. The angles_mixed d = 14 figure (1.1e7) belongs to the other design, so there is no conflict.

4. U3, the 2-adic sea lemma. Take V on odd row y_V ≡ alpha and Q on even row y_Q ≡ beta, so Y = y_Q - y_V is odd. Take E = (x_E, s) with s in {L, F, H}, and X = x_Q - x_V with 4 | X.
- Right angle at V: (x_E - x_V) X + (s - y_V) Y = 0. This forces 4 | (s - y_V). But s - y_V ≡ 2 (mod 4) for s in {L, F}, and is odd for s = H.
- Right angle at Q: the same argument with the roles swapped.
- Right angle at E: put A = x_V - x_E. Then A(A+X) = -(y_V - s)(y_Q - s). One factor on the right is ≡ 2 (mod 4) and the other is odd, so the right side is ≡ 2 (mod 4). The left side is ≡ A^2, which is 0 or 1 (mod 4). Contradiction.
- X = 0 (one label's own pair) is covered by the same lines.
H7 has 4 | 28, so the block rows are constant mod 4, and it has 4 | S.

This voids the skeptic's (C)/(C') obstruction for H7. That obstruction needs s ≡ y_V (mod 2^(v2(S))), which is achievable at d = 14: there 14i runs over all residues of one parity mod 32. At d = 28 it is impossible. The skeptic's result stands for the d = 14, S = 1568 filled_mod7 design.

5. Conflict between p_count's Hypothesis H and p_rule's Statement D, resolved in favour of D. Take the near-axis structure of Pythagorean pairs. Primitive pairs have density ~ c/L in the (X, Y) plane (from the Jacobian of z -> z^2), and none exist where Y^2 < 2X+1. Summing the multiples k <= min(X, Y, Y^2/2X) gives density ~ c log(min(X, Y, Y^2/2X))/L. Integrate over X <= h at fixed y = |2T+1| = h^u, with H = log h. This gives degree(y) ~ (c'/S)(u H)^2/2 for u <= 1/2, and (c'/S)(H - uH)(3uH - H)/2 for u >= 1/2. The maximum is H^2/6 at y = h^(2/3), against about H * O(1) for typical y ~ h. Partners stay within O(sqrt(h/(SM))) << h^(0.6) in T. So the band [h^0.6, h^0.7] induces a subgraph of average degree ~ 0.16 c' (log h)^2/S. Its degeneracy is at least half of that, which eventually exceeds c0 + c1 * 16 log h/(pi S). So H fails for large h under this heuristic; the data (mu <= 2.86) cannot tell the two forms apart.

Census and p_rule Theorem B do not conflict. Theorem B's h0(512) = 2*512^2 + 8*512 + 1 = 528385 is above the census range (h <= 16384), and H's own prediction at h = 528385 is 2 + 1.2 * 1.37 ~ 3.6 >= 3.

6. C4 width. S_k <= 2 sigma0 * 6272 (k+1). Level k occupies 3 * 2^k squares of rank size n_b^2 4^(-k), so 3 n_b^2 2^(-k) ranks. Summing gives sum_k 2(k+1) * 3 * 2^(-k) = 24, so the core width is <= 24 * 6272 sigma0 M n_b^2 per block, plus the final level's 3 n_b^2/log h ranks times S_K ~ sigma0 log h, so O(sigma0 M n_b^2). The heuristic degree at level k is ~ (c/S_k)(k log 2)(2H - 3k log 2)/2 <= c k H/S_k, which is bounded once sigma0 ~ H. Window count: sum_{k<=K} 3 * 2^k <= 6 log h per block. Here 2W_h + 1 <= h^2/2 + 3 is the audited fact from audit_consolidated_board_v4_steps.md.

7. Exponents. 7/3 ~ 2.333 and 57/23 ~ 2.478 are scaffolds. C2 heuristic: b = 2. C4 conditional: b = 1 < 1.3108172.

## Checks

I checked the following by hand: the width and constant bookkeeping (full grid and H7), the U2 linear program, Lemma 0 and Theorem 1 of angles_mixed, the reconstruction of the Lambda3 threshold in the profile, the U3 2-adic lemma (all three vertex cases), the scope of the skeptic's obstruction (d = 14 against d = 28), the consistency of Theorem B with the census and with H at h0 = 528385, and the C4 width sums.

I ran one script as a sanity check: scripts_hb1_synthesis/band_degree.py. It computes exact in-strip P candidate degrees of sampled labels by y-band. Each run took under 15 seconds. At S=16, M=3 the band-mean peaks are 2.9, 3.3 and 4.7 at h = 4096, 16384, 65536, while the y ~ h/2 band stays at 0.47 to 0.66. At S=32, h=16384 the peak is 1.32 against 0.20 to 0.48. These figures are evidence for a growing band excess, not a proof.

## Gaps

- No unconditional full board. U2 is a label-only scaffold with no sea, and its exponent (57/23) is far above the menu.
- Every board statement (C1, C2, C4) depends on the unaudited H7 inputs: Lemma AP4, N1 with a Hilbert core, Lemmas S1-S6 and Theorem H7. U3 kills F1 in H7 only if the AP4 profiles exist.
- The band heuristic (degree about (log h)^2/S near |b-a| = h^(2/3)) and its use against Hypothesis H assume equidistribution of Hilbert partner offsets (p_rule's H-EQ). They are not proved. My sanity runs support it qualitatively. At S=16 the sampled band-mean P degree is 2.9, 3.3 and 4.7 at h = 4096, 16384, 65536, against 0.47-0.66 for y near h/2. These runs use a standard Hilbert variant and 80-1000 sampled labels per band.
- Hypothesis (G) of C4 is unproved for every family. For R2s, FW and 6PT not even a heuristic incidence or band profile exists, so they could bind more tightly than P.
- C4 is a design proposal I have not written in full. I did not check the per-window costs: T1 profile, BL4 collars, and exceptional labels in roughly 1200 log h windows. I assumed they are O(h^2) each, as for the 196 blocks.
- I did not re-derive angles_mixed Theorem 2 or Propositions 3-5, or the sea route's thresholds other than Lambda3.
- Event charging in C2/C4 requires a placed-point label in each event. I did not check that every FW/6PT/R2s event has one.
- No P or R2s census exists for the H7 block systems (S=6272, row step 28). All P evidence is for the full-grid S=32 placement.
- O(h^2) needs a structural bounded-M theorem for P. Counting arguments cannot give it, because the mean degree grows like log h/S.

## Missing estimate

For b = 1 (C4): in every square tile of side l on or next to the diagonal, holding the labels with |j-i| in [l/2, l), the P and R2s candidate systems at stride S must have induced-average factor count, max over U of avg F^-_U, at most c0 + c1 (1 + log(n/l)) log h/S. Equivalently, an equidistribution bound for the rank-gap-d partner offsets j_{H(r+d)} - i_{H(r)} on the tile, strong enough to feed criterion (8). For O(h^2): a bounded-M solvability theorem for the P system whose mean degree grows like log h/S. This requires structure beyond degree counting, of the kind the factor-one theorem gives for one factor.

## Next steps

- Audit AP4 (rerun the profile verifier with the mod-28 and mod-4 conditions), N1 with the Hilbert core, S1-S6, and the U3 2-adic lemma.
- Build the H7 block P and R2s candidate systems at S=6272. Measure degeneracy by y-band, and check whether R2s has a band excess.
- Try to prove the Hilbert partner-offset equidistribution lemma on diagonal tiles, using the self-similar digit structure. Then feed it into criterion (8) to get (G) for P.
- Write out C4 in full: tile cores, window and collar costs, and the subset-rank convention. Confirm that the per-core theorems apply to each tile verbatim.
- Derive heuristic incidences for R2s, FW and 6PT, and the anti-concentration lemma for Lambda3/Lambda4.

