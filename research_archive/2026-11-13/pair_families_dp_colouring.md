# Pair families and locally sparse colouring

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (obstruction to a method): in a T1-type block, the Lemma F part of the conflict cover is an edge-disjoint union of lines, each meeting each label's slot list at most once, and every option's neighbourhood contains cliques of about n options. So no colouring theorem based on local sparsity certifies a price below c Lambda^2/log Lambda. This bounds a method, not the price. A placement that uses the line structure directly (a nibble or random greedy) stays possible, and it needs a cross-direction triangle count that is not proved. Not audited yet.

# Result

## Status

obstruction

## Summary

Obstruction to the colouring route: in a T1-type block, every option's neighbourhood in the DP cover contains a clique of about n options. One clique comes from the coincidence events. A second, of about n/2 options, lies on the (3,4) Pythagorean line of the Lemma F family. So the local sparsity is at most about (D/n)^2. That is about Lambda^4 in the Theorem E blocks, where D/n is about Lambda^2. Every locally-sparse or F-free colouring theorem then certifies a price of at least c Lambda^2/log Lambda, and Anderson-Dhawan-Kuchukova (ADK) Theorem 1.13 does not apply at all. A price of Lambda^(1+o(1)) is not proved; the price stays at Lambda^2 ell^C. The Lemma F part of the cover is exactly a union of lines (a collinearity graph). A clique-aware nibble remains possible, but it needs a cross-triangle bound that is not proved and a new semi-random theorem. Under the existing higher-arity bound (14), even an ideal greedy placement is heuristically capped at Lambda^(3/2).

## Statements

Setting. Take a T1-type relocation block, that is, a T2 block (safe_triangle_pair_first_moment.md Sections 1, 2, 7), or a Theorem E or Theorem D class block (t1_cost_decomposition.md (E2) to (E5), polylog_relocation_diluted.md (D4)). It has:
- slot columns 7j, for j in [0, N);
- empty slots holding F;
- the label set Z, with n = |Z| labels, all inside one profile and block type, so that the odd rows of Z agree mod 14 and the even rows agree mod 14;
- the T2 event system E (two-, three- and four-label events, coincidences included, evaluated with F at every other period-zero column).

The cover H has vertex set Z x [N], the "options". Two options (e, j) and (f, j') with e != f are adjacent when {e at j, f at j'} is a two-label event of E. Coincidence j = j' counts as an event. Let Lambda = log h and ell = loglog h.

STATEMENT 0 (only the slot assignment changes; proved by reading). By block_layout_n1.md BL1, input I2 and Lemma RL, with the audit's patch (T2's events and T2's block map), the layout uses the centre map X_c only through two facts: it is injective, and it avoids every E_J with |J| = 2, 3 or 4. So any placement method that produces such an X_c (colouring, greedy or nibble) leaves the profiles, collars, T2 block map, separations and row-h tails unchanged. Only N_c changes.

PROPOSITION 1 (degree and multiplicity; proved).
(a) Each pair e != f has a set D_ef of nonzero column offsets in 7Z. The option (e, j) is adjacent to (f, j + X/7) exactly when X is in D_ef and the slot is in range. Also mu_ef := |D_ef| <= G_{e,f} <= G_max = h^(o(1)).
(b) The degree D(e, j) is at most (n - 1) + sum_f G_{e,f}, which is at most n + B(w) (T2 (10); Theorem E (E2)).
(c) The average of D(e, j) is N times the average incident two-label sum. By Theorem R(a) it is at least c n Lstar / 7, with Lstar = ln R2 ln min(R1, R2^(1/3)). In the main Theorem E classes, Lstar >= c c1 Lambda^2.
(d) For f in a positive proportion of the partners of e, mu_ef >= 2, so the correspondence between L(e) and L(f) is not a matching.

PROPOSITION 2 (line decomposition of the Lemma F part; proved). Fix a parity. Write P(e, j) = (j, rho(e)) for the point of option (e, j) in slot units and row units. Let H_F be the Lemma F part of H: same-parity points at integral distance, nonzero row gap, sea pair at u+ and u-. Then:
- H_F is the edge-disjoint union of cliques, the "lines". Each line is a coset P0 + Z w_v. Here v = (p, q) is a primitive Pythagorean vector with p, q != 0, and w_v = 7v/gcd(7, p) or 14v/gcd(7, p) (the multiple forced by the slot condition and the parity condition).
- Each line meets each list L(f) at most once.
- Every option lies on exactly one line of each direction.
So, inside one block, avoiding the Lemma F family means choosing one option per label with no line holding two chosen options.

THEOREM C (neighbourhood cliques; proved).
(C1) For every option o = (e, j), the set {(f, j) : f != e} is a clique of size n - 1 inside N(o), through the coincidence events. So e(H[N(o)]) >= (n - 1)(n - 2)/2.
(C2) The robust version, which survives any device that removes coincidences. Let A_e = #{f != e : f's odd row is congruent to e's odd row a mod 28}. Take any slot j with 3h/28 <= j <= N - 1 - 3h/28. Then
 K(e, j) = {(f, j + 3(c_f - a)/28) : f != e, c_f congruent to a mod 28}
is a clique of size A_e inside N(e, j), and all its edges are genuine two-label events of E. The sum over e of (A_e + 1) is at least n^2/2. So A_e >= n/2 - 1 for every e in the more popular class mod 28, which holds at least half the labels. The same statement holds for even points.

COROLLARY C3 (what locally-sparse colouring can certify; proved, given the quoted theorems). Let d = Delta(H), and let f_loc = min over o of d^2/e(H[N(o)]). By (C1), f_loc <= 2.1 (d/n)^2.
(i) ADK, arXiv:2402.19271, Theorem 1.13 and Corollary 1.14 (correspondence colouring in the colour-degree setting). This theorem does not apply to H. Its hypothesis (CC3), a matching between any two lists, fails by Proposition 1(d). Its range hypothesis k <= d^((s+t)/10) also fails for every K_(s,t) when n >= h^c: a clique of size n - 1 contains at least c n^(s+t) copies of K_(s,t), while d <= n^(1+o(1)). Even if the range were extended, the list size the theorem asks for is C d / log(d k^(-1/(s+t))) >= C d / log(2(s+t) d/n). By Proposition 1(c), that is a price N/n of at least c Lstar / log Lstar, which is at least c Lambda^2/log Lambda in the Theorem E blocks.
(ii) Every theorem that assumes G or H to be triangle-free or F-free for a fixed graph F fails here. This covers Johansson-Molloy, Bernshteyn's DP version, and the almost-bipartite F-free versions. The reason is that K_(n-1) contains every graph on at most n - 1 vertices, and the label graph G contains two cliques of size about n/2 (the (3,4) direction).
(iii) Alon-Krivelevich-Sudakov (AKS) Theorem 1.1, with its tightness Proposition 1.2 as read in the audit of three_term_relations.md (2 <= f <= 2d^2). No criterion that uses only (d, f_loc) and the list size certifies an independent transversal below c d / log f_loc, which is at least c' d / log(d/n). The reason: a graph G0 with chi(G0) > N gives the cover G0 x [N], which has the same parameters and no transversal.
So, in the exponent, the locally-sparse route yields beta = 2: the price is Lambda^2/log Lambda at best, against Lambda^2 ell^C now.

PROPOSITION 4 (unbounded effective uniformity; proved). Every option o lies on at least D_F(o)/n lines of size at least 2. So the average option of a main Theorem E class lies on at least c Lstar >= c' Lambda^2 nontrivial lines. Viewed as a list-edge-colouring of the hypergraph whose vertices are the lines, the hyperedge sizes are unbounded.

LEMMA G (exact accounting for greedy; proved). Let a placement of some labels avoid all pair events, and let e be unplaced. Let nu(j) be the number of placed options adjacent to (e, j) in H_F. Then each line through (e, j) carries at most one placed option, and
 #free slots of e (for the family F) = N - D_P(e) + sum_j (nu(j) - 1)_+, where D_P(e) = sum_j nu(j).
So greedy can beat N > D only through slots excluded from two or more different directions at once.

HEURISTIC H (not proved). Suppose the placed options behave like independent rare events across directions. Then a random greedy or nibble placement avoids the pair families when lambda_2 = D/N <= (1 - eps) ln N, which gives a price of about Lambda. But the higher-arity bound (14) gives lambda_3 = Lambda^(4 - 2 beta) at N = n Lambda^beta. So an ideal greedy needs beta >= 3/2 (theta(1.5) = 1.2225) unless the three-label first moment is at most n^2 Lambda^(3+o(1)).

PRICE PROVED: no improvement. The relocation price stays at Lambda^2 ell^C (T2, Theorem E). Below that, the route has an obstruction.

## Proofs

0. STATEMENT 0 (only the slot assignment changes).
- block_layout_n1.md BL1 asks only for an injective centre map X_c with N_c >= |c|, taken from I2.
- The audit restates I2 as T2's events with T2's slot counts.
- Lemma RL, as corrected in the audit, says that E_J depends only on X_c restricted to J and on s_pi, with F at every other period-zero column.
- Claims (a) to (f) use X_c only through injectivity and the avoidance of the E_J.
So any injective map that avoids every E_J, whatever produced it, yields the same layout. Only the core lengths 7N_c change. The separations D = 2W_h + 1, the collars and the J5 gluing do not depend on N_c.

1. PROPOSITION 1.
(a) An event for J = {e, f} depends only on the relative column offset X = 7(j' - j). The sea pattern is periodic mod 7 and both columns are multiples of 7. The other sea points lie within 2W_h + 1 columns, and therefore in sea, as long as both slots lie in the core. So the adjacency set of (e, j) inside L(f) is the translate j + D_ef/7, cut to [0, N). T2 counts exactly these relative geometries: G_{e,f} >= |D_ef|. The uniform bound G_max <= h^(o(1)) is the one quoted in polylog_relocation_diluted (D3).
(b) Add the n - 1 coincidences. Then sum_f G_{e,f} <= B(w), uniformly in e in C_w, by T2 (10), Theorem E (E2) or (D2).
(c) For a two-label event A = {x_f - x_e = X}, P(A) = #{j : j and j + X/7 in [0, N)}/N^2. Summing over A containing e gives sum_j D(e, j) = N^2 I_e + (coincidence terms), where I_e is e's incident two-label sum. So the average over j of D(e, j) is at least N I_e. Theorem R(a), with the audit's correct form, gives avg_e I_e >= c n Lstar / W with W = 7N. For the main Theorem E classes, the audit checked R1 >= h^(c1/2) and R2 >= h Lambda^(-14)/7, which gives Lstar >= c c1 Lambda^2.
(d) Take f with c_f congruent to a mod 28 and c_f != a. The offsets X = +-3(c_f - a)/4 both lie in D_ef (step 3 below). So mu_ef >= 2 for all these f. That is at least half the labels for e in the larger class mod 28.

2. PROPOSITION 2 (lines).
Take same-parity points with difference (X, y) = t(p, q) and (p, q) primitive. The distance is |t| l, with l^2 = p^2 + q^2, so it is integral exactly when (p, q) is a primitive Pythagorean vector.

Lemma F also needs two things:
- u+- = x + t(p +- l)/2 must be integers that are multiples of 7;
- y must be even and a multiple of 7. Both rows lie in the same block, so their rows agree mod 14.

Check of these conditions:
- If q is even, then p and l are odd, so (p +- l)/2 is an integer.
- If q is odd, the parity condition forces t to be even.
- Mod 7: X = 7 dJ forces 7 | tp. If 7 does not divide p, then 7 | t. If 7 | p, then 7 does not divide l, and u+- being multiples of 7 again forces 7 | t.
- Conversely, 7 | t with the right parity of t gives all the conditions.
- The midpoint row lies in the bulk, while F is a low row. So s0 != (a+c)/2 holds automatically.
- |u+- - x| <= 2|y| < 2h, much less than D, so u+- lie in core or separation columns, which hold F when empty.
- L <= y^2/2 + 1 <= h^2/2, so the event is within locality.

So (e, j) and (f, j') are H_F-adjacent exactly when P(f, j') - P(e, j) lies in Z w_v minus {0} for some admissible v. For a fixed v this relation is "same coset of the subgroup Z w_v", an equivalence relation, so its classes are cliques.

The other properties:
- Two distinct options determine their difference vector, hence v up to sign. So the lines are edge-disjoint and cover H_F.
- q != 0 means the row determines the position on a line. So each line meets each list at most once.
- Each option lies on exactly one coset of each Z w_v.

3. THEOREM C.
(C1) Coincidence events are events of E (T2 (17), the "+n" term). So (f, j) and (g, j) are adjacent for all f != g, and all of them are adjacent to (e, j).

(C2) Use v = (3, 4), with t = 7k and k = y/28. This gives dJ = 3k and L = 35|k|.
- For f, g in K(e, j) with c_f != c_g, the slots differ by 3(c_g - c_f)/28.
- The rows differ by y' = c_g - c_f, which is a multiple of 28.
- (3y'/28)^2 + (y'/7)^2 = (5y'/28)^2, so the scaled distance is integral, and step 2 shows that the Lemma F event holds. Here u+- = x_f + 21k' +- 35|k'|/... is computed in columns: (X +- L)/2 = 7(3k' +- 5|k'|)/2 is a multiple of 7.
- If c_f = c_g, the two options share a slot, which is a coincidence.
- The same holds with e in place of f.
- The interior condition puts every slot j + 3k with |k| <= h/28 inside [0, N).
The odd rows of Z agree mod 14, so they fall into two classes mod 28, of sizes n1 and n2. Then sum_e (A_e + 1) = n1^2 + n2^2 >= n^2/2, and every e in the larger class has A_e >= n/2 - 1.

4. COROLLARY C3.
- f_loc <= d^2/C(n-1, 2), which is at most 2.1 (d/n)^2 for n >= 50.
- (i) The ADK hypotheses, as read in the arXiv HTML: Definition 1.9 (CC3) requires H[L(u), L(v)] to be a matching. Theorem 1.13 requires 1/2 <= k <= d^((s+t)/10) and st <= alpha eps log d/loglog d, and asks for |L(v)| >= C d / log(d k^(-1/(s+t))), with C in {4 + eps, 8}.
- (CC3) fails by Proposition 1(d).
- The clique of (C1) holds C(n-1, s+t) sets of size s+t, and each contains a copy of K_(s,t). So k >= C(n-1, s+t) >= ((n - 1 - s - t)/(s+t))^(s+t). This exceeds d^((s+t)/10), because d <= n + n G_max = n^(1+o(1)) when n >= h^c.
- Formally, d k^(-1/(s+t)) <= (s+t) d/(n - 1 - s - t) <= 2(s+t) d/n. The function x/log(2(s+t)x) is increasing for large x, and d/n >= c Lstar/7, which gives the stated price.
- (ii) F-freeness fails because of K_(n-1). The label graph G contains, on each class mod 28, a complete graph, since every such pair has the offsets +-3y/4, which lie within range because 3h/28 < N.
- (iii) Let G0 have maximum degree d, neighbourhoods spanning at most d^2/f edges, and chi(G0) > N (AKS Proposition 1.2 gives such G0 for N < c d/log f). The cover V(G0) x [N], with (u, c) ~ (v, c) for uv in E(G0), has the same maximum degree, the same neighbourhood edge counts and no independent transversal.

5. PROPOSITION 4. D_F(o) = sum over v of (s_v - 1), where s_v is the size of the line of direction v through o. Since s_v <= n, at least D_F(o)/n lines have s_v >= 2. Then average with Proposition 1(c).

6. LEMMA G.
- Validity means that no line holds two placed options. Proposition 2 shows that a line through (e, j) meets each list once. So nu(j) = #{v : ell_v(e, j) contains a placed option}.
- Slot j is excluded exactly when nu(j) >= 1. Then #excluded = sum_j min(nu(j), 1) = D_P(e) - sum_j (nu(j) - 1)_+.

7. HEURISTIC H (labelled heuristic, not proved).
- If the lines through (e, j) are hit independently with probabilities s_v/N, then P(j free) is about the product of (1 - s_v/N), which is about e^(-lambda_2).
- The free slots then number about N e^(-lambda_2), which is at least 1 while lambda_2 <= ln N. That gives N of order D/ln N and a price of about Lambda^2/(2 Lambda).
- Three-label events: given f and g placed, the slots excluded for e number about the sum over J of G_J/N, which (14) bounds by n Q A(w)/N with A = Lambda^4. In the light Theorem E class (Q -> Delta h, n about Delta h) the excluded fraction is lambda_3 = n^2 Lambda^4/N^2 = Lambda^(4 - 2 beta). Keeping lambda_3 <= ln N needs beta >= 3/2. For k = 4, lambda_4 = Lambda^(4 - 3 beta), which allows beta >= 1.
- The values of theta(beta) come from the audited exponent table of relocation_price_floor.md.

## External results used

- Anderson, Dhawan, Kuchukova, 'Coloring locally sparse graphs', arXiv:2402.19271, Definition 1.9 (a correspondence cover needs (CC3): H[L(u), L(v)] is a matching, empty for non-edges; G simple). Theorem 1.13: if d >= d*, 1 <= t <= s, st <= alpha eps log d/loglog d, 1/2 <= k <= d^((s+t)/10), H is (k, K_(s,t))-locally-sparse, Delta(H) <= d and |L(v)| >= C d/log(d k^(-1/(s+t))) with C = 4 + eps or 8, then G has a proper H-colouring. Corollary 1.14 is the same for bipartite F, with k <= d^(|V(F)|/10).
- Alon, Krivelevich, Sudakov, J. Combin. Theory Ser. B 77 (1999) 73-82. Theorem 1.1: maximum degree at most d and every neighbourhood spanning at most d^2/f edges imply chi <= c d/log f. Proposition 1.2: tightness up to the constant for 2 <= f <= 2d^2. Quoted as read in the audit of three_term_relations.md, not re-read by me.
- Theorem R(a) and the separation-floor amendment from relocation_price_floor.md and its audit: the average incident two-label sum is at least c|Z| ln R2 ln min(R1, R2^(1/3))/W.
- T2 (safe_triangle_pair_first_moment.md) (10), (14), (17); Theorem E (E2) to (E5); polylog (D2) to (D4); G_max <= h^(o(1)) as quoted in polylog (D3).
- block_layout_n1.md BL1, I2 and Lemma RL, with the patches from audit_block_layout_n1.md (T2 events, T2 block map).

## Checks

Read: relocation_price_floor.md and its audit (in full); t1_cost_decomposition.md (in full) and the relevant parts of its audit (E3, E5, Theorem A); polylog_relocation_diluted.md (statements, (D2) to (D4), gaps); safe_triangle_pair_first_moment.md (T2, in full, at research_archive/2026-11-09/full_problem_push/); block_layout_n1.md (statements, BL, inputs) and its audit (the serious issues, the T2 framework fix, the I2 restatement); three_term_relations.md (its AKS citation and the audit's reading of AKS Theorem 1.1 and Proposition 1.2).

Web: ADK arXiv:2402.19271, abstract and HTML. Read: Definition 1.9 (CC1 to CC3, simple graphs), Theorem 1.13 and Corollary 1.14, including the k range. The AKS PDF was password-protected, so I relied on the audited quote.

By hand:
- the line decomposition, including the mod-7 and parity analysis of u+- and the midpoint;
- the (3,4) clique, using (3k)^2 + (4k)^2 = (5k)^2 in scaled units, u+- multiples of 7, the interior range and the mod-28 class count;
- the counting of K_(s,t) copies against ADK's range;
- the transfer from G0 x [N] in C3(iii);
- the identity of Lemma G.

Numerics: one script, run with py in under 60 s, in script folder: scripts_pairs/nbhd_lines.py. It uses a toy cover with one parity and one label per row index; conflict means dJ^2 + (2 dY)^2 is a square, or a coincidence. It counts, for the central option, the degree D, the collinear edges (line cliques) and the cross edges.

| (R, N) | D | line-edge fraction | cross fraction | random-model D/(R N) |
| --- | --- | --- | --- | --- |
| (150, 1500) | 1249 | 0.031 | 0.0156 | 0.0056 |
| (300, 3000) | 2901 | 0.024 | 0.0110 | 0.0032 |
| (500, 5000) | 5351 | 0.020 | 0.0082 | 0.0021 |

So the line cliques dominate the local density, and the cross part is polynomially sparse but about 3 to 4 times random. This is a sanity check only, at tiny Lambda. The repository was only read. No git command was run, and no report file was written.

## Gaps

- The obstruction is to a method, namely colouring theorems whose hypotheses are local sparsity, F-freeness or (d, f) alone. It is not a lower bound on the relocation price, and it does not rule out a bespoke nibble or random greedy placement that uses the line structure of Proposition 2.
- Cross-direction sparsity is unproved. The non-collinear integral triangles through an option should be at most D^2 h^(-c). That needs counts of points on genus-1 intersections of two quadrics. Only toy numerics support it: one parity, one label per row index, no T2 profile. The cross-edge density was about 3 to 4 times the random-model value D/(R N), with a slowly growing ratio.
- No published semi-random theorem covers covers of the form 'edge-disjoint lines of unbounded number (Proposition 4) plus a sparse remainder'. My remark that the hypergraph nibble theorems I know (Pippenger-Spencer, Kahn, Molloy-Reed) need bounded uniformity is from memory. I did not check it against the sources.
- Heuristic H is not proved, including the price of about Lambda for the pair families and the Lambda^(3/2) cap from three-label events. The cap uses the Cauchy-Schwarz bound (14) with A = Lambda^4 as if it were the true first moment. If the true three-label first moment is at most n^2 Lambda^(3+o(1)), the cap disappears. I did not compute it.
- AKS Proposition 1.2 (tightness for 2 <= f <= 2d^2) is quoted from the reading of the AKS PDF recorded in three_term_relations.md and its audit. My copy was password-protected, so I could not re-read it. Corollary C3(iii) depends on it; C3(i) and (ii) do not.
- I read the ADK Theorem 1.13 and Definition 1.9 hypotheses from a summary of the arXiv HTML page, not line by line. I did not check whether a multigraph or non-matching (local degree mu) version of ADK exists. Such a version would fix only the (CC3) failure, not the clique obstruction.
- (C2) is stated for interior slots, at least 3h/28 slots from the core ends. (C1) holds for every slot. Rows are assumed to be T2 bulk rows, so the midpoint is never F. That holds for the non-exceptional labels of T2 and Lemma AP.
- The other Lambda^2 pair family, the two-sea supports (a,c|s,t) of Theorem A(ii), was not analysed for line structure. The obstruction does not need it.
- The mod-p column rule (x/7 congruent to sigma' a mod p, with ((49 sigma'^2 + 1)/p) = -1) is a slot-assignment rule that kills every odd-odd integral distance at price O(1). That part is elementary. The even-even half and the effect on the T2 budgets under restricted lists are not proved, and nothing here changes because of it.
- Nothing in this note has been audited.

## Missing estimate

To get a price of Lambda^(1+o(1)) one needs two inputs, neither of which exists.
(1) An arithmetic estimate (IT). For an option o of a Theorem E block, the number of pairs of neighbours of o that are adjacent but not collinear with o (integral lattice triangles with three Pythagorean sides in three different directions) is at most D(o)^2 h^(-c).
(2) A semi-random theorem for covers H = H_lines + H_rest. H_lines is an edge-disjoint union of cliques, each meeting each list at most once. The number of lines through a vertex is unbounded, with total size D_1 and maximum line size at most D_1/K. The edges of N(o) that are not inside a line through o number at most d^2/f. The conclusion should be that lists of size (1 + eps) d / min(ln f, ln K, ln N) suffice.
Neither the local-sparsity theorems nor (as I recall) the bounded-uniformity hypergraph nibbles give (2).
Separately, the three-label first moment must be at most n^2 Lambda^(3+o(1)) per label in the light class, rather than the Cauchy-Schwarz bound n^2 Lambda^4 of (14). Otherwise even (1) and (2) cap the price at Lambda^(3/2), which is theta = 1.2225.

## Next steps

- Audit Proposition 2 and Theorem C. Both are short and elementary: the mod-7 and parity analysis of the lines, and the (3,4) clique with its mod-28 count. If they pass, record in the ledger that locally-sparse DP colouring cannot lower beta in T1-type blocks, as a method obstruction next to Theorem R.
- Compute the true first moment of the three-label events (the k = 3 roles of compatible_profile_threshold.md) in the light class. If it is at most n^2 Lambda^(3+o(1)), the higher-arity side no longer caps a greedy at Lambda^(3/2). This is a divisor-moment computation in the style of T2 (7), with no new arithmetic.
- Test (IT) numerically on a real T2 profile block: both parities, Theorem E rows 2i+1 and 2i+T+1, Delta diagonals. Measure the cross-edge density against D/(nN) as h grows, and check whether the excess over random is a power of Lambda or a power of h.
- Before attempting (2), simulate random greedy on a toy block whose pair degree D/n is well above 1. Then check that greedy succeeds at N of about D/ln N, while LLL needs N of about D. At feasible h the Lemma F degree per partner is near 1, so the toy must boost the conflict set, for example by keeping all Pythagorean offsets without the window.
- If both checks are positive, write the line-nibble: one round per epoch, with McDiarmid concentration. Each other label's choice kills at most mu_ef <= h^(o(1)) options of e, and options of e use disjoint lines (Proposition 2), so the Lipschitz constants are small. Track the list size and the line loads, and finish with T2's local lemma once D/N < 1/e.

