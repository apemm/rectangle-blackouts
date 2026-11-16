# Multiplicative-function bounds cannot prove (E)

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (obstruction to a method): pointwise (E) is false, with an explicit 4-cycle that violates it for every C < 4144, and Shiu, Nair-Tenenbaum and Henriot bounds can never certify a density below (log x)^(-g), while each relation needs a saving of order L/log h. A position-averaged (E) looks true numerically for 4-cycles. Proved along the way: exact leg formulas, a closed-polygon form of the cycle relations, a T-averaged (E) for dense windows, and polylogarithmic moments of the per-diagonal hub weight. Not audited yet.

# Result

## Status

obstruction

## Summary

The multiplicative-function route can't prove (E) in any form that gives bounded cores. Pointwise (E) is false, with an explicit 4-cycle violating it for every C < 4144. A position-averaged (E) looks true numerically for 4-cycles (off-diagonal solutions at 0.7 to 2.0 times the random level). Shiu, Nair-Tenenbaum and Henriot bounds never certify a density below (log x)^(-g), and each relation needs a saving of order L/log h. The route does prove exact leg formulas, a closed-polygon form of the relations, a T-averaged (E) for dense windows, and polylogarithmic moments for the per-diagonal hub weight. Nothing here is audited.

## Statements

NOTATION. S = 2^s with s >= 2. A P-vector is (q, Y) with q >= 1, Y odd, (Sq)^2 + Y^2 = L^2. P_h is the set of P-vectors with L <= h-1. q_o is the odd part of q. For a configuration, edge k joins i_a to j_b in Gamma_C. Its signed vertical displacement is y_k = 2(j_b - i_a) + 1, and Y_k = |y_k|. Its candidate horizontal displacement is S(M(r_b - r_a) + delta_k). The window W_k(T) is {Y odd : |Y - (2T+1)| <= 8 sqrt(d_k)}, which has width w_k = 16 sqrt(d_k). The leg count is N_k(T) = #{(delta, Y) : |delta| <= M-1, Y in W_k(T), (M d_k + delta, Y) in P_h}. "Proved" means proved here, and nobody has audited it.

THEOREM A (exact leg functions; proved).
(A1) q side. For each q >= 1, the number of odd Y >= 1 with (q, Y) a P-vector is exactly tau(q_o^2). So legs per gap form a genuine multiplicative function of q_o. With the cap L <= h-1, the count nu_h(q) satisfies nu_h(q) <= tau(q_o^2).
(A2) Y side. For odd Y, the map q -> alpha = L - Sq is a bijection from the legs of Y onto {alpha | Y^2 : alpha < Y, alpha = +-Y (mod 2^s)}. The inverse is q = (Y^2/alpha - alpha)/(2S) and L = (Y^2/alpha + alpha)/2. Hence psi_S(Y) := #legs = (Psi_S(Y) - 1)/2, where
 Psi_S(Y) = #{alpha | Y^2 : alpha = +-Y mod 2^s} = 2^(2-s) * sum over even characters chi mod 2^s of conj(chi)(Y) g_chi(Y),
 g_chi(Y) = sum over alpha | Y^2 of chi(alpha).
 Each g_chi is multiplicative, with g_chi(p^l) = sum_(i=0..2l) chi(p)^i and g_1 = tau(Y^2). So 0 <= psi_S(Y) <= tau(Y^2)/2.
(A3) Windowed legs are divisors in a short multiplicative interval. Fix [q_-, q_+] = [Md - M + 1, Md + M - 1]. The legs of Y with q in this window correspond to the alpha | Y^2 with alpha = +-Y mod 2^s and alpha in [alpha(q_+), alpha(q_-)], where alpha(q) = sqrt(S^2 q^2 + Y^2) - Sq. This interval satisfies log(alpha(q_-)/alpha(q_+)) <= 2S(M-1)/L(q_-). For Y and L of order h, its relative length is of order SM/h.
(A4) Every P-vector satisfies Y^2 >= 2Sq + 1. In Gaussian form, y + i x = eps kappa z^2 with eps = +-1, kappa odd and z = E +- iO from the T1 normal form.

THEOREM B (cycle relations are closed alternating integral polygons; proved). Let gamma be a cycle of Gamma_C of length 2l, written i_(a_1) - j_(b_1) - i_(a_2) - j_(b_2) - ... - j_(b_l) - i_(a_1). Let k_(2m-1) = (i_(a_m), j_(b_m)) and k_(2m) = (i_(a_(m+1)), j_(b_m)). Then:
 - sum over m of (y_(k_(2m-1)) - y_(k_(2m))) = 0 exactly. The relation has no branch constants once you use signed y.
 - The alternating sum of the horizontal displacements is S * Delta_gamma, where Delta_gamma = sum over m of (delta_(k_(2m-1)) - delta_(k_(2m))) and |Delta_gamma| <= 2l(M-1).
 - Under any actual choice assignment, Delta_gamma = 0. The polygon P_1 Q_1 P_2 Q_2 ... P_l Q_l is closed, with P_m the odd point of a_m and Q_m the even point of b_m, and every side has integer length.
 So the relation system of Proposition 7 counts near-closed alternating polygons of integer-length vectors. In Gaussian form it reads sum over the cycle of +-eps_k kappa_k z_k^2 = i S Delta_gamma, a diagonal quadratic system over Z[i].

PROPOSITION C (pointwise (E) is false; computer-assisted, verified by brute force). Take S = 32, M = 3, h = 2^21. Take ranks r_a = 0, r_c = 800, r_d = 13175 and r_b = 21718. Use the 4-cycle i_a - j_b - i_c - j_d - i_a, so u = 4, |C| = 4 and R = 1. Then:
 - d = (21718, 20918, 12375, 13175) and q = (65155, 62755, 37125, 39525) = 3d + (1, 1, 0, 0).
 - Y = 76773 carries the legs of edges 1 and 2, with L = 2086373 and 2009627.
 - Y' = 76725 carries the legs of edges 3 and 4, with L = 1190475 and 1267125.
 - With 2T + 1 = 76749, each window holds exactly one leg, so N_k = 1.
 - The tuple (Y, Y, Y', Y') satisfies the relation. The count is 1.
 - The relation range is sum_k 8 sqrt(d_k) = 4144.2.
 So (E) as stated needs C >= 4144. These are pairing solutions: i_a = i_c forces c_1 = c_2 and c_3 = c_4. At this height, 346 such configurations exist, 328 of them with ratio above 1000. The ratio grows like the range, about 32 sqrt(d). An infinite family, which would refute every C, is not proved. Any usable (E) must therefore average over positions.

PROPOSITION D (the ceiling of multiplicative-function bounds; proved, as a statement about the theorems' right-hand sides).
(D1) Shiu: the bound (y/(phi(k) log x)) exp(sum over p <= x, p not dividing k, of f(p)/p) is at least y/(phi(k) log x) for every f >= 0.
(D2) Henriot's New Theorem 5, and also the Nair-Tenenbaum bound: the right side y * prod over g < p <= x of (1 - rho(p)/p) * sum of F~ rho'/[..] is at least c_g y (log x)^(-g). The n = (1,..,1) term of the sum equals 1, and rho(p) <= g for p > g because Q is primitive.
(D3) Consequence for (E). Fix a relation lattice Lambda and the box B of windows. Suppose a proof majorizes each windowed leg indicator by a nonnegative multiplicative function of a linear form and then applies (D1) or (D2), one variable at a time over D variables. Its bound is at least c |Lambda ∩ B| (log h)^(-gD). The (E) right side is about C^R |Lambda ∩ B| prod_k (N_k/w_k). So the route can't prove (E) whenever prod_k (N_k/w_k) < c' C^(-R) (log h)^(-gD). That covers every configuration with legs of length L >= (log h)^A, because there N_k is O(polylog) and w_k >= sqrt(d_k). The q-window, 2M - 1 consecutive gaps, is also too short for Shiu or Henriot whenever 2M - 1 < (Md)^beta.

LEMMA E (bipartite cores carry no curve saving; proved). Split a core into labels A that use only their odd point and labels B that use only their even point, with every constraint joining A-odd to B-even. Then Gamma_C has u non-isolated vertices and u isolated ones. The curve can pin at most u - 1 coordinates, so R = |C| - u + 1. A weighted K0-core of this type has R >= (K0/2 - 1)u + 1, and every extra edge is a pure arithmetic relation.

THEOREM F (what the route proves; proved, elementary apart from the standard Mertens and Euler-product facts).
(F1) T-averaged (E) for dense windows. Let B be any finite set of cell-offset vectors z, and let the forms c_k(z) satisfy |c_k| <= h for k = 1..m. Then
 sum over |T| <= h, z in B of prod_k psi_S(|2(T + c_k(z)) + 1|) <= C_m h |B| (log h)^(3^m).
 Relations are built in, because c_k are the actual forms. No short interval enters. This is (E) with each N_k replaced by w_k (log h)^(O(1)), so it is a trivial bound for sparse windows.
(F2) Hub moments. Define Lambda(T) = sum over d >= 1 of d^(-1/2) N_d(T), the curve-free exploration weight of diagonal T. Then
 Lambda(T) <= 2 * sum over odd Y of min(1, 8/|Y - 2T - 1|) psi_S(Y),
 sum over T of Lambda(T)^k <= C_k h (log h)^(3^k + k), for every k >= 1.
 Hence #{T : Lambda(T) > lambda} <= C_k h (log h)^(3^k + k) lambda^(-k). Pointwise, Lambda(T) is at most h^(o(1)), and the bound is attained at divisor-rich 2T + 1.
(F3) Rank-averaged q-side moments. Let the label-tree gaps g_t lie in [G_t, 2G_t] for t = 1..u-1. Let q_k = M d_k(g) + delta_k >= 1 with d_k = |sum_t a_kt g_t|, a_kt in {0, +-1}, and every form nonconstant. Then
 sum over g of prod_(k=1..m) tau((q_k)_o^2) <= C_m u M (prod_t G_t)(log h)^(3^m).
 This replaces the pointwise loss max tau(q_o^2) = h^(o(1)) by a polylogarithm wherever the rank variables are summed. That covers the label-tree and pinning edges.

RANGES (where the short-interval theorems apply).
 - Y windows have half-width 8 sqrt(d) at Y of order |2T + 1| <= h. Shiu (y > x^beta) and Henriot NT5 apply when 16 sqrt(d) >= (|2T+1| + 8 sqrt d)^beta for a fixed beta > 0, with constants depending on beta. For Henriot, shift the window to (x, x+y] with x = y. Then ||Q~|| <= (Ch)^g, and x >= C0 ||Q~||^delta holds with delta = beta/g. A sufficient condition is d >= h^(2 beta). Near the diagonal, they apply for every d once |2T+1| <= (16 sqrt d)^(1/beta).
 - If d < h^(2 beta) and |T| is of order h, no short-interval theorem applies. Only tau(Y^2) <= exp(O(log h / log log h)) remains.
 - q windows (2M - 1 gaps at q of order Md) are never long enough when M = O(log h).
 - The divisor intervals of (A3), with relative length about SM/h, are beyond all three theorems.
 - T-averaged sums run over a range of length h and need no short intervals.

NUMERICAL EVIDENCE G (sanity only, not proof). Take blocks of Y of length 128 and keep the P-vectors with q >= 768, so that one window serves all four edges. Count 4-cycle quadruples with |q_1 - q_2 + q_3 - q_4| <= 8. The solutions with s = Y_1 - Y_2 + Y_3 - Y_4 = 0 split as follows:
 - Identical-vector diagonals (v_1 = v_2 and v_3 = v_4, or v_1 = v_4 and v_2 = v_3) dominate. These are the repeated-factor slot twins of the fixed-factor lemma.
 - Two-leg-Y diagonals occur at 1.91 times (S = 32, h = 2^18) and 0.72 times (S = 16, h = 2^16) the mean count at small nonzero s.
 - Off-diagonal solutions occur at 0.87 times and 2.02 times that mean.
 So after slot grouping, a position-averaged (E) for 4-cycles looks true with C of about 2.

CONDITIONAL THEOREM H (not proved). Call a local-lemma window W c-bulk if every candidate P edge with an endpoint in W has L >= h^c. Assume:
 - (H_Lambda') with 4 Lambda < 1;
 - the averaged hypothesis (E_avg): after slot grouping, for every skeleton with u <= C log h labels and e extra edges, the expected number of copies rooted in W, summed over roots, is at most |W| Lambda^(u-1) (C_0 M h^(-c) log h)^e.
 Then for large h, P(W contains a weighted K0-core) <= 1/(3e) for every K0 > 1 + 2/c. The random model predicts (E_avg) in c-bulk windows, where each extra edge costs about M log h / L. Proposition D shows the multiplicative route can't supply it. Windows near the diagonal, with small L, are not covered. By the support principle, local cores recur there.

NOT PROVED: (E) in any form strong enough for bounded cores; (E_avg); any width improvement.

## Proofs

A1. By T1 (audited), the odd Y carrying Sq correspond one to one with triples (kappa, e', O), where kappa and O are odd, gcd(e', O) = 1 and kappa e' O = q. Distinct triples give distinct Y. Write q = 2^v q_o. Then e' = 2^v e'' with kappa e'' O = q_o and gcd(e'', O) = 1. The count is multiplicative in q_o. At p^l, kappa takes p^i. The rest, p^(l-i), goes entirely to e'' or entirely to O by coprimality, which gives 2 choices if i < l and 1 if i = l. The total is 2l + 1 = tau(p^(2l)). Check: check_leg_functions.py, with S = 4..32 and q < 400, found 0 failures.

A2. Put alpha = L - Sq and beta = L + Sq. Then alpha beta = Y^2, both are odd, and beta - alpha = 2^(s+1) q. So the condition is beta = alpha mod 2^(s+1), that is, (Y - alpha)(Y + alpha) = 0 mod 2^(s+1). Exactly one of Y - alpha and Y + alpha is 2 mod 4, so this holds iff alpha = Y or alpha = -Y mod 2^s. Also alpha < beta iff alpha < Y. If alpha = eps Y, then Y^2/alpha = eps Y mod 2^s. So alpha -> Y^2/alpha preserves the class and pairs the divisors other than alpha = Y, which gives psi_S = (Psi_S - 1)/2. Orthogonality on (Z/2^s)^*/{+-1}, a group of order 2^(s-2), gives the character formula, and |g_chi| <= tau(Y^2). The same script found 0 failures for Y < 2000.

A3. alpha(q) = L(q) - Sq, so d alpha/dq = S^2 q/L - S = -S alpha/L and d log alpha/dq = -S/L. Integrate over [q_-, q_+], whose length is 2M - 2, and use L >= L(q_-).

A4. L > Sq gives L >= Sq + 1, so Y^2 = L^2 - S^2 q^2 >= 2Sq + 1. The Gaussian form: kappa(E + iO)^2 = kappa(E^2 - O^2) + 2i kappa E O. The sign choices +-kappa(E +- iO)^2 reach all four quadrants.

B. In y: (2(j_(b_m) - i_(a_m)) + 1) - (2(j_(b_m) - i_(a_(m+1))) + 1) = 2(i_(a_(m+1)) - i_(a_m)), which telescopes to 0. In x: the rank parts M(r_(b_m) - r_(a_m)) - M(r_(b_m) - r_(a_(m+1))) telescope the same way, which leaves S * sum of (delta_(2m-1) - delta_(2m)). Under an actual assignment, delta_k = xi_b - xi_a, which telescopes to 0. Then the polygon's sides are the constraint vectors, each of integer length L_k.

C. The script pointwise_E_counterexamples.py enumerates P_h by T1. It finds pairs Y != Y', each carrying two legs with equal leg differences q_1 - q_2 = q_4 - q_3 = 3g. It sets d_1 = round(q_1/3), d_2 = d_1 - g, d_3 = round(q_3/3) and d_4 = d_3 + g, and then computes the window counts and the exact tuple count. verify_example.py rechecks the reported example without T1: it tests every odd Y in every window and every delta for exact squareness, and confirms N_k = 1, the four values of L, and d_1 - d_2 = d_4 - d_3 = 800. Ranks r_a < r_c < r_d < r_b realize these gaps. If i_a = i_c, then c_1 = j_b - i_a = c_2 and c_3 = c_4, so the relation holds automatically. Locality allows this, because |r_c - r_a| = 800 and |Y - Y'| = 48 < 8 sqrt(12375).

D. For (D1), exp(...) >= 1 because f >= 0. For (D2), take Henriot's New Theorem 5 as restated in 2026-11-13/ap_hypothesis_henriot.md. The sum on the right contains n = (1,..,1), whose term is F(1,..,1) rho'(1) = 1. Each Q_j is primitive, so Q is nonzero mod p and has at most g roots when p > g. Mertens then gives prod over g < p <= x of (1 - g/p) >= c_g (log x)^(-g). For (D3), any bound for sum over Lambda ∩ B of prod phi_k that ends with these theorems is a sum, over the outer variables, of inner bounds. Each inner bound is at least c (number of inner terms)(log h)^(-g). Iterating over D variables gives at least c |Lambda ∩ B| (log h)^(-gD). Bounding some phi_k trivially, by 2M - 1, only weakens this. The count of lattice points in the window box is |Lambda ∩ B| = C^(O(|C|)) prod w_k / prod range_r. Compare it with the (E) right side, C^R prod N_k / prod range_r. For (A3), Shiu needs y > x^beta, and 2M - 1 < (Md)^beta violates that.

E. Under the bipartite hypothesis, only i_a (a in A) and j_b (b in B) touch edges. Gamma_C is then connected on u vertices whenever the label graph is connected, and #comp(Gamma_C) = 1 + u. Proposition 7 gives R = |C| - 2u + 1 + u = |C| - u + 1. A K0-core has |C| >= K0 u/2.

F1. AM-GM gives prod_(k=1..m) a_k <= (1/m) sum_k a_k^m. For fixed z and k, n = 2(T + c_k) + 1 runs injectively over odd n with |n| <= 4h + 1, and psi_S(n) <= tau(n^2). For f(n) = tau(n^2)^m, sum over n <= x of f(n) <= x sum of f(n)/n <= x prod over p <= x of (1 + 3^m/p + sum over nu >= 2 of (2nu+1)^m p^(-nu)) <= C_m x prod (1 + 1/p)^(3^m) <= C_m x (log x)^(3^m). Sum trivially over z.

F2. Swap the sums. A fixed (q, Y) is reached only through slots (d, delta) with Md + delta = q and |delta| <= M - 1. There are at most 2 such d, because they lie in an open interval of length (2M-2)/M < 2. Each needs d >= max(1, t^2/64) with t = |Y - 2T - 1|, so d^(-1/2) <= min(1, 8/t). This gives the pointwise inequality. Now put weights w_t = 2 min(1, 8/|t|) on even t with |t| <= 2h. Then W = sum of w_t <= 50 + 16 log h. Jensen gives Lambda(T)^k <= W^(k-1) sum_t w_t psi_S(2T+1+t)^k. Sum over T: each odd n <= h occurs at most once for each t. So sum over T of Lambda^k <= W^k sum over n <= h of tau(n^2)^k <= C_k h (log h)^(3^k + k), by the bound in F1.

F3. Use AM-GM as in F1. For each k, pick a variable g_t with a_kt != 0 and the largest G_t among the variables of form k. Fix the other variables. Then q_k = M a_kt g_t + c with |q_k| <= 4uM G_t, and q_k runs injectively as g_t varies. So the inner sum is at most the sum over 1 <= n <= 4uM G_t of tau(n_o^2)^m, which is at most C_m u M G_t (log h)^(3^m). Sum trivially over the other variables.

G. averaged_energy_classes.py enumerates every (v_1, v_2, v_3) in a block, every q_4 in q_1 - q_2 + q_3 + [-8, 8], and every Y_4. It records s and sorts the s = 0 solutions into identical-vector diagonals, same-Y diagonals and the rest. The figures are those in the Theorem field.

H (conditional). A connected component of a K0-core is a K0-core, and a K0-core with u labels has e >= (K0/2 - 1)u + 1 extra edges. There are at most 4^(u-1) tree shapes and at most 8Mu^2 choices of pair, role, delta and branch for each extra edge. With u <= C log h, M <= log h and h large, 8C_0 M^2 u^2 log h * h^(-c) <= h^(-c/2). So E[#cores with u labels] <= 2|W| (4 Lambda)^(u-1) h^(-(c/2)((K0/2-1)u+1)). Summing over u >= 2 gives at most 4|W| h^(-(c/2)(K0-1)). Since |W| <= h, this is at most 1/(3e) when K0 > 1 + 2/c. Theorem 6 of the P-cores note excludes components with more than C log h labels, given H_Lambda.

## External results used

- P. Shiu, A Brun-Titchmarsh theorem for multiplicative functions, J. reine angew. Math. 313 (1980), Theorem 1, cited from memory and not re-read. Hypotheses: f >= 0 multiplicative, f(p^l) <= A^l, f(n) <= B_eps n^eps, x^beta < y <= x, gcd(a,k) = 1 and k < y^(1-beta). Conclusion: the progression sum over (x-y, x] is << (y/(phi(k) log x)) exp(sum over p <= x, p not dividing k, of f(p)/p). Used only in Proposition D1 and the Ranges statement.
- K. Henriot, Nair-Tenenbaum bounds uniform with respect to the discriminant, Math. Proc. Camb. Phil. Soc. 152 (2012), and its Erratum, 157 (2014), New Theorem 5, as restated in the archive note 2026-11-13/ap_hypothesis_henriot.md, not re-read. Hypotheses: Q_1..Q_k primitive, Q of degree g, F in M_k(A,B,eps), x >= C0||Q||^delta and x^alpha < y <= x. Conclusion: the sum is << y prod over g < p <= x of (1 - rho(p)/p) * sum of F~ rho'_R / [n kappa(n)]. Used only in D2 and the Ranges statement.
- Nair-Tenenbaum (Acta Math. 1998): a bound of the same shape, mentioned only for D2's remark.
- Standard facts: Mertens' theorems; orthogonality of characters mod 2^s; Jensen and AM-GM; the Euclid parametrization through the audited T1.

## Checks

The scripts are in scripts_hb4_e_mult/. Each ran with py -B, one at a time, in under 11 s and well under 1 GB.
- check_leg_functions.py checks A1 (S = 4, 8, 16, 32 and q < 400) and A2 with the parametrization (Y < 2000). It found 0 failures.
- pointwise_E_counterexamples.py searches 4-cycle pairing configurations at S = 32, M = 3 and h = 2^21. It found 202945 P-vectors, 36538 Y with two legs, and 346 configurations, all with ratio above 100. The largest ratio is 4144.2.
- verify_example.py rechecks the leading example by brute-force square tests, without T1.
- averaged_energy_test.py, averaged_energy_offdiag.py and averaged_energy_classes.py run the block 4-cycle energy test. Results are in Evidence G.
By hand I checked A1 to A4, B (both telescoping sums), the ceiling inequalities D1 and D2, the count in Lemma E, F1 to F3, and the first-moment arithmetic of H. Neither repository was modified, and no git command was run.

## Gaps

- (E) is not proved in any form that gives bounded cores. The averaged hypothesis (E_avg) of Theorem H is unproved. Proposition D shows that this route can't prove it.
- Proposition C refutes pointwise (E) only for C < 4144, using finitely many examples. An infinite family with N_k bounded and windows growing, which would refute every C, is not proved. The data suggest the ratio grows like 32 sqrt(d).
- Proposition D is a statement about the form of the Shiu and Henriot bounds, and about proofs that end with them. It doesn't rule out other arithmetic methods, such as sieves, lattice-point counting or the circle method.
- Shiu's Theorem 1 is cited from memory, with the hypotheses the archive audit recorded, and not re-read. Henriot's New Theorem 5 is used as restated in 2026-11-13/ap_hypothesis_henriot.md, also not re-read. Both enter only through (D1), (D2) and the Ranges statement. F1 to F3 use only an elementary Euler-product bound.
- Theorem H rests on (H_Lambda') and (E_avg), which are both unproved. It covers only c-bulk windows. In near-diagonal windows the edge lengths L are small, and K0 may grow like 1 + 2 log h/log T.
- The numerical energy test G is small (h <= 2^18, S in {16, 32}, M = 3, one block geometry). It covers 4-cycles only, and it uses block windows rather than the exact windows of (E). It is evidence, not proof.
- The character expansion in A2 gives the 1/S saving only on long ranges, and only through a complex-valued sum. I did not prove the mean value of psi_S. F1 and F2 bound psi_S by tau(Y^2) and so lose a factor of about S/4.
- Lemma E names a structural class with no curve saving. I did not show that bipartite K0-cores occur in the candidate graph.
- Nothing here is audited. The scripts are single implementations, though verify_example.py checks the main counterexample independently of the T1 enumeration.

## Missing estimate

You need a position-averaged count of near-closed alternating integral polygons, as in Theorem B, that saves about L_k/(log h)^C for every relation. After slot grouping, for each skeleton with u <= C log h labels in a c-bulk window, the root-summed curve-weighted count should be at most |W| Lambda^(u-1) (C M h^(-c) log h)^e (hypothesis E_avg). In Gaussian form, each relation is sum over the cycle of +-eps_k kappa_k z_k^2 = i S Delta, with each z_k in a thin sector, because the Y windows have width sqrt(d) at radius L. Equivalently, you need upper bounds, along linear forms, for counts of divisors of Y^2 in multiplicative intervals of relative length about SM/L. The bound has to be power-saving and averaged over positions. Multiplicative-function theorems can't reach it (Proposition D). Candidate tools are Heath-Brown's square sieve, integer points on the conics |XA| +- |XC| = m (each a binary quadratic equation with at most C tau(N) points), and the delta method for systems of quadrics over Z[i]. The 4-cycle data (Evidence G) suggest that after slot grouping the true constant is about 2.

## Next steps

- Prove the averaged 4-cycle case. For fixed odd points A and C, every even point D at integer distance from both lies on one of O(|AC|) conics. Each conic carries at most C tau(N) lattice points. Sum over (A, C) with the curve weights, and aim for one factor of h^(-c) in c-bulk windows.
- Treat the two-leg-Y diagonal separately. Bound, on average over the two q windows, the number of Y <= h carrying legs in both. This is the class that breaks pointwise (E).
- Extend Evidence G to 6-cycles and to the exact (E) windows, at S = 32, M = 3 and h up to 2^20, with each run under 60 s. Check that off-diagonal and two-leg solutions stay at the random level after slot grouping.
- Restate the P-cores conditional with (E_avg), averaged over positions, in place of pointwise (E). Add the near-diagonal caveat: Theorem H gives K0 > 1 + 2/c only in c-bulk windows.
- Feed F2 (polylogarithmic moments of Lambda(T)) into the graded Theorem G, which charges hubs through M_e proportional to 1 + lambda_e. Check whether higher moments simplify its hub accounting.
- Ask a second reader to audit A1 to A3, B, D, E and F1 to F3, and to recheck verify_example.py and averaged_energy_classes.py with an independent enumerator.

