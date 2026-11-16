# Three-term relations and locally sparse distance graphs

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: sum_T chi(G_T) = O(h log h / log log h). The three-term theorem passed two audits (algebra and counting). The audit of the counting found fixable gaps only; see its section.

# Result

## Status

partial

## Summary

Summed over all diagonals, the solutions of +-d1 +- d2 +- d3 = 0 inside the distance sets, other than the reflection solutions, number O(h); so every G_T is locally sparse and sum_T chi(G_T) = O(h log h / log log h) by the Alon-Krivelevich-Sudakov theorem, but the full factor log h (a linear total) is not reached.

## Statements

NOTATION. h >= 2 integer, A = ceil(h/2), K = floor(h/2). For odd T: s = (T-1)/2, I_T = [max(0,-s), min(A,K-s)) (integers), n_T = |I_T|, Q(T,d) = 20 d^2 + 4 T d + T^2, S_T = S_T(h) = { d in Z, d != 0 : Q(T,d) = L^2 for an integer 0 < L < h }, D_T = { |d| : d in S_T, |d| < n_T }, k_T = |D_T|, G_T = graph on I_T with i ~ i' iff |i-i'| in D_T. The diagonals are the h-1 odd T with n_T >= 1 (all have |T| <= h-1). ||x|| = distance from x to the nearest integer. A RELATION of T is a pair (d,e), d = (d1,d2,d3) in S_T^3, e = (e1,e2,e3) in {+1,-1}^3, with e1 d1 + e2 d2 + e3 d3 = 0; put e0 = e1+e2+e3. It is a REFLECTION relation if e0 = +-1 and d_j = -T/5 for the index j with e_j = -e0 (these exist only when 5 | T and say d + d' = -T/5). R_T = R_T(h) = number of relations of T that are not reflection relations.

THEOREM 1 (three-term relations). There is an absolute constant C1 such that for every h >= 2: sum over odd T with 0 < |T| < h of R_T(h) <= C1 h. Conversely this sum is >= 12 (h/58 - 1) (offsets T = 11t carry 2t + 3t = 5t), so the order h is exact.

LEMMA 5.1 (local sparsity). For every h, every diagonal T and every vertex i of G_T: the maximum degree of G_T is at most 2 k_T, and at most 6 k_T + R_T edges of G_T have both ends in the neighbourhood of i. In particular G_T is triangle-free when R_T = 0 and 5 does not divide T.

THEOREM 2 (total bound; uses the cited theorem of Alon, Krivelevich, Sudakov). There are absolute constants C0, C2 such that
(1) for every h and every diagonal T with k_T >= 13 and R_T <= k_T^(3/2): chi(G_T) <= C0 k_T / log k_T;
(2) for every h: sum over the diagonals with R_T > k_T^(3/2) of (k_T + 1) <= 2 C1 h;
(3) for every h >= 16: sum over all diagonals of chi(G_T) <= C2 h log h / log log h.
COROLLARY. For h >= 16 the labels (i,j), 0 <= i < A, 0 <= j < K, split into at most C2 h log h / log log h classes, each a subset of one diagonal and independent in its G_T; by Proposition 1 of research_archive/2026-11-12/arc_classes_monotone_partition.md each class is monotone of slope 1, P-free and has no right angle among its black points. (Previous bound: O(h log h).)

PROPOSITION 3 (relations split at a large prime). Let h >= 5, T odd, 0 < |T| < h, p a prime divisor of T, r >= 1 an integer with p^3 > 5 r^2 h^2. If (c_d), d in S_T, are integers with sum |c_d| <= r and sum c_d d = 0, then sum over the d not divisible by p of c_d (10 d + T) = 0. Hence s = sum_{p not | d} c_d is even, 5 | s if 5 does not divide T, sum_{p | d} c_d d = s T/10, and s = 0 if c is supported on the d prime to p. Consequence: if E_p = { delta in D_T : p does not divide delta }, k = |E_p| and p^3 > 5 (m k)^2 h^2, every integer relation sum c_delta delta = 0 on E_p with |c_delta| <= m has even coefficient sum (the even-relation condition (6) of research_archive/2026-11-12/continuation_arc_parity_riesz.md).

PROPOSITION 4 (one rotation for all distances prime to p). Let T be odd, 0 < |T| < h, p != 5 a prime dividing T exactly once, t = T/p, eta = 10.1 h / p^(3/2). For every real z0 there is a real theta with (i) || theta d - t z0 || <= eta for every d in S_T not divisible by p, and (ii) theta p d' = -10 z0 d' modulo 1 for every integer d'.

COROLLARY 4.1. Let a prime p >= 19 h^(2/3) divide T, and k' = #{ delta in D_T : p | delta }. (1) There is an integer N with || N d/p - 1/2 || <= 1/8 for every d in S_T prime to p; so i -> floor(3 frac(N i/p)) properly 3-colours the distance graph of the distances of D_T prime to p, and chi(G_T) <= 3 (k' + 1). (2) If M is an integer with (2k'+2)/M + 2 eta < 1, some theta has ||theta delta|| >= 1/M for all delta in D_T; so the diagonal has an arc partition with at most floor((2k'+2)/(1 - 2 eta)) + 1 classes (the union bound for the whole diagonal gives 2 k_T + 1).

NOT PROVED: sum_T chi(G_T) = O(h), or any bound o(h log h / log log h).

## Proofs

[0] KNOWN INPUT, re-proved: sum_T |S_T| <= 2 h log h. For d in S_T, (x,y) = (4d, T+2d) satisfies x^2+y^2 = L^2 with x != 0, y odd, 0 < L < h, and (T,d) -> (x,y) is injective. Positive solutions with x even are (2guv, g(u^2-v^2), g(u^2+v^2)), u > v >= 1, g >= 1. So the count is <= 4 sum_{u>v>=1, u^2+v^2<h} floor((h-1)/(u^2+v^2)) <= 4h sum_{2<=u<sqrt h} (u-1)/u^2 <= 4h log(sqrt h).

[1] THE RING. phi = (1+sqrt5)/2, O = Z[phi], x' = conjugate, N(a+b phi) = a^2+ab-b^2, Tr = 2a+b, |x| and |x'| the two real absolute values. Standard facts: (O1) O is norm-Euclidean, hence a PID with unique factorization of ideals; v_P = valuation at a prime ideal P; N((x)) = |N(x)|. (O2) Units are +-phi^n; |phi'| = 1/phi. (O3) A rational prime p is inert (a prime element of O), or split (pO = P P', P != P' of norm p, exchanged by conjugation, O/P = Z/pZ), or p = 5 = (sqrt5)^2 (O = Z[x]/(x^2-x-1), discriminant 5). (O4) v_{P'}(x) = v_P(x'). (O5) The number of ideals of norm n is <= tau(n) (prime by prime: a+1 ideals P^i P'^(a-i) of norm p^a at a split prime, at most one otherwise).

[2] DICTIONARY. T odd, d in S_T, Q(T,d) = L^2, L > 0, X = 10d + T. Then X^2 - 5L^2 = -4T^2, X and L are odd, beta_d := (X-L)/2 + L phi = (X + L sqrt5)/2 is in O, N(beta_d) = -T^2, Tr(beta_d) = 10d + T, and |beta_d|, |beta_d'| < sqrt5 L < sqrt5 h because |X| = sqrt(5L^2-4T^2) < sqrt5 L. The trace recovers d.

[3] PROOF OF THEOREM 1.
(3.1) A CONFIGURATION is c = (T; beta_1,beta_2,beta_3; e1,e2,e3), T nonzero odd, beta_j in O, e_j = +-1, e0 = e1+e2+e3, with (C1) N(beta_j) = -T^2; (C2) sum e_j Tr(beta_j) = e0 T; (C3) e_j Tr(beta_j) != e0 T for each j. Size ||c|| = max_j max(|beta_j|,|beta_j'|) >= |T|. PRIMITIVE: no rational prime divides all three beta_j. N(x) := number of primitive configurations with |T| <= x and ||c|| <= sqrt5 x.
(3.2) Relations to configurations. For odd 0 < |T| < h, (d,e) -> (T; beta_{d1},beta_{d2},beta_{d3}; e) injects the non-reflection relations into configurations with ||c|| < sqrt5 h. (C2): sum e_j (10 d_j + T) = e0 T. (C3): if e_j(10 d_j + T) = e0 T then either e_j = e0 and d_j = 0 (not in S_T); or e0 = +-3, e_j = e0/3, d_j = T/5, but Q(T,T/5) = 13T^2/5 is not a square (65 is not a square); or e0 = +-1, e_j = -e0, d_j = -T/5, a reflection relation.
(3.3) Content. Let G be the largest positive integer dividing all beta_j in O. Then G^2 | T^2, so G | T, and c/G is a primitive configuration ((C1)-(C3) are homogeneous) with ||c/G|| = ||c||/G; c -> (G, c/G) is injective.
(3.4) Local structure. Let c be primitive and p a prime dividing T exactly once. (a) p is not inert: an inert p is a prime element dividing beta_j beta_j' = -T^2, hence beta_j or beta_j', hence (conjugating) beta_j, for all j. p != 5: if 5 | T write beta_j = a + b phi; N = (a+3b)^2 mod 5, so a = 2b mod 5 and beta_j = b(2+phi) + 5c = sqrt5 (b phi + c sqrt5) because 2+phi = sqrt5 phi; so beta_j = sqrt5 gamma_j with N(gamma_j) = T^2/5 divisible by 5, and the same step gives sqrt5 | gamma_j, so 5 | beta_j for all j. Hence pO = P P' splits. (b) v_P(beta_j) + v_{P'}(beta_j) = v_P(T^2) = 2; put sigma_j(P) = v_P(beta_j) - 1 in {-1,0,1}; sigma_j(P') = -sigma_j(P). (c) sigma(P) = (sigma_1,sigma_2,sigma_3)(P) has at most one zero coordinate: three zeros mean pO | beta_j for all j; if exactly two are zero, say sigma_j(P) = 0 for j != j0 and (after exchanging P, P') sigma_{j0}(P) = 1, then beta_{j0} is in P^2, beta_{j0}' is not in P, so Tr(beta_{j0}) is not in P, while by (C2) e_{j0} Tr(beta_{j0}) = e0 T - sum_{j != j0} e_j Tr(beta_j) lies in pZ, inside P. Contradiction.
(3.5) Types and blocks. Sigma = vectors of {-1,0,1}^3 with at most one zero (20 vectors); Sigma+ = one of each pair {sigma,-sigma} (10 vectors). Each prime p dividing T exactly once has exactly one prime ideal P_p above it with sigma(P_p) in Sigma+; this vector is the TYPE of p. T1 = product of the primes dividing T exactly once, T2 = |T|/T1 (squarefull), P_sigma = product of the primes of type sigma, k_sigma = product of the ideals P_p over these primes; prod_sigma P_sigma = T1. Fix sigma, P = P_sigma, m = |T|/P. Then k_sigma = (kappa) with |N(kappa)| = P and 1 <= |kappa/kappa'| < phi^2 (multiply a generator by a power of phi; unique up to sign), so |kappa|^2 >= P and |kappa'|^2 > P/phi^2. kappa is not divisible by a rational prime q, because qO (a prime of norm q^2, or Q Q', or Q^2) does not divide a product of distinct degree-one primes that never contains both P_p and P_p'. Define nu_j = beta_j/kappa^2 if sigma_j = 1 (k_sigma^2 divides (beta_j) since v_{P_p}(beta_j) = 2 for each p of the type), nu_j = beta_j/kappa'^2 if sigma_j = -1 (the conjugate ideal), nu_j = beta_j/P if sigma_j = 0 (each pO divides beta_j). Then nu_j is in O, N(nu_j) = -m^2, and |nu_j|, |nu_j'| <= phi^2 ||c||/P. (If no prime has type sigma: P = 1, kappa = +-1, nu_j = beta_j.)
(3.6) Elimination. Let sT = sign T, eta = sign N(kappa), Omega = sum_{sigma_j=1} e_j nu_j + sum_{sigma_j=-1} e_j nu_j' in O, c0 = sT e0 m - sum_{sigma_j=0} e_j Tr(nu_j) in Z. Since Tr(beta_j) = Tr(kappa^2 nu_j), Tr(kappa^2 nu_j') or P Tr(nu_j) in the three cases, (C2) reads Tr(kappa^2 Omega) = c0 P, i.e. Omega kappa^2 + Omega' kappa'^2 = c0 eta kappa kappa', i.e. rho = kappa/kappa' satisfies Omega rho^2 - eta c0 rho + Omega' = 0. c0 != 0: if sigma has no zero coordinate, c0 P = e0 T != 0; otherwise there is exactly one, j0, and c0 P = e0 T - e_{j0} Tr(beta_{j0}) != 0 by (C3). Omega != 0: otherwise Omega' = 0 and eta c0 rho = 0, which is false.
(3.7) Reconstruction. The tuple D = (sigma, sT, eta, e, m, nu_1, nu_2, nu_3) determines the primitive configuration up to two possibilities: D gives Omega, c0, hence at most two values of rho (a genuine quadratic). rho determines kappa up to sign: if kappa_1/kappa_1' = kappa_2/kappa_2' with both not divisible by rational primes, then kappa_1/kappa_2 = a/b is rational in lowest terms, b kappa_1 = a kappa_2, and with ra + sb = 1, kappa_2 = b (r kappa_1 + s kappa_2), so b = +-1; likewise a = +-1. Then P = |N(kappa)|, T = sT P m, beta_j = kappa^2 nu_j, kappa'^2 nu_j or P nu_j.
(3.8) Counts. (i) For m >= 1, Y >= 1: #{nu in O : |N(nu)| = m^2, |nu| <= Y, |nu'| <= Y} <= 2 tau(m^2)(1 + 2 log Y/log phi): at most tau(m^2) ideals; generators +-phi^n nu_0; |nu| |nu'| = m^2 >= 1 and |nu'| <= Y give phi^n |nu_0| in [1/Y, Y]. (ii) sum_{n<=z} tau(n)^6 <= z (1+log z)^64: from tau(ab) <= tau(a) tau(b), tau(n)^k <= sum_{ab=n} tau(a)^(k-1) tau(b)^(k-1), so sum_{n<=z} tau(n)^k/n <= (sum_{a<=z} tau(a)^(k-1)/a)^2 <= (1+log z)^(2^k) by induction, and sum_{n<=z} tau(n)^k <= z sum_{n<=z} tau(n)^k/n. (iii) Cq = sum over squarefull q of tau(q)^6 q^(-9/10) is finite: Euler product, exp(sum_p sum_{a>=2} (a+1)^6 p^(-9a/10)) with inner sum <= const * p^(-9/5).
(3.9) N(x) <= C4 x^(9/10) (1+log x)^67 for x >= 1. Take a primitive c with |T| <= x, ||c|| <= sqrt5 x and the sigma in Sigma+ with P = P_sigma largest; P >= T1^(1/10). With q = T2, m1 = T1/P: m = q m1, q squarefull <= x, 1 <= m1 <= T1^(9/10) <= (x/q)^(9/10), and |nu_j|, |nu_j'| <= phi^2 sqrt5 x. By (3.7), N(x) <= 2 #{D}. There are 320 choices of (sigma, sT, eta, e). By (3.8)(i) and 1 + 2 log(phi^2 sqrt5 x)/log phi <= 9(1+log x), each nu_j has at most 18 tau(m)^2 (1+log x) values (tau(m^2) <= tau(m)^2). So #{(m,nu_1,nu_2,nu_3)} <= sum_q sum_{m1 <= (x/q)^(9/10)} (18 tau(q)^2 tau(m1)^2 (1+log x))^3 <= 18^3 Cq x^(9/10) (1+log x)^67 by (ii), (iii).
(3.10) Conclusion. By (3.2), sum_T R_T <= number of configurations with 0 < |T| < h and ||c|| < sqrt5 h; sorting by content (3.3), this is <= sum_{G=1}^{h} N(h/G) <= C4 C5 sum_{G<=h} (h/G)^(19/20) <= 20 C4 C5 h, where (1+log u)^67 <= C5 u^(1/20). The power saving is for primitive configurations; the factor h comes only from dilations.
(3.11) Lower bound. For odd t with 29t < h: Q(11t,2t) = (17t)^2, Q(11t,-3t) = (13t)^2, Q(11t,5t) = (29t)^2, and 2t - (-3t) - 5t = 0; the minority-sign element is 2t != -11t/5, so it is not a reflection relation; 6 orders and 2 global signs give 12 relations.

[4] LEMMA 5.1. Neighbours of i are among i + x, x in +-D_T. An edge inside the neighbourhood is an unordered pair {x,y} of +-D_T, x > y, with z = x - y in D_T (an inner pair). Fix delta -> d(delta) in S_T with |d(delta)| = delta; put d1 = d(|x|), d2 = d(|y|), d3 = d(z), e1 = x/d1, e2 = -y/d2, e3 = -z/d3. Then e1 d1 + e2 d2 + e3 d3 = x - y - z = 0 and (x,y) = (e1 d1, -e2 d2), so inner pairs inject into relations. If the relation is a reflection relation, one of |x|, |y|, x-y equals |T|/5: at most 2(2k_T - 1) inner pairs contain +-|T|/5 and at most 2 k_T have x - y = |T|/5. The others inject into non-reflection relations.

[5] THEOREM 2. Cited theorem (Alon, Krivelevich, Sudakov, Theorem 1.1): there are absolute c, d0 such that a graph of maximum degree at most d >= d0 in which every neighbourhood spans at most d^2/f edges (f > 1) has chi <= c d/log f. (1) k = k_T >= 13, R_T <= k^(3/2): d = 2k, f = (4/7) k^(1/2) > 2; by Lemma 5.1 neighbourhoods span <= 6k + k^(3/2) <= 7 k^(3/2) = d^2/f edges, and log f >= (1/4) log k, so chi <= 8 c k/log k if 2k >= d0; if 2k < d0 use chi <= k+1 <= d0. So C0 = max(8c, d0 log d0) works. (2) R_T > k_T^(3/2) gives R_T >= 1 and k_T < R_T, so k_T + 1 <= 2 R_T; apply Theorem 1. (3) chi(G_T) <= k_T + 1 always (greedy in increasing order). So sum_T chi <= 13h + C0 S + 2 C1 h with S = sum_{k_T >= 13} k_T/log k_T. Split at K0 = (log h)^(1/2): terms with k_T <= K0 are <= K0; in the others log k_T > (1/2) log log h, and sum_T k_T <= 2 h log h by [0]. So S <= h (log h)^(1/2) + 4 h log h/log log h <= 5 h log h/log log h, and log h/log log h >= 1 for h >= 16. C2 = 13 + 5 C0 + 2 C1.

[6] PROPOSITION 3. p^3 > 125 so p > 5, and p^2 > h > |T| so p divides T exactly once. For d in S_T: p | beta_d iff p | d (p | beta_d gives p | 10d+T; p | d gives p | X_d and p | L_d). If p is inert, p | beta_d beta_d' forces p | beta_d for all d, so no d is prime to p and the claim is empty. Let pO = P P'. For d prime to p, (v_P, v_{P'})(beta_d) is (2,0) or (0,2); let b_d be the conjugate of beta_d in P'^2, so b_d' is in P^2 and 10d+T = b_d + b_d'. E := sum_{p not | d} c_d b_d lies in P'^2, and modulo P: E = sum_{p not | d} c_d (10d+T) = (sum c_d) T - sum_{p | d} c_d (10d+T) = 0 (use sum c_d (10d+T) = (sum c_d) T, p | T, p | 10d+T when p | d). So p^3 | N(E), while |E|, |E'| < r sqrt5 h give |N(E)| < 5 r^2 h^2 < p^3. Hence E = 0 and sum_{p not | d} c_d (10d+T) = E + E' = 0. Then 10 sum_{p not | d} c_d d = -T s with T odd gives the rest. For positive distances choose d(delta) as in [4] and apply this to c_delta sign(d(delta)); the parity of the coefficient sum is unchanged.

[7] PROPOSITION 4. If p is inert, no d in S_T is prime to p (as in [6], p != 2, 5) and theta = -10 z0/p works. Let pO = P P', P = (pi), 1 <= |pi/pi'| < phi^2, so |pi|^2 < phi^2 p, |pi'|^2 <= p. For d prime to p let b_d be as in [6] and zeta_d = b_d/pi'^2 in O: X_d = 10d+T = Tr(pi'^2 zeta_d), |zeta_d| < sqrt5 h phi^2/p, |zeta_d'| = |b_d'|/|pi|^2 < sqrt5 h/p. Choose mu in O with |mu - z0 pi'| <= c* and |mu' - z0 pi| <= c*, c* = (sqrt5+2)/4 (for reals s1, s2 take b nearest to (s1-s2)/sqrt5 and a nearest to (s1+s2-b)/2; the errors are -(e1+e2)/2 and (e1-e2)/2 with |e1| <= sqrt5/2, |e2| <= 1). pi' is invertible mod P and O/P = Z/pZ, so some integer n has n pi' = mu mod P; then (n pi' - mu) pi' is in pi pi' O = pO. Put theta = 10(n - z0)/p. (ii) is clear. (i): theta d = (n-z0)(X_d - pt)/p = (n-z0) X_d/p + z0 t mod 1, and (n-z0) X_d = Tr((n pi' - mu) pi' zeta_d) + (mu - z0 pi') pi' zeta_d + (mu' - z0 pi) pi zeta_d'; the first term is in pZ, the other two are at most c* sqrt5 (phi^2 + phi) h/sqrt p < 10.1 h/sqrt p. Divide by p.
COROLLARY 4.1. p >= 19 h^(2/3) gives p > 5, p^2 > |T| and eta <= 1/8. (1) z0 = 1/2: theta = N/p with N = 10n - 5, and t z0 = 1/2 mod 1 (t odd). Two integers in one of the three arcs differ by x with ||N x/p|| < 1/3 < 3/8. Multiply with a greedy colouring for the multiples of p. (2) Let theta1 be uniform on [0,10): each event ||theta1 delta'|| < 1/M (delta = p delta' in D_T) has probability 2/M, and ||theta1 t/10|| < 1/M + eta has probability 2/M + 2 eta; so some theta1 avoids all. Apply Proposition 4 with z0 = -theta1/10: theta (p delta') = theta1 delta' mod 1 and, for d prime to p, ||theta d|| >= ||t theta1/10|| - eta >= 1/M.

[8] WHY IT STOPS AT log log h (not a theorem). The cited theorem is tight up to the constant for all admissible d, f (its abstract; Proposition 1.2 there), so degree and local sparsity give only log k_T; Lemma 5.1 is already best possible sparsity. Heuristically sum_T k_T comes from diagonals with k_T near (log h)^1.65, where log k_T is about 1.65 log log h. An arc partition with M about k/log h classes needs one theta good for all k distances, an event of proportion h^(-c); that needs the joint distribution of about log h distances, while Theorem 1 controls three (its method with r distances has 3^r types and loses the power saving beyond r of order log log h). Proposition 4 removes only the distances prime to one large prime; the multiples of p are the same problem for T/p at height h/p.

## External results used

- N. Alon, M. Krivelevich, B. Sudakov, Coloring graphs with sparse neighborhoods, J. Combin. Theory Ser. B 77 (1999), 73-82, Theorem 1.1: a graph with maximum degree at most d in which every neighbourhood spans at most d^2/f edges has chromatic number at most c d / log f (absolute c). Tightness up to the constant: Proposition 1.2 of the same paper and its abstract (DIMACS TR 98-32). Used in Theorem 2 only.
- Standard arithmetic of Z[(1+sqrt5)/2]: norm-Euclidean, units +-phi^n, decomposition of rational primes, ideals in a quadratic field. G. H. Hardy and E. M. Wright, An Introduction to the Theory of Numbers, Chapter XIV (Sections 14.7, 14.8) and Chapter XV (Sections 15.4, 15.6, 15.7). Cited by section; theorem numbers not verified.
- From the repository: Proposition 1 of research_archive/2026-11-12/arc_classes_monotone_partition.md (a subset of a diagonal is a monotone class without right angles, P-free iff independent in G_T; arc classes need ||theta d|| >= 1/M). Used for the corollaries.
- From the repository: the even-relation condition (6) and the parity Riesz lemma of research_archive/2026-11-12/continuation_arc_parity_riesz.md. Only named in the consequence of Proposition 3; not used in any proof here.

## Checks

All scripts are in scripts_local_sparsity/ and run with py in under a minute. No check failed.
1. check_triples.py, check_triples2.py (R = sum of R_T over odd |T| < h; the two enumerations agree for h <= 4000). R/h = 1.272, 1.452, 1.469, 1.483 at h = 1000, 4000, 16000, 64000, while sum |S_T|^2 / h grows 9.35, 15.12, 22.52, 32.16. About 6.6 percent of the offsets have a non-reflection relation (4228 at h = 64000).
2. check_neighbourhoods.py, h = 16384: sum k_T = 41271 (matches the 41,271 gap constraints of the 12 November report), sum R_T = 24000, 42132 inner pairs in total, no diagonal violates Lemma 5.1, and 13985 of 16383 diagonals have a triangle-free G_T.
3. check_elimination.py, h = 3000: 2154 non-reflection relations in four sign classes, 186 primitive. For each primitive one and each type that occurs: primes dividing T once split, 5 does not divide T, at most one zero pattern, exact divisions, c0 != 0, Omega != 0 and the identity Omega kappa^2 + Omega' kappa'^2 = c0 eta kappa kappa'. 306 identities checked.
4. check_abstract.py (all configurations by brute force, T > 0, four sign classes): 6376, 13208, 26488 configurations at x = 400, 800, 1600 (linear), of which 1184, 1904, 2792 primitive (sublinear). The local lemma was checked on 4368 pairs (configuration, prime).
5. check_large_prime2.py, h = 10^8, 40 primes T = p above h/20, r = 13: 660 relations with support at most 4, 250 of them mixing multiples of p with other distances, no violation of Proposition 3. Example with odd coefficient sum: T = p = 5000011, -(-7821939) + 8(-1340270) + 3(-699930) + p = 0. (check_large_prime.py at h = 6000 found no relations at all on such offsets, so it tests nothing.)
6. check_character.py, h = 10^8, 25 offsets T = p t with p > 4*10^6, t in {1, 3, 7, 11, 19}, z0 in {1/2, 1/3, 137/1000, 0}, exact rational arithmetic: all 116 distances prime to p satisfy Proposition 4(i); the largest deviation is 0.21 of the bound 10.1 h/p^(3/2); part (ii) holds exactly.

## Gaps

- The target is not reached: sum_T chi(G_T) = O(h) is not proved, and no bound o(h log h / log log h) is proved. Section [8] of the outline (why the method stops) is an explanation, not a theorem.
- Theorem 2 rests on the Alon-Krivelevich-Sudakov theorem as a black box. I could not open the paper (the author's PDF did not load). The statement was checked against the DIMACS TR 98-32 abstract and against the restatement as [AKS99, Theorem 1.1] in Anderson, Dhawan, Kuchukova, arXiv:2402.19271. The exact wording in the journal should be re-read. It is used only with 2 < f <= d.
- The facts (O1) to (O5) about Z[(1+sqrt5)/2] (Euclidean, units +-phi^n, decomposition of rational primes) are cited from textbooks and not re-proved. I did not verify theorem numbers in Hardy and Wright, so the citation is by chapter and section.
- Theorem 1 is an average over T. There is no per-diagonal bound R_T = o(k_T^2); diagonals with R_T > k_T^(3/2) are handled only through their total cost O(h).
- The constants C0, C1, C2 are not explicit (C0 depends on the constant of the cited theorem). The colourings of Theorem 2 are not explicit and are not arc classes.
- No independent audit. I re-read every step of Theorem 1, Lemma 5.1, Theorem 2 and Propositions 3 and 4, and the scripts found no failure, but nobody else has checked them.
- Unproved remarks that are not part of the theorems: the mass of sum_T k_T sits at k_T near (log h)^1.65; about a third of D_T is divisible by a split prime p; a divisor P with j prime factors would need P >= h^(1-3^(-j)) for the analogue of Proposition 4; the extension of Theorem 1 to r-term relations.

## Missing estimate

(E) There is an absolute constant C such that for every h and every odd T with n_T >= 1: chi(G_T) <= C (1 + |D_T| / log h). Arc form: some real theta has ||theta delta|| >= min(1, log h / |D_T|) / C for every delta in D_T. With sum_T |D_T| <= 2 h log h this gives sum_T chi(G_T) <= 3 C h. Local sparsity cannot give (E): it needs the joint distribution of about log h distances of D_T under one rotation, and by pigeonhole the rich diagonals do have relations with coefficients in {-1,0,1}, so the proof must use cancellation, not the absence of relations.

## Next steps

- Have Theorem 1 audited by hand: the local analysis at primes dividing T exactly once (3.4), the elimination identity (3.6), the reconstruction (3.7) and the count (3.9).
- Re-read Theorem 1.1 of Alon, Krivelevich, Sudakov in the journal and confirm the admissible range of f.
- Extend the relation count to r-term relations with odd coefficient sum, with 'degenerate' meaning an exact sub-relation in Z[phi]. Expected result: O_r(h) nondegenerate relations in total. This would bound the deletion cost of bounded-length odd relations in the Riesz programme.
- Extend Proposition 4 from one prime to a divisor P of T with j prime factors. It needs an inhomogeneous simultaneous approximation in dimension about 3^j; the expected condition is P >= C h^(1-3^(-j)).
- Compute the arc numbers M_T on diagonals with a prime factor above 19 h^(2/3) and compare with Corollary 4.1(2), to see how much of the gap to 2|D_T|/ln h this structure explains.
- For (E), try a second-moment or large-deviation argument over theta = a/q using the description beta_d/T = +-phi^j prod_p (pi_p/pi_p')^(sigma_p), which writes D_T/T as (+-2 sinh(u) - 1)/10 for u in a generalized arithmetic progression of dimension omega(T)+1.

# Audit of the algebra

## Verdict

correct

## Summary

Theorem 1 (sum over odd 0<|T|<h of R_T(h) <= C1 h, and >= 12(h/58 - 1)) holds up. I re-derived every algebraic step myself and found no error: the dictionary [2], the injection (3.2) with condition (C3) and the exclusion of reflection relations, content (3.3), the local structure (3.4) (inert primes, p = 5, at most one zero coordinate in sigma(P)), types and kappa (3.5), the elimination identity (3.6), the reconstruction (3.7), and the counts (3.8)-(3.10). Reconstruction is sharper than claimed: in every test the tuple D fixed the primitive configuration exactly (fibre size 1, while the bound allows 2). Scripts check the injection, the C3/reflection equivalence, the elimination identity and an exact reconstruction from D. They ran on all relations for h = 500, 1000, 2000, 4000 and 9000, on all abstract configurations with |T| <= 400, and on synthetic T built to exercise composite kappa and squarefull T2, branches that never occur at h <= 9000. No case failed. The lower bound is correct, and the true sum is about twice it, since negative T and repeated-entry relations add more. Remaining caveats are minor: standard facts about Z[phi] are cited, not proved; the tie-break for choosing sigma is not stated; C1 is astronomically large (about e^430 from the (1+log u)^67 <= C5 u^(1/20) step); the theorem is purely asymptotic. I audited only Theorem 1, not Lemma 5.1, Theorem 2 (AKS) or Propositions 3 and 4.

## Issues

- location: (3.9)-(3.10), constants; severity: minor; description: C1 is absolute but enormous: (1+log u)^67 <= C5 u^(1/20) forces C5 about e^415, and C4 adds 2*320*18^3*Cq. So Theorem 1 has no useful numerical content. The data show sum R_T / h is about 1.27 to 1.46 for h <= 9000. This does not affect correctness.; fix: State that C1 is ineffective-in-practice, or trade the exponent 9/10 and the tau^6 moment for a smaller log power if a usable constant is ever needed.
- location: (3.9), choice of sigma; severity: minor; description: 'The sigma in Sigma+ with P_sigma largest' needs a deterministic tie-break, for example when T1 = 1 and all P_sigma = 1, so that D is a function of c. Any fixed rule works, and the case P = 1 (kappa = +-1, rho = 1) is consistent with (3.6)-(3.7).; fix: Add: 'ties broken by a fixed ordering of Sigma+'.
- location: [1] facts (O1)-(O5); severity: minor; description: The Euclidean property, units +-phi^n, decomposition of rational primes and the ideal count <= tau(n) are cited from textbooks, not proved. All are standard and correct as stated.; fix: Cite precise theorem numbers, for example from Hardy and Wright Chapter XV, or from any algebraic number theory text.
- location: Theorem 1, lower-bound clause; severity: minor; description: The bound 12(h/58 - 1) is correct but loose. Negative offsets T = -11t carry the mirrored relations, since Q(-T,-d) = Q(T,d), and T = 11t carries 24 relations, not 12, in every tested case. So at least 24(h/58 - 1) holds. Not an error.; fix: Optional: state 24(h/58 - 1), or leave it as is.
- location: (3.7) reconstruction; severity: minor; description: The proof bounds the fibre by 2, the number of roots rho. In every test the fibre was 1 (4736 abstract primitive configurations, 996 from relations at h = 9000, 3456 synthetic). This shows the bound has slack, not an error.; fix: None needed.

## Corrected statement

Theorem 1 as stated holds. A slightly stronger version also holds: sum over odd 0<|T|<h of R_T(h) is between 24(h/58 - 1) and C1 h for an absolute (ineffective-size) C1, and each primitive configuration is determined by its tuple D up to at most two choices; in every tested case it was determined uniquely.

## Independent derivation

I derived each step before comparing it with the author's text.

[2] Dictionary. Put X = 10d + T. Then X^2 = 100d^2 + 20Td + T^2 and 5L^2 = 100d^2 + 20Td + 5T^2, so X^2 - 5L^2 = -4T^2. T is odd, so X is odd, and L^2 = Q is congruent to T^2 mod 4, so L is odd. Hence beta = (X - L)/2 + L phi = (X + L sqrt5)/2 lies in O. N(beta) = (X^2 - 5L^2)/4 = -T^2 and Tr(beta) = X. Both |beta| and |beta'| are at most (|X| + sqrt5 L)/2 < sqrt5 L < sqrt5 h. Given T, the trace recovers d.

(3.2) Injection and (C3). From sum e_j d_j = 0 we get sum e_j(10 d_j + T) = e0 T, which is (C2). Suppose e_j(10 d_j + T) = e0 T. Then 10 d_j = T(e0 e_j - 1), and e0 e_j = 1 + e_j(sum of the other two signs) is 3, 1 or -1.
- e0 e_j = 1 gives d_j = 0, which is not in S_T.
- e0 e_j = 3 gives d_j = T/5. Then T = 5u and Q = 65u^2, which is not a square.
- e0 e_j = -1 forces the other two signs to equal -e_j, so e0 = -e_j = +-1 and d_j = -T/5, the minority index: exactly a reflection relation.
So (C3) holds if and only if the relation is not a reflection relation. The map is injective because T is part of the configuration and the traces return the d_j. Remark: Q(T, -T/5 - d) = Q(T, d) and Q(T, -T/5) = T^2, so reflection relations are plentiful whenever 5 | T, about 36000 at h = 9000. Excluding them is necessary.

(3.3) Content. If G divides every beta_j in O, then G^2 = N(G) divides N(beta_j) = -T^2, so G | T. Conditions (C1)-(C3) are homogeneous under division by G, T/G stays odd, and c/G is primitive by the maximality of G. Sizes scale by 1/G, so c with |T| < h and ||c|| < sqrt5 h lands in N(h/G).

(3.4) Local structure, for c primitive.
- Inert p dividing T: the prime element p divides beta beta' = -T^2, hence beta or beta', hence beta (p' = p), for every j. That contradicts primitivity. This works for any p | T, not only exact divisors.
- p = 5: N(a + b phi) is congruent to (a + 3b)^2 mod 5, so a = 2b mod 5. Since 2 + phi = sqrt5 phi, beta = sqrt5 gamma with N(gamma) = T^2/5, which is still divisible by 5. Repeating gives sqrt5 | gamma, so 5 | beta_j for every j, again a contradiction. Hence 5 does not divide T for primitive c.
- Split p with p || T: v_P(beta) + v_P'(beta) = v_P(T^2) = 2 (P unramified, since p != 5), so sigma(P') = -sigma(P).
- At most one zero coordinate in sigma(P). Three zeros put pO in every beta_j. Exactly two zeros: pO divides beta_j for j != j0, so Tr(beta_j) is in pZ, and (C2) puts e_j0 Tr(beta_j0) in pZ, inside P. But v_P(beta_j0) = 2 and v_P(beta_j0') = 0, so Tr(beta_j0), which is congruent to beta_j0' mod P, is not in P. Contradiction.

(3.5) Types and kappa. |Sigma| = 8 + 12 = 20, and since sigma != 0 exactly one of sigma, -sigma lies in Sigma+.
- (kappa) is the product of distinct degree-one primes P_p, never containing both P_p and P_p', so |N(kappa)| = P. A unit change multiplies |kappa/kappa'| by phi^(2n), so the normalization 1 <= |kappa/kappa'| < phi^2 fixes kappa up to sign. Then |kappa|^2 >= P and |kappa'|^2 > P/phi^2.
- No rational prime divides kappa: an inert q has norm q^2, split q would need Q Q' to divide (kappa), and 5 does not divide T.
- sigma_j = 1 means v_P_p(beta_j) = 2 for every p of the type, so kappa^2 | beta_j. sigma_j = -1 gives kappa'^2 | beta_j. sigma_j = 0 gives p | beta_j for every p of the type, so P | beta_j.
- In each case N(nu_j) = -T^2/P^2 = -m^2 and |nu_j|, |nu_j'| <= phi^2 ||c||/P.

(3.6) Elimination. Tr(beta_j) equals Tr(kappa^2 nu_j), Tr(kappa'^2 nu_j) = Tr(kappa^2 nu_j') or P Tr(nu_j) in the three cases. Hence Tr(kappa^2 Omega) = e0 T - P sum_{sigma_j=0} e_j Tr(nu_j) = c0 P, using T = sT P m. Since P = eta kappa kappa', dividing by kappa'^2 gives Omega rho^2 - eta c0 rho + Omega' = 0.
- c0 != 0: with no zero coordinate, c0 P = e0 T, and e0 is odd. With one zero j0, c0 P = e0 T - e_j0 Tr(beta_j0), which is nonzero by (C3).
- Omega != 0: otherwise the identity gives c0 eta kappa kappa' = 0.

(3.7) Reconstruction. D determines Omega and c0, and Omega != 0, so rho takes at most 2 values.
- If kappa1/kappa1' = kappa2/kappa2', the ratio kappa1/kappa2 is fixed by conjugation, hence rational, say a/b in lowest terms with b kappa1 = a kappa2. Bezout (r a + s b = 1) gives b | kappa2, so b = +-1, since kappa2 has no rational prime factor. Likewise a = +-1.
- Explicitly, kappa is the primitive part of 1 + rho, because (1 + rho)/(1 + rho)' = rho, and Tr(kappa) != 0 since sqrt5 does not divide kappa.
- Then P = |N(kappa)|, T = sT P m, and beta_j = kappa^2 nu_j, kappa'^2 nu_j or P nu_j. The sign of kappa does not matter.
So the fibre has at most 2 elements.

(3.8)-(3.10) Counts.
- The number of ideals of norm m^2 is at most tau(m^2) <= tau(m)^2. Generators are +-phi^n nu0, and |nu| |nu'| = m^2 >= 1 confines |nu| to [1/Y, Y], which gives the count 2 tau(m^2)(1 + 2 log Y / log phi).
- With Y = phi^2 sqrt5 x, 1 + 4.156(1.767 + log x) <= 9(1 + log x).
- tau(n)^k <= sum_{ab=n} tau(a)^(k-1) tau(b)^(k-1) follows from tau(ab) <= tau(a) tau(b), and induction gives sum tau^k/n <= (1 + log z)^(2^k).
- The squarefull Euler product converges, with p-term about p^(-9/5).
- By pigeonhole over the 10 types, P >= T1^(1/10), so m1 <= (x/q)^(9/10).
- Total: N(x) <= 640 * 18^3 * Cq x^(9/10)(1 + log x)^67, and sum over G <= h of N(h/G) = O(h).

Lower bound. 20*4 + 88 + 121 = 289 = 17^2, 180 - 132 + 121 = 169 = 13^2, 500 + 220 + 121 = 841 = 29^2. The relation is 2t - (-3t) - 5t = 0, its minority element 2t is not -11t/5, and 6 orders times 2 signs give 12 relations per t. The number of odd t below h/29 is at least h/58 - 1/2.

## Checks

Script folder: scripts_audit_relations_algebra/. Every script runs with py in under 60 seconds and uses exact integer arithmetic in Z[phi] (a + b phi as (a, b)).

1. audit1.py H. It enumerates S_T for all odd |T| < H through Pythagorean triples (4d)^2 + (T + 2d)^2 = L^2 and lists every relation. For each relation it:
   - asserts that (C3) fails exactly when the relation is a reflection relation;
   - asserts that the map to configurations is injective;
   - divides out the content and asserts G | T;
   - runs the local analysis: no inert prime, 5 does not divide T, at most one zero in sigma(P), the kappa generator by Gauss reduction of the ideal lattice, exact divisions, N(nu_j) = -m^2, c0 != 0, Omega != 0, and the identity Omega kappa^2 + Omega' kappa'^2 = c0 eta kappa kappa' exactly;
   - reconstructs from D alone (solves the quadratic in Q(sqrt5), takes kappa as the primitive part of 1 + rho, rebuilds T and the beta_j) and asserts the original configuration is among the candidates.
   Results:
   | h | sum R_T | R/h | reflection relations | primitive configurations | max fibre |
   |---|---|---|---|---|---|
   | 500 | 696 | 1.392 | 1128 | 276 | 1 |
   | 1000 | 1272 | 1.272 | 2664 | 372 | 1 |
   | 2000 | 2880 | 1.440 | 6072 | 612 | 1 |
   | 4000 | 5808 | 1.452 | 14160 | 804 | 1 |
   | 9000 | 13128 | 1.459 | 36096 | 996 | 1 |
   The h = 1000 and h = 4000 values match the author's 1.272 and 1.452. The lower bound 12(h/58 - 1) holds at every h; for example, T = 11t alone gives 4176 relations against a bound of 1850 at h = 9000.

2. audit2.py 400. Brute force over all abstract configurations (C1)-(C3), both signs of T, |T| <= 400, ||c|| <= sqrt5 x. It found 25504 configurations, 4736 primitive (exactly 4 times the author's T > 0 counts of 6376 and 1184) and none with 5 | T. All 4736 D values are distinct and every reconstruction succeeds.

3. audit3.py and audit4.py (branch coverage). Up to h = 9000 and x = 400, composite P and squarefull T2 > 1 never occur. Zero coordinates with P > 1 occur 192 and 576 times.

4. audit5.py 6 (synthetic stress test). It builds every configuration with ||c|| <= 6|T| for T in {209, 6061, 9889, 24149, 2299, 3971, 187891, 43681, 25289, 505571, -6061, 255529, 14641}, which includes products of 3 to 4 split primes and squarefull parts. It found 29104 configurations and 3456 primitive, of which 864 have composite P, 1440 have a zero coordinate with P > 1, and T = 3971 = 11 * 19^2 exercises T2 > 1. All checks pass, every reconstruction succeeds, and the maximum fibre is 1.

No counterexample was found to any step.

# Audit of the counting and of the consequences

## Verdict

correct_with_fixable_gaps

## Summary

I re-derived every step in scope by hand. That covers the counting in (3.8) to (3.10) of Theorem 1, Lemma 5.1, Theorem 2 and its use of Alon, Krivelevich and Sudakov (AKS), the final sum to O(h log h / log log h), Proposition 3, Proposition 4 and Corollary 4.1. I found no mathematical error. The estimates hold as written:
- P >= T1^(1/10) holds by pigeonhole over the 10 types.
- m1 <= T1^(9/10) <= (x/q)^(9/10) holds.
- Every |nu_j| and |nu_j'| is at most phi^2 ||c|| / P.
- Primes dividing T to a higher power go into the squarefull part q and cost nothing extra. The sum over q converges.
- No configuration is left out. Any double counting only makes the upper bound larger.

I also read the AKS paper itself (Alon's PDF). Its Theorem 1.1 fits the use in Theorem 2, with f between 2 and d.

The gaps are in how things are stated and cited:
1. The write-up quotes AKS Theorem 1.1 incorrectly in two places. It adds a hypothesis "d >= d0" and the open range "f > 1". The original says "maximum degree d" and gives no explicit range for f. The theorem cannot hold for f much larger than d^2: a triangle-free graph can have chromatic number about d / log d. The use here keeps 2 < f <= d, so nothing breaks.
2. Proposition 1 of the 12 November note is stated only for arc classes. Applying it to any independent set of G_T needs one added sentence: the same proof works.

Running my own script reproduced the counts in the write-up: sum R_T / h = 1.272, 1.452, 1.469 at h = 1000, 4000, 16000. The numbers of primitive relations are 228, 420 and 708, which grow sublinearly as Theorem 1 predicts.

## Issues

- location: Theorem 2 proof [5], statement of the cited AKS Theorem 1.1; external_results; severity: minor; description: The write-up misquotes AKS Theorem 1.1. JCTB 77 (1999) 73-82 says: 'There exists an absolute positive constant c such that the following holds. Let G be a graph on n vertices with maximum degree d in which the neighborhood N(v) of any vertex spans at most d^2/f edges. Then chi(G) <= c d / log f.' Three differences from the quote:
  - The original has no threshold d0. The proof gets rid of small f and d by using chi <= d+1.
  - The original gives no explicit range for f. It needs f <= poly(d): the proof turns the case f > d^(1/7) into Theorem 2.1, which gives O(d / log d), and for f much larger than d^2 the claim fails on triangle-free graphs. The write-up's open range 'f > 1' is too broad.
  - The original says 'maximum degree d', not 'at most d'.
  The use here has f = (4/7) k^(1/2) in (2, d] with d = 2k, so it is safe.; fix: Quote the theorem with 1 < f <= d^2 (or note that only 2 < f <= d is used) and drop d0. To apply it when the maximum degree is below d, take the disjoint union with K_{d,d}. Its neighbourhoods span no edges, the maximum degree becomes exactly d, and the chromatic number of G is unchanged. The constants C0 and C2 stay valid: when d is small, chi <= k+1 already covers that case.
- location: Corollary to Theorem 2 (also the summary): appeal to Proposition 1 of research_archive/2026-11-12/arc_classes_monotone_partition.md; severity: minor; description: Proposition 1 there is stated for arc classes C_c under ||theta d|| >= 1/M, not for an arbitrary independent set of G_T. The extension is true, but by the proof, not by the statement:
  - Item 2 (P-free) is exactly independence in G_T. Slots i and i' in one diagonal conflict exactly when |i-i'| is in {|d| : d in S_T}, and only differences below n_T occur.
  - Items 1 and 3 (slope 1, no right angle) do not use the arc structure.
  The AKS colouring classes are not arc classes, so the citation needs this remark.; fix: Add one sentence: 'Items 1 and 3 of Proposition 1 hold for any subset of a diagonal, and item 2 holds for every independent set of G_T, by the same proof.'
- location: Corollary 4.1(2), the arc partition; severity: minor; description: Proposition 1 of the note assumes ||theta d|| >= 1/M for all d in S_T. Corollary 4.1(2) gives this only for delta in D_T. That is enough, because two slots of one diagonal differ by less than n_T, but the write-up does not say so.; fix: State that only distances below n_T matter inside the diagonal, so the hypothesis on D_T suffices.
- location: Proposition 4 proof [7], constant 10.1; severity: minor; description: The bound is valid but loose. A direct estimate gives |pi'||zeta_d| = |b_d|/|pi'| < sqrt5 phi h / sqrt p and |pi||zeta_d'| = |b_d'|/|pi| <= sqrt5 h / sqrt p. The error is then below c* sqrt5 phi^2 h / sqrt p, about 6.2 h / sqrt p, not 10.03. The weaker constant is correct, so nothing breaks. The sharper one would lower the threshold 19 h^(2/3) in Corollary 4.1 to about 13.6 h^(2/3) (taking eta <= 1/8).; fix: Optional: replace 10.1 with 6.3 and recompute the threshold in Corollary 4.1.

## Corrected statement

Theorem 1, Lemma 5.1, Theorem 2 (sum_T chi(G_T) <= C2 h log h / log log h for h >= 16), Proposition 3, Proposition 4 and Corollary 4.1 hold as stated. Two changes are needed:
- Quote AKS Theorem 1.1 as: maximum degree d (pad with K_{d,d} when it is smaller), every neighbourhood spans at most d^2/f edges, 1 < f <= d^2, and then chi <= c d / log f. Only 2 < f <= d is used.
- Justify the corollary on classes by the proof of Proposition 1 of the 12 November note, not by its statement. Any independent set of G_T in one diagonal is monotone of slope 1, P-free and has no right angle.
Optionally, the constant 10.1 in Proposition 4 can be lowered to 6.3.

## Independent derivation

These are my own derivations of the steps in scope.

[0] Sum of |S_T|. Put x = 4d and y = T + 2d. Then x^2 + y^2 = 20d^2 + 4Td + T^2 = L^2, and the map (T,d) -> (x,y) is injective. Write (|x|, |y|, L) = g(2uv, u^2 - v^2, u^2 + v^2). With 4 sign choices, the count is at most 4 sum over u from 2 to sqrt h of (u-1)h/u^2, which is at most 2h log h. Since k_T <= |S_T|, sum k_T <= 2h log h.

(3.8)(i) Count of nu. The number of ideals of norm m^2 is at most tau(m^2): a split prime contributes a+1, an inert or ramified prime at most 1. A generator is ±phi^n nu0. From |nu||nu'| = m^2 with |nu|, |nu'| <= Y we get |nu| in [m^2/Y, Y]. That interval allows at most 1 + 2 log Y / log phi values of n, and 2 signs. Correct.

(3.8)(ii) Sum of tau^6.
- tau(n)^k = sum over ab = n of tau(n)^(k-1), and tau(n) <= tau(a) tau(b), so tau(n)^k <= sum over ab = n of tau(a)^(k-1) tau(b)^(k-1).
- Hence sum over n <= z of tau(n)^k / n <= (sum over a <= z of tau(a)^(k-1) / a)^2.
- The base case is sum 1/a <= 1 + log z. Induction gives (1 + log z)^(2^k), which is (1 + log z)^64 for k = 6.
- Since n <= z, sum tau^k <= z times sum tau^k / n.
Correct.

(3.8)(iii) Finiteness of Cq. Cq is the Euler product of (1 + sum over a >= 2 of (a+1)^6 p^(-9a/10)). Each factor is 1 + O(p^(-9/5)), and sum p^(-9/5) converges. Finite.

(3.4) and (3.5) Local structure, checked as input to the count.
- An inert p dividing T, or 5 dividing T at any power, forces the configuration to be imprimitive. For p = 5: N(a + b phi) ≡ (a + 3b)^2 (mod 5) and 2 + phi = sqrt5 phi. So a primitive configuration has 5 ∤ T.
- For p dividing T exactly once, v_P + v_P' = 2 and sigma(P') = -sigma(P).
- sigma has at most one zero. If two coordinates were zero, Tr(beta_j0) ≡ beta_j0' would not lie in P, but (C2) puts it in pZ.
- kappa is free of rational primes.
- nu_j lies in O and has norm -m^2. The bounds |kappa|^2 >= P and |kappa'|^2 > P/phi^2 give |nu_j|, |nu_j'| <= phi^2 ||c|| / P.

(3.6) and (3.7) Elimination and reconstruction.
- Tr(kappa^2 Omega) = c0 P with P = eta kappa kappa', so Omega rho^2 - eta c0 rho + Omega' = 0.
- c0 is not 0: e0 is odd, or (C3) applies. So Omega is not 0.
- rho determines kappa up to sign. kappa_1 / kappa_2 is rational, and a gcd argument shows its numerator and denominator are ±1.
- D determines T = sT P m and every beta_j. So N(x) <= 2 #D.

(3.9) The count.
- The 10 types multiply to T1, so the largest has P >= T1^(1/10).
- m = q m1 with q = T2 squarefull, m1 = T1/P <= T1^(9/10), and T1 <= x/q. So m1 <= (x/q)^(9/10).
- Box: Y = phi^2 sqrt5 x. Then 1 + 2 log Y / log phi = 8.34 + 4.16 log x <= 9(1 + log x). So each nu_j has at most 18 tau(m)^2 (1 + log x) values, using tau(m^2) <= tau(m)^2.
- tau(m) = tau(q) tau(m1) because the two are coprime.
- Total: #D <= 320 · 18^3 (1 + log x)^3 times sum over q of tau(q)^6 times sum over m1 <= (x/q)^(9/10) of tau(m1)^6. That is at most 320 · 18^3 · Cq · x^(9/10) (1 + log x)^67.
- Nothing is missing: every primitive configuration gives a D in the counted set. Overcounting (q, m1) only loosens the bound. Higher prime powers sit inside q, and 5 cannot divide T.

(3.10) Sum over content.
- The relation map (d, e) -> configuration, with T recorded, is injective over all T. The trace recovers d, and |beta_d|, |beta_d'| < sqrt5 L < sqrt5 h.
- (C3) fails only for reflection relations: d_j = 0, or d_j = T/5 with 13T^2/5 a square (impossible), or the reflection case itself.
- Content G: G^2 divides T^2, so G divides T. c/G is primitive with |T/G| < h/G.
- Sum over G <= h of N(h/G) <= C4 C5 h^(19/20) times sum G^(-19/20) <= 20 C4 C5 h.

Lemma 5.1.
- The neighbours of i are i + x with x in ±D_T, so the degree is at most 2k_T.
- An inner pair x > y with z = x - y in D_T maps injectively to a relation (e1, e2, e3) = (x/d1, -y/d2, -z/d3).
- A reflection relation needs |d_j| = |T|/5 at the minority index. At most 2(2k_T - 1) pairs contain ±|T|/5, and at most 2k_T pairs have difference |T|/5. That is at most 6k_T - 2 pairs.
- Everything else counts toward R_T.

Theorem 2.
- d = 2k and f = (4/7) sqrt k, which exceeds 2 for k >= 13. Then d^2/f = 7k^(3/2), which is at least 6k + k^(3/2).
- log f >= (1/4) log k needs log k >= 4 log(7/4) = 2.24, which holds for k >= 13.
- Hence chi <= 8ck / log k. Cases with R_T > k^(3/2) give k + 1 <= 2R_T, total at most 2C1 h. Greedy colouring gives chi <= k + 1.
- Split at K0 = sqrt(log h). Diagonals with k_T <= K0 cost at most h sqrt(log h) <= h log h / log log h, since sqrt(u) >= log u for all u > 0. The others cost at most 2 sum k_T / log log h <= 4h log h / log log h.
- Small k_T costs at most 13h.

Proposition 3.
- p^3 > 5r^2h^2 and h >= 5 give p > 5 and p^2 > (5h^2)^(2/3) > h > |T|, so p divides T exactly once.
- p divides beta_d exactly when p divides d, using 5L^2 = X^2 + 4T^2.
- E = sum over p ∤ d of c_d b_d lies in P'^2. Modulo P it equals sum over p ∤ d of c_d (10d + T), and that sum is in pZ. So E lies in PP'^2, and p^3 divides N(E).
- |N(E)| < 5r^2h^2 < p^3, so E = 0 and the trace vanishes. 10 sum c_d d = -Ts with T odd gives the parity claims.
- For the distance version, r <= mk. Flipping signs keeps parity, and with support prime to p we get s = 0.

Proposition 4.
- c* = (2 + sqrt5)/4 comes from rounding b to (s1 - s2)/sqrt5 and a to (s1 + s2 - b)/2.
- An n with n pi' ≡ mu (mod P) exists. Then (n pi' - mu) pi' lies in pO.
- theta d ≡ (n - z0) X_d / p + t z0 (mod 1), using 10d = X_d - pt.
- The error terms are c* |b_d|/|pi'| + c* |b_d'|/|pi|, which is less than 6.2 h / sqrt p and so less than 10.1 h / sqrt p.
- Part (ii) holds because theta p = 10n - 10 z0. In the inert case no d is prime to p.

Corollary 4.1.
- 19^1.5 = 82.8 gives eta <= 0.122 < 1/8.
- With z0 = 1/2, t odd and N = 10n - 5, we get ||N d / p|| >= 3/8 > 1/3, so the three arcs colour properly. Taking the product with the greedy colouring of the multiples of p gives 3(k' + 1).
- (2) The union bound uses theta1 uniform on [0, 10). theta1 δ' and t theta1 / 10 are both uniform mod 1, and the total probability is (2k' + 2)/M + 2 eta < 1. Then z0 = -theta1/10.

Lower bound in Theorem 1. 289 = 17^2, 169 = 13^2 and 841 = 29^2 check out. The minority element 2t is not -11t/5.

Computation (sanity only). My script reproduced R/h = 1.272, 1.452, 1.469 at h = 1000, 4000, 16000, with 228, 420 and 708 primitive relations.

## Checks

Files: my script is scripts_audit_relations_counting/rel_count.py. The AKS paper copy is scripts_audit_relations_counting/pdf/aks.pdf.

1. The script builds S_T independently from Pythagorean triples and counts non-reflection relations and primitive relations by brute force. It ran in under 60 seconds. Results: h = 1000 gives R = 1272 and 228 primitive; h = 4000 gives R = 5808 and 420 primitive; h = 16000 gives R = 23508 and 708 primitive. These match the earlier R/h figures (1.272, 1.452, 1.469), and the primitive counts grow sublinearly.

2. I read the AKS text itself (web.math.princeton.edu/~nalon/PDFS/logf4.pdf, extracted with pdftotext): Theorem 1.1, Proposition 1.2 (2 <= f <= 2d^2) and the opening of the proof of Theorem 1.1 (the case f > d^(1/7) goes to Theorem 2.1 with epsilon = 1/28).

3. I read Proposition 1 and its proof in research_archive/2026-11-12/arc_classes_monotone_partition.md, read-only.

Everything else was checked by hand, line by line. No repository was modified.

