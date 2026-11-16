# The energy bound (E) is false as stated

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (obstruction): (E) fails because of repeated vectors on vertex-disjoint edges (translation copies), which first appear in 6-cycles. They beat (E) by a factor equal to the relation range, the fixed-factor lemma cannot cap them, and they are the mechanism behind the cores of hilbert_random_curve_p_cores.md. In 4-cycles every degenerate solution sits at a common vertex: repeated vectors (capped), proportional vectors (ruled out for S >= 32 by a new lemma), or common legs with distinct q, which are rare at short gaps by a Pell reduction but carry an excess growing like log h at long gaps. Not audited yet.

# Result

## Status

obstruction

## Summary

(E) as stated is false. The cause is repeated vectors on vertex-disjoint edges ("translation copies"), which first appear in 6-cycles. They beat (E) by a factor equal to the relation range, the fixed-factor lemma cannot cap them, and they are the mechanism behind the Corollary 5 cores. In 4-cycles every degenerate solution sits at a common vertex. These are repeated vectors (capped), proportional vectors (ruled out for S >= 32 by a new lemma), or common legs with distinct q. The fixed-factor lemma does not cap common legs. They are provably rare at short gaps (a Pell reduction), and at long gaps they carry an excess kappa that grows like log h numerically.

## Statements

Notation follows hilbert_random_curve_p_cores.md. A constraint between labels a (odd row 2i_a+1) and b (even row 2j_b+2) has signed difference y = 2(j_b - i_a) + 1 and Y = |y|. It carries leg S q with q = M d + delta, |delta| <= M-1, d the rank gap. A_q is the set of odd Y with (Sq)^2 + Y^2 = square and L < h. B_k is the set of legs of slot k (all q in M d_k + [-(M-1), M-1]) in edge k's window. N_k = |B_k|. "Bulk configuration" means every signed y_k is positive. For a cycle i_{a1} j_{b1} i_{a2} ... of Gamma_C, the relation is the alternating sum of the c_k = (y_k - 1)/2 equal to 0.

THEOREM A (the relations are the geometric identities; proved). In a bulk configuration with Gamma_C connected, the Y-tuples that satisfy all cycle relations correspond one to one to cell configurations modulo the common diagonal shift (i,j) -> (i+s, j+s). An equality Y_k = Y_l between a + edge and a - edge that share a vertex j_b (edges i_a j_b and i_c j_b) holds exactly when i_a = i_c (and symmetrically j_b = j_d at a shared i_a).

THEOREM B (4-cycles; proved). In a 4-cycle of Gamma_C, every + edge shares a vertex with every - edge. So in a bulk 4-cycle, every solution of the relation that has an equality Y_k = Y_l is a coordinate coincidence at a common vertex, of one of three kinds:
(B1) Repeated vector, q_k = q_l. At a fixed label, role and side, a fixed vector (q,Y) has at most 2 partners (slots). This is capped as the fixed-factor lemma and b^- <= 4F^- cap it.
(B2) Proportional vectors, same primitive direction and different scale k. This is impossible for S >= 32 (Lemma P below).
(B3) Common leg, q_k != q_l with the same Y. The smaller half-factors then differ, so the fixed-factor lemma does not apply.

LEMMA P (no proportional partners; proved). Let S >= 32 be a power of two. At a fixed label, role and horizontal side, two P constraints whose vectors are multiples k1 v0, k2 v0 of the same primitive P vector v0 = (S e' O, |E^2 - O^2|) satisfy k1 = k2.

LEMMA Q (common legs at nearby gaps; proved). Let delta >= 1 and Y odd. Suppose Y is a leg of both S q and S(q+delta). Then f = L1 - L2 is even with 2 <= f < g := S delta. With z = 2Sq + g,
 (g^2 - f^2)(z^2 - f^2) = (2 f Y)^2.
Hence, for fixed S and D, the number of triples (q, delta, Y) with 1 <= delta <= D and L < h is at most C(S,D)(1 + log h). If g^2 - f^2 is a perfect square, the count for that (delta, f) is at most tau(f^2), independent of h.

THEOREM C ((E) fails, pointwise and on average; proved, with computer-found instances). Take the 6-cycle Sigma6 with labels a1, a2, a3 (odd-row side) and b1, b2, b3 (even-row side). Its ranks are r(a1) = 0, r(b1) = g, r(a2) = g - g'', r(b2) = g + g' - g'', r(a3) = g' - g'', r(b3) = g'. Its edges are a1b1, a2b1, a2b2, a3b2, a3b3, a1b3. Matched edges get equal deltas: a1b1 with a3b2 (gap g), a2b2 with a1b3 (gap g'), a3b3 with a2b1 (gap g''). Matched edges then have identical B-sets.
- For every diagonal, the number of relation solutions is at least N1 N2 N3.
- The right side of (E) is C (N1 N2 N3)^2 / rho, where rho is the relation range.
- So pointwise (E) fails whenever N1 = N2 = N3 = 1 and rho > C.
- On average over the diagonal, (E) fails whenever sum_T (N1N2N3)^2 < (rho/C) sum_T N1N2N3.
Instance at S = 32, M = 3, h = 2^18, half-windows 8 sqrt(gap): Y = 32775 carries legs q = 943, 2896, 3015 (gaps 314, 965, 1005). Over all T, sum N1N2N3 = sum (N1N2N3)^2 = 141, so the averaged (E) fails for every C < 141. Three more instances behave the same way. The failure factor grows like the window, so no constant C works as h grows.

COROLLARY D (what the fixed-factor lemma covers; proved). Repeated vectors at a common vertex are exactly what the fixed-factor lemma and slot counting cap. Repeated vectors on vertex-disjoint edges (which first occur in 6-cycles) are not capped by any per-vertex lemma. The Corollary 5 witness of hilbert_random_curve_p_cores.md is such a pattern: 6 constraints with only 2 distinct vectors, and (544,33,545) appears on four pairs, two of which are vertex-disjoint.

NUMERICAL (not proved). Let kappa be the excess of equal-Y common legs over shifted Y + 2tau (bulk Y >= h/8, all q != q').
- S = 8: kappa = 3.10, 3.79, 4.51, 5.28, 5.68 at h = 2^12, 2^14, 2^16, 2^18, 2^19.
- S = 32: kappa = 3.54, 4.94, 6.16, 7.34, 7.95 at h = 2^15, 2^17, 2^19, 2^21, 2^22.
- This is roughly linear in log h.
- The shifted counts show a bounded singular-series profile (0.53 to 2.05 times the mean for tau <= 30).
- Common legs with |dq| <= 7 number 1 to 29 over the whole range, which grows like log h, as Lemma Q predicts.

CONDITIONAL / HEURISTIC CONSEQUENCE (not proved). The conditional theorem of the p_cores note cannot be discharged with (E) as stated. It must be restated as (E-natural) plus a curve hypothesis (H_copy); see the missing estimate. A bulk pairing 4-cycle at a-c gap g has expected actual/random ratio about 1 + (kappa^2 - 1)/(8 sqrt g). That is bounded once g >> kappa^4, about (log h)^4, and Lemma Q handles bounded g. Intermediate gaps are open.

## Proofs

0. SETUP. A constraint between labels a, b with even row of b and odd row of a has y = 2(j_b - i_a) + 1 (the archive's role 0; role 1 swaps a and b). In Gamma_C it is the edge {i_a, j_b} with constant c = (y-1)/2.

Around a cycle i_{a1} j_{b1} i_{a2} j_{b2} ... the alternating sum of the c's is
 (j_b1 - i_a1) - (j_b1 - i_a2) + (j_b2 - i_a2) - ... = 0
identically in the coordinates. So every cycle relation is the geometric closing identity. Its arithmetic content is only that each y_k lies in +-A_{q_k}.

Every leg satisfies X^2 = (L-Y)(L+Y) = 4a(a+Y) >= 4(Y+1), since a >= 1. So X >= 2 sqrt(Y+1). Also Y = X^2/(4a) - a, where a = (L-Y)/2 is the smaller half-factor. For fixed a this is strictly increasing in X, so a fixed Y and a fixed a determine X.

1. THEOREM A. Assume the configuration is bulk and Gamma_C is connected, with 2u vertices. Fix y-values on the edges of a spanning tree. They determine every coordinate from one base coordinate i_0, and the base coordinate is a free shift. The remaining edges hold exactly when the cycle relations hold. Conversely, every cell configuration gives a relation-consistent tuple. Both maps are inverse to each other modulo the shift (i,j) -> (i+s, j+s), which leaves every j - i fixed.
For edges i_a j_b and i_c j_b, y_ab - y_cb = 2(i_c - i_a). In the bulk both are positive, so Y_ab = Y_cb exactly when i_a = i_c. QED.

2. THEOREM B. A 4-cycle i_a j_b i_c j_d has + edges i_a j_b and i_c j_d, and - edges i_c j_b and i_a j_d. Each + edge meets each - edge: i_a j_b meets i_c j_b at j_b and i_a j_d at i_a. The other + edge is symmetric. So any equality between a + and a - Y is at a common vertex, hence a coordinate coincidence by Theorem A.
(B1) Same q and same Y means the same vector. At label b with this role, the partner a must have i_a = j_b - c. Its rank gap is one of the at most 2 slot values of q on each side (archive (12)-(13)). Each rank holds one label, so there are at most 2 partners per side.
(B2) This is Lemma P.
(B3) Same Y with distinct q means distinct X, so by the monotonicity in section 0 the factors a are distinct. The fixed-factor lemma constrains only equal factors. QED.

3. LEMMA P. Suppose A = B - k1 v0 and C = B - k2 v0 at the same role and side (both odd-row points; the even-row case is identical), with k = k1 - k2 != 0. Then C - A = k v0.
- Columns. x_C - x_A = k S e'O = S(M(r_C - r_A) + xi_C - xi_A). So |r_C - r_A| <= (|k| e'O + M - 1)/M <= |k| e'O, using e'O >= 1 and |k| >= 1.
- Rows. 2(i_C - i_A) = k n with n = |E^2 - O^2|.
- Locality gives (|k| n/2)^2 < 16|r_C - r_A| <= 16|k| e'O, so |k| n^2 < 64 e'O.
- Now E != O, because the two have opposite parity. So n = |E-O|(E+O) >= E+O, and n^2 >= 4EO = 2S e'O, using E = S e'/2.
- Hence |k| * 2S e'O < 64 e'O, that is |k| < 32/S <= 1. This contradicts k != 0.
QED. (For S <= 16, |k| = 1 is not excluded for near-axis directions.)

4. LEMMA Q. Let q1 = q + delta and q2 = q. Then L1^2 - L2^2 = S^2 delta (2q + delta), and L1, L2 are odd because Y is odd and X is even. So f = L1 - L2 is even and positive. Also L1 + L2 > S(2q + delta), so f < S delta = g.
From 2 L2 = S^2 delta(2q+delta)/f - f:
 4 f^2 Y^2 = (g z - f^2)^2 - f^2 (z - g)^2, where g z = S^2 delta(2q + delta) and 2Sqf = f(z - g).
Factor this as the product of (g z - f^2 - f(z-g)) = (g - f)(z + f) and (g z - f^2 + f(z-g)) = (g + f)(z - f). This gives the identity.
Counting:
- Write g^2 - f^2 = m^2 D0 with D0 squarefree. Then m divides 2fY, and D0 divides (2fY/m)^2, hence divides 2fY/m. So z^2 - f^2 = D0 t^2 with t = 2fY/(m D0).
- The map (q, Y) -> (z, t) is injective.
- If D0 = 1, then (z - t)(z + t) = f^2 has at most tau(f^2) solutions.
- If D0 > 1, let eps > 1 be the fundamental solution of x^2 - D0 y^2 = 1 (Lagrange). Each alpha = z + t sqrt(D0), with z, t > 0 and norm f^2, can be written beta eps^n with n >= 0 and f <= beta < f eps. Its conjugate f^2/beta lies in (f/eps, f]. So beta = u + v sqrt(D0) with 0 < u <= f(eps+1)/2 and |v| < f eps/(2 sqrt D0), which leaves finitely many beta.
- Since alpha < 2z <= 2(2h + g), n <= log(2(2h+g)/f)/log(eps), and log(eps) >= log(1 + sqrt 2).
- Summing over delta <= D and even f < S delta gives C(S,D)(1 + log h).
QED.

Consequence: two labels at rank gap g on the same side of b have |q_ab - q_cb| <= M g + 2(M-1). So all distinct-q common legs that short-gap pairings can use come from at most C(S, M g + 2M)(1 + log h) triples.

5. THEOREM C.
- Rank gaps. |r(b1) - r(a1)| = |r(b2) - r(a3)| = g, |r(b2) - r(a2)| = |r(b3) - r(a1)| = g', and |r(b1) - r(a2)| = |r(b3) - r(a3)| = g''. Every later label is the b. So with equal deltas, matched edges have equal slot sets. Their windows depend only on the gap, so the B-sets are identical.
- Solutions. Assign Y1 to a1b1 and a3b2, Y2 to a2b2 and a1b3, and Y3 to a3b3 and a2b1. The alternating sum is c1 - c3 + c2 - c1 + c3 - c2 = 0. That gives N1 N2 N3 solutions.
- Bound. The (E) right side is C times the product over the six edges of N_k, divided by rho, which equals C (N1N2N3)^2/rho. Then (E) forces N1N2N3 <= C (N1N2N3)^2/rho, which fails when N1 = N2 = N3 = 1 and rho > C. The averaged statement is the same inequality summed over T.
- Range. Varying one Y_k alone already moves the sum over its whole window, so rho is at least the largest window, which is at least 141 in the instance.
- Instance. copy6.py found it. All N_k lie in {0,1} on the support, so the two sums agree (141 = 141). Three more instances (Y = 33033, 33075, 33165) give equal sums 123, 181, 93.
QED (computer-assisted for the instances only; the inequality is general).

6. COROLLARY D. In a 2l-cycle, the + edge e_1 and the - edge e_4 are vertex-disjoint only when 2l >= 6. The fixed-factor lemma and the slot count are per-vertex statements. The Corollary 5 data (p_cores note, item 5) put q = 17 with Y = 33 on pairs (r, r+5) and (r+6, r+11) at delta = 2, and on (r, r+6) and (r+5, r+11) at delta = -1. So the vector (544,33,545) appears on vertex-disjoint pairs.

7. IMPLICATION FOR CORES (heuristic, labelled). The first moment is a sum over cell configurations of the curve probability times the product of the leg indicators. A copy edge costs the curve's one-dimensional coincidence probability, about 1/w. A genuine edge costs about N/w. In the bulk N << 1, so copies dominate. The archive's b^- <= 4F^- (applied on both sides) gives deg(v) <= 8 F_v. So a K0-core needs at least K0/8 distinct factors at each vertex, but possibly only O(K0) distinct vectors in total. Cores built from copies are therefore controlled by the curve, not by arithmetic. At short gaps under Model K, copy events have probability of order 1, which matches the 3-cores that appear with high probability at M = 3.
For a pairing 4-cycle at a-c gap g: Delta = i_c - i_a takes about 8 sqrt(g) values. The value Delta = 0 is weighted kappa^2 relative to the others, which gives the ratio 1 + (kappa^2 - 1)/(8 sqrt g).

## External results used

- Euclid parametrization and its 2-adic form (archive T1, audited).
- Fixed-factor lemma, finite-factor theorem and slot count (12)-(13) of continuation_hilbert_factor_one_choices.md (audited).
- Lagrange: x^2 - D y^2 = 1 has a solution with y > 0 for every nonsquare D > 0. This is standard and was not looked up.
- Archive T5: b^- <= 4F^- (audited), used only in the heuristic section.

## Checks

Scripts are in scripts_hb4_e_param/:
- pair_corr.py: T1 enumerator and the shift test.
- pair_corr2.py: per-tau counts in the bulk.
- pair_scale.py: kappa against h.
- pair_small.py: the |dq| <= 7 band.
- close_q.py: checks the Lemma Q identity on every close-q common leg found, with 0 failures, and counts them (S = 32: 1, 3, 9, 12, 15 at h = 2^14 to 2^21).
- copy6.py: the Theorem C instances.
Each ran with py -B in under 3 seconds and well under 1 GB. Neither repository was touched.

By hand I checked:
- the cycle identity and Theorem A;
- the 4-cycle adjacency argument;
- the Lemma P inequality chain, including n^2 >= 2S e'O;
- the factorization in Lemma Q, the bound f < S delta, the reduction to z^2 - D0 t^2 = f^2, and the unit-box class count;
- the rank and gap bookkeeping of Sigma6 and the matching cancellation;
- the Corollary 5 copy pattern, read off the p_cores note.

## Gaps

- The corrected bound (E-natural), which counts solutions with no repeated vectors and no common legs against the random model, is not proved. The only evidence for it is the bounded singular-series profile of the shifted counts.
- kappa growing like log h is numerical only (S = 8, h up to 2^19; S = 32, h up to 2^22). Neither its growth rate nor an upper bound for slot-restricted pairs is proved. The divisor-moment explanation is heuristic.
- The constant C(S,D) in Lemma Q is not uniform in D: the class bound involves the fundamental unit. So Lemma Q covers only bounded pairing gaps, and gaps between O(1) and about (log h)^4 are not covered.
- The curve-side hypothesis for copy patterns (H_copy), a one-dimensional local-limit bound for coincidences of displacement combinations under Model K, is not proved. The bound degree <= 8 x (distinct factors at a vertex) does not bound the number of distinct vectors per core, so bounded K0 does not follow.
- Near-diagonal configurations (signed y of both signs) are not classified. Theorems A and B assume the bulk. Off the bulk, Y_k = Y_l can also come from y_k = -y_l, which is a different coincidence.
- The Theorem C instances and all numerics come from one implementation (pair_corr.py and the T1 enumerator). The T1 enumerator matches the audited normal form but was not re-checked against brute force in this session. The Pell identity was checked on every close-q common leg found (0 failures).
- No width improvement. No statement about the other H7 families. Nothing here is audited.

## Missing estimate

Restate the energy bound in two parts.

(E-natural): fix a configuration and an equality pattern pi, meaning the classes of edges that carry the same vector (q,Y). The number of relation solutions with exactly pattern pi, in which distinct classes carry distinct vectors, is at most C^{R_pi} times the product over classes of N_c, divided by the product of the ranges of the R_pi relations that pi leaves independent. Repeated vectors at a common vertex are capped by slots and the fixed-factor lemma, and proportional ones are excluded by Lemma P (S >= 32).

(H_copy), the curve side: under Model K, each vertex-disjoint repeated vector (an equality j_b - i_a = j_b' - i_a' with matched rank gaps) costs at most C 4^{v_4(x)}/sqrt(x), conditionally on the history, where x is the smallest rank gap involved.

You also need a uniform form of Lemma Q for |dq| up to M (log h)^4, or a proof that kappa(slot pair) <= (log h)^{O(1)}, to close the intermediate pairing gaps.

Even with all three, bounded K0 needs one more step. The core first moment must beat copy-heavy patterns, whose arithmetic cost is only (genuine cost)^{#distinct vectors}. That requires bounding the number of distinct vectors per locality patch in terms of K0, or a curve estimate that kills copy-heavy patches.

## Next steps

- Rewrite the conditional statement of hilbert_random_curve_p_cores.md with (E-natural) plus (H_copy), and recount Proposition 7 by equality pattern: copy edges do not reduce the arithmetic count.
- Test (H_copy) numerically under Model K. Measure the frequency of matched 6-cycles and of rank-translated repeated vectors against 1/sqrt(gap). Separately, measure the share of 3-core and 4-core edges that are copies; the Corollary 5 witness is 4 of 6.
- Prove a uniform Lemma Q. Count the classes of z^2 - D0 t^2 = f^2 by ideals of norm f^2 (at most tau(f^2) times a bounded factor) instead of the unit box, so that the bound is C(S) D^{2+o(1)} log h.
- Try to prove kappa <= (log h)^{O(1)} for slot-restricted pairs. Bound the sum over Y of n(Y)^2 by the second moment of the divisors of Y^2 in [Y - SQ, Y], and give a lower bound for the mean from the T1 sum.
- Classify near-diagonal degenerate solutions (y_k = -y_l). The densest 3-cores sit at Y < 2^8, where Theorems A and B do not apply.

