# The local-limit hypothesis for random curves fails

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (obstruction): the local-limit hypothesis (H_Lambda') is false for random corner-gated king curves in both its two- and one-dimensional forms. It fails pointwise in the history for every corner-entry curve law at x = 4^k + 1, and for these curves also after averaging over the rank, with the best uniform exponent between 0.2844 and 0.2950 instead of 1/2. The correct form has a 4-adic proximity factor, proved harmless on average over x, and a grouped exploration lemma holds with threshold 16 Lambda' < 1. The P core count still does not close: it needs a target-averaged estimate and an averaged exploration lemma. Not audited yet.

# Result

## Status

obstruction

## Summary

Hypothesis (H_Lambda') is false as a local limit for random CGK curves, in both its 2D form C 4^(v_4 x)/x and its 1D form C 2^(v_4 x)/sqrt(x). It fails pointwise in the history for every corner-entry curve law, at x = 4^k + 1 where v_4(x) = 0. For CGK it also fails after averaging over the rank, with the best uniform exponent between 0.2844 and 0.2950 instead of 1/2. The correct form has a 4-adic proximity factor, which is proved harmless on average over x. A grouped exploration lemma is proved with threshold 16 Lambda' < 1. The P core count does not close with provable inputs: it still needs a target-averaged estimate (L*) and an averaged exploration lemma.

## Statements

SETTING. H is a random CGK curve (hilbert_random_curves_cgk.md, Definition 2) of side 2^n, with N = 4^n ranks. Write Delta(r,x) = H(r+x) - H(r) and Delta_c for its coordinate c. lambda_1 and lambda_2 are the spectral radii of the 144-state collision transfer matrices for one coordinate (cgk Theorem 6) and for both coordinates. Numerically lambda_1 = 0.66441 and lambda_2 = 0.52508. A "corner-entry curve" means any king-continuous quadtree order in which each aligned square's sub-curve starts and ends at corner cells. This covers Hilbert, CGK, RQC and Model K. "Proved" means proved here, with no audit yet.

T0 (what the exploration needs; proved). Every P edge pins one coordinate. In role 0, Delta_2(r_v, x) is (Y-1)/2 - T_v or -(Y+1)/2 - T_v; role 1 is the mirror image with Delta_1. A group gamma = (q, role, side) has at most 2 partner labels. They sit at ranks r_v + s d0 and r_v + s(d0+1), with d0 = floor(q/M) and only one rank when M | q. These ranks are consecutive, so the partners are king-adjacent cells. If P(Delta_c(r_v, s x) = z | ranks of R) <= A(x) for every z and every history, then the grouped exploration constant of T5 satisfies
 Lambda' <= 8 sup_v sum over x >= 1 of A(x) N_v(x).
Here N_v(x) is the number of pairs (q, Y) with x a slot of q, Y in Y(q), and Y inside v's locality window ||Y| - |2T_v + 1|| <= 8 sqrt(x) + 2. The 2D form P(Delta = z) <= C 4^(v_4 x)/x implies the 1D form with A(x) = 8C 4^(v_4 x) x^(-1/2). So the 1D statement A(x) = C 2^(v_4 x) x^(-1/2) is the real target.

T1 (pointwise failure for every corner-entry law; proved). Take any probability law on corner-entry curves, k >= 1, K >= k+2, and r = beta 4^K, and let x = 4^k + 1, so v_4(x) = 0. Given the cell H(r), the vector Delta(r,x) takes at most 64 values and Delta_c at most 8. So max_z P(Delta = z | H(r)) >= 1/64 and max_z P(Delta_c = z | H(r)) >= 1/8. The 2D form fails once 4^k > 64C, and the 1D form fails once 2^k > 8C. For CGK, exact laws give 2D atoms of at least 3/32 and 1D atoms of at least 0.28 for k <= 4. The failure also holds on average over x under the same history:
 sum over 1 <= x < 4^K of max_z P(Delta_c(r,x) = z | H(r)) >= 0.78 (2 * 1.1404)^K - 1, against sum over x of 2^(v_4 x) x^(-1/2) <= 4 * 2^K;
 sum over x of max_z P(Delta(r,x) = z | H(r)) >= 0.5 * 1.5^K - 1, against sum over x of 4^(v_4 x)/x <= K(1 + K ln 4).
The constant 1.1404 is (5 + sqrt 17)/8.

T2 (CGK, averaged over the rank; proved, with an exact rational certificate). Suppose n >= k+2 and x = 4^k + 1. Then
 max_z (1/N) sum over r of P(Delta_c(r,x) = z) >= (7/2592)(0.737 * 0.6644^(k-1) - 4^(-k)),
 max_z (1/N) sum over r of P(Delta(r,x) = z) >= (7/20736)(0.694 * 0.525^(k-1) - 4^(-k)).
So the rank-averaged 1D form fails once k >= 21 + 3.6 ln C, and the 2D form fails once k >= 11 + 1.35 ln C. Combined with cgk Theorem 6(ii) (unaudited), the best exponent theta in a bound (1/N) sum over r of P(Delta_c = z) <= C x^(-theta) that is uniform in x and z lies in [0.2844, 0.2950]. The upper end is -log_4 0.6644.

T3 (the form that does hold pointwise; proved). Let L be the least level at which r and r+x share a block. Let B1 and B2 be the distinct level-(L-1) blocks of r and r+x, with gates g_i and local offsets rho_i. Then
 P(Delta_c = z | Sigma_(L-1)) <= min(alpha_c(g_1, rho_1), alpha_c(g_2, rho_2)) and also <= sqrt(coll_c(g_1, rho_1) coll_c(g_2, rho_2)).
Here alpha is the largest single-cell atom and coll is the collision probability. Now condition instead on F_Q, everything outside a block Q that contains r+x but not r, as an exploration does. Then P(Delta_c = z | F_Q) <= alpha_c(g_Q, o), where o is the offset of r+x in Q. This single-cell atom is inflated on average over offsets:
 - E_o alpha_c(g, o) >= 0.737 * 0.6644^(l-1) for CGK at level l;
 - E_o alpha_c(g, o) >= 0.78 * 0.5702^l for every corner-entry law.
So a step bound by single-cell atoms loses a factor of at least (2 lambda_1)^l, about x^0.205, for CGK, and at least 1.1404^l, about x^0.095, for every corner-entry curve.

T4 (the 4-adic proximity factor is harmless on average; proved). Let Phi(x) = max over 0 <= m <= log_4 x of (2 lambda_1)^m (1 + dist(x, 4^m Z))^(-1/2). For 1 <= p < ln 4/ln(2 lambda_1) = 4.876,
 sum over x <= W of x^(-1/2) Phi(x)^p <= C_p sqrt(W).
So in a weighted sum, Phi costs at most a constant times an L^(p') norm of the arithmetic weights, with p' >= 1.26, by Hölder.

T5 (grouped exploration lemma; proved). Assume each label v has groups gamma with random partner sets P_gamma(v) of size at most 2, and that {B in P_gamma(v)} is measurable with respect to the ranks of {v} and B. Suppose that for s = 1, 2, every finite R and every v in R,
 ess sup over the ranks of R of [sum over gamma, sum over B in V \ R with |B| = s, of P(B in P_gamma(v) | ranks of R)] <= Lambda'.
Then the expected number of present block trees rooted at e0 with t blocks is at most (16 Lambda')^t. If 16 Lambda' < 1, then with probability at least 1 - 1/N every component has at most 2 ceil(2 ln N/ln(1/(16 Lambda'))) + 1 labels. The ess sup has to sit outside the sum over partners. Theorem 6 of the cores note puts it inside, which is a stronger hypothesis than its proof uses.

CONJECTURE (numerical evidence only). The correct averaged two-point form is
 (1/N) sum over r of P(Delta_c(r,x) = z) <= C x^(-1/2) Phi(x),
and in 2D it is <= C x^(-1) Phi_2(x), where Phi_2(x) = max over m of (4 lambda_2)^m (1 + dist(x, 4^m Z))^(-1).

VERDICT. (H_Lambda') cannot be proved as a local limit for CGK, because it is false in every stated form. The P core count does not close with provable inputs. It would close for tree-like components at S of order log h only under three things, none of which is proved: (L*) of the Missing estimate, an averaged exploration lemma, and, for dense cores, (E). If only atom bounds are used, the exploration constant comes out polynomial in h (heuristic count in the proof, part 7).

## Proofs

1. PROOF OF T0.
 - Role 0. Y = |2(j_w - i_v) + 1|, and j_w - i_v = Delta_2 + T_v. So Delta_2 has 2 targets per Y; role 1 is the same with Delta_1.
 - Slots. The slots of q are the d with |Md - q| <= M-1, namely floor(q/M) and ceil(q/M). These are two consecutive integers, or one when M | q.
 - Locality (1) gives |Delta_c| < 4 sqrt(x), so only Y inside the stated window can be hit.
 - Size-1 blocks. Sum over B of P(B in P_gamma) = E|P_gamma \ R|, which is at most the sum over the two slots and over Y of 2 A(x).
 - Size-2 blocks. Sum over B of P(B in P_gamma) = P(|P_gamma \ R| = 2), which is at most the same quantity.
 - Summing over 2 sides and 2 roles gives the factor 8.
 - 2D implies 1D. Sum the 2D bound over the free coordinate, which takes fewer than 8 sqrt(x) values.

2. DESCENT LEMMA (used in T1 and T3). Let N be a level-j node with entry corner alpha. If digit d_j = 0, the selected child is N's alpha-quadrant: N's sub-curve starts at N's alpha corner cell, which lies in that quadrant, and the quadrant's curve starts there. That cell is the quadrant's own alpha corner, so the child's entry corner is again alpha. Digit 3 works the same way with the exit corner omega. Consequence: along a maximal run of equal digits in {0,3}, all coordinate bits of those levels equal the corner bits of the run's top node. Each such run therefore contributes one free bit per coordinate, and none if the run's top node is B itself with its corner known. Each digit 1 or 2 contributes at most one free bit. So per coordinate there are at most l - |J(o)| free bits, where J(o) is the set of adjacent equal digit pairs in {0,3}. This is T5(a) of the other-families note, re-proved here.

3. PROOF OF T1.
 - Write x = 4^k + 1 with K digits. The digits are 0 at levels K to k+2, 1 at level k+1, 0 at levels k to 2, and 1 at level 1.
 - Let B be the level-K block of r. H(r) is B's entry corner cell, so alpha_B is known from H(r), since K >= 1 and the corner is congruent to 0 or -1 mod 2^K.
 - By the descent lemma, H(r+x) - O_B = (2^K - 2^(k+1)) alpha_B + 2^k p + (2^k - 2) alpha_Q + c_1, with p, alpha_Q, c_1 in {0,1}^2.
 - Also H(r) - O_B = (2^K - 1) alpha_B.
 - So Delta = -(2^(k+1) - 1) alpha_B + 2^k p + (2^k - 2) alpha_Q + c_1. Given H(r), this takes at most 4^3 = 64 values, and each coordinate at most 2^3 = 8.
 - The largest atom is at least the reciprocal of the support size, which gives the pointwise bounds.
 - Average over x. By the descent lemma, the support of Delta_c(r,x) given H(r) has size at most 2^(K - |J_K(x)|). So the sum of atoms is at least 2^(-K) times the sum over x of 2^|J_K(x)|, which is 2^(-K) 4^K (1/4) 1^T T^(K-1) 1, where T[a][b] = (1/4)(2 if a = b in {0,3}, else 1).
 - T has the positive eigenvector w = (1, t, t, 1) with t = (sqrt 17 - 1)/4 < 1 and eigenvalue (5 + sqrt 17)/8. Since 1 >= w, we get 1^T T^(K-1) 1 >= (2 + 2t) 1.1404^(K-1), and hence the sum is at least 0.78 (2.2808)^K. Subtract 1 for the term x = 0.
 - For the reference sum: the sum over x < 4^K of 2^(v_4 x) x^(-1/2) equals the sum over b of the sum over x' < 4^(K-b), 4 not dividing x', of x'^(-1/2), which is at most the sum over b of 2 * 2^(K-b), so at most 4 * 2^K.
 - 2D is the same with weight 4 on the diagonal of {0,3}: the eigenvector (1, 1/2, 1/2, 1) has eigenvalue 3/2, so 4^(-K) times the sum of 4^|J| is at least 0.75 * 1.5^(K-1). Also the sum over x of 4^(v_4 x)/x is at most the sum over b of (1 + ln 4^(K-b)), which is at most K(1 + K ln 4).

4. PROOF OF T2.
 (a) Gate facts, from the table, which I enumerated again independently:
 - |R(A)| = 6 and |R(D)| = 2, and the Hilbert refinement is in the table.
 - A D-gate parent has only A children.
 - An A-gate parent has an expected fraction 7/12 of A children.
 - Exactly one of the 6 refinements of each A-gate (the image of Hilbert's canonical refinement) gives children 2 and 3 the same gate. For D-gates there is none.
 - So for n >= k+2, the expected number of A-gate level-(k+1) blocks is at least (7/12) N/4^(k+1). Condition on Sigma_(k+2): each such block's expected number of A children is at least 4 * 7/12.
 (b) Take a level-(k+1) block P with an A-gate whose refinement shares the gate g' between children 2 and 3. This has probability 1/6 given Sigma_(k+1), since it is a fresh choice.
 - By cgk Theorem 4, given Sigma_k the local curves h_2 and h_3 are independent with the law CGK(g').
 - The offset satisfies O_3 - O_2 = 2^k (p_3 - p_2), and each of its coordinates lies in {-2^k, 0, 2^k}.
 (c) Take r in child 2 with local offset rho <= 4^k - 2. Then r + x is in child 3 with offset rho + 1.
 - X(rho+1) = h_3(rho+1) is king-adjacent to X(rho).
 - On the event X_c(rho) = Y_c(rho), with Y = h_2, the difference X_c(rho+1) - Y_c(rho) lies in {-1,0,1}.
 - So the sum over z in Z of P(Delta_c(r,x) = z) is at least coll_c^(g')(rho), where Z = {-2^k, 0, 2^k} + {-1,0,1} is a fixed set of 9 values.
 (d) Sum over r. The sum over rho <= 4^k - 2 of coll is at least 4^k m_k - 1, where m_k = min over g of E_rho coll_c^g at level k. Hence (1/N) sum over r of the sum over z in Z of P is at least (7/12)(1/4)(1/6)(m_k - 4^(-k)). Divide by |Z| = 9.
 - In 2D, Z has at most 8 * 9 = 72 values, and m_k is replaced by the 2D collision.
 (e) Transfer identity, re-derived. For two independent copies with gate g at a uniform offset rho, the digits are i.i.d. uniform. The pair of gates is a Markov chain: each copy picks a uniform refinement, emits the bits of child p_delta and moves to the gate g_delta. So E_rho coll^g = e_(g,g)^T T^(k-1) b, with b the side-2 base vector.
 (f) Certificate (cgk_transfer2.py, exact Fractions).
 - A rational vector u >= 0, supported on 136 of the 144 states, satisfies T u >= lambda u with lambda = 0.66440816 > 0.6644. Off the support, u = 0, so the inequality also holds there.
 - min over g of u(g,g) = 0.767774, and min over the support of b/u = 0.960296.
 - So m_k >= 0.960296 * 0.767774 * lambda^(k-1) >= 0.737 * 0.6644^(k-1).
 - 2D: lambda = 0.52508195 > 0.525, min u(g,g) = 0.925785, min b/u = 0.75, so m_k >= 0.694 * 0.525^(k-1).
 (g) Failure thresholds.
 - 1D: the lower bound divided by C 2^(-k) grows like (2 * 0.6644)^k = 1.3288^k, and exceeds 1 once k >= 21 + 3.6 ln C.
 - 2D: the ratio grows like (4 * 0.525)^k = 2.1^k, with the stated threshold.
 - The exponent window combines this with cgk Theorem 6(ii).

5. PROOF OF T3.
 - Given Sigma_(L-1), X = h_B2(rho_2) and Y = h_B1(rho_1) are independent, and the offset O_B2 - O_B1 is fixed (cgk Theorem 4).
 - P(X - Y = w) is the sum over y of P(Y = y) P(X = y + w). This is at most each single atom, and at most sqrt(coll(X) coll(Y)) by Cauchy-Schwarz.
 - Given F_Q, the cell of r is fixed and the law of h_Q(o) is CGK(g_Q), so the conditional atom is alpha.
 - CGK average: alpha >= coll, and coll is controlled by 4(f).
 - Average for every corner-entry law: alpha >= 2^(|J(o)| - l), and E_o 2^|J(o)| >= 0.89 * 1.1404^(l-1) by part 3.

6. PROOF OF T4.
 - Phi(x)^p is at most the sum over m with 4^m <= x of (2 lambda)^(mp) (1 + d_m(x))^(-p/2).
 - Fix m with 4^m <= W. For x >= 4^m, write x = j 4^m + b with j >= 1 and |b| <= 4^m/2. Then d_m(x) = |b| and x >= j 4^m/2.
 - So the sum over x of x^(-1/2)(1 + |b|)^(-p/2) is at most the sum over j <= 2W/4^m of (j 4^m/2)^(-1/2) times 2 A_p(m), where A_p(m) = sum over b <= 4^m of (1+b)^(-p/2). This is at most c sqrt(W) 4^(-m) A_p(m).
 - A_p(m) <= c_p 2^(m(2-p)) for p < 2, at most c(m+1) for p = 2, and at most c_p for p > 2.
 - Multiply by (2 lambda)^(mp) and sum over m. The terms behave like lambda^(pm) for p < 2, like (m+1) lambda^(2m) for p = 2, and like ((2 lambda)^p/4)^m for p > 2. All three series converge when (2 lambda)^p < 4.

7. PROOF OF T5.
 (a) Encoding. A block tree has the root e0 and t blocks of size 1 or 2. Each block hangs from one label of an earlier node through a group of that label. Labels are distinct, and the tree is present when each block lies in its group's partner set. There are at most 16^t shapes: Catalan C_t <= 4^t plane trees on t+1 nodes, 2^t choices of block sizes, and 2^t choices of which label of a 2-block each child block hangs from.
 (b) Probability bound. Order the blocks breadth-first and let R_(i-1) be the labels found before block i. The event A_i is measurable with respect to the ranks of R_i, and A_1, ..., A_(i-1) lie in sigma(ranks of R_(i-1)). So the sum over (gamma_i, beta_i) of P(A_1 ... A_i) equals E[1_(A_1 ... A_(i-1)) times the sum over (gamma_i, beta_i) of P(A_i | ranks of R_(i-1))], which is at most Lambda' P(A_1 ... A_(i-1)). Iterating gives (16 Lambda')^t.
 (c) From components to block trees.
 - Take a component U containing e0, with a spanning tree rooted at e0.
 - Each child w of v lies in P_gamma(v) for some group gamma of v, since groups include both sides. Choose one such gamma.
 - The children of v sharing (v, gamma) number at most 2, so they form one block.
 - That gives at least (|U| - 1)/2 blocks. Removing leaf blocks one at a time reaches exactly t blocks.
 - Union bound: the expected number of components with at least 2t+1 labels is at most N (16 Lambda')^t, which is at most 1/N for t = ceil(2 ln N/ln(1/(16 Lambda'))).
 - Theorem 6 of the cores note needs only the ess sup outside the sum, by the same step (b).

8. NUMERICAL CHECKS (sanity only; py; each run under 60 s, under 1 GB).
 - Rank-averaged atoms by Monte Carlo (cgk_mc.py and cgk_mc2.py, side 256, 357 to 400 curves).
   - Generic x (17, 37, 101, ..., 9999): sqrt(x) max 1D is 0.42 to 0.58, and x max 2D is 0.22 to 0.66.
   - x = 4^k, k = 2..6: 1D 0.42, 0.55, 0.73, 0.98, 1.37 (ratio about 1.33 per level); 2D 0.43, 0.83, 1.72, 3.67, 7.44 (ratio about 2.1 per level).
   - x = 4^k + 1, k = 3..6: 1D 0.44, 0.56, 0.73, 1.01; 2D up to 3.38.
   - Near-multiples: 9472 = 37 * 4^4 gives 1.05; 9473 gives 0.79; 9488 gives 0.72; 4113 = 4096 + 17 gives 0.62.
   - These match Phi and agree with (2 lambda_1, 4 lambda_2) = (1.33, 2.10).
 - Exact laws (cgk_exact_law.py). At block starts with x = 4^k + 1, the CGK support is at most 15 cells for k <= 4, under the proved 64. The 1D atom is at least 0.28. The block-start ratio of the summed atoms to the sum of 2^(v_4) x^(-1/2) is 1.46, 1.99, 2.68, 3.74, 5.28 for K = 2..6.
 - Heuristic consequence (random-row leg density, not proved). With step factors of order x^(-theta), the exploration sum is about the sum over x <= h/(SM) of 2M (16 sqrt(x)/h)(log K/pi) x^(-theta), which is about log K * M^(theta - 1/2) h^(1/2 - theta) S^(theta - 3/2). Keeping this below a constant needs S >= h^((1/2 - theta)/(3/2 - theta)). That is h^0.170 for CGK (theta = 0.295) and h^0.087 at the corner-entry ceiling (theta = 0.405). Either way the width is far above h^2 (log h)^1.31.

## External results used

- No published theorem used. Only standard facts: for a nonnegative matrix T and a vector u >= 0 with T u >= lambda u, T^m u >= lambda^m u (by induction); Cauchy-Schwarz; Catalan bound C_t <= 4^t.
- Internal, unaudited, used as stated: cgk Theorems 2(c), 4 and 6(ii) (decoupling, junction offsets, averaged exponent 0.2844); the archive's locality inequality (1); the p_family_counts slot definition.

## Checks

Scripts are in scripts_hb4_local_limit/ (32 KB). Each ran once with py -B in under 60 s and well under 1 GB.
 - cgk_transfer.py and cgk_transfer2.py: an independent refinement table with counts 6/2 and the Hilbert entry present; the gate facts 7/12 and 1/6; exact 144-state transfer matrices; spectral radii 0.66441 (1D) and 0.52508 (2D); exact rational Collatz-Wielandt certificates lambda > 0.6644 and lambda > 0.525 with their constants; and exact averaged collisions for k <= 8.
 - cgk_exact_law.py: exact laws at block starts, confirming the support bound of T1 and the growth of the averaged atoms.
 - cgk_mc.py and cgk_mc2.py: Monte Carlo of rank-averaged 1D and 2D atoms for generic and near-4-adic x, with bijection asserted for each curve.
 By hand I checked the descent lemma, the formula for Delta at 4^k + 1, both Perron eigenvectors, the T2 counting chain, both Cauchy-Schwarz uses, the T4 series, and the T5 encoding, its conditioning step and its pruning argument.
 Neither repository was modified, and no git command was run.

## Gaps

- The conjectured rank-averaged two-point local limit with the factor Phi is supported only by Monte Carlo (side 256, x <= 10^4). The upper bound is not proved. A proof would need a transfer operator that tracks gates top-down and carries bottom-up at the same time.
- There is no averaged or multi-point exploration lemma. The ess-sup lemma (T5) sees single-cell conditional atoms, which T1 and T3 show are inflated. A count averaged over histories would need a joint local limit for all cells of a tree, and none is proved.
- Hypothesis (H_Lambda') itself, as opposed to the local limit, is not refuted. It may hold if the P target sets miss the heavy atoms of the fractal single-cell laws, which is estimate (L*). T1 to T3 show only that atom bounds cannot prove it.
- The ess sup over arbitrary R includes near-collision histories, where a new rank sits next to an earlier tree rank. Grouping handles only clumping under the same parent. Near-collision steps behave like overlap or approximate-cycle steps and need arithmetic control of (E)/(SS) type, which is not done.
- Hubs are not addressed. Even an ideal local limit leaves Lambda' controlled by sup_v of the window leg sums N_v, which is the divisor-rich and hub problem. Graded M_e (Theorem G) is still needed.
- The universal (all corner-entry laws) results are pointwise and block-start statements. The rank-averaged failure T2 is proved only for CGK, because it uses the CGK gate table.
- The exact certificate rests on one implementation of the refinement table. It is independent of the cgk note's table.py and reproduces its counts, its Hilbert entry and its spectral radius 0.66441, but no second reader has checked it. T2's constants (7/2592, 0.737) are crude.
- The heuristic Lambda' computation in proof part 7 uses the random-row leg density, not a theorem.
- cgk Theorem 6(ii), used for the upper end of the exponent window, is unaudited. Nothing here is audited.

## Missing estimate

(L*), a target-averaged conditional local limit. Let Q be a fresh block of level l with gate g, o the offset of r_v + s x in Q, and F_Q the history. Let T_x(v) be the P target set, of size at most 2 N_v(x). The estimate needed is: for every history,
 sum over z in T_x(v) of P(h^g(o)_c = z - const | F_Q) <= C 2^(-l) Phi(x) |T_x(v)| + (overlap terms paid by (E)).
Equivalently, P target sets have to be equidistributed against the corner-chain supports and the heavy atoms of CGK single-cell laws (dimension about 0.59 per coordinate). This is the same 2-adic compatibility issue as (CC') in the other-families note. Two more inputs are needed: an exploration lemma that averages over histories instead of taking their ess sup, and (E) for dense cores. With all three, T0, T4 and T5 give Lambda' = O(mu) away from hubs.

## Next steps

- Test (L*) directly. For CGK at side 2^8 to 2^9 and S = 8 to 32, compute exact single-cell laws at block-start and generic histories. Compare E[number of P partners | history] with the model value 8 sum over x of x^(-1/2) N_v(x), on diagonals with divisor-rich windows.
- Try to prove the two-point averaged form with Phi. Condition on the split level and write X - Y as two independent Markov-modulated digit chains. Bound the characteristic function by a product of 144-state matrices; the near-4-adic factor Phi should come from the levels where rho and rho' share digits.
- Prove an averaged exploration lemma: weight histories by their probability rather than taking an ess sup. Block-start histories at level K have probability of order 4^(-K) per vertex, so their cost might be paid explicitly.
- Corner-entry curves cap single-cell exponents at 0.405 (T3). Test a non-corner-gated or base-3 king curve, as suggested in the other-families note, to see whether single-cell atoms can reach exponent 1/2, which would make atom-based exploration viable.
- Correct the hypothesis of Theorem 6 in hilbert_random_curve_p_cores.md: the ess sup belongs outside the sum over w. Replace its Lambda < 1/4 by the grouped threshold 16 Lambda' < 1 of T5.
- Have a second reader audit T1 (descent lemma), T2 (gate facts and certificate) and T5.

