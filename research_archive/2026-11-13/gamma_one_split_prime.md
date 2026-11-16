# A finite colouring of Gamma for one split prime

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: chi(Gamma_l) <= 6400 for every split prime l, uniformly in l and in the exponent, by a three-character Bohr colouring built from an adelic Pisot identity. So chi_inf(T) <= 6400 for every odd T with at most one split prime factor. chi_inf(5) = 5. For two or more split primes the question reduces to the real-short edges. Not audited yet.

# Result

## Status

partial

## Summary

chi(Gamma_l) is finite for every split prime l, with a bound of 6400 that does not depend on l or on the exponent. The proof is a three-character Bohr colouring built from an adelic Pisot identity. For two or more split primes the question reduces to the real-short edges, and that case stays open. No 5- or 6-colouring was found for an unlucky l.

## Statements

Notation is as in gamma_linearization.md. K = Q(sqrt5), eps = -phi^2, phi' = -1/phi. For a split prime l, l = N(pi), omega = pi/pi' = pi^2/l, and Gamma_l is Gamma restricted to G_l = Z_(2) ∩ Z[1/(5l)]. Every r in R_+ ∩ G_l is r(beta) = L(beta - 1) with beta = ±eps^n omega^k (Theorem 1(c) there). Put gamma = phi·beta and s = sigma1(beta). Fix the embedding iota of K into Q_l with iota(pi) ≡ 0 mod l, and put s5 = iota(sqrt5) in Z_l^*. {q}_l is the l-adic fractional part.

PROPOSITION 0 (proved by hand). Every d in D_5^inf satisfies ||d/sqrt5|| >= sqrt5 - 2 = 0.2360. So x -> floor(5{x/sqrt5}) is a proper 5-colouring of Cay(Z, D_5^inf), and chi_inf(5) <= 5. Together with the earlier uncertified SAT bound chi_inf(5) >= 5, this gives chi_inf(5) = 5, so Gamma restricted to Z_(2) ∩ Z[1/5] has chromatic number 5.

THEOREM A (adelic Pisot identity, proved). Define chi_±(x) = 2 sqrt5 x - {±2 s5 x}_l, two characters of Z[1/(10l)]. Put f_A(s) = (2phi'/s - 1)/sqrt5 and f_C(s) = (2 phi s - 1)/sqrt5. For every beta = ±eps^n omega^k with r = r(beta), modulo 1:
 if k >= 0: chi_-(r) ≡ f_A(s) and chi_+(r) ≡ f_C(s);
 if k <= 0: chi_+(r) ≡ f_A(s) and chi_-(r) ≡ f_C(s).
So on the whole connection set, both character values are functions of the real size s alone.

LEMMA B (off-strip separation; algebra proved by hand, constant certified by computer). Let Sigma = (0.8, 1.2) ∪ (-1.2 phi^-2, -0.8 phi^-2). Define F(s) = max(||f_A(s)||, ||f_C(s)||). F vanishes exactly at s = 1 and s = -phi^-2, and F(s) >= 0.0514 for every real s ≠ 0 outside Sigma.

LEMMA C (strip count, proved). For each k, at most one beta = ±eps^n omega^k has s in (0.8, 1.2), and at most one has s in -phi^-2·(0.8, 1.2). For k = 0, the only beta in the strip are 1 and eps^-1, and both give r = 0. On the strip, |r(beta)| < 0.06.

LEMMA D (digit choice, proved). Let c_l = 1/11 for l = 11 and c_l = 1/16 for l >= 19. There is zeta in Z_l with ||{zeta r(beta)}_l|| >= c_l for every beta with s in Sigma and k ≠ 0.

THEOREM E (proved, given Lemma B's certified constant). The colouring c(x) = (floor(20{chi_+(x)}), floor(20{chi_-(x)}), floor(N_l {zeta x}_l)) is proper on Gamma_l, with N_l = 11 for l = 11 and N_l = 16 for l >= 19. Hence chi(Gamma_l) <= 4400 for l = 11 and chi(Gamma_l) <= 6400 for every split l >= 19. By L2 and T2 of limit_graph_gamma.md, chi_inf(T) <= 6400 for every odd T with at most one split prime factor, for any exponent, any power of 5 and any inert part. This settles the question that Proposition 5 of chi_orbit_bound.md left open (chi(Gamma_l) < infinity): F(1) <= 6400 holds uniformly in l and e.

THEOREM F (reduction for several primes, proved). Let S = {l_1, ..., l_w} be split primes. Put rho(x) = 2 sqrt5 x, lambda_i(x) = {2 s5_i x}_{l_i}, and chi_z = rho - sum_i z_i lambda_i for z in {±1}^w. For beta = ±eps^n prod omega_i^{k_i}, let sigma_i = sign(k_i), with either sign allowed when k_i = 0. Then chi_{-sigma}(r) ≡ f_A(s) and chi_sigma(r) ≡ f_C(s). Consequently:
 chi(Gamma_S) <= (20(w+1))^{w+1} · chi(Gamma_S^Sigma),
where Gamma_S^Sigma is the Cayley graph on G_S whose connection set is {±r(beta) : sigma1(beta) in Sigma}. All of its edges have real length below 0.06, and it has at most 2 connection elements per exponent vector k in Z^w. So, for each finite S, Gamma_S is finitely colourable if and only if its subgraph of real-short edges is.

COMPUTED (sanity checks and evidence, not proofs).
 (i) The identities of A and F agree to within 1e-44 on 1124 elements (l = 11, 29, and S = {11, 19}).
 (ii) The colouring of Theorem E has no monochromatic edge on windows [0, 8000) of Cay(Z, D_T^inf) for T = 5·11^3 and T = 5·29^2.
 (iii) For S = {11, 19}, the strip has 6, 12, 22, ..., 180, 276 elements at levels max|k_i| = 1, 2, 3, ..., 26, 40, so the count grows linearly. A greedy one-character-per-prime digit scheme survives to level 40, but its forbidden digit sets nearly fill up (18 of 19 at levels 30 and 40).
 (iv) Single-real-character Pisot colourings g(bin(alpha x/sqrt5), x mod M) of D_145 fail in the conservative bin model, with no colouring for k <= 9 in the tested ranges.

NOT PROVED: chi(Gamma) < infinity; chi(Gamma_S) < infinity for |S| >= 2; chi_inf(5l) = 5 for any unlucky l; any 5- or 6-colouring of D_{5l}^inf.

## Proofs

[0] PROPOSITION 0. The elements of Z[phi] of norm -25 generate ideals of norm 25. Since 5 = (sqrt5)^2 ramifies, the only such ideal is (5), so these elements are ±5 phi^m with m odd. So S_5^inf = {(±L_m - 1)/2 : m odd, 3 ∤ m} \ {0}. Divisibility by 3 is excluded because L_m is even iff 3 | m.
Write L_m = sqrt5 F_m + 2 phi'^m. For odd m with 3 ∤ m, F_m is odd. Then d/sqrt5 = ±(F_m/2 + phi'^m/sqrt5) - 1/(2 sqrt5) ≡ 0.2764 ± phi'^m/sqrt5 (mod 1).
- For |m| >= 5, |phi'^m|/sqrt5 <= phi^-5/sqrt5 = 0.0403, so the phase lies in [0.2361, 0.3167].
- For m = ±1, d = -1 and ||1/sqrt5|| = 0.447.
The minimum is ||5/sqrt5|| = sqrt5 - 2 > 1/5. Two integers in the same arc of length 1/5 differ by e with ||e/sqrt5|| < 1/5, so e is not in D_5^inf.

[A] THEOREM A. Write gamma = phi·beta = a + b phi with a, b in Z[1/l]. Then sigma1(gamma) - sigma2(gamma) = b sqrt5, and r = (Tr gamma - 1)/10.
Real place. 2 sqrt5 r = (Tr gamma - 1)/sqrt5. Using Tr gamma = 2 sigma2(gamma) + sqrt5 b, this is (2 sigma2(gamma) - 1)/sqrt5 + b = f_A(s) + b, because sigma2(gamma) = phi'·sigma2(beta) = phi'/s (as N(beta) = 1). Using Tr gamma = 2 sigma1(gamma) - sqrt5 b instead gives (2 phi s - 1)/sqrt5 - b = f_C(s) - b.
l-adic place. In Q_l, Tr gamma = 2 iota(gamma) - s5 b = 2 iota(gamma') + s5 b. So 2 s5 r = s5(Tr gamma - 1)/5.
- If k >= 0, then v_pi(beta) = k >= 0, so iota(gamma) is in Z_l. Then ±2 s5 r = ±s5(2 iota(gamma) - 1)/5 ∓ b ≡ ∓b mod Z_l.
- If k <= 0, then iota(gamma') is in Z_l, and ±2 s5 r ≡ ±b mod Z_l.
For q in Z[1/l], {q}_l ≡ q mod 1, because q - {q}_l lies in Z_l ∩ Z[1/l] = Z.
Combining the two places: for k >= 0, chi_+(r) ≡ 2 sqrt5 r + b = f_C(s) and chi_-(r) ≡ 2 sqrt5 r - b = f_A(s). The case k <= 0 is symmetric.
chi_± are characters of Z[1/(10l)]: the defect {zeta(x+y)}_l - {zeta x}_l - {zeta y}_l lies in Z_l ∩ Z[1/l] = Z.

[B] LEMMA B. Substitute u = phi s. Then f_C = (2u - 1)/sqrt5 and f_A = (-2/u - 1)/sqrt5.
Joint zeros. Suppose f_A = j and f_C = j' with j, j' integers. Then (1 + sqrt5 j)(1 + sqrt5 j') = -4. Comparing the sqrt5-parts gives j' = -j, and then 1 - 5j^2 = -4 gives j = ±1. So s = 1 or s = -phi^-2.
Tails. For |u| >= 20, f_A lies in [-0.4919, -0.4025], so ||f_A|| >= 0.4025. For |u| <= 1/20, the same holds for f_C.
Middle range. On t = log|u| in [-log 20, log 20], both f_A and f_C have t-derivative below 18, and ||·|| is 1-Lipschitz. A grid with step 2e-6 over both signs, with Sigma removed, gives a minimum of 0.051463 (near s = 0.3446, where f_A ~ -2.05 and f_C ~ 0.05). The Lipschitz error is at most 3.6e-5, so F >= 0.0514 off Sigma. This uses floating point with an error near 1e-15, far below the margin, but not interval arithmetic.

[C] LEMMA C. log|sigma1(±eps^n omega^k)| = 2n log phi + k log|sigma1 omega|. Each target window, log|t| + (log 0.8, log 1.2) for t in {1, -phi^-2}, has length log 1.5 = 0.405 < 2 log phi = 0.962. So at most one n fits, and the sign of t then fixes ±.
For k = 0: sigma1(±eps^n) = ±(-1)^n phi^{2n}. This lies in Sigma only for beta = 1 (s = 1) and beta = eps^-1 (s = -phi^-2). The element -1 has s = -1, and -eps^-1 has s = phi^-2 > 0, and neither is in Sigma.
r(s) = (phi(s - 1) + phi'(1/s - 1))/10 is increasing on each half-line. Its values at the strip ends are -0.048, 0.043, -0.039 and 0.053.

[D] LEMMA D. Let beta be in the strip with |k| = j >= 1. By Theorem 1(c), v_l(r) = -j, so r = u l^{-j} with u in Z_(l)^*, and {zeta r}_l = ((zeta u) mod l^j)/l^j.
Write zeta = sum zeta_i l^i. The leading base-l digit of zeta u mod l^j is t = (zeta_{j-1} u_0 + c) mod l, where u_0 = u mod l ≠ 0 and c depends only on zeta_0, ..., zeta_{j-2}. So t is a bijective function of zeta_{j-1}, and {zeta r}_l lies in [t/l, (t+1)/l).
That interval lies in [c_l, 1 - c_l] unless t < c_l·l or t > l - 1 - c_l·l. At most 2 ceil(c_l l) values of t fail this. By Lemma C there are at most 4 such beta at level j (k = ±j). Choose zeta_{j-1} level by level, avoiding at most 8 ceil(c_l l) values:
- for l = 11 and c_l = 1/11, that is 8 < 11;
- for l >= 19 and c_l = 1/16, it is at most l/2 + 8 < l.

[E] THEOREM E. Suppose c(x) = c(y) and y - x = ±r(beta) with r ≠ 0. Then ||chi_±(r)|| < 1/20 = 0.05 and ||{zeta r}_l|| < 1/N_l = c_l.
- If s is not in Sigma, Theorem A and Lemma B give max(||chi_+(r)||, ||chi_-(r)||) = F(s) >= 0.0514, a contradiction.
- If s is in Sigma, Lemma C gives k ≠ 0, and Lemma D gives ||{zeta r}_l|| >= c_l, a contradiction.
For T = 5^a l^e times an inert part, Cay(Z, D_T^inf) ≅ Gamma[(1/T*)Z] ⊂ Gamma_l, by L2 and T2.

[F] THEOREM F. At l_i, Theorem A's computation gives {2 z_i s5_i r}_{l_i} = {-z_i sigma_i b}_{l_i}. When k_i = 0, b is l_i-integral and the term is 0 for either z_i.
- For z = -sigma, every term equals {b}_{l_i}. By partial fractions, sum_i {b}_{l_i} ≡ b mod 1 for b in Z[1/S], so chi_{-sigma}(r) ≡ 2 sqrt5 r - b = f_A(s).
- For z = sigma, every term equals {-b}_{l_i}, so chi_sigma(r) ≡ 2 sqrt5 r + b = f_C(s).
Colour x by its cell in the torus of values (rho, lambda_1, ..., lambda_w), with cell side 1/(20(w+1)). Two vertices in one cell differ by e with ||chi_z(e)|| < 0.05 for every z. So no edge with s outside Sigma joins two vertices in one cell (Lemma B). Multiplying by any proper colouring of Gamma_S^Sigma gives the bound. The count of at most 2 elements per vector k is Lemma C, with the sum of k_i log|sigma1 omega_i| in place of k log|sigma1 omega|.

[WHY THE DIGIT SCHEME STOPS AT w = 1] For w >= 2, the strip is a codimension-1 slab in the rank-(w+1) lattice. Level j has about C j^(w-1) elements; for S = {11, 19}, about 7j. Each element is unsafe with probability about (2c)^2. In a Peres-Schlag local-lemma window this load grows without bound, so a fixed finite set of l-adic characters is expected to fail at some large level. This is a heuristic, not proved. The greedy test of computation (iii) has not failed yet at level 40.

## External results used

- Theorem 1(a),(c) of gamma_linearization.md (repository, unaudited): R_+ ∩ Z[1/(5S)] = {L(beta - 1) : beta in ±<eps, omega_l>}, with v_l(L(beta - 1)) = -|k_l|. Used in Theorem E and Lemma D.
- L2 and T2 of limit_graph_gamma.md (repository): chi_inf(T) = chi_inf(T*), and Cay(Z, D_T^inf) ≅ Gamma[(1/T)Z]. Used to pass from chi(Gamma_l) to chi_inf(T).
- Standard algebraic number theory: Z[phi] is a PID, the units are ±phi^Z, 5 ramifies, and the split l = pi pi' with iota_pi into Q_l. The partial-fraction identity q ≡ sum_i {q}_{l_i} mod 1 for q in Z[1/S] is elementary.
- No web sources were used.

## Checks

All scripts are in scripts_gamma_finite. Each ran with py in under 60 s, and the repository was not touched.

- bohr.py and chk.py: exact orbit enumeration of S_T^inf with Pisot-phase tails (residue-state periods and an explicit error radius). It matches brute force on |d| <= 3000 for T = 5, 55, 145, 295, 305.
- scan1.py to scan4.py, one.py and sub.py: bin-model SAT for Pisot-Bohr colourings.
  - T = 5 is 5-colourable with theta = 1/sqrt5. The colouring found is the rotation floor(5{x/sqrt5}), which led to Proposition 0.
  - T = 145 fails in every tested model. The failing part is the exact intermediate-range distances (for example M = 233 with the exact part alone is UNSAT, while the tails alone are SAT).
- adelic.py: Theorem A identity, max error 4.7e-68 (l = 11, 440 elements) and 9.2e-72 (l = 29, 284 elements).
- multi.py: Theorem F identity for S = {11, 19}, 400 random elements, max error 1.3e-44.
- cdelta.py, cdelta2.py and crig.py: Lemma B.
  - Grid minimum 0.051463 and certified bound 0.0514.
  - The minimum does not depend on delta in [0.1, 0.44].
  - m = 1 is best among m = 1 to 8.
- colour_l.py: full three-character check on boxes |n| <= 40, |k| <= 10 (l = 11) and |k| <= 8 (l = 29).
  - At most 4 strip elements per level.
  - Off-strip minimum of max(||chi_±||) is 0.073 for l = 11 and 0.105 for l = 29.
  - On-strip chi_± values reach 1.7e-3 (l = 29), so the zeta character is needed.
  - The minimum of ||chi_zeta|| on the strip is at least its target.
- brute_check.py: the explicit colouring has 0 monochromatic edges on [0, 8000).
  - T = 6655: 24 distances, 4400 colours used.
  - T = 4205: 19 distances, 5183 colours used.
- strip2.py, strip2b.py and strip2c.py: strip counts and greedy digit tests for S = {11, 19} up to level 40.

## Gaps

- The main question is open: chi(Gamma) is neither proved finite nor infinite. Theorem E covers only one split prime, so chi(Gamma_S) for |S| >= 2 remains open, reduced by Theorem F to the real-short subgraph Gamma_S^Sigma.
- Theorem F's off-strip factor (20(w+1))^(w+1) is not uniform in w: every sign pattern needs its own aligned pair chi_{±sigma}. Even a bounded short-edge graph would therefore not give chi(Gamma) < infinity by this route.
- Target (a) was not reached: there is no explicit 5- or 6-colouring of D_{5l}^inf for an unlucky l, and the uniform bound 6400 is far from 5. Single-real-character Pisot colourings fail in the bin model for T = 145 (no colouring for k <= 9 at M = 1, N = 200; none for k <= 6 with M = 29; none for k <= 8 with M = 29, alpha = 10, N = 20). The bin model is conservative, so this is evidence, not proof of nonexistence.
- Lemma B's constant 0.0514 is certified by a floating-point grid plus a Lipschitz bound, not by interval arithmetic. The joint-zero algebra and the tail bounds are by hand.
- chi_inf(5) >= 5 rests on the earlier uncertified SAT run (n = 400). Only the upper bound in Proposition 0 is by hand.
- Theorem E relies on Theorem 1(c) of gamma_linearization.md (v_l(r) = -|k|, and the form of the connection set). That theorem is unaudited, though this round's scripts asserted the valuation on every strip element.
- None of this round's results are audited. Theorem A, Lemmas C and D and Theorem F were re-derived once by me and checked numerically (identity errors below 1e-44).
- The w = 2 evidence (strip counts, greedy survival to level 40) is a finite computation. The claim that the digit scheme must eventually fail is heuristic.

## Missing estimate

To finish chi(Gamma_S) < infinity for S = {l1, l2}: a finite colouring of the short-edge graph Gamma_S^Sigma. Its connection set is {r(beta) : sigma1(beta) within a factor 1.2 of 1 or -phi^-2}, a rank-2 slab with about 7j elements at level max|k_i| = j for (11, 19). Two cases matter:
- In Bohr form, this needs finitely many l-adic characters zeta_i with ||(zeta·r(beta))|| >= c on the whole slab, that is, an l-adic Diophantine (local-lemma) estimate that beats linear growth per level.
- Conversely, Bohr recurrence of the slab for every finite set of characters would rule out every Bohr colouring of Gamma_{l1,l2}. Then any finite colouring of Gamma would have to be non-Bohr.
For chi(Gamma) itself, the off-strip treatment must in addition be made uniform in w. The current cost is (20(w+1))^(w+1) colours, one aligned pair of characters for each sign pattern of the exponent vector.

## Next steps

- Audit Theorem A, Lemmas C and D, Theorem E and Theorem F. They are short algebra plus one digit argument. Redo Lemma B's 0.0514 with interval arithmetic.
- Record in the ledger: chi_inf(T) <= 6400 for every odd T with omega_s(T) <= 1 (all exponents), and chi_inf(5) = 5 (upper bound by the rotation floor(5{x/sqrt5}), lower bound SAT). Correct Proposition 5 of chi_orbit_bound.md: F(1) is finite.
- Lower the 6400. The off-strip values (chi_+, chi_-) lie on the curve s -> (f_A(s), f_C(s)) in T^2, which accumulates on two circles at -1/sqrt5. Colour T^2 against that curve instead of using 20 x 20 boxes.
- For w = 2: decide Bohr recurrence of the slab. Rerun the greedy with t >= 2 characters per prime to much higher levels (outside the 60 s limit), and look for the configuration that blocks it. Try orbit-closure results for rank-3 S-unit actions (Berend, Lindenstrauss and Z. Wang) on the slab.
- Try to make the off-strip part uniform in w, for example with characters adapted to the sign pattern of the largest exponents only, together with a Peres-Schlag step for the bounded rest.
- chi_inf(5l) = 5 for an unlucky l is still open. Any small colouring must be non-Bohr in the intermediate range |T|/10 < |d| < |T|^2, where Pisot phases have not converged.

