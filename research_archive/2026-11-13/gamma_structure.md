# Structure of the limit graph Gamma

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

chi(Gamma) remains open. Not audited yet.

# Result

## Status

partial

## Summary

chi(Gamma) is still undecided: there is no proof of infinity and no finite colouring. This round proves four structural facts. (1) The "hub" symmetry r -> -1/5 - r. (2) R_+ ∩ (-R_+) is empty, by a complete 2-descent, so Gamma has a canonical orientation. (3) Local genus counts: a vertex's neighbourhood is a conic, an edge's common neighbourhood lies on genus-1 curves unless the edge is a hub edge, and a triangle has finitely many common neighbours unless it contains a hub pair (Faltings). (4) For multi-prime S-unit products, the finite-adelic phases separate exactly, while the archimedean phase cannot be kept small (product-formula obstruction). Fact (4) places the remaining difficulty of the spectral and Bohr routes entirely at the real place.

## Statements

Notation as in limit_graph_gamma.md and gamma_linearization.md. R_+ = {r in Q* : 20r^2+4r+1 in Q^2}; r(beta) = L(beta-1), L(a+b phi) = (a+3b)/10; the vertex set is Z_(2), and x ~ y iff x - y lies in ±R_+ ∩ Z_(2). eps = -phi^2. For a split prime l, omega_l = pi/pi'. Every statement below is proved unless it is labelled COMPUTED.

THEOREM A (hub symmetry). sigma(r) = -1/5 - r is an involution of R_+ ∪ {0} that swaps 0 and -1/5 and preserves Z_(2). In torus terms, sigma(r(beta)) = r(-beta). Consequences:
 (A1) -1/5 is in R_+, and R_+ \ {-1/5} ⊆ N(0) ∩ N(-1/5). By translation, every edge {x, y} with y - x in R_+ lies in the triangle {x, y, x - 1/5}.
 (A2) chi(Gamma) >= 2 + chi(Gamma[R_+ ∩ Z_(2) \ {-1/5}]). Also, K_{n+2} ⊆ Gamma whenever K_n ⊆ Gamma[R_+ \ {-1/5}]. The known K5 {0,35,209,260,434}/1045 has exactly this shape: it is the hub pair {1/5, 0} plus a triangle inside 1/5 + R_+.
 (A3) R_+ contains no pair {y, y ± 1/5}, so the hub structure does not recur inside Gamma[R_+]. This uses Theorem B.

THEOREM B (orientation). R_+ ∩ (-R_+) is empty. Equivalently, the two conditions 20r^2+4r+1 in Q^2 and 20r^2-4r+1 in Q^2 hold together only at r = 0. So Gamma is the underlying graph of the oriented Cayley digraph x -> y iff y - x in R_+, and every edge has exactly one direction. With this orientation, A1 reads N^+(x) \ {x - 1/5} = N^-(x - 1/5) \ {x}.

THEOREM C (local genus counts).
 (C1) N(x) = x ± R_+ is the set of rational points of two conics.
 (C2) Let a be in Q \ {0, ±1/5}. Then N(0) ∩ N(a) is contained in the r-projection of the rational points of four curves of genus 1: s^2 = 20y^2 ± 4y + 1 and t^2 = 20(y-a)^2 ± 4(y-a) + 1. For a = 1/5, N(0) ∩ N(1/5) = (-R_+) ∪ (R_+ ∩ (1/5 - R_+)), so it contains a whole conic. The genus drops exactly at the hub edges.
 (C3) Let {0, a, b} be a triangle in which no two vertices differ by ±1/5. Then its common neighbourhood is finite: for each of the 8 sign choices it lies on a curve of genus 5, and Faltings' theorem applies. In particular, every triangle of {0} ∪ (R_+ \ {-1/5}) has only finitely many common neighbours.

LEMMA F (local separation for multi-prime products). Let l_1, ..., l_w be distinct split primes. For each j, let beta_j be in ±<eps, omega_{l_j}> with pole order e_j at l_j, and suppose beta_j ≡ 1 mod 10·prod_{i≠j} l_i^{e_i} in O[1/l_j] (mutual congruences). For F ⊆ [w], put beta_F = prod_{j in F} beta_j. Then:
 - r(beta_F) - sum_{j in F} r(beta_j) is an integer;
 - for each j in F, r(beta_F) - r(beta_j) is l_j-integral;
 - r(beta_F) is 2- and 5-integral.
Hence, for every character chi of Z_(2), written as chi(x) = e(theta x - sum_l {theta_l x}_l) with theta real and theta_l in Z_l,
  chi(r(beta_F)) = e( theta·r(beta_F) - sum_{j in F} {theta_{l_j} r(beta_j)}_{l_j} ).
The finite-adelic phases factor exactly over the primes. Only the real term theta·r(beta_F) couples the factors.

LEMMA O (archimedean obstruction). Under the hypotheses of Lemma F, take w = 2, with beta_1 and beta_2 not in ±<eps>. Then the integer kappa = r(beta_1 beta_2) - r(beta_1) - r(beta_2) is nonzero. Hence max(|r(beta_1)|, |r(beta_2)|, |r(beta_1 beta_2)|) >= 1/3. Moreover |N(beta_j - 1)| >= (10·prod_{i≠j} l_i^{e_i})^2 / l_j^{e_j}. So in any mutually congruent family, at least one factor is very far from 1 at the real place. Lemma F's exact local separation therefore cannot be paired with archimedean smallness.

COMPUTED (sanity checks, not proofs).
 - chi(Cay([0,400), D_5)) > 4 (two solvers), so chi_inf(5) >= 5. [0,3000) with D_5 is 5-colourable. With chi_inf(55) >= 6 and chi_inf(1045) >= 7 from the earlier note, the data fit the pattern chi_inf >= 5 + (number of split primes) for w = 0, 1, 2.
 - Link of 0 at height (|p|,|q| <= 30): 744 vertices and 1020 edges, of which 742 meet the two hubs ±1/5. The link minus the hubs has 278 edges on 742 vertices.
 - Lemma F checked exactly for (l_1, l_2) = (29, 59), with beta_1 = eps^536·omega_29 and beta_2 = eps^117·omega_59.

## Proofs

[A] For r ≠ 0, put q(r) = 20r^2+4r+1 = 20(r+1/10)^2 + 4/5. Then q(-1/5-r) = q(r), so sigma preserves the set {r : q(r) in Q^2} = R_+ ∪ {0}. sigma(0) = -1/5 and sigma(-1/5) = 0, and q(-1/5) = 1. Since -1/5 lies in Z_(2), sigma preserves Z_(2).
Torus form: r(-beta) = L(-beta-1) = -L(beta-1) - 2L(1) = -r(beta) - 1/5. The mod-2 condition (beta ≡ 1 or phi mod 2) is unchanged by beta -> -beta.
(A1) Let x be in R_+ \ {-1/5}. Then x - 0 is in R_+, and x - (-1/5) = -(sigma(x)) is in -R_+, so x is adjacent to both 0 and -1/5. For an edge with y - x = r in R_+ \ {-1/5}: (x - 1/5) - y = sigma(r) is in R_+, so y ~ x - 1/5. When r = -1/5, the triangle degenerates to the edge itself.
(A2) 0 and -1/5 are adjacent and both are adjacent to all of R_+ \ {-1/5}. No colour of that set can equal theirs, so chi >= 2 + chi(Gamma[R_+ \ {-1/5}]), and cliques extend by 2.
K5 check: 1/5 = 209/1045, and 0 - 1/5 = -1/5 is in R_+. The differences 35-209 = -174, 260-209 = 51 and 434-209 = 225 have Q(1045,d) square (L-values 985, 1165, 1745, as listed in limit_graph_gamma.md T3a). So the other three vertices lie in 1/5 + R_+.
(A3) Suppose y and y - 1/5 are both in R_+ and y - 1/5 ≠ -1/5. Then sigma(y - 1/5) = -y is in R_+, which contradicts Theorem B. The case y - 1/5 = -1/5 gives y = 0, which is not in R_+. The pair {y, y + 1/5} is handled the same way, using sigma(y) = -(y + 1/5).

[B] Suppose r ≠ 0 satisfies s^2 = 20r^2+4r+1 and t^2 = 20r^2-4r+1. Then (st)^2 = 400r^4 + 24r^2 + 1. So (r, st) is a rational point of C0: y^2 = 400x^4 + 24x^2 + 1.
Put w = y - 20x^2, X = -10w and Y = 5x(40w - 24). This gives a birational map C0 -> E: Y^2 = (X-10)(X+10)(X+6). (sympy: Y^2 - (X-10)(X+10)(X+6) reduces to 0 modulo the quartic.) The inverse is w = -X/10, x = Y/(5(40w-24)), y = w + 20x^2.
Torsion of E. The 2-torsion is full. E has good reduction at 3, 7 and 11, with #E(F_3) = 4, #E(F_7) = 12 and #E(F_11) = 8. Reduction is injective on prime-to-p torsion, so the torsion group has order 4: E(Q)_tors = (Z/2)^2.
Rank 0 by complete 2-descent. The descent map is P -> (X-10, X+10) in (Q*/Q*^2)^2, with values in <-1,2,5>^2. The torsion image is H = {(1,1), (5,5), (-5,5), (-1,1)}. On E(R), X+10 >= 0, so d2 > 0. Modulo H, the coset representatives are d1 in {1,2} and d2 in {1,2,5,10}. The system is X-10 = d1 u^2, X+10 = d2 v^2, X+6 = d1 d2 w^2, which gives d1 u^2 - d1 d2 w^2 = -16 and d2(v^2 - d1 w^2) = 4. Each of the 7 nontrivial representatives fails locally:
 (1,2): u^2 = 2w^2 - 16 forces v_2(w) = 2, and then v^2 = w^2 + 2 has odd valuation.
 (1,5) and (1,10): u^2 - 5w^2 = -16 (resp. u^2 - 10w^2 = -16) forces w to be in Z_5, and then v^2 = w^2 + 4/5 (resp. w^2 + 2/5) has v_5 = -1.
 (2,1): v^2 = 2u^2 + 20 has no 2-adic solution; check v_2(u) < 0, = 0 and > 0 separately.
 (2,2): v^2 = 2(w^2+1) forces w to be a 2-adic unit, and then u^2 = 2(w^2-4) has odd valuation.
 (2,5) and (2,10): u^2 - 5w^2 = -8 (resp. u^2 - 10w^2 = -8) forces w to be in Z_5, and then v^2 = 2w^2 + 4/5 (resp. 2w^2 + 2/5) has v_5 = -1.
So E(Q)/2E(Q) = H, the rank is 0, and E(Q) has 4 points.
Under the inverse map: (10,0) -> (0,-1), (-10,0) -> (0,1), (-6,0) -> infinity_+, and O -> infinity_-. So C0(Q) = {(0,±1), infinity_±}, and the only affine rational x is 0. Hence r = 0, a contradiction.
Orientation form of A1: if x -> y, then (x - 1/5) - y = sigma(y - x) is in R_+, so y -> x - 1/5. The converse holds because sigma is an involution.

[C] (C1) holds by definition and by L1.
(C2) The quadratic 20(y-c)^2 + 4·eps·(y-c) + 1 has roots c + (-eps ± 2i)/10. Root sets for shifts c1, c2 and signs eps1, eps2 meet iff c1 - c2 = (eps1 - eps2)/10, which lies in {0, ±1/5}. For two quadratics with four distinct roots, {s^2 = q1, t^2 = q2} is a smooth curve of genus 1.
For a = 1/5: N(1/5) = (1/5 + R_+) ∪ (1/5 - R_+), and 1/5 + R_+ = -R_+ because R_+ + 1/5 = -sigma(R_+). Intersect with R_+ ∪ -R_+ and use Theorem B.
(C3) Three quadratics with six distinct roots (by the same root computation) give a (Z/2)^3-cover of P^1 branched at 6 points. Riemann–Hurwitz gives 2g - 2 = 8(-2) + 6·4 = 8, so g = 5. The cover is irreducible because the quadratics are independent modulo squares. Faltings' theorem then gives finitely many rational points. Inside {0} ∪ (R_+ \ {-1/5}) there are no ±1/5 differences: 1/5 is not in R_+ (q(1/5) = 13/5), and A3 covers the rest.

[F] Use r(xy) = r(x) + r(y) + L((x-1)(y-1)), and induct on |F| by splitting F = A ⊔ B, with x = beta_A and y = beta_B.
At l_j with j in A: x - 1 has pole order at most e_j, because the other factors are l_j-units ≡ 1 mod l_j^{e_j}. Also y ≡ 1 mod l_j^{e_j}. So (x-1)(y-1) is l_j-integral. The same holds at l_j with j in B.
At 2 and 5: both factors are ≡ 1 mod 10, so the product lies in 100·O.
At all other primes, everything is integral. So (x-1)(y-1) lies in 10·O, and L(10(a + b phi)) = a + 3b is in Z.
Next, r(beta_F) - r(beta_j) = r(beta_{F\j}) + L(...). Here beta_{F\j} - 1 lies in l_j^{e_j}·10·O_(l_j), so r(beta_{F\j}) is l_j-integral, and so is the L-term. Hence the l_j-adic fractional parts agree. Since beta_F ≡ 1 mod 10, r(beta_F) is 2- and 5-integral. The denominator of r(beta_F) involves only the l_j with j in F, which gives the character formula.

[O] kappa is an integer by F. If kappa = 0, then L(xy) = 0 with x = beta_1 - 1 and y = beta_2 - 1. By Hilbert 90, beta_i - 1 = c_i·sqrt5·delta_i with beta_i = delta_i/delta_i'. Then delta_1 delta_2 lies in Q·kappa_0, where kappa_0 = phi - 3 spans ker L. So beta_2 = (kappa_0/kappa_0')·beta_1^{-1} = -eps^{-1}·beta_1^{-1}, using (phi-2)(-2-phi) = 3-phi. Then beta_2 has the same split support as beta_1, which contradicts disjointness unless both are units.
So |kappa| >= 1, and |r(beta_1 beta_2)| + |r(beta_1)| + |r(beta_2)| >= 1.
Norm bound: beta_j - 1 lies in m_j·O[1/l_j], with m_j = 10·prod_{i≠j} l_i^{e_i}. It has valuation -e_j at one place above l_j and valuation 0 at the other. So N(beta_j - 1) is a nonzero element of m_j^2·l_j^{-e_j}·Z, and N(beta_j - 1) = -(b_j - 1)^2/b_j with b_j = sigma_1(beta_j). Multiplying the two bounds for j = 1, 2 gives prod_j (b_j - 1)^2/|b_j| >= 10^4·l_1^{e_1} l_2^{e_2}.

[Consequences for the routes (rigorous remarks).]
(i) Characters trivial on Z cannot give a Bohr colouring, because 1 is in R_+ (q(1) = 25). Real-only characters cannot either (Theorem 2 of gamma_linearization.md). So any finite Bohr colouring must mix an irrational real part with l-adic parts.
(ii) In the lazy product measure (F uniform, factors from Lemma F), nu^(chi) = E_F[ e(theta r(beta_F)) · prod_{j in F} zeta_j ], where zeta_j is the independent local phase at l_j. The local part is a product of independent factors. By Lemma O the real values r(beta_F) cannot all be small. So Proposition 4 for such measures is exactly an equidistribution statement for theta·r(beta_F) mod 1, jointly with the local phases.
(iii) Theorem C explains why the hub and self-similarity recursion stops. Any rational-map homomorphism from Gamma into the link of a vertex would have to send a conic (a neighbourhood) into genus-1 curves (a link neighbourhood), so it would be constant. Only hub edges escape this, and A3 shows they do not recur.

## External results used

- G. Faltings, Endlichkeitssätze für abelsche Varietäten über Zahlkörpern, Invent. Math. 73 (1983): a curve of genus at least 2 over Q has finitely many rational points. Used in C3.
- Standard: reduction mod a prime of good reduction is injective on prime-to-p torsion of an elliptic curve. Used in Theorem B.
- Standard complete 2-descent for elliptic curves with full rational 2-torsion. Used in Theorem B.
- Hilbert's Theorem 90 for Q(sqrt5)/Q: every norm-one element is delta/delta'. Used in Lemma O.
- Repository: limit_graph_gamma.md (L1, the K5, SAT values chi_inf(55) >= 6 and chi_inf(1045) >= 7) and gamma_linearization.md (Theorem 1 linearization, Theorem 2, Proposition 4). These are cited and not re-proved.

## Checks

All scripts are in the matching scripts_ folder of this directory (run with py, each under 60 s).
- link.py H=30: link of 0 has 744 vertices and 1020 edges; the hubs ±1/5 have degree 371 each.
- e0.py: no r = u/v ≠ 0 with |u| < 9000, v < 3000 and both quadratics square. This agrees with Theorem B.
- e0check.py: sympy confirms the birational map C0 -> E; point counts #E(F_p) are 4, 12, 8, 16, 16, 16 for p = 3, 7, 11, 13, 17, 19.
- v2_chi.py (copied from the archive): T = 5 with n = 400 is not 4-colourable (CaDiCaL and Glucose); [0,3000) is 5-colourable. Runs for T = 605 and for larger windows at T = 95 and 145 timed out and are not used.
- pairs.py and fact2.py: exact check of Lemma F for primes 29 and 59. The cross term is an integer with 272 digits; den r(beta_1) = 29, den r(beta_2) = 59, den r(beta_1 beta_2) = 1711; r12 - r1 has denominator 59 and r12 - r2 has denominator 29. The sizes |r| are about 10^223, 10^48 and 10^272, as Lemma O predicts.
- d3.py: D_30305 below 4000 has 21 elements, the smallest being 286.

## Gaps

- The main question is open: chi(Gamma) is neither proved infinite nor proved finite. No lower bound for max_T chi(G_T(h)) that tends to infinity is proved.
- The pattern chi_inf >= 5 + w (w = number of split primes) rests on three SAT data points (T = 5, 55, 1045), with no DRAT certificates. A larger case such as T = 30305 (w = 3) was out of reach within the 60 s limit, because its smallest distance is 286.
- Lemma F's hypotheses (mutually congruent families) are verified for the explicit pair (29, 59), and 3 good pairs were found among split primes below 140. For arbitrary w, existence needs omega_{l_j} to lie in ±<eps> modulo the other primes. That is an Artin-type condition I did not prove for infinitely many primes. Lemmas F and O are conditional statements about such families when they exist, and the obstruction conclusions do not need existence.
- C3 uses Faltings' theorem, which is cited and not re-proved. The genus-5 claim rests on the root-distinctness computation and Riemann–Hurwitz, done by hand once. The common-neighbourhood finiteness in C3 is not uniform; there is no bound on clique size.
- The 2-descent in Theorem B was done by hand once. The birational map was checked by sympy, and the torsion by point counts mod 3, 7 and 11. A second reader should redo the seven local obstructions.
- I tried a class of colourings c(x) = g(theta x + s([x])), with one real character and an arbitrary phase s on Z_(2)/Z. Refuting it reduces to cliques with tiny differences, plus the density of the 'gain sets' theta·N_c mod 1, which is a Pisot-type question. It is not settled. My first argument for it was wrong (it needs exact cliques) and is not claimed.
- No independent audit of anything in this round.

## Missing estimate

Via Proposition 4 and Lemma F, the remaining estimate is a joint real equidistribution statement. Find mutually congruent families beta_1, ..., beta_w (Lemma F) and probability weights on subsets F, together with the choice of factors, such that for every real theta and every choice of local phases zeta_j:
Re E_F[ e(theta·r(beta_F)) · prod_{j in F} zeta_j ] >= -delta_w, with delta_w -> 0.
By Lemma O, smallness cannot achieve this; it has to come from equidistribution of theta·r(beta_F) mod 1, with resonances at theta in Q(sqrt5)-type (Pisot) directions. A uniform ratio bound of this kind would give chi_f(Gamma) = infinity, and hence chi(Gamma) = infinity. In the other direction, a finite colouring must be non-Bohr in the mixed real-times-l-adic directions, or else defeat joint Bohr recurrence for at least two characters.

## Next steps

- Have Theorems A, B, C and Lemmas F, O audited. They are short. B (no r ≠ 0 with both 20r^2 ± 4r + 1 squares) is a full 2-descent on y^2 = (x-10)(x+10)(x+6).
- Attack the Pisot resonance directly: for theta in sqrt5·Q, compute theta·r(beta eps^{Pm}) mod 1. These sequences become periodic in m, which is the first case where the gain sets are not dense. Decide whether such theta give a non-trivial colouring of any infinite family of fibres.
- Test the w-pattern: get chi_inf(5·l) >= 6 for several other single split primes, and chi_inf(5 l1 l2) >= 7 for other pairs, using longer SAT runs outside this 60 s budget. Also try to find the +1-per-prime gadget in the SAT certificates; the K5 is hub plus triangle.
- Study the split analogue Gamma_0 = Cay(Q, W), W = {w : 1 + w^2 in Q^2}. Gamma is Cay(Q, (1/4)·1/(W - 1/2)), the fold of the sqrt5-distance graph between two parallel lines; Gamma_0 is the same with mu = 0. Its T-pieces have finite connection sets {d : d^2 + T^2 = square}. Deciding chi(Gamma_0) may show which way Gamma goes.
- For the spectral route, choose the factor measure so that log sigma_1(beta_F) is smoothed by a second rank-2 prime (as in Theorem 2), and prove the real equidistribution in the missing estimate for theta outside Q(sqrt5)-resonances. Handle the resonant theta separately through the periodicity above.

