# Families of configurations in Gamma and the growth question

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

No growing lower bound for chi_inf(T). A structure theorem through Laurent's theorem and computations on which primes add a colour. Not audited yet.

# Result

## Status

partial

## Summary

No growing lower bound for chi_inf(T). Two results instead. First, a proved structure theorem (via Laurent's theorem) says that in every infinite unit-parameter family of copies of a configuration, the moving edges are bipartite and add at most a factor 2 to the chromatic number. Second, computations suggest the "+1 per split prime" pattern holds only for a few small 'lucky' primes.

## Statements

NOTATION. As in gamma_linearization.md. K = Q(sqrt5), phi, phi' = -1/phi, eps = -phi^2. Lambda_S is the group of norm-one S-units of K, where S = {5} ∪ a finite set of split primes. r(beta) = L(beta - 1) = (Tr(phi beta) - 1)/10. Gamma_S is the graph Gamma restricted to denominators supported on S. For z = sigma_1(beta), r = rho(z) := (phi z + phi' z^{-1} - 1)/10, because sigma_2(beta) = 1/z.

THEOREM 1 (frozen-and-moving structure of families) [proved, citing Laurent's theorem]. Let H be a finite connected graph with fixed edge orientations, and let f: V(H) -> Z_(2) be an injective map with f(v_e) - f(u_e) = s_e r(beta_e), s_e = ±1 and beta_e in Lambda_S, for every edge e (a copy of H in Gamma_S). Let X_{H,s} ⊂ G_m^E be the variety of z = (z_e) with sum_e c_e(C) s_e rho(z_e) = 0 for every cycle C, and let z^0 = (sigma_1 beta_e). Suppose z^0 lies in a coset z^0·B ⊂ X_{H,s} with B a subtorus of positive dimension; call such a copy NON-ISOLATED. Write B = {(t^{a_e})_e : t in G_m^m}, and call e FROZEN if a_e = 0 and MOVING otherwise. Then:
 (i) There are at least two frozen components (components of the frozen spanning subgraph H_0). On the whole family, each frozen component moves by a single translation tau_C(t).
 (ii) (Parity) The map pi(v) = 10(y_v - y_{v0}) mod 2 is well defined in Z_(2)/2 = F_2, where y_v is the constant term of the Laurent polynomial x_v(t). It is constant on each frozen component, and every moving edge changes it. So no moving edge has both ends in one frozen component, and the graph obtained by contracting the frozen components is bipartite (and loopless).
 (iii) (Two offsets) For two frozen components C1 and C2, there is a delta(C1,C2) such that every moving edge u in C1, v in C2 satisfies p_v - p_u in {delta, delta + 1/5}. Here p is the fixed position inside a component, so x_v(t) = p_v + tau_C(t). Hence each vertex has at most 2 moving neighbours in each other frozen component.
 (iv) chi(H) <= 2·max_C chi(H[C]), the maximum over frozen components C. Each H[C] has fewer vertices than H and is carried to a translate of one fixed configuration by every member of the family.
 (v) By Laurent's theorem, for fixed S and fixed (H, s), all but finitely many copies of H in Gamma_S, up to translation, are non-isolated.

COROLLARY 1.1 [proved]. In a non-isolated copy, every odd cycle of H contains a frozen edge. A construction that realises a graph H with chi(H) = k along an infinite set of unit exponents (a family of copies with a free S-unit parameter) contains a fixed configuration with chi >= k/2 that does not depend on the parameter. Mechanisms that put the chromatic mass on edges indexed by a free unit exponent therefore gain at most a factor 2 over a rigid core. This covers mechanism (b) with n as a free coordinate, and Borsuk or shift-type maps whose 'antipodal' or 'shift' edges vary with the parameter. Cross-configuration edges, as used in Ramsey arguments, are not covered.

COMPUTED (sanity checks, not proofs; SAT without DRAT certificates).
 (C1) Lucky primes. Take a split prime l < 1200 and |d| <= 10^14. Gamma restricted to (1/l)Z or (1/5l)Z has a triangle avoiding the hub only for l in {11, 19, 29, 31, 41}.
 (C2) A K4 (hub pair plus an edge inside R_+) exists in Gamma_{5l} exactly for l = 11, 19, 31, 41. These are exactly the l for which a short-window SAT run gives chi_inf(5l) >= 6: UNSAT with 5 colours on [0,n) for n = 54 or 330, 300, 930 and 1230 (T = 55, 95, 155, 205). For l = 29, 59, 61, 71, 79 and 89, every window tried was 5-colourable: [0,1500) for T = 145, 295, 305, 355, 395, 445, and [0,2000) for T = 305. Larger windows timed out. Whether chi_inf(5l) = 5 for unlucky l is open.
 (C3) Neighbourhood graphs. Over 59 values T = 5·(1 to 3 split primes) and prime powers, chi(Gamma_T[N(0)]) equals its clique number: 2 to 4, never 5. The clique number of Gamma_T is at most 5 throughout. K5 occurs at T = 1045 and 30305; T = 30305 (w = 3) has no K6.
 (C4) Step anatomy. The 6-chromatic window structure for T = 55 uses only distances with 11 ∤ d, together with the hub 11: with these distances only, [0,400) is still not 5-colourable. For T = 1045, the new distances (19 ∤ d) plus the hub give a 5-colourable [0,700), so the old distances 19·D_55 are needed. Neither witness is made of copies of the previous witness joined by new orbits.
 (C5) Null model, T = 55 window ([0,54), 9 distances in [4,54)). Random distance sets of the same size give chi of 3 to 5, mostly 4. Random hub-structured sets {11} ∪ A ∪ (A+11) give 4 to 6. D_55 gives 6.

NOT PROVED: chi(Gamma) = infinity; any lower bound for chi_inf(T) that grows with w; chi_inf(T) >= 5 + w for any infinite family; any exponential lower bound; that the lucky set is finite.

## Proofs

[0] Laurent's theorem (Mordell–Lang for tori). Let X ⊂ G_m^n be defined over C, and let G be a finitely generated subgroup of (C*)^n. Then X ∩ G is contained in a finite union of cosets gamma_i H_i ⊂ X, with H_i algebraic subgroups. Equivalently, X ∩ G = ∪ (gamma_i H_i ∩ G).
Setup. Lambda = sigma_1(Lambda_S) is finitely generated (Dirichlet's S-unit theorem). The relations of X_{H,s} are Laurent polynomials in z because rho is. For each copy f, the point z^0 lies in X_{H,s} ∩ Lambda^E, because the cycle sums of f(v_e) - f(u_e) vanish. Each such point lies in some gamma_i H_i ⊂ X. If H_i is finite, only finitely many points lie there. Otherwise z^0·H_i^0 ⊂ gamma_i H_i ⊂ X, which proves (v), with B = H_i^0 a subtorus {t^A}.

[1] Positions. On z^0·B every cycle relation holds identically in t ∈ (C*)^m. So x_v(t) := f(v0) + (sum along any path from v0 to v of ± s_e rho(z^0_e t^{a_e})) is a well-defined Laurent polynomial, and x_v(1) = f(v). For a moving edge, CT(rho(z^0_e t^{a_e})) = -1/10, because t^{±a_e} has no constant term. For a frozen edge, the term is the constant r(beta_e). So y_{v_e} - y_{u_e} = -s_e/10 on moving edges and s_e r(beta_e) on frozen edges.
(i) If H_0 were connected and spanning, every vertex difference would be constant, so every a_e would be 0 and B would be trivial. That is a contradiction, so there are at least two frozen components. Inside a frozen component, the differences are constant in t, so the component moves by a single tau_C(t).
(ii) For a frozen edge, r(beta_e) = ±(f(v_e) - f(u_e)) lies in Z_(2), so 10 s_e r(beta_e) lies in 10Z_(2) ⊂ 2Z_(2). For a moving edge, 10·(-s_e/10) = -s_e is odd. Hence 10(y_v - y_{v0}) lies in Z + 10Z_(2) ⊂ Z_(2), pi is well defined, frozen edges preserve pi and moving edges flip it. A moving edge inside one frozen component would join two vertices with equal pi, which is impossible. So the contracted graph has no loops and is 2-coloured by pi.
(iii) Let u ∈ C1 and v ∈ C2 be joined by a moving edge e. Then p_v - p_u + (tau_2 - tau_1)(t) = s_e rho(gamma_e t^{a_e}). So the nonconstant part NC of tau_2 - tau_1 equals (s_e/10)(phi gamma_e t^{a_e} + phi' gamma_e^{-1} t^{-a_e}) for every such edge. Compare two such edges e and e'. If a_{e'} = a_e, the coefficient of t^{a_e} gives s'gamma' = s gamma. If a_{e'} = -a_e, it gives s phi gamma = s' phi' gamma'^{-1}, that is, gamma' = s s' eps^{-1} gamma^{-1}; the other coefficient then agrees because phi phi' = -1 and phi'/phi = eps^{-1}. In both cases the constant terms -s/10 and -s'/10 are equal or differ by ±1/5. Comparing constant terms gives p_v - p_u = -s_e/10 - CT(tau_2 - tau_1), which takes one of two values that differ by 1/5. f is injective, so the p_v are distinct inside C2. Hence each u has at most 2 moving neighbours in C2.
(iv) Colour v by (pi(v), c_C(v)), where c_C is a proper colouring of H[C] for the frozen component C containing v. Moving edges are proper because pi changes. Frozen edges stay inside one C, by (ii), and c_C separates their ends. Also H[C] = H_0[C], by (ii).
Corollary 1.1. An odd cycle cannot consist of moving edges only, because pi alternates along moving edges. The rest follows from (iv).

[2] Remark (known, recorded for completeness). For every modulus P, D_T^inf contains a nonzero multiple of P. The orbit beta = T phi^{2k+1} gives d_k = T(L_{2k+1} - 1)/10, with d_0 = 0, and Lucas numbers are purely periodic modulo 10P. So no periodic colouring of Cay(Z, D_T^inf) is proper. This is a special case of Corollary 2.1 of gamma_linearization.md.

[3] Check of the payoff computation (conditional). Assume chi <= C(1+w)^c. With w approximately Poisson of mean mu = (1/2)L, where L = log log h, the tail at 3L = 6 mu is exp(-mu(6 ln 6 - 5)) = (log h)^{-2.875} <= (log h)^{-2}. So delta_h(B) log^2 h = o(1), and the width is O(h^2 (log log h)^c), as claimed. Weighting by n_T does not change the order. A rigorous version needs a Hardy–Ramanujan-type tail for omega_split. I did not write that out.

## External results used

- M. Laurent, 'Équations diophantiennes exponentielles', Invent. Math. 78 (1984) 299–327 (Mordell–Lang for tori): for X ⊂ G_m^n and a finitely generated subgroup G, X ∩ G = ∪ γ_i(H_i ∩ G) with γ_i H_i ⊂ X. I read the statement only in secondary sources. Search results used: https://math.leidenuniv.nl/~evertsejh/00-torus.pdf, https://pub.math.leidenuniv.nl/%7Eevertsejh/09-varietiesfinal.pdf, https://eudml.org/doc/182179
- Dirichlet's S-unit theorem: Lambda_S is finitely generated.
- Repository (cited, not re-proved): Theorem 1 and Corollary 2.1 of gamma_linearization.md; Theorems A, B, C3 and Lemmas F, O of gamma_structure.md; L2 and T3 of limit_graph_gamma.md; Lemma G of inert_scaling_equivalence.md.

## Checks

I wrote every script in the matching scripts_ folder of this directory and ran each with py, under 60 s and well under 1 GB.
- sinf.py enumerates S_T^inf exactly, through beta = a + b phi with N(beta) = -T^2 and the orbits phi^{±2k}. It asserts agreement with brute force on |d| <= 3000; this passed for T = 55 and 1045.
- clq.py: maximum cliques through 0.
- nbchi.py and scan.py: chromatic number and clique number of Gamma_T[N(0)] (SAT) for 59 values of T.
- tri.py: non-hub triangles for split l < 1200 at |d| <= 10^14.
- step.py and win.py: window SAT (CaDiCaL 1.5.3 or Glucose 4).
- split.py: new and old distance split for T = 55 and 1045.
- rnd.py and rndhub.py: null models.
dt.py and col.py are helpers.
Timeouts: T = 145 at n = 2000 and 3000 (and 6000 in an earlier run); T = 295 at n = 2000 and 4000; T = 305 at n = 3000 and 4000. T = 55 with all distances at n = 400 and k = 6 also timed out, and is already known to be UNSAT at n = 54 with k = 5.
I re-derived Theorem 1 by hand once. Its proof contains no computation.

## Gaps

- The target is not reached. There is no proof that chi(Gamma) = infinity, no lower bound for chi_inf(T) that grows with w, and no exponential lower bound.
- Laurent's theorem is cited, not re-proved. I read its statement only in secondary sources (an Evertse survey and lecture notes), not in Laurent's paper: M. Laurent, Equations diophantiennes exponentielles, Invent. Math. 78 (1984), also in Sem. Theorie des Nombres Bordeaux 1983-84. Both the coset form and the 'contained in finitely many cosets inside X' form give what Theorem 1 uses.
- Theorem 1 is a structural obstruction only. It does not cover isolated (rigid) configurations, which for fixed S and fixed shape are finitely many. It does not cover cross-configuration edges, as used in Ramsey or Hales–Jewett arguments, or growing S, where Laurent's theorem is not uniform. Iterating (iv) gives only 2^depth bounds.
- Theorem 1 has not been audited. A second reader should check (iii): the comparison of Laurent coefficients, including the hub case s' = -s, and the identity gamma' = s s' eps^{-1} gamma^{-1}.
- Every computed claim is a truncation (|d| <= 10^14, or windows [0,n)) or an uncertified SAT result, with one solver and no DRAT log. 'Lucky primes are only 11, 19, 29, 31, 41' is not proved even below 1200, because larger heights are not excluded rigorously.
- chi_inf(5l) for unlucky l (for example l = 29, 59) is undecided: every window tried was 5-colourable, and larger windows timed out. So the step lemma chi_inf(Tp) >= chi_inf(T) + 1 for every split p is neither proved nor refuted. It is only shown to lack the support the 5 + w pattern assumed.
- The payoff check is a conditional heuristic, using a Poisson model for omega_split. The poly(w) hypothesis behind it is neither supported nor refuted by this round.

## Missing estimate

To show that chi_inf grows with w, one must produce isolated (rigid) configurations in Gamma_S with chi growing in w, or use cross-configuration (Ramsey) structure. By Theorem 1, unit-parameter families give at most a factor 2 over such a core. The data say rigid configurations with extra cliques, such as K4 or K5, occur only at a few small primes. The remaining plausible source of growth is the bounded-window regime |T| comparable to h, where about 3^w distances behave like a random set. There, a lower bound needs either a uniform exponential-sum bound min_theta sum_{d in D_T} cos(2 pi d theta) >= -o(k_T) (Lemma G of inert_scaling_equivalence.md, which is spectral), or a combinatorial independence-number bound alpha(G_T) = o(n_T) for these sets. Conversely, to show that no step occurs at an unlucky prime, one needs an explicit non-periodic 5-colouring of Cay(Z, D_{5l}^inf), for example a Bohr-type colouring combined with chi_inf(5) = 5.

## Next steps

- Audit Theorem 1, especially (ii) and (iii). If it holds, record in the ledger that 'free unit exponent' constructions gain at most a factor 2 over a rigid core.
- Correct the round-4 summary. The pattern chi_inf >= 5 + w rests on T = 5, 55, 1045, which are built from the lucky primes 11 and 19. Single unlucky primes (59 <= l < 1200) give no non-hub triangle, and no 6-colour lower bound has been found for them.
- Decide chi_inf(295) or chi_inf(145) with longer SAT runs outside the 60 s limit: windows [0,n) with n of 3000 to 10000, and DRAT logs if UNSAT. If both stay at 5, the step lemma is false, which would support the heavy-light payoff.
- Test growth in the bounded-window regime with unlucky primes only, for example T = 5·59·61 = 17995 and 5·59·61·71, with G_T(h) at h = 2|T|. This separates the random-model growth (about 3^w/log h) from sporadic small-prime cliques.
- Try to prove that the lucky set is finite: a triangle in Gamma_{5l} is a rank-2 S-unit equation. Uniform Evertse–Schlickewei–Schmidt bounds give at most an absolute number of triangles per l. Existence for large l would need a polynomial family l(s) = N(p(s), q(s)) with a three-term identity, and none appears below 1200.

