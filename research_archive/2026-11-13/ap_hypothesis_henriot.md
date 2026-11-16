# Hypothesis (AP) from Henriot

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: hypothesis (AP) holds, even for moduli up to h^(1-eta), from the corrected Theorem 5 of Henriot (2014 erratum). The weighted Theorem D follows, and Theorem IV no longer needs (AP). Not audited yet.

# Result

## Status

proved

## Summary

(AP) is proved as stated, even for moduli up to h^(1-eta), from Henriot's corrected Theorem 5 (2014 erratum, which I read in full). The Euler factors at primes dividing q cost nothing and the 1/q comes from the length of the progression. The tau(q)^C comes only from the contents of the substituted forms. As a result the weighted Theorem D holds with rho*kappa*ell^C in place of rho, and Theorem IV loses its (AP) hypothesis.

## Statements

NOTATION. Lambda = 1 + log h, ell = 1 + loglog(3h). tau_+(0) = 1. A "form" is an integer affine form. "Bounded" means bounded by a constant A0 fixed in advance. All constants depend only on A0, the number of forms, the exponent range s in [0,3], and eta.

LEMMA 1 (one variable, AP form of T2 (7) and of sharper (3) to (5); PROVED).
- Fix eta in (0,1) and k <= 4.
- Let A_j(t) = a_j t + b_j (j = 1..k) have 1 <= |a_j| <= A0, |b_j| <= A0 h, and be pairwise non-proportional (a_i b_j != a_j b_i).
- Each f_j is tau^(s_j) or tau(.^2)^(s_j), with s_j in [0,3]. Put c_j = f_j(p), which is 2^(s_j) or 3^(s_j).
- Let I be an integer interval of length <= A0 h, 1 <= q <= h^(1-eta), and t0 in Z.
Then
 S := sum over t in I with t = t0 (mod q) and prod A_j(t) != 0 of prod_j f_j(|A_j(t)|) <= C (h/q) tau(q)^(C') Lambda^(c_1+...+c_k-k) ell^(C0).
Here C' = 2(s_1+...+s_k), and C0 depends only on k and the s-range. With c = 2^s, 3, 2 and so on, this gives exactly the exponents of T2 (7): beta(s)+2, beta(s)+2 and beta(s)+1. It also gives those of sharper (4) and (5): 2(2^s-1), and 3^s-1 for the repeated factor tau(c L^2)^s.

LEMMA 2 (box, AP form of sharper (2); PROVED).
- Let L1 and L2 be nonconstant forms in the variables (i_1..i_m), m bounded, ranging over intervals of length <= h. The coefficients are bounded and the constant terms are O(h).
- The constant terms may depend arbitrarily on further fixed parameters, such as the diagonals T_j and the label e.
- Let R be a subset of {1..m}, and restrict each i_j, j in R, to one residue class mod q_j, with q_j <= h^(1-eta).
Then, for s in a compact range,
 sum over the restricted box of tau_+(L1 L2)^s <= C h^m Lambda^(beta(s)) ell^C * prod_{j in R} (C tau(q_j)^(C') / q_j),
with beta(s) = 3^s - 1 near s = 2, uniformly in all constant terms. The same holds for the one-form s-moments, sum tau_+(L)^s <= C h^m Lambda^(2^s-1) * prod_{j in R}(...), and for the "one factor fixed at c(e)" roles. Lemma 2 is (AP) for the box second moment.

LEMMA 3 (class counts and six-cell counts in AP; PROVED).
(a) On every diagonal T and in every class C_w,
 #{f = f_(T,i) in C_w : i = i0 (mod q)} <= C tau(q)^C ell^C (h/q) M(w),
with T1's M(w) = min(1, C Lambda/w, C Lambda^3/w^2), and n_G <= C tau(q)^C (h/q) Lambda^3/W^2 for a coarse group.
(b) Six-cell events (T2 (15) as re-indexed in (E3)) with restricted i-variables number at most (Delta h)^(k-1) prod_{j in R}(2/q_j) h^(-1/2+o(1)), for q_j <= h^(1/2). This is still a power saving.

LEMMA 4 (per-diagonal pair budget in AP; PROVED modulo the audited Theorem A, Lemma 1 and (E2) role analysis of t1_cost_decomposition.md).
- For e in C_w, a diagonal T that is not one of e's O(1) coincidence diagonals, and q <= h^(1/2):
 sum over f in C_w ∩ T with q | u_f of G^main_(e,f) <= C tau(q)^C ell^C q^(-1) h (Lambda^2 + w Lambda) M(w).
- G^main is G minus its O(1)-per-pair roles: the one-sea roles of Lemma 1 and the lone-point triangles. Those satisfy G^rem_(e,f) = O(1).
- On the coincidence diagonals the AP sum is <= C tau(q)^C ell^C (h/q) Lambda^3.
- Here u_f = (2i+1-r0)/2, or more generally any affine function lambda i + mu of i with bounded lambda != 0. Then {i : q | u_f} is a union of at most |lambda| residue classes mod q.

COROLLARY ((AP) as stated in polylog_relocation_diluted.md; PROVED). Lemmas 1 to 4 are exactly hypothesis (AP): the one-variable s-moments of T2 (7) and the box second moment of sharper (2), with label variables restricted to i = i0 (mod q), q <= h^(1/2), at an extra factor C tau(q)^C ell^C / q per restricted variable. In fact q <= h^(1-eta) is allowed for any fixed eta > 0.

THEOREM D-WEIGHTED (PROVED modulo the same inputs as the unweighted Theorem D: the audited Theorem E and the T1/T2 bounds). Suppose P(f in Y) <= rho_f := min(1, rho * sum_{q in Q_T} c_q 1[q | u_f]), with every q <= h^(1/2), independence across diagonals, and kappa := sup_T sum_{q in Q_T} c_q tau(q)^C / q < infinity. Then the conclusion of Theorem D holds with rho replaced by C rho kappa ell^C: with probability >= 1/2 there is an E with |E| <= h^(2-eps) and
 R(Y \ E) <= C(rho kappa |D| h Lambda^2 ell^(C1) + h^2 ell).
CONSEQUENCE. Theorem IV of polylog_relocation_diluted.md no longer needs (AP). It remains conditional on (O2), the rest of (O3), (U1) to (U3), J1 to J5, the prime p, and the audit of Theorem D's own steps. The (FF) clause for R_FF is still open.

## Proofs

0. WHAT T1/T2 CITE, AND WHAT I USE.
T2 (safe_triangle_pair_first_moment.md (7)), sharper_polylogarithmic_threshold.md (2) to (5) and T1 (two_moment_threshold_refinement.md, Section 1) all cite Henriot, Corollary 2, with the 2014 erratum, "only the upper bound". I read arXiv 1102.1643v1 (Theorem 5, Corollaries 1 and 2, (2.8), (2.9)) and the erratum (Math. Proc. Camb. Phil. Soc. 157 (2014) 375-377) in full.

The erratum makes three changes:
- It replaces the congruence function rho_R of (2.8) by a smaller function rho'_R, defined through a property (P_(a,n)). (P_(a,n)) includes a_i | R_i(n) for every i, and rho'_R <= rho_R.
- It repairs Lemmas 2 and 3.
- It replaces D by a*D in Theorem 6 and Corollaries 1 and 2, where a* is the leading coefficient of Q.
It then restates the upper bound as "New Theorem 5":
- Hypotheses: Q_1..Q_k are primitive, Q = prod Q_j has degree g and irreducible factors R_1..R_r, alpha and delta are in (0,1], A, B >= 1, 0 < eps < alpha/(50 g (g + 1/delta)), and F is in M_k(A,B,eps).
- Conclusion: uniformly in x >= C0 ||Q||^delta and x^alpha < y <= x,
 sum_(x<n<=x+y) F(|Q_1(n)|,...,|Q_k(n)|) << y prod_(g<p<=x) (1 - rho(p)/p) sum_(n1...nr <= x) F~(n) rho'_R(n) / [n1 kappa(n1), ..., nr kappa(nr)].
- C0 and the implied constant depend only on g, alpha, delta, A and B.
- ||Q|| is the sum of the absolute values of the coefficients, and kappa(n) is the squarefree kernel.

I use only New Theorem 5, and I bound its main-term sum myself. So the D versus a*D issue of Corollary 2 never enters, and nothing depends on the discriminant factor Delta_D. This is more robust than the T1/T2 citation. The only fact about rho'_R that I need follows from the erratum's definition, as in the first chain of (2.9):
 rho'_R(n) / [n1 kappa(n1), ...] <= omega(n) := density of integers m with n_j | R_j(m) for all j.
The reason is that (P) implies n_j | R_j(m), and this condition is periodic mod lcm(n_j), which divides the modulus.

1. PROOF OF LEMMA 1.
(a) Substitution and contents. Let t1 be the least element of I in the class t0 mod q, and write t = t1 + q m with 0 <= m <= K, where K <= A0 h / q. Then
 A_j(t) = a_j q m + (a_j t1 + b_j), with |a_j t1 + b_j| <= 2 A0 h.
Let g_j = gcd(a_j q, a_j t1 + b_j). Then g_j | a_j q, so tau(g_j) <= tau(a_j) tau(q) <= C tau(q). Put A'_j = A_j / g_j = alpha_j m + beta_j. It is primitive, with |alpha_j| <= A0 q and |beta_j| <= 2 A0 h.
- Submultiplicativity: tau(xy) <= tau(x) tau(y) and tau(x^2 y^2) <= tau(x^2) tau(y^2) <= tau(x)^2 tau(y^2). So f_j(g_j N) <= tau(g_j)^(2 s_j) f_j(N), which gives S <= C tau(q)^(C') S', where S' is the same sum for the A'_j.
- Resultants: alpha_i beta_j - alpha_j beta_i = q (a_i b_j - a_j b_i) / (g_i g_j) != 0. So the A'_j are pairwise coprime irreducible primitive linear polynomials.
- Put Dfrak := prod_j alpha_j * prod_(i<j) Res(A'_i, A'_j). Then 0 < |Dfrak| <= h^(O(1)).
This content step is the only source of tau(q)^C, and it is genuine: for t0 = 0 and A(t) = t, tau(qm) is about tau(q) tau(m).

(b) Zeros and the size condition. The k real roots split [0,K] into at most k+1 runs of consecutive integers on which no A'_j vanishes. The roots themselves are excluded from S. Take a run of length L.
- If L <= (K+2)^(1/4), bound it trivially by L h^(o(1)) <= (h/q) h^(-3 eta/4 + o(1)).
- Otherwise shift m = n - N0 so that the run becomes (x, x+y], with x = K+1 >= y = L > x^(1/4).
The shifted polynomial Q~ = prod_j A'_j(n - N0) has every coefficient O(h). So ||Q~|| <= (C h)^k, and with delta = eta/(4(k+1)) we get C0 ||Q~||^delta <= C0 h^(eta/4) <= x for large h, since x >= h^eta - 1.
F = prod_j f_j(n_j) lies in M_k(A, B, eps):
- for coprime tuples F(ab) = F(a) F(b);
- prod_j f_j(a_j) <= 3^(3 Omega(a_1...a_k));
- prod_j f_j(a_j) <= tau(a_1...a_k)^(6k) <= B_eps (a_1...a_k)^eps.
So New Theorem 5 applies with g = k, alpha = 1/4, delta = eta/(4(k+1)), and constants independent of q, t0 and the b_j. Here r = k and F~ = F. The local quantities rho(p) and omega are invariant under translation.

(c) The main term. Write omega_p(nu) for the p-adic density of {m : p^(nu_j) | A'_j(m) for all j}. By the Chinese remainder theorem omega(n) = prod_p omega_p(nu_p(n)), and F is multiplicative over primes. Dropping the condition n1...nk <= x and keeping only that all prime factors are <= x gives
 sum F omega <= prod_(p<=x) E_p, where E_p := sum over nu in N^k of prod_j f_j(p^(nu_j)) omega_p(nu).
Local facts, which are elementary:
- If nu_j >= 1 and p | alpha_j, then omega_p = 0, because p does not divide beta_j by primitivity.
- Otherwise omega_p(nu) <= p^(-max nu): an intersection of balls of radii p^(-nu_j).
- If p does not divide Dfrak and two of the nu_j are >= 1, then omega_p = 0, because the roots r_i and r_j differ by a p-adic unit.
- f_j(p^nu) <= (2nu+1)^3.
Hence:
- E_p <= 1 + C0'/p for every p, with C0' = sum_(m>=1) 2^(1-m) (m+1)^k (2m+1)^(3k).
- For p not dividing Dfrak, rho(p) = k, E_p = 1 + (sum_j c_j)/p + O(p^(-2)), and (1 - k/p) E_p <= 1 + (c - k)/p + O(p^(-2)), with c = sum_j c_j >= k.
- Factors with p <= g are bounded. Factors with p | Dfrak and p > g are at most E_p, because 0 <= 1 - rho(p)/p <= 1.
Therefore
 prod_(g<p<=x) (1 - rho(p)/p) prod_(p<=x) E_p <= C exp((c-k) sum_(p<=x) 1/p) * prod_(p|Dfrak) (1+1/p)^(C0') <= C Lambda^(c-k) (Dfrak/phi(Dfrak))^(C0') <= C Lambda^(c-k) ell^(C0'),
since Dfrak <= h^(O(1)).
At the primes p | q, which divide every alpha_j, we have E_p = 1 and rho(p) = 0. These Euler factors are smaller than the generic ones, so they cost nothing. Summing over the runs, sum L <= K + 1 <= 2 A0 h/q, which gives Lemma 1.

2. PROOF OF LEMMA 2. Follow the proof of sharper (2), Section 1.
- Case 1: a common variable i_c occurs in both forms. Fix all other variables and sum over i_c by Lemma 1 (k = 2 distinct primitive factors, or k = 1 with f = tau(.^2)^s in the repeated case tau(c L^2)^s <= tau(c)^s tau(L'^2)^s; here c divides a bounded number times g^2, so tau(c) <= C tau(q)^2). If c is in R, we gain C tau(q_c)^C ell^C / q_c. If not, we use the unrestricted Lemma 1 with q = 1. The fixed restricted variables j != c range over at most h/q_j + 1 <= 2h/q_j values each. The inner bound is uniform in the constant terms, so multiplying gives the claim.
- Case 2: disjoint supports. Then tau_+(L1 L2)^s <= tau_+(L1)^s tau_+(L2)^s, and the sum factorises over the two disjoint variable sets. Each single-form moment is handled as in Case 1 with k = 1.
- Zeros: a vanishing form contributes tau_+ = 1 at <= 2 points per inner sum, which is absorbed.
In (E3) of t1_cost_decomposition.md the restricted variables are the i-variables of the other labels, and the T-variables are outer parameters. (E3) asserts, and its audit accepted, that for each fixed T-tuple both forms stay nonconstant in the i-variables. So Lemma 2 applies per T-tuple, uniformly. The "one factor fixed at c(e)" roles use tau(c(e) L)^2 <= tau(c(e))^2 tau(L)^2 and the single-form moment at s = 2.

3. PROOF OF LEMMA 3.
(a) v(f)^s <= 7^s (1 + sum of the 6 terms tau(|r-t|)^s), and r - t != 0, because r is a bulk row and t a sea row. Each term is a one-form AP moment, so Lemma 1 with k = 1 gives sum over the restricted i of v^s <= C tau(q)^C ell^C (h/q) Lambda^(2^s - 1). By the positivity of the summands we may extend the i-range of any diagonal, even a short one, to [1,h]. The profile progression mod 7, and in L** the progression mod 16, combine with i0 mod q into one class mod q' = lcm(q, m0), where m0 is bounded, or into the empty set. Then tau(q')^C/q' <= tau(m0)^C tau(q)^C / q. Markov's inequality at s = 1, 2, plus the count h/q + 1 <= 2h/q at s = 0, gives the minimum M(w). The coarse groups are the same at s = 2.
(b) (E3) says (15) is a nontrivial linear equation in the i-variables. Choose an i_j with nonzero coefficient and fix all the other variables. Then i_j has at most 1 value instead of h/q_j + 1 (if j is restricted) or h (if not). The loss is a factor <= 2 q_j/h <= 2 h^(-1/2) or h^(-1). G_J^2 <= h^(o(1)). So the six-cell count is (Delta h)^(k-1) prod(2/q_j) h^(-1/2+o(1)), which is still absorbed in the Lambda^8 term.

4. PROOF OF LEMMA 4. In the (T,i) parametrisation f = f_(T,i) has rows 2i+1 and 2i+T+1, so every surviving role of Theorem A is a product of divisor functions of forms affine in i with coefficient 2 and constant terms O(h). The surviving roles are (i) tau((c-a)^2), (ii) tau(c-a) tau(c+a-s-t) and tau((c-a)^2), and (iii) w * tau(nonprivate form). In (iii) the private factor is bounded by v(e) <= w or by v(f) <= w. The class indicator is 1_(C_w)(f) <= C w^(-s) sum_k tau(C_k(i))^s for s in {1,2}, or <= 1 for s = 0, with class forms 2i+1-t and 2i+T+1-t (T2 (9)).
- Off the coincidence diagonals, the class forms are distinct from the geometric forms, so each term is a Lemma 1 sum:
 - for s = 0: tau(A^2), or tau(A) tau(B), or tau(A);
 - for s = 1, 2: tau(C)^s tau(A^2) and its analogues.
 Lemma 1 gives (h/q) tau(q)^C ell^C Lambda^(2 + beta(s)) w^(-s), and the analogous bounds. The minimum over s in {0,1,2} reproduces h (Lambda^2 + w Lambda) M(w), times C tau(q)^C ell^C / q, exactly as in (E2).
- On the O(1) coincidence diagonals per e, drop the class restriction: sum (sum_k tau(C_k)) tau(A^2). Where C_k = A, this is the single form tau^3, and Lemma 1 still applies. It gives (h/q) tau(q)^C ell^C Lambda^3.
- The set {i : q | lambda i + mu} is a union of at most |lambda| classes mod q.

5. PROOF OF THEOREM D-WEIGHTED. I follow D1 to D4 of polylog_relocation_diluted.md and change only the expectations. All other steps are unchanged: the Chernoff ranges [0, h G_max], the variance bound of D3, the Chebyshev threshold t = (n_w h^(-eps))^(k-1), the bound E|E| <= h^(2-eps) (it uses only rho_f <= 1), and the monotonicity under removal. Write R_w := sum_(f in S_w) rho_f.
- (D1) By Lemma 3(a), R_w <= rho sum_T sum_q c_q C tau(q)^C ell^C (h/q) M(w) <= C rho kappa ell^C |D| h M(w). Chernoff then gives n_w(Y) <= 2 R_w + 9 h log h.
- (D2) Split G = G^main + G^rem. Then E Phi'_e <= rho sum_T sum_(q in Q_T) c_q sum_(f in T, q|u_f) G^main + C R_w + C h Lambda^3 + h^(1+o(1)).
 - By Lemma 4 the first term is <= C rho kappa ell^C * ell^C |D| h (Lambda^2 + w Lambda) M(w).
 - The term C R_w comes from the O(1)-per-pair roles, which must be weighted by rho_f, not counted deterministically. The note's sketch did not say this, and it is the one point that needs the class-count part of (AP).
 - The coincidence diagonals (O(1) per e, unrestricted bound h Lambda^3) and the slice terms (h^(1+o(1))) are bounded deterministically. They are absorbed because they carry no |D| factor: summed over the O(ell) classes they give h^(1+o(1)), far below h^2.
 So E Phi'_e <= C rho kappa ell^C B_S(w) + h^(1+o(1)) + C h Lambda^3. Chernoff and the union bound follow as before.
- (D3) The J that contain a label on T_e, or two labels on one diagonal, are split off deterministically as before. For the remaining J the labels of J \ {e} lie on distinct diagonals, so P(J \ {e} ⊆ Y) <= prod rho_f by independence. Weighted Cauchy-Schwarz gives
 E Z'_e <= (sum_J prod rho_f)^(1/2) (sum_J prod rho_f G_J^2)^(1/2) <= R_w^((k-1)/2) * (sum_J prod rho_f G_J^2)^(1/2).
 Expand each rho_f <= rho sum_(q in Q_(T_f)) c_q 1[q | u_f]. For a fixed T-tuple and fixed (q_1..q_(k-1)), Lemma 2 with Lemma 3(b) bounds the restricted i-sum of G_J^2 by prod_j (C tau(q_j)^C ell^C / q_j) * C h^(k-1) (Lambda^8 ell^C + v(e)^2 Lambda^3). Summing over the q_j, and then over the T-tuples in D^(k-1), gives
 sum_J prod rho_f G_J^2 <= (C rho kappa ell^C)^(k-1) (|D| h)^(k-1) (Lambda^8 ell^C + v(e)^2 Lambda^3).
 Hence E Z'_e <= (C rho kappa ell^C)^(k-1) (|D| h M(w) * |D| h)^((k-1)/2) A(w). This is the unweighted bound with rho replaced by C rho kappa ell^C and n_w replaced by its bound C |D| h M(w).
- (D4) Use N_w with these replacements. The sums over classes need sum_w M(w) << ell, sum_w w M(w) << Lambda ell, sum_w sqrt(M(w)) << ell (at most an extra sqrt(ell) against T1 (9)) and sum_w sqrt(w M(w)) << sqrt(Lambda) ell. The coarse groups (E5) are the same with n_G from Lemma 3(a). Total: C rho kappa |D| h Lambda^2 ell^(C1) + O(h^(2-eps')) + h^2 ell.
- For Theorem IV, c_q = 1 on Q_T = {q_lambda, p_lambda : max <= h^(1/2)}. By Lemma IV, kappa_IV = sum_lambda (tau(q_lambda)^C/q_lambda + tau(p_lambda)^C/p_lambda) < infinity for every fixed C. The exponent C needed here is <= 2 * (sum of the s_j), about 10. So the weighted hypothesis holds, and Theorem IV's arithmetic input is now proved.

## External results used

- K. Henriot, Nair-Tenenbaum bounds uniform with respect to the discriminant, Math. Proc. Camb. Phil. Soc. 152 (2012) 405-424 (arXiv 1102.1643v1): Theorem 5 and inequality (2.9) (first chain).
- K. Henriot, Nair-Tenenbaum uniform with respect to the discriminant - ERRATUM, Math. Proc. Camb. Phil. Soc. 157 (2014) 375-377: New Theorem 5 (the upper bound with rho'_R, Q_j primitive, x >= C0||Q||^delta, x^alpha < y <= x, constants depending only on g, alpha, delta, A, B), and the replacement of D by a*D in Corollaries 1 and 2. I do not use the corollaries.
- Mertens' theorem, sum_{p<=x} 1/p = loglog x + O(1); n/phi(n) << loglog n; tau(n) << n^eps; Chinese remainder theorem; Gauss's lemma (a product of primitive polynomials is primitive).
- The Chernoff, Chebyshev and Markov inequalities and the product-form local lemma, exactly as already used in Theorem D.

## Checks

I did the analysis first and checked it once numerically. The script folder script is scripts_ap_hypothesis/ap_check.py. It ran with py in 3.8 s at h = 3*10^5.
- What it computes: the ratio (q/h) * sum over t = t0 (mod q) of F, divided by (1/h) * sum over all t of F, taken over all residues (or 40 random residues plus the residues where some form is divisible by q), for q in {3,...,511}.
- Functions tested: F = tau(2t+c1)^2 tau((2t+c2)^2), tau(2t+c1)^2 tau(2t+c2) tau(4t+c3), and tau(2t+c1)^2 tau(2t+c2)^2.
- Results: the worst ratios were 1.8 to 10.1, for example 10.08 at q = 105 (tau = 8) and 8.66 at q = 420 (tau = 24). The worst residue was always one where q divides a form, which is the content case.
- Reading: this fits a bound C tau(q)^C with small C, and it supports the claim that the restricted Euler factors give no loss beyond the contents. It is a finite check only.
- Sources read: polylog_relocation_diluted.md; t1_cost_decomposition.md (Lemma 1, Theorem A, Theorem E (E1) to (E5)); the ledger rows T1 and T2; two_moment_threshold_refinement.md; safe_triangle_pair_first_moment.md (Sections 3, 4 and 6); sharper_polylogarithmic_threshold.md. Of Henriot's paper (arXiv 1102.1643v1) I read Theorem 5, Corollaries 1 and 2, (2.8), (2.9) and Section 6. I also read the full 3-page erratum, fetched as a PDF and converted to text in a separate folder.
- The repository was only read. No git commands were run.

## Gaps

- Lemma 2 applies per T-tuple only because (E3) of t1_cost_decomposition.md says both forms stay nonconstant in the i-variables for each fixed T-tuple, with T ranging over an arbitrary set D, not an interval. The audit accepted this, but I did not re-derive it. If some form were constant in the i's and varied only in T, neither the unrestricted (E3) nor my AP version would cover it.
- Lemma 4 inherits the role list of Theorem A, Lemma 1 and (E2) (audited), including the claim that form coincidences occur on O(1) diagonals per e. I did not re-derive that list.
- Theorem D-weighted is proved modulo the unweighted Theorem D's own steps (Chernoff, the D3 variance count k^2 h n_w^(2k-3), Chebyshev, local lemma). Those steps are not audited; polylog_relocation_diluted.md lists them as needing an audit. Lemmas 1 to 4 have not been checked by a second reader either.
- Theorem IV stays conditional on (O2), the rest of (O3), (U1) to (U3), the unaudited J1 to J5, the existence of p, and (for R_FF) on (FF). None of these is touched here.
- Citation: I use Henriot's New Theorem 5 as restated in the 2014 erratum, and only the upper bound. I take rho'_R/[...] <= omega from the erratum's definition (P implies a_i | R_i(n)). Some OCR symbols in the erratum were garbled, notably the relation symbol in the first clause of (P) and the exact form 'x^alpha < y <= x'. I read both from context and from the 2012 statement. Neither reading changes anything here, because both 'divides' and 'exactly divides' imply divisibility.
- The constant exponents C, C', C0 are not optimised. The claim covers q <= h^(1-eta) at fixed eta, and the constants degrade as eta tends to 0.

## Missing estimate

None for (AP) itself. For Theorem IV the remaining inputs are unchanged: (FF) for R_FF (summability of tau(height)^C/height over the admissible ratios of the nodal cubic), the audit of Theorem D's D1 to D4, and the L** hypotheses (O2), (O3) and (U1) to (U3).

## Next steps

- Have a second reader audit Lemma 1, especially step (c): the local densities omega_p, the bound E_p <= 1 + C0'/p, and the fact that primes p | q give E_p = 1. Then have them audit Lemma 2 and the weighted D2/D3. If these pass, add a ledger row: '(AP): Henriot moments in progressions mod q <= h^(1-eta) at factor C tau(q)^C ell^C/q'.
- Correct the sketch in polylog_relocation_diluted.md, weighted form. The O(1)-per-pair roles (one-sea roles and lone-point triangles) must be weighted by rho_f, which needs the AP class count (Lemma 3(a)). Coincidence diagonals and slices can stay deterministic.
- Optional gain: since Lemma 1 allows q <= h^(1-eta), Theorem IV can send to Proposition partial only the labels on edges with max(p_lambda, q_lambda) > h^(1-eta). By the counting of Lemma IV that is O(h^(5/3+eta/3+o(1))) labels instead of O(h^(11/6)). This does not change the exponent.
- Move on to (FF) for R_FF. The same Lemma 1 already covers its progressions, so only the tau-weighted height summability over the nodal cubic remains.

