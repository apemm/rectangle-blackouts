# Conditional costs and small sets for the other families

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (partial): (CC) is not proved for any of the five families. (SS) is settled at the level of single label sets for Lambda3, Lambda4 and FW, and for 6PT under explicit size conditions: a curve-free lattice-point lemma caps the patterns per role structure at 2 (Lambda3, FW) or 4 (Lambda4), independent of M and h, so (SS) reduces to a pattern-free sparsity statement for label sets. The simplest grouped averaging cancels the corner-chain inflation exactly, but cannot push a cost below 1. Not audited yet.

# Result

## Status

partial

## Summary

(CC) is not proved for any of the five families. (SS) is now settled at the level of single label sets for Lambda3, Lambda4 and FW, and for 6PT under explicit size conditions. A curve-free lattice-point lemma caps the patterns per role structure at 2 (Lambda3, FW) or 4 (Lambda4), independent of M and h. So (SS) reduces to a pattern-free label-set sparsity statement (LS_theta). The simplest grouped averaging does cancel the corner-chain inflation exactly, but it can never push a cost below 1.

## Statements

Conventions. Design H7 or one tile of the multilevel tiling: stride S = 6272 sigma (sigma a power of 2), choices 0 <= xi < M, label columns x_e = x_0 + S(M r_e + xi_e). Here r is the rank in ANY curve satisfying (Hil): Hilbert, every CGK or RQC realization, any Q_1 curve. A candidate constraint is (label set J, choice-difference pattern), with m_E = 1. A "role structure" fixes which point of which label plays each geometric role, plus the sea row s where one is used. G = S^2 in mixed blocks and G = S^2/343 in zero-residue blocks. That is the divisor of the same-parity leg in H7 Lemma S3(c), which is unaudited. Put
 x_*(y) := M(sigma y^2/(2S) - 1) + 1.
By (Hil), x_*(y) is a lower bound for |x_f - x_e|/S whenever e, f have same-parity points whose rows differ by y.

LEMMA H (hyperbola; proved). Let N != 0. Let three distinct lattice points (x_k, y_k) lie on xy = N, with the x_k inside an interval of length L_x and the y_k inside an interval of length L_y. Then (2 Area)^2 = |P_x P_y|/|N| exactly, where P_x and P_y are the products of the pairwise x-differences and the pairwise y-differences. Hence |N| <= L_x^3 L_y^3/16. In particular, if both coordinates are confined to windows of w consecutive integers and |N| > (w-1)^6/16, there are at most 2 points.

LEMMA D (divisors in a window; proved). If N > 0 has three divisors in [x0, x0 + L] with x0 > 0, then N >= 4(x0/L)^3.

THEOREM M (pattern multiplicity per role structure; proved; curve-free, uses only (Hil), S | X and the normal forms).
 (a) Lambda3. Every role structure (vertex label, far label, parity of V) carries at most 2 patterns if
   (C3) x_*(G) > 4(M-1)^6.
  A label triple carries at most 24 patterns, and the two-label case (f = g) at most 1 pattern per role structure. Mixed blocks: x_*(G) ~ 1.23e11 M sigma^4, so (C3) holds for M <= 125 at sigma = 1. Zero-residue blocks: x_*(G) ~ 1.05e6 M sigma^4, so (C3) holds for M <= 13 at sigma = 1. The admissible range grows like sigma^(4/5). Full grid, S = 2^e: (C3) is M S^4/16 > 4(M-1)^6.
 (b) Lambda4. For every mixed four-support (side AB, diagonal CD) with fixed points, the patterns satisfy X(m+n) = -Y(p+q) != 0. Here X = x_B - x_A, m = x_C - x_A, n = x_D - x_B, Y = B_y - A_y, p = C_y - A_y and q = D_y - B_y. Each role structure carries at most 4 patterns if
   (C4) |Y(p+q)| > 32(M-1)^6 S^2.
  In the even-component case (b) of angles Theorem 2, |Y(p+q)|/S^2 >= x_*(G). In the odd-component case (c), |Y(p+q)|/S^2 > sigma G^2/(32 S): about 7.7e9 sigma^4 (mixed blocks) and 6.6e4 sigma^4 (zero-residue blocks). Both use H7 S3(c).
 (c) FW. Each role structure (ordered (e,f,g) and parity of A) carries at most 2 patterns. The condition |delta m|/S^2 >= x_*(S^2/2) ~ 3.1e10 M sigma^4 > 4(M-1)^6 holds for M <= 95 at every sigma >= 1. A triple carries at most 24 patterns, and the arity-2 case (g = e) at most 1 pattern per role structure.
 (d) 6PT-same (labels e, f, e'; role structure = which label is f, the pairing, and s; 18 in all). Patterns are the lattice points (x, x') = k(m, m')/g with g = gcd(m, m'), so:
   #patterns <= floor((2M-2) g / max(|m|,|m'|)) + 1 <= M,
  and at most 2 unless g >= 4 x_*(delta)^3 S/(|delta| (2M-2)^3). With |delta| >= S this threshold is about sigma^3 |delta|^5/(16 S^2) >= 1.5e10 sigma^6. Since g divides f's row gap b_f - a_f, every triple with row gap below the threshold carries at most 36 patterns.
 (e) 6PT-distinct. Each role structure carries at most 4 patterns when |delta m|/S < 4(x_*(delta)/(2M-2))^3 and the same holds with m'. This covers |delta| above about (16 S^2 h/sigma^3)^(1/5). Smaller delta is open.
 (f) R2s. No new bound. The archive's bound stands: 2 tau(|N|) patterns per pair, role structure and s.

COROLLARY S (what (SS) now requires; proved). Write c_J for the number of pattern constraints of Lambda3, Lambda4 and FW on the label set J. Under (C3), (C4) and the FW condition, c_J is bounded by constants independent of M and h. Crude role counts give c_J <= 32, 336 and 384 for |J| = 2, 3 and 4, so |J| c_J <= 1536.
 Hence, for every label set U,
  sum over E inside U of |J_E| m_E <= 1536 · #(candidate label sets inside U).
 So (SS) for these families follows from a statement in which patterns and M play no role, beyond which sets are candidates:
  (LS_theta) every connected U with |U| <= s1 contains at most (1+theta)|U| candidate label sets.
 Then beta0 <= 1536(1+theta). (SS) holds outright for every U with |U| <= 4. Stars (a near pair with t far ends) and books (a far pair with t near ends) have density below 3·24 = 72. These are the structures behind the polylog-cheap overlap steps flagged in hilbert_random_curve_other_families.md (gaps). So cheap overlaps never threaten (SS). Only "internal" label sets do, that is, sets beyond a spanning family of at most |U| - 1 sets.

IMPLICATION FOR THE MIXED-ARITY LEMMA. Theorem A(b) needs M > 8 calB(M) + B_Lambda3 + B_Lambda4 (+ residual). Before this note, a single triple could carry up to 4(2M-1) patterns, more than M, which made the inequality self-defeating at one triple. Under (C3), (C4) and the FW condition, single label sets contribute at most an absolute constant. With (LS_theta) and the (CC) of Theorem R, the lemma closes with M = floor(8 calB(M) + max(1536(1+theta), 5)) + 1, for the families Lambda3, Lambda4 and FW, and for 6PT within (d) and (e). R2s and the large-g part of 6PT still have unbounded single-set multiplicity bounds. The width stays O(h^2 log h) (b = 1), with a worse constant.

PROPOSITION A (exact grouped averaging and its limit; proved for CGK and RQC). Condition on Sigma_k (all choices at nodes of side > 2^k). For every gate g and every beta in [0, 2^k): sum over offsets o < 4^k of P_g(h(o)_1 = beta) = 2^k exactly. Let Pi be a Sigma_k-measurable family of (block, offset) pairs whose blocks contain no prefix rank, with each (gate, offset) pair used at most R times. Then the conditional expected number of pairs in Pi whose cell has first coordinate ≡ beta (mod 2^k) is at most 12 R 2^k. This exactly cancels the 2^|J(o)| corner-chain inflation of T5 for every family whose targets are fixed mod 2^k: Lambda3 (mod K), FW and 6PT-same. But the bound is at least 12 · 2^k > 1 as soon as Pi is nonempty. So no fixed-target grouping can verify a (CC) cost below 1/256. The missing input is anticoncentration on sparse offset sets.

HEURISTIC (labelled, not proved). Suppose overlap costs are of order eps ~ S^(-2) and tree costs of order mu. Then a geometrically realizable configuration with s labels and excess t is expected somewhere in a tile once h^2 mu^(s/2) eps^t >> 1. So B is at least the largest density among realizable configurations of size up to about 2 ln h/ln(1/eps). Bounded beta0 can therefore come only from deterministic geometry, a statement of the (LS_theta) type, which is consistent with CGK Proposition 7. Theorem M is the base case of such a statement, and T3 is the Theorem B case.

NOT PROVED: (CC) for any family; (LS_theta) for |U| >= 5; single-pair R2s multiplicity; 6PT-same for f row gaps above the threshold in (d); 6PT-distinct for small delta.

## Proofs

LEMMA H. Order x1 < x2 < x3. The x_k are distinct because y = N/x. Using y_k = N/x_k,
 det(P2-P1, P3-P1) = (x2-x1)(y3-y1) - (x3-x1)(y2-y1) = N (x2-x1)(x3-x1)(x3-x2)/(x1 x2 x3).
Swapping the roles of x and y maps the hyperbola to itself and changes only the sign, so also |det| = |N| |P_y|/|y1 y2 y3|. Multiply the two expressions and use x1 x2 x3 y1 y2 y3 = N^3:
 det^2 = |P_x P_y|/|N|.
The three points are not collinear: a line y = alpha x + beta meets xy = N where alpha x^2 + beta x - N = 0, which has at most 2 roots because N != 0, and a vertical line meets it once. So det is a nonzero integer, and |N| <= |P_x P_y|. For three numbers in an interval of length L, (u)(v)(u+v) with u + v <= L is at most L^3/4. Hence |N| <= (L_x^3/4)(L_y^3/4). For windows of w integers, L = w - 1.

LEMMA D. The cofactors y_k = N/x_k satisfy y1 - y3 = N(x3 - x1)/(x1 x3) <= N L/x0^2. Lemma H gives N <= (L^3/4)(N L/x0^2)^3/4, so N^2 >= 16 x0^6/L^6.

THEOREM M. In every case below a role structure fixes all rows, so every row difference is a constant. A pattern is a vector of slot differences. A difference between two distinct labels lies in the window M Δr + [-(M-1), M-1], which has length 2M-2. A sum of two such differences lies in a window of length 4M-4. Each pattern corresponds to exactly one lattice point described below, so counting lattice points counts patterns.
(a) Write F - V = (S x1, Y1) and G - V = (S x2, Y2). Here x1 and x2 are the slot gaps v->f and v->g, and Y1, Y2 are constant. Orthogonality S^2 x1 x2 + Y1 Y2 = 0 puts (x1, x2) on x1 x2 = N0 := -Y1 Y2/S^2.
 - N0 != 0: Y2 is odd, and Y1 = 0 would force X1 X2 = 0, which is impossible for distinct label columns.
 - F and V are same-parity points, so |x1| >= x_*(|Y1|) by (Hil) in the M-dependent form x_f - x_e >= S(M(Δr - 1) + 1), with Δr > sigma y^2/(2S) (because 16 · 28^2 = 2S/sigma).
 - G | Y1 (H7 S3(c)), so |Y1| >= G. Also |x2| >= 1, so |N0| >= |x1| >= x_*(G).
 - Lemma H with w = 2M-1 then gives at most 2 points under (C3).
 - Counting: 3 vertex labels, 2 far labels and 2 parities give 12 role structures, so at most 24 patterns per triple.
 - Two-label case: x1 = x2, so x1^2 = N0, and the window excludes 0 and holds only one sign. So at most 1 pattern.
 - Full grid: S^2 | Y1 and |x1| = lambda|a| > M S^4/16 by angles Theorem 1(iii).
 - Numbers: 6272^3/2 = 1.2336e11; dividing by 343^2 = 117649 gives 1.0486e6. M = 13 satisfies (C3) and M = 14 fails it at sigma = 1 in zero-residue blocks; M = 125 holds and M = 150 fails in mixed blocks.
(b) For any four points, C + D - A - B = (m+n, p+q) and D - C = (X + n - m, Y + q - p). Perpendicularity gives (I) X(m+n) + Y(p+q) = 0. Equal lengths give (II) u^2 + 2Xu + v(2Y + v) = 0, with u = n - m and v = q - p fixed.
 - p + q != 0 in both cases of angles Theorem 2: in (b) it equals 2(c - b_row) with Y(c - b_row) != 0, and in (c) S^2 | p+q != 0.
 - Lemma H applies to (X/S, (m+n)/S) with window lengths 2M-2 and 4M-4. Three points need |Y(p+q)|/S^2 <= (2M-2)^3 (4M-4)^3/16 = 32(M-1)^6. So under (C4) there are at most 2 pairs (X, m+n).
 - For each pair, (II) is a monic quadratic in u, so at most 2 roots, and (m, n) = ((s-u)/2, (s+u)/2). That gives at most 4 patterns.
 - If two points belong to one label, the corresponding window has a single value, and the same bound holds.
 - Lower bounds: in case (b), m + n = 2 Z0 != 0 and S | m+n, so |Y(p+q)|/S^2 = |X/S| |(m+n)/S| >= |X|/S >= x_*(|Y|). AB is a same-parity pair and G | Y. In case (c), H7 S3(c) gives |Y| > sigma S G/32 and G | (p+q).
(c) A PT with s = F has C - A = (X, delta) and S0 - A = (xi, m), with X xi = -delta m. FW needs xi ≡ 0 (mod S), and g is the owner of slot column x_f + xi, so xi = x_g - x_f.
 - So (X/S, xi/S) lies on a hyperbola with constant delta m/S^2, and both coordinates lie in windows of length 2M-2.
 - |xi| >= S gives |delta m|/S^2 >= |X|/S >= x_*(|delta|).
 - |delta| >= 2^(2 v2(S) - 1) 7^4 = S^2/2 (H7 S4, residual Prop E), so x_*(S^2/2) = M(sigma S^3/8 - 1) + 1 ~ 3.08e10 M sigma^4.
 - Lemma H gives at most 2 points. The case g = e gives xi = -X and X^2 = delta m, so at most 1 pattern.
(d) Residual Prop F(ii) gives X xi = -delta m and X' xi = -delta m' with the same xi. So (x, x') = (X/S, X'/S) is proportional to (m, m'), and since gcd(m/g, m'/g) = 1, (x, x') = k(m/g, m'/g) with k in Z.
 - The x-window has length 2M-2, so k lies in an interval of length (2M-2) g/|m|. Likewise for x'. That gives the first bound.
 - m and m' are measured from one sea row s, which lies outside the bulk rows, so they have the same sign and differ. Both are multiples of g, so max(|m|,|m'|) >= 2g, and the bound is at most M.
 - Also xi = -delta g/(S k), so the points (k, xi) lie on k xi = -delta g/S. The k-interval has length L <= (2M-2) g/|m|. Its smallest |k| satisfies k_min >= g x_*/|m|, so k_min/L >= x_*/(2M-2).
 - Lemma D: three patterns force |delta| g/S >= 4(x_*/(2M-2))^3, which is the stated threshold.
 - g | m - m' = b_f - a_f.
(e) Each PT pair (e,f) has x = X/S in a window of length 2M-2, and (x, xi) lies on x xi = -delta m/S. By Lemma D, if |delta m|/S < 4(x_min/(2M-2))^3, at most 2 values of X occur. The same holds for X'. The pattern (X, X', xi' - xi) is determined by X and X', so there are at most 4 patterns.
(f) The R2s patterns are values of X(g1) = -m delta/(g2 - g1) - g1/2 over the factorizations g1 g2 = N. This is not a hyperbola in two windowed coordinates. In the long-range regime (n+), g1 is close to g2, and neither Lemma H nor a curvature version gives a constant bound uniformly in m.

COROLLARY S.
 - Every E inside U has a candidate label set J inside U, so the sum is at most the sum over J of |J| c_J.
 - Role counts: Lambda3 and FW have at most 12 role structures on 3 labels; Lambda4 has 16 point choices times 6 side/diagonal splits, so 96 role structures on 4 labels; three-label Lambda4 has 72 and two-label Lambda4 has 6.
 - Sums: c_J <= 4 + 4 + 24 = 32 (|J| = 2), <= 24 + 24 + 288 = 336 (|J| = 3) and <= 384 (|J| = 4). So |J| c_J <= 1536.
 - Stars and books: each triple carries at most 24 patterns, and a star with t triples has t + 2 labels, so its density is at most 72t/(t+2) < 72.
 - Spanning bound: a connected U has a spanning sequence of at most |U| - 1 label sets, each adding a new label. Any density above 3 c_max needs label sets beyond that sequence.
 - Theorem R (T6(b)) uses (SS) only through sum over P in K of |J_P| <= beta0 |W(K)|, with K inside the candidate sets on W(K).

PROPOSITION A. Every local curve h_B is a bijection [0, 4^k) -> [0, 2^k)^2 by (Q1). So for every realization, #{o : h(o)_1 = beta} = 2^k, and taking expectations gives the identity. Given Sigma_k, the local curve of a block that contains no prefix rank has the CGK law with its gate (CGK Theorem 4(b)), whatever is revealed inside other blocks. A target ≡ beta (mod 2^k) inside a block whose corner is a multiple of 2^k requires h(o)_1 = beta. Linearity, grouping by gate (12 gates, or 12 RQC types), and at most R uses per (gate, offset) give the bound sum over g of R · 2^k. If Pi is nonempty, R >= 1, so the bound is at least 12 · 2^k = 6 S^2 > 1 at k = 2e - 1. The targets are fixed mod K = 2^(2e-1) because lambda K b ≡ 0 mod K (Lambda3), because delta is divisible by S^2/2 (FW), and because S | delta (6PT-same).

HEURISTIC. Expected count ~ n · C^s · mu^(tree) · eps^(t), with n <= h^2. This exceeds 1 whenever t ln(1/eps) + (s/2) ln(1/mu) < 2 ln h - O(s). So configurations of size up to about 2 ln h/ln(1/eps) appear wherever geometry allows them. CGK Theorem 4(d) makes disjoint blocks conditionally independent, which is Proposition 7's mechanism. This step is not a proof, because the realization probabilities of specific configurations are not computed.

## External results used

- No published theorem used. The divisor-window bound (Lemma D) is a classical elementary fact, re-proved here from Lemma H.
- Internal, unaudited, used for the H7 constants: H7 Lemma S3(c) (G | Y1, G | Y, G | p+q, |Y| > sigma S G/32) and Lemma S4 (FW divisibility); residual-note Propositions E and F (FW and 6PT normal forms); angles-note Theorems 1-2 (normal forms, p+q != 0, m+n != 0); CGK Theorems 4 and 1(b) (decoupling, Q1 bijection); T6 (Theorem R) of hilbert_random_curve_other_families.md.
- Internal, audited: inequality (1) and (Hil) as used in H7 and tiling Step 1.

## Checks

I checked by hand: the area identity of Lemma H (including the sign symmetry and non-collinearity), the reductions of Lambda3, FW, 6PT-same and 6PT-distinct to lattice points on xy = N or on lines, the Lambda4 equations (I) and (II) from the definitions of a mixed quadruple, the window lengths 2M-2 and 4M-4, the role counts, and the numerical constants (6272^3 = 2.4673e11, D_FW = S^2/2 = 19,668,992 sigma^2, the M ranges for (C3)).

Two scripts, run with py one at a time, each under 4 s and well under 1 GB, in scripts_hb4_cc_ss/:
- s1_hyperbola.py: exhaustive over N <= 40000. The largest N with 3 points in w x w windows is 12, 72, 240 and 600 for w = 4..7, against the bound (w-1)^6/16 = 45.6, 256, 977 and 2916. The identity (2 Area)^2 = |P_x P_y|/|N| holds exactly on 8562 triples, with 0 failures.
- s2_lambda4_6pt.py: brute force on the geometric definition, with planted mixed four-supports (S = 1, M = 2..4). Above the (C4) threshold, 937 instances have at most 2 solutions (bound 4). Below it, 1086 instances have up to 3. For 6PT-same, 19485 planted instances give 0 violations of floor((2M-2)g/max) + 1 and of <= M. The maximum seen is 6 (at M = 8), which confirms that 6PT-same multiplicity can grow with M.

These are sanity checks only. The claims are the proofs. Neither repository was touched, and no git command was run.

## Gaps

- (CC) is not proved for Lambda3, Lambda4, R2s, FW or 6PT. No summed (averaged) conditional cost bound below 1 was obtained at any stride. Proposition A shows that grouping with fixed targets, which does cancel the T5 inflation exactly, is limited to bounds of at least 12 * 2^k.
- (LS_theta), the pattern-free small-set statement, is unproved for |U| >= 5. Theorem B shows that it fails for locality-only arguments; T3 caps Theorem B in quadtree orders.
- R2s: single-pair multiplicity is still only 2 tau(|N|) per role structure and sea row (archive H7 S5). So (SS) can still fail at one R2s pair in principle when tau(|N|) is large relative to M.
- 6PT-same: for f row gaps above about 1.5e10 sigma^6, and for m'/m a ratio of small integers, a triple can carry up to M patterns per role structure (18M in all). The toy check shows growth with M (6 patterns at M = 8). 6PT-distinct with small delta is open.
- The constants in Corollary S (|J| c_J <= 1536) come from crude role counts. Most role structures probably cannot co-occur, through near/far scale separation and parity, but I did not prove this. If such dense sets existed, M would have to exceed about 1536(1 + theta).
- The H7 constants in (C3), (C4) and FW use H7 Lemma S3(c) (G | Y1, G | Y, G | (p+q), |Y| > sigma S G/32) and Lemma S4, which are unaudited. The full-grid versions use only the angles-note Theorems 1-2.
- The extreme-value statement that bounded beta0 must come from geometry is a heuristic. The realization probabilities of specific dense configurations are not computed.
- Nothing here is audited.

## Missing estimate

Two estimates remain. With them, Theorem R and Corollary S give M = floor(8 calB(M) + 1536(1+theta)) + 1 per tile and width O(h^2 log h), still b = 1.
(1) (LS_theta), deterministic, for every realization of the random curve (or with probability 1 - o(1)). Every connected set U of at most s1 = O(ln h/ln(1/eps)) labels contains at most (1+theta)|U| candidate label sets of Lambda3, Lambda4 and FW. Patterns no longer matter, by Theorem M. The first cases to settle are "double stars" generalizing Theorem B: m vertices whose far ends lie on common lines of direction z. Here the near partners pin both coordinates of the vertices to within O(sqrt(near rank gap)) of an affine function of lambda, so the T3 straddle count should apply. R2s pairs and large-g 6PT-same triples also need a single-set multiplicity below M - 1.
(2) (CC_Sigma), summed form. Fix a prefix W with known ranks and a label z. Then E[# tree constraints at z whose other labels avoid W | ranks of W] <= 1/256, and likewise for constraints meeting W in at least 2 labels and having at least 1 new label. By Proposition A this needs anticoncentration of the one-coordinate cell at SPARSE offset sets: sum over lambda <= Lambda of P(h(o_lambda)_1 = t_lambda) <= C sum over lambda of 2^-l, for line families o_lambda = (r + lambda a) mod 4^l, t_lambda = c + lambda K b. It must hold uniformly in z and with few lambda (Lambda = O(1) is typical when |b| is near sqrt(Lambda_max)). It also needs to average over the near partners g, which change a and b. T5 rules out every pointwise version.

## Next steps

- Prove (LS_theta) for Lambda3 double stars. Take m vertices whose far ends lie on lines of a common direction z, with near partners g at rank gap O(1). Use the near pair to fix both coordinates of each vertex up to O(1), then apply the T3(b) straddle count without the exact arithmetic progression of Theorem B.
- Cut the crude role counts in Corollary S. Near and far scale separation (near gap < 64h/(M S^4), far gap > M S^4/16 in the full grid) excludes two vertex choices on one triple only when M^2 S^8 >= 2048 h. Look for a parity or 7-adic exclusion instead.
- R2s single pairs: bound the number of factorizations g1 g2 = N with g1 near g2 (the (n+) pole region) whose X falls in one window. Treat the regimes (c), (s), (n-) and (n+) separately, with Lemma H on (g1, g2) and the U-spacing |X(U) - X(U')| ~ |m delta| |1/U - 1/U'|/2.
- 6PT-same: test whether the large-g triples (m'/m a ratio of small integers, f's row gap above 1.5e10 sigma^6) are killed by Prop F's 7-adic conditions. If not, turn them into pair constraints in the P budget.
- (CC_Sigma): attack sparse-offset anticoncentration through the two-parameter family (g, lambda) at a fixed vertex. The near partners vary a and b, so the offsets r + lambda a(g) are spread even when Lambda = O(1).
- Have a second reader audit Lemma H, Theorem M(a)-(e) and Proposition A. All proofs are short; the H7 constants depend on S3(c).

