# Polylog-cost relocation for diluted label sets

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: T1 cost scales with the diagonals touched, not with the labels placed. For label sets diluted independently across diagonals the cost is rho |D| h log^2 h (loglog h)^C + h^2 loglog h. With it, family IV is handled by a random class split, giving m_h <= C h^2 (log h)^1.5 (loglog h)^C, conditional on the rest of L** and on an AP form (AP) of Henriot. Not audited yet.

# Result

## Status

partial

## Summary

A polylog relocation rule exists for diluted label sets, not for arbitrary sets. With it, family IV is handled without any colouring of R_IV, which gives m_h <= C h^2 (log h)^1.5 (loglog h)^C. This is conditional on L** minus (O1) and on one AP form of Henriot. For arbitrary Y, the best bound I can prove is n Lambda^6.5 + h^2 Lambda^1.5.

## Statements

NOTATION. Q = floor(h^2/4), Lambda = 1 + log h, ell = 1 + loglog(3h). Here R(Y) is the least width of a violation-free block that carries exactly the labels of Y as doubles, has constant row-h tails, and can be glued by J5. "T1-exceptional" means the O(h^1.5) labels with an exceptional row in some profile. Those labels always go to Proposition partial.

ANSWER TO THE SCALING QUESTION. T1's cost does not scale with the number n of labels placed. Theorem E scales with |D| h, where |D| is the number of diagonals touched: (E1) and (E2) are complete sums over i on each touched diagonal. For an arbitrary Y, nothing in T1 gives a bound linear in n. Lemma M4 shows the method itself cannot give n Lambda^2 + h^2 ell^C. The right measures are the following:
- |D(Y)| h for any Y (Lemma M1);
- rho |D| h for sets diluted independently across diagonals (Theorem D);
- for an arbitrary Y, only n Lambda^a + h^2 Lambda^b with a about 6.5 at b = 1.5 (Theorem H).

LEMMA M1 (monotone form; PROVED modulo audited Theorem E). If Y is a set of non-exceptional labels on a set D of diagonals, then R(Y) <= C(|D| h Lambda^2 ell^C1 + h^2 ell).

THEOREM D (dilution; PROVED modulo audited Theorem E and the T1/T2 inputs; the weighted form needs (AP)). Let D be a set of diagonals and S the non-exceptional labels on D. Let Y be a random subset of S with:
- (i) independence across diagonals: the sets Y ∩ T for T in D are mutually independent;
- (ii) P(f in Y) <= rho for every f, with rho >= (log h)^(-C').
Then, with probability at least 1/2, some set E ⊂ Y with |E| <= h^(2-eps) has
 R(Y \ E) <= C(rho |D| h Lambda^2 ell^C1 + h^2 ell),
and E goes to Proposition partial at cost h^(2-eps+o(1)).
WEIGHTED FORM. Suppose instead P(f in Y) <= rho sum_{q in Q_T} c_q 1[q | u_f], with every q <= h^(1/2), and kappa := sup_T sum_q c_q tau(q)^C/q. Then the same holds with rho kappa in place of rho, provided (AP) holds.
(AP) [HYPOTHESIS; it should follow from Henriot Cor. 2 by substitution, but I have not written it out or had it audited]: the one-variable s-moments of T2 (7) and the box second moment of sharper_polylogarithmic_threshold (2) still hold when label variables are restricted to i = i0 (mod q), q <= h^(1/2), at an extra factor C tau(q)^C ell^C/q per restricted variable.

LEMMA IV (structure of R_IV^(4); PROVED, elementary). For lambda = (al, be) put g = gcd(F, be - al). Then g divides 5, and q_lambda, p_lambda >= al be^2/5. Consequences:
- R_IV has at most C X edges on [1, X];
- sum over lambda of tau(q_lambda)^C/q_lambda and of tau(p_lambda)^C/p_lambda is finite;
- the labels touched by edges with max(p_lambda, q_lambda) > h^(1/2) number O(h^(2-1/6) log h).

THEOREM IV (family IV with no colouring of R_IV; CONDITIONAL). Change board L** as follows. Drop (O1) and the psi split. On each light diagonal T with c_T greedy G_T classes, split every class at random into K_T = floor(B/c_T) subclasses with iid uniform colours psi_T(u). Send the labels with a monochromatic small-lambda R_IV edge inside their subclass to Theorem D blocks, grouped by c_T in [2^(j-1), 2^j). Send the labels touched by large-lambda edges to Proposition partial. Assume (O2), (O3), (U1) to (U3) and (AP). Then the board is valid and
 M <= C(B h^2 + h^2 Lambda^(E+1) B^(-a) ell^C1 + h^2 Lambda^3 ell^C1/B + h^2 ell^2).
With B = (log h)^1.5 and a = 0.91 this gives m_h <= C h^2 (log h)^1.5 (loglog h)^C1. That beats T1 and loses only 0.0033 against the 1.4967 that L** gets with (O1).
- If R_FF (oo and ee) satisfies (FF): the sum over admissible ratios v0/u0 of tau(max(u0,v0))^C/max(u0,v0) is finite. Then the same split also removes (O3)(iii-b) at the same exponent.
- A within-class family with load (log h)^c per label and the same summable dilation structure costs exponent 1.5 + c/2.

THEOREM H (arbitrary Y; PROVED inequalities, exponent from a numerical optimisation over the free parameters). For any set Y of n non-exceptional labels:
 R(Y) <= C ell^C (n Lambda^(a(b)) + h^2 Lambda^b + h^2),
with a(1.5) about 6.5 and a(0) about 8.3.
LEMMA M4 (limit of the method; heuristic, a statement about the method only). With fixed T1 profiles, the local-lemma placement needs a >= 1 + 2e ln 2 = 4.77 at b = 0 and a >= 3.48 at b = 1.5 for some Y. So no version of T1 gives n Lambda^2 + h^2 ell^C for arbitrary sets.

WHICH LOADS ARE ABSORBED IN B h^2 (B = Lambda^1.4967):
- (a) Any family whose hit set is diluted in the Theorem D sense and hits n <= h^2 B/(Lambda^2 ell^C) = h^2/Lambda^0.5033 labels. This is the "O(h^2/Lambda^0.51)" of the route, but only for diluted hit sets.
- (b) An arbitrary deterministic hit set on at most h B/(Lambda^2 ell^C) diagonals (Lemma M1).
- (c) An arbitrary deterministic hit set with n <= h^2 Lambda^(-5.0) ell^(-C) (Theorem H; at B = Lambda^1.5 the threshold is n <= h^2 Lambda^(-5.0)). This replaces the power saving O(h^(2-delta)) of (O2) and (O3) by a polylog saving.
- (d) Families fatal only inside a class, with O(1) load and summable dilation structure, at a cost of 0.0033 in the exponent (Theorem IV).

## Proofs

0. INPUTS. All of the following are audited:
- T1 (two_moment_threshold_refinement.md): (2) to (11) and the local lemma of T2 Section 7.
- Theorem E with (E1) to (E5) (audit_t1_cost_decomposition.md: "Theorem E CORRECT modulo T1/T2"). The audit re-derived (E3): sharper (2) holds for nonconstant forms on any (T, i) box, uniformly in the constant terms.
- compatible_profile_threshold.md (5), with the role analysis of its Section 3. Every G_J is O(tau(|AB|)) or O(tau(d^2)) for affine forms A, B, d in rows, or O(1) times such a factor. Hence G_max := max_J G_J <= h^(o(1)) uniformly, for k = 2, 3, 4 and for the six-cell events (T2 (16)).
- Heavy_light Theorem S (audited): the sum over T of (k_T + 1) is at most h + C h Lambda^(beta_1), with beta_1 = E_F(1) - 1 = 1 for the menu {4}. So the sum over light T of c_T is at most C h Lambda.
- full_layout_junctions.md: J3 (closure in the F(Lambda) sense), J4 (classes of one diagonal never meet) and J5 (gluing with one switch).
- Paper Proposition partial (sec5_threshold.tex lines 335-345): cost c0 n tau*(h)^2.

1. LEMMA M1. T1/E places the labels of a set S by choosing centers independently among N_w designated period-zero slots of a fully filled profile block. A slot with no label keeps its sea pattern, which the profile hypotheses already cover (compatible Section 4: "zero, one, or at least two assigned labels"). Run the same construction for Y ⊆ S with S's slot counts. Every quantity the local lemma uses is monotone:
- class sizes: n_w(Y) <= n_w(S);
- per-variable pair sums: the sum over f in Y_w of G_{e,f} is at most the sum over f in S_w;
- higher arity: by Cauchy-Schwarz, the sum over J ⊆ Y_w with e in J of G_J is at most n_w(Y)^((k-1)/2) (sum over J ⊆ S, J ∋ e of G_J^2)^(1/2), which is at most E3's bound for S.
So S's N_w works for Y. Collars, coarse groups (E5), O(ell) blocks and row-h tails are unchanged. []
COMMENT. Applied to all light labels, M1 gives h^2 Lambda^2: no gain. This is why every touched diagonal costs h Lambda^2, whatever |Y ∩ T| is.

2. THEOREM D. Fix a profile family and a class w (dyadic below Lambda^3, coarse group above). Write S_w = S ∩ C_w, n_w = |S_w| and Y_w = Y ∩ C_w. By (E1), n_w <= C |D| h M(w).

(D1) Class sizes. The count n_w(Y) is a sum over T in D of independent variables X_T in [0, h], with mean at most rho n_w. Chernoff gives n_w(Y) <= 2 rho n_w + 9 h log h with probability at least 1 - h^(-3).

(D2) Pairs. Fix e. Partners on e's own diagonal T_e contribute at most h G_max = h^(1+o(1)), deterministically. For the other partners, the sum Phi'_e of G_{e,f} over f in Y_w with T_f != T_e splits as a sum over T of independent X_T in [0, h G_max]. The mean of X_T is at most rho b_T(e,w), where b_T is the per-diagonal budget of (E2). Summing (E2) over T gives at most rho B_S(w), with B_S(w) := ell^C |D| h (Lambda^2 + w Lambda) M(w) + h Lambda^3 + h^(1+o(1)). The coincidence diagonals and slices of (E2) are included in the last two terms. Chernoff gives Phi_e <= 2 rho B_S(w) + 10 h G_max log h with probability at least 1 - h^(-3). A union bound over at most h^2 labels and O(ell) classes fails with probability at most h^(-1+o(1)).

(D3) Higher arity, k = 3 and 4. Let Z_e be the sum over J ∋ e with J \ {e} ⊆ Y_w of G_J.
- First split off the J that have a label on T_e or two labels on one diagonal. There are at most C h n_w^(k-2) of them, so they contribute at most h^(1+o(1)) n_w^(k-2). The rest, Z'_e, depends only on Y off T_e, so it is independent of the event {e in Y}.
- E Z'_e <= rho^(k-1) times the sum over J ⊆ S_w, J ∋ e of G_J. By Cauchy-Schwarz and (E3), this is at most rho^(k-1) (n_w |D| h)^((k-1)/2) A(w), with A(w) = Lambda^4 ell^C + w Lambda^(3/2) (w^(4/3) in a coarse group).
- Covariances vanish unless J and J' meet a common diagonal, and each covariance is at most G_max^2. The number of such pairs is at most k^2 h n_w^(2k-3). So Var Z'_e <= h^(1+o(1)) n_w^(2k-3).
- Put t = (n_w h^(-eps))^(k-1). Chebyshev gives P(Z'_e > E Z'_e + t) <= h^(1 + 2 eps (k-1) + o(1))/n_w, which is at most h^(-eps) once n_w >= h^(1+8 eps).
- Classes with n_w < h^(1+8 eps) contribute at most O(ell) h^(1+8 eps) labels. Put them in E.
- Put into E every e in Y whose Z'_e exceeds the threshold. Then E|E| <= rho |S| h^(-eps) <= h^(2-eps), because {e in Y} and Z'_e are independent. By Markov, |E| <= 4 h^(2-eps) with probability at least 3/4.
- Removing labels only lowers the other labels' sums, so the bounds stay valid for Y \ E.

(D4) Local lemma exactly as in T2 Section 7, with
 N_w = C0 [2 rho B_S(w) + rho (n_w |D| h)^(1/2) A(w)^(1/2) + rho (n_w |D| h)^(1/2) A(w)^(1/3) + n_w h^(-eps) + 2 rho n_w + h^(5/3+o(1))].
The last term absorbs the coincidence terms h^((2k-3)/(k-1)+o(1)), which are at most h^(5/3+o(1)) for k <= 4. The e-dependence of A through v(e) is handled as in T1, where v(e) <= w. Summing over classes as in (E4) and (E5), with |D| h in place of Q, gives C rho |D| h Lambda^2 ell^C1 + O(h^(2-eps')) + O(ell) separations of 2W_h. Total: C(rho |D| h Lambda^2 ell^C1 + h^2 ell). [] (The events of D1 to D3 hold together with probability at least 1/2.)

WEIGHTED FORM. Only the expectations in D1 to D3 change. For pairs, the sum over T of rho times the sum over q of c_q times the sum over f in T with q | u_f of G_{e,f} is handled by (AP) on each diagonal: it is at most rho kappa B_S(w). For D3, Cauchy-Schwarz with weights gives E Z' <= (sum over f in S_w of rho_f)^((k-1)/2) (sum over J of the product of rho_f times G_J^2)^(1/2). The second factor is at most (rho kappa)^(k-1) (|D| h)^(k-1)(...) by (AP) applied to E3's boxes. The variance and the Chernoff steps used only the crude bounds G_max <= h^(o(1)) and 0 <= xi_f <= 1, so they are unchanged. []

3. LEMMA IV. Put d = be - al and g = gcd(F, d), with F = 4(al - 2be)^2 + be^2.
- Modulo g, be = al, so F = 4al^2 + al^2 = 5al^2 (mod g), and g divides 5 al^2.
- Since g divides be - al and gcd(al, be) = 1, gcd(g, al) = 1. So g divides 5.
- F >= be^2 gives q = al F/g >= al be^2/5, and p > q.
- The edges on [1, X] number at most the sum over lambda of X/p_lambda, which is at most 5X times the sum over al < be of 1/(al be^2). That is at most 5X times the sum over be of (1 + ln be)/be^2, which is at most C X.
- tau(n) << n^eps gives the summability of tau(q)^C/q and tau(p)^C/p.
- For large lambda (max(p, q) > h^(1/2)): each diagonal has at most h/p_lambda + 1 labels on edges of lambda. The sum of 1/(al be^2) over al be^2 > Y is << Y^(-1/3) log Y, because be^2 > Y/al > Y/be forces be > Y^(1/3). The "+1" terms involve only the λ with p_lambda <= h/2, of which there are at most #{al be^2 <= 3h} << h^(2/3); this gives h^(5/3) in total. So the total is O(h^(11/6) log h). []
Check (riv_edges.py): g in {1, 5} for every lambda with p <= 10^7; edges/X = 0.0020 at X = 10^6 and 0.0021 at X = 10^7; the smallest edge is (349, 749). So family IV's load is about 0.004 per u.

4. THEOREM IV.
- Classes. On a light T, c_T <= B, so K_T >= 1 and c_T K_T <= B. Every type and diagonal still has at most B classes, so the regions keep width 40960 B h^2 (J6 accounting with X = 1). Subclasses of independent sets are independent, and J4 rules out new interactions.
- Bad set. A label f in class c of T, with odd u_f, is bad only if some lambda with q_lambda | u_f or p_lambda | u_f has an edge inside c whose ends got equal colours. That happens with probability at most 1/K_T <= 2c_T/B for each such lambda. So the weighted Theorem D hypothesis holds with rho_j = 2^(j+1)/B on group j, Q_T = {q_lambda, p_lambda : max <= h^(1/2)}, c_q = 1 and kappa_IV < infinity (Lemma IV). Independence across diagonals holds because the psi_T are independent.
- Closure. Bad contains every label of every 2-label family-IV violation of the final subclasses, in the F(Lambda) sense. Supersets of Bad are allowed in J3. So J3 gives a clean light region.
- Cost of group j: C(rho_j kappa |D_j| h Lambda^2 ell^C1 + h^2 ell). Here |D_j| 2^(j-1) <= the sum over T in D_j of c_T. Summing over the O(log B) groups gives at most (4 kappa/B) times the sum over light T of c_T, times h Lambda^2 ell^C1, plus C h^2 ell^2. This is at most C h^2 Lambda^3 ell^C1/B + C h^2 ell^2.
- Large-lambda labels: O(h^(11/6)) of them, sent to Proposition partial.
- Gluing. The relocation blocks have row-h tails and sit right of z with the heavy Theorem E blocks, glued by J5.
- Exponent. Write B = Lambda^x. The total is max(x, E(a) + 1 - a x, 3 - x), minimised at x = 1.5. At a = 0.91, E = (1 + 3^0.91)/2 = 1.8588, so E + 1 - 1.365 = 1.494 <= 1.5. []
R_FF. The same argument works for any within-class family whose edges are dilations (u, r u) with summable tau-weighted inverse heights. That is hypothesis (FF), and it is true if the admissible points of the nodal cubic have O(X^(2/3+o(1))) primitive ratios of height at most X (not checked). For the T-dependent ee graph, the split is per diagonal anyway. For load (log h)^c, the third term becomes 3 + c - x, which gives exponent 1.5 + c/2.

5. THEOREM H (arbitrary Y). By Theorem A and Lemma 1 (audited), every pair role that is not O(1) has its geometric factors in a single endpoint c of f. The roles are:
- Psi_e(c): tau((c-a)^2) and tau(c-a) tau(c+a-s-t);
- v(e) Theta_e(c), with Theta built from tau(c-a) and tau(a+s-c-t);
- v(f) Theta'_e(c), and v(f) <= w for f in C_w.
Let d_w(c) be the number of labels of Y_w with endpoint c. Then d_w(c) <= h/2 and the sum of d_w(c) is at most 2n_w. Hölder over c, with Henriot one-variable s-moments that are uniform in the constant terms, gives:
- the sum over f in Y_w of Psi(c_f) is << n_w^(1-1/s) Q^(1/s) Lambda^((3^s-1)/s);
- the sum over f in Y_w of Theta(c_f) is << n_w^(1-1/s) Q^(1/s) Lambda^((2^s-1)/s).
These hold uniformly in e, so no peeling is needed. Further:
- class sizes: n_w <= min(n, C Q Lambda^(2^t-1) w^(-t));
- a partner-weighted variant: the sum over f in Y_w of Theta is at most 2^t'' w^(-t'') n^(1-1/s) (Q Lambda^(2^s + 2^(t'' s) - 2))^(1/s);
- higher arity, by deterministic Cauchy-Schwarz with (5): sqrt(n_w Q) (Lambda^2 + w_+^(1/2) Lambda^(3/4));
- T1's full-class bounds, wherever they are smaller.
Young's inequality turns each term into n Lambda^a + Q Lambda^b. holder_exponent3.py and refine.py optimise the free parameters (s, t, t'') against the worst (n, w) and give a(1.5) = 6.50 and a(0) = 8.27. The worst case is the private-weight term, with w about Lambda^3.2 and n about Q Lambda^(-5). The exponent values are numerical. Each inequality used is a proved inequality, but the adversary grid is finite, so the true optimum of this bookkeeping may be slightly higher. A safe quote is a(1.5) <= 7.

6. LEMMA M4 (heuristic, about the method). Take Y = {e : v(e) ~ W} with W = Lambda^(alpha ln 2). Selberg-Delange for omega gives n ~ Q Lambda^(-(1 - alpha + alpha ln alpha)). Every e in Y meets about W times the sum over f in Y of tau(c_f - a), which is about W n Lambda, label-point triangle geometries. These are fatal, since only high-sea-rooted triangles are allowed. So the per-variable first moment needs N >= c n W Lambda. Requiring n W Lambda <= n Lambda^a + Q Lambda^b for all alpha < 2e (b = 0) forces a >= 1 + 2e ln 2 = 4.77. For b = 1.5, alpha = 3.575 forces a >= 3.48. A second adversary concentrates d_Y on the top rows of tau((r - a0)^2). It shows that max_e Phi can reach n Lambda^7.77, but only for the h labels at a0, so it can be peeled. It is not a lower bound for the method.

## External results used

- Henriot, Nair-Tenenbaum bounds uniform with respect to the discriminant, Corollary 2, with the 2014 erratum. Used as quoted in T2 (7) and sharper (2). The AP form (AP) is a hypothesis I derive from it but have not verified in writing.
- Chernoff bound for sums of independent bounded variables; Chebyshev's inequality; Markov's inequality.
- Lovasz local lemma, product form, as in T2 Section 7.
- Selberg-Delange for omega(n) = k with k <= A loglog x, used only in the heuristic Lemma M4.
- Shiu's short-interval divisor bound, mentioned only as a suggested route.
- Paper sec5_threshold.tex: Proposition partial (cases (a) and (c)), the 2W_h + 1 locality, and the row-1/row-h switch.

## Checks

Scripts are in scripts_relocation_polylog/. Each ran with py in under 60 s, one at a time. One run timed out (holder_exponent3.py on a fine grid); I stopped it and reran it on a coarser grid. The repository was only read.
- riv_edges.py: enumerates the R_IV^(4) lambdas. It confirms g = gcd(F, be - al) is in {1, 5} for every lambda with p <= 10^7, and that gcd(p, q) = 1. Edge counts are 1993 on [1, 10^6] and 20895 on [1, 10^7], so edges/X is about 0.002. The smallest edge (349, 749) matches the note.
- holder_exponent.py, holder_exponent2.py, holder_exponent3.py and refine.py: the exponent bookkeeping for Theorem H. Without the partner-weight option, the required a diverges as n shrinks. With it, a(0) = 8.27 and a(1.5) = 6.50, and nothing is needed at b = 2, consistent with T1.
I re-read audit_t1_cost_decomposition.md (Theorem E, E3 and E5 pass) and audit_heavy_light_split.md (Theorem 3 and Lemma P pass), and Proposition partial at sec5_threshold.tex lines 335-345.

## Gaps

- (AP) is a hypothesis. It is needed for the weighted Theorem D and so for Theorem IV, because the relocated labels are AP-structured: P(bad) is proportional to the number of lambda with q_lambda | u. I sketched why Henriot Cor. 2 gives the extra factor tau(q)^C ell^C/q by substitution: Euler factors over the primes dividing q and the resultants. I did not write it out for the box second moment, and nobody audited it.
- Theorem D's variance step (D3) uses only crude bounds: G_max <= h^(o(1)), and for k = 4 a count of at most k^2 h n_w^(2k-3) pairs sharing a diagonal. I re-read it once; it needs an audit. Uniformity of G_max <= h^(o(1)) is read off compatible Section 3, including its exceptional roles. Those roles have O(1) choices of j times a divisor count, which I believe is h^(o(1)) per J, but I did not re-derive every one.
- Theorem IV is conditional on everything else in L**: (O2), the rest of (O3), (U1) to (U3), the unaudited J1 to J5, and the existence of the prime p. It also needs (AP). For R_FF it needs hypothesis (FF), whose summability I did not check against the nodal-cubic parametrisation.
- Theorem IV uses only the proved bound sum_T c_T <= C h Lambda (Theorem S). That costs the 0.0033. If sum over light T of c_T = O(h) (the data give about 1.1h), the relocation term is h^2 Lambda^2/B and the exponent returns to 1.4967.
- Theorem H's exponents are numerical bookkeeping on a finite grid. The bound n Lambda^6.5 + h^2 Lambda^1.5 is weak. Its constituent Hölder steps need Henriot s-moments for multi-form products at general fixed s; T2 states them only for s in a compact interval around 1, although the same theorem applies.
- Lemma M4 is a first-moment statement about the method, with a heuristic Selberg-Delange count. It is not a lower bound on m_h or on R(Y).
- Feo (O3)(iii-a) in SAW: its per-label rate grows with h (0.127 at h = 20481), so its load may be (log h)^c. I did not show it has the summable dilation structure Theorem IV needs. The alternative SAW* still needs its compatibility with L** checked.
- Cross-class and deterministic families, namely (O2)(a) to (d), (O3)(ii), (iv) and (vii), are not diluted across diagonals. For them I prove only the weakened thresholds: Theorem H (n <= h^2 Lambda^-5) or Lemma M1 (few diagonals).
- The row-degree measure (H1') of heavy_light remains unproved for full boards. Decoupled endpoint class weights cost an extra Lambda in pairs (Delta h Lambda^3 by the König/rearrangement argument, not written out), and the higher-arity term does not scale with Delta.

## Missing estimate

For the near goal on this route:
(1) Hypothesis (AP): T2 (7) and sharper (2), restricted to label variables in progressions mod q <= h^(1/2), with factor tau(q)^C ell^C/q. This is a direct Henriot application, and it is the only new arithmetic input Theorem IV needs.
(2) For R_FF: summability (FF) of tau(height)^C/height over the admissible d < 0 points of the nodal cubic.
(3) For the deterministic families of (O2) and (O3), one of these:
- a count n <= h^2 (log h)^(-5-eps) (Theorem H; a polylog saving instead of the h^(-delta) that L** needs);
- a per-diagonal randomisation of the layout (for example independent random m_c orderings or random primes per residue block) that makes their hit sets diluted across diagonals, so that h^2/(log h)^0.51 suffices.
Sharpening the private-weight term of Theorem H, for example by choosing the relocation block's profile rows from windows of length h^theta (Shiu's short-interval bound would then make the average of v(e) O(Lambda)), would lower a(1.5) toward the vertical-rival value of 5.4.

## Next steps

- Write out (AP) for the one-variable moments and for the box second moment (sharper (2)), with the Euler factor over the primes dividing q and the resultants. Then have Theorem D (the D1 to D3 Chernoff and Chebyshev steps) and Lemma IV audited. If they pass, add ledger rows: 'R_IV has O(X) edges, g | 5' and 'diluted relocation: rho |D| h log^2 h (loglog h)^C + h^2 loglog h'.
- Re-state Theorem J6 of full_layout_junctions.md with the random split K_T = floor(B/c_T) in place of psi. (O1) is then no longer needed, at exponent 1.5.
- Check hypothesis (FF) for R_FF by computing the primitive admissible ratios of the nodal cubic up to height X. Count them and sum tau^C/height, in the style of riv_edges.py. Do the same census for Feo in SAW to see whether it has dilation structure.
- Try to prove sum over light T of c_T = O(h), or at least O(h (log h)^c) with c < 1. This would return Theorem IV to exponent 1.4967 or between the two values.
- For the cross-class (O2) families, test whether a per-region independent randomisation of the m_c assignment keeps Proposition R's rule and gives hit sets that are independent across diagonals. Theorem D would then absorb them at about h^2/Lambda^0.51 labels instead of h^(2-delta).
- Try the wide-profile-window variant (H in [h - h^theta, h]) of Lemma AP and filled_mod7_profile_cover. It would cut Theorem H's private-weight exponent, and it costs only O(h^(1+theta)) extra exceptional labels.

