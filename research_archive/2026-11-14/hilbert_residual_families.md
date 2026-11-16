# The residual sea families R2s, FW and 6PT

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: the three residual families of design H7 are parametrized. Every R2s is short-range or has a bounded row offset; every R2s, FW and 6PT event has 2 to 4 placed labels and forbids exactly one value of the label placed last; FW is empty for h <= 6.16e10 M sigma^4 and the unequal-offset part of 6PT for h <= 1.76e5 sigma^2; none shows a near-diagonal band excess. Hypothesis (G) holds for them only heuristically, and no deterministic exclusion was found. Audited in audit_hilbert_tiling_and_residuals.md (correct with fixable gaps).

# Result

## Status

partial

## Summary

The residual families R2s, FW and 6PT of design H7 are now fully parametrized. Every R2s is either short-range (|X| < 2.04h/sqrt(sigma), |delta| < 2.02 sqrt(h) sigma^(-3/4)) or has a bounded row offset (|delta| <= 2(F-1) < 48000). For R2s, FW and 6PT, every event has 2-4 placed labels and forbids exactly one value of whichever label is placed last. FW is empty for h <= 6.16e10 M sigma^4, and the unequal-offset part of 6PT for h <= 1.76e5 sigma^2. None of the three shows a near-diagonal band excess. A complete census of one block at h = 4e4 finds 8 R2s pairs at M = 1 and none at M = 2, 3, 4. Hypothesis (G) holds for them only heuristically, and I found no deterministic exclusion.

## Statements

Notation (design H7, one block). Rows: odd label rows a = a0 + 28i and even label rows b = b0 + 28j. Sea rows L <= 28, F <= 24000 and H >= h - 783. Label rows are bulk rows in [C1, h - C1].
- Columns: x_e = S(M r_e + xi_e), with S = 6272 sigma (sigma a power of 2), so v2(S) = 7 + log2(sigma) and v7(S) = 2.
- The sea type of a column is fixed by its residue mod 7, measured from the label columns: F at 0, L where chi_7 = -1, H where chi_7 = +1. Unused slots hold F.
- (Hil) For same-parity points of two labels: delta = 28 Delta, where Delta is the Hilbert-coordinate difference, satisfies Delta^2 < 16 Dr, where Dr is the rank distance. Also |X|/S >= M(Dr - 1) + 1. Hence |X| > sigma delta^2/2 (weak form) and |X| > M sigma delta^2/2 - (M-1)S.
- (Al) For a label row y and a sea row s: v2(s - y) = 0 if their parities differ, and 1 if they agree.
- m = s - y. It is negative for s in {L, F} and positive for s = H.

THEOREM A (exact form of R2s; proved). Write A = (x_e, y) for e's point, C = (x_e + X, y + delta) for f's point of the same parity, B = (x_e + U, s) and D = (x_e + X + V, s). The four points form a mixed quadruple (side AB, diagonal CD) if and only if:
 (E1) V^2 - U^2 = N := delta(2m - delta);
 (E2) T U = -m delta, where T := 2X + V - U;
 (E3) 2X = U + T - V.
Equivalently, there is a signed factorization g1 g2 = N with g1 = g2 (mod 2) such that U = (g2 - g1)/2, V = (g1 + g2)/2, T = -2m delta/(g2 - g1) and X = (T - g1)/2.

Put e1 = U - X (B's column minus f's column) and e2 = e1 + T (D's column minus e's column). Then:
 (E4) 4 e1 (X - T) = T^2 + delta^2;
 (E5) 4 e2 X = T^2 + delta^2 - 4m delta;
 (E6) 4 e1 U = (T + 2e1)^2 + delta^2;
 (E7) 4 U (X - T) = (T - 2X)^2 + delta^2.

In a valid board U, V, T, e1 and e2 are all nonzero. T and delta are even. The shared corners p = A + n and q = B + n, with n = (T, delta)/2, have rows y + delta/2 and s + delta/2.

c-family (proved). For integers U, c, w with m = (1 - w^2 - c^2 U^2)/(2c) integral, the choice delta = -c U^2 and V = U w solves (E1) and (E2). It gives T = m c U and X = -U((w+1)^2 + c^2 U^2 - 4)/4. Every solution found by the censuses below is in this family.

THEOREM B (regimes and a displacement cap; proved). Assume |X| >= S >= 6272 and |X| > sigma delta^2/2. Then exactly one of the following holds.
 (c) |e1| <= |X|/2. Then |X| < 2.037 h sigma^(-1/2).
 (s) |e1| > |X|/2 and |U| > |X|/2. Then |X| < 3.175 h^(2/3) sigma^(-1/3).
 (n-) |e1| > |X|/2, |U| <= |X|/2 and m delta < 0. Then |X| < sqrt(2|m delta|) < 2 h^(2/3) sigma^(-1/3).
 (n+) |e1| > |X|/2, |U| <= |X|/2 and m delta > 0. Then |T| > |X|/2 and |U| < 2|m delta|/|X| < 4|m|/(sigma |delta|). Moreover the row s + delta/2 of q gives -2(s-1) <= delta < 0 for s in {L, F}, and 0 < delta <= 2(h - H) <= 1566 for s = H.

Hence every R2s has |delta| < max(2.02 sqrt(h) sigma^(-3/4), 2(F-1)) <= max(2.02 sqrt(h) sigma^(-3/4), 47998). The long-range R2s ((n+), the only regime where |X| can reach about h|delta|/2) have |Delta_i| <= 1714 for s = F, |Delta_i| <= 55 for s = H, and delta = -28 or nothing for s = L. In the other three regimes the partner's rank distance is below 2.04h/(M S sqrt(sigma)) + 1.

THEOREM C (necessary congruences for R2s; proved). Let k = v2(delta) and tau = v2(T), and assume tau < v2(S) and k <= v2(S).
- If m is odd, then k is even, k >= 4 and tau = k/2 + 1.
- If m = 2 (mod 4), then (k, tau) is (2, 2), (3, 4), or (k, (k+3)/2) with k odd and k >= 5.
7-adic conditions:
- If s is in {L, H} and 7 does not divide m, then v7(delta) = v7(X) >= 2. In mixed blocks these are the pairs (odd, H), (even, L) and (even, H).
- If s = F, then 49 divides delta.

THEOREM D (Hilbert-free degree bound; no band term; proved). Let A(y, s) count the solutions of Theorem A that pass every arithmetic test, for point row y and sea row s. The tests are: S | X, the weak (Hil) bound, the sea types of B and D, the strip, and a partner row y + delta in the block. Let B(y, s) count the solutions of other rows y' with y' + delta = y. Then every label e has
 deg_R2s(e) <= 2 sum over roles and s of [A(y_role, s) + B(y_role, s)].
So the R2s arithmetic of a label depends only on its own row in that role, never on j - i. The Hilbert curve enters only through (Hil) and the exact partner lookup. Rigorously, A(y, s) <= (2 delta*/28) * 2 tau_max(6h^2) with delta* = max(2.02 sqrt(h) sigma^(-3/4), 48000).

PROPOSITION E (FW; proved from H7's S4).
- FW is a parked triangle with sea row F and xi = 0 (mod S). It needs slot x_e + xi empty and slot x_f + xi occupied by a label g.
- It needs 2^(2 v2(S) - 1) 7^4 | delta (odd role) and 2^(2 v2(S)) 7^4 | delta (even role), so |delta| >= D := 19,668,992 sigma^2.
- It needs M sigma delta^2/2 - (M-1)S < |X| <= |delta|(h-1)/S.
- So FW is empty for h <= 6.16e10 M sigma^4. This sharpens H7's 6.1e10 sigma^4 by the factor M.
- Its candidates have arity 3 (e, f, g), or 2 when g = e. Each fixes two column differences.

PROPOSITION F (6PT; built on H7's S6).
- (i) Either xi = xi' (6PT-same) or |xi - xi'| >= S (6PT-distinct).
- (ii) 6PT-same has exactly three labels e, f, e'. C and C' are the two points of f, with a_f - a_e = b_f - b_e' = delta. Then X xi = -delta m and X' xi = -delta m', with m - m' = b_f - a_f, so gcd(m, m') divides f's own row gap.
- Divisibility in mixed blocks: S | delta for s in {L, H}, and 7S | delta for s = F. In zero-residue blocks: (S/7) | delta for L, S | delta for H, and 7S | delta for F.
- Mixed-block 6PT-same with s in {L, H} is empty for h < 3136 M sigma^2 - M + 2.
- (iii) 6PT-distinct is empty for h <= 1.756e5 sigma^2, for every M. Its arity is 2 to 4.

LEMMA G (how the three families enter the choice argument; proved).
- Each R2s, FW or 6PT candidate (all geometric parameters fixed) names a set J of 2, 3 or 4 placed labels and fixes every column difference inside J.
- Every condition involving an unused slot has the form "slot c is empty". These conditions are dropped, which only enlarges the event.
- Hence, whatever the order, the last-placed label of J has exactly one forbidden value of xi.
- Charge each candidate to its last-placed label in a fixed order. Then M = K + 1 avoids all of them, where K is the largest number of candidates charged to one label.
- Every event contains at least two placed labels: A and C always belong to distinct placed labels. So no event exists only through an unused slot holding F.

HEURISTIC (labelled; not proved). These assume equidistribution of the residues mod 4S of the free parameters, and Hilbert hit probability about kappa/sqrt(d) for a prescribed same-coordinate displacement at rank distance d.
- R2s: the mean incidence per label is bounded in h and decreases in sigma. The long-range part decays like h^(-1/2+o(1)).
- 6PT-same: of order kappa^2 log(h/S)/(sigma S).
- FW: of order 1e-5 kappa tau_bar log(h/h_FW)/sigma^2, and only above h_FW.
- 6PT-distinct: smaller still.
- So hypothesis (G) holds for all three on every tile, with room to spare. None of them has a near-diagonal band term.

CENSUS. One aligned mixed block (h = 4e4, bulk from 1e4, sigma = 1), all 1429 rows. Only 3 odd rows carry feasible R2s solutions, all in the c-family with s = F. The whole block has 8 R2s candidate pairs at M = 1 and none at M = 2, 3, 4.

No deterministic exclusion of any of the three families by a small change of the sea or the slots was found. The reasons are in the proof field.

## Proofs

0. Inputs and conventions. I use H7's tools (Hil) and (Al), (Bulk), Lemma S4 (parked triangles, PT) and Lemma S6 (V3 collisions reduce to 6PT). I also use the criterion (V1)-(V5) of block_sea_classification.md. S4, S6 and AP4 are unaudited. A mixed quadruple (side AB, diagonal CD) is black and fatal under (V4) when |B-A| = |D-C|, (B-A).(C+D-A-B) = 0, D-C != +-(B-A), and the shared corners p = A+n, q = B+n (2n = C+D-A-B) lie in rows 1..h.

1. Theorem A.
- Coordinates relative to x_e: A = (0, y), B = (U, s), C = (X, y+delta), D = (X+V, s), with m = s - y.
- Equal norms: U^2 + m^2 = V^2 + (m - delta)^2, which is (E1).
- C+D-A-B = (2X + V - U, delta) = (T, delta). Perpendicularity is U T + m delta = 0, which is (E2). (E3) is the definition of T.
- Factorization form: given (E1), put g1 = V - U and g2 = V + U. Then U - V = -g1 and 2X = U - V + T = T - g1. Conversely the formulas give (E1)-(E3).

Identities.
- (E4): substitute V = U + T - 2X into (E1) and use 2m delta = -2TU. This gives (T - 2X)^2 + 4UT - 4UX + delta^2 = 0, which rearranges to 4(X - T)(U - X) = T^2 + delta^2.
- (a,b) form: with a = 2(X - T) and b = 2e1, we get ab = T^2 + delta^2, X = T + a/2, U = T + (a+b)/2 and m = -T(2X + b)/(2 delta).
- (E6) and (E7) are ab = T^2 + delta^2 rewritten: 2b U = (T + b)^2 + delta^2, and 2a U = (T + a)^2 + delta^2.
- (E5) follows from (2T + b)(2T + a) = T^2 + delta^2 - 4m delta, which uses 2T(a+b) = -4m delta - 4T^2.

Nonvanishing.
- U = 0 or e1 = 0 would put the sea point B in a label column. Likewise V = 0 or e2 = 0 puts D in a label column. A label column holds only its two bulk label points.
- T = 0 would force m delta = 0.
- n must be integral, so T is even.

c-family. With delta = -cU^2: N = -cU^2(2m + cU^2) = U^2(w^2 - 1), so V^2 = U^2 + N = U^2 w^2. Then T = -m delta/U = m c U. Finally 2X = U + T - Uw, and substituting 2mc = 1 - w^2 - c^2 U^2 gives X = -U((w+1)^2 + c^2 U^2 - 4)/4.

Checks: r2s_identities.py verified (E1)-(E6) on 28968 small solutions, and checked by brute force over a box that the factorization form misses no solution. (E7) was checked on census solutions. r2s_block_exact.py confirmed that all six census solutions are c-family.

2. Theorem B. Throughout, delta^2 < 2|X|/sigma and |m| <= h - 1.

(c) Suppose |e1| <= |X|/2.
- (E4) with |e1| >= 1 gives |X - T| <= (T^2 + delta^2)/4.
- So |X| < |T| + T^2/4 + |X|/(2 sigma) <= |T| + T^2/4 + |X|/2. Hence (|T| + 2)^2 > 2|X| + 4, that is |T| > sqrt(2|X|) - 2.
- Also |U| >= |X| - |e1| >= |X|/2.
- So (sqrt(2|X|) - 2)|X|/2 < |T||U| = |m delta| < h sqrt(2|X|/sigma).
- Dividing gives |X|(1 - 2/sqrt(2|X|)) < 2h/sqrt(sigma). With |X| >= 6272 the factor is at least 1 - 2/112, so |X| < 2.037 h sigma^(-1/2).

(s) Suppose |e1| > |X|/2.
- (E4) gives |X - T| < (T^2 + delta^2)/(2|X|).
- If |T| <= |X|/2, then |X - T| >= |X|/2, so X^2 < X^2/4 + 2|X|/sigma and |X| < 8/3. That contradicts |X| >= S. So |T| > |X|/2, and |U| = |m delta|/|T| < 2|m delta|/|X|.
- If also |U| > |X|/2, then X^2 < 4|m delta| < 4h sqrt(2|X|/sigma). So |X|^(3/2) < 4 sqrt(2) h sigma^(-1/2), and |X| < 2^(5/3) h^(2/3) sigma^(-1/3).

(n-) Suppose |U| <= |X|/2 < |e1| and m delta < 0.
- Then N = -|delta|(2|m| + |delta|) <= -2|m delta|.
- V^2 = U^2 + N >= 0 forces |U| >= sqrt(2|m delta|).
- Together with |U| < 2|m delta|/|X| this gives |X| < sqrt(2|m delta|) < sqrt(2h sqrt(2|X|/sigma)). Hence |X| < 2 h^(2/3) sigma^(-1/3).

(n+) Here only the strip is used. q = B + n has row s + delta/2, which must lie in [1, h].
- For s in {L, F}: m < 0, so delta < 0, and s + delta/2 >= 1 gives |delta| <= 2(s - 1).
- For s = H: delta > 0 and delta <= 2(h - H).

Caps. In (c), (s) and (n-), delta^2 < 2|X|/sigma < 4.074 h sigma^(-3/2), so |delta| < 2.019 sqrt(h) sigma^(-3/4). The rank-distance bound follows from |X|/S >= M(Dr - 1) + 1. The numbers 1714, 55 and 1 are 2(F - 1)/28, 2(h - H)/28 and 2(L - 1)/28 < 28, using F <= 24000, h - H <= 783 and L <= 28.

3. Theorem C, the 2-adic part. Write m = -T(2X + b)/(2 delta) and a = 2(X - T). Since tau < v2(S) <= v2(X), v2(a) = tau + 1.
- If tau < k: v2(T^2 + delta^2) = 2 tau, so v2(b) = tau - 1. Since v2(b) < v2(2X), v2(2X + b) = tau - 1, and v2(m) = 2 tau - 2 - k.
- If tau > k: v2(b) = 2k - tau - 1, which must be at least 1, and v2(m) = k - 2.
- If tau = k: v2(T^2 + delta^2) = 2k + 1, v2(b) = k and v2(m) = k - 1.
- Setting v2(m) = 0 or 1, and requiring k >= 2 and b even, gives exactly the stated lists.
- Census check: delta = -196 with m = 2 (mod 4) has tau = 2, and delta = -392 has tau = 4.

The 7-adic part.
- s in {L, H}. U and V are 7-units. Mod 7, (E2) gives T = 0 (since 7 | delta), and (E3) gives U = V. So U + V is a unit.
- Then v7(V - U) = v7(delta) + v7(2m - delta) = v7(delta) =: alpha, because 7 does not divide m and 7 divides delta. Also v7(T) = alpha.
- With P = U - V, P' = P/7^alpha, T' = T/7^alpha and delta' = delta/7^alpha: (E1) gives P' = -m delta'/U and (E2) gives T' = -m delta'/U, both mod 7.
- So P' + T' = 2P' is not 0 mod 7, and v7(X) = v7((P + T)/2) = alpha. Since 49 | X, alpha >= 2.
- s = F. U = V = 0 mod 7, so 49 | (V - U)(V + U) = delta(2m - delta). Here m is a 7-unit (F has normalized residue 3, label rows 0 or 5), so 2m - delta is a unit and 49 | delta.

4. Theorem D.
- Side-owner role: each solution counted in A(y, s) fixes X, hence the slot gap q = X/S. Only the labels at the two slot ranks d in {floor(|q|/M), ceil(|q|/M)} can be f, so each solution gives at most 2 candidates.
- Diagonal-owner role: each solution counted in B(y, s) fixes the gap -X from e, so again at most 2 candidates.
- Nothing else depends on e. The quantities m = s - y and delta, and the tests, involve only the role row and the block's row set.
- The explicit bound follows from Theorem B: at most 2 delta*/28 values of delta, each with at most 2 tau(|N|) signed factorizations, and |N| <= 6h^2.
- P is different. Its arithmetic involves the cross-parity gap b_f - a_e, which is small in the band |j - i| small. That is the source of its band excess. R2s has no such variable.

5. Proposition E.
- From S4: a PT is A, C = A + (X, delta) and S0 = A + (xi, m) with X xi = -delta m, and W = (x_f + xi, s + delta).
- W is in a label column only if xi = 0 (mod S). Then s = F, and S0 lies on the slot column x_e + xi, which must be empty for S0 to be black.
- W in g's column is fatal: if W is white, the column holds both parities (V2); if W is black, the rectangle is fully black (V1).
- Divisibility: S^2 | X xi = -delta m, with v2(m) = 1 (odd role) or 0 (even role) by (Al), and v7(m) = 0. This gives the stated conditions.
- Bounds: |X| <= |delta m|/S because |xi| >= S, and |X| > M sigma delta^2/2 - (M - 1)S by (Hil).
- At |delta| = D the left side is at least about M sigma D S/2. Hence h - 1 >= M S sigma D/2 (1 - o(1)), and S sigma D/2 = 6.168e10 sigma^4.
- Arity: g is the owner of the slot x_f + xi. The candidate fixes x_f - x_e = X and x_g - x_f = xi.

6. Proposition F.
- (i) and the subcase split are H7's S6: W is common, so s and delta are common, and x_C - x_C' = xi' - xi is 0 mod S.
- (ii) If xi = xi', then C and C' share a column, so they are the two points of one label f. Then A has C's parity and A' has C''s parity.
- e != e': if e = e', then X = X' forces m = m' and a_e = b_e, which is impossible. e and e' differ from f because each pairs with a distinct point of the same parity.
- m - m' = b_e' - a_e = b_f - a_f.
- m and m' have opposite parities, so one of them is odd. Then v2(delta) >= v2(X_*) + v2(xi) >= v2(S) for the corresponding X_*.
- 7-adic: xi is a unit for s in {L, H} (L and H columns). In mixed blocks one of m, m' is a 7-unit for each s: s = L gives residues (0, 2) and s = H gives (1, 3). So v7(delta) >= 2.
- s = F: xi = 0 mod 7 and m, m' are units, so v7(delta) >= 3.
- Zero-residue blocks: both label residues are 0, so s = L gives 7 | m and 7 | m', and nothing beyond 7 | delta is forced.
- Threshold: S(M delta^2/12544 - M + 1) <= |X| <= |delta|(h - 1) at |delta| >= S.
- (iii) For each PT, |xi| = |delta m|/|X| <= |delta| h/max(S, M sigma delta^2/2 - (M-1)S) < h sqrt(2/(sigma S)). The maximum is at delta^2 = 2S/sigma, for every M.
- So |xi - xi'| >= S needs S/2 < h sqrt(2/(sigma S)), that is h > S^(3/2) sigma^(1/2)/(2 sqrt 2) = 1.756e5 sigma^2.

7. Lemma G.
- R2s: J = {e, f}. The event requires x_f - x_e = X. B and D are black if they lie in hole columns. If they lie in slot columns, they are black only when the slot is empty.
- FW: J = {e, f, g}, with x_f - x_e and x_g - x_f fixed. The emptiness of slot x_e + xi is dropped.
- 6PT-same: J = {e, f, e'}, with x_f - x_e = X and x_f - x_e' = X' fixed. Any emptiness conditions on S0, S0' or W, when xi = 0 mod S, are dropped.
- 6PT-distinct: J is the union of {e, f} and {e', f'}, with X, X' and x_f - x_f' = xi' - xi fixed.
- In every case all column differences inside J are fixed. So given all but one label of J, the remaining label's slot is determined (or no event occurs). That is exactly one forbidden value of xi.
- Slot windows S[Mr, Mr + M - 1] of distinct ranks are disjoint, so a fixed column names at most one rank.
- Greedy along any order, charging each candidate to its last-placed label, succeeds when M exceeds the maximum charge.
- Every event has at least 2 placed labels: A and C are label points of distinct labels in R2s, FW and 6PT alike.

8. Why no deterministic exclusion was found.
- R2s: by (E2), (E3) and Theorem C, T = 0 mod 7^(v7 T) 2^(v2 T). So B and D sit at column offsets e1 and e2 (from f and from e) that are congruent modulo 7 and to high 2-power. Any reassignment of the period-7 sea types gives B and D the same type, so the type test only asks chi(e1) = type(s).
- Mod-2^j row alignments only shift the allowed values of (v2 delta, v2 T). For example, row step 56 kills the (k, tau) = (2, 2) branch (the delta = -196 solutions), but (3, 4) survives (the delta = -392 solution), at a 4x width cost.
- The c-family is a polynomial family covering a positive density of residue classes, so it is not O(sqrt h) exceptional rows.
- FW and 6PT: their conditions are divisibility conditions (S^2 | delta m, S | delta), and delta can supply the divisibility. Raising v7(S) or v2(S) only moves the polynomial thresholds.
- Setting unused slots or holes to H moves FW to an "HW" family with the same threshold, and breaks H7's mod-7 sieve S1, because H would then occur at residue 0.

9. Heuristic derivations (labelled; not proofs).
- R2s, long range (n+): |delta| <= 48000. The partner sits at rank distance d about |m delta|/(2|U| S M), so it is hit with probability about kappa/sqrt(d) = O(h^(-1/2)) for a typical label.
- R2s, short range: the c-family estimate, summed over c <= |m|/(M sigma U^3) with the M-dependent (Hil), gives a contribution bounded in h and decreasing in M and sigma.
- 6PT-same: about sum over delta in SZ and over xi of p_e p_e', with p about kappa/sqrt(d) and |xi| < 2|m|/(sigma |delta|). The sum over delta = S delta1 of 1/delta1 gives log(h/S). The dependence on M cancels.
- FW: about sum over delta in DZ with |delta| <= 2h/(M S sigma) of tau(delta m/S^2) sqrt(2S/sigma)/|delta|.
- These are compatible with (G) as stated: c0 + c1(k+1) log h/S_k on level-k tiles and c0 + c1 (log h)^2/S_K at the last level, with S_k >= 6272 sigma0 and sigma0 = C log h. On a tile the partners are restricted to the tile, which only shrinks the delta range.

## External results used

- None. No published theorem was used, and no web source was consulted. Repository inputs (unaudited ones marked in H7): H7 tools (Hil), (Al), (Bulk) and Lemmas S4 and S6 (hilbert_sea_design_h7.md); the Hilbert locality bound (continuation_hilbert_placement.md, audited); criterion (V1)-(V5) (block_sea_classification.md); the profile normalizations of filled_mod7_profile_cover.md.

## Checks

All scripts are in scripts_hb2_residuals/. Each was run once at a time with py, under 60 s and well under 1 GB. The repository was not touched.
- r2s_identities.py: (E1)-(E6) hold on 28968 small solutions. The factorization form misses none of the 900 brute-force box solutions. On 6412 Hilbert-type solutions (276 in (c), 20 in (s), 6116 in (n)) every bound of Theorem B holds. No (n-) solutions occur in the toy.
- hilbert_test.py: the Hilbert maps used are bijective and mutually inverse, and locality max(dx^2, dy^2) < 16|dr| has 0 violations for n = 16 and 64.
- r2s_census.py: full factorization enumeration with exact partner lookup in the aligned mixed block (S = 6272).
 - h = 4e4: 200 + 190 + 100 + 10 labels, 0 hits. The pre-Hilbert arithmetic rate was 0.04-0.08 per label, and every solution violated weak (Hil) by a factor of 65-7000 in the arH run.
 - h = 1e5, M = 2: 20 labels, 0 hits.
 - E4 and the 7-adic rule had 0 failures.
- r2s_pruned.py (exact feasible enumeration via Theorem B): 0 hits everywhere. Feasible solutions per label: 0.02 and 0.0067 (h = 4e4), 0 (h = 1e5, 200 labels) and 0 (h = 1e6 with the H7 bulk 1e5, 25 labels).
- r2s_rows.py (complete row census, h = 4e4, sigma = 1, all 714 odd and 715 even rows): A > 0 only for odd rows 13513, 19225 and 24041, all with s = F. The solutions are delta = -196, U = +-14 and delta = -392, U = +-7, with X/S = +-13, +-19 and +-98. The even role has none. At h = 1e5, odd rows 0-800 give the same three rows.
- r2s_block_exact.py: all six solutions are c-family members (assertions pass). Whole-block R2s candidate pairs: 8 at M = 1, 0 at M = 2, 3, 4, among 510510 labels.
- sixpt_same_census.py (scans delta = 0 mod 896, which Proposition F proves necessary):
 - h = 4e4: 1.81 arithmetic events per hub, 0.0008 one-sided hits, 0 full events in 5000 hubs.
 - h = 1e5: 19.5 arithmetic, 0.0043 one-sided, 0 full in 3000 hubs.
 - 0 violations of 49 | delta.
By hand: all proofs in the proof field, the threshold constants 6.168e10 M sigma^4, 1.756e5 sigma^2 and 3136 M sigma^2, and the caps 2.037, 3.175 and 2.019.

## Gaps

- Hypothesis (G) is not proved for R2s, FW or 6PT. The proved results are thresholds, displacement caps, arities and the Hilbert-free bound of Theorem D, whose row count A(y,s) is only bounded rigorously by about (sqrt(h) + 48000) h^(o(1)). A bounded per-label incidence needs equidistribution heuristics, in the same way that P needs H-EQ.
- 6PT-same is not exhausted at any height. Census: 0 full events among 5000 hubs at h = 4e4 and 3000 hubs at h = 1e5. It has no asymptotic emptiness threshold, and its incidence is heuristic only.
- FW above 6.16e10 M sigma^4 and 6PT-distinct above 1.76e5 sigma^2 have only worst-case bounds of order h^(1+o(1)) and heuristic incidences. No census can reach those heights.
- The exact block census (8 R2s pairs at M = 1, 0 at M = 2, 3, 4) covers one mixed block with toy rows (L=3, F=2015, H about h, a = 17 and b = 8 mod 28), bulk from 1e4 instead of C1 = 1e5, at h = 4e4. Zero-residue blocks and the other 195 residue blocks were not run. At h = 1e5 only 800 of the 2857 odd rows were exhausted (same 3 solution rows), and at h = 1e6 only 25 sampled labels.
- Theorems B, C and D, Propositions E and F, and Lemma G are new and unaudited. Propositions E and F rest on H7's S4 and S6, and Lemma G on the (V1)-(V5) criterion. AP4, N1 and S1-S6 are all unaudited, as stated in H7.
- Theorem C's 2-adic list assumes v2(T) < v2(S) and v2(delta) <= v2(S). Other patterns are possible outside this range; I did not classify them.
- The heuristic constants (kappa, residue-root counts) are uncertain by a factor of about 10. My c-family density estimates disagree with the observed per-row rate of 0.008 by up to about 50x in the per-row count, though the per-label hit rate matched. Only the qualitative claims (bounded in h, no band term, small) are supported by data.
- The degeneracy of the union of P, Lambda, R2s, FW and 6PT was not computed. Lemma G gives M = K + 1 with K the maximum charge in one fixed order. Combining with P's ordering adds the three families' back-degrees; I did not bound those for every label.

## Missing estimate

Three estimates would turn the heuristics into (G) for these families. One: an average bound over bulk rows y for the Hilbert-free count A(y,s) + B(y,s), restricted to S | X. This is pure arithmetic: for the long range, the representations of m^2 + U^2 as a sum of two squares with a = m (mod 28), U | m(m - a) and S | X. A uniform bound A + B <= c would already give deg_R2s <= 12c with no Hilbert input. Two: for 6PT-same, a bound for the number of hubs f whose two Hilbert partners at rank gaps |X|/(SM) and |X'|/(SM) have the prescribed same-coordinate displacements delta/28. This is a pairwise anti-concentration statement for i_{r+d} - i_r and j_{r+d'} - j_r. Three: for FW above threshold, the same anti-concentration at displacements |Delta| >= 7e5 sigma^2.

## Next steps

- Audit Theorems B and C (the regime split, the (n+) strip cap and the 2-adic list) and Lemma G. They are short and self-contained.
- Prove a bound on the row count: an average over y of A(y,F) via r2(m^2 + U^2) with the congruence S | X. Start with the c-family, where for fixed (U, c) the solutions are the lattice points (Uw, U^2 c - |m|) on the circle of radius sqrt(m^2 + U^2).
- Run r2s_rows.py over all rows of a zero-residue block and of a second mixed block. Run it at h = 1e5 in chunks of about 300 rows to finish the exact block census. Then run r2s_block_exact.py on the solution rows.
- Exhaust 6PT-same in one block at h = 4e4 with a faster hub loop (precompute partner displacements per rank gap), to replace the sampled zero by an exact count.
- Feed the R2s candidates (Theorem D lists) into the P certificate scripts at h = 2048/4096 profile scale to measure the joint degeneracy, as hilbert_round1_synthesis step 2 asks.

