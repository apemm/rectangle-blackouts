# An orbit bound for the chromatic number of one diagonal

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: chi(G_T(h)) <= 1920 rho_s(T) log2(8 rho_s(T)) + 1 for every h, with rho_s(T) the product of (2e+1) over split prime powers l^e || T. Not audited yet.

# Result

## Status

partial

## Summary

Proved, uniformly in h: chi(G_T(h)) <= chi_inf(T) <= 1920 rho_s(T) log2(8 rho_s(T)) + 1, where rho_s(T) = prod over split l^e || T of (2e+1). The proof counts orbits per dyadic window and applies Peres-Schlag Theorem 3.1, which I read in the paper. The bound is polynomial in the exponents for a fixed number of primes, but exponential in w = omega_split. The payoff computation is checked and correct. A polynomial bound in w alone would contain the open question chi(Gamma_l) < infinity, so the hypothesis should use Omega_split. No polynomial or subexponential bound in w was found, and no exponential lower bound for a natural class of colourings.

## Statements

Notation: stride 4. Q(T,d) = 20d^2 + 4Td + T^2. D_T^inf = {|d| : d != 0, Q(T,d) a square}, chi_inf(T) = chi(Cay(Z, D_T^inf)). For odd T, rho_s(T) = prod over l^e || T with l = +-1 mod 5 of (2e+1). Omega_s(T) and omega_s(T) count those split primes with and without multiplicity.

THEOREM 1 (window count) [proved]. D_T^inf lies in the union of 2 rho_s(T) sets O_gamma. Each O_gamma meets every interval [D, 2D] (D > 0) in at most 4 points. Hence |D_T^inf ∩ [D,2D]| <= 8 rho_s(T) for every D > 0.

THEOREM 2 (generic chromatic bound, uniform in h) [proved, citing Peres-Schlag Thm 3.1]. For every odd T and every h:
 chi(G_T(h)) <= chi_inf(T) <= floor(240 M log2 M) + 1, with M = 8 rho_s(T).
So chi <= C rho_s log(2 rho_s). For T squarefree in its split part this is C 3^w w. For T = (inert part)·5^a·l^e it gives chi_inf <= C e log(2e), polynomial in Omega_s. For fixed omega_s = w it is at most C (3 Omega_s)^w log, polynomial of degree w in Omega_s.

PROPOSITION 3 (payoff; conditional, computation verified). Assume (H_c): chi(G_T(h)) <= C0 (1 + Omega_s(T))^c for all h and all diagonals T. This hypothesis is weaker than the same bound with omega_s. Then for h >= h0 the q_h labels have a label scaffold (no corner triple and no rival pair; mixed quadruples and the sea are not treated) of width <= C h^2 (loglog h)^c. The heavy threshold is t = 2.5 loglog h and the light bound is B = C0 (1 + 2.5 loglog h)^c. The number of heavy diagonals is <= C h (log h)^(-2.03); the target's choice t = 3 loglog h gives (log h)^(-2.875). If instead chi <= exp(o(Omega_s)), the width is h^2 (log h)^(o(1)). Inputs: Proposition R, Lemma P, Lemma G and Theorem 3's gluing from heavy_light_split.md; R is assembled from audited parts, while P and G are unaudited.

PROPOSITION 4 (unconditional consequence of Theorem 2) [proved modulo the same inputs]. Putting Theorem 2 into the light-heavy split gives the label scaffold in width O(h^2 (log h)^(1.4967)) at stride 4. That is exactly the m = 1 exponent of heavy_light_split Theorem 3, so there is no exponent gain. The light/heavy criterion now depends only on rho_s(T) and not on h.

PROPOSITION 5 (what the omega-version contains) [proved, elementary]. If chi(G_T(h)) <= F(omega_s(T)) for all T and h, then chi(Gamma_S) <= F(|S|) for every finite set S of split primes. Here Gamma_S is Gamma restricted to Z_(2) ∩ Z[1/(5 prod S)]. In particular chi(Gamma_l) <= F(1) for every split l. Whether chi(Gamma_l) is finite is open (gamma_linearization.md, Next steps). So the target as stated in w = omega_split includes an open problem. The Omega_s or rho_s form does not include it, and Theorem 2 proves that form for omega_s <= 1, with polynomial growth.

NOT PROVED: any bound subexponential in omega_s; any lower bound showing that Bohr (rotation) colourings need exponentially many colours; chi(Gamma_l) < infinity.

## Proofs

[1] ORBITS (check of the derivation in the setting). Take d in S_T^inf with L = sqrt Q(T,d) > 0, and put X = 10d + T. Then X^2 - 5L^2 = -4T^2 (L3 of limit_graph_gamma.md, which I re-derived). So beta = (X + L sqrt5)/2 lies in Z[phi], N(beta) = -T^2, X = Tr(beta) and d = (Tr beta - T)/10.
Z[phi] is a PID. The ideals of norm T^2 are (q)^a at an inert q^a || T, (sqrt5)^(2a) at 5^a || T, and Q^i Q'^(2e-i) (0 <= i <= 2e) at a split l^e || T. So there are exactly rho_s(T) of them.
The generators of one ideal are +-phi^n beta0. Exactly the n of one parity give norm -T^2, because N(phi) = -1. So the elements of norm -T^2 fall into exactly 2 rho_s(T) classes under multiplication by phi^(2k), k in Z. Each class is {+- gamma phi^(2k)}, with the sign fixed per class.
This confirms the target's count of "about tau_split(T^2) orbits": the exact count is 2 prod(2a_p + 1). The valuation statements of the target agree with gamma_linearization Theorem 1(c), v_l(r) = -|k_l|, and I did not need them.
Fix a class with representative gamma (real embedding). Then gamma gamma' = -T^2 < 0. Write gamma = s|T| e^(u0) and gamma' = -s|T| e^(-u0), with s = +-1. Then Tr(gamma phi^(2k)) = 2 s |T| sinh(u_k), with u_k = u0 + k·Delta and Delta = 2 log phi. So |d_k| = (|T|/10)|z_k|, where z_k = 2 sinh(u_k) - sigma and sigma = s·sgn(T) is in {+-1}. O_gamma is the set of those |d_k| that are positive integers.

[2] PROOF OF THEOREM 1. z_k is strictly increasing in k, and
 z_{k+1} - z_k = 2(sinh(u_k + Delta) - sinh u_k) = 4 cosh(u_k + Delta/2) sinh(Delta/2) = 2 cosh(u_k + Delta/2),
because sinh(log phi) = (phi - 1/phi)/2 = 1/2. In particular the gaps are >= 2.
Put a = 10D/|T|. We need #{k : |z_k| in [a, 2a]} <= 4.
Positive side. Suppose three indices have z in [a, 2a]. By monotonicity some three consecutive k, k+1, k+2 do. Then a >= z_{k+2} - z_k >= 4, so a >= 4. Next, 2 sinh u_{k+1} = z_{k+1} + sigma >= a - 1 > 0, so u_{k+1} > 0 and cosh(u_{k+1} + Delta/2) > sinh u_{k+1} >= (a-1)/2. Hence z_{k+2} - z_k > 2 + (a - 1) = a + 1 > a, which is a contradiction.
Negative side, [-2a, -a]. The same argument works: 2 sinh u_{k+1} <= 1 - a < 0, so u_{k+1} < 0. Then u_k + Delta/2 = u_{k+1} - Delta/2 < u_{k+1} < 0, which gives cosh(u_k + Delta/2) > |sinh u_{k+1}| >= (a-1)/2, and the same contradiction follows.
So each class contributes at most 2 + 2 points to [D, 2D]. Several classes may give the same |d|, which only lowers the count.

[3] PROOF OF THEOREM 2. Cited result: Peres and Schlag, "Two Erdős problems on lacunary sequences: chromatic number and Diophantine approximation", Bull. LMS 42 (2010), arXiv 0706.0223. I read Theorem 3.1 in the arXiv text. It says: if M >= 4 and the increasing sequence S = {n_j} satisfies n_{j+M} > 2 n_j for all j, then some theta has ||n_j theta|| >= c0/(M log2 M) for all j, with c0 = 1/240. The proof uses their one-sided local lemma, Lemma 2.1, with dyadic-interval events.
Apply it to S = D_T^inf in increasing order, with M = 8 rho_s(T) >= 8. If n_{j+M} <= 2 n_j, then the M+1 distinct elements n_j, ..., n_{j+M} lie in [n_j, 2n_j], which contradicts Theorem 1. So the hypothesis holds.
Let delta = 1/(240 M log2 M) and k = floor(1/delta) + 1. Colour i by floor(k·frac(theta i)). If two integers get the same colour, their difference e has ||theta e|| < 1/k < delta, so e is not in D_T^inf. This gives chi_inf(T) <= k.
G_T(h) is a subgraph of Cay(Z, D_T^inf), because D_T(h) is contained in D_T^inf. That gives the bound for every h.
Prime-power and fixed-w cases: prod(2e_l + 1) <= (1 + 2 Omega_s/w)^w by AM-GM.
Remark (sketched, not written in full): for stride 2 sigma the same proof runs in Z[sqrt(sigma^2+1)]. There X^2 - Delta L^2 = -sigma^2 T^2 with X = 2 Delta d + T, and the unit eta = sigma + sqrt(sigma^2+1) has sinh(log eta) = sigma >= 1, so the gap step still works. The orbit count becomes C(sigma) prod over primes split in that field. I did not write out the order and class-group bookkeeping.

[4] PROOF OF PROPOSITION 3 (the payoff computation).
Divisor-type sum. f(n) = z^(Omega_s(n)) satisfies f = 1 * g, where g is supported on products of split primes and g(p^e) = (z-1) z^(e-1). So
 sum_{n<=x} f(n) <= x sum_{m<=x} g(m)/m <= x prod_{p split <= x} (1 + (z-1)/(p - z)).
This needs z < 11, since the least split prime is 11. By Mertens' theorem for primes = +-1 mod 5 (sum 1/p = (1/2) loglog x + O(1)), the right side is <= C_z x (log x)^((z-1)/2).
Tail. #{odd t < h : Omega_s(t) > tau loglog h} <= C_z h (log h)^((z-1)/2 - tau ln z).
Light region. Diagonals with Omega_s <= t have chi <= B = C0(1+t)^c. So each has at most B independent classes, and Proposition R (stride 4) places them in width <= 240 B h^2 + 2h + 2.
Heavy region. There are H_d <= 2 C_z h (log h)^((z-1)/2 - tau ln z) heavy diagonals, so the row degree is Delta <= H_d. Lemma P gives width <= 816 H_d h (1 + ln h)^2 + 1 <= C h^2 (log h)^(2 + (z-1)/2 - tau ln z).
Choice of parameters. The exponent is negative iff tau > (z+3)/(2 ln z). That is minimised near z ~ 4.97, where it equals ~2.486, so tau = 2.5 works, and tau = 3 with z = 6 gives exponent 2 + 2.5 - 3 ln 6 = -0.875 (heavy-diagonal fraction (log h)^(-2.875), which matches the target's claim).
Gluing. m + 1 = 2 regions are joined with gaps 2W_h + 1 (Lemma G), at cost O(h^2).
Total: O(h^2 (loglog h)^c) + o(h^2). With F = exp(o(Omega)), B = F(2.5 loglog h) = (log h)^(o(1)).
The omega_s version in the setting is also correct: the same product without the higher powers, with any z > 1.

[5] PROOF OF PROPOSITION 4. Use rho_s(t)^a (log2 8 rho_s)^a <= C_eps rho_s^(a+eps). Then sum_{t<h} rho_s(t)^a <= C h (log h)^((3^a - 1)/2) by the same divisor-sum bound, with g(p) = 3^a - 1 at split p and g(p^e) <= (2e+1)^a.
Markov's inequality gives H_d(B) <= C h (log h)^(E(a)-1) B^(-a+eps), with E(a) = (1 + 3^a)/2. This is the m = 1 case of Theorem 1(b) of heavy_light_split.md, without the factor log(3h/|T|). The optimisation is the same: theta = min_a (3 + 3^a)/(2(1+a)) = 1.4967 at a ~ 0.91.

[6] PROOF OF PROPOSITION 5.
For every k >= 1, T_k = 5 l^k has omega_s = 1, so sup_h chi(G_{T_k}(h)) = chi_inf(T_k) <= F(1). This uses T1 of limit_graph_gamma.md, chi(G_T(h)) = chi_inf(T) for large h.
Cay(Z, D_T^inf) is isomorphic to Gamma[(1/T)Z] (T2 there). Every finite subgraph of Gamma_l lies in some (1/(5 l^k))Z ∩ Z_(2) (the union over k exhausts Z[1/(5l)] ∩ Z_(2)). By de Bruijn-Erdős, chi(Gamma_l) <= F(1).
The same argument works for a finite set S of split primes, with T = 5 prod_{l in S} l^k.

## External results used

- Y. Peres and W. Schlag, Two Erdős problems on lacunary sequences: chromatic number and Diophantine approximation, Bull. London Math. Soc. 42 (2010), 295-300; arXiv:0706.0223. Theorem 3.1: if M >= 4 and n_{j+M} > 2 n_j for all j, then some theta has ||n_j theta|| >= 1/(240 M log2 M) for all j. Read in the arXiv text; used in Theorem 2.
- Katznelson's colouring by arcs of theta·i (as recalled in Peres-Schlag's introduction).
- Mertens' theorem for primes in residue classes mod 5 (sum over p = +-1 mod 5, p <= x, of 1/p = (1/2) loglog x + O(1)); used in Proposition 3.
- de Bruijn-Erdős compactness; used in Proposition 5.
- Archive inputs, cited and not re-proved: L3, T1 and T2 of limit_graph_gamma.md; Theorem A and Lemma B of inert_scaling_equivalence.md; Theorem 1 of gamma_linearization.md; Lemmas F and O of gamma_structure.md; Proposition R, Lemma P, Lemma G and Theorems 1 and 3 of heavy_light_split.md (Lemma P and Lemma G unaudited).

## Checks

Scripts are in the script folders of this directory. Each ran with py in under 60 s; the repository was not touched.
- dset.py builds D_T^inf ∩ [1,X] from Theorem A of inert_scaling_equivalence.md. It agrees with brute force on 20d^2 + 4Td + T^2 = square for T = 1, 5, +-11, 55, 209, 605, +-1045 and |d| <= 3000.
- rot.py, window counts: maxwin <= 8 rho_s in every case (1 <= 8, 2 <= 8, 3 <= 24, 6 <= 24, 6 <= 72, 12 <= 72, 4 <= 40, 5 <= 56, 16 <= 216, 29 <= 216, 42 <= 648).
- rot.py, best rotation delta* by binary search on exact interval intersection. Values are listed in gaps.
- dsat.py (DSATUR on [0,2500)) gave 8, 8, 13, 17, 10 for T = 5, 11, 209, 1045, 6061. Those finite pieces are too small and DSATUR too weak, so these numbers are not used.
- The argument uses Theorem 3.1 and Lemma 2.1 of Peres and Schlag, arXiv 0706.0223.

## Gaps

- The target as posed is not reached. There is no bound subexponential in omega_s(T), so Proposition 3's hypothesis remains unproved. Theorem 2 is exponential, C 3^w w, in the number of distinct split primes.
- Proposition 5: a bound in omega_s alone would imply chi(Gamma_l) <= F(1) for every split l, which is an open problem in this archive. Future attempts should use Omega_s or rho_s, which suffice for the payoff.
- Natural-type obstruction not proved. For rotation (one-character Bohr) colourings, an exponential lower bound needs, for every theta, some d in D_T with ||theta d|| <= C^(-w). Lemma F gives exact additivity modulo T only for local characters a/T. The real part is uncontrolled (Lemma O), so the cube pigeonhole bound 2^(-w) applies only to theta in (1/T)Z. Such characters alone cannot colour T·D_1, which lies inside D_T. So no rigorous statement for a nontrivial class was obtained.
- Numerics, COMPUTED and not proofs. The best single rotation for the truncated sets D_T^inf ∩ [1,X] gives rotation-colour lower bounds 1/delta* = 2.40 (T=1), 4.40 (11), 10.07 (209), 17.09 (1045), 19.67 (6061), all at X = 2e6 except T = 1 and T = 11 (X = 2e4), and 22.45 (30305) and 21.5 (187891) at X = 3e5. These are lower bounds for the infinite sets, not limits: truncation lowers them, and T = 1045 went from 12.66 at X = 2e4 to 17.09 at X = 2e6. They grow by a factor of about 2 per added prime, but they have not converged. True chi_inf is known only from below (5, >= 6 for T = 55, >= 7 for T = 1045 by SAT), so these numbers neither show nor refute that rotation colourings are lossy.
- Measured maximal window counts max_D |D_T ∩ [D,2D]| are 1, 3, 6, 16, 42 for T = 1, 11, 209, 6061, 187891 (truncated sets; T = 1 to 6061 at X = 2e4, T = 187891 at X = 3e5), against the bound 8 rho_s = 8, 24, 72, 216, 648. These counts grow about like 3^w with a constant near 0.5 to 1, so the M ~ rho_s input to Peres-Schlag is not an artefact of the proof. The extra slack comes from the integrality condition Tr(gamma phi^(2k)) = T mod 10, which keeps only some k.
- The stride-menu version of Theorems 1 and 2 is sketched, not written in full (order index and class-group bookkeeping in Z[sqrt(sigma^2+1)]). It is not needed for Propositions 3 and 4 at stride 4.
- Proposition 3 and Proposition 4 inherit the caveats of heavy_light_split.md. Lemma P, Lemma G and Theorem 3's gluing are unaudited, and the scaffold excludes only corner triples and rival pairs: mixed quadruples and the sea are not treated. So this is not a bound on m_h.
- Peres-Schlag Theorem 3.1 is cited, not re-proved. I read its statement and proof in the arXiv text (hypothesis n_{j+M} > 2 n_j, M >= 4, delta = 1/(240 M log2 M)). The rest was re-derived once by me, with no independent audit.

## Missing estimate

To get a polynomial F, one needs a colouring of Cay(Z, D_T^inf) with poly(Omega_s(T)) colours. Here D_T^inf has about rho_s(T) ~ 3^w elements in every dyadic window above |T|/10 (Theorem 1 is sharp up to a constant: the measured window counts grow like 3^w). Any single-rotation (Bohr) colouring needs min_d ||theta d|| >= 1/poly(w). For a set with M elements per window that is not additively structured, the expected answer is theta-separation of order 1/M, so rotations are expected to need about 3^w colours, in line with the computed 1/delta* growth. A polynomial F therefore almost certainly needs a non-Bohr colouring that exploits the factorisation of orbits over the primes of T (support S of the exponent vector; l-adic disagreement exactly on S). Conversely, an exponential lower bound for Bohr colourings needs a joint equidistribution estimate. For every real theta, the values theta·T·r(beta) mod 1, with beta running over one dyadic window of the exponent box of ±<eps, omega_l : l | T>, must hit (-C^(-w), C^(-w)). This is an S-unit exponential-sum statement of the kind that is already missing in gamma_linearization.md.

## Next steps

- Record Theorem 2 in the ledger: chi(G_T(h)) <= 1920 rho_s(T) log2(8 rho_s(T)) + 1 uniformly in h. The window-count proof is half a page (the gaps of 2 sinh u_k satisfy z_{k+1} - z_k = 2 cosh(u_k + log phi), since sinh(log phi) = 1/2). It replaces the crude P·27^(2|F_T|) bound of L3 and turns the Peres-Schlag remark in limit_graph_gamma.md into a theorem.
- Restate the target for this route as F(Omega_s) or F(rho_s), not F(omega_s). The omega form contains chi(Gamma_l) < infinity (Proposition 5); the Omega form suffices for the payoff (Proposition 3).
- Uniform in the exponent: decide whether chi_inf(5 l^e) is bounded in e (Theorem 2 gives O(e log e); the ratio bound of gamma_linearization.md is flat near 4.9). Any colouring that is uniform in e must be non-Bohr in the real-plus-residue sense (Corollary 2.2 there). Peres-Schlag rotations avoid that corollary only because theta depends on T.
- Test the support-splitting idea for non-Bohr colourings by SAT on small cases. An edge of support S changes i mod l^(e_l) exactly for l in S. Look for colourings of Cay(Z, D_T) for T = 11·19, 11·19·29 of the form (rotation colour, colour of the disagreement pattern), and compare with the rotation lower bounds 10.1 and 19.7.
- For an obstruction: prove for one family of T an exponential lower bound on rotation colourings, through equidistribution of theta·T·L(beta - 1) mod 1 over beta in one dyadic window of the S-unit box (Hecke characters at the real place jointly with the l-adic phases of Lemma F). That would show the Bohr/LLL route cannot give poly(w), and that the payoff needs genuinely new colourings.

