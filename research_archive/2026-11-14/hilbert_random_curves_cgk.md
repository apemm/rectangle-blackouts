# Randomized Hilbert-type curves (corner-gated king curves)

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: randomized corner-gated king curves keep Hilbert locality with the same constant 16 and Lemma 0 verbatim, so every audited Hilbert result survives with the same strides, design H7 included (Theorems 1 to 3). The randomness decouples exactly at height ceil(log_4 d) given a 144-state gate pair (Theorem 4), a local-lemma window reduction turns (G) into a constant-probability bound for one window (Theorem 5), and the translation and transposition atoms are broken in expectation at rate 0.6742^k per level (Theorem 6). (G) itself is not proved. A support principle shows that at fixed (S, M) randomization cannot remove local obstructions of positive probability; it only delays them. Audited in audit_hilbert_random_curves_cgk.md (correct with fixable gaps).

# Result

## Status

proved

## Summary

Randomized corner-gated king curves (CGK) keep Hilbert locality with the same constant c = 16 and keep Lemma 0 verbatim. So every audited Hilbert result survives with S unchanged (32, 1568 and 6272 sigma), H7 included. Given a gate pair with 144 states, the randomness decouples exactly at height ceil(log_4 d). The 4^k translation and transposition atoms are broken in expectation, at a certified rate of 0.6742^k per level. A local-lemma window reduction turns (G) into a constant-probability bound for one window. (G) itself is not proved. A support principle shows that at fixed (S, M), randomization cannot remove local obstructions that have positive probability; it only delays them.

## Statements

Setting. q = 2^n. A curve is a bijection H: [0,q^2) -> [0,q)^2. A level-j rank block is [beta 4^j, (beta+1) 4^j). An aligned square of side 2^j is [2^j a, 2^j(a+1)) x [2^j b, 2^j(b+1)). The two coordinates H(r)_1 and H(r)_2 play the roles of (i, j) for labels. "Proved" below means proved in this note, which nobody has audited yet.

DEFINITION 1 (the class Q_kappa). H is in Q_kappa if (Q1) every level-j rank block maps onto an aligned square of side 2^j, for every j, and (Q2) the Chebyshev distance ||H(r+1) - H(r)||_inf is at most kappa for every r. The Hilbert order of recursion (2) is in Q_1.

THEOREM 1 (locality; proved). Let H be in Q_kappa, let t = |r - s| >= 1, and let k be least with 4^k >= t. Then for c = 1, 2,
 |H(r)_c - H(s)_c| <= 2^(k+1) - 2 + kappa.
Consequences:
 (a) If kappa <= 2, then max(Di^2, Dj^2) < 16 t. This is inequality (1) of the placement note, with the same constant.
 (b) If kappa = 1, Lemma 0 holds verbatim: |D| >= 2^m with m >= 1 forces t > 4^(m-1).
 (c) For every kappa, max D^2 < (kappa+2)^2 t. If kappa <= 2, the weak Lemma 0 form t > 4^(m-2) holds.
 (d) Converse: if a (Q1) order satisfies max D^2 < c t for all pairs, then it is in Q_kappa with kappa = ceil(sqrt c) - 1. Bounded junction steps are exactly what a constant locality bound requires. An order with free child orientations, such as Morton order, fails.

DEFINITION 2 (CGK curves). Corners and children of a square are labelled by bit vectors in {0,1}^2. Child p has origin s p inside a parent of side 2s, and parent corner c is corner c of child c. A gate is g = (in, out) with in != out. There are 8 A-gates (adjacent corners) and 4 D-gates (diagonal corners).
A refinement of g at a node with child side s >= 2 is a child order (p1, ..., p4) together with child gates g_k = (in_k, out_k). The conditions are:
 - p1 = in and in_1 = in; p4 = out and out_4 = out;
 - in_k != out_k for every k;
 - junction rule J between consecutive children: on each axis a, if p_k,a != p_k+1,a then out_k,a = p_k+1,a and in_k+1,a = p_k,a; otherwise out_k,a = in_k+1,a.
R(g) is the set of refinements of g. A node of side 2 instead uses one of the two orders of its four cells that start at in and end at out.
The random CGK curve with root gate g0 makes an independent uniform choice at every node, indexed by rank blocks, from R(gate of that node).

THEOREM 2 (structure; proved; the table is also enumerated by script).
 (a) |R(g)| = 6 for A-gates and 2 for D-gates. The table is equivariant under D4.
 (b) Every realization lies in Q_1, starts at the in-corner cell and ends at the out-corner cell.
 (c) Junction lemma: if r and r+1 lie in distinct level-k blocks B and B' (k >= 1), then H(r+1) - H(r) = out_B - in_B' as bit vectors, and the block origins satisfy O_B' - O_B = 2^k (out_B - in_B').
 (d) The Hilbert order H_q is one realization. Its root gate is (00 -> 10), and each node takes the image of ((00,01,11,10); 00->01, 00->10, 00->10, 11->10) under the symmetry that carries 00->10 to the node's gate.

THEOREM 3 (what survives; proved by checking each proof's dependence on the curve). Replace the Hilbert order by any H in Q_1, for example any CGK realization, and keep original ranks on subsets.
These hold verbatim, with the same constants and the same S:
 - placement Theorem 1 (same-parity exclusion at S = 32, and S = 8 d^2 in profiles, d = 14 giving 1568);
 - the same-parity slope argument and placement Theorem 2 (S^4 >= 64 h);
 - the mixed-supports theorem (S^4 >= 1024 h);
 - the factor-one theorem, including the M = 2 rank-parity rule and the two-earlier-neighbour greedy;
 - the uniqueness lemma (one candidate gap per factor, role and side) and the finite-factor theorem (M >= 4R+1, S >= 8; profile S >= 4d);
 - angles-note Theorems 1-2 and Proposition 3, with thresholds M S^4 >= 16(h-1), S >= 16 and sqrt(M) S^4 >= 128 sqrt 2 (h-1);
 - lambda note: Theorem A, Lemmas H1-H2, Propositions G and T, and Theorem B, which remains a barrier for locality-only methods;
 - g_for_p: Theorem A, Theorem C (random diagonal shift) and Proposition D;
 - H7: Lemmas S1-S6, Theorem H7 as corrected by its audit, U3, all thresholds, and the Corollary width 6272 sigma M (h+28)^2 + C1 h^2;
 - the tiling assembly (Theorem T, C4', graded Theorem G).
For Q_kappa with kappa > 2, use c = (kappa+2)^2. Then S >= 2c (full grid), S = c d^2/2 (profiles), and in H7 S = 392 c sigma (128 | S still needs 16 | c sigma). The factor-one theorem needs S^2/8 > kappa + 2.5. The finite-factor theorem needs S >= 2(kappa+2), and the angle thresholds lose a factor 4.
These do not transfer, because they are statements about the one Hilbert curve:
 - Lemma H3 and Theorem B(i)-(iv) of g_for_p;
 - the height-independent cores (the diagonal blocks are id or swap only in Hilbert);
 - Lemma H4, whose proof uses the four Klein-group orientations;
 - placement Section 6 and the recursive, orientation, dyadic-residue, two-choice and P-triangle obstructions;
 - all Hilbert census data.

THEOREM 4 (decoupling; proved). Let Sigma_k be the sigma-field generated by the choices at nodes of side > 2^k.
 (a) Sigma_k determines the origin O_B and the gate g_B of every level-k block B.
 (b) Given Sigma_k, the local curves h_B(rho) = H(beta_B 4^k + rho) - O_B are independent over B, and h_B has the law of a CGK curve of side 2^k with gate g_B.
 (c) Let 0 < s - r = d <= 4^k with k >= 1. Either r and s share a block B, and H(s) - H(r) = h_B(rho_s) - h_B(rho_r). Or they lie in consecutive blocks B and B', and H(s) - H(r) = 2^k (out_B - in_B') + h_B'(rho_s) - h_B(rho_r).
 So everything above height k = ceil(log_4 d) enters only through (g_B, g_B'), which has 144 states. Below height k, only the choices on the two root-to-leaf paths inside B and B' matter, at most 2k node choices.
 (d) Statistics that depend on disjoint sets of level-k blocks are conditionally independent given Sigma_k. In particular, pairs whose rank separation is at least 2 * 4^k plus their own span are conditionally independent.

THEOREM 5 (window reduction and local lemma; proved). Let F be any family of constraints of arity 2 to 4 with multiplicities m_E, and let every constraint have rank diameter at most 4^k. For P this means 4^k >= (h-2)/(S M) + 1. Let W_t be the union of the consecutive blocks B_t and B_t+1, and let beta_t be the largest induced weighted density (1/|U'|) * sum of |J_E| m_E over U' inside W_t, where each constraint is assigned to the first window that contains it. Then
 max over t of beta_t <= B_F <= 2 max over t of beta_t,
where B_F is the quantity of lambda-note Theorem A. Fix any value of Sigma_k, and let the local curves below height k be random. Suppose P(beta_t > beta | Sigma_k) <= 1/(3e) for every t. Then some realization has B_F <= 2 beta, so floor(2 beta) + 1 private choices avoid F. The top levels can be chosen freely, Hilbert included.

THEOREM 6 (atoms broken in expectation; proved, with an exact rational matrix computation). Let d >= 4^k with k >= 1, let a, b be in {1,2}, and let w be any integer. Then
 E #{r : H(r+d)_a - H(r)_b = w} <= q^2 mu_k.
Here mu_k = max over gates g of the average over rho of P(two independent CGK curves with gate g agree in one coordinate at rho). It satisfies mu_k <= ||T^(k-1)||_inf, where T is an explicit 144 x 144 transfer matrix. Exact rational arithmetic gives ||T^40||_inf = 1.41305e-7, so mu_k <= 0.67415^(k-40). The spectral radius of T is 0.66441 (computed in floating point), against 1 for Hilbert and 1/2 for an equidistributed curve.
Corollaries:
 (i) For every vector v, E #{r : H(r+4^k) - H(r) = v} <= q^2 mu_k. Hilbert has at least q^2/16 for one v (Lemma H3).
 (ii) The pointwise-in-gap hypothesis that Lemma H3 refutes for Hilbert holds in expectation with exponent 0.2844 instead of 1/2: E #{r : H(r+d)_1 - H(r)_1 = D} <= C q^2 d^(-0.2844).
 (iii) For every t and d = 4^k, E #{r : j_(r+d) - i_r = t} <= 4 q sqrt(d) mu_k, which is about q d^0.216. Hilbert has a fiber of at least q sqrt(d)/8 (Theorem B(iv)).

PROPOSITION 7 (support principle; proved, conditional on the unaudited Corollary A1 of the cores note, whose proof transfers line by line). Fix S, M, a side B, a gate g and one realization tau of a side-B CGK curve with gate g, of probability p_tau > 0. Let N be the number of mid-strip main-diagonal B-blocks with gate g. Given Sigma_b, the probability that none of them carries tau is (1 - p_tau)^N. If the diagonal system G_B^tau has weighted degeneracy at least D, or has no M-choice assignment, then that holds for the whole placement except on that event. So at fixed (S, M), randomization delays local obstructions of positive probability but does not remove them. For the Hilbert sub-curve at B = 512, p_tau is about 6^(-B^2/12) 2^(-B^2/4), which is astronomically small.

## Proofs

PROOF OF THEOREM 1. Take r < s. Since s - r <= 4^k, the two ranks lie in one level-k block or in two consecutive ones, B and B'.
 - Same block: (Q1) gives a difference of at most 2^k - 1.
 - Consecutive blocks: let l be the last rank of B. By the triangle inequality, the difference is at most |H(r) - H(l)| + |H(l) - H(l+1)| + |H(l+1) - H(s)| <= (2^k - 1) + kappa + (2^k - 1).
 - If k = 0, then t = 1 and the bound is kappa.
 - If k >= 1, then 4^(k-1) < t, so 2^(k+1) < 4 sqrt(t).
 (a) For k >= 1, D <= 2^(k+1) < 4 sqrt(t). For k = 0, D <= 2 < 4.
 (b) D <= 2^(k+1) - 1. So 2^m <= D forces m <= k, hence k >= 1 and t > 4^(k-1) >= 4^(m-1).
 (c) D < 4 sqrt(t) + kappa - 2 <= (kappa+2) sqrt(t). Weak Lemma 0 for kappa <= 2: 2^m <= 2^(k+1), so t > 4^(k-1) >= 4^(m-2).
 (d) Take t = 1.
The proof uses only (Q1) and (Q2). In particular, consecutive squares need only touch, possibly at a corner.

PROOF OF THEOREM 2.
(a) Hand count for g = (00 -> 10). Only two orders put child 00 first and child 10 last.
 - Order (00, 01, 11, 10). Rule J forces out_1 = (a,1) and in_2 = (a,0); then out_2 = (1,b) and in_3 = (0,b); then out_3 = (c,0) and in_4 = (c,1). The only distinctness constraints are not (a=1 and b=0) and not (b=0 and c=0). That leaves 8 - 2 - 2 + 1 = 5 refinements.
 - Order (00, 11, 01, 10). J forces g_1 = 00->11, in_2 = 00, out_2 = (0,b) with b = 1, g_3 = 11->10 and g_4 = 01->10. That is 1 refinement.
 So |R(A)| = 6.
 For g = (00 -> 11) and order (00, 10, 01, 11), J forces g_1 = 00->10, g_2 = 00->01, g_3 = 10->11 and g_4 = 01->11. The transposed order gives one more, so |R(D)| = 2.
 Rule J is defined axis by axis and is invariant under bit flips and under the axis swap, so the table is D4-equivariant. table.py enumerates all 12 gates and confirms 6/2 and the Hilbert entry.
(b) Induction on n. Side 2: any order of the four cells of a 2x2 square is a king path. Side 2s with s >= 2:
 - Each child curve is in Q_1 on its square and runs from corner in_k to corner out_k.
 - The last cell of child k is s p_k + (s-1) out_k, and the first cell of child k+1 is s p_k+1 + (s-1) in_k+1.
 - On an axis where the children differ, with e = p_k+1,a - p_k,a = +-1, rule J gives a difference of s e - (s-1) e = e. On the other axes the difference is 0.
 - So the junction is a king step. Aligned sub-blocks lie inside a child, and the first and last cells are the parent's gate corners.
(c) Let P and P' be the consecutive children of the lowest common ancestor that contain B and B'. B is the last level-k descendant of P, so out_B = out_P as a label; likewise in_B' = in_P'. Rule J gives out_P - in_P' = p' - p, and the cell difference computed in (b) is p' - p. Then O_B' - O_B = (cell(r+1) - (2^k - 1) in_B') - (cell(r) - (2^k - 1) out_B) = 2^k (p' - p).
(d) Recursion (2) has quarters (y,x), (x, y+q), (x+q, y+q) and (2q-1-y, q-1-x).
 - Their gates are 00->01 (transpose), 00->10, 00->10 and 11->10 (antitranspose), which is the canonical refinement.
 - D4 acts simply transitively on the 8 A-gates, so "image of the canonical refinement" is well defined.
 - curve.py reproduces recursion (2) exactly for n = 3, 5 and 7.

PROOF OF THEOREM 3. For each listed proof, I checked where the Hilbert order enters.
 - Placement Theorem 1, the profile form (6)-(7), the slope argument and placement Theorem 2 use only (1).
 - The mixed-supports note uses (3), which comes from (1).
 - Factor-one theorem: (5)-(6) come from (1); Sections 3-4 are arithmetic on ranks.
 - Finite-factor theorem: (21) is arithmetic; (22) is (1) between the two partners.
 - Angles Theorems 1-2 use Lemma 0 and (1); Proposition 3 uses locality.
 - Lambda note: H1 and H2 use only (Q1); Proposition G and Theorem A use locality or nothing; Proposition T uses Theorem 1's inequalities.
 - g_for_p: Theorem A uses only (Q1); Theorem C uses locality and the fact that ranks do not depend on the shift J.
 - H7: the reduction uses (Hil), S | X, 49 | X, (Al), (Bulk) and residues mod 7. Of these, only (Hil) involves the curve, and (Hil) is (1) with d = 28. Period-zero columns and 128 | S come from x_e = x_0 + S(M r_e + xi_e) and do not depend on the curve.
 - Tiling Step 1 uses (Q1) and (1).
 - Every list item above was proved for Hilbert using only these inputs, and Theorem 1 supplies all of them for every H in Q_1.
 - Dropping Lemma 0 to its weak form (kappa = 2) changes the angle and mixed thresholds by a factor 4. The other constants come from Theorem 1(c).

PROOF OF THEOREM 4. Given the gate, the curve of a node is a deterministic function of the choices at the nodes inside it. The origin and gate of a level-k block depend only on choices at its strict ancestors. This gives (a) and (b). Theorem 2(c) gives the offset in (c). Statement (d) follows from the product structure in (b).

PROOF OF THEOREM 5. A set of ranks of diameter at most 4^k lies in at most 2 consecutive level-k blocks, so every constraint lies in some window. Let t(E) be the first window containing E. For any U,
 sum over E inside U of |J_E| m_E = sum over t of (sum over E with t(E) = t and E inside U ∩ W_t) <= sum over t of beta_t |U ∩ W_t| <= 2 max beta |U|,
because each label lies in at most 2 windows. The lower bound holds because each beta_t is a value of the maximum defining B_F. Given Sigma_k, the event {beta_t > beta} depends only on the local curves of B_t and B_t+1. It is therefore mutually independent of all events with |t' - t| >= 2, so each event has at most 2 dependency neighbours. The symmetric local lemma (e p (D+1) <= 1 with D = 2) gives positive probability that no window is bad. Lambda-note Theorem A(a) then finishes, since B < M is enough.

PROOF OF THEOREM 6.
 - Transfer identity. Coordinate a of the cell at local rank rho is the sum over node levels of s_level * p_level,a. Two independent copies agree in coordinate a exactly when all these bits agree.
 - Along rho's digits the pair of gates is a Markov chain: each copy picks a uniform refinement, emits the bit of child p_delta and moves to the gate g_delta.
 - Averaging over uniform rho makes the digits i.i.d. uniform. This gives E_rho P(agree) = e_(g,g)^T T^(k-1) b, where T[(g1,g2),(g1',g2')] = (1/4) sum over delta of P(the bits agree and the next gates are (g1', g2')), and b is the side-2 base vector. T >= 0 and b <= 1, so mu_k <= ||T^(k-1)||_inf.
 - The sequence ||T^L||_inf is submultiplicative and ||T||_inf = 1. chain2.py computes T^40 times the all-ones vector exactly with Fractions, which gives 1.41305e-7. Hence mu_k <= (1.41305e-7)^floor((k-1)/40) <= 0.67415^(k-40).
 - T_y is conjugate to T_x under the axis swap, so the same bound holds for both coordinates.
 - Main bound. Condition on Sigma_k. Since d >= 4^k, r and r+d lie in distinct blocks, and their offset is fixed. With X and Y independent,
 P(X - Y = w') = sum over y of P(Y = y) P(X = y + w') <= (coll_b(g_B, rho) coll_a(g_B', rho'))^(1/2)
 by Cauchy-Schwarz. Summing over r and applying Cauchy-Schwarz again gives at most the square root of (sum over r of coll(r)) times (sum over r of coll(r+d)). Each of these sums is at most (q^2 / 4^k) 4^k mu_k = q^2 mu_k.
 - (i) Use a single coordinate.
 - (ii) Put k = floor(log_4 d).
 - (iii) Write the offset as 2^k (y_beta - x_beta + u_2), and note that the local difference lies in (-2^k, 2^k). So only blocks with |t/2^k - (y - x)| < 2 contribute: at most 4 block diagonals, with at most q/2^k blocks each. Each block contributes at most 4^k mu_k in expectation.

PROOF OF PROPOSITION 7. Given Sigma_b, the diagonal blocks have independent local curves, so the first claim follows. The proof of Corollary A1 uses four facts:
 - each block is a contiguous rank interval, by (Q1);
 - row differences on the diagonal are local;
 - the completion rows of mid-strip blocks stay inside the strip;
 - the owners of the completion rows exist and lie outside the block.
None of these depends on which orientation the block has. So G_B^tau occurs as genuine rivals whenever a block carries tau. Degeneracy is monotone under taking subgraphs, and an unsatisfiable subsystem leaves no valid assignment.

CHECKS (sanity only; py; each run under 60 s; scripts in the script folder).
 - table.py: the table, with 6 or 2 refinements per gate; the Hilbert entry is present.
 - curve.py: bijection, king steps and the (Q1) block structure, all exact. max D^2/t is 5.5 or less against the bound 16 (exhaustive for n <= 5, sampled plus all block junctions for n = 7-9). Lemma 0 has 0 violations. Recursion (2) is reproduced.
 - chain2.py: Monte Carlo agrees with the transfer prediction, for example 0.1746 against 0.1748 at m = 5. The exact certificate is above.
 - atoms.py at q = 256, k = 0..6:
   - Translation-atom fraction: Hilbert 0.25 to 0.10 (never below 0.096); three random curves 0.18, 0.065, 0.030, 0.015, about 0.010, 0.004, 0.004.
   - Transposition fiber divided by q sqrt(d), m = 1..6: Hilbert 0.99 to 0.50; random 0.61 to 0.06, close to 0.664^m.
 - pcensus.py, weighted P degeneracy, full grid; Hilbert compared with 2-3 random curves:
   - h = 512, S = 8, M = 2: degeneracy 4 against 4, 4, 4; mean degree 1.83 against 1.84-1.86.
   - h = 1024, S = 8, M = 3: 4 against 4, 4.
   - h = 2048, S = 16, M = 3: 3 against 3, 3; mean degree 0.81 against 0.80.
   So at small h, randomization does not change the P statistics.
 - Gate chain (floating point): the Dobrushin coefficient is below 1 for every digit word of length L = 4 to 7 except 14 explicit words. The exceptions are runs of first-child or last-child digits, which inherit the in or out corner exactly, for example 0^L and 3^L. Words over {1,2}^6 have coefficient at most 0.177. Words with at least half middle digits have coefficient at most 0.82 at L = 6 and 0.68 at L = 8.

## External results used

- Symmetric Lovasz local lemma (standard; not looked up): if each event has probability at most p, each is mutually independent of all but at most D others, and e p (D+1) <= 1, then with positive probability no event occurs. Used in Theorem 5 with D = 2.
- Cauchy-Schwarz inequality, used twice in Theorem 6.
- Dobrushin contraction coefficient (half the largest L1 distance between rows of a stochastic matrix), used only to report the computed mixing numbers.
- Internal, audited: recursion (2) and inequality (1) (continuation_hilbert_placement.md); the factor-one and finite-factor theorems; the mixed-supports note; the H7 reduction as corrected by audit_hilbert_sea_design_h7.md.
- Internal, unaudited, used only through statements re-checked here: lambda-note Theorem A, Lemma 0, angles Theorems 1-2, g_for_p Theorems A and C, and cores-note Corollary A1 (for Proposition 7).

## Checks

Scripts are in scripts_hb3_rc_def/ (65 KB):
 - table.py: refinement table;
 - curve.py: generator, the Q1/Q2/locality/Lemma 0 checks, and Hilbert reproduction;
 - chain.py: gate chain and transfer matrices;
 - chain2.py: Monte Carlo check and exact rational certificate;
 - atoms.py: Hilbert against random atoms;
 - pcensus.py: P degeneracy census;
 - words.py: non-contracting digit words.
Each ran with py in under 60 s, one at a time. The repositories were only read. No git command was run.
By hand I checked the |R| = 6/2 count, rule J giving king junctions, the junction lemma, Theorem 1 with all its cases, the transfer identity and both Cauchy-Schwarz steps, the fiber block count (at most 4 diagonals), the window double-count, and the dependency degree 2 in the local lemma.

## Gaps

- (G) is not proved for any family. Theorem 5 reduces it to a per-window bound, sup over Sigma_k of P(beta_t > beta | Sigma_k) <= 1/(3e) with beta = c0 + c1 (k+1) log h / S_k, which is unproved.
- CGK is only partly anticoncentrated. The certified collision rate is 0.674 per level (spectral 0.664), against 1/2 for equidistribution, because the first and last children are fixed by the gate. The rigorous pointwise-in-gap exponent is 0.284, against the 1/2 that H-EQ would want.
- All anticoncentration is averaged over local ranks. For a fixed rank at a block start (rho = 0), the local position is deterministic given the gate, so per-rank statements fail.
- Gate-chain mixing is computed in floating point only (14 non-contracting words per length). No proved contraction rate exists, so unconditional decoupling above height k is not proved; only conditional independence given Sigma_k is.
- Lemma H4 (residue equidistribution) does not transfer; its proof uses the four Klein orientations. The HJ-conditional mean bound therefore loses that input for random curves.
- Survival for notes I did not read in full (local factor budget (13)-(14), residual families Theorem D, p_family_counts T3) rests on those notes' own statements that the curve enters only through (1).
- Proposition 7: at fixed (S, M), any local core of positive probability recurs as h grows, so randomization cannot give O(h^2) through degeneracy-type certificates. It does not rule out satisfiability-type arguments. Its premise rests on the unaudited Corollary A1, re-derived here only for the transfer.
- The exact certificate for T comes from a single implementation, cross-checked only by Monte Carlo. The constant 0.67415^(-40), about 7e6, is crude.
- Census evidence is tiny (h <= 2048) and full-grid only. No random-curve census exists for H7 blocks (S = 6272) or for the band excess.
- Nothing here is audited.

## Missing estimate

This is the window estimate for b = 1. For each tile level k, the family needs rank diameter D_F <= 4^kappa. For P, D_F = (h-2)/(S_k M) + 1. Each window W_t holds two consecutive level-kappa blocks with independent CGK sub-curves of side about sqrt(h/S_k), given the gates and absolute positions. The estimate needed is
 sup over Sigma_kappa and t of P(beta_t > c0 + c1 (k+1) log h / S_k | Sigma_kappa) <= 1/(3e),
and the analogue at the final level with (log h)^2 / S_K. The same is needed for all six H7 families at once, with D_F their largest rank diameter. By Theorem 5 this gives (G), and C4' or Theorem G then gives width O(h^2 log h). The probability needs to be constant, not polynomially small, because of the local lemma. A natural first target is a first-moment bound on dense subsets of bounded size inside one window. In a window, each pair event depends only on the at most 2 ceil(log_4 d) node choices on its two paths and on a 144-state gate pair. Pair events whose level-floor(log_4 d) blocks are disjoint are conditionally independent.

## Next steps

- Attack the window estimate for P. Write beta_t > beta as the existence of a subset U' with |E(U')| >= beta |U'|. Bound the expected number of such subsets of bounded size using Theorem 4(c): pair events depend on 2k path choices plus a gate pair. Treat large U' with the shifted first-moment count of g_for_p Theorem C, now averaged over the curve instead of a shift.
- Enlarge the family to push the collision rate toward 1/2, for example with gates at non-corner boundary cells (beta-Omega type) or with kappa = 2 jumps. Theorem 1 keeps c = 16 for kappa <= 2. Also prove a lower bound on the rate for any corner-gated scheme.
- Write a faster census (numba) of weighted P degeneracy by band and level, Hilbert against random CGK, at S = 16-64 and h up to 2^14, and in real H7 blocks (S = 6272, row step 28). Test whether random curves reduce the band excess at |b-a| near h^(2/3), which the small census cannot see.
- Prove gate-chain contraction outside the 14 exceptional words, for example a Doeblin bound for every word with at least one middle digit in each window of 3. This would turn Theorem 4 into unconditional near-independence across heights.
- Have a second reader audit Theorems 1, 2(c), 5 and 6, and the dependency check behind Theorem 3, especially H7 S4-S6 and tiling Step 1.

