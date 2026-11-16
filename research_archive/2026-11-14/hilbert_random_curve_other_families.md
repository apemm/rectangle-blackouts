# The angle, mixed and residual families under a random curve

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (partial, with an obstruction): no with-high-probability bound on the induced density of Lambda3, Lambda4, R2s, FW or 6PT under a random curve. Proved: the barrier configurations on file cannot embed in any quadtree order, and random curves cut the frequency of exact translation atoms from at least 1/16 to at most (3/4)^k. An obstruction no randomization removes: continuity forces corner chains, so pointwise conditional anti-concentration fails by a power of the scale. Conditional on subcritical costs (CC) and sparse small sets (SS), B <= max(beta0, 5) with probability 1 - O(1/h). Not audited yet.

# Result

## Status

obstruction

## Summary

Target not reached. I did not prove a with-high-probability bound on the induced density of Lambda3, Lambda4, R2s, FW or 6PT under a randomized curve. Proved instead: (1) A randomized king-continuous Hilbert-type curve (RQC) keeps locality (1) and Lemma 0 exactly, so every locality-only H7 tool carries over. (2) Both barrier configurations on file fail to embed in any quadtree order, random or not. Theorem B is capped at m <= 68 (density <= 100.5), its sub-configurations at density O(log(h/S^4)), and the Prop 4 star at 10 angles. (3) RQC cuts the frequency of exact translation atoms from at least 1/16 to at most (3/4)^k. (4) An obstruction that no randomization removes: continuity forces corner chains. In every corner-entry Hilbert-type curve, pairs of equal base-4 rank digits 00 or 33 force equal coordinate bits, and block starts are dyadically resonant with the 2-adic filters of all five families. So pointwise conditional anticoncentration, which the random-hypergraph route needs, fails by a power of the scale. (5) A conditional theorem. If the conditional costs are subcritical (CC) and small sets are sparse (SS), then B <= max(beta0, 5) with probability 1 - O(1/h), and M > 8 calB(M) + max(beta0, 5) suffices.

## Statements

Conventions. Full-grid language unless stated. A tile is a 2^n x 2^n cell square, and each cell is a label. Rank r is in [0, 4^n). Each rank has base-4 digits d_n ... d_1, where d_j is the position, in the order of its level-j ancestor square, of the child that contains the cell. The H7 versions follow through (Hil) with row step 28 and S = 6272 sigma. B, m_E and calB are as in Theorem A of hilbert_lambda_anticoncentration.md. "Quadtree order" means any curve whose aligned rank blocks of length 4^k are aligned squares of side 2^k. The deterministic Hilbert curve and RQC are both quadtree orders.

DEFINITION (RQC, the random king-continuous quadtree curve). Each aligned square Q of side at least 2 carries a type tau_Q = (alpha, omega), an ordered pair of distinct corners of Q, so there are 12 types. Given tau_Q, Q draws its configuration independently of everything else:
- Order. The first child is the quadrant at alpha and the last child is the quadrant at omega. The two middle quadrants come in either order, with probability 1/2 each.
- Transition points. Index the corner points of the four quadrants as a 3 x 3 grid. Put P0 = alpha and P4 = omega. Choose (P1, P2, P3) uniformly among the triples with P_t shared by children t and t+1 and with P_{t-1} != P_t for t = 1..4. The second condition is dropped when the children are single cells.
- Child types. Child t gets type (P_{t-1}, P_t) in its own local corners.
The root type is arbitrary. All 24 triples of conditions are satisfiable (proof, step 1).

T1 (exact locality and transfer; PROVED). For every realization of RQC:
(a) H is a bijection. Every aligned rank block of length 4^k maps onto an aligned square of side 2^k. Each square's sub-curve starts at its alpha corner cell and ends at its omega corner cell.
(b) Consecutive cells are king-adjacent.
(c) Lemma 0 holds verbatim: |Delta coordinate| >= 2^m with m >= 1 forces t > 4^(m-1). Inequality (1) holds verbatim: max(Di^2, Dj^2) < 16|Dr|.
Consequence. Every archive statement whose proof uses only (1), Lemma 0, "aligned rank blocks are aligned squares" and the slot structure x = S(M r + xi) holds for every realization. This covers:
- the H7 tool (Hil), and hence the H7 completeness reduction to the six families;
- angles_mixed Theorems 1 and 2 and their thresholds, and Proposition T;
- the factor-one and finite-factor theorems;
- Step 1 of the tiling assembly;
- Theorems A to D and Lemma G of the residual note, and the FW, 6PT-distinct and Lambda thresholds.
Theorem A, the mixed-arity choice lemma, does not involve the curve.

T2 (Markov property and isolation chain bound; PROVED). Let Q be an aligned square, and let F_Q be the sigma-algebra of the configurations of all squares outside the subtree of Q. Then F_Q determines:
- tau_Q and base(Q), where base(Q) is the rank of Q's first cell;
- the rank of every cell outside Q;
- the cell at every rank outside Q's rank block.
Conditional on F_Q, the configurations inside Q follow the RQC law with root type tau_Q.
Chain bound. Let w_1, ..., w_s be fixed cells. For k >= 2, let Q_k be an aligned square that contains w_k and none of w_1, ..., w_{k-1}. Let E_k be an event determined by the ranks of w_1, ..., w_k, with P(E_k | F_{Q_k}) <= p_k almost surely. Then P(E_2 and ... and E_s) <= p_2 ... p_s.

T3 (straddle lemma and the two barriers; PROVED; holds in every quadtree order, random or not).
(a) Straddle lemma. If |r_f - r_v| >= 4^l, then v and f lie in different aligned squares of side 2^l. Hence some coordinate of v and f lies in different 2^l-intervals.
(b) Theorem B of hilbert_lambda_anticoncentration.md. Its full configuration with m pairs can be realized as the relative ranks of a quadtree order only if m - 1 <= 67. So its weighted density 1.5(m-1) is at most 100.5, for every h, S and M. Theorem B needs m - 1 >= 12(h-1)/(M^3 S^4) - 2, so it fails in every quadtree order once h > 69 M^3 S^4/12 + 1.
(c) Sub-configurations. Every realizable sub-configuration of Theorem B with k chosen pairs has k - 1 <= 67(1 + floor(log2(m-1))). Its density is therefore at most 100.5(1 + log2(m-1)), which is O(log(h/(M^3 S^4))), against order h/(M^3 S^4) under locality alone.
(d) Proposition 4 of hilbert_angles_mixed_thresholds.md, the star at one vertex. It can be realized only with Lambda <= 10 angles.
How randomness enters: it does not. These barriers are beaten by quadtree structure, not by randomness.

T4 (RQC breaks exact atoms; PROVED). Let N12(o) be the number of base-4 digits of o equal to 1 or 2.
(a) Let Q be a square of level l, and condition on F_Q. For every offset o < 4^l and every cell z, the cell at rank base(Q) + o equals z with probability at most 2^(-N12(o)). The same bound holds in the cell view: P(offset of cell c in Q = y | F_Q) <= 2^(-N12(y)).
(b) For every gap d >= 1, every vector v, and k0 with 4^k0 <= d:
 E #{r : H(r+d) - H(r) = v} <= q^2 (3/4)^k0.
For the deterministic Hilbert curve, Lemma H3 gives at least q^2/16 ranks with H(r+4^k) - H(r) = ±(2^k, 0) for one sign. So the exact translation atoms behind the census hubs have expected frequency at most (3/4)^k in RQC. By Markov's inequality, P(frequency >= 1/16) <= 16 (3/4)^k.

T5 (corner-chain obstruction; PROVED; holds for every probability law on king-continuous corner-entry quadtree curves: Hilbert, RQC, or any other randomization).
(a) Bit equality. If d_j(r) = d_(j-1)(r) and this digit is 0 or 3, then bits j-1 and j-2 of both coordinates of H(r) are equal. This holds for every realization.
(b) Restricted support. So H(r) lies in a fixed set R(r) with |R(r)| = 4^(n - |J(r)|), where J(r) = {j in [2, n] : d_j = d_(j-1) in {0, 3}}. Each coordinate takes at most 2^(n - |J(r)|) values. Hence max_z P(H(r) = z) >= 4^(-(n - |J(r)|)), and each one-coordinate atom is at least 2^(-(n - |J(r)|)).
(c) The same holds inside any square Q of level l given F_Q, with J computed from the offset o. So no bound of the form P(H(r)_c = x | F_Q) <= C 2^(-l) holds for all offsets. Over a uniform offset, |J(o)| >= l/32 except on a fraction at most exp(-l/128). Also E 2^|J(o)| grows like ((5 + sqrt 17)/8)^l = 4^(0.0947 l).
(d) Dyadic resonance. The cell at rank beta 4^m is the entry corner of its level-m block, so both of its coordinates are congruent to 0 or -1 (mod 2^m). Among any 5 such ranks, two have both coordinate differences divisible by 2^m. The random-row heuristic gives this event probability 4^(-m).
All five families, and P, impose 2-adic divisibility of this kind on coordinate differences:
- Lambda3 and Lambda4: G = 2^(2 v2(S)) 7^(2 v7(S)) divides Y1;
- FW: 2^(2 v2(S) - 1) 7^4 divides delta;
- 6PT-same: S divides delta;
- R2s: Theorem C fixes (v2 delta, v2 T);
- P: E = S e'/2.
Therefore the isolation-plus-pointwise-anticoncentration method that a random-hypergraph proof of (G) needs loses a power of the scale, in every such curve.

T6 (reduction of the target to two hypotheses; PROVED as stated).
(a) Deterministic part. For any hypergraph H of constraints with m_E = 1:
 B(H) <= max over connected sub-hypergraphs K of (sum over P in K of |J_P|)/|W(K)|,
where W(K) is the label set of K. Also
 sum over P in K of |J_P| <= 2(|W| - 1 + t(K)), with excess t(K) = sum over P in K of (|J_P| - 1) - (|W| - 1) >= 0.
(b) Conditional theorem R. Let H be the union of the Lambda3, Lambda4, R2s, FW and 6PT candidate hypergraphs of one tile, with n <= h^2 labels. Each family has m_E = 1 (Theorem A(b) and Lemma G). Assume the following.
- (CC) Conditional costs. There are numbers c(P | P_1..P_(i-1)) >= 0 such that P(all of P_1..P_e present) <= the product of the costs, for every sequence in which each P_i meets the labels of the earlier ones. For every prefix and label z, the costs of the "tree" constraints P that contain z and no other prefix label sum to at most mu. The costs of the "overlap" constraints that contain z and at least one other prefix label sum to at most eps. Also 128 max(mu, eps) <= 1/2.
- (SS) Small-set sparsity. Every connected K with |W(K)| <= s1 = ceil(6 ln h / ln(1/(128 eps))) has sum of |J_P| <= beta0 |W(K)|.
Then P(B(H) > max(beta0, 5)) <= C/h. With Theorem A(b), every tile has a choice vector that avoids P and the five families once
 M > 8 calB(M) + max(beta0, 5).
Over the fewer than 2352 ln h tiles of C4', a union bound costs a factor O(log h) in the failure probability.
Sigma. (CC) holds heuristically when sigma >= 0.0072 ln h, which is within the sigma0 = C log h that the tiling already uses for P. This rests on the random-row heuristic for the Lambda3 mean, about 2e-7 (ln h)^2/sigma^2, and T5 shows that this heuristic is not a valid conditional bound in any Hilbert-type curve. With beta0 <= 5, the conditional width is the C4' bound O(h^2 log h), b = 1, so no gain over what is on file.
Status. (CC) and (SS) are unproved for every family. T5 blocks the natural route to (CC).

NUMERICAL (sanity only, not claims). Exact dynamic programming over RQC, cross-checked by Monte Carlo:
- The one-coordinate atom of the cell at a fixed offset decays like 2^(-0.53 k).
- The atom of the x-displacement at gap d = 4^k decays like d^(-0.27) (worst type at the split level), against the d^(-1/2) that the families need.
- P(dx = 0 mod 2^(k-1)) is 1.5 to 4.7 times its uniform value and grows with k.

## Proofs

1. T1.
Satisfiable triples. Take the order (q1, q2, q3, q4) and the sets S12, S23, S34 of shared corner points. Every pair of quadrants shares the center. Edge-adjacent pairs also share one midpoint of the parent's boundary, and that midpoint is a corner point of exactly those two quadrants.
- If q2 and q3 are edge-adjacent, take P2 = their midpoint. It differs from every point of S12 and S34.
- If q2 and q3 are diagonal, then q1 and q4 are the other diagonal pair. So q1 is edge-adjacent to q2, and q3 to q4. Take P1 and P3 to be the midpoints and P2 = center.
Children never get entry = exit: the outer corner alpha is not a shared point, and the middle children have P_{t-1} != P_t by construction.

Induction on the side. A 2x2 square: the order alpha, mid, mid, omega visits 4 mutually king-adjacent cells, starting at alpha and ending at omega. For side 2s with s >= 2:
- By induction, child t's sub-curve runs from its corner cell at point P_{t-1} to its corner cell at point P_t.
- At a shared point p = (px, py), in units of s, quadrant q's corner cell is (px(s-1) + qx, py(s-1) + qy). Two quadrants sharing p therefore have corner cells at L-infinity distance max |q - q'| <= 1.
- So consecutive children connect by a king step.
- The first cell is child 1's corner at P0 = alpha, which is the alpha corner cell of the square. The last cell is the omega corner cell.
- Each child is an aligned square and is visited in one contiguous rank block. This gives (a) and (b).

(c) Let 4^k be the least power of 4 with 4^k >= t.
- The two ranks lie in one aligned 4^k-block or in two consecutive ones.
- Consecutive blocks contain king-adjacent cells, namely the last cell of one and the first cell of the next. So the two aligned 2^k-squares fit in a box of side 2^(k+1).
- So every coordinate difference is at most 2^(k+1) - 1.
- If |D| >= 2^m, then m <= k. If k >= 1, then t > 4^(k-1) >= 4^(m-1). If k = 0, then t = 1 and |D| <= 1, which contradicts m >= 1.
- For (1): D^2 < 4^(k+1) = 16 * 4^(k-1) < 16t.
The transfer clause holds because each cited proof uses the curve only through these facts. I checked this by reading the proofs for (Hil), angles Theorem 1, the factor-one equation (3) with |z| < 4 sqrt(q), tiling Step 1 and residual Theorem D. Each uses only (1), Lemma 0, aligned blocks and slot ranks.

2. T2.
Realize RQC with independent uniforms U_Q, one per aligned square. Put kappa_Q = f(tau_Q, U_Q). Then tau_Q is a function of kappa of Q's parent, so it is F_Q-measurable. So is base(Q) = base(parent) + 4^level(Q) * pos(Q).
A cell c outside Q has rank sum over ancestors A of c of 4^(level(A)-1) * pos_A(c). No ancestor of c lies in the subtree of Q, so its rank is F_Q-measurable.
Rank view: the root-to-cell path of a rank outside Q's block never enters the subtree of Q, by induction along the path.
The variables inside the subtree of Q are independent of F_Q, and they generate the subtree with root type tau_Q.
Chain bound. For j < k, the event E_j depends on the ranks of w_1, ..., w_j, which all lie outside Q_k, so E_j is F_{Q_k}-measurable. Then
 P(E_2 ... E_s) = E[1_{E_2 ... E_(s-1)} P(E_s | F_{Q_s})] <= p_s P(E_2 ... E_(s-1)).
Induct on s.

3. T3.
(a) An aligned 2^l-square is a single rank block of length 4^l, so ranks inside it differ by less than 4^l.

(b) Write P_p = (i0 - pMK, j0 - pMK). Adjacent pairs have rank gap floor((p+1)a/M) - floor(pa/M) >= a/M - 1.
- Let l be the largest integer with 4^l <= a/M - 1. Then 2^l > sqrt(a/M - 1)/2.
- The definition of m, ((m-1)MK + 1)^2 < 4((m-1)a/M - 2), gives a/M - 1 > (m-1)M^2K^2/4, using MK >= 32. So 2^l > sqrt(m-1) MK/4.
- By (a), every adjacent pair changes its 2^l-interval in i or in j.
- Both coordinates are monotone along the progression. So the number of changes in one coordinate is at most (m-1)MK/2^l + 1 < 4 sqrt(m-1) + 1.
- Hence m - 1 < 8 sqrt(m-1) + 2, so sqrt(m-1) < 4 + sqrt 18 < 8.25, and m - 1 <= 67.

(c) Choose indices p_1 < ... < p_k with gaps g_i, so sum g_i <= m - 1. The rank gap of pair i is at least g_i(a/M - 1) >= g_i (m-1) M^2 K^2/4.
- Group the pairs by g_i in [2^t, 2^(t+1)). Every pair in group t needs a separating line from the grid of spacing L > sqrt(2^t (m-1)) MK/4. The minimum over the group is a grid that contains all the coarser grids.
- The coordinate intervals of distinct pairs are disjoint, so distinct pairs need distinct lines in each coordinate.
- So |G_t| <= 2(4 sqrt((m-1)/2^t) + 1). Also |G_t| <= (m-1)/2^t.
- With x = (m-1)/2^t, min(x, 8 sqrt x + 2) <= 67.
- Summing over t = 0..floor(log2(m-1)) gives the bound on k - 1. Every ordered pair of chosen indices still gives a constraint, so the density is 1.5(k-1).

(d) Here M = 1. Consecutive far ends f_lambda and f_(lambda+1) have rank gap a, equal j and i-difference K = S^2/2.
- With 4^l <= a < 4^(l+1), 2^l > sqrt(a)/2.
- The i-interval changes number at most (Lambda-1)K/2^l + 1 < (Lambda-1) S^2/sqrt(a) + 1 <= (Lambda-1) sqrt(8/Lambda) + 1, because a >= Lambda S^4/8.
- (a) requires Lambda - 1 changes, so (Lambda-1)(1 - sqrt(8/Lambda)) < 1. This fails at Lambda = 11, where the left side is 1.47, and the left side increases for Lambda >= 8.

4. T4.
(a) Fix o and z. Inside Q, walk down the path of offset o.
- At level j, the current square's configuration is fresh given everything above it (T2).
- If d_j is 1 or 2, the child at position d_j is one of two distinct middle quadrants, each with probability exactly 1/2, decided by the order coin. So the probability that it matches z's quadrant is at most 1/2.
- Put X_j = 2^(number of middle levels so far) * 1{all quadrants so far match z}. This is a supermartingale, so E X <= 1 and P(match) <= 2^(-N12(o)).
- The cell view is the same: digit y_j in {1, 2} needs c's quadrant to be a middle one placed at position y_j, which has probability at most 1/2.
(b) Fix r. Let L be the least level at which r and r+d share a rank block of length 4^L. They lie in distinct level-(L-1) blocks, and L - 1 >= k0 because 4^k0 <= d.
- Sum over the aligned squares Q of level L-1. On the event that the block of r+d maps to Q, H(r) lies outside Q and is F_Q-measurable. Also r + d - base(Q) = (r+d) mod 4^(L-1).
- By (a), P(H(r+d) - H(r) = v) <= 2^(-N12((r+d) mod 4^(L-1))) <= 2^(-N12((r+d) mod 4^k0)).
- Average over r. The bottom k0 digits of r + d are uniform, and the sum over o < 4^k0 of 2^(-N12(o)) is (1 + 1/2 + 1/2 + 1)^k0 = 3^k0. This gives q^2 (3/4)^k0.

5. T5.
(a) Let N_j be the level-j square that contains H(r).
- If d_j = 0, then N_(j-1) is the quadrant at N_j's entry corner alpha. Its sub-curve starts at the same cell, which is its own alpha-direction corner, so its entry corner has the same direction.
- If also d_(j-1) = 0, then N_(j-2) is the alpha-quadrant of N_(j-1). Both bits j-1 and j-2 of each coordinate equal the alpha bits.
- Digit 3 is the same argument with omega: the last child ends at the parent's last cell.
- Squares are aligned, so "quadrant bit" equals "coordinate bit".
(b) The equalities link disjoint pairs of adjacent bit positions into paths. That leaves n - |J| free bits per coordinate, and support size bounds the maximum atom from below.
(c) Given F_Q, the cell is the corner of Q plus a point of R(o).
- The indicators for even j are independent Bernoulli(1/8) variables over floor(l/2) pairs. Chernoff's bound P(Bin(m,p) <= mp/2) <= exp(-mp/8) gives the tail.
- E 2^|J| is u^T T^(l-1) 1, with T[a][b] = (1/4)(2 if a = b in {0, 3}, else 1). Its Perron root solves 16x^2 - 20x + 2 = 0.
- The rank-view tree costs that (CC) needs are P(H(r_v + d)_c = target | F_B). They inherit the factor 2^|J(o)| at targets compatible with R(o) and are 0 elsewhere. A uniform bound must take the maximum, so it loses that factor.
(d) The first cell of a level-m block is its entry corner. Pigeonhole over the 4 corner directions gives the pair. The list of 2-adic filters is quoted from H7 S3(c), residual Propositions E and F and Theorem C, and the P normal form.

6. T6.
(a) The constraints inside U form components K_1, ..., K_c, and each is a connected sub-hypergraph. So the maximum ratio over U is at most the maximum over connected K.
For connected K, |K| <= sum of (|J_P| - 1) = |W| - 1 + t. So
 sum of |J_P| = (|W| - 1 + t) + |K| <= 2(|W| - 1 + t).

(b) Exploration count. Fix a root label. Explore K by breadth-first search: process the labels in order of discovery, and at each processed label add the constraints of K that contain it and are not yet added, in a fixed order. Each step is "tree" or "overlap" relative to the labels found so far.
- The sequence is determined by the composition of e into N <= 3e + 1 processed labels, at most (3e+1) 2^(4e) <= 2^(6e) choices, and by the constraints chosen.
- Sum over the last constraint first, using (CC). Choosing which steps are overlap steps costs C(e,x) <= 2^e.
- So E[number of present explorations with e steps and x overlap steps] <= n (128 mu)^(e-x) (128 eps)^x.

Component size. If some component has more than s0 = 12 log2 h labels, the exploration prefix that first exceeds s0 labels has e >= s0/3 steps. The expected count is at most n * sum over e >= s0/3 of (e+1) 2^(-e) = o(1/h).

Density witnesses. Suppose B > beta >= max(beta0, 5). By (a), some connected K has sum of |J_P| > beta |W|.
- By (SS), s = |W| > s1.
- By (a), t > (beta/2 - 1) s >= 3s/2. Each overlap step adds at most 3 to t, so x > s/2. Also e <= s + 3x.
- The expected count is at most n * sum over s1 < s <= s0 and x > s/2 of (s + 3x + 1)(128 eps)^x.
- Since s > s1, (128 eps)^(s/2) < h^(-3). So the count is at most n * polylog(h) * h^(-3) = O(1/h).

Theorem A(a) then needs M > B over the union. Subadditivity adds 8 calB(M) for P, using (7) of the budget note.

## External results used

- Chernoff lower-tail bound P(Bin(m,p) <= mp/2) <= exp(-mp/8). Standard, not looked up. Used only for the typical size of J in T5(c).
- Perron-Frobenius: a positive matrix has a simple largest eigenvalue that governs u^T T^l 1. Standard. Used only for the growth rate in T5(c).
- Internal inputs: Theorem A of hilbert_lambda_anticoncentration.md (curve-free); (7) of the local factor budget note (audited); the Theorem B and Prop 4 configurations as stated in their notes; the 2-adic filters of H7 S3(c) and of residual Propositions E and F and Theorem C (unaudited). No web sources.

## Checks

I checked all proofs by hand: satisfiability of the triples, the king-adjacency formula for shared corner cells, the straddle counts and the constants 67, 100.5 and 10, the middle-digit supermartingale, the 3^k0 sum, the corner-chain induction, the Perron root (5 + sqrt 17)/8, and the exploration count 128.

Scripts, each run once with py in under 60 s, are in scripts_hb3_rc_rest/:
- rqc.py builds sampled RQC curves at n = 4 and 6. Every curve is a bijection with king steps of length 1. The largest D^2/t is 5.8 (against 16), and Lemma 0 has 0 violations over all pairs.
- mc_check.py compares the exact dynamic-programming laws with 4000 sampled curves. The difference is within 1.5 standard deviations.
- atoms.py (exact). In the rank view, 2^k times the one-coordinate atom has median 4.2, 7.5, 10.4, 15.3, 21.0, 33.9, 43.1, 78.8 and 109.9 for k = 3..11. In the cell view, the median atom times 4^k grows from 28 to 3558 for k = 3..8.
- disp.py (exact, worst split type). sqrt(d) times the x-displacement atom has median 2.6, 2.6, 3.0, 6.9, 7.6, 7.6 and 17.5 for k = 3..9. 2^(k-1) P(dx = 0 mod 2^(k-1)) has median 1.5 to 4.7.
- chain_atom_check.py checks T5(a) on 49152 digit pairs with 0 violations. It also measures the largest fraction of ranks on one exact translation vector at gap 4^k, n = 7, k = 1..5. The Hilbert curve gives 0.155, 0.119, 0.106, 0.119 and 0.129. RQC gives 0.047, 0.022, 0.011, 0.008 and 0.0045, below (3/4)^k.
- straddle_thmB.py runs the necessary separation count on the archive's Theorem B instances. The prefix configurations fail already at 2 to 4 pairs. This is illustrative only, and the claim is the analytic bound.
Neither repository was touched.

## Gaps

- The target is not proved. No with-high-probability bound on B_Lambda3, B_Lambda4 or the residual B at any sigma below a power of h.
- Theorem R's hypotheses (CC) and (SS) are unproved for every family. By T5, (CC) cannot be verified through the isolation chain bound with pointwise conditional atoms in any corner-entry curve, because the uniform conditional costs are inflated by 2^|J(o)|. A proof must track the 2-adic compatibility between targets and corner chains.
- (SS) can fail at a single triple in principle. Prop G only bounds the per-triple pattern multiplicity by 4(2M-1), and Theorem A needs it below M. Arithmetic shows at most one pattern per lambda-window for h < M S^8/256, but nothing uniform in h.
- Even with ideal anticoncentration, overlap steps exist with only polylog-small cost: a near pair with a second far end costs about 16/(S^2|b|). So bounded B needs (SS) for sets of up to about 3 ln h/ln ln h labels. That is a deterministic small-set statement, and it is not proved.
- T3(c) bounds sub-configurations of Theorem B only by O(log(h/S^4)), not by a constant. T3 does not exclude other dense locality-consistent configurations. I did not build an H7 (row step 28) version of Theorems B and T3.
- T4 controls only exact 2D displacements. One-coordinate and cross-coordinate atoms, such as the transposition identity and the f-match i_f - i_v = lambda K b, have no proved RQC bound. The numerics show one-coordinate displacement atoms decaying like d^(-0.27), short of the d^(-1/2) needed.
- The sigma estimate (sigma >= 0.0072 ln h) uses the random-row heuristic for the Lambda3 mean, which T5 shows is not a valid conditional bound. The heuristic means for Lambda4, R2s, FW and 6PT are taken from the archive and not re-derived.
- T1's transfer claim rests on my reading that the cited proofs use only (1), Lemma 0, aligned blocks and slot ranks. The unaudited H7 inputs (AP4, N1, S1-S6) stay unaudited.
- Nothing here is audited.

## Missing estimate

Two estimates are missing, for a random quadtree curve placed in each tile at S = 6272 sigma0 with sigma0 = C log h.
1. (CC'), an averaged conditional anticoncentration. For every structure W of O(log h) labels and every label z of W, the conditional expected number of candidate constraints of the five families that attach at z must be at most 1/256, given the ranks of W. New labels found through z count as "tree" attachments. Constraints meeting W twice count as "overlap" attachments, and their expected number must also be at most 1/256.
 Requirements. The estimate must be stated with the true conditional laws, not their pointwise maxima. T5 shows that the maxima are too large by 2^|J(o)|, at least l/32 bits of inflation at typical offsets, in every corner-entry curve. The estimate must also cancel the inflation through 2-adic incompatibility of the targets lambda K b, G | Y1, S | delta and 2^(2 v2 S - 1) | delta with the corner-chain supports R(o).
2. (SS), deterministic small-set sparsity. Every connected set of at most 3 ln h/ln ln h labels must carry constraints of total weight at most 5 per label, with per-triple pattern multiplicity at most M - 1. T3 is the first instance: it does this for the Theorem B family, as m <= 68 for the full configuration.
With both estimates, Theorem R gives M = floor(8 calB(M)) + 6 per tile, and the C4' width O(h^2 log h).

## Next steps

- Try a base-3 randomized Peano-type curve with king continuity. Corner chains then align 3-adic rank digits with 3-adic coordinates, not with the 2-adic and 7-adic filters of H7, so T5(d) has no resonance with them. The locality constant becomes 36 instead of 16 (D^2 < 4*9^k = 36*9^(k-1) < 36t), so S = 14112 sigma. Check whether the P family's 3-divisibility of Pythagorean legs reintroduces resonance.
- Prove (SS) for the Lambda3 family on sets of O(log h/log log h) labels with the straddle lemma plus the Theorem 1 arithmetic. Start with near-pair clusters, which are the only heavy codegrees by Prop G.
- Replace pointwise atoms with low-bit-compatible bounds. Write P(H(r+d)_c = x | F_B) as 1{x mod 2^l in R_c(o)} * 2^(|J(o)|) * (smoothed atom). Then average the indicator over the AP of targets lambda K b, as in the shift averaging of hilbert_g_for_p Theorem C.
- Prove a one-coordinate version of T4(a). This needs the orientation statistics of RQC types: the probability that a node is vertical-adjacent given its ancestors.
- Have a second reader audit T1-T5 and Theorem R. All proofs are short. T5(a) and T3(b) are the most consequential.

