# R2s multiplicity on one label pair

14 November 2026. Problem 001. Continues continuation_gap_mixing_audit.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (partial): on one curve, the R2s constraints in a window have distinct |U| for all h and 1 <= M <= 40; outside an explicit middle zone there is at most one per arc, so at most 3 per live curve; at most 8 live curves exist per pair. The middle zone, where most H7 pairs lie, has neither a bound nor a construction. Not audited yet.

# Result

## Status

partial

## Summary

R2s on one curve: constraints in a window have distinct |U| (all h, 1 <= M <= 40), at most one per arc outside an explicit middle zone, at most 8 live curves per pair. Middle zone still open; no construction found.

## Statements

SETTING. Design H7 with stride S = 6272 sigma (sigma a power of 2), e := v2(S) = 7 + log2 sigma, and M choices. A "curve" means one label pair (e,f), one parity role, one side owner and one sea row s. It fixes m = s - y and delta = (partner row) - y, with N = delta(2m - delta) != 0 and K = 2 m delta = N + delta^2. sign K = sign N, and K/N lies in (1,2) if N > 0 and in (0,1) if N < 0; this follows from (Bulk). The pair's window is I = S*[M dr - (M-1), M dr + (M-1)], with length W = 2(M-1)S. Every X in I has |X| >= S, and all X in I have one sign. Write X_- = min over I of |X| and X_+ = max. A constraint of the curve in I is a distinct value X in I that comes from a solution of Theorem A of hilbert_residual_families.md (TU = -m delta, V^2 - U^2 = N, 2X = U + T - V) and passes the archive tests: S | X, weak Hil and M-dependent Hil, the sea types of B (offset U) and D (offset V), the strip, and e1, e2 != 0. Put g = V - U. Then T = Kg/(g^2 - N) and X = F(g) := (Kg/(g^2 - N) - g)/2. Each arc of g (N > 0: (-inf,-sqrt N), (-sqrt N, sqrt N), (sqrt N, inf); N < 0: all of R) carries F strictly decreasing.

THEOREM 1 (sign orbit; proved).
(0) Every R2s solution has v2(U) != v2(T).
(a) The solutions with a given |U| are (U,V), (U,-V), (-U,-V) and (-U,V), with X-values X, X+V, -X and -(X+V). If s is L or H, at most one of the four passes the sea-type tests. So for s in {L,H}, each |U| carries at most one solution at any distance.
(b) If s = F and two members of the orbit with values of the same sign both have S | X, then v2(U) >= e, v2(T) >= e and v2(delta) + v2(m) >= 2e+1. Hence 49 * 2^(2e) | delta and |delta| >= 802816 sigma^2. By Theorem B's delta cap, this is impossible for h < 1.58e11 sigma^5.5.
(c) For every h, every sigma and 1 <= M <= 40, two distinct R2s constraints of one curve in one window have distinct |U|. The (U,-V) partner is excluded for 2 <= M <= 2731 sigma^3. The (-U,V) partner is excluded for M <= 40.
COROLLARY. For M <= 40, the number of R2s constraints per (pair, role, side, s) and window equals the number of distinct admissible |U| whose solution lands in the window. The archive's 2 tau(|N|) is now a bound on this |U| count, not on +-V or sign duplicates.

THEOREM 2 (slow-variable zones; tau-free; proved). Let d_U = 7 if s = F and d_U = 1 otherwise.
N > 0. Take X > 0; X < 0 is the mirror image under g -> -g. Each of the three arcs carries at most one constraint in I if X_- >= sqrt(KW/3.5) (s = F) or X_- >= sqrt(KW) (s = L or H). Separately, the inner arc |g| < sqrt N carries at most one if 3 X_+^2 + 4 X_+/sigma < 14K/W. So far from the window centre a curve carries at most 3 constraints in I.
N < 0. The curve is one arc. It carries at most one constraint in I if X_- >= max(sqrt|N|, sqrt(|K|W/9.54)), or if 12 X_+^2 + 2 X_+/sigma < 12.25|N|/W.
All of these bounds are independent of tau(|N|), h and the Hilbert curve.

THEOREM 3 (live curves per pair; proved from the audited Theorem C). Let k = v2(delta) for one parity, with k <= e - 2. Then only seas whose (Al) valuation v2(m) equals [0 if k is even and >= 4, else 1] can carry R2s solutions. Odd role: {L,F} if k is in {2,3,5,7,...}, {H} if k is even and >= 4. Even role: the opposite. So a pair has at most 8 of its 12 curves live, two sides times at most two seas per parity. If 49 does not divide delta, only the L curves with 7 | m can be live.

EXACT FINITE CENSUS (Hilbert-free; exact on the stated domains). This is evidence, not a theorem. For s = F with |X| <= 1500 S, |delta| <= 12000 and delta in 196Z, 56,518 curves carry an admissible solution. Every one carries exactly one |U|, which gives the pair +-X, and none carries two positive X/S. A complete enumeration from all factorizations g1 g2 = N, at any distance, on 7,000 sampled curves finds exactly one admissible positive X each. For all three seas (|X| <= 150 S, |delta| <= 3500, delta in 28Z), the counts are: F, 1,643 curves; L, 42,840 curves (2,500 fully enumerated); H, 1,873 curves. Each has exactly one admissible |U|, there are 0 +-V doubles, and each L and H curve has exactly one solution in total.

NOT PROVED. Neither alternative of the target is settled in the middle zone. For N > 0 that zone is sqrt(14K/(3W)) <~ |X| <~ sqrt(KW/3.5) on the inner arc, and |X| < sqrt(KW/3.5) on the two outer arcs. For N < 0 it is between the two thresholds of Theorem 2. Most H7 pairs lie there. Example: h = 1e11, s = F, delta = -784, y ~ h/2, M = 3 gives rank gaps from about 6 to about 4e4. No pair with more than M - 1 distinct R2s constraints was constructed.

## Proofs

CONVENTIONS. (Al) gives v2(m) in {0,1}, with the value by role and sea as in H7. 28 | delta, so k = v2(delta) >= 2. Theorem A gives T even and delta != 0. (Bulk) and the strip give |m| >= 1e5 - F >= 76048, F <= 23952, and delta >= -2(F-1) > -47904 when s = F. M-dependent Hil (H7 tools, audited in the residual audit) gives |X| > M sigma delta^2/2 - (M-1)S for every constraint in the pair's window: dr > delta^2/12544 and |X| >= S(M(dr-1)+1).

Lattice facts, valid at every solution:
- 14 | g. Here g = T - 2X with T even and 7 | X. If 7 does not divide U, then 7 | T because 7 | delta. If 7 | U, then s = F, so 7 | V and g = V - U.
- 14 | T, because T = g + 2X.
- 28 | q := -T - g, because q = -2X - 2g.
- 7 | U if s = F, by the type test.
- U | V^2 + delta^2, because 2UT = -K = -(V^2 - U^2 + delta^2) and T is an integer.

PROOF OF THEOREM 1.
(0) Suppose v2 U = v2 T = u. Then v2(m) + k = 2u is even, which excludes (v2 m, k) = (1,2). So k > 1 + v2(m), v2(2m - delta) = 1 + v2(m) and v2(N) = 2u + 1. But v2(V^2 - U^2) equals 2 min(v2 V, u) if v2 V != u, and is at least 2u+3 if v2 V = u, because odd squares are 1 mod 8. Neither value is 2u+1.
(a) For fixed U, T = -m delta/U is fixed and V = +-sqrt(U^2+N). The four sign changes preserve the curve equations, with the stated X-values; for example (-U,V) gives 2X'' = -U - T - V. For s in {L,H}, the tests need 7 not dividing U or V and stype(U) = stype(V) = s. Since -1 is a non-residue mod 7, stype(-x) != stype(x) for 7 not dividing x. Flipping one sign breaks one test, and flipping both breaks both.
(b) Two same-sign members with S | X are, up to renaming within the orbit, either {X, X+V} or {X, -(X+V)}. In both cases S | V and S | U + T, since U + T = 2X + V. By (0), v2(U+T) = min(v2 U, v2 T) >= e, so v2(m) + k = v2 U + v2 T >= 2e+1. Then k >= 2e, and Theorem C gives 49 | delta. Theorem B caps |delta| below max(2.02 sqrt(h) sigma^(-3/4), 47998). This gives the stated height range.
(c) Two constraints in one window with equal |U| come from the same orbit. {X,-X} and {X+V,-X-V} have opposite signs and so cannot share a window. For s in {L,H}, (a) applies. For s = F, (b) gives delta^2 >= 802816^2 sigma^4 = 16384 sigma^2 S^2.
- Type {X, X+V}, with |V| <= W. The identity 4UX = (3U+V)(U-V) - delta^2 follows from 2UT = -(N + delta^2). With 1 <= |U| <= R := V^2 + delta^2 and convexity of 3u/4 + R/(4u), it gives |X| <= |V| + 3(V^2+delta^2)/4 + 1/4. With M-dependent Hil this gives (M sigma/2 - 3/4) delta^2 < 3(M-1)^2 S^2 + 3(M-1)S + 1/4. That means 16384 sigma^2 (M sigma/2 - 3/4) < 3(M-1)^2 + o(1), which is false for 2 <= M <= 2731 at sigma = 1 (first failure at M = 2732), and for a larger range when sigma > 1.
- Type {X, -(X+V)}, with |U + T| <= W. Since delta < -47904 is impossible, delta > 0. Since s = F lies below the bulk, m < 0. So UT = -m delta > 0, |U| + |T| = |U+T| <= W and |m delta| <= W^2/4 = (M-1)^2 S^2. Hence |m| <= (M-1)^2 S^2/(802816 sigma^2) = 49 (M-1)^2, which contradicts |m| >= 76048 when M <= 40.
The Corollary follows, because constraints are distinct X values.

PROOF OF THEOREM 2. On each arc F is a strictly decreasing bijection onto R. For N > 0, F' = (R'-1)/2 with R' = -K(g^2+N)/(g^2-N)^2 < 0. For N < 0, R' = |K|(g^2-|N|)/(g^2+|N|)^2 <= |K|/(8|N|) < 1/8, so |F'| > 7/16. So the solutions on an arc with X in I lie in one g-interval J and have distinct X. For a variable phi that is injective and nonzero on J and takes values in d_phi Z at solutions, two solutions give |1/phi1 - 1/phi2| >= d_phi/|phi1 phi2|. The mean value theorem bounds the same quantity by W sup_J |d(1/phi)/dX|.
- U on N > 0. U = (N/g - g)/2 is strictly decreasing on each arc and vanishes only at g^2 = N. The derivative satisfies |dU/dX| = (N+g^2)(g^2-N)^2/(g^2((g^2-N)^2 + K(g^2+N))) <= (g^2-N)^2/(K g^2) = 4U^2/K, so |d(1/U)/dX| <= 4/K and |U1 U2| >= d_U K/(4W). The identity 4UX = g^2 - N - K comes from (E7) and K = N + delta^2. It gives |U| < K/(2|X|) on the inner arc (|g^2 - N - K| <= N + K < 2K). It gives |U| < K/(4|X|) on the outer arc where X > 0 (N < g^2 < N + K). These yield the thresholds sqrt(KW/d_U) and sqrt(KW/(4 d_U)).
- T on the other outer arc, N > 0. There X > 0 and g^2 > N + K. T = Kg/(g^2-N) is strictly monotone and nonzero. Also dT/dX = 2|R'|/(1+|R'|) <= 2|R'| = 2T^2(g^2+N)/(K g^2) <= 4T^2/K, so |T1 T2| >= 14K/(4W). From |g| = 2X + |T| and g^2 - N >= g^2 K/(N+K), we get |T| <= (N+K)/|g| < K/X. So X_-^2 >= KW/3.5 is a contradiction.
- q on the inner arc, N > 0. q = g(g^2+delta^2)/(N - g^2) is strictly increasing. Its derivative satisfies |dq/dX| = 2[N(3g^2+delta^2) - g^4 + g^2 delta^2]/[(N-g^2)^2 + K(g^2+N)] <= 2(3g^2 + 2 delta^2)/K. Also |g| <= |X|, because T and g have opposite signs and |T| >= |g|. Weak Hil gives delta^2 < 2X_+/sigma. A range below 28 allows at most one value.
- N < 0. q = -g(g^2+delta^2)/(g^2+|N|) is strictly monotone, because its derivative numerator g^4 + g^2(3|N| - delta^2) + delta^2|N| is positive (|N| > delta^2). Also q' <= (3g^2+delta^2)/|N|, |dq/dX| <= (16/7) q' and |g| <= 2|X|. This gives the small-X condition. For X_- >= sqrt|N|, we have |T| < sqrt|N|/2 and |g| > 1.5 X_- >= 1.5 sqrt|N|, so T is monotone and nonzero on J. Then |dT/dX| <= (16/7)|K|/(g^2+|N|) <= (16/7)(13/9) T^2/|K|, and |T| < |K|/(1.5 X_-). The contradiction holds once X_-^2 >= |K|W/9.54.

PROOF OF THEOREM 3. v2(U) = v2(m) + k - tau >= 0, so tau <= k + 1. For k <= e - 2 this gives tau < e and k <= e, which are Theorem C's hypotheses. Theorem C (audited) says: if m is odd, then k is even and k >= 4; if m = 2 mod 4, then k is in {2,3} or k is odd and >= 5. So v2(m) is determined by k. By (Al), v2(m) is 1 for (odd; L,F) and (even; H), and 0 for (odd; H) and (even; L,F). The side-f curve uses a row of the same parity, so it has the same v2(m) and the same k. For the 7-adic remark: s = F needs 49 | delta (Theorem C). s = H, and s = L in the even role of mixed blocks, have 7 not dividing m, so v7(delta) >= 2.

CHECKS (sanity; each script < 60 s).
- check_lemmas.py: 368 toy-modulus doubles all satisfy v2(delta) + v2(m) >= 2e+1, so the bound is attained. The identity 4UX = g^2 + delta^2 - 2K and the zone bounds hold on 3,756 solutions with 0 violations.
- The numeric constants were checked by one-line computations: 802816^2 = 16384 S^2; first failure at M = 2732 and at M = 41; 1.58e11.

## External results used

- No published theorem used, and no web source consulted.
- Internal and audited (audit_hilbert_tiling_and_residuals.md, 'hold as stated with fixable gaps'): Theorem A (exact form, (E1)-(E7)), Theorem B (delta caps |delta| < max(2.02 sqrt(h) sigma^(-3/4), 47998)) and Theorem C (2-adic list under tau < v2 S and k <= v2 S; s = F needs 49 | delta; s in {L,H} with 7 not dividing m gives v7 delta = v7 X >= 2) of hilbert_residual_families.md. I use Theorem C only where I verified its hypotheses (k <= e - 2, which forces tau <= k + 1 < e).
- Internal, H7 tools: (Al) v2(s-y) in {0,1} by parity; (Bulk) label rows in [1e5, h - 1e5], F <= 23952, h - H <= 783; (Hil) and its M-dependent form |X| > M sigma delta^2/2 - (M-1)S; the strip condition of (V4). These come from hilbert_sea_design_h7.md, audited as correct with fixable gaps, and inherit its unaudited inputs (AP4, S1-S6, N1).
- Remark only, not used in the theorems: tile separation. Theorem T of hilbert_tiling_assembly.md (audited, conditional on hypothesis (A)) allows any partition of a block's labels into tiles with original ranks, at core cost S M Q^2 per tile. Candidate sets defined with slot-emptiness dropped (Lemma G) restrict to tiles. So if the pairs of some bad set form a graph of degeneracy at most D_B in every block, D_B + 1 tiles separate every bad pair, at width at most (D_B + 1) 6272 sigma M (h+28)^2 + O(D_B h) + C1 h^2. No bound on D_B is proved.

## Checks

All scripts are in scripts_gm1_r2s_mult/ (40 KB). I ran them one at a time with py, each under 60 s and well under 1 GB.
- explore_xy.py 1500 12000 (42 s): s = F, both roles, delta in 196Z with -3998 <= delta <= 12000, |X| <= 1500 S. It generates curves from 4 delta m Y = -(X-Y)((X+Y)^2+delta^2) with Y | X^2+delta^2. Result: 113,036 solutions on 56,518 curves, exactly 2 per curve (+-X), and 0 curves with two X/S in one window for M = 2..5. The 5 hits at M = 5 are the pairs X/S = +-4, which have opposite signs and so do not share a window.
- full_curve.py: complete enumeration from all signed factorizations of N on 4,000 sorted and 3,000 random curves. Every curve has exactly one positive admissible X/S, at any distance.
- diag.py and diag2.py: without the S | X filter, 1,498 of 1,500 F-curves have exactly 4 F-type solutions (one |U|). One has 8 and one has 12. In every printed example the second solution is the +-V partner, and it fails S | X.
- census_seas.py with seas F, L and H (n <= 150, |delta| <= 3500, delta in 28Z, all six H7 m-classes): F, 1,643 curves with exactly one |U|; L, 42,840 curves (2,500 fully enumerated) with exactly one solution each; H, 1,873 curves with exactly one each; 0 +-V doubles.
- pmv_double.py: 0 +-V doubles for |v| <= 4 and delta <= 7840. This agrees with Theorem 1.
- check_lemmas.py: 368 toy 2^e doubles all satisfy v2(delta) + v2(m) >= 2e+1, and 3,756 solutions satisfy the zone identity and bounds.
- curv_consts.py: closed forms of G'' and G''' agree with finite differences. These are numerical sup values only and support no claim.
By hand: every derivation in the proof field, and the constants 802816^2 = 16384 S^2, M <= 2731, M <= 40, 1.58e11, 3.5, 9.54, 12.25, 14/3 and the example zone 19 S to 1.2e5 S. Neither repository was touched, and no git command was run.

## Gaps

- The middle zone is open. For N > 0 it is sqrt(14K/(3W)) <~ |X| <~ sqrt(KW/3.5) on the inner arc, and |X| < sqrt(KW/3.5) on both outer arcs. For N < 0 it lies between the two thresholds of Theorem 2. There no tau-free bound is proved: a curve could carry several admissible |U| in one window. Most H7 R2s candidates lie in this zone, so the target is not resolved.
- No construction was found. The obvious double, the +-V partner, is impossible in-window for M <= 40 (Theorem 1). A second admissible |U| with S | X in the same window is a two-condition Diophantine coincidence. A naive search would need about 1e13 trials, and I found no polynomial family that makes S | X automatic for two solutions.
- Theorem 1(c) covers only M <= 40, the range of the current M = 3 or 4 work. For 41 <= M the (-U,V) partner with 49*2^(2e) | delta, delta > 0 and |U + T| <= W is not excluded, and it is arithmetically possible only for h >= 1.58e11 sigma^5.5.
- Theorem 3 needs v2(delta) <= e - 2 = 5 + log2 sigma for the parity concerned. Larger 2-adic valuations of delta are unclassified, as in Theorem C.
- The per-pair corollaries are weak: at most 3 constraints per live curve far from the window centre and at most 8 live curves, so at most 24 per pair outside the middle zone. This is tau-free but not below M - 1 for M = 3 or 4.
- Theorem 2 is curvature-free. A curvature (determinant) argument in the lattice 14Z x SZ would put any three constraints on one arc on a line, hence at most 3 per arc, when |N| > (c2 (M-1)^3 S^2/14)^2. The constant c2 = sup|G''| sqrt|N| was evaluated only numerically (about 2.35, script curv_consts.py), not certified. It does not beat the trivial bound 2M-1 at M = 3, so I do not claim it.
- Inputs used but not re-derived here: Theorem A, Theorem B (delta caps) and Theorem C of hilbert_residual_families.md (audited, correct with fixable gaps); H7 tools (Al), (Bulk), (Hil) and the M-dependent Hil form; the strip condition of (V4). H7's own unaudited inputs (AP4, S1-S6, N1) are inherited.
- The census is Hilbert-free and covers small |X| and |delta| only. It cannot exclude rare middle-zone coincidences at h ~ 1e11, where heuristically some may exist. The heuristic is not computed.
- Nothing here is audited.

## Missing estimate

To settle the target, one statement in the middle zone is needed. For a curve (m, delta, s) of H7 and a window I of length W = 2(M-1)S, at most c admissible values |U| (c absolute, ideally 1) have their constraint in I. Admissible here means: U | m delta with T = -m delta/U even, U^2 + N a square, the sea types, S | X with X = (U - V + T)/2, Hil and the strip. Equivalently, show that N has no two signed factorizations g1 g2 = N with (g2 - g1) | K, 14 | g1, g1^2 = 2N + delta^2 (mod 4S), and X-values within W of each other, inside the zone sqrt(|N|/W) <~ |X| <~ sqrt(|K|W). Short of that, a count would do: the number of labels per block lying in a pair with two such |U|, of order O(h) or bounded degeneracy. With it, the tile-separation remark below relocates them at constant-factor cost.

## Next steps

- Middle zone, first case: N < 0 (delta > 0 for s = F), which has a single arc. Two admissible |U| in one window give two divisors of K/2 and two factor pairs of |N| near sqrt|N|, all with g = sqrt(2N + delta^2) mod 4S. Try to combine the 4S-congruence on g with Lemma D, applied to the divisors U of K/2 in the window's U-interval of length about W.
- Look for polynomial or Gaussian-integer families with two solutions on one curve. Write T + i delta = (x + iy)(z + iw), so a = x^2 + y^2 and b = z^2 + w^2, and impose a common (m, delta) with X' - X = jS constant. Such a family would decide the construction alternative. If none exists at degree <= 2, that is evidence for c = 1.
- Extend Theorem 1(c) beyond M = 40 if the large-M framework needs it. The (-U,V) case needs delta > 0, 49*2^(2e) | delta and |m| <= 49 (M-1)^2; check it against (Hil) for the real Hilbert partner.
- Classify v2(delta) >= e - 1 to complete Theorem 3, and use the live-curve list in the gap-mixing graph. Each live curve contributes at most one gap per distinct |U|.
- Have a second reader audit Theorems 1-3. They are short. The key steps are v2 U != v2 T, the identity 4UX = (3U+V)(U-V) - delta^2, the identity 4UX = g^2 - N - K, and the four derivative bounds.
- Optional: certify sup|G''| by interval arithmetic and state the collinearity lemma, giving at most 3 per arc when |N| > (c2 (M-1)^3 S^2/14)^2. It is useful only for large M.

