# The heavy-diagonal count is sharp

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: the number of diagonals with kappa_T >= (log h)^xi is h (log h)^(-phi(xi)+o(1)) (sieve lower bound), so no moment bound can lower the cap 1.4967 of this architecture. A uniform random proper colouring of each light (T, type) cuts the Bad_split term to Lambda^2/B, which also gives exponent 1.4967. Rigid placement is priced by the maximum class count. Below 1.4967 only under open hypotheses. Not audited yet.

# Result

## Status

partial

## Summary

The heavy-diagonal count is sharp, so no count or moment bound can lower the cap of 1.4967. A uniform random proper colouring of each light (T, type) cuts the Bad_split term from Lambda^3/B to Lambda^2/B, so Theorem N drops from exponent 1.5 to 1.4967 without assuming sum c_T = O(h). Inside a rigid layout, neither cheaper heavy diagonals nor a label width proportional to c_T is possible. Under stated open hypotheses the exponent falls to about 1.25 or to 1.

## Statements

NOTATION. As in consolidated_board.md: stride 4, Lambda = log h, ell = loglog h, D_T = {|d| : 16d^2 + (2d+T)^2 = L^2, 0 < L < h, d != 0, |d| < n_T}, kappa_T = |D_T|, H_d(B) = #{T : kappa_T >= B}, E(a) = (1+3^a)/2. g(T) = product of (2e+1) over p^e || T with p = +-1 (mod 5). For xi > 0 put y = xi/ln 3 and phi(xi) = 1/2 - y + y ln(2y) (for y >= 1/2). theta* = min_a (E(a)+1)/(1+a) = 1.49674, attained at a = 0.9124.

LEMMA 1 (ideal lower bound; PROVED). For h >= 6 and every odd T with 5 not dividing T and 0 < |T| < sqrt(5) h/18 (about 0.124h), kappa_T >= g(|T|).

THEOREM 2 (the heavy count is sharp; PROVED, using the fundamental lemma of sieve theory). Fix xi > (ln 3)/2. Then H_d(Lambda^xi) = h Lambda^(-phi(xi) + o(1)). Rankin's bound in heavy_light Theorem 1(b) is optimal: min over a > 0 of [E(a) - 1 - a xi] = -phi(xi), at a = ln(2y)/ln 3.
Consequence for candidate (i). With heaviness kappa_T >= B and Theorem E's price of h Lambda^2 per heavy diagonal, the heavy term of Theorem N is h^2 Lambda^(2 - phi(x) + o(1)) at B = Lambda^x, and min_x max(x, 2 - phi(x)) = theta* exactly. A bound on sum kappa_T^a, or on the number of diagonals with kappa_T >= B, cannot push the exponent of this architecture below 1.4967. Two refinements change only constants or powers of ell: the type-restricted count |D_T ∩ 32Z| (upper bound only), and AKS colourings (three_term_relations Theorem 2, audited), which give chi(G_T) <= C kappa_T/log kappa_T off a set of at most 2 C1 h/B diagonals with kappa_T >= B.

PROPOSITION 3 (uniform random proper colourings; PROVED modulo the inputs of Theorem N, NOT audited). Board L***U is L*** with three changes:
- (B1') A diagonal is heavy if kappa_T >= B/4.
- (B4') On each light (T, tau), the classes are the colour classes of a uniformly random proper B-colouring chi_{T,tau} of G_T[tau], the graph G_T on the slots of type tau. The colourings are independent over (T, tau). This replaces the greedy colouring and the floor(B/c_T) split.
- (B8') Bad_split is defined from these classes as before, and all of it goes to one weighted Theorem D group with rho = 2/B.
Then:
- (a) every (T, tau) has at most B classes, each independent in G_T;
- (b) P(chi(u) = chi(v)) <= 1/(B - 2kappa_T) < 2/B for any two distinct slots of one (T, tau);
- (c) the Bad_split cost is C h^2 Lambda^2 ell^C1/B + C h^2 ell, not C h^2 Lambda^3 ell^C1/B;
- (d) under the hypotheses of Theorem N, M <= C h^2 (B + Lambda^(E(a)+1) B^(-a) + Lambda^2/B) ell^C1 + c0 n_rel tau*(h)^2 + C h^2.
So m_h <= C h^2 (log h)^1.4967 (loglog h)^C with the Bad_split family included (c = 0.5033 in the near goal), where Theorem N gives 1.5. The extra hypothesis sum c_T = O(h) of Theorem N is no longer needed.

PROPOSITION 4 (rigid placement is priced by the maximum; PROVED).
- (a) In L*** and L***U, two classes of one diagonal in one region are more than 64lp > 2600h^2 columns apart. So a region holding a (T, tau) with M classes has width > 2600h^2(M-1), whatever else it holds.
- (b) Treating a set H of diagonals rigidly costs more than 2600h^2(max over T in H of chi(G_T[tau]) - 1). A label width proportional to c_T on each diagonal (candidate (iii)) is impossible in any layout that keeps the position rule mod 16l. Moving heavy diagonals into a rigid region only moves the threshold.
- (c) Remark about the method, not a theorem: keeping B of a heavy diagonal's classes and diluting the rest through Theorem D needs a lower bound on the independence ratio of G_T. With the colourings now available (kappa_T + 1 or 4kappa_T + 1 classes of uncontrolled sizes), the provable dilution is >= 1/2 once kappa_T >= B. By Theorem 2 this changes the heavy term by a constant factor only.

PROPOSITION 5 (CONDITIONAL on hypothesis (F)). Hypothesis (F): there is K0 such that for all h and T, Cay(Z, D_T) has a periodic independent set of density >= 1/K0. This is weaker than chi(Gamma) < infinity. Under (F) and the hypotheses of Theorem N, all diagonals go to the rigid region with no Theorem E blocks, and m_h <= C h^2 log h (loglog h)^C. The exponent is 1 with the Bad_split family, and only (loglog h)^C without it.

PROPOSITION 6 (CONDITIONAL on (NR)). Hypothesis (NR): a layout with the board's validity properties whose label width is C(h * total number of classes + h^2). Under (NR) the exponent is 1 with Bad_split (by Proposition 3's colouring with 4kappa_T + 1 + Lambda colours) and 1 without it (sum chi(G_T) <= C h log h/loglog h by AKS).

ROUTE L (layers by i mod Q, CONDITIONAL on (Pc), (Eq) and (Bal), defined in Gaps). Split each (T, tau) into pieces by i mod Q (Q = Lambda^q a power of 2, Q > 32). Each piece of one j-residue gets its own rule constant kappa_rho = kappa (mod 16), placed in the same region. Classes of different j-residues never form an (E;O,E) angle (rigid note Theorem 4(c), PROVED). Under the three hypotheses the exponent is 1.2493 with Bad_split (it solves 2 - phi(3E - 2) = E, at q = 0.499 and heavy threshold Lambda^1.748), and 1 without it.

EXPONENT TABLE (with the Bad_split term / without it):
- L*** as stated (Theorem N): 1.5 / 1.4967.
- (i), better moment or count bounds for kappa-heaviness: ruled out by Theorem 2: 1.5 / 1.4967.
- (i'), type-restricted or AKS heaviness: changes only constants and powers of ell: 1.5 / 1.4967.
- Proposition 3, uniform random colouring: 1.4967 / 1.4967. This is the only proved change.
- (ii), diluting heavy diagonals with the available colourings: 1.4967 / 1.4967. A rigid heavy region: no gain (Proposition 4).
- (ii) under (F): 1 / 0 (only powers of ell).
- (iii) in rigid layouts: impossible (Proposition 4). (iii) under (NR): 1 / 1.
- Route L under (Pc), (Eq) and (Bal): 1.2493 / 1.0.
NOT PROVED: any exponent below 1.4967. Theorem N's own hypotheses still apply to Proposition 3.

## Proofs

1. PROOF OF LEMMA 1. Take T > 0 first. Work in O = Z[phi], phi = (1+sqrt5)/2. O is a PID, its units are +-phi^n, and N(phi) = -1. The prime 2 is inert (O/2 = F_4), and 5 = (sqrt5)^2 (O/sqrt5 = F_5).
- Dictionary (three_term_relations [2]). Every beta in O has the form beta = (X + L sqrt5)/2 with X = Tr beta and L in Z, and X = L (mod 2). If N(beta) = -T^2, 0 < L < h and X = T (mod 10), then d := (X - T)/10 satisfies 16d^2 + (2d+T)^2 = L^2. The reason is the identity (10d+T)^2 - 5(16d^2+(2d+T)^2) = -4T^2. Also d = 0 only when X = T.
- Generators. Let J be an ideal with N(J) = T^2. Its generators are +-phi^n beta_0. Those of norm -T^2 have n of one parity. Since beta beta' = -T^2 < 0, we have L = (beta - beta')/sqrt5 > 0 exactly when beta > 0. Hence the admissible generators are beta_j = phi^(2j) beta_+ (j in Z). Write beta_j = T e^(t_j) and beta_j' = -T e^(-t_j), with t_j = t_0 + 2j log phi. Then L = 2T cosh(t_j)/sqrt5 and X = 2T sinh(t_j). So L < h exactly when cosh t_j < R := sqrt5 h/(2T).
- Mod 2. L is odd exactly when beta mod 2 is phi or phi^2, that is, not 1. The class phi mod 2 has order 3 in F_4^*. So beta_j mod 2 = phi^(2j+m) equals 1 for exactly one residue of j mod 3, and L_j is odd for 2 of every 3 consecutive j. When L is odd, X is odd, which is X = T (mod 2).
- Mod 5. phi = 3 (mod sqrt5), so phi^2 = -1, and X = 2 beta (mod sqrt5). Hence X_j = (-1)^j X_0 (mod 5). Also X^2 = -4T^2 = T^2 (mod 5) with 5 not dividing T, so X_j = +-T. The congruence X_j = T (mod 5) holds for exactly one parity of j.
- Combining the two by CRT, 2 of every 6 consecutive j satisfy X_j = T (mod 10).
- Window. The admissible t form an open interval of length 2 arccosh R, and the lattice spacing is 2 log phi. If arccosh R > 6 log phi, the interval holds 6 consecutive t_j. Now cosh(6 log phi) = (phi^6 + phi^(-6))/2 = L_6/2 = 9 (Lucas number). So R > 9, that is T < sqrt5 h/18, gives at least 2 admissible beta for every J.
- Range. |X| < sqrt5 L < sqrt5 h, so |d| < (sqrt5 h + T)/10 < 0.237h. Also n_T >= (h-1)/2 - T/2 > 0.43h - 1 > 0.237h, so |d| < n_T holds automatically.
- Counting. Different ideals have different generators. Distinct beta give distinct X, hence distinct d. At most one beta gives d = 0, and |d| comes from at most 2 values of d. The number of ideals of norm T^2 is g(T): a split p^e gives 2e+1, and inert primes and 5 give 1. Hence kappa_T >= (2g(T) - 1)/2, so kappa_T >= g(T).
- For T < 0, use S_{-T} = -S_T, which follows from Q(-T,-d) = Q(T,d) with Q = 20d^2 + 4Td + T^2, and the same range bound for n_{-T}. []

2. PROOF OF THEOREM 2.
- Upper bound. heavy_light Theorem 1(b) (audited) holds for each fixed a. Take a = ln(2y)/ln 3 > 0. The function (3^a - 1)/2 - a xi has derivative 3^a ln3/2 - xi, which vanishes at 3^a = 2y. Its value there is y - 1/2 - y ln(2y) = -phi(xi). So H_d(Lambda^xi) <= C h Lambda^(-phi(xi)).
- Lower bound. By Lemma 1, H_d(B) >= #{n < x : n odd, 5 not dividing n, omega_s(n) >= k}, with x = h/9 (and h/9 < 0.124h), k = ceil(log B/log 3), and omega_s the number of distinct split prime factors, because g(n) >= 3^omega_s(n).
- Sieve step. Put z = x^(1/(2k)) and fix p0 = p0(y). Count n = P m where:
  - P is a product of k distinct split primes in (p0, z];
  - m <= x/P, and m is coprime to 10 and to every split prime <= z.
  This representation is unique, and each such n is counted. Since x/P >= x^(1/2) = z^k with k -> infinity, the fundamental lemma (sieve dimension 1/2, level D = (x/P)^(1/2)) gives #m >= c (x/P)(log z)^(-1/2).
- Sum over P. The sum of 1/P over k-sets is at least (S1^k - C(k,2) S2 S1^(k-2))/k!. Here S1 = sum of 1/p over split p in (p0, z], which is (1/2) loglog x - (1/2) log(2k) + O(1) by Mertens in progressions mod 5. S2 = sum of 1/p^2 over p > p0, small enough that k^2 S2/(2S1^2) <= 1/2, because k/S1 -> 2y.
- Stirling. With lambda = (1/2) loglog x and k ~ 2y lambda, S1^k/k! >= (e lambda/k)^k (loglog x)^(-O(1)) = (log x)^(y - y ln 2y) (loglog x)^(-O(1)).
- Altogether H_d(B) >= x (log x)^(-1/2 + y - y ln 2y - o(1)), and phi is continuous in y = (log B/ln 3)/loglog h. []
- Corollary. Theorem N's heavy term is C h^2 Lambda^(E(a)+1) B^(-a) ell^C. Optimised over a it is h^2 Lambda^(2 - phi(x)) ell^C, and by the two bounds this equals h * H_d * Lambda^2 up to Lambda^(o(1)). The root of x = 2 - phi(x) is 1.49674 = theta* (exponents.py). AKS remark: three_term_relations Theorem 2(1) gives chi <= C0 kappa/log kappa when R_T <= kappa^(3/2), and Theorem 2(2) gives sum (kappa_T + 1) <= 2C1 h over the other diagonals. So #{chi > B} <= H_d(c B log B) + 2C1 h/B, which differs from H_d(B) by a factor ell^(-a) only.

3. PROOF OF PROPOSITION 3.
- (a) Every vertex of G_T[tau] has degree at most 2|D_T ∩ 32Z| <= 2kappa_T < B/2. So proper B-colourings exist (greedy), and the uniform law is well defined. Colour classes are independent sets of G_T inside one (T, tau), and there are at most B of them.
- (b) Condition on chi(w) for every w != v. Each colour not used on N(v) gives exactly one proper colouring, so chi(v) is uniform on at least B - 2kappa_T > B/2 colours. If u is not in N(v), P(chi(v) = chi(u) | rest) <= 1/(B - 2kappa_T). If u is in N(v), the probability is 0. Average over the conditioning.
- (c) Bad_split. A label f is in Bad_split only if it is the designated end of a monochromatic small-height edge {f, f'} of R_IV, R_FF^oo, R_FF^ee (4 filler rows each) or R_FF^+, with f' in the same (T, tau). For each graph, the edges with f as the designated end are indexed exactly as in Theorem IV and Lemma FF': by lambda with q_lambda | u_f (one partner per lambda and end), by shapes with |U'| dividing delta'(f), and by the bounded R_FF^+. By (b) and a union bound, P(f in Bad_split) <= (2/B) times the sum over q in Q_T of 1[q | u_f or q | delta'(f)]. These are the weights of Theorem IV, so kappa_IV and kappa_FF are finite (Lemma IV, Lemma FF'). Bad_split ∩ T is a function of (chi_{T,tau}) over tau, so the sets are independent across T. The weighted Theorem D, with (AP) (audited in round 10), applies to the one group D = {light T}, |D| <= h, with rho = 2/B >= Lambda^(-C'). Its cost is C(rho kappa |D| h Lambda^2 ell^C1 + h^2 ell) <= C h^2 Lambda^2 ell^C1/B + C h^2 ell, plus an exceptional set of size h^(2-eps) sent to Proposition partial.
- (d) Heavy part. H_d(B/4) <= C 4^a h Lambda^(E(a)-1) B^(-a), and Theorem E costs C h^2 Lambda^(E(a)+1) B^(-a) ell^C. The light width is unchanged, because each (T, tau) has at most B classes. Exponent: max(x, E(a)+1-ax, 2-x). For x >= 1 the last term is at most x, so the optimum is theta* at B = Lambda^theta*, a = 0.9124. exponents.py gives 1.49675 on a grid, against 1.5 for max(x, 2-phi, 3-x).
- Compatibility, checked against consolidated_board K1-K10 and the proofs of Theorem IV and Theorem D. They use only these facts:
  - classes are G_T-independent subsets of one (T, tau), with at most B per (T, tau) (Proposition 1', Proposition R, 1(b), J4, J6 accounting);
  - the split is hereditary;
  - the random choices are independent across T and fixed before (l, p) (K6), and every first-moment family is uniform over class structures.
  None uses the greedy order or K_T except through c_T <= kappa_T + 1 in the cost, which is what changes here. Census scripts use greedy colourings, but only for numerics.

4. PROOF OF PROPOSITION 4.
- (a) In one region, every class c has n(c) = kappa (mod 16l), and its position t_c = p^(-1)(s_c - kappa) (mod 16l) depends only on s_c. So two classes of one diagonal have |Delta t| >= 16l and are at least 4p * 16l > 2600h^2 columns apart (J4). M classes of one (T, tau) need M distinct positions in one residue class, so the width exceeds 2600h^2(M-1).
- (b) Any partition of (T, tau) into G_T-independent classes has at least chi(G_T[tau]) parts. Apply (a) to the region holding the T in H with the largest chi. The bound involves the maximum, not |H| or the sum of c_T.
- (c) For a random choice of B kept classes, the average over f of P(f in Y) is at least 1 - B alpha(G_T[tau])/n, and current tools give no lower bound on alpha beyond 1/(kappa+1). With the colourings now available and kept classes chosen uniformly, P(f in Y) is about 1 - B/c_T >= 1/2 when c_T >= 2B. So the bound Theorem D gives for the heavy part is >= (1/2) h Lambda^2 H_d(2B), which by Theorem 2 has the same exponent.

5. PROOF OF PROPOSITION 5 (CONDITIONAL on (F)).
- On every (T, tau), take independent uniform translates I + tau_1, ..., I + tau_B of a periodic independent set I of density alpha >= 1/K0, restricted to the type. A translate of an independent set is independent. Class k is (I + tau_k) minus the earlier translates.
- Uncovered labels have probability (1 - alpha)^B <= Lambda^(-3) when B = ceil(3 K0 ell).
- Split each class into K iid uniform subclasses. An in-class edge is monochromatic with probability at most 1/K, with the Theorem IV weights.
- Send the uncovered labels and Bad_split to the weighted Theorem D, with rho = 1/K plus an unweighted part Lambda^(-3). The cost is C h^2 (Lambda^(-1) + Lambda^2/K) ell^C1 + C h^2 ell.
- There is no heavy region. The width is 512 x (4p 16l BK + 4A) = O(h^2 BK). With K = ceil(Lambda/sqrt B) the total is C h^2 Lambda sqrt(B) ell^C, so the exponent is 1. Without the Bad_split family, K = 1 and the cost is h^2 B ell^C.

6. PROOF OF PROPOSITION 6 (CONDITIONAL on (NR)).
- Colour each (T, tau) by Proposition 3's uniform law with B_T = 4kappa_T + 1 + B0 colours, so P(mono) <= 1/B0.
- The width is h times the sum over T of B_T, at most h^2 (8 Lambda + B0) by sum kappa_T <= 2h log h (three_term_relations [0]).
- Bad_split costs h^2 Lambda^2/B0. Take B0 = Lambda.
- Without Bad_split, use chi-colourings: h times sum chi <= C h^2 Lambda/ell.

7. ROUTE L ARITHMETIC (CONDITIONAL).
- The (E;O,E) part is proved. Let V and P be in c0, whose slots lie in one class i = r (mod Q). Then Q | t1, g = gcd(t1, T0) is odd, so Q | t', and c2 = 8qt' has j_Q = j_V (mod 8Q) (rigid note Theorem 4(c)). So a Q in a piece of another j-residue mod Q is impossible. Pieces of one diagonal never interact in this family (Theorem 2(d)).
- Each piece is coloured by Proposition 3 with B0 + 4w + 1 colours, where w = |D_T ∩ QZ|.
- Width parameter: M <= C(B0 + B1 + (Q B0 + Lambda)/384), using (Bal) and the first moment in (Eq).
- Heavy diagonals are those with w >= B1/4. By (Eq) there are h Lambda^(-phi(q + b1) + o(1)) of them.
- Bad_split costs Lambda^2/B0.
- In exponents: max(q + b0, b1, 1), 2 - phi(q + b1) and 2 - b0. At the optimum b0 = 2 - E, q = 2E - 2, b1 = E and 2 - phi(3E - 2) = E, so E = 1.24932. Without Bad_split: b0 = 0 and q = b1 = E, and 2 - phi(2E) = E gives 0.990, so the exponent is max(1, 0.990) = 1.

## External results used

- Arithmetic of Z[(1+sqrt5)/2]: PID, units +-phi^n with N(phi) = -1, 2 inert, 5 ramified, and the count of ideals of norm n. Used as in three_term_relations.md section [1] (audited note).
- Fundamental lemma of sieve theory, sieve dimension 1/2, lower-bound form (for example Halberstam-Richert, Sieve Methods, or Friedlander-Iwaniec, Opera de Cribro, Chapter 6). Theorem numbers not verified.
- Mertens' theorem for primes in the progressions +-1 mod 5: the sum of 1/p over these p up to z is (1/2) loglog z + O(1) (Dirichlet), and Stirling's formula.
- Alon-Krivelevich-Sudakov colouring theorem, only through three_term_relations Theorem 2 (audited), for the AKS remark.
- Repository inputs, used as audited: heavy_light Theorem 1(b) and Lemma 3'; Theorem E (t1_cost_decomposition); weighted Theorem D, Lemma IV and Theorem IV (polylog_relocation_diluted), with (AP) per ap_hypothesis_henriot; Lemma FF', J4 and K1-K10 (consolidated_board); rigid note Theorems 2(d) and 4(c); three_term_relations [0] and Theorem 2.

## Checks

Scripts are in scripts_heavy_term/. Each ran with py, one at a time, in under 60 s. The repository was only read.
- dsets.py: builds D_T from Pythagorean triples (4d, 2d+T, L), L < h.
  - Lemma 1 check: at h = 6000 and h = 20000, all odd T with 5 not dividing T and |T| < 0.124h were tested (596 and 1984 diagonals) with 0 violations of kappa_T >= g(T). The smallest kappa/g among g >= 9 was 2.0 and 1.89.
  - 2-adic check: the fraction of all distances divisible by 2^a at h = 6000 was 0.416, 0.164, 0.060, 0.020, 0.005 and 0 for a = 1..6. On the richest diagonals (T = +-1045, kappa = 45 at h = 20000), |D_T ∩ 2^a Z| = 22, 10, 4, 0, 0, 0. So at these heights the type-restricted graphs G_T[tau] (distances divisible by 32) have no edges even on the richest diagonals. This is a sanity check for (Eq), not a proof.
- exponents.py:
  - theta* = 1.49674 at a = 0.9124; the root of x = 2 - phi(x) is also 1.49674.
  - Rankin's optimum equals phi(x) at x = 1.2, 1.4967, 1.5, 1.75 and 2.
  - Board exponents: max(x, 2-phi, 3-x) = 1.50000, and max(x, 2-phi, 2-x) = 1.49675.
  - Route L: 1.24932 with Bad_split (x' = 1.748); 0.990 without, so the exponent there is 1.
  - Heavy fraction at the optimum: Lambda^(-0.5033).
- By hand: the dictionary identity; phi = 3 and phi^2 = -1 (mod sqrt5); phi of order 3 mod 2; cosh(6 log phi) = L_6/2 = 9; the range |d| < 0.237h < n_T; the conditional-uniformity step of Proposition 3; J4's 64lp > 2600h^2; and the CRT count of 2 of every 6 consecutive j.

## Gaps

- No second reader has audited any of these. The first to audit are Lemma 1, Theorem 2 and Proposition 3; all are short.
- Proposition 3 holds conditional on everything Theorem N assumes: the round-10 audits, U1 to U8, the completeness of the K2 and K4 lists, and the (B7) D11 relocation found by the census. My check that no downstream proof uses the greedy order covered consolidated_board.md K1-K10, Theorem IV and Theorem D of polylog_relocation_diluted.md, and its audit. I did not re-read full_layout_junctions J6 or the sea and filler notes line by line, so a grep-level confirmation is owed.
- Theorem 2's lower bound cites the fundamental lemma of sieve theory (dimension 1/2) and Mertens' theorem for primes = +-1 (mod 5). Both are standard, but I did not verify theorem numbers in a source.
- Theorem 2 is sharp for kappa-heaviness only. For heaviness by |D_T ∩ 32Z|, or by chi(G_T[tau]), it gives an upper bound only. The true counts there are open and could be smaller, though 2-adic equidistribution suggests a constant factor at most.
- Proposition 4(c) is a remark about the method, not a lower bound for m_h.
- (F) is open. It is weaker than chi(Gamma) < infinity, but it fails if Gamma has cliques of every size, which is not known either way. The K5 at T = 1045 only gives K0 >= 5.
- (NR) is open. It is the rigid note's Missing estimate (B), and no non-rigid cross-block kill is known.
- Route L needs three open hypotheses. (Pc): every Table-T family whose kill uses n(c) = n(c') (mod l) also dies, or hits O(h^(2-delta)) labels, for class pairs in one type but different j-residues mod Q, including pairs on the same diagonal. These are Proposition 1(c), Proposition 1(d), Lemma L-adic (i)(ii), J4, and the random-l first moments behind A4 and B7. Only (E;O,E) is proved. (Eq): #{T : |D_T ∩ QZ| >= M} <= h Lambda^(-phi(log_Lambda(QM)) + o(1)), plus the first moment sum_T Q |D_T ∩ QZ| <= C h Lambda, for Q = 2^a <= Lambda^C. Data at h = 6000 and 20000 show the fraction of distances divisible by 2^a decaying faster than 2^(-a), but nothing is proved. (Bal): layer constants kappa_rho exist with max_r load(r) <= C(max piece colours + average load). With random kappa_rho the Chernoff maximum adds a factor of about Lambda/ell, which destroys the gain.
- Remark about the method, not a theorem: in every variant here, in-class Bad_split labels are relocated at Lambda^2 each while the rigid width grows with the number of classes per (T, tau). So exponent 1 is a floor for this architecture unless Theorem D's price per relocated label drops below Lambda^2.
- m_h = O(h^2) is not addressed beyond these conditional routes.

## Missing estimate

To go below 1.4967, the heavy diagonals need a price below h Lambda^2 each, or heaviness must be measured by something smaller than kappa_T. Theorem 2 shows that counting kappa-heavy diagonals more carefully cannot help. The most concrete arithmetic target is (Eq), a 2-adic moment bound: for Q = 2^a <= (log h)^C and every b in a fixed compact range, sum over T of |D_T ∩ QZ|^b << Q^(-b) h Lambda^(E(b)-1+o(1)). In ideal terms, this asks how Tr(beta) mod 2^(a+1) is distributed over the generators beta of norm -T^2. It should follow from equidistribution of split prime ideals of Z[phi] in ray classes mod 2^(a+1), uniform in the modulus up to (log h)^C (Siegel-Walfisz type for Hecke characters). Expanding the condition Tr beta = T (mod 2^(a+1)) in characters makes |D_T ∩ QZ| a combination of multiplicative functions of T, which is the shape Lemma 3' handles. To make Route L pay, (Eq) must be combined with (Pc), the cross-layer kills of the l-adic families, and with (Bal). The other way down is (F), a uniform lower bound on the independence density of Cay(Z, D_T).

## Next steps

- Audit Lemma 1, Theorem 2 and Proposition 3. If they pass, change Theorem N's statement to exponent theta* = 1.4967 with Bad_split, and drop the extra hypothesis sum c_T = O(h).
- Grep full_layout_junctions.md (J6), sea_census_rigid.md, saw_residual_families.md and v3_and_cross_block.md for any use of the greedy order or of K_T, to confirm the compatibility claim of Proposition 3.
- Attack (Eq). Write |{beta : N(beta) = -T^2, Tr beta = T mod 2^(a+1)}| as a character sum over (O/2^(a+1))^*, bound the nontrivial-character products prime by prime, and run Lemma 3' with the averaged Euler factors.
- Check (Pc) family by family for pieces in one type with different j-residues mod Q. Start with Lemma L-adic (i)(ii) and Proposition 1(c),(d), where Dj and Dn are no longer controlled mod l. Look for a 2-adic substitute that uses the i-residue mod Q of both classes.
- Test (F) numerically: compute the independence density of Cay(Z_P, D_T mod P) for the richest diagonals (T = 1045c and the top-kappa T at h of about 2*10^4) by exact or SAT search. If it stays bounded while chi grows, (F) becomes the cleanest route to exponent 1.
- Do not spend effort on sharper moment bounds for kappa-heaviness. Theorem 2 shows they cannot move the exponent.

