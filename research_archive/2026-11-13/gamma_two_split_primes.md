# Gamma for two split primes

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Undecided. Four partial results: characters on the slab reduce to the rational coordinate b; algebraic characters cannot separate the slab; Bohr colourability reduces to finite truncations; chi_inf(T) for two split primes is bounded independently of the larger exponent. Not audited yet.

# Result

## Status

partial

## Summary

Not decided: I could not show that chi(Gamma_S^Sigma) is finite or infinite for S = {11, 19} or for any pair. Proved four smaller results: every character on the slab reduces to a function of the rational coordinate b; algebraic characters cannot separate the slab; Bohr colourability reduces to finite truncations by compactness; and chi_inf(T) for two split primes depends only on the smaller exponent.

## Statements

Notation is as in gamma_one_split_prime.md. S = {l1, l2} is a pair of split primes, and G_S = Z[1/(5 l1 l2)]. The slab D^Sigma is the set of r = r(beta) = L(beta - 1) with beta = ±eps^n omega1^k1 omega2^k2 and s = sigma1(beta) in Sigma. Write gamma = phi·beta = a + b·phi with a, b in Z[1/(l1 l2)], and sig_i = sign(k_i). Every character of G_S can be written chi(x) = theta·x + sum_l {zeta_l x}_l + {g x}_5 with theta real, zeta_l in Z_l and g in Z_5. To get this form, subtract the element sum_p {zeta_p}_p of Z[1/N] from every component.

(R) b-REDUCTION [proved]. For every slab element (in fact for every beta) and every l in S with k_l ≠ 0, and every zeta in Z_l:
 {zeta r}_l = {-sig_l · zeta · s5_l · b / 10}_l, and v_l(b) = -|k_l|.
If k_l = 0, the term is 0. So on the slab every character is theta·r + sum_l {xi_l b}_l + (a 5-part that depends only on g mod 5), with xi_l = -sig_l zeta_l s5_l/10. Each xi_l ranges over all of Z_l as zeta_l does. Also r = (b - 1)/2 + O((b - 1)^2) near s = 1, and b ~ 1 near s = 1 (b ~ -1 near s = -phi^-2). For characters that live on one prime, the sign sig is irrelevant. The Bohr question for the slab is therefore a question about the set B of rationals b in Z[1/(l1 l2)], at most 8 for each pair (|k1|, |k2|).

(Q) ALGEBRAIC CHARACTERS ARE RECURRENT ON THE SLAB [proved, given Theorem 2 of gamma_linearization.md]. Let F be a finite family of characters of G_S. Suppose there is an l0 in S such that every chi in F has l0-parameter zeta_{l0} = alpha + beta·s5_{l0} with alpha, beta in Q ∩ Z_(l0), the other parameters being arbitrary. Then for every delta > 0 there are infinitely many r in the slab with ||chi(r)|| < delta for all chi in F. For these r, sigma1(beta_el) → 1 and k is supported on l0.
COROLLARY Q1. Every Bohr colouring of Gamma_S^Sigma, of Gamma_S, or of Gamma uses, at every split prime l in S, a character whose l-adic parameter lies outside Q + Q·s5_l. This strengthens Corollary 2.1 of gamma_linearization.md (outside Q) to outside the embedded copy of Q(sqrt5). In particular, the characters rho and lambda_i and their rational combinations are never enough.

(P) RESIDUAL AFTER ALL ALGEBRAIC CHARACTERS [proved, given Theorems A and F and Lemma B]. For 0 < delta < 0.017:
 chi(Gamma_S) <= ceil(1/delta)^3 · chi(Cay(G_S, R(delta))),
where R(delta) = {r in D^Sigma : ||{b}_{l1}|| < delta, ||{b}_{l2}|| < delta, F(s) < 3 delta}, with F(s) = max(||f_A(s)||, ||f_C(s)||) (Lemma B). Since {b}_{l1} + {b}_{l2} ≡ b ~ ±1 (mod 1), the two b-conditions agree up to O(delta).

(K) COMPACTNESS DICHOTOMY [proved]. For m >= 1 and c > 0, put U(m,c) = {(chi_1, ..., chi_m) in (dual of G_S)^m : max_i ||chi_i(r)|| >= c for all r in D^Sigma}.
 (i) If U(m,c) is nonempty, then chi(Gamma_S) <= 60^3 · ceil(1/c)^m.
 (ii) U(m,c) is empty iff some finite subset F of D^Sigma already blocks every m-tuple.
 (iii) Gamma_S has a Bohr colouring iff D^Sigma is not a set of Bohr recurrence, iff D_S = r(Lambda_S) is not a set of Bohr recurrence.
For each (m, c), nonexistence therefore has a finite certificate.

(E) THE LARGEST EXPONENT IS FREE [proved, given Theorem F and Theorem 1(c)]. Let T = (inert part)·5^a·l1^e1·l2^e2 and m = min(e1, e2). Put t_i = ceil(log_{l_i}(4(2m+1) + 1)). Then:
 chi_inf(T) <= 60^3 · (2 l1 + 1)^t1 · (2 l2 + 1)^t2.
This bound does not depend on max(e1, e2). For example, chi_inf(11^e · 19 · (inert) · 5^a) <= 216000 · 23^2 · 39 for every e, whereas chi_orbit_bound.md Theorem 2 grows like e log e. As m grows, the bound is m^(2.55 + o(1)) for {11, 19}.

NOT PROVED: chi(Gamma_S^Sigma) < infinity or = infinity for any pair; Bohr recurrence of the slab; a bound uniform in w for the off-strip factor (route (d)).

## Proofs

[R] The two places at l are P (where gamma is non-integral, with v_P(gamma) = -|k|) and P'. Theorem A's computation: iota(phi) = (1 + s5)/2. If sig = +, then iota(gamma) = a + b·iota(phi) lies in Z_l. So 2a = 2 iota(gamma) - b(1 + s5), and 2a + b - 1 = 2 iota(gamma) - 1 - s5·b. Hence zeta·r = zeta(2 iota(gamma) - 1)/10 - zeta·s5·b/10 ≡ -zeta·s5·b/10 (mod Z_l). If sig = -, use iota(gamma') = a + b(1 - s5)/2 in Z_l, which gives +zeta·s5·b/10. Valuation: b = (gamma - gamma')/sqrt5, and gamma' is integral at P, so v_l(b) = v_P(gamma) = -|k|. Near s = 1: on the conic a^2 + ab - b^2 = -1 at (0, 1) we have da = 2 db, so r = (2a + b - 1)/10 = (b - 1)/2 + O((b - 1)^2). Also b = (phi s + phi^-1/s)/sqrt5 equals 1 at s = 1 and -1 at s = -phi^-2.

[Q] Let D be the lcm of the denominators of all alpha and beta, and N = 20D. N is prime to l0, because the alpha and beta are l0-integral. As in Theorem 2 of gamma_linearization.md, (O[1/l0]/N)^* is finite. So there are infinitely many beta_el in <eps^(2u), omega_l0^(2v)> with beta_el ≡ 1 mod N, sigma1(beta_el) > 0 and sigma1(beta_el) → 1, because the two logarithms are independent. Then a ≡ 0 and b ≡ 1 mod N·Z[1/l0], and r = (2a + b - 1)/10 lies in 2D·Z[1/l0].
- Primes l ≠ l0 and the prime 5: r is integral there, so those terms vanish.
- At l0, alpha part: alpha·r lies in Z[1/l0], and {q}_l ≡ q (mod 1) for q in Z[1/l], so {alpha r}_l0 ≡ alpha·r.
- At l0, beta part: by [R] with zeta = beta·s5 and s5^2 = 5, {beta s5 r}_l0 = {-sig·beta·b/2}_l0 = {-sig·beta(b - 1)/2}_l0. The term beta/2 has zero fractional part because 2 is an l0-unit. Then beta(b - 1)/2 lies in 10D·beta·Z[1/l0], inside Z[1/l0], so this term is ≡ -sig·beta(b - 1)/2.
So chi(r) ≡ (theta + alpha)r - sig·beta(b - 1)/2 (mod 1). This tends to 0 because r → 0 and b → 1. Finally r ≠ 0, and s lies in the near-1 window of Sigma.
Corollary Q1. If the l0-parameters of all characters lie in Q + Q·s5, then (Q) gives an edge inside one colour cell. For Gamma_S, use Theorem F, or note that D^Sigma ⊂ D_S.

[P] Colour x by the cell of side delta of (rho(x), lambda_1(x), lambda_2(x)) in T^3. Two vertices in one cell differ by d with |rho(d)| < delta and |lambda_i(d)| < delta (mod 1), so ||chi_z(d)|| < 3 delta for every z.
- Off the slab: Theorem F gives max(||chi_sig||, ||chi_-sig||) = F(s) >= 0.0514 > 3 delta.
- On the slab: lambda_i(r) = {-sig_i b}_{l_i} (Theorem F), so ||lambda_i(r)|| = ||{b}_{l_i}||. So an edge inside one cell must lie in R(delta). Multiply by any proper colouring of Cay(G_S, R(delta)).
- Also {b}_{l1} + {b}_{l2} ≡ b (mod 1), by partial fractions.

[K] The dual group of G_S is compact. For each r, the set {max_i ||chi_i(r)|| >= c} is closed, so U(m,c) is closed. U(m,c) is empty iff the open sets {max_i ||chi_i(r)|| < c}, for r in D^Sigma, cover the compact product, iff finitely many of them do.
- For (i): use cells of side c. Two points in one cell differ by d with ||chi_i(d)|| < c for every i, so d is not in D^Sigma. The factor 60^3 is Theorem F.
- For (iii): add rho, lambda_1 and lambda_2 to any family. A common recurrence r then has F(s) small, so s is near {1, -phi^-2} and r lies in the slab. The converse direction is immediate.

[E] At prime l1, level j <= e1, assign the slab elements with |k1| = j and |k2| <= min(j, e2). At l2, level j <= e2, assign those with |k2| = j and |k1| < j, |k1| <= e1. In both cases the other exponent is at most m, so a level has at most 2(2m+1) vectors k, and at most 2 elements per k (Lemma C or Theorem F). That is at most 4(2m+1) elements. Every nonzero slab element is assigned exactly once (k = 0 gives r = 0).
At prime l, take t characters zeta^(1), ..., zeta^(t) in Z_l and choose their base-l digits level by level, as in Lemma D. For an assigned r at level j, v_l(r) = -j (Theorem 1(c)). With the lower digits fixed, the values {zeta^(i) r}_l, as the digit d^(i)_{j-1} runs over Z/l, form one coset c_i + (1/l)Z/Z, because the leading unit digit u0 of r is nonzero. Use cells of width 1/(2l+1). An open arc of length 2/(2l+1) < 1/l holds at most one point of the coset. So r is unseparated for at most one digit vector in [l]^t. Since 4(2m+1) < l^t, some vector avoids all assigned elements. Colour by the product of the cells of the t1 + t2 characters. If d is an edge inside one cell, d is assigned to some l_i, and one of that prime's characters has ||·|| >= 1/(2 l_i + 1), which is a contradiction. Restrict to (1/T*)Z (L2 and T2 of limit_graph_gamma.md) and multiply by Theorem F's off-strip factor 60^3. Only D_T^inf ⊂ box(e1, e2) is used (Theorem 1(c)).

[WHY THE QUESTION STAYS OPEN: analysis, not proofs]
1. By (R) and (P), the transcendental characters must handle R(delta). In the independence model, R(delta) keeps a fraction of about (delta/0.2)·2·delta of the slab, so about 7j·delta^2/0.1 elements per level. This is still linear growth, so no fixed delta makes it bounded per level, the condition that Lemma D needs.
2. The 2D digit game. With one character per prime, an element in cell (j1, j2) is unseparated iff d1_{j1} is in Bad1(e) and d2_{j2} is in Bad2(e). Each digit serves infinitely many cells, a whole row or column. In the random model with t characters per prime at width c, the expected number of valid digit choices is about (l1 l2)^{tN}·exp(-p_t N^2), with p_t ~ 3.5·(2c)^{2t}. This tends to 0, but only at N ~ t·log(l1 l2)/p_t, which is about 97 for t = 1, c = 1/16 and {11, 19}, where the peak count is about e^129. That is consistent with the greedy surviving to level 40, and it rules out any exhaustive finite certificate under (K) within these limits. This is the l-adic analogue of the gap between lacunary sequences (de Mathan, Pollington, Peres–Schlag: a separating theta exists; this is the w = 1 case) and sequences with about log X elements per dyadic scale (w = 2), where the local-lemma method gives no uniform constant.
3. Route (c) in dynamical form. By (K)(iii), Bohr recurrence of the slab is equivalent to this: every point Psi = (chi_i ∘ L) in X^m, with X the dual of O[1/(10S)], returns under the diagonal Lambda_S action (rank w+1) to the cylinder {y : y_i(1) ~ Psi_i(1)}. Theorem E's triple (chi_+, chi_-, zeta) is a non-recurrent point for the rank-2 group Lambda_l (w = 1). This parallels Lindenstrauss–Wang (Duke 161 (2012), arXiv 1101.0323), who construct a rank-2 counterexample and prove for faithful Cartan Z^r actions on T^d with r >= 3 that closed, invariant, topologically transitive subsets of (T^d)^2 are homogeneous. Their theorem does not apply here: the space is an S-adic solenoid, not a torus; the action is not Cartan (rank w + 1 = 3, against the S-unit rank 2w + 1 = 5); and the application needs m-fold products, not pairs. I conjecture that for |S| >= 2 the set D_S is a set of Bohr recurrence (so Gamma_S has no Bohr colouring). It would follow from an orbit-closure rigidity theorem of Lindenstrauss–Wang type for the rank-3 norm-one S-unit action on products of the S-adic solenoid of Q(sqrt5). Even then, chi(Gamma_S) = infinity would still need Katznelson's question or Proposition 4 of gamma_linearization.md.
4. Bohr colourings of fixed type do not settle the question, and Proposition 4 would need nu_n with liminf Re nu_n^(chi) >= 0 for all chi. Heuristically the row sums cancel at about the square root of the row length, which supports infinity, but no proof is in sight. Large cliques are ruled out: a k-clique is an S-unit equation with 2k + 1 terms, which has finitely many nondegenerate solutions (Evertse–Schlickewei–Schmidt). So infinity would need a non-clique mechanism.

## External results used

- Theorem 2, Theorem 1(a),(c) and Corollary 2.1 of gamma_linearization.md (repository, unaudited); Theorems A, F, Lemmas B, C, D of gamma_one_split_prime.md (repository, unaudited); L2 and T2 of limit_graph_gamma.md; Theorem 2 of chi_orbit_bound.md (for comparison only).
- E. Lindenstrauss and Z. Wang, Topological self-joinings of Cartan actions by toral automorphisms, Duke Math. J. 161 (2012) 1305-1350, arXiv 1101.0323: for a faithful Cartan Z^r action on T^d with r >= 3, closed, invariant, topologically transitive subsets of (T^d)^2 under the diagonal action are homogeneous, and the paper constructs a rank-2 counterexample. Read through the arXiv abstract and the publisher record only (https://arxiv.org/abs/1101.0323, https://pure.psu.edu/en/publications/topological-self-joinings-of-cartan-actions-by-toral-automorphism/). Used only as an analogy.
- Peres-Schlag (Bull. LMS 2010), de Mathan and Pollington (lacunary Diophantine approximation), and Evertse-Schlickewei-Schmidt (finiteness of nondegenerate S-unit solutions): cited from memory, in remarks only, not as proof inputs.

## Checks

I ran these scripts with py; each finished in seconds. They are in the matching scripts_ folder of this directory. adelic_copy.py is a copy of the repository helper; the repository was not modified.
(1) bred.py checks the b-reduction [R] and v_l(b) = -|k_l| on 600 random beta for S = {11, 19}, |n| <= 20 and |k_i| <= 6: 3285 exact rational identity checks with random zeta mod l^16, and 0 failures.
(2) algid.py checks the exact identity behind (Q), {(alpha + beta s5) r}_19 + {(5 + 4 s5_11) r}_11 ≡ alpha·r - sig·beta(b - 1)/2 (mod 1), for beta = eps^(15x) omega_19^(15y) (≡ 1 mod 10, |x|, |y| <= 4): 1152 cases, 0 failures. b - 1 lies in 10·Z[1/19] in every case.
(3) rdelta.py checks R(delta) for {11, 19} at levels <= 22. The slab counts per level are 6, 12, 22, ..., 152 (about 7j, matching gamma_one_split_prime.md). The share of two-prime residual elements is 0.381, 0.081 and 0.016 for delta = 0.2, 0.1 and 0.05; the independence model predicts 0.4, 0.1 and 0.025.
A first, overlong version of the recurrence script timed out at 60 s and was killed. I replaced it with the exact identity check (2).

## Gaps

- The main question is open. I did not decide chi(Gamma_S^Sigma) for S = {11, 19} or for any pair, and found neither a finite colouring nor a proof of Bohr recurrence or of infinite chromatic number.
- Route (d), an off-strip factor uniform in w, made no progress. The obstruction is that the sign pattern sig of the edge cannot be read off from the vertex data rho and lambda_i, and the l1-type cells give (10w/e)^w as well.
- Proposition Q uses Theorem 2 of gamma_linearization.md (unaudited, elementary). Proposition P and Theorem E use Theorems A and F and Lemma B of gamma_one_split_prime.md (unaudited; Lemma B's 0.0514 comes from a floating-point grid plus a Lipschitz bound, not interval arithmetic) and Theorem 1(c) (v_l(r) = -|k_l|, unaudited). None of my results has an independent audit; I re-derived each once.
- Theorem E only improves chi_orbit_bound's Theorem 2 for unbalanced exponents. For balanced exponents it is worse (m^2.55 against e1 e2 log). It is a small gain and does not change the payoff of Proposition 3 there.
- The density of R(delta) (about (delta/0.2)·2·delta of the slab) and the random-model thresholds (N about 97, peak e^129) are heuristic or numerical, not proved. I proved no lower bound showing that R(delta) has unboundedly many two-prime elements per level.
- Lindenstrauss–Wang was read only through its arXiv abstract and the publisher record. It is used only as an analogy, not as an input.
- Bohr recurrence of D_S, even if proved, would not by itself give chi(Gamma_S) = infinity (Katznelson's question).

## Missing estimate

To get chi(Gamma_{l1,l2}) < infinity, one needs a finite colouring of Cay(G_S, R(delta)) for some delta > 0. R(delta) is the set of rationals b in Z[1/(l1 l2)] coming from norm-one S-units, with b within O(delta) of ±1 and ||{b}_{l1}|| < delta. Any Bohr version needs, at each prime, l-adic parameters outside Q(sqrt5) (Corollary Q1). It would require finitely many xi in Z_l1 x Z_l2 such that some ||{xi1 b}_l1 + {xi2 b}_l2|| >= c on all of R(delta), which is a 2D digit system in which each digit serves a whole row of cells. For the converse (no Bohr colouring), one needs that every point of (X^m) of the form (chi_i ∘ L) is recurrent at the coordinate 1 under the diagonal action of the rank-3 group Lambda_S on products of the S-adic solenoid of Q(sqrt5). That is a Lindenstrauss–Wang-type rigidity statement for a non-Cartan solenoid action on m-fold products.

## Next steps

- Audit [R], (Q), (P), (K) and (E). They are short: [R] is three lines of Theorem A's algebra, (Q) is Theorem 2 plus [R], and (E) is Lemma D with t characters and the dominant-coordinate assignment.
- Record in the ledger: every Bohr colouring of Gamma_S needs non-quadratic l-adic parameters at every split prime (Corollary Q1); and chi_inf(T) for two split primes is bounded in terms of min(e1, e2) alone (Theorem E).
- Route (c): look for orbit-closure or recurrence results for non-Cartan higher-rank S-adic solenoid actions on products, after Wang's 'non-hyperbolic' paper and Lindenstrauss–Wang. Reduce first to m = 2: is every point of Y_0 x Y_0 recurrent at 1 under Lambda_{11,19}? A positive answer for all m would rule out every Bohr colouring for |S| >= 2.
- Prove a lower bound on two-prime elements in R(delta) per level, using Baker-type and l-adic (Yu) linear forms for the joint distribution of (log s, {b}_l1). That would make the 'linear growth survives every algebraic sieve' statement rigorous.
- Test Proposition 4 numerically on R(delta): minimise the uniform-weight character average over (xi1 mod 11^K, xi2 mod 19^K, theta) by annealing for K up to about 12. If averages bounded below 0 persist, that is evidence against proving infinity with uniform weights.
- Since the program's payoff (chi_orbit_bound Proposition 3) needs bounds polynomial in Omega_s, generalise Theorem E to w primes (the largest exponent is free), and check whether it improves the heavy/light threshold.

