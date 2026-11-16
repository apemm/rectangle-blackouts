# R2s labels can be relocated at o(h^2) width

15 November 2026. Problem 001. Continues continuation_gap_mixing_audit.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: a block has at most C0 tau*(h)^2 h^(10/11) side-owner rows for R2s, so every label in any R2s pair (at most about 1e4 tau*(h)^2 h^(21/11) labels) can be moved to a Proposition partial window at o(h^2) width. Asymptotically the R2s family can be dropped from design H7. The per-pair bound M - 1 is not proved and no heavy pair was constructed, and the relocation is harmless only for astronomically large h, not at 1e11. Not audited yet.

# Result

## Status

partial

## Summary

R2s solution rows are o(h): a block has at most C0 tau*(h)^2 h^(10/11) side-owner rows. So every label in any R2s pair (at most about 1e4 tau*(h)^2 h^(21/11) labels) can be moved to a Proposition partial window at o(h^2) width. Asymptotically R2s can be dropped from H7. The per-pair bound M - 1 is not proved, and no heavy pair was constructed. The relocation is harmless only for astronomically large h, not at 1e11.

## Statements

SETTING. Design H7 with any sigma >= 1 and any M >= 1. Fix one block, one parity role rho and an offset delta in 28Z \ {0}. A solution is a tuple of integers (T, U, V, m) with T U = -m delta, V^2 - U^2 = N := delta(2m - delta) and 1 <= |m| <= h - 1, and X = (U + T - V)/2. By Theorem A and (E4) of hilbert_residual_families.md (audited), this is the same as a signed factorization a b = T^2 + delta^2 with a = 2(X - T), b = 2(U - X) and U = T + (a + b)/2. A solution is admissible for a sea s in {L, F, H} and a row y_hat = s - m if S | X, |X| >= S, |X| > sigma delta^2/2 (weak Hil), and the strip condition s + delta/2 in [1, h] holds. The sea-type tests are not needed. tau*(h) = max{tau(n) : n <= h^2}, as in the paper; this is exp((2 ln 2 + o(1)) ln h / lnln h).

FACT 0 (proved from audited inputs). Every R2s event between two labels of one H7 core gives an admissible solution with y_hat = row_rho(side owner).

LEMMA K (congruence; proved). Suppose T U = -m delta, a b = T^2 + delta^2 and 2U = 2T + a + b. Put g = gcd(T, delta) and delta' = |delta|/g, and let delta1(n) = prod p^ceil(e_p/2) be the least d with n | d^2. Then delta1(delta') divides both a + T and b + T.

LEMMA B1 (proved). For each delta with |delta| <= h/5, the number of solutions is at most (12 sqrt(h|delta|) + 2) tau*(h).

LEMMA B2 (proved). For each delta and each T0 >= |delta| with 9 T0^2 + delta^2 <= h^2, the number of solutions with |T| <= T0 is at most 4 tau*(h) tau(|delta|) (6 T0 |delta|^(-1/3) + 1).

THEOREM 1 (R2s rows are sparse; proved from Theorem B, which is audited). Let C(h) be the number of admissible solutions (y_hat, s, delta, X) of one block and one role, over all seas, offsets and rows. Then for every eps > 0, C(h) <= C_eps h^(10/11 + eps). Explicitly, C(h) <= C0 tau*(h)^2 h^(10/11) with an absolute C0, about 22 once h >= 1e17 (hand count). So the set Y_rho of side-owner rows of admissible solutions has |Y_rho| <= C(h). This is o(h) rows, out of about h/28 per residue class.

COROLLARY 2 (conditional; relocation). Assume (Rel): a set of n labels taken out of the H7 cores can be placed in one Proposition partial window (paper, prop:partial, cases (a) or (c)), glued to the H7 board by J5 with the global switch z, at width c0 (n + 4) tau*(h)^2 + O(h^2). This is how the v4 board places WP windows (audited in audit_consolidated_board_v4_steps.md). Let Rel be the set of labels e with a_e in Y_odd or b_e in Y_even, over all 196 blocks. Then:
 (a) |Rel| <= 2 * 196 * C(h)(h/2 + 1) <= 1e4 tau*(h)^2 h^(21/11).
 (b) After Rel is moved, no pair of labels left in any core carries an R2s constraint. So the per-pair R2s multiplicity is 0 <= M - 1 for every M and sigma.
 (c) The added width is at most 1e4 c0 tau*(h)^4 h^(21/11) + O(h^2) = O(h^2). Hence the conditional width of the H7 Corollary holds with (R2s) removed from the list of families that must be avoided: if every block has a choice vector for its remaining labels that avoids (P), (Lambda3), (Lambda4), (FW) and (6PT), then m_h <= 6272 sigma M (h + 28)^2 + O(h^2).

NOT PROVED. (i) Any per-pair bound M - 1 on distinct R2s constraints in the original board. No heavy pair was constructed either. (ii) Harmlessness at practical heights. The bound in (c) is below h^2 only when tau*(h)^4 is below about h^(1/11), and that needs lnln h > about 30, which is astronomically large h. At h about 1e11, tau*(h)^2 is about 1e11 by my estimate, so moving even a few rows of labels costs more than h^2.

## Proofs

CONVENTIONS. Inputs are Theorem A with its identities (E1) to (E7) and the (a, b) form, and Theorem B (regimes and displacement caps), both from hilbert_residual_families.md and both audited in audit_hilbert_tiling_and_residuals.md ('correct with fixable gaps'; none of the gaps concern the steps used here). Hilbert locality and the (Hil) tool of H7 are also audited. Every R2s solution has delta != 0, T != 0 and U != 0 (Theorem A, 'Nonvanishing', with delta != 0 as fixed in the audit).

FACT 0. Let e (the side owner, point A) and f (point C) be labels of one core with the same role rho, and put X = x_f - x_e. Distinct labels have distinct ranks, and |xi_f - xi_e| <= M - 1, so |X| >= S(M(dr - 1) + 1) >= S dr >= S. Hilbert locality gives Delta^2 < 16 dr, where delta = 28 Delta, so delta^2 < 12544 dr <= 12544|X|/S = 2|X|/sigma. S | X holds because label columns are x0 + S(M r + xi). The strip condition is part of the definition of an R2s support (V4). Theorem A turns the support into a solution with m = s - row_rho(e). So y_hat = row_rho(e) lies in Y_rho.

LEMMA K. g divides T and delta. Write T = g T' and |delta| = g delta' with gcd(T', delta') = 1. delta | T U gives delta' | T' U, so delta' | U.
- (a + T)(b + T) = ab + T(a + b) + T^2 = T^2 + delta^2 + T(2U - 2T) + T^2 = delta^2 + 2TU. This is 0 mod delta', because delta' | delta and delta' | U.
- (a + T) + (b + T) = 2U, which is 0 mod delta'.
- So a + T = -(b + T) mod delta', and (a + T)(b + T) = -(b + T)^2 = 0 mod delta'. Hence delta' | (b + T)^2, so delta1(delta') | b + T. The same holds for a. ∎

LEMMA B1. |T||U| = |m delta| <= h|delta|, so |T| <= R or |U| <= R, where R = floor(sqrt(h|delta|)).
- Case |T| <= R. The pair (T, a), with a a signed divisor of T^2 + delta^2, determines the solution: b = (T^2 + delta^2)/a, U = T + (a + b)/2, m = -TU/delta, X = T + a/2 and V = U + T - 2X. Here T^2 + delta^2 <= h|delta| + delta^2 <= h^2. That gives at most 2R * 2 tau*(h) solutions.
- Case |U| <= R. From 2m delta = N + delta^2 = V^2 - U^2 + delta^2 and TU = -m delta, we get 2TU = U^2 - V^2 - delta^2, so U | V^2 + delta^2. Also V^2 = U^2 + N <= h|delta| + |delta|(2h + |delta|) <= 4h|delta|, so |V| <= 2 sqrt(h|delta|). The pair (V, U) determines N, then m, then T and X. Since V^2 + delta^2 <= 5h|delta| <= h^2, that gives at most (4 sqrt(h|delta|) + 1) * 2 tau*(h) solutions.
- The sum is at most (12 sqrt(h|delta|) + 2) tau*(h). ∎

LEMMA B2. Sort the solutions by g = gcd(T, delta), a divisor of |delta|, and put delta1 = delta1(|delta|/g). There are two counts.
- Count A. T lies in gZ with |T| <= T0, so there are at most 2T0/g + 1 values of T. Each has at most 2 tau*(h) signed a.
- Count B. Let s0 be whichever of a, b has |s0| <= sqrt(T^2 + delta^2) <= T0 + |delta|. By Lemma K, s0 + T = delta1 k with |k| <= (2T0 + |delta|)/delta1 <= 3T0/delta1. Since T = delta1 k - s0, we have T = delta1 k (mod s0), and s0 | T^2 + delta^2 gives s0 | delta1^2 k^2 + delta^2. That number is nonzero and at most 9T0^2 + delta^2 <= h^2. Given k, s0 is one of at most 2 tau*(h) signed divisors. Then T = delta1 k - s0, and the choice of which of a, b equals s0 fixes the solution. That gives at most (6T0/delta1 + 1) * 4 tau*(h).
- Hence the count for g is at most 4 tau*(h)(6 T0 min(1/g, 1/delta1) + 1). Since delta1 >= sqrt(|delta|/g), min(1/g, 1/delta1) <= min(1/g, (g/|delta|)^(1/2)) <= |delta|^(-1/3): if g >= |delta|^(1/3) the first term is at most |delta|^(-1/3), and otherwise the second is.
- Summing over the at most tau(|delta|) values of g gives the claim. ∎

T-BOUNDS FROM THEOREM B. Theorem B needs |X| >= S and |X| > sigma delta^2/2, and both hold for admissible solutions. Then exactly one of four regimes holds.
- (c) |e1| <= |X|/2 and (s) |e1| > |X|/2 with |U| > |X|/2. In both, |U| >= |X|/2 > sigma delta^2/4, so |T| = |m delta|/|U| < 4h/(sigma|delta|) <= 4h/|delta|. Also |delta| < 2.02 sqrt(h).
- (n-). Here N <= -2|m delta|, so |U| >= sqrt(2|m delta|) and |T| <= sqrt(h|delta|/2). Theorem B gives |X| < 2h^(2/3), so |delta| < 2h^(1/3). For |delta| <= 3.17 h^(1/3) we have sqrt(h|delta|/2) <= 4h/|delta|.
- (n+). |delta| <= max(2(F - 1), 2(h - H), 2(L - 1)) <= 47998.
So every admissible solution outside (n+) has |delta| <= 2.02 sqrt(h) and |T| <= T0(delta) := max(4h/|delta|, |delta|) <= h/7. That meets the hypothesis 9T0^2 + delta^2 <= h^2 of B2. B1 needs |delta| <= h/5, which holds.

PROOF OF THEOREM 1. Each solution (T, U, V, m) gives one row y_hat = s - m for each of the 3 seas, so C(h) <= 3 times the solution count. Split the offsets at D = h^(3/11). All sums run over delta in 28Z.
- (n+) solutions, by B1: at most 12 tau* sqrt(h) * sum over |delta| <= 47998 of sqrt|delta|, plus lower order. This is about 6e6 tau* sqrt(h).
- Non-(n+) solutions with |delta| <= D, by B1: at most 12 tau* sqrt(h) * (4/84)(D + 28)^(3/2) + O(tau* D). This is O(tau* h^(1/2 + 9/22)) = O(tau* h^(10/11)).
- Non-(n+) solutions with D < |delta| <= 2.02 sqrt(h), by B2 with T0 = T0(delta): at most 4 tau* tau_delta * sum of (24 h|delta|^(-4/3) + 6|delta|^(2/3) + 1). Here tau_delta = max tau(|delta|) <= tau*(h). The sum is at most (144/28) h D^(-1/3) + 0.83 h^(5/6) + 0.15 sqrt(h) = O(h^(10/11)).
- Adding up, C(h) <= C0 tau*(h)^2 h^(10/11). The leading constant is 3 * 4 * 144/28, about 62, for the B2 term. (The value 22 stated earlier counted the B2 term without the factor 3 for the seas; I count 62 here and give no certified value.) The (n+) term is below h^(10/11) once h >= about 4e16. Since tau*(h) = h^(o(1)), C(h) <= C_eps h^(10/11 + eps).
- Every element of Y_rho is the y_hat of at least one admissible solution, so |Y_rho| <= C(h). ∎

PROOF OF COROLLARY 2.
- (a) For a fixed odd row a there are at most h/2 + 1 labels (parity edges) {a, b}, and likewise for even rows. There are 196 blocks and 2 roles.
- (b) By Fact 0, every R2s event among core labels has a side owner e with row_rho(e) in Y_rho, and every such e is in Rel. The events of the remaining labels are evaluated in the same cores, with original Hilbert ranks and with the moved labels' slots left unused (F columns, as for padding). Their R2s candidate set is empty, because the admissible-solution set is Hilbert-free and does not depend on occupancy: Lemma G drops all slot-emptiness conditions. The candidate sets of the other families only shrink, by the same Lemma G convention. Theorem H7's completeness argument is per core and allows any slot occupancy, so it still applies.
- (c) Proposition partial (c) places any n parity edges at width c0(n + 4) tau*(h)^2 + 6h^2 + 4, and case (a) at c0 n tau*(h)^2. Under (Rel), the J5 gluing adds O(h^2). With (a) this gives 1e4 c0 tau*(h)^4 h^(21/11) + O(h^2) = O(h^2), because tau*(h)^4 = h^(o(1)). ∎

REMARK (what this does to the per-pair question). Corollary 2(b) makes the M - 1 per-pair bound unnecessary for the asymptotic goal m_h = O(h^2). In the original board, Theorem 1 says that the fraction of labels in any R2s pair is at most h^(-1/11 + o(1)). Before I found Theorem 1 I also proved a weaker split: every pair with R2s constraints in both roles is one of at most C_eps h^(3/2 + eps) pairs. Theorem 1 supersedes it.

SANITY CHECKS (each run under 60 s with py; the scripts are in script folder; both repositories were only read; no git command was run).
- check_congruence.py tests Lemma K, the identity (a + T)(b + T) = delta^2 + 2TU, and (E1) to (E3) on 62,925 solutions (delta in 2Z up to 400 and several 7-adic and 2-adic values, random T up to 6000). There were 0 failures.
- check_counting.py runs an exhaustive toy at h = 1500, delta in 2Z up to 160, with all solutions where 1 <= |m| <= h. It confirms the (k, s0) reparametrization of B2 on 175,726 cases (0 failures) and the bounds of B1 and B2. The worst count/B1 ratio was 0.014 and the worst count/B2 ratio 0.009.
- check_coverage.py brute-forces over all m (h = 600, delta up to 60), with all factorizations of N. It finds 29,704 solutions, and every one lies in the T-small or the U-small branch.
- By hand: every proof step above, the regime T-bounds and the exponent balance h^(1/2) D^(3/2) = h D^(-1/3) at D = h^(3/11).

## Checks

Three sanity scripts in scripts_gm3_r2s_doubles/. Each ran with py in under 60 s and well under 1 GB, and all use relative imports only.
- check_congruence.py tests Lemma K and Theorem A's identities on 62,925 solutions. There were 0 failures.
- check_counting.py runs an exhaustive toy (h = 1500, delta <= 160). The B2 reparametrization had 0 failures in 175,726 cases. The worst count/B1 ratio was 0.014 and the worst count/B2 ratio 0.009.
- check_coverage.py brute-forces over m (h = 600, delta <= 60). All 29,704 solutions lie in one of the two branches of B1.
I read r2s_middle_zone.md, r2s_single_pair_multiplicity.md, hilbert_sea_design_h7.md, audit_hilbert_sea_design_h7.md, hilbert_residual_families.md, the Theorem B section of audit_hilbert_tiling_and_residuals.md, Proposition partial in sec5_threshold.tex, and the header of audit_consolidated_board_v4_steps.md. I ran no census over heights and installed nothing. I did not touch the repositories and ran no git command.

## Gaps

- The target as stated is not met. No per-pair bound of M - 1 on distinct R2s constraints in the original board is proved, and no pair with M or more constraints was constructed. Theorem 1 makes this unnecessary only for the asymptotic goal.
- Asymptotic only. The relocation cost 1e4 c0 tau*(h)^4 h^(21/11) is o(h^2), but it drops below h^2 only when tau*(h)^4 < h^(1/11)/const, which needs lnln h > about 30. At h about 1e11, tau*(h)^2 is about 1e11 by my estimate, so moving even one full row of labels costs about h^2. For explicit widths at practical heights, the per-pair question or a cheaper relocation is still needed.
- Corollary 2 rests on the layout hypothesis (Rel): a Proposition partial window glued to the H7 board by J5 with the global switch z. The H7 board has row-h tails everywhere, and the WP case (a) block has a row-1 background. So WP must sit on the row-1 side of z, or be the reflected case (c) block, which carries the global z. The v4 board does this (audited), but I did not re-derive the junction for H7 cores with N1 collars.
- Corollary 2(b) uses Lemma G's dropped-emptiness convention and the claim that Theorem H7 holds per core for any slot occupancy (moved labels leave unused F slots, like padding). I argued this but did not re-check it line by line against N1 Claims (a) and (b) or the T1 one-label theorem.
- The explicit constants C0 and 1e4 are hand counts, not certified. The exponent 10/11 is not optimized: the worst case of Lemma B2 is square-full delta/g, and the typical saving is |delta|^(-1/2).
- Inputs used but not re-derived: Theorem A and Theorem B (audited, correct with fixable gaps), Hilbert locality (audited), Theorem H7 (audited, conditional on N1, AP4 and the positional lemma), Proposition partial (paper, Section 5). H7's unaudited inputs (N1, S1 to S6 as audited, the exceptional-label tails) are inherited by Corollary 2.
- Nothing in this note is audited.

## Missing estimate

At practical heights (h about 1e11 and above), one of two estimates is still needed. (1) A per-pair bound of M - 1 on R2s constraints. Lemma 3 of r2s_middle_zone.md reduces this to Hilbert-free single-row multiplicities: in a pair whose constraints are all in one role, one side carries at least ceil(M/2) values, all from the at most 2 live seas of one row and one offset. (2) A relocation that costs h^(o(1)) per row of labels, or O(1) per label, instead of the tau*(h)^2 per label of Proposition partial. One candidate is a secondary H7-type core holding only the labels of the rows in Y_rho. The rows would be re-indexed, and that needs a replacement for (Hil), because row differences are no longer 28 times index differences.

## Next steps

- Audit Lemma K, Lemmas B1 and B2, the regime T-bounds and Theorem 1. They are short and self-contained, and the key step is that delta' | U forces delta1(delta') | a + T.
- Feed the result into the gap-mixing synthesis. Asymptotically R2s can be dropped from the candidate multigraph, so the full-component and boundary-repair work needs to handle only P constraints. Ask Arjun whether an asymptotic-only removal is acceptable for the O(h^2) program.
- Try the same row-relocation count on FW and on 6PT-same. Their arithmetic is also fixed by rows and offsets (X xi = -delta m with fixed rows), so their solution rows may also be o(h).
- Check the J5 junction of one Proposition partial window with the H7 board (row-h tails, N1 collars, the side of z) to turn (Rel) into a proved step.
- Optional: sharpen the exponent. In Lemma B2 the saving is |delta|^(-1/2) unless delta/g is square-full, which may give about h^(5/6). Also compute C0 exactly.

