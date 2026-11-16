# Hypothesis (F) and the independence density of Cay(Z, D_T)

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: (F) is equivalent to chi_f(Gamma[32 Z_(2)]) < infinity, and its untyped form to chi_f(Gamma) < infinity. Both are open. Proposition 5 does not need (F): Theorem 4 gives the exponent under a saving 1/alpha_T <= kappa_T^beta Lambda^(-gamma), and a saving of log h over the trivial density on heavy diagonals already gives exponent 1. A lacunarity barrier (Proposition 3) shows that window and orbit counts alone cannot give that saving. Not audited yet.

# Result

## Status

partial

## Summary

Proposition 5 does not need (F). A saving of log h over the trivial density on heavy diagonals is enough for exponent 1. (F) itself is equivalent to chi_f(Gamma[32 Z_(2)]) < infinity. Both are open: (F) looks false and the weak form looks true.

## Statements

NOTATION. Lambda = log h, ell = loglog h, kappa_T = |D_T(h)|. For a finite set D of positive integers, mu(D) is the supremum of the densities of periodic sets A in Z with (A - A) ∩ ±D empty. The typed density is alpha_T(h) = mu((D_T(h) ∩ 32Z)/32), the same for every type tau. The untyped density is alpha^u_T(h) = mu(D_T(h)). Gamma^(32) is the induced subgraph Gamma[32 Z_(2)] of the limit graph Gamma (limit_graph_gamma.md). E(a) = (1+3^a)/2. phi is as in heavy_diagonals_sharp.md, and Phi(xi) = sup_{a>0} (a xi - E(a) + 1), which equals phi(xi) for xi > (ln 3)/2.

PROPOSITION 1 (dictionary; PROVED).
(a) mu(D) = 1/chi_f(Cay(Z, D)) for every finite D.
(b) alpha_T(h) <= alpha(G_T(h)[tau])/|V(G_T(h)[tau])| <= 2 alpha_T(h). So the finite-window graph and the periodic density agree up to a factor 2.
(c) alpha_T(h) >= alpha^u_T(h), and both are nonincreasing in h for fixed T.
(d) inf over h of alpha_T(h) = 1/chi_f(Gamma[(32/T)Z]). inf over (h, T) of alpha_T(h) = 1/chi_f(Gamma^(32)), and inf of alpha^u_T(h) = 1/chi_f(Gamma). Consequences:
 - (F) with constant K0, typed, for all h and T, holds iff chi_f(Gamma^(32)) < infinity.
 - The untyped (F) holds iff chi_f(Gamma) < infinity.
 - chi_f(Gamma^(32)) <= chi_f(Gamma) <= chi(Gamma).
 - A constant K0 uniform in h is the infinite-graph statement. Only a K0 that depends on h makes the finite window weaker.
(e) chi_f(Gamma) >= 5 (the K5). The K5 has odd differences, so it gives no typed bound. The only proved typed bound is chi_f(Gamma^(32)) > 2, from an odd cycle built on r1 = 32/4031 and r2 = 64/16255, which lie in R_odd with v_2 = 5 and 6.

PROPOSITION 2 (known instances; PROVED from audited inputs).
- alpha_T(h) >= alpha^u_T(h) >= 1/6400 whenever omega_s(T) <= 1 (Theorem E).
- alpha_T(h) >= 1/(2|D_T(h) ∩ 32Z| + 1) always.
- alpha^u_T(h) >= c log kappa_T/kappa_T when R_T <= kappa_T^(3/2) (three_term_relations Theorem 2).
- Theorem W (audited) and chi_orbit_bound Theorem 2 (unaudited) bound 1/alpha by chi, but both grow at least like 3^(omega_s).
None of these saves a positive power of Lambda over kappa_T on squarefree T with many split primes.

PROPOSITION 3 (lacunarity barrier; PROVED). For every M there is a set D with at most M elements in every window [X, 2X] and mu(D) = 1/(M+1): D = {m, 2m, ..., Mm}. When |T| is comparable to h, D_T(h) lies in O(1) windows. So no argument that uses only the orbit or window count (chi_orbit_bound Theorem 1, Peres-Schlag) can give alpha_T >> 1/kappa_T in the regime that carries the heavy diagonals.

THEOREM 4 (what Proposition 5 needs; CONDITIONAL on everything Proposition 3 of heavy_diagonals_sharp.md assumes: Theorem N's N-1 and N-3, the listed audits, and Theorem E). Hypothesis H(beta, gamma): for h >= h_F and every diagonal T, 1/alpha_T(h) <= C_F kappa_T^beta Lambda^(-gamma) ell^(C_F). Then m_h <= C h^2 Lambda^(theta(beta,gamma)) ell^C, where
 theta(beta,gamma) = inf_x max{ x, 2-x, 2-x-gamma+Psi, 2-Phi((x+gamma)/beta) },
 Psi = min_{a>=0} [E(a)-1+(beta-a)·(x if a>=beta, else (x+gamma)/beta)].
Without the Bad_split family the bound is inf_x max{x, 2-Phi((x+gamma)/beta)}.
Computed values:
- gamma = 0 (pure power saving), with / without Bad_split: beta = 0.2: 1.028/0.478; beta = 0.5: 1.172/0.991; beta = log_3 2: 1.246/1.157; beta = 0.8: 1.352/1.334; beta = 1: theta* = 1.4967.
- beta = 1 (saving Lambda^gamma over kappa_T): gamma = 0.25: 1.375; 0.5: 1.25; 0.75: 1.125; 0.9: 1.05; 1: 1.000.
- K0 = Lambda^c, needed only on diagonals with kappa_T > Lambda/4: exponent 1 for c <= phi(1) = 0.13508; 1.026 at c = 0.2; 1.140 at 0.5; 1.323 at 1.

COROLLARY 5 (CONDITIONAL as Theorem 4).
(a) (F_avg) is (1/h) sum over T with kappa_T >= Lambda/5 of min(Lambda, 1/alpha_T(h)) <= ell^C. It implies m_h <= C h^2 log h (loglog h)^C, Bad_split included.
(b) H(1,1), which says alpha_T(h) >= c Lambda/(kappa_T ell^C), implies (F_avg).
(c) (F_Omega) is 1/alpha_T(h) <= C(1 + Omega_s(T))^c for all T. It gives Proposition 5's full conclusion: exponent 1 with Bad_split, and (loglog h)^C without it.
So the weakest form Proposition 5 needs is (F_avg), or H(1,1). It needs only the typed finite-window graphs, only on heavy diagonals, and only a saving of log h over the trivial density 1/kappa_T. A constant K0 is not needed.

STATUS (not proved either way):
- (F) with constant K0 is undecided. It is equivalent to chi_f(Gamma^(32)) < infinity. Heuristically it is false: the random-set model gives 1/alpha_T about kappa_T/log h, which is unbounded.
- H(1,1) is undecided. Heuristically it is true, through a single rotation, and the numerics agree, but nothing here proves it.

## Proofs

0. SETTING. G_T[tau] is G_T(h) on the slots i ≡ iota (mod 32) of I_T. Its edges are at distances in D_T(h) ∩ 32Z. In the coordinate j = (i - iota)/32 it is the graph of Cay(Z, D') with D' = (D_T(h) ∩ 32Z)/32, restricted to an interval V of ⌈n_T/32⌉ or ⌊n_T/32⌋ integers. Since every element of D_T(h) is < n_T, max D' <= |V| (A0).

1. PROOF OF PROPOSITION 1.
(a) Let A be periodic and independent, with period P and density alpha. Take a uniform random translate A + t, t in Z/P. Each A + t is independent, and P(x in A + t) = alpha for every x. So chi_f <= 1/alpha. (chi_f is the infimum of 1/p over probability measures on independent sets that cover every vertex with probability >= p.) Conversely, let nu be such a measure with p = 1/k. Then E|I ∩ [0,N)| >= N/k, so some independent J in [0,N) has |J| >= N/k. Put m = max D. The set J + (N+m)Z is independent: two elements of different copies differ by at least N + m - (N-1) = m+1. Its density is >= N/(k(N+m)), which tends to 1/k. So mu >= 1/chi_f, and mu = 1/chi_f.
(b) Lower bound: average |(A+t) ∩ V| over the translates; it equals alpha|V|. Upper bound: let J be independent in V. Then J + (|V| + m)Z is periodic and independent, so |J| <= mu(|V| + m) <= 2 mu |V| by (A0).
(c) Typed versus untyped: an untyped A of density alpha meets some coset 32Z + j with relative density >= alpha, and A ∩ (32Z + j), rescaled, avoids D'. Monotonicity: D_T(h) ⊆ D_T(h+1), because L < h and |d| < n_T are both monotone (n_T is nondecreasing; limit_graph_gamma T1).
(d) Compactness for chi_f in countable graphs. Exhaust G by finite induced subgraphs H_n, each with a measure nu_n on its independent sets with P(v in I) >= 1/k. View the nu_n as measures on {0,1}^V and take a weak-* limit nu. For each edge uv, the event {u, v in I} is clopen and has nu_n-measure 0 once uv lies in H_n, so nu-almost every I is independent. Also nu(v in I) = lim nu_n(v in I) >= 1/k. So chi_f(G) = sup over finite subgraphs.
 - Isomorphism: j -> 32j/T maps Cay(Z, (D_T^inf ∩ 32Z)/32) onto Gamma[(32/T)Z]. This holds by L1 and T2 of limit_graph_gamma: |i - i'| is in D_T^inf iff i/T ~ i'/T in Gamma, and 32(j - j')/T lies in 32Z_(2).
 - For fixed T, D_T(h) increases to D_T^inf, and every finite subgraph of the limit lies in some Cay(Z, D_T(h) ∩ 32Z) with h large.
 - Every finite subgraph of Gamma^(32) lies in Gamma[(32/T)Z] with T the lcm of its denominators, which is odd.
 - Combining these with (a) gives the infima, and Gamma^(32) ⊆ Gamma gives the chain.
(e) Take (p,q) = (64,1): N = 4031, so r1 = pq/(2N) = 32/4031, and 20r^2 + 4r + 1 = (4097/4031)^2. Take (p,q) = (128,1): r2 = 64/16255. In Z with T = 4031·16255, a = T r1 and b = T r2 lie in D_T^inf ∩ 32Z, with v_2(a) = 5 and v_2(b) = 6. Put g = gcd(a,b). The closed walk of b/g steps +a and a/g steps -b has odd length (a+b)/g, so Cay(Z,{a,b}) contains an odd cycle C, and chi_f(C) > 2. The K5 {0, 35, 209, 260, 434}/1045 has odd differences, so it is not in Gamma^(32).

2. PROOF OF PROPOSITION 2. chi_f <= chi. Theorem E (audited) gives chi(Gamma_l) <= 6400, and Cay(Z, D_T^inf) embeds in Gamma_l when omega_s(T) <= 1 (L2, T2). The greedy bound comes from degree <= 2|D ∩ 32Z|. The AKS bound comes from three_term_relations Theorem 2(1), with alpha >= 1/chi. Theorem W and chi_orbit_bound Theorem 2 give 1/alpha <= F_w prod_i K(4 rho_{<i}) and 1/alpha <= C rho_s log rho_s. For squarefree T both are >= c 3^(omega_s), which is kappa_T^(1-o(1)) in the regime |T| comparable to h.

3. PROOF OF PROPOSITION 3. Cay(Z, {m, ..., Mm}) is a disjoint union, over the cosets of mZ, of copies of Cay(Z, {1..M}). That graph contains K_{M+1} on any M+1 consecutive integers, and the residue classes mod M+1 colour it. So mu = 1/(M+1). Each window [X, 2X] holds at most M elements. For |T| comparable to h, every orbit gamma phi^(2k) contributes O(1) elements to D_T(h). So kappa_T and the maximal window count agree up to constants (chi_orbit_bound Theorem 1), and window-count hypotheses allow alpha of order 1/kappa_T.

4. PROOF OF THEOREM 4. This uses the board L***F: L***U of heavy_diagonals_sharp Proposition 3, with B replaced by the width parameter W = ⌈Lambda^x⌉ and with three classes of (T, tau):
 - Light: 4kappa_T + 1 <= W. Use Proposition 3's uniform random proper W-colouring of G_T[tau]. By Proposition 3(b) (audited), P(u, v same class) <= 2/W.
 - F-treatable: not light, and B_T := ⌈3 ell/alpha_T⌉ <= W. Fix a periodic I_T, independent for D', of density alpha_T - o(1). Choose B_T i.i.d. uniform translates; class k is (I_T + t_k) minus the earlier translates, restricted to V. Split each class into K_T = ⌊W/B_T⌋ subclasses by i.i.d. uniform labels.
 - Heavy (H): the rest, sent to the Theorem E blocks of (B9).
 Facts:
 - (i) Classes are G_T-independent subsets of one (T, tau), with at most B_T K_T <= W of them.
 - (ii) A slot is uncovered with probability (1 - alpha_T)^(B_T) <= e^(-3 ell) = Lambda^(-3).
 - (iii) Two distinct slots share a subclass with probability <= 1/K_T <= 2B_T/W, because the labels are independent of the translates.
 - (iv) All choices are independent across (T, tau), hereditary, and made before (l, p).
 These are exactly the facts that heavy_diagonals_sharp Proposition 3's compatibility check (confirmed by its audit) lists as the only ones K1-K10, J6, Theorem IV and Theorem D use. Hence:
 - Bad_split ∩ T has weights rho_T in {2/W, 1/K_T}.
 - Group the T dyadically by rho_T into O(log W) weighted Theorem D groups. Each has rho >= 1/W >= Lambda^(-C'), and each costs C(rho_j |D_j| h Lambda^2 ell^C1 + h^2 ell).
 - The uncovered slots go to Theorem D with rho = Lambda^(-3), at cost O(h^2 Lambda^(-1) ell^C).
 - H costs C h Lambda^2 ell^C per diagonal (Theorem E).
 - The width is 512(4p·16l·W + 4A) = O(h^2 W) (Proposition 4 and J6).
 Total: M <= C h^2 ell^C [W + Lambda^2/W + (Lambda^2/(hW)) ell sum_{T in F} 1/alpha_T + (Lambda^2/h)|H| + Lambda^(-1)] + c0 n_rel tau*(h)^2 + C h^2.
 Under H(beta, gamma):
 - F is contained in {kappa_T > (W-1)/4}, and on F, 1/alpha_T <= C kappa_T^beta Lambda^(-gamma) ell^C.
 - H is contained in {kappa_T^beta > W Lambda^gamma ell^(-C)}.
 - Rankin, using heavy_light Theorem 1(b) (audited): (1/h) sum_T kappa_T^a <= C_a Lambda^(E(a)-1) for each fixed a >= 0. For a >= beta use the lower cut kappa >= Lambda^x/5. For a < beta use the upper cut kappa <= Lambda^((x+gamma)/beta). This gives (1/h) sum_F kappa^beta <= Lambda^(Psi+o(1)).
 - (1/h)|H| <= Lambda^(-Phi((x+gamma)/beta)+o(1)) (Theorem 2's upper bound, audited).
 Taking exponents gives theta(beta, gamma). Without Bad_split, take K_T = 1. A diagonal then needs min(kappa_T + 1, B_T) <= W classes, and only the width and H terms remain.
 Numerics: expo.py and expo2.py evaluate these exact Rankin expressions, with a >= 0 and grids of step 0.001 or 0.0025.
 - Checks: they return theta* = 1.497 at beta = 1, gamma = 0. Rankin's tail equals -phi to 1e-7 at xi = 1.5 and 2. Phi(xi) = 1 at xi = 1.9726.
 - For K0 = Lambda^c, the heavy term is 2 - x - phi(x) + c, with x >= c. At x = 1 this is <= 1 iff c <= phi(1) = 0.135085.

5. PROOF OF COROLLARY 5.
(a) Take W = ⌈Lambda ell^(C_W)⌉.
 - On F, 1/alpha_T <= W/(3 ell), so 1/alpha_T <= ell^(C_W) min(Lambda, 1/alpha_T), and the F term is <= C h^2 Lambda ell^C.
 - H is contained in {kappa_T >= Lambda/5, 1/alpha_T > Lambda/4}. So |H| Lambda/4 <= sum min(Lambda, 1/alpha_T) <= h ell^C, and the H term is <= C h^2 Lambda ell^C.
 - The light term is h^2 Lambda^2/W, and the width is h^2 W ell^C.
(b) sum_T min(Lambda, kappa_T ell^C/Lambda) <= (ell^C/Lambda) sum_T kappa_T <= 2h ell^C, because sum_T kappa_T <= 2h log h (three_term_relations [0], audited).
(c) The tail bound for Omega_s (proved here). Write 10^(Omega_s) = 1 * g, with g(p^e) = 9·10^(e-1) at split p and g = 0 elsewhere. Then
 sum_{n<h} 10^(Omega_s(n)) <= h prod_{p split < h} (1 + 9/(p-10)) <= C h Lambda^(9/2).
 This uses that the least split prime is 11 > 10, and Mertens for p ≡ ±1 (mod 5). By Markov, #{T : Omega_s(T) > 3 ell} <= C h Lambda^(4.5 - 3 ln 10) <= C h Lambda^(-2.4).
 Every other T has 1/alpha_T <= C(1 + 3 ell)^c.
 - With Bad_split, take W = Lambda ell^(C_W). Every such T is light or F-treatable with rho_T <= ell^C/W, so Bad_split costs h^2 Lambda ell^C. The exceptional T cost h^2 Lambda^(-0.4) ell^C through Theorem E.
 - Without Bad_split, take W = 3 ell^(c+2) and K_T = 1. The width is h^2 ell^C.

6. HEURISTIC ASSESSMENT (NOT PROVED; labelled analysis).
- (F) with constant K0 needs 1/alpha_T bounded even on diagonals with kappa_T >> log h. These exist: |T| < 0.124h with omega_s about log h/loglog h, and kappa_T >= 3^(omega_s) by Lemma 1. For a set of kappa random-like integers in [1, N], one rotation achieves density about ln N/(2kappa): each event ||theta d|| < delta has probability 2 delta, and there are about N essentially independent theta. Hoffman's bound gives at most sqrt(ln N/kappa). Either way 1/alpha tends to infinity, so (F) should fail. It should then also fail for Gamma: chi_f(Gamma^(32)) = infinity, and hence chi(Gamma) = infinity.
- The same model gives 1/alpha_T about 2kappa_T/log h, which is H(1,1) and hence exponent 1. Arc colourings would then also give chi(G_T) about kappa_T/log h, the linear total of limit_graph_gamma [9].
- Proving H(1,1) needs a theta that is good for all kappa_T distances at delta = c Lambda/kappa_T, an event of probability about h^(-c). This is the wall described in three_term_relations [8]: it needs the joint behaviour of about log h distances, while the relation counts control three.
- The adelic characters of Theorems A, F and W do not help here: their off-strip cost is (20(w+1))^(w+1). Proposition 3 rules out window-count arguments, and AKS and Shearer give only log kappa.
- Cliques are not the mechanism. In the computed ranges the typed graphs have no triangles, and three-term relations number O(h) in total (three_term_relations Theorem 1).

7. COMPUTATIONS (sanity only; each under 60 s; scripts in scripts_f/).
- dens1.py (finite window, brute-force D_T(h); sampled best rotation over 4·10^5 theta; Z_P greedy for P <= 3001; a control set made by shifting each d by a uniform offset in ±40). Each line gives kappa, |D∩32Z|, rotation density, control rotation density, Z_P greedy density and control:
 - h = 2e6: T = 1045: 105, 2, 0.0565, 0.0614, 0.032, 0.031.
 - h = 2e6: T = 30305: 185, 3, 0.0349, 0.0422, 0.019, 0.020.
 - h = 2e6: T = 187891: 178, 4, 0.0345, 0.0362, 0.021, 0.020.
 - h = 2e7: T = 2066801: 285, 7, 0.0253, 0.0212, 0.014, 0.013.
 - h = 2e7: T = 939455: 433, 12, 0.0143, 0.0154, 0.011, 0.010.
 The arithmetic sets behave like the controls. The sampled values match the sampling-limited prediction ln(4·10^5)/(2kappa).
- rotexact.py (exact best rotation by an interval sweep). kappa·delta* is:
 - 5.40 at T = 6061, h = 6e4 (control 5.14);
 - 6.80 at T = 30305, h = 3e5 (control 6.66);
 - 6.82 at T = 1045, h = 2e6 (control 7.27).
 These exceed ln(kappa) and are about 1.1 to 1.2 times ln(max D)/2. That is consistent with gamma = 1, but at these sizes it cannot separate log h from log kappa.
- clq.py (maximum cliques in D_T^inf ∩ [1, 10^6]): omega = 4 or 5 for T = 55, 1045, 6061, 30305, 187891 and 939455. omega among even distances is <= 3. omega among distances divisible by 32 is 2.
- tri.py (triangles {0, r1, r1+r2} in R_odd, from (p,q) boxes):
 - 1753 triangles untyped with |p|, q <= 40;
 - 68 with 2 | r and 6 with 4 | r, for |p|, q <= 90;
 - 0 with 8 | r for |p|, q <= 90, and 0 with 32 | r for |p|, q <= 260.
- expo.py and expo2.py: the exponent tables of Theorem 4.

## External results used

- de Bruijn-Erdos type compactness, in the fractional form proved inline: weak-* compactness of probability measures on {0,1}^V.
- Mertens' theorem for primes ≡ ±1 (mod 5): sum of 1/p = (1/2) loglog x + O(1). Used in the Omega_s tail bound.
- Repository, audited: Theorem E and Lemma B of gamma_one_split_prime; Theorem W of gamma_two_split_primes_w; L1, L2 and T2 of limit_graph_gamma (through the audits); Lemma 1, Theorem 2 and Proposition 3 of heavy_diagonals_sharp; heavy_light Theorem 1(b); three_term_relations [0] and Theorems 1 and 2; weighted Theorem D and Theorem E as used in Proposition 3.
- Repository, unaudited and cited only as context: chi_orbit_bound Theorems 1 and 2; consolidated_board_v2 Theorem N and its hypotheses N-1 and N-3; round-12 Theorems N1 and U.

## Checks

I re-derived by hand:
- the fractional compactness argument and mu(D) = 1/chi_f;
- the periodization bound behind the factor 2 (A0, max D' <= |V|);
- the isomorphism to Gamma[(32/T)Z];
- the odd cycle from 32/4031 and 64/16255;
- the AP barrier;
- the cost accounting of Theorem 4, term by term, against Proposition 3(c) and (d) and Proposition 5's proof;
- Corollary 5(a) to (c), including the 10^(Omega_s) divisor-sum tail with exponent 4.5 - 3 ln 10 = -2.41.

Scripts (py, each under 60 s and well under 1 GB), all in scripts_f/: dens1.py, rotexact.py, clq.py, tri.py, expo.py, expo2.py.

The exponent scripts reproduce theta* = 1.497 at beta = 1, gamma = 0, and the Rankin tail equals -phi(xi) to 1e-7. The rectangle-blackouts repository was only read, and no web sources were used.

## Gaps

- (F) is neither proved nor refuted. By Proposition 1(d) it is equivalent to chi_f(Gamma^(32)) < infinity (typed) or chi_f(Gamma) < infinity (untyped). Both are open. The heuristic says both fail, and that is not proved.
- H(1,1) and (F_avg), the weakest forms Proposition 5 needs, are not proved. No current tool gives a saving of a positive power of Lambda over 1/kappa_T on squarefree T with many split primes. Proposition 3 shows that window and orbit counts alone cannot give one.
- Theorem 4 and Corollary 5 are conditional on everything Heavy_diagonals_sharp Proposition 3 assumes. That covers Theorem N's N-1 and N-3 (the round-12 Theorem N1 and Theorem U are unaudited), the listed audits and Theorem E. The compatibility of translate-plus-split classes rests on the same four facts that Proposition 3's audited compatibility check lists. I did not re-read J6 or the sea notes line by line.
- The Rankin input (1/h) sum kappa_T^a <= C_a Lambda^(E(a)-1) is used for fractional a in (0,1). I took this from heavy_light Theorem 1(b) as 'each fixed a > 0' and did not re-check that note for fractional exponents.
- The exponent values are computed on grids of step 0.001 to 0.0025 from exact formulas. They are not certified by interval arithmetic.
- The typed lower bound chi_f(Gamma^(32)) > 2 is all that is proved. I did not compute the length of the shortest odd cycle.
- The numerics are lower bounds on alpha only (rotations and Z_P greedy). They cannot separate log kappa from log h at kappa <= 433, and the sampled rotations are sampling-limited. They neither refute (F) nor confirm H(1,1).
- Nothing here is audited. Propositions 1 to 3 and the accounting proof of Theorem 4 were re-derived once, by me.

## Missing estimate

H(1,1), restricted to the typed finite-window graphs of heavy diagonals: for h >= h0 and every diagonal T with kappa_T >= Lambda/4, Cay(Z, (D_T(h) ∩ 32Z)/32) has a periodic independent set of density >= c log h/(kappa_T (loglog h)^C). The averaged form (F_avg) is enough. A single rotation would do: a theta with ||theta d|| >= c log h/kappa_T for every d in D_T(h) ∩ 32Z. In the random model a uniform theta succeeds with probability about h^(-c). Proving this needs near-independence of about log h of the events {||theta d|| < delta} over the S-unit structure of D_T(h). For instance, one could bound the r-term relations sum ±d_i = 0 for r up to log h/loglog h with only C^r loss. Without this, the (F) route stays at theta* = 1.49674. With a saving of only Lambda^gamma, gamma < 1, it gives (3 - gamma)/2 for gamma >= 0.3, between the computed 1.375 at gamma = 0.25 and theta* at gamma = 0.

## Next steps

- Replace (F) in heavy_diagonals_sharp Proposition 5 by (F_avg), or by H(1,1), using Theorem 4 and Corollary 5. Record that a constant K0 is not needed. Record that the K5 says nothing about the typed hypothesis: the typed lower bound is only chi_f(Gamma^(32)) > 2.
- Record in the ledger: (F) with constant K0 iff chi_f(Gamma[32 Z_(2)]) < infinity, and the untyped form iff chi_f(Gamma) < infinity. Record the lacunarity barrier (Proposition 3) so that window-count or Peres-Schlag arguments are not tried for H(1,1).
- Attack H(1,1) through a single rotation. Try to bound the r-term relations among the distances of one diagonal, sum ±d_i = 0 with r up to log h/loglog h, losing only C^r. This would extend three_term_relations Theorem 1, whose method loses 3^r types. Then a Bonferroni or Janson argument at depth r gives delta about r/kappa_T. Depth r about Lambda/ell already gives gamma = 1 - o(1), but the exponent needs ell^C precision, so the loss must be at most C^r.
- Try an averaged version first. (F_avg) needs H(1,1) only for all but h Lambda^(-1) ell^C of the heavy diagonals, so a second moment over T, with theta = a/P chosen per T, may be within reach.
- Test the scaling numerically at larger heights. Enumerate D_T(h) through the ideals of norm T^2 for T comparable to h with 5 to 7 split primes. Compute the exact best rotation with a faster sweep, outside the 60 s limit, and check whether kappa·delta* grows like (log h)/2 or like log kappa.
- Audit Propositions 1 to 3 and the accounting in Theorem 4. The accounting reuses Proposition 3's audited framework with one new class rule, translates plus an independent random split.

