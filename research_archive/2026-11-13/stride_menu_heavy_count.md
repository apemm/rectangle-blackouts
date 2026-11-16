# The heavy count for a menu of strides

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: Theorem M1. For a menu of m strides 4u (u odd, the fields Q(sqrt(4u^2 + 1)) independent), the sum over T of min_i kappa_T^(i)^a is at most C h Lambda^(beta_m(a)) with beta_m(a) = ((1 + 3^(a/m))/2)^m - 1, from audited inputs. Theorem LB gives a matching lower bound for menus of prime discriminants with class number 1, for example strides {4, 12, 20, 28, 52}. Theorem X: the exponent is x_m = 1.4967, 1.4295, 1.3987, 1.3807, 1.3690, 1.3606 for m = 1 to 6, decreasing to 1.3108. Theorem E, Proposition partial and J5 do not depend on the stride. The bound on m_h holds only if the stride-4u board is valid. Not audited yet.

# Result

## Status

proved

## Summary

I proved the menu heavy count for strides 4u, sum_T min_i kappa_T^(i)^a <= C h Lambda^(beta_m(a)) with beta_m(a) = ((1+3^(a/m))/2)^m - 1, and a matching lower bound for menus of up to 5 strides. Fed into the board, the exponent is x_m = 1.4967, 1.4295, 1.3987, 1.3807, 1.3690, 1.3606 for m = 1..6, tending to 1.3108. Theorem E, Proposition partial and J5 do not depend on the stride. The bound on m_h holds only if the stride-4u board is valid.

## Statements

Notation. Lambda = log h and ell = loglog h. U = {u_1, ..., u_m} is a menu of odd u_i with Delta_i = 4u_i^2 + 1, and no product over a nonempty subset of the Delta_i is a square. sigma_i = 2u_i is half the stride s_i = 4u_i. kappa_T^(i) = |D_T^(sigma_i)|, with D_T^(sigma) as in stride_menu.md Derivation 2: the distinct |d| with 0 < |d| < n_T and (4u d)^2 + (2d+T)^2 = L^2 for some 0 < L < h. kappa_T^U = min_i kappa_T^(i). H^U(B) = #{odd T, 0 < |T| < h : kappa_T^U >= B}. A_a = (1 + 3^(a/m))/2 and beta_m(a) = A_a^m - 1, so beta_1(a) = E(a) - 1. phi_m(xi) = sup_{b>0} (b xi - beta_m(b)), its Legendre transform.

THEOREM M1 (menu moment and heavy count; PROVED from audited inputs). For every fixed a > 0 there is C = C(a, U) with, for all h >= 4,
 sum over odd T, 0 < |T| < h, of (kappa_T^U)^a <= C h Lambda^(beta_m(a)).
Hence H^U(B/4) <= C 4^a h Lambda^(beta_m(a)) B^(-a) for every B >= 1. For xi > ln3/2, with a = a(xi) fixed, H^U(Lambda^xi) <= C h Lambda^(-phi_m(xi)).
This is heavy_light_split Theorem 1(b) (audited in audit_heavy_light_split.md, with the Kronecker-form Lemma 2), written out for the strides 4u.

THEOREM LB (matching lower bound; PROVED for menus that satisfy (LB-hyp), modulo standard facts). Hypothesis (LB-hyp): every Delta_i is prime and Q(sqrt Delta_i) has class number 1. Example: U5 = {1, 3, 5, 7, 13}, strides {4, 12, 20, 28, 52}, Delta = {5, 37, 101, 197, 677}; I verify class number 1 by the Minkowski bound. Under (LB-hyp):
 (a) for every fixed a > 0, sum over odd 0 < T < h of (kappa_T^U)^a >= h Lambda^(beta_m(a) - o(1));
 (b) for every fixed xi > ln3/2, H^U(Lambda^xi) >= h Lambda^(-phi_m(xi) - o(1)).
So Theorem M1 is sharp, and the geometric-mean step loses nothing in the exponent. The ingredient is Lemma L: kappa_T^(i) >= g_i(T)/6 for odd T coprime to Delta_i with 0 < T < c_i h, plus one designated prime q_i dividing T exactly once when the fundamental unit is 1 mod 2.

THEOREM X (exponent; arithmetic, PROVED). x_m := min over a > 0 of (beta_m(a) + 2)/(1 + a). Equivalently, x_m is the root of x + phi_m(x) = 2, and x_m = beta_m'(a*) = (ln3/2) 3^(a*/m) A_(a*)^(m-1).
 m=1: 1.4967429 (a* = 0.912415); m=2: 1.4295234 (1.105665); m=3: 1.3986920 (1.209672); m=4: 1.3807491 (1.275681); m=5: 1.3689530 (1.321566); m=6: 1.3605885 (1.355404); m=10: 1.3424579 (1.432808).
 Limit: x_inf = min_a (1 + 3^(a/2))/(1 + a) = 1.3108172 (a* = 1.583361). x_m decreases strictly in m, because A_a^m is the power mean of 1 and 3^a with exponent 1/m.
At the optimum the heavy fraction is Lambda^(x_m - 2), and the Bad_split exponent 2 - x_m is below x_m.

THEOREM W (CONDITIONAL on (V_u) for every u in U, and on everything Theorem N v4 assumes). (V_u) is defined in the proof, section 6. Build the menu board as follows:
- A diagonal T is light if kappa_T^U < B/4. It goes to the least i with kappa_T^(i) = kappa_T^U, into the stride-4u_i chain L***(u_i).
- A diagonal is heavy if kappa_T^(i) >= B/4 for every i. Its labels in S go to the single Theorem E instance, and the rest go to Proposition partial.
Then M <= C h^2 (B + Lambda^(beta_m(a)+2) B^(-a) + Lambda^2/B) ell^C + C m h^2 ell + o(h^2), so m_h <= C h^2 (log h)^(x_m) (loglog h)^C.
Theorem DC is not needed for the exponent. With DC in place of the Bad_split route, the exponent is max(x_m, eta) for every eta > 0.

STRIDE-FREE CHECKS (PROVED by reading the statements).
- Theorem E (t1_cost_decomposition, A-6) takes any set H of diagonals at cost C(|H| h Lambda^2 ell^C + h^2 ell).
- Proposition partial (sec5) takes any set of parity edges.
- J5 glues any number of violation-free blocks with constant tails, given windows more than 2W_h apart.
- So the chains of different strides glue at an extra cost of O(m h^2).

NOT PROVED: (V_u) for any u >= 3. No new unconditional bound on m_h; Theorem N stays at theta* = 1.4967429. m_h = O(h^2) is not proved.

## Proofs

All inputs are notes in research_archive/2026-11-13 unless a path says otherwise. They are used as audited: stride_menu Lemma 2 in its Kronecker form (audits_stride_menu_and_gamma.md), Proposition 1', Lemma 4, and heavy_light Lemma 3' and Theorem 1(b) (audit_heavy_light_split.md).

1. PROOF OF THEOREM M1.
Setup.
- For stride 4u, sigma = 2u. So s^2 = 16u^2 and s^2 + 4 = 4 Delta.
- Corrected Lemma 2 gives k_T^(sigma) <= tau(sigma^2) g_sigma(T)(1 + 2 log(3h/|T|)/log phi).
- Here g_sigma(T) is the product of (2e+1) over p^e || T with chi_sigma(p) = 1, and chi_sigma is the Kronecker character of Q(sqrt Delta).
- The step Y^2/n < (3h/T)^2 holds at every u: Y = 2 sqrt(Delta) h and n = sigma^2 T^2, so Y^2/n = (1 + 1/(4u^2)) h^2/T^2 <= (5/4) h^2/T^2.
- Since 1 + 2x/log phi <= (2/log phi)(1 + x), kappa_T^(i) <= C3 (1 + log(3h/|T|)) g_i(|T|), with C3 = max_i tau(4u_i^2) · 2/log phi.

Reduction to one multiplicative function.
- (kappa^U)^a = min_i (kappa^(i))^a <= C3^a (1 + log(3h/|T|))^a min_i g_i^a.
- A minimum is at most the geometric mean, so min_i g_i^a <= prod_i g_i^(a/m) = F_a(|T|).
- F_a is multiplicative, with F_a(p^e) = (2e+1)^(a N(p)/m) <= (2e+1)^a and N(p) = #{i : chi_i(p) = 1}.

Prime sum.
- For p not dividing 2 prod Delta_i, F_a(p) = prod_i (A' + B' chi_i(p)), with A' = A_a and B' = (3^(a/m) - 1)/2. Check: chi = 1 gives 3^(a/m), and chi = -1 gives 1.
- Expanding the product gives sum over U' of A'^(m-|U'|) B'^|U'| chi_U'(p).
- For U' nonempty, chi_U' agrees off finitely many primes with the Kronecker character of Q(sqrt(prod_{U'} Delta_i)). That character is nonprincipal because the product is not a square. So sum_p chi_U'(p)/p converges (Dirichlet: L(1, chi) != 0).
- The finitely many p dividing 2 prod Delta contribute O(1).
- Mertens then gives sum_{p<=x} F_a(p)/p = A_a^m loglog x + O(1).
- Lemma 3' gives S_a(x) := sum_{n<=x} F_a(n) <= C x (log x)^(A_a^m - 1).

Partial summation.
- Use the weight w(t) = (1 + log(3h/t))^a, exactly as in relocation_price_exponent Lemma K. This works for every a > 0, and A_a^m >= 1.
- The result is sum_{t<h} w(t) F_a(t) <= C h Lambda^(beta_m(a)). Both signs of T give a factor 2.

Consequences.
- Markov's inequality gives H^U(B/4) <= (4/B)^a times the sum.
- For xi > ln3/2 = beta_m'(0), take b with beta_m'(b) = xi. This b exists because beta_m' increases from ln3/2 to infinity. Then beta_m(b) - b xi = -phi_m(xi). []

2. LEMMA L (per-stride lower bound; PROVED).
Setting.
- Let u be odd, Delta = 4u^2 + 1 prime, and K = Q(sqrt Delta) with class number 1.
- O_K = Z[w] with w = (1 + sqrt Delta)/2.
- 2 is inert in K, because Delta = 5 (mod 8) for u odd. So O_K/2 = F_4, and conjugation acts on F_4 as Frobenius.
- 𝔮 = (sqrt Delta) is ramified, with O_K/𝔮 = F_Delta.
- Let eta > 1 be the fundamental unit. Since sigma + sqrt Delta has norm -1, N(eta) = -1.
- Case B: eta is not 1 mod 2. Then eta has order 3 in F_4^*. Examples: Delta = 5 (eta = phi), and Q(sqrt 13).
- Case A: eta = 1 mod 2. Then every unit is 1 mod 2, and psi(J) := (a generator of J) mod 2, a value in F_4^* = mu_3, is a well-defined multiplicative function on ideals prime to 2. Examples (checked by script): Delta = 37, 101, 197, 677, with eta = 2u + sqrt Delta.
- In case A, let q be a split prime with psi(𝔮_q) != 1. Then psi of the conjugate ideal is psi(𝔮_q)^2, which is also != 1. Examples: q = 3 for 37 (2 + w, norm -3, w mod 2); q = 17 for 101 (6 + w); q = 7 for 197 (7 + w = 1 + w); q = 13 for 677 (13 + w).

Claim.
- Let T be odd with gcd(T, Delta) = 1 and 0 < T < c_Delta h, where c_Delta = sqrt(Delta)/(2u cosh(N log eta)), with N = 2 in case A and N = 6 in case B. In case A, assume also q || T.
- Then kappa_T^(sigma) >= g(T)/6 in case A and >= g(T)/2 in case B. Here g(T) is the product of (2e+1) over split p^e || T.

Proof.
(i) Dictionary.
- Put X = 2 Delta d + T. Then (4ud)^2 + (2d+T)^2 = L^2 is equivalent to X^2 - Delta L^2 = -sigma^2 T^2. Expand: Delta(16u^2 d^2 + (2d+T)^2) = (2 Delta d + T)^2 + (Delta - 1) T^2.
- Conversely, integers X and L with that norm equation, X = T (mod 2 Delta) and 0 < L < h give an integer d.
- d = 0 exactly when X = T and L = T, which is one alpha = X + L sqrt Delta.
(ii) Construction.
- Every ideal J0 with N(J0) = T^2 is principal. Pick a generator delta0 with N(delta0) = +T^2, using the norm -1 unit if needed.
- Put alpha_k = 2u eta^(2k+1) delta0 for k in Z, with the overall sign chosen so that alpha_0 > 0. Then N(alpha_k) = -4u^2 T^2.
- Since eta^2 > 0 and alpha_k' = eta^(-2k) alpha_0', we get alpha_k > 0 > alpha_k' for every k. So L_k = (alpha_k - alpha_k')/(2 sqrt Delta) > 0.
- Write alpha_k = 2 gamma_k with gamma_k in O_K. Then alpha_k lies in Z[sqrt Delta], with X = 2a + b and L = b, where gamma_k = a + bw.
(iii) Congruences.
- Parity: X is odd exactly when b is odd, that is when gamma_k mod 2 is not in F_2, that is when gamma_k mod 2 != 1.
- Mod 𝔮: alpha_k^2 = alpha_k alpha_k' = -sigma^2 T^2 = T^2 (mod 𝔮), so alpha_k = ±T (mod 𝔮). Because 𝔮 is ramified, eta' = eta (mod 𝔮), so eta^2 = eta eta' = -1 (mod 𝔮). So the sign alternates with k, and X = T (mod Delta) holds for exactly one parity of k.
- Mod 2, case B: gamma_k = eta^(2k+1) delta0 runs through all of F_4^* with period 3, so 2 of every 3 consecutive k have the right parity. With the CRT, 2 of every 6 consecutive k satisfy both conditions.
- Mod 2, case A: gamma_k = delta0 (mod 2) for every k. The parity holds exactly when psi(J0) != 1, and then 1 of every 2 consecutive k satisfies both conditions.
(iv) Window.
- Write alpha_k = 2uT e^(t_k) with t_k = t_0 + 2k log eta. Then L_k = 2uT cosh(t_k)/sqrt Delta.
- L_k < h exactly when cosh t_k < R := sqrt(Delta) h/(2uT).
- The admissible t form an interval of length 2 arccosh R, and the lattice step is 2 log eta. So R > cosh(N log eta) puts N consecutive k in the window, and T < c_Delta h guarantees that.
(v) Range.
- |X| < sqrt(Delta) h, so |d| < h/(2 sqrt Delta) + T/(2 Delta) < 0.25h.
- n_T >= (h - T)/2 > 0.45h, so |d| < n_T holds automatically.
(vi) Count in case A.
- J0 = prod over split p of 𝔭^a 𝔭'^(2e-a), times the inert parts, and psi((p)) = 1.
- For split p with psi(𝔭) = zeta != 1, the local sum of psi^r is sum_{a=0}^{2e} zeta^(2r(a-e)). At q, where e = 1, it is zeta^(-2r) + 1 + zeta^(2r) = 0 for r = 1, 2.
- So the number of J0 with psi(J0) = 1 is (1/3) sum over J0 of (1 + psi + psi^2) = g/3, and 2g/3 of the J0 are good.
(vii) Distinctness and conclusion.
- Distinct pairs (J0, k) give distinct alpha, and distinct alpha give distinct d.
- Removing d = 0 and folding d to |d| gives kappa >= (#good - 1)/2.
- Case A: kappa >= (2g/3 - 1)/2 >= g/6, since g >= 3 (q splits).
- Case B: kappa >= (2g - 1)/2 >= g/2. []

Class number 1 by the Minkowski bound sqrt(Delta)/2.
- Delta = 37: 3 splits, and 2 + w has norm -3.
- Delta = 101: 5 splits, and 4 + w has norm -5.
- Delta = 197: 3 and 5 are inert, 7 splits, and 7 + w has norm 7.
- Delta = 677: 3, 5, 7 and 11 are inert, 13 splits, and 13 + w has norm 13.
- 2 is inert in all of them, and Q(sqrt 5) is trivial.
The script classno1.py reproduces these. It did not certify any field with u in [15, 79]; there Delta is composite (genus theory makes h even), or the search failed, as for 2917.

3. PROOF OF THEOREM LB.
Setup.
- lambda = 2^(-m). For a prime p not dividing 2 prod Delta_i, its pattern epsilon(p) is in {0,1}^m, with epsilon_i = 1 exactly when chi_i(p) = 1.
- The indicator of pattern epsilon is lambda times sum over U' of ±chi_U'(p). So S_eps(y) := sum over p <= y with pattern epsilon of 1/p equals lambda loglog y + O(1).
- Fix nu_eps > 0. Let x = c_* h, where c_* = min_i c_(Delta_i) is a constant. Put L = loglog x, k_eps = floor(nu_eps L), k = sum k_eps and z = x^(1/(4k)).
- Fix p0 larger than every prime of 2 prod Delta_i and every designated q_i, with p0 >= 2 max (nu_eps/lambda)^2 + 2.
- Q0 = prod of the q_i over the case-A strides.

The constructed diagonals.
- Count T = Q0 P m, where:
  - P is a product of k_eps distinct primes of pattern epsilon in (p0, z], for each epsilon;
  - m is a prime in (z, x/(Q0 P)].
- Each such T is odd, coprime to every Delta_i, has q_i || T, and satisfies T < x.
- The representation is unique: P is the part of T/Q0 made of primes in (p0, z].
- Lemma L applies at every stride, so min_i kappa_T^(i) >= (1/6) min_i g_i(T) >= (1/6) min_i 3^(w_i).
- Here w_i = sum over epsilon with epsilon_i = 1 of k_eps, and g_i(T) >= g_i(P) because g_i(Q0 m) >= 1.

Counting.
- P <= z^k = x^(1/4), so x/(Q0 P) >= x^(3/4)/Q0. By Chebyshev, the number of choices of m is at least c x/(Q0 P log x).
- So the sum over T < x of (kappa^U)^a is at least c (x/log x) 3^(a min_i w_i) times sum_P 1/P.
- For each epsilon, sum over k_eps-sets of distinct primes of prod 1/p >= (S^(k_eps) - C(k_eps, 2) S2 S^(k_eps - 2))/k_eps!. Here S2 = sum_{p > p0} p^(-2) <= 1/p0, so the bracket is at least S^(k_eps)/2.
- The primes of different patterns are disjoint.
- S_eps over (p0, z] equals lambda L (1 + o(1)), since loglog z = L - log(4k).
- Stirling gives sum_P 1/P >= exp(L sum_eps nu_eps (1 + ln(lambda/nu_eps)) - o(L)).

Optimisation.
- (a) Take nu_eps = lambda 3^(a|eps|/m). By symmetry each w_i equals L lambda 3^(a/m) (1 + 3^(a/m))^(m-1) + O(1).
  - sum_eps nu_eps = A_a^m.
  - sum_eps nu_eps ln(lambda/nu_eps) = -(a ln3/m) sum_eps |eps| nu_eps, and this cancels a ln3 · w_i/L exactly.
  - The total exponent is A_a^m - 1 = beta_m(a).
- (b) Take nu_eps = lambda 3^(b|eps|/m) with beta_m'(b) = xi + delta, using the identity lambda 3^(b/m)(1 + 3^(b/m))^(m-1) ln3 = beta_m'(b).
  - Then min_i kappa >= Lambda^xi for large h.
  - The count exponent is A_b^m - 1 - b beta_m'(b) = -phi_m(xi + delta).
  - Let delta -> 0, using the continuity of phi_m. []
The only external facts are Dirichlet/Mertens for real characters, Chebyshev, Stirling, the Minkowski bound and ideal counting in quadratic fields. No sieve lemma is needed: making m prime costs a factor 4k = O(ell), which is Lambda^(o(1)).

4. PROOF OF THEOREM X.
- (beta_m(a) + 2)/(1 + a) equals 2 at a = 0 and tends to infinity as a grows. Its derivative at 0 is (log 3)/2 - 2 < 0, so the minimum over a > 0 is attained in (0, infinity). (Corrected 15 November 2026: the earlier wording said it tends to infinity at both ends. The conclusion is unchanged.)
- At a stationary point, beta_m'(a)(1 + a) = beta_m(a) + 2, and the value there is beta_m'(a*).
- Duality: min_x max(x, min_a (beta_m(a) + 2 - a x)) = min_a (beta_m(a) + 2)/(1 + a), by the infimum swap of relocation_price_exponent Lemma O1. The inner minimum is 2 - phi_m(x).
- So x_m is the root of x = 2 - phi_m(x). The script's bisection agrees to 1e-7 for m = 1, 2, 5 and the limit.
- As m -> infinity, A_a^m -> 3^(a/2) (the power mean with exponent tending to 0 is the geometric mean).
- At the optimum, beta_m - a x_m = x_m - 2.
The values come from golden-section search, cross-checked on a grid of step 5e-5. They are not certified by interval arithmetic.

5. PROOF OF THEOREM W (CONDITIONAL).
Inputs: (V_u) for every u in U, and everything Theorem N v4 assumes. B = Lambda^x.

Assignment.
- i(T) depends only on the deterministic kappa^(i). So it is fixed before (l, p) and chi, which K6-v3 needs.
- Every label lies in exactly one destination, so the doubles carry each parity edge exactly once (J5 and K8').

Light chains.
- Chain u has its own primes l in (1.04h, 2.08h] and p in (P_u h, 2 P_u h], with P_u = max(40, 8u^2 + 4). This gives p > (s^2/2 + 4)h, the hypothesis of stride_menu Lemma 4 and heavy_light Proposition R.
- On the slots of type tau of a light T, the degree in G_T^(i(T))[tau] is at most 2 kappa^(i(T)) < B/2. So the uniform proper B-colouring exists, and Proposition 3 (a) and (b) hold verbatim.
- The slot is n = u i + p t + b with t < 16lB, so the width per type is <= 4 · 2 P_u h · 16 · 2.08h · B (1 + o(1)).
- Over 512 types this is 136314.88 P_u B h^2 (P_u = 40 recovers v4's 5452595.2 B h^2). So the width scales with s^2 (8u^2 = s^2/2).
- Sum over U: C_U B h^2, with C_U = 136314.88 sum_i P_(u_i).

Heavy part.
- One Theorem E instance with Delta = H^U(B/4) <= C 4^a h Lambda^(beta_m(a)) B^(-a) by Theorem M1.
- Cost: C h^2 Lambda^(beta_m(a)+2) B^(-a) ell^C + C h^2 ell.
- Since kappa^U <= kappa^(stride 4), the heavy set is contained in v4's heavy set.

Bad_split and Theorem D.
- One weighted Theorem D group over all light T, or one group per chain, with rho = 2/B. Cost C h^2 Lambda^2 ell^C/B. This is part of (V_u) for u >= 3.

Other terms.
- Proposition partial: c0 sum_u n_rel^(u) tau*(h)^2 = o(h^2), by (V_u).
- Each chain is its own J5 window, glued with gaps of 2W_h + 1. So V4-1's window count grows by O(m), and the cost is O(m h^2).
- N1 collars: O(h^2 ell).

Total and exponent.
- M <= C h^2 ell^C (Lambda^x + Lambda^(beta_m(a)+2-ax) + Lambda^(2-x)) + O(m h^2 ell) + o(h^2).
- The exponent is max(x, beta_m(a) + 2 - ax, 2 - x). At x = x_m and a = a* the middle term equals x_m, and 2 - x_m < 1 < x_m.
- Truncation and the passage to m_h are as in Theorem N v4 section 5.
- With DC, the exponent is max(x_m, eta), as in relocation_price_exponent Theorem P(b). []

Stride-free checks.
- Theorem E: its statement takes any H, and its proof (E1)-(E5) uses only the label rows 2i+1 and 2i+T+1 and T1/T2's profiles.
- Proposition partial: the paper's statement takes any set F of parity edges.
- J5: its proof uses only the 2W_h + 1 locality, separated windows, constant tails, and each edge carried once.
- For u = 1, a stride-4 chain that holds only part of the light diagonals is covered by J3, which is stated for arbitrary Y0, and by the monotonicity of every counted family in the label set. I checked this by reading only, without an audit.

6. HYPOTHESIS (V_u), u >= 3 odd. The chain L***(u) is L***U with:
- slot n = u i + p t + b and column 4n;
- p in (P_u h, 2 P_u h];
- the same 512 types, filler law, colouring law and destinations.
The chain is assumed to satisfy every claim that Theorem N v4 makes of the stride-4 chain:
- validity of the chain with row-1 tails, after Bad_split, R-e and R-f leave;
- the Theorem D hypotheses (i), (ii) and (AP) for its Bad_split, with rho = 2/B;
- n_rel^(u) = O(h^(2-delta)) through Theorem U and the deterministic counts;
- J1 and J2 seams and the J1* phase table.
What transfers by reading: Proposition 1', Lemma 4 and Proposition R hold at every even stride. Their 2-adic step needs only v2(sigma) = 1, which u odd keeps. Theorems D and E, P1-P3, A-14, A-16, A-18 and A-19 transfer in form (degree_capped_colouring Proposition S).
What must be redone at ratio r = 4u, by the inventory in Proposition S:
- the in-class cubic, Theorem F at r = 4u, for two_filler (A-20) and R_IV / R_FF;
- block_sea Theorems 1-2 (A-1), rigid Theorem C (A-2), mixed_quadruples 1-4 (A-3) and the v3 cells (A-15), which use Delta = mu Dt;
- Lemma N, Q3, Q4, Theorem K and K2/K4/S1L (A-23 to A-26);
- the SAW* deep layer, Table J1* and BH16 (A-9, A-12, A-21, A-22), since labels sit at slot gaps 32u;
- the K4 constants that use p <= 80h, for example U1's (40h)^2.

## External results used

- Dirichlet: L(1, chi) != 0 for a nonprincipal real character, so sum_p chi(p)/p converges. Mertens: sum_{p<=x} 1/p = loglog x + O(1). Textbook results; I did not look them up.
- Chebyshev: pi(y) >= y/(2 log y) for large y. Stirling's bound k! <= e sqrt(k) (k/e)^k.
- Real quadratic fields: the ideals of norm n are counted by sum_{d|n} chi_K(d); the splitting of odd p is given by the Legendre symbol, and 2 is inert when Delta = 5 mod 8; the Minkowski bound sqrt(d_K)/2 for class number checks; units are ±eta^k. Textbook (Hardy and Wright, chapters XIV and XV).

## Checks

I ran three scripts in the script folder, one at a time with py -I, each under 60 s.
- expo_menu.py: x_m by golden-section search and by a grid, plus the Legendre root of x = 2 - phi_m(x). The two agree to 1e-7, and m = 1 reproduces theta* = 1.4967429.
- lemmaL_check.py: brute-force kappa_T^(sigma) from the definition, compared with Lemma L's bound.
  - h = 20000: u = 1 (994 diagonals), u = 3, 5, 7 and 13.
  - h = 120000: u = 3 (180 diagonals), 5 (17), 7 (19) and 13 (3).
  - 0 violations. The smallest kappa/g is 0.889, well above the proved 1/6.
  - It also confirms case A (the fundamental unit lies in Z[sqrt Delta]) for 37, 101, 197 and 677, and case B for 5.
- classno1.py: the Minkowski-bound check of class number 1. Proved for u in {1, 3, 5, 7, 13}; not shown for any other u up to 79.
By hand: Lemma L's dictionary identity, unit sign and window, the F_4 Frobenius action, the local sums at q, the large-deviation cancellation, and the Theorem W width count. P_u = 40 recovers v4's constant 5452595.2.
I read in full or in the needed parts: stride_menu.md, its audit, heavy_light_split.md and its audit, heavy_diagonals_sharp.md, relocation_price_exponent.md, consolidated_board_v4.md (statement, B0-B10 and section 5), full_layout_junctions.md (J5), the Theorem E statement in t1_cost_decomposition.md, Proposition partial in sec5_threshold.tex, and Proposition S of degree_capped_colouring.md.

Files: scripts_menu_count/expo_menu.py, scripts_menu_count/lemmaL_check.py, scripts_menu_count/classno1.py.

The repository was only read. I ran no git command and used no web source.

## Gaps

- Theorem W is conditional on (V_u) for each u >= 3 in the menu, that is, on the stride-4u board being valid. About 20 audited inputs must be redone at ratio 4u (degree_capped_colouring Proposition S inventory). Until that is done, no exponent below theta* = 1.4967429 is proved for m_h.
- Theorem LB covers only menus with Delta_i prime and class number 1. I certified 5 such fields (u = 1, 3, 5, 7, 13), so the lower bound is proved for m <= 5. For m = 6 and the limit it is open. u = 9 (Delta = 325, order Z[5 sqrt 13]) and composite Delta need a ray-class version of Lemma L that I did not write. The upper bound and the exponent table hold for every m.
- Lemma L case A needs a designated prime q_i || T. Without it, the count can drop to 0 on the thin set where every split prime has psi = 1. This does not affect the exponent, but it shows the per-diagonal bound kappa >= c g is false in general at strides 12, 20, 28 and 52.
- No second reader has audited Lemma L, Theorem LB or the stride-free reading. Theorem M1 is heavy_light Theorem 1(b), which is audited.
- The u = 1 claim that a stride-4 chain holding only a subset of the light diagonals is covered by J3 and the monotonicity of the counted families comes from reading only. It has not been audited.
- Constants are non-explicit (Dirichlet character sums), and h0 is not explicit. The menu's light constant is sum P_u/40 times v4's: 51.8 for U5 and 2.9 for {1,3}. So the gain is asymptotic only. For example, at m = 5 it needs Lambda^0.128 > 34.
- The exponent values are floating-point minimisations agreeing to about 1e-7, not interval-certified.

## Missing estimate

To turn Theorem W into a theorem about m_h, one thing is missing: (V_u) for u >= 3. The stride-4u chain must satisfy, at ratio 4u, every claim Theorem N v4 makes of the stride-4 chain: validity, the Theorem D hypotheses, and n_rel = O(h^(2-delta)). The count side is closed. By Theorems M1 and LB, the heavy moment is h Lambda^(beta_m(a) +- o(1)), so no counting improvement can lower x_m within menu-heaviness at relocation price Lambda^2.

## Next steps

- Attack (V_3) first. The menu {4, 12} already gives 1.4295 (x_2). Redo Theorem F's cubic at r = 12 and the inventory of Proposition S, keeping v2(s) = 2 so that the 2-adic steps (Proposition R, types mod 32) carry over.
- Have a second reader audit Lemma L and Theorem LB (about 1.5 pages), then add a ledger row: 'menu heavy moment h Lambda^(beta_m(a) +- o(1)), sharp, m <= 5'.
- To extend Theorem LB to every m, prove a ray-class version of Lemma L for composite or non-squarefree Delta. Alternatively, find more prime Delta = 4u^2+1 with class number 1 by a proper class-number computation.
- Since Theorem LB makes x_m exact for menu-heaviness at price Lambda^2, going below 1.3108 needs a heavy price below Lambda^2 or a heaviness measure finer than kappa. One finer measure is splitting one diagonal's residue classes across strides, which leads to the (Eq)-type 2-adic moments of heavy_diagonals_sharp.

