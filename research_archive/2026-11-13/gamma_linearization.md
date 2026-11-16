# The limit graph Gamma: linearization and Bohr recurrence

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Not audited yet.

# Result

## Status

partial

## Summary

chi(Gamma) is still open. Proved: Gamma linearizes to the norm-one torus of Q(sqrt5), so its edge set is L(Lambda - 1) for a group Lambda of S-units, and every colouring built from real arcs and residues has a monochromatic edge. With Berend's theorem cited, this also holds for colourings built from any one adelic character.

## Statements

Notation. K = Q(sqrt5), phi = (1+sqrt5)/2, O = Z[phi], N and Tr are the norm and the trace. sigma1 and sigma2 are the real embeddings. eps = -phi^2 is a unit of norm 1. For a split prime l (l = +-1 mod 5), write l = pi pi' with N(pi) = l and put omega_l = pi/pi', which has norm 1. Define the Q-linear map L: K -> Q, L(x) = Tr(phi x)/10, so that L(a + b phi) = (a + 3b)/10. R_+ = { r in Q* : 20r^2 + 4r + 1 in Q^2 }. Gamma = Cay(Z_(2), (R_+ ∪ -R_+) ∩ Z_(2)), as in limit_graph_gamma.md.

THEOREM 1 (linearization) [proved].
(a) R_+ = { L(beta - 1) : beta in K, N(beta) = 1, beta not in {1, eps^{-1}} }. Each r comes from at most two beta.
(b) L(beta - 1) lies in Z_(2) iff beta = 1 or beta = phi mod 2 (beta is automatically a 2-adic unit).
(c) Let S be a finite set of split primes. The elements of R_+ ∩ Z_(2) whose denominators use only 5 and the primes of S are exactly the L(beta - 1) with beta in +-<eps, omega_l (l in S)>, beta = 1 or phi mod 2, and beta not in {1, eps^{-1}}. If beta = +-eps^n prod omega_l^{k_l}, then v_l(L(beta - 1)) = -|k_l| for every k_l != 0. Hence for odd T = 5^a prod l^{e_l}, the set D_T^inf is a finite union of lacunary orbits n -> |T L(+-eps^n omega^k - 1)|, indexed by the exponent vectors with |k_l| <= e_l. There are prod(2e_l + 1) of them, up to sign and mod-2 classes. This re-derives L3 and the 3^w count. Brute force agrees for T = 5, 55, 605, 6655 and |d| <= 4000.

THEOREM 2 (rational Bohr recurrence) [proved, elementary]. Let theta_1, ..., theta_k be real, M >= 1 odd and delta > 0, and let l be a split prime with l ∤ 10M. Then there are infinitely many r in R_+ such that:
- r lies in M Z[1/l] ⊂ M Z_(2);
- 0 < r < delta (either sign of r can be prescribed);
- hence ||theta_j r|| < delta max|theta_j| for every j.
COROLLARY 2.1 [proved]. Fix real theta_1..theta_k, odd M and s >= 1. Every colouring of Z_(2) that is constant on the cells { x = a mod M, floor(s{theta_j x}) = m_j for all j } has a monochromatic edge of Gamma. More generally, in a proper finite colouring no colour class contains a nonempty set { x in a + M Z_(2) : {theta_j x} in J_j for all j } with open arcs J_j. So lead (2), taken literally (arcs of theta x for several real theta, together with residues), cannot give chi(Gamma) < infinity. The same holds when the real and residue data are used only on one subgroup Z[1/(5l)]. Any finite Bohr-type colouring must therefore use, for every split prime l, a character whose l-adic component is irrational.
COROLLARY 2.2 [proved]. Fix real theta_j, odd M and s. In the diagonal language, give label i of diagonal T > 0 the colour (i T^{-1} mod M, floor(s{theta_j i/T})). For some T = 3^n 5 l^k and all large h, this rule leaves a monochromatic edge in G_T(h).

THEOREM 3 (one arbitrary character) [proved modulo Berend's theorem]. Let chi be any character of Z_(2), M >= 1 odd, l a split prime with l ∤ 10M, and delta > 0. Then there are infinitely many r in R_+ ∩ M Z[1/l] with ||chi(r)|| < delta.
COROLLARY 3.1. For any single character chi, any odd M and any s, every colouring constant on the cells { x = a mod M, floor(s{chi(x)}) = m } has a monochromatic edge.

PROPOSITION 4 (ergodic sufficient condition for chi(Gamma) = infinity) [proved, using the Furstenberg correspondence principle]. Suppose there are finitely supported symmetric probability measures nu_n on the connection set with liminf_n Re nu_n^(chi) >= 0 for every nontrivial character chi of Z_(2). Then chi(Gamma) = infinity. No uniformity in chi is needed. In the uniform case this is the infinite-group form of Lemma G.

SIDE CHECK (the earlier derivation). The algebra is correct as written:
- the perpendicularity equation;
- u = -Delta s + 8 t1 N/(10 t1 - T0) with N = Delta s - P Delta c;
- uniqueness of u (10 t1 - T0 is odd, so it is never 0);
- u is an integer iff m = |10 t1 - T0|/gcd(T0, t1) divides N (because gcd(10t1 - T0, 8t1) = gcd(T0, t1));
- R = P + Q - V sits in odd row 2(i0 + t1 + u + Delta s) + 1 and in the column of slot iQ + t1 of class c';
- when Delta s = 0, R is the black odd point of that label (a fully black rectangle);
- the fatal/harmless split follows from the axis owner lemma.
The expected-count formula rho^3 tau(T0) log h/320 is a heuristic, and I did not check it.

## Proofs

[1] PROOF OF THEOREM 1.
(a) Multiply 20r^2 + 4r + 1 = Y^2 by 5. This gives (10r + 1)^2 + 4 = 5Y^2, that is X^2 - 5Y^2 = -4 with X = 10r + 1. So alpha = (X + Y sqrt5)/2 has N(alpha) = -1 and Tr(alpha) = X. Conversely, for alpha in K with N(alpha) = -1, write alpha = (X + Y sqrt5)/2 with X, Y rational. Then r = (X - 1)/10 satisfies 20r^2 + 4r + 1 = ((10r+1)^2 + 4)/5 = Y^2. Since N(phi) = -1, alpha = phi beta with N(beta) = 1, and Tr(phi) = 1. So r = (Tr(phi beta) - Tr(phi))/10 = L(beta - 1).
r = 0 iff Tr(phi beta) = 1. Then phi beta is a root of x^2 - x - 1, so beta is in {1, phi'/phi = -phi^{-2} = eps^{-1}}. Since r determines Tr(phi beta) and N(phi beta) = -1, at most two beta give the same r.
(b) The prime 2 is inert in K. A norm-1 element has v_2(beta) = v_2(beta') and v_2(beta) + v_2(beta') = 0, so beta is in O_(2)^*. Put gamma = beta - 1. Then r is in Z_(2) iff Tr(phi gamma) is in 2 Z_(2), iff phi gamma mod 2 lies in the kernel of Tr: F_4 -> F_2, which is F_2. That means gamma = 0 or phi^{-1} = phi^2 mod 2, so beta = 1 or 1 + phi^2 = phi mod 2.
(c) Valuations. At an inert prime and at sqrt5, the valuation is Galois-invariant, so a norm-1 beta has valuation 0 there. At a split prime q = Q Q', v_Q(beta) = -v_{Q'}(beta). Suppose v_Q(beta) = -e < 0. Then v_Q(phi beta) = -e and v_Q(phi' beta') = v_{Q'}(phi beta) = e > 0, so v_Q(10r + 1) = v_Q(Tr(phi beta)) = -e, and v_q(r) = -e. So the denominator of r is supported on 5 (from the 1/10) and on the split primes where beta is not a unit, with v_l(r) = -|k_l|.
If those primes lie in S, then beta is a norm-1 element of O[1/S]^* = +-phi^Z prod (pi^Z pi'^Z), taking N(pi) = l > 0. Norm 1 forces the exponents of pi and pi' to be opposite and the exponent of phi to be even, and phi^{2m} = (-eps)^m. So beta is in +-<eps, omega_l>.
The orbit description follows. For fixed (sign, k), the values are T L(+-eps^n omega^k - 1), which grow like phi^{2|n|} in both directions. Brute force (c1_linearization.py) found 0 failures on 292 elements, and equality with the brute-force D_T for T = 5, 55, 605, 6655.

[2] PROOF OF THEOREM 2.
Let G be the finite group (O[1/l]/10M)^*, which makes sense because l ∤ 10M. Let a be the order of eps in G and b the order of omega_l. Put eta1 = eps^{2a} and eta2 = omega_l^{2b}. Then:
- every beta = eta1^x eta2^y satisfies beta = 1 mod 10M O[1/l];
- sigma1(eta1) = phi^{4a} > 0 and sigma1(eta2) > 0.
Independence of the logarithms. Suppose x log sigma1(eta1) + y log sigma1(eta2) = 0 with integers x, y. Then sigma1(beta) = 1, so sigma2(beta) = 1/sigma1(beta) = 1, and beta = 1. But eta2 has Q-valuation 2b != 0 at the prime Q = (pi), so y = 0, and then x = 0. So the two logarithms are Q-linearly independent, and {x log sigma1 eta1 + y log sigma1 eta2} is dense in R. Pick (x, y) with t := log sigma1(beta) in (0, t0) for any t0 > 0, or in (-t0, 0) if the other sign is wanted.
Put r = L(beta - 1) = (phi(e^t - 1) - phi^{-1}(e^{-t} - 1))/10. Then:
- r is in R_+ by Theorem 1(a), and r != 0 because beta != 1 and sigma1(beta) > 0 > sigma1(eps^{-1});
- 0 < r <= sqrt5 (e^t - 1)/10 for t > 0;
- beta - 1 is in 10M O[1/l], so Tr(phi(beta - 1)) is in 10M Z[1/l] and r is in M Z[1/l];
- distinct (x, y) give distinct beta, and at most two beta share an r, so there are infinitely many such r.
Check (c2b.py): M = 21, l = 11. The group orders are 120 and 60; (x, y) = (-54, 157) gives r ~ -0.01356 in R_+. The script confirmed that 21 | r in Z_(2), that 20r^2 + 4r + 1 is a rational square, and that the denominator is a product of powers of 5 and 11.
COROLLARY 2.1. Take x = M/3^n, which is in M Z_(2), with 0 < x < 1/(2s max|theta_j|). For each j, theta_j x lies in (0, 1/s), in (-1/s, 0) or at 0, according to the sign of theta_j. Take r from Theorem 2 with 0 < r < x. Then theta_j(x + r) has the same sign as theta_j x and absolute value below 1/s, and x + r = x mod M. So x and x + r lie in the same cell, and x ~ x + r is an edge. The open-set version is the same argument with a margin. For the version on one subgroup Z[1/(5l)], restricted to Z[1/l] a character with rational l-component is a real character times a character of finite order, so Theorem 2 applies with M enlarged.
COROLLARY 2.2. The edge (x, x + r) lies in (1/T)Z for T = 3^n 5 l^k. Its labels Tx and T(x + r) are small and positive, so they lie in I_T(h), which starts at 0 for T > 0. Its distance |Tr| lies in D_T(h) once h exceeds its L-value and n_T(h) exceeds Tr. The colour rule is exactly the cell colouring at x = i/T.

[3] PROOF OF THEOREM 3, modulo Berend.
Let Lambda'' be the set of beta in <eps^3, omega_l^3> with beta = 1 mod 10M. It is free abelian of rank 2. On N0 = 10M O[1/l] define psi(x) = chi(Tr(phi x)/10). The argument Tr(phi x)/10 lies in M Z[1/l], which is inside Z_(2), and psi is a homomorphism. Extend psi to psi~ in X := Hom(O[1/l], T). The circle T is divisible, so the extension exists. For beta in Lambda'', beta - 1 is in N0, and chi(L(beta - 1)) = psi~(beta) - psi~(1).
Lambda'' acts on X by (beta.y)(x) = y(beta x). These are continuous automorphisms of a solenoid in the sense used by Einsiedler-Lindenstrauss: X is compact, connected and metrizable, and its dual O[1/l] embeds in Q^2.
Berend's hypotheses:
- Total irreducibility. Let H != 0 be a subgroup of O[1/l] invariant under a finite-index subgroup Lambda' of Lambda''. Put A = Z[Lambda']. With omega^b in A and coprime pi^b, pi'^b, one gets O[omega^b] = O[1/pi'], so O[omega^{+-b}] = O[1/l]. If f O ⊂ Z[eps^c], then f O[1/l] ⊂ A. So H ⊇ A h ⊇ f h O[1/l], which has finite index, and H^perp is finite. So no proper infinite closed invariant subgroup exists for any finite-index subgroup.
- Not virtually cyclic, because Lambda'' has rank 2 and acts faithfully.
- A hyperbolic element exists: eps^{3a} omega^{3b} with b != 0 and sigma1 != 1 has absolute value != 1 at both real places and both l-adic places.
Berend's theorem, in the form quoted in Einsiedler-Lindenstrauss (arXiv 2101.11120, introduction, citing Berend [1, 2]), says that such an action has no proper infinite closed invariant subsets. So the orbit Lambda''.psi~ is finite or dense.
If the orbit is finite, its stabiliser is infinite, and every beta != 1 in it gives chi(r) = 0.
If the orbit is dense, X is a compact Hausdorff space without isolated points, so the open set { y : |y(1) - psi~(1)| < delta } contains infinitely many orbit points beta.psi~. Each gives ||chi(L(beta - 1))|| < delta.
In both cases r != 0, because beta != 1 and eps^{-1} is not in <eps^3, omega^3>. At most two beta share an r, so there are infinitely many r. Corollary 3.1 follows as in [2], with a margin, or with exact recurrence when chi has finite order.

[4] PROOF OF PROPOSITION 4.
Suppose c is a proper colouring of Gamma with C colours. Some class E has positive upper Banach density d*(E) along a Følner sequence of Z_(2). By the Furstenberg correspondence principle for countable abelian groups, there are a measure-preserving action (X, mu, T_g) and a set A with mu(A) = d*(E) and mu(A ∩ T_r^{-1}A) <= d*(E ∩ (E - r)) = 0 for every r in the connection set. Bochner's theorem gives <U_g 1_A, 1_A> = ∫ chi(g) dsigma(chi), with sigma({1}) = ||P_inv 1_A||^2 >= mu(A)^2 > 0. So 0 = ∫ nu_n^ dsigma for every n. Apply Fatou's lemma to the functions 1 + Re nu_n^ >= 0: ∫ liminf Re nu_n^ dsigma <= 0. The left side is at least sigma({1}) > 0, which is a contradiction.
Why this does not yet decide the question: for nu_n uniform on L(B_n - 1) with B_n Følner boxes in Lambda'', liminf nu_n^(chi) is the infimum over weak-star limits mu of empirical orbit measures of ∫ Re(y(1) conj psi~(1)) dmu(y). Those limits are Lambda''-invariant. Positive-entropy ergodic ones are Haar (Einsiedler-Lindenstrauss rigidity), and they contribute 0. Atomic parts at fixed points of finite orbits can contribute negatively, and so can zero-entropy measures, if they exist (a question of Furstenberg times-2-times-3 type). So the box-average route stalls exactly at measure rigidity.

[5] NUMERICS (sanity checks, uncertified). c3_ratio.py and c3b.py compute the weighted ratio (LP) bound for Cay(Z, D_T^inf ∩ [1, B]) on the one-prime tower T = 5·11^k, using cutting planes and a fine grid:
- T = 5: 3.633;
- T = 55: 4.883;
- T = 605: 4.873 to 4.915;
- T = 6655: 4.907 to 4.978.
The bound is essentially flat in k. The earlier note reports 5.74 for T = 1045 = 5·11·19, which has two split primes. This suggests that spectral growth, if any, comes from the number of split primes and not from prime powers.

WHY T31 AND FKM DO NOT TRANSFER. Gamma is translation-invariant, and its relation 20(x-y)^2 +- 4(x-y) + 1 = square is inhomogeneous in the coloured variables. Homogenizing introduces the common denominator T as a third variable, which is not coloured. No rational vertex map u -> g(u) with g(u) - g(v) homogeneous of degree 0 exists. With vertices 1/u the relation becomes a quartic form, which is outside Frantzikinakis-Klurman-Moreira.

## External results used

- Berend's theorem, as summarized in M. Einsiedler and E. Lindenstrauss, Rigidity properties for commuting automorphisms on tori and solenoids, arXiv 2101.11120 (Ergodic Theory Dynam. Systems), introduction, citing D. Berend, Multi-invariant sets on tori, Trans. AMS 280 (1983) 509-532, and Berend's paper on compact abelian groups. It says that a Z^d-action by automorphisms of a solenoid has no proper infinite closed invariant subsets iff it is totally irreducible, not virtually cyclic, and contains a hyperbolic element. Used in Theorem 3.
- The Furstenberg correspondence principle for countable abelian groups, together with Bochner's theorem. Used in Proposition 4.
- The positive-entropy rigidity theorem of Einsiedler-Lindenstrauss (same paper, Theorem 1.3). Used only in the remark on why box averages stall.

## Checks

c1_linearization.py: 292 elements beta = +-eps^n omega^k gave 0 failures on squareness, the 2-adic criterion and the denominator support. The beta enumeration equals the brute-force set S_T^inf/T for T = 5, 55, 605, 6655 with |d| <= 4000. c2b.py found an explicit edge r ~ -0.01356 with 21 | r, a square check and denominator 5^a 11^b. c3_ratio.py and c3b.py give the ratio bounds quoted above. Every script ran with py in under 60 s (the c3b run on T = 73205 was cut off at 60 s). Scripts are in the script folders of this directory. The earlier derivation was re-derived by hand: the perpendicularity equation, the formula for u, the integrality criterion, the position of R and the fatal/harmless split all check out. Its expected-count formula is a heuristic and was not checked.

## Gaps

- The main question is not decided: chi(Gamma) is neither proved finite nor proved infinite.
- Bohr recurrence of the connection set for several arbitrary adelic characters at once is not proved. Theorems 2 and 3 cover all real-and-residue characters jointly, one arbitrary character, and tuples of the form psi(c_i x) with c_i in O[1/l], all by the same argument. K-independent tuples need joint recurrence for the diagonal action on X^k, which is not totally irreducible. So lead (2) is refuted only in its real-arcs-plus-residues form and its one-character form.
- Even full Bohr recurrence would not give chi(Gamma) = infinity. Whether Bohr recurrence implies chromatic recurrence is Katznelson's question, open as far as I know.
- Theorem 3 rests on Berend's theorem. I read it only in the summary given by Einsiedler and Lindenstrauss (arXiv 2101.11120, introduction), not in Berend's original TAMS papers, and I checked its hypotheses against that summary.
- Proposition 4 uses the Furstenberg correspondence principle and Bochner's theorem without re-proof. Its hypothesis is unverified for every natural choice of nu_n. The box-average choice needs control of zero-entropy invariant measures, a question of times-2-times-3 type.
- The ratio-bound numerics come from an LP on a grid, with no rigorous minimum certificate. They are evidence only.
- Nothing here has an independent audit. Theorems 1 and 2 and the corollaries were re-read line by line by me.

## Missing estimate

To prove chi(Gamma) = infinity: finitely supported probability measures nu_n on L(Lambda - 1), with Lambda the norm-one S-units of Q(sqrt5), such that liminf Re nu_n^(chi) >= 0 for every nontrivial character chi of Z_(2) (Proposition 4). Its necessary topological shadow is joint Bohr recurrence: for any k characters of Z_(2) there is a beta != 1 in Lambda with chi_i(L(beta - 1)) ~ 0 for all i. To prove chi(Gamma) < infinity: a colouring that, for every split prime l, uses an l-adically irrational character. Theorem 2 rules out the alternatives.

## Next steps

- Decide chi(Gamma_l) for one split prime, where Gamma_l = Gamma restricted to Z[1/(5l)] with connection set L(+-<eps, omega_l> - 1) and chi(Gamma_l) = sup_k chi_inf(5 l^k). It is a rank-2 S-unit Cayley graph, and its ratio bound is flat near 4.9. A finite colouring of Gamma_l would show that infinite chi(Gamma), if true, comes from unbounded rank. An infinite chi(Gamma_l) would settle the question outright.
- Try joint Bohr recurrence for K-independent pairs of characters, using the diagonal Lambda-action on X x X and the orbit-closure results of Lindenstrauss and Z. Wang for non-irreducible actions. If even pairs fail, build an explicit two-character colouring candidate and test it on D_T for T with many split primes.
- Look for nu_n supported on beta near 1 at all real places and congruent to 1 modulo growing moduli, where Theorem 2 makes the rational characters close to 1. Ask whether irrational l-adic characters can be averaged out by summing over many split primes at once, which Gamma allows and Gamma_l does not.
- Have Theorems 1 and 2 audited. They are short and change how lead (2) should be posed: any Bohr colouring must be l-adically irrational at every split prime.

