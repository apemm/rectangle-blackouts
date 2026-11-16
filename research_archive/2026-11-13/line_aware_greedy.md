# A line-aware greedy placement for the pair price

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: in a group model, the conflict-free matching theorem of Glock, Joos, Kim, Kuhn and Lichev runs in the regime lambda up to c ln d, which is a price of about Lambda, and every hypothesis holds except two codegree conditions. Both fail for structural reasons: the Pythagorean lines and the near-full columns of label-rooted triangles, which are cliques meeting each label once. Conditional on a weak-codegree version of that theorem (W) and a pointwise codegree bound (IT-w), the price is Lambda (loglog h)^C and the exponent is theta_E(1) = 0.9101. Not audited yet.

# Result

## Status

partial

## Summary

Line-aware greedy for the pair price. Proved: the published conflict-free matching theorem (Glock-Joos-Kim-Kuhn-Lichev, GJKKL) already runs in the 'lambda up to c ln d' regime, which is price about Lambda. Every T1-block hypothesis it needs holds except two codegree conditions, and both of those fail for structural reasons: Proposition 2 lines and the near-full columns of label-rooted triangles. Three-label events cost nothing extra once they are tracked as test systems. Conditional on a weak-codegree version of that theorem (W) and a pointwise codegree bound (IT-w), the price is Lambda (loglog h)^C, so bE = 1 and the exponent is theta_E(1) = 0.9101 under Theorem P with DC. No price below Lambda^2 is proved. In a toy, random greedy follows the line-product law within 5%.

## Statements

SETTING. A T1-type relocation block (pair_families Statement 0 setting): label set Z, n = |Z|, slots 7j for j in [0, N), N = m n (m is the price), event system E with |J| = 2, 3, 4, coincidences included. Lambda = 1 + log h, ell = 1 + loglog 3h. An option is a pair o = (e, j). D(o) is the number of pair conflicts of o. In a Theorem E class block C_w, D(o) <= n_w + B(w) and B(w) <= C n_w ell^C (Lambda^2 + w Lambda) (T2 (10), (E2), audited). mu_ef <= G_max = h^(o(1)) (polylog (D3)). M0 is the largest number of labels sharing a row (M0 <= Delta). K(o, j') is the number of labels f with (f, j') adjacent to o (the column count).

PROPOSITION 1 (validity and bookkeeping; PROVED). (a) Take any procedure that places a set Z' injectively, avoids every two-label event, and then deletes one label from each realized three- or four-label event. Its output avoids every E_J, so by Statement 0 the layout is valid. (b) Take a block method of price m whose leftover fraction is at most 1/ell^C per round. Run it for O(ell) rounds, then send the final leftover (at most Lambda^(-2) n labels) to the old Lambda^2 ell^C method. The total width is at most 2 m n + C n ell^C + O(ell^2 h^2).

PROPOSITION 2 (group model; PROVED). Cut [0, N) into n groups of m consecutive slots. For each label e and group g, choose a position r(e, g) uniformly at random and independently, so the option (e, g) is the slot g m + r(e, g). Let H = K_{n,n} (labels x groups), let d = n, and let C be the set of pairs of options in distinct groups that form a two-label event. Then:
- H is a simple, n-regular 2-graph with Delta_2(H) = 1.
- A C-free matching is an injective placement that avoids all pair events, coincidences included.
- With probability 1 - o(1): Delta(C^(2)) <= (1 + o(1)) max_o D(o)/m + O(log n), so GJKKL's (C2) holds with Gamma = (1 + o(1)) max_o D(o)/(m n). (C3) is void. (C4) holds at label vertices, with bound G_max.
GJKKL Theorem 3.1 needs mu^(-ell' Gamma) <= d^(eps^2), where ell' = 3 for triples. So the class-w price this theorem would deliver is m_w = C_eps ell^C (Lambda + w) ln(1/mu). That is the 'lambda < c ln N' heuristic, in published form.

THEOREM 3 (the published theorem does not apply; PROVED). In the group model with m <= c n^eps:
(a) (C5) fails. Some option o has, on its (3,4)-line, an assigned option o' in another group such that o and o' have at least n/(4m) - m - 2 common C-neighbours. More generally, for any option sets of size d per label and any line direction of row step sigma_y, some line carries at least about 7d/(sigma_y m) options of distinct labels.
(b) (C4) fails at group vertices. Let e be a label whose odd row lies above the block median, and let o = (e, j) sit in the last position of its group. Then at least c n/m assigned options in the next group conflict with o. The conflicts are label-rooted tilted right angles: e's point, f's point at column offset 7, and a high-sea point at offset -(c - a)(H - a)/7.
(c) Both violating sets are cliques that meet each label's options at most once. Their relative weight is Theta(1/m): polylogarithmic, not polynomial. Suppose instead the long-line events (row step at most n^eps/(2m)) are left out of C and deleted afterwards. Their incident weight is at least c eps^2 Lambda^2/m per label. So any placement with near-independent pair statistics realizes that many per label, and the method falls back to price c eps^2 Lambda^2.

LEMMA 4 (three-label events as a test system; PROVED from higher_arity Lemma 0, Theorem 1 and Proposition 3, which are unaudited). Let Z_3 be the set of three-label events among assigned options that contain no pair event. Then Z_3 satisfies (Z1) |Z_3| >= n^(3+eps) (for rich Z), (Z2) and (Z4). The close-label codegree U Lambda/t is at most U h^(o(1))/m pointwise, while (Z2) allows n^(2-eps) Lambda^2/m^2. Only (Z3) remains, and (Z3) is the same condition as (C5).

LEMMA 5 (exact line loads; PROVED). Replace E by its cyclic closure modulo N. This adds constraints only and does not raise any option's degree above max_o D(o). In random-order greedy, P(line l used by step t) = (1/N) * sum over the labels f on l of P(f placed by step t). This is exact, and it is at most s_l t/N. In particular, the coincidence line gives a factor (1 - t n/N) exactly.

LEMMA 6 (column counts; PROVED except where noted). For X = 7(j' - j) != 0:
- Lemma F, vertical rivals, two-sea supports R1 and nonhorizontal R3: K(o, j') <= 8 M0 max over w in W_S of tau(|X^2 - w^2|) = M0 h^(o(1)). Here W_S is the set of sea row differences, and X = +-w is impossible because 7 | X and no sea row difference is 0 mod 7.
- R2 supports: K(o, j') <= C M0 h^(3/4). This uses Bombieri-Pila (cited from memory, not re-read).
- Label-rooted triangles: K(o, j + t) <= sum over the six private differences P = s - r of M0 (h gcd(t, P)/(7t) + 1).
- One-sea roles and lone-point triangles: K(o, j') <= C M0.

HYPOTHESIS W (weak-codegree conflict-free matching; OPEN). GJKKL Theorems 3.1 and 3.2 hold with (C4), (C5) and (Z3) weakened to the bound d/K, for some K = K(d) tending to infinity, and with the error d^(-eps/900) replaced by o(1).

HYPOTHESIS IT-w (pointwise codegree; OPEN). For every two options o1, o2 of distinct labels in distinct groups of a Theorem E class block, the number of slot-options adjacent to both is at most N/K. Lines (at most n/2 each) and label-rooted columns (at most C n w (1 + ln m)^2) already satisfy this. The open part is the cross-direction part. The trivial y-sum bound n Lambda^2 h^(o(1)) misses N/K by a factor of about Lambda K.

THEOREM 7 (conditional price; PROVED conditional on W, IT-w, an arithmetic-progression class-count input (AP) in Lemma 6, and the unaudited higher_arity inputs). Every Theorem E instance on Delta diagonals can be built with all of N1 (a)-(f) at width C Delta h Lambda ell^C + C h^2 ell^2 ln Lambda. So (PE) holds with bE = 1 + o(1). The higher-arity part costs C Delta h Lambda ell^(3/2), the same as higher_arity Theorem 4. Under Theorem P (unaudited), the exponent is theta_E(1) = 0.9101 with DC, and 1.0000 with Bad_split and bD = 2.

PRICE PROVED: none below Lambda^2 ell^C. PRICE CONDITIONAL: Lambda ell^C.

## Proofs

0. WHAT THE ROUTE NEEDS.
The target is a semi-random placement inside one class block that pays about Lambda per label for every pair family at once. By Statement 0 only the slot assignment changes, so validity reduces to two facts: the centre map is injective, and it avoids every E_J. The published tool closest to the heuristic is the conflict-free hypergraph matching theorem of Glock, Joos, Kim, Kuhn and Lichev (GJKKL, arXiv 2205.05564; hypotheses below). Its conflict degree may reach Gamma d^(j-1), with mu^(-ell Gamma) <= d^(eps^2). That is exactly the 'lambda up to c ln d' tolerance: price about Lambda. So I set the block up as a GJKKL instance, checked each hypothesis, and isolated what fails.

1. PROPOSITION 1.
(a) By Lemma RL, E_J depends only on X restricted to J, with every other slot empty. Suppose the final survivors contain a set J that realizes E_J. Then the original placement realized E_J too. If |J| = 2, that contradicts pair-freeness. If |J| >= 3, one label of J was deleted, so J is not contained in the survivors. Injectivity is preserved under deletion. Statement 0 then gives the layout.
(b) Each round re-places its leftover in a fresh block of the same type, flanked by its own c' h^2 separation. Upper bounds on degrees and incident sums pass to subsets of a class, so the same parameters apply. After k = O(ell) rounds with leftover fraction at most ell^(-C), the leftover is at most n Lambda^(-2), because ln(Lambda^2)/ln(ell^C) = O(ell/C). Those labels go to the old method at Lambda^2 ell^C each, which is n ell^C in total. The separations cost O(ell) rounds times O(ell) class blocks times c' h^2.

2. PROPOSITION 2.
The structure of H is immediate. Two chosen options never share a group, so they never share a slot: coincidences are absorbed by the group vertices.
Fix e, g and r(e, g), so o is fixed. The number of C-partners of o is a sum over (f, g'), with g' != g, of independent indicators 1{r(f, g') in R_(f,g')(o)}. Here R_(f,g')(o) is the set of conflicting positions, and |R_(f,g')(o)|/m has total sum at most D(o)/m.
- Chernoff with a union bound over the n^2 m triples (e, g, r) gives the bound on Delta(C^(2)). Here D(o)/m >= n Lambda^2 c/m >> log n.
- At a label vertex f, the partners of o are at most the conflicting slots of f, which number mu_ef <= G_max.
- With max D(o) <= n_w ell^C (Lambda^2 + w Lambda), Gamma = ell^C (Lambda^2 + w Lambda)/m_w (1 + o(1)).
- The GJKKL condition with ell' = 3 and mu = Lambda^(-2) reads m_w >= (6/eps^2) ell^C (Lambda^2 + w Lambda) ln Lambda/ln n_w. Since ln n_w >= Lambda/2 for main classes, this is m_w = C_eps ell^(C+1) (Lambda + w).

3. THEOREM 3.
(a) Take an interior option o = (e, j), with e in the more popular class mod 28. By Theorem C (C2) and Proposition 2, its (3,4)-line holds the options (f, j + 3(c_f - a)/28) of at least n/2 - 1 labels, and every pair on the line is a genuine Lemma F event. The position of each f is assigned independently with probability 1/m, so with probability 1 - o(1) at least n/(3m) of these options are assigned. Pick one of them, o', in a different group. Every other assigned option on the line in a third group is a C-neighbour of both o and o'. At most 2(m/3 + 1) line options share a group with o or o', which leaves at least n/(4m) - m - 2 common neighbours. Since d = n, (C5) asks for at most n^(1-eps), which fails once n^eps > 5m.
General option sets: the lines of direction (sigma_x, sigma_y) that meet the strip number at most N + |sigma_x| h/sigma_y + 1 <= 2N. They carry at least (14n/sigma_y) d (1 - o(1)) options of the popular class. Some line therefore carries at least the average 7d/(sigma_y m). Cauchy-Schwarz is not even needed.
(b) Let A = (x, a) be e's odd point and C = (x + 7, c) f's odd point, with c = a mod 14, so (c - a)/7 = kappa is even. Put S = (x + X_S, H) with 7 X_S + (c - a)(H - a) = 0, so the angle at A is right. Then X_S = -kappa (H - a) mod 7, and H - a != 0 mod 7 (normalized residues 1 and 0). As kappa mod 7 runs over the residues, X_S lands on a nonzero square, which is a high-sea column, for 3 of the 7 classes.
Further checks:
- The fourth corner has row c + H - a, which lies in [1, h] when c <= a - (h - H).
- Both legs are tilted.
- S is a sea point in a non-slot column, so it is present in every configuration.
- |X_S| <= h^2/7, so S lies in the block or its separation.
- T2 Section 2 forbids every three-black tilted rectangle that is not rooted at a high sea point. This one is rooted at a label point, so it is a two-label event of E. It is the Q w Lambda M(w) role of T2 Section 4.
So at least (3/7 - o(1)) #{f : c_f < a - O(1)} >= c n labels conflict with o at slot j + 1 when e's row is above the median. Let o sit in the last position of group g. Each such f has its group-(g+1) option at slot j + 1 with probability 1/m, independently, so Chernoff gives at least c n/(2m) of them. These all contain the vertex g + 1, and (C4) allows at most n^(1-eps).
(c) A line meets each label once (Proposition 2), and the options through a group vertex pairwise share that vertex, so both sets are cliques that meet each label's options at most once. Their relative size is Theta(1/(sigma_y m)) for lines and Theta(1/m) for columns, never d^(-eps). For the deletion claim, restrict the sum in Theorem R(iv) to coprime (r, s) with rs <= Q = n^eps/(28m). The row step 14 rs is then below n^eps/(2m), which are exactly the lines with assigned load above d^(1-eps). The same computation (with R1, R2 >= Q) gives a sum of 1/(rs) of at least c (ln Q)^2. So the incident weight of these events is at least c |Z| (ln Q)^2/W >= c' eps^2 Lambda^2/m per label, using ln n >= Lambda/2. A placement whose pair statistics match i.i.d. slots up to a factor of 2 realizes half of this in expectation, which is what GJKKL Theorem 3.2 would give for the 2-uniform test system of these events. Deleting them is then affordable only when m >= c eps^2 Lambda^2.

4. LEMMA 4.
- Lemma 0 (higher_arity): every k = 3 event is of type T3, M, Hz or S6.
- Pointwise codegree. Fix two options and a third label g. A T3 event with the vertex at e or f fixes X_g through X_g X_B = -u1 u2, so at most 1 value per role. With the vertex at g, the Thales condition is quadratic in x_g, so at most 2. An M event with the side {e, f} has (P) linear and (N) quadratic in the remaining columns, so at most 2. An M event with the side {e, g} has (P) fixing the sea column as a function of X; then (N) is a polynomial of bounded degree in X (at most 4 roots), or it vanishes identically and X | yz leaves at most tau(yz) values. Hz and S6 give h^(o(1)). So there are at most U h^(o(1)) slot completions, and at most U h^(o(1))/m + O(log n) assigned ones by Chernoff.
- Per option. The number of triples through one slot-option is at most I_3(e) <= C n^2 (ell Lambda^2 + w Lambda) + C U h Lambda^2 (Theorem 1, unclassed form, U ~ n). No randomness is needed.
- Size. E|Z_3| = (n^2/3)(average triple degree)/m^2 >= c n^4 Lambda^2/m^2 by Proposition 3 (rich Z). Chebyshev gives concentration, because the variance is dominated by pairs sharing an option.
- Hence (Z1): n^4 Lambda^2/m^2 >= n^(3+eps). (Z2) with j' = 1: n^2 Lambda^2 ell <= n^(3-eps) Lambda^2/m^2. (Z2) with j' = 2: U h^(o(1))/m <= n^(2-eps) Lambda^2/m^2. (Z4) holds by removing the events that contain a pair event, which a C-free matching avoids anyway.
- (Z3) requires |N(e) ∩ N(f)| <= d^(1-eps) for e, f in a common test set, which is (C5) again.
- The close-label codegree U Lambda/t of higher_arity Remark 7 is an average over (f, t). Pointwise it is at most U h^(o(1)), far below the n^(2-eps) that (Z2) allows. It only breaks (C3) when triples are put into C, so they should not be put there.

5. LEMMA 5.
- Each real event is a relation x_f - x_e in D_ef with both ends in [0, N). The cyclic event x_f - x_e = d mod N contains it, and adds only the wrap-around pairs. Each option has exactly one f-slot per d in D_ef, so its degree is sum over f of |D_ef| <= max_o D(o). Triples close up the same way.
- The cyclic system, a uniformly random label order and uniform choice among free slots are all invariant under j -> j + 1. So P(f placed at j by step t) = P(f placed by step t)/N.
- A line holds at most one placed option, because the output is valid. So 1{l used} = sum over (f, j) on l of 1{f at j}, and taking expectations gives the identity.
- The line-product law is the unproved statement that these line factors multiply over the lines and columns through o. With line loads s/N <= 1/(2m), it gives a free fraction exp(-lambda t (1 + O(1/m))).

6. LEMMA 6.
- Lemma F and vertical rivals: X^2 + y^2 = L^2 with X fixed gives y = (u - v)/2 with uv = X^2, so at most 2 tau(X^2) values of y. Multiply by 2 parities and M0 labels per row.
- R1 (side = two labels, diagonal = two seas): (N) is X^2 + y^2 = xi^2 + w^2, so (y - xi)(y + xi) = w^2 - X^2 != 0. That leaves at most 2 tau(|w^2 - X^2|) values of y; (P) then only fixes the sum of the sea columns.
- R3 (side = two seas, diagonal = two labels): same, with xi^2 = X^2 + y^2 - w^2. The horizontal case w = 0 is Lemma F.
- The exclusion X = +-w: all sea row differences t - s with s != t have normalized residue 3, 1 or 2 mod 7 (T2 Section 1), while 7 | X.
- R2 (side = label point A = (0, a) and sea B = (u, s); diagonal = label point (X, c) and sea (v, t)):
 - (P) reads u(X + v - u) = -A0 (c - c0), with A0 = s - a != 0 and c0 = a + s - t. The case c = c0 forces u = 0 (a vertical side, excluded) or v = u - X, and (N) is then linear in u.
 - Otherwise write u kappa = A0 (c - c0). (N) becomes the quartic F(u, kappa) = 2 A0^2 u (2X + kappa) - A0^2 (2X + kappa)^2 - (A0 (t - c0) - u kappa)^2 + A0^4 = 0.
 - F is quadratic in u with leading coefficient kappa^2 (linear with coefficient 4 A0^2 X != 0 when kappa = 0). F is quadratic in kappa with leading coefficient A0^2 + u^2 != 0. The u^2 kappa^2 term survives on every line u = lambda kappa + nu. So F has no linear component, and each component has degree at least 2.
 - The constraint is |u kappa| <= 2 |A0| h. If |u| <= h^(3/4) or |kappa| <= h^(3/4), there are at most 2 values of the other coordinate each, so O(h^(3/4)) points. Otherwise both |u| and |kappa| are below 2h^(5/4). Bombieri-Pila applied to each of the at most 4 components gives O(h^(5/8 + eps)).
 - So K <= C M0 h^(3/4).
- Label-rooted triangles with the vertex at e: 7t | (c - a)(s - a), with 7 | c - a, forces c = a mod t/gcd(t, s - a). Count rows in [1, h]. With the vertex at f, the condition is a quadratic congruence in c with roots a and s, which has at most 2^(omega(t)+1) gcd(t, (s - a)^2)^(1/2) roots. Its window sums are of the same order.
- Group loads: (1/m) sum over t <= m of K_w(o, j + t) <= C n_w w (1 + ln m)^2/m. This needs (AP), #{f in Z_w : c_f = a mod q} <= C tau(q)^C n_w/q + C M0 h^(1/2) for q <= m. That is an elementary divisor sum in progressions, sketched but not written out.

7. THEOREM 7.
Run the Proposition 2 instance per class C_w with w <= Lambda^2, mu = Lambda^(-2) and m_w = C_eps ell^C (Lambda + w).
(a) Hypotheses of W.
- (C1)-(C3) and the label-vertex part of (C4): Proposition 2.
- Group-vertex part of (C4): Lemma 6 gives a load of at most n_w C w (1 + ln m)^2/m_w = n_w/K with K >= ell^(C - 3).
- (C5) and (Z3): lines contribute at most n/(2m) after Chernoff, columns at most C n w (1 + ln m)^2/m, and the rest is IT-w.
- Z_3: Lemma 4.
- Four-label events: by higher_arity Theorem 2 their expected number is n h^(-1+o(1))/m^3. Their test-system padding for (Z1) is not verified (see Gaps).
(b) W then gives a C-free matching covering (1 - Lambda^(-2)) n_w labels with near-independent triple counts. Realized triples number at most (1 + o(1)) |Z_3| n_w^(-3) <= C I_3^max/(m_w^2 n_w).
- Enlarge m_w by H(w)/n_w ell^(C/2), with H(w) from higher_arity Theorem 4. The deletion fraction is then at most ell^(-C).
- Since the sum over w of H(w) is at most C (Delta h Lambda ell^(3/2) + h^2), the higher-arity part costs Lambda ell^(3/2) per label.
(c) Proposition 1(b) re-places the deleted and leftover labels.
(d) Weights above Lambda^2 hold at most C Delta h Lambda^3/w^2 labels each (from (E1) and (E5)). Placing them by the old method costs at most C Delta h ell^C/Lambda in total.
(e) Summing m_w n_w over w gives C_eps ell^C (Lambda * sum of n_w + sum over e of v(e)) <= C Delta h Lambda ell^C, using (D4).
(f) N1 (a)-(f) hold by Statement 0. Classes with n_w < h^(1/2) number O(ell) and are harmless by the relocation rule. Theorem P with bE = 1 then gives the exponents stated.

8. NUMERICS (sanity check only).
The toy has n labels on rows 0, ..., n-1, N cyclic slots, and conflicts dj^2 + dr^2 = square, plus coincidences. This is the toy of pair_families, with D/n of about 4.5. The scripts are toy_greedy.py and toy_curve.py in the script folder, and each run took under 11 s.
- Random greedy succeeded at n = 1000, N = 1400 (D/N = 3.59) and N = 2000 (D/N = 2.90) in 3 trials of 3, and at N = 1100 (D/N = 4.09) in 1 trial of 3. The first-moment method needs N > D.
- At n = 1000, N = 1200 (lambda = 3.92, coincidence part n/N = 0.83), the observed free fraction against the line-product prediction (1 - tau n/N) exp(-tau (lambda - n/N)) was:

| tau | observed | prediction |
| --- | --- | --- |
| 0.05 | 0.826 | 0.821 |
| 0.25 | 0.370 | 0.366 |
| 0.45 | 0.152 | 0.156 |
| 0.65 | 0.062 | 0.062 |
| 0.85 | 0.0188 | 0.0213 |
| 0.95 | 0.0106 | 0.0112 |

- The naive exp(-lambda tau) misses by a factor of 2 at the end. Exactly the coincidence line (s/N = 0.83) accounts for that, as Lemma 5 predicts. In real blocks s/N <= 1/(2m), so the distinction disappears.

## External results used

- Glock, Joos, Kim, Kuhn, Lichev, 'Conflict-free hypergraph matchings', arXiv:2205.05564, Theorem 3.1. Quantifiers: for k >= 2 there is eps0; for eps < eps0 there is d0; for d >= d0, any integer ell >= 2 and reals Gamma >= 1, mu in (0, 1/ell] with mu^(-Gamma ell) <= d^(eps^2). Hypotheses: H is a k-graph on n <= exp(d^(eps^2/ell)) vertices with (1 - d^(-eps)) d <= delta(H) <= Delta(H) <= d and Delta_2(H) <= d^(1-eps), and C is (d, ell, Gamma, eps)-bounded. Bounded means: (C1) 2 <= |C| <= ell; (C2) sum over j of Delta(C^(j))/d^(j-1) <= Gamma, and at most Gamma uniformities occur; (C3) Delta_j'(C^(j)) <= d^(j-j'-eps); (C4) for each edge e and vertex v, at most d^(1-eps) 2-conflict partners of e contain v; (C5) |N(e) ∩ N(f)| <= d^(1-eps) for disjoint e, f. Conclusion: a C-free matching of size (1 - mu) n/k. Theorem 3.2 adds test systems Z (sets of matchings) with (Z1) |Z| >= d^(j+eps), (Z2) Delta_j'(Z) <= |Z|/d^(j'+eps), (Z3) |C_e^(j') ∩ C_f^(j')| <= d^(j'-eps) for e, f in a common test set, (Z4) each test set C-free. Its conclusion is that the number of test sets inside the matching is (1 +- d^(-eps/900)) (|M|/|H|)^j |Z|. Read from the arXiv HTML through a summarising tool.
- Bombieri and Pila, Duke Math. J. 59 (1989), Theorem 5, as I recall it (not re-read): an irreducible algebraic curve of degree d >= 2 has at most c(d, eps) T^(1/d + eps) integer points in a square of side T. Used only for the R2 column bound.
- Chernoff bounds for sums of independent indicators, and Chebyshev's inequality.
- Repository inputs: T2 (10) and Section 2 (audited); Theorem E (E1), (E2) and (E5); Theorem R(iv) and its audit; Proposition 2 and Theorem C of pair_families (unaudited); Lemma 0, Theorems 1, 2 and 4, and Proposition 3 of higher_arity (unaudited); Statement 0 and Lemma RL of block_layout_n1 with its audit patch; Theorem P of relocation_price_exponent (unaudited).

## Checks

Read in full: pair_families_dp_colouring.md, higher_arity_true_counts.md, relocation_price_floor.md, audit_relocation_price_floor.md, t1_cost_decomposition.md, relocation_price_exponent.md, safe_triangle_pair_first_moment.md (T2), safe_triangle_pair_third_audit.md and safe_triangle_first_moment_independent_audit.md. Web: arXiv 2205.05564 (GJKKL), HTML version, through a summarising fetch tool, not a line-by-line read. I took (C1)-(C5), (Z1)-(Z4) and the quantifiers of Theorems 3.1 and 3.2 from fetched quotations, so a line-by-line re-read is still owed. By hand: Theorem 3(a) and (b), including the mod-7 residue check for the label-rooted triangle; Lemma 4's pointwise codegree roles; the Lemma 6 algebra, including the claim that the R2 quartic has no linear factor; and the Lemma 5 symmetry argument. Scripts (py, script folder only, each run under 11 s): toy_greedy.py and toy_curve.py. The repository was only read, and no git command was run.

## Gaps

- Hypothesis W (GJKKL with (C4), (C5) and (Z3) weakened to d/K for K tending to infinity) is unproved. Theorem 3 shows why the published version cannot be used: the violations have polylogarithmic size by structure. The GJKKL proof absorbs error amplification of order e^(O(Gamma)) = d^(O(eps^2)) using d^(-eps) precision, so polylogarithmic codegree errors do not go through that proof. A proof of W probably needs the clique structure (each line or group star meets each label once) built into the tracked trajectory, and not left as error.
- IT-w (pointwise codegree at most N/K for all disjoint option pairs) is unproved for cross-direction pairs. The trivial y-sum bound gives n Lambda^2 h^(o(1)), which misses by a factor of about Lambda K. The pair_families averaged estimate (IT) is neither necessary nor sufficient here: a maximum over pairs is needed.
- Lemma 6 for heavy weight classes uses an arithmetic-progression class-count input (AP). It is sketched as an elementary divisor sum in progressions, not written out. The R2 column bound cites Bombieri-Pila (Duke 1989, Theorem 5) from memory, without re-reading the exact hypotheses (irreducibility over R or over C, uniformity of the constant in the coefficients).
- Four-label events are not verified as a trackable test system. (Z1) needs |Z_4| >= n^(4+eps), and only an upper bound on 4-events is available. Padding with an auxiliary family, or putting them into C^(4), needs pointwise codegree bounds that I did not check for every role. Their expected number is negligible (higher_arity Theorem 2).
- Lemma 4 relies on higher_arity Lemma 0, Theorem 1 and Proposition 3, which are unaudited. (Z1) for non-rich class blocks is not checked.
- Theorem 3(c), the deletion claim, is a statement about placements with near-independent pair statistics. That is the method of GJKKL Theorem 3.2, not every placement.
- The heuristic that the free fraction stays near e^(-lambda t) is not proved. Only the exact per-line identity (Lemma 5) is proved. Independence across lines and columns is supported by the toy (agreement within 5%) at tiny Lambda, with one parity and no profile.
- Theorem 7 inherits every open item of Theorem N v3 ((H1) for the 13 notes read only in part, plus the minor fixes) and of Theorem P (unaudited, and DC is unaudited). Nothing in this note has been audited.

## Missing estimate

Two inputs, both about codegrees at polylogarithmic (not polynomial) strength.
(1) Hypothesis W, a semi-random theorem: an almost-perfect conflict-free matching in a d-regular k-graph with 2-conflict degree at most Gamma d and Gamma <= c ln d/ln(1/mu), when the codegree conditions (C4), (C5) and (Z3) hold only in the form d/K. In the application, every large common neighbourhood is a union of cliques that meet each label once: the Proposition 2 lines and the group stars. Those cliques carry relative weight O(1/(sigma_y m)) and O(w (ln m)^2/m).
(2) IT-w: for two options of distinct labels in distinct groups of a Theorem E class block, the number of slot-options adjacent to both is at most N/K. Lines and label-rooted columns already satisfy this. The missing part is the cross-direction (genus-1) part, which needs a saving of a factor of about Lambda over the trivial y-sum bound n Lambda^2 h^(o(1)).
Given (1) and (2), the price is Lambda ell^C and the exponent is theta_E(1) = 0.9101 (with DC).

## Next steps

- Audit Theorem 3. It is the robust negative finding: the published conflict-free matching theorem cannot lower beta, because (3,4)-lines break (C5) and adjacent-column label-rooted triangles break (C4). Check part (b) against T2 Section 2: the high-column residues are the nonzero squares mod 7, and the fourth-corner row condition.
- Prove IT-w for pure Lemma F pairs first. Bound #{y : S(y) ∩ (dx + S(y - dy)) is nonempty} by h^(1-c), or at least by h/Lambda^2, uniformly in (dx, dy). Here S(y) = {X : X^2 + y^2 is a square}. A possible route is the parametrisation X = (y^2/u - u)/2 together with Bombieri-Pila on the resulting curves.
- Attempt Hypothesis W in the special clique-structured form: a nibble that tracks, for each alive option, the line and group-star loads as part of the trajectory (Lemma 5 gives each line factor exactly), with the polynomial-precision GJKKL analysis kept for the non-clique remainder.
- Write out (AP) and re-read Bombieri-Pila Theorem 5 to close Lemma 6.
- Larger toy runs with both parities and a real T2 profile: check the line-product law and greedy success at D/N up to about 0.5 ln N.

