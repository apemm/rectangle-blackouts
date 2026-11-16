# The weak-codegree matching hypothesis W is false

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (obstruction): a tensor-type instance on the group-model host K_{n,n} satisfies every hypothesis of the conflict-free matching theorem of Glock, Joos, Kim, Kuhn and Lichev except the two codegree conditions, which hold only at d/K for polylogarithmic K, with every violating set a clique meeting each label once. Still no conflict-free matching covers 3/4 of the labels. A true theorem of this type needs Gamma <= 8 ln K + O(lnln K), which caps the certifiable price at Lambda^2/(C log Lambda). So Theorem 7 of line_aware_greedy.md rests on a false hypothesis. Not audited yet.

# Result

## Status

obstruction

## Summary

Hypothesis W is false. A tensor-type instance on the group-model host K_{n,n} satisfies every GJKKL Theorem 3.1 hypothesis, except that (C4) and (C5) hold only at d/K for any polylogarithmic K. The violating sets are group-star cliques that meet each label once. Even so, no conflict-free matching covers 3/4 of the labels. A true theorem of this type needs Gamma <= 8 ln K + O(lnln K). In the T1 block that caps the certifiable price at Lambda^2/(C log Lambda), so bE stays at 2 and Theorem 7 of line_aware_greedy.md rests on a false hypothesis.

## Statements

NOTATION. GJKKL is Glock, Joos, Kim, Kuhn and Lichev, arXiv 2205.05564, Theorem 3.1 and the definition of a (d, ell, Gamma, eps)-bounded conflict system, with conditions (C1) to (C5). Hypothesis W is as stated in line_aware_greedy.md: GJKKL Theorem 3.1 (and 3.2) still holds when the codegree conditions (C4) and (C5) (and (Z3)) only require d/K instead of d^(1-eps), for some K = K(d) tending to infinity.

THEOREM 1 (W is false, even in its clique-structured form, on the group-model host; PROVED).
- Fix eps in (0, 1). Let K(.) be any function with 1 <= K(d) <= d^(eps^2/25) for all large d; every polylogarithmic K qualifies.
- Then for every n >= n0(eps, K) there is an instance (H, C) with these properties:
  - H = K_{n,n}, with labels on one side and groups on the other. It is a 2-graph on 2n vertices, every degree equals d = n, and Delta_2(H) = 1. This is exactly the host of line_aware_greedy.md Proposition 2.
  - C is a set of 2-conflicts. Each conflict is a pair of options with distinct labels and distinct groups.
  - Take k = ell = 2, mu = 1/4, Gamma = 8(1 + ln D) + 1 and n <= exp(d^(eps^2/2)). Then 1/mu^(Gamma ell) <= d^(eps^2), and (C1), (C2) and (C3) hold.
  - (C4) and (C5) hold with the bound d/K_inst, where K_inst = D/(20(1 + ln D)) >= K(d). The parameter D lies in [(ln n)^2, n^(eps^2/24)]; it is defined in the proof.
  - Every C-free matching has fewer than (3/4) n = (1 - mu)|V(H)|/2 edges. So the conclusion of GJKKL Theorem 3.1 fails.
- Clique structure. The only sets that exceed the original d^(1-eps) codegree bound are group-star pieces S_y = {(x, y) : x in Q}. Here y is a group and Q is a label block. Each piece is a set of options through one group vertex, so its options pairwise exclude each other in any matching. Each piece meets each label's options at most once. Every (C5) common neighbourhood lies inside a union of at most 4 such pieces. These are the label-rooted columns (group-vertex cliques) of line_aware_greedy.md Theorem 3(b) and (c).

PROPOSITION 2 (robustness: spread versions fail too; PROVED). Add to C a random-shift conflict system C'. For each unordered label pair {x, y}, draw phi(x, y) uniformly from Z_n \ {0}, and put {(x, g), (y, g + phi(x, y))} into C' for every g. With high probability, (H, C union C') satisfies:
- all hypotheses of Theorem 1 with Gamma + 1 in place of Gamma, and with K_inst replaced by D/(35(1 + ln D));
- every option conflicts with options of every other label;
- the number of options of label y that conflict with a fixed option of label x is at most 2D + 1 = polylog(n) when D = (ln n)^3.
Adding conflicts cannot create matchings, so there is still no C-free matching of size 3n/4. This matches the T1-block features (all label pairs interact, mu_ef <= G_max = h^(o(1))). So those features do not rescue W.

COROLLARY 3 (what a true clique-aware theorem can give; PROVED from Theorem 1).
- Take any theorem whose hypotheses are the degree conditions of GJKKL 3.1, a Gamma-bound, and codegree conditions (C4) and (C5) at d/K, with large common neighbourhoods allowed only as unions of at most 4 cliques that meet each label once.
- If its conclusion is a (3/4)-matching, it must require Gamma < 8 ln K + 8 ln ln K + C0. The reason: at mu = 1/4, the instances of Theorem 1 have Gamma = 8(1 + ln D) + 1 and K = D/(20(1 + ln D)).
- In the group model of Proposition 2, Gamma = (1 + o(1)) max_o D(o)/(m n). In a Theorem E main class, max D(o)/n >= c Lambda^2. The cliques have relative weight of order 1/m at least (lines: about 1/(2m); columns: about w (ln m)^2/m), so K <= 2m.
- Such a theorem can therefore certify at best m >= c Lambda^2/log Lambda. That is exponent bE = 2, the same ceiling as conflict_free_matchings.md (Theorem L, Corollary DP).
- Consequence: Theorem 7 of line_aware_greedy.md (price Lambda ell^C, theta_E(1) = 0.9101) is conditional on a false statement. Its conclusion is not refuted, but it has no support. W must be dropped from the board, and any route to bE < 2 by this method must use structure that the tensor instances lack.

NOT PROVED. Proposition 2's real instances (independent uniform positions r(e, g), translation-invariant offset sets D_ef) are neither proved nor refuted. The open special case is stated in Gaps.

## Proofs

0. THE GJKKL STATEMENT USED (read today from the arXiv HTML of 2205.05564 through a fetch tool that returned verbatim quotes).
- Theorem 3.1 quantifiers. For every k >= 2 there is eps0 > 0. For every eps in (0, eps0) there is d0, and the following holds for all d >= d0.
- Theorem 3.1 hypotheses:
  - ell >= 2 is an integer, Gamma >= 1, and mu is in (0, 1/ell], with 1/mu^(Gamma ell) <= d^(eps^2);
  - H is a k-graph on n_V <= exp(d^(eps^2/ell)) vertices with (1 - d^(-eps)) d <= delta(H) <= Delta(H) <= d and Delta_2(H) <= d^(1-eps);
  - C is a (d, ell, Gamma, eps)-bounded conflict system for H.
- Theorem 3.1 conclusion: a C-free matching of size (1 - mu) n_V/k.
- The bounded conditions:
  - (C1) 2 <= |C| <= ell for every conflict;
  - (C2) the sum over j of Delta(C^(j))/d^(j-1) is at most Gamma, and at most Gamma uniformities occur;
  - (C3) Delta_j'(C^(j)) <= d^(j-j'-eps) for 2 <= j' < j;
  - (C4) for every edge e and vertex v, at most d^(1-eps) of the 2-conflict partners of e contain v;
  - (C5) any two disjoint edges have at most d^(1-eps) common 2-conflict partners.
- W keeps everything except (C4) and (C5), where d^(1-eps) becomes d/K(d).

1. CONSTRUCTION.
- Choose D: the least integer D >= (ln n)^2 with D/(20(1 + ln D)) >= K(n). Since K(n) <= n^(eps^2/25), for large n this gives D <= max((ln n)^2 + 1, 40 K ln(40K) + C) <= n^(eps^2/24) <= n^(1/4).
- Put p = D/n and a* = ceil(1 + (2/p)(1 + ln D)), and s = 2a*.
- Partition the labels [n] into q = floor(n/s) blocks Q_1, ..., Q_q of size s, plus a remainder R with |R| < s.
- Let G2 be a graph on the groups [n] with these three properties:
  - (i) maximum degree at most 2D;
  - (ii) every two groups have at most 4 common neighbours;
  - (iii) independence number alpha(G2) <= a*.
- Define C as the set of all pairs {(x, g), (y, g')} with x != y in the same block Q_i and g g' an edge of G2. The two options of such a pair are disjoint.

2. G2 EXISTS. Take the random graph G(n, p) and check each property.
- (i) A degree is Bin(n - 1, p) with mean at most D. By Chernoff, P(deg >= 2D) <= e^(-D/3). A union bound over the vertices gives n e^(-(ln n)^2/3), which tends to 0.
- (ii) P(codegree >= 5) <= C(n, 5) p^10 <= (n p^2)^5 = (D^2/n)^5 <= n^(-5/2), using D <= n^(1/4). A union bound over the n^2 pairs gives n^(-1/2), which tends to 0.
- (iii) P(alpha >= a) <= C(n, a)(1 - p)^(a(a-1)/2) <= [(en/a) e^(-p(a-1)/2)]^a. At a = a*, p(a* - 1)/2 >= 1 + ln D, so the bracket is at most n/(a* D) = 1/(a* p) <= 1/2. So the probability is at most 2^(-a*), which tends to 0.
- All three properties hold together with probability 1 - o(1).

3. HYPOTHESES OF THEOREM 3.1 (W form).
- Host. H = K_{n,n} has n_V = 2n <= exp(n^(eps^2/2)) vertices. Every degree is n = d, and two vertices lie in at most one common edge, so Delta_2(H) = 1.
- (C1). Every conflict has size 2. (C3) is vacuous, because only j = 2 occurs.
- (C2). The conflict partners of (x, g) are the options (y, g') with y in Q(x) \ {x} and g' in N(g). So Delta(C^(2)) <= (s - 1) 2D. Then
  Delta/d <= 2sD/n <= (4D/n)(2 + (2n/D)(1 + ln D)) = 8(1 + ln D) + 8D/n <= Gamma.
  Only one uniformity occurs, and 1 <= Gamma.
- Gamma condition. 1/mu^(Gamma ell) = 16^Gamma, and 2 Gamma ln 4 <= 2.78 (9 + (8 eps^2/24) ln n) = 25 + 0.925 eps^2 ln n <= eps^2 ln n for large n. Also mu = 1/4 lies in (0, 1/2].
- (C4). Fix an option e = (x, g) and a vertex v.
  - If v is a label y, then the partners of e containing v are the options (y, g') with g' in N(g). There are at most 2D <= 2 n^(1/4) of them, which is below d^(1-eps) whenever eps < 3/4.
  - If v is a group g', then the partners containing v are the options (y, g') with y in Q(x) \ {x}. There are at most s - 1 of them, and only when g' is in N(g). Using D <= n^(1/4),
    s - 1 <= 4 + 4(n/D)(1 + ln D) <= 5(n/D)(1 + ln D) <= n/K_inst.
- (C5). Disjoint options (x, g) and (x', g') have x != x' and g != g'. A common partner (y, gamma) needs y in Q(x) intersect Q(x') minus {x, x'}, and gamma in N(g) intersect N(g').
  - If Q(x) != Q(x'), there is none.
  - Otherwise there are at most (s - 2) times 4 of them, at most 20(n/D)(1 + ln D) = n/K_inst.
- K_inst >= K(n), by the choice of D (D/(1 + ln D) is increasing).

4. NO LARGE C-FREE MATCHING.
- Let M be a C-free matching, so each matched label x has its own group pi(x). Fix a block Q_i.
- If two matched labels x, y of Q_i had adjacent groups pi(x) pi(y) in G2, then {(x, pi(x)), (y, pi(y))} would be a conflict of C. So pi restricted to the matched labels of Q_i is injective onto an independent set of G2.
- So each block has at most a* = s/2 matched labels, and |M| <= q s/2 + |R| <= n/2 + s.
- s <= 4 + 4(n/D)(1 + ln D) = o(n), because D >= (ln n)^2. So |M| < 3n/4 = (1 - mu) n_V/2 for large n.
- W fixes eps0(2) and d0 but no single eps. For every eps in (0, 1) and every d0, the instance with n >= max(n0, d0) violates W's conclusion. This refutes W for every choice of eps0 and every K(d) <= d^(eps^2/25), in particular for the K = ell^(C-3) of Theorem 7.

5. CLIQUE STRUCTURE.
- The group-vertex sets in (C4) are S_{g'} = {(y, g') : y in Q}. They share the vertex g', so they exclude each other in any matching, and they meet each label once.
- A (C5) common neighbourhood lies inside the union of S_gamma over gamma in N(g) intersect N(g'), which is at most 4 such sets.
- Everything else satisfies the original GJKKL bounds: label-vertex counts are at most 2D <= d^(3/4).
- So the instance meets the clique-aware form that the target asks about: every violating set is a clique of the exclusion relation that meets each label at most once. These are the column-type cliques of line_aware_greedy.md Theorem 3(b).

6. PROPOSITION 2.
- Each option (x, g) gets exactly one C'-partner in each other label y, namely (y, g + phi(x, y)). So the C'-degree is n - 1, and Gamma increases by 1.
- (C4) for C union C'.
  - At a label vertex, C' adds 1.
  - At a group vertex g + t, C' adds #{y : phi(x, y) = t}. For fixed (x, t) this is a sum of independent indicators, each of probability 1/(n - 1), so P(>= r) <= 1/r!. With r = ceil(ln n), 1/r! <= n^(-3), and a union bound over the n^2 pairs (x, t) works.
- (C5) for C union C'. The common neighbourhood splits into four parts.
  - The C, C part is at most 4s.
  - Each C, C' cross part is at most s: N_C'(f) has exactly one option per label, and N_C(e) involves only the labels of Q(x).
  - The C', C' part counts y with phi(x, y) - phi(x', y) = g' - g. For x != x' these indicators are independent over y, each of probability at most 1/(n - 1). So P(>= ln n) <= (1.01 e/ln n)^(ln n) <= n^(-4), and a union bound over the n^3 triples works.
  - The total is at most 6s + ln n <= n/(D/(35(1 + ln D))).
- The multiplicity bound: label y has at most 2D options in conflict with (x, g) through C (only when y is in Q(x)), plus exactly 1 through C'.
- Adding conflicts never creates C-free matchings, so step 4 still applies.

7. COROLLARY 3.
- In the instances, Gamma = 8(1 + ln D) + 1 and K = D/(20(1 + ln D)). Hence ln K = ln D - ln(20(1 + ln D)), and Gamma = 8 ln K + 8 ln ln K + O(1) (the O(1) can be negative).
- So any valid theorem with only these hypotheses must exclude such Gamma at that K.
- In the group model, take K <= 2m and Gamma >= (1 + o(1)) c Lambda^2/m. The requirement Gamma < 8 ln(2m) + 8 ln ln(2m) + C0 forces m ln m >= c' Lambda^2, that is, m >= c'' Lambda^2/log Lambda.
- The relocation price exponent therefore stays at 2 by this method. A constant mu = 1/4 suffices for this conclusion: by Proposition 1(b) of line_aware_greedy.md, O(ell) re-placement rounds absorb a constant leftover fraction. So refuting W at mu = 1/4 is enough.

8. WHY THIS IS THE AMPLIFICATION, NOT A PROOF ARTEFACT. In the instances, K is about e^(Gamma/8)/Gamma. So the codegree saving needed to run at conflict level Gamma is exponential in Gamma. This is exactly the e^(O(Gamma)) error amplification that line_aware_greedy.md Gaps found in the GJKKL proof. The amplification is a property of the hypothesis class, not of that proof.

9. SANITY CHECK (not part of the proof). The script tensor_check.py ran with py -I in about 30 s on the instance n = 20000, D = 200. That D is above n^(1/4), so the codegree bound of (ii) is not expected there, and the sampled maximum codegree was 10.
- Maximum degree: 265.
- Clique blocks: s = 2522, 7 of them.
- Gamma: 33.4 measured, against the bound 51.4.
- Random greedy conflict-free matching: it covered 0.297 n.
- Labels placed per block: 502 to 528. This is close to (n/D) ln D = 530, the greedy independent-set size in G(n, p), and far below the 3n/4 that W would promise.

## External results used

- Glock, Joos, Kim, Kuhn, Lichev, 'Conflict-free hypergraph matchings', arXiv 2205.05564v1, Theorem 3.1 and the definition of (d, ell, Gamma, eps)-bounded conflict systems (C1) to (C5). Read today as verbatim quotes from the arXiv HTML. In my words: for k >= 2 there is eps0; for eps < eps0 there is d0; for d >= d0, any ell >= 2, Gamma >= 1 and mu in (0, 1/ell] with mu^(-Gamma ell) <= d^(eps^2), any k-graph H on at most exp(d^(eps^2/ell)) vertices with every degree in [(1 - d^(-eps)) d, d] and codegree at most d^(1-eps), and any (d, ell, Gamma, eps)-bounded C, there is a C-free matching with (1 - mu) n/k edges. Here (C4) bounds by d^(1-eps) the number of 2-conflict partners of an edge that contain a given vertex, and (C5) bounds by d^(1-eps) the common 2-conflict partners of two disjoint edges.
- Chernoff bounds for binomial variables, and the first-moment bound P(alpha(G(n,p)) >= a) <= C(n,a)(1-p)^C(a,2). Both are standard.

## Checks

I read line_aware_greedy.md, conflict_free_matchings.md, pair_families_dp_colouring.md and cross_direction_triangles.md in full. I read GJKKL Theorem 3.1 and conditions (C1) to (C5) from the arXiv HTML, quoted verbatim. By hand I checked the construction, the three G(n,p) properties, the bounds for (C2), (C4) and (C5) and the Gamma condition, the block-independence counting, Proposition 2's codegree bounds, and the Corollary 3 arithmetic. One sanity script, scripts_w/tensor_check.py, ran with py -I in about 30 s and under 1 GB at n = 20000 and D = 200. Random greedy covered 0.297 n, with 502 to 528 labels placed per block. The repository was only read. No git command was run, and no report file was written.

## Gaps

- The special case that matters is open: Proposition 2's real instances, with independent uniform positions r(e,g) and translation-invariant offset sets D_ef from the T2 events. Theorem 1 refutes W on Proposition 2's host, but its conflicts are a tensor K_Q x G2 with one fixed group graph G2 for all label pairs in a block, not slot arithmetic. I did not prove that random-position, translation-invariant conflicts avoid every tensor-like obstruction. My only evidence is a heuristic: a Cayley-graph version of G2 needs independence number about (n/D) ln D, and arithmetic progressions push the independence number of sparse random Cayley graphs on Z_n up to about (n/D) ln n, which would put Gamma above the GJKKL range. That is unproved.
- A sharper exact statement of the open special case: in Proposition 2 instances with m = C Lambda ell^C, does a C-free matching of size (1 - Lambda^(-2)) n_w exist? Any proof must use structure that the tensor instances lack, such as independence of the positions across label pairs. Degree and codegree bounds plus clique structure are not enough (Theorem 1, Corollary 3).
- I did not prove the positive side of Corollary 3: that GJKKL Theorem 3.1 holds with codegrees d/K when Gamma <= c ln K/(ell ln(1/mu)). That is what would make 8 ln K the true threshold up to constants. It would only give the known log Lambda gain, so I did not pursue it.
- The GJKKL statement and definitions were read through a fetch tool that returned verbatim quotes from the arXiv HTML of 2205.05564v1. I read no other version line by line. The refutation needs only Theorem 3.1's hypotheses and conclusion as quoted, with k = ell = 2, so the unspecified eps0 does not matter: the counterexample works for every eps in (0, 1).
- W's Theorem 3.2 form (test systems, (Z3)) is refuted only through its matching conclusion. I did not separately analyse the test-system statements.
- Nothing here is audited. A second reader should check the parameter arithmetic: the Gamma condition 2 Gamma ln 4 <= eps^2 ln n, the bounds s - 1 <= 5(n/D)(1 + ln D) and 4(s - 2) <= n/K_inst, and the first-moment bound on alpha(G(n, p)).

## Missing estimate

This route produces no missing estimate: it ends in an obstruction. To reach bE < 2 through conflict-free matchings, one would need a theorem for the specific Proposition 2 instances (independent uniform positions, translation-invariant D_ef, mu_ef <= G_max) at Gamma of about Lambda/C, and its proof must use the independence of conflict relations across label pairs. Theorem 1 shows that degree and codegree bounds, even with clique-structured violators, cannot reach beyond Gamma of about 8 ln m. Separately, if the new mod-p list idea removes the Lemma F family and cuts the pair degree to D/n <= Lambda ell^C, then the T2 local lemma alone gives price Lambda ell^C and no W-type theorem is needed. That is conditional and not checked here.

## Next steps

- Record in the ledger: Hypothesis W (line_aware_greedy.md) is false (Theorem 1). Theorem 7's conditional price Lambda ell^C loses its support, and the conflict-free matching route has a hard ceiling of Lambda^2/log Lambda (Corollary 3), which agrees with conflict_free_matchings.md Theorem L.
- Audit Theorem 1. It is one page: the G(n,p) properties (i) to (iii), the block counting, and the parameter arithmetic.
- Move effort to label-dependent arithmetic lists (the mod-p1, mod-p2 idea). If they cut the Lemma F weight to about 3 Lambda^2/p and no other family has weight Lambda^2, then plain LLL already gives price about Lambda ell^C, and no semi-random theorem is needed.
- If anyone pursues the Proposition 2 special case, first look for a tensor-like obstruction built from slot arithmetic: a label set Q and a translation-induced group graph with small independence number. A Cayley-graph analogue of Theorem 1 would close the special case negatively as well.

