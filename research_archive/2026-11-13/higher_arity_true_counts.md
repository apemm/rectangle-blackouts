# Three- and four-label events in relocation blocks

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: direct third and fourth moments replace the Cauchy-Schwarz budget of T1. The three-label count is about n^2 Lambda^2 per label, set by three-corner right angles, so the local lemma or first-moment deletion needs about Lambda slots per label. Four-label events are of codimension one and cost nothing. So the higher-arity part costs Lambda, not Lambda^2, and does not block a price of Lambda per label. The pair families still cost Lambda^2 in class P, so theta* is unchanged. Not audited yet.

# Result

## Status

proved

## Summary

The three- and four-label events cost Lambda per label, not Lambda^2. Direct third and fourth moments replace T1's Cauchy-Schwarz budget. The three-label count is about n^2 Lambda^2 per label, set by three-corner right angles. The local lemma or first-moment deletion then needs m about Lambda slots per label (beta_3 = 1). That is sharp for certificates of class P on blocks without weight classes. Four-label events are codimension one, so they cost nothing. The higher-arity part is below Lambda^2 and does not block beta = 1. Pair families still cost Lambda^2 in class P, so theta* = 1.4967 is unchanged. Not audited.

## Statements

NOTATION. Lambda = 1 + log h, ell = 1 + loglog(3h). Fix one T1 profile with sea rows S = {L, F, H}. Z is the set of ordinary labels on a set H of Delta diagonals, as in Theorem E: the label f = f_{T,i} has odd row 2i+1 and even row 2i+T+1. Taking H = all diagonals gives the full label set. Put U = Delta h. Then |Z| <= U, and |Z| >= cU when every T in H has |T| <= (1-c)h. The quantities v(e), C_w = {w/2 < v <= w}, n_w and M(w) = min(1, C Lambda/w, C Lambda^3/w^2) are T1's. Put M'(w) = min(1, Lambda/w). G_J is T1's count of relative translated geometries of forbidden supports that use exactly the labels of J (compatible_profile_threshold.md Section 3; T2 Sections 2, 4 and 6). Sea points lie in rows of S, and the periodic restrictions are ignored. For Y a subset of Z, put I_k(e; Y) = sum of G_J over J containing e with |J| = k and J inside Y. A block has N slots spaced q0 apart and width W = q0 N. "m slots per label" means N = m |Z|.

LEMMA 0 (the k >= 3 events; PROVED from T1/T2's audited support classification). Every forbidden support with |J| >= 3 labels is one of four types.
 (T3) A three-black tilted right angle with one corner from each of three labels (so k = 3). G <= 4 tau(|u1 u2|), where u1 and u2 are the two nonzero vertical legs from the vertex.
 (M) A nonhorizontal, nonvertical mixed four-cell support. The cell patterns are (1,1,1) plus one sea point, or (2,1,1), for k = 3, and (1,1,1,1) for k = 4. Put y = B_y - A_y, z = C_y + D_y - A_y - B_y and w = D_y - C_y for side AB and diagonal CD. Then G <= 2 #{X != 0 : X | yz and X^2 + y^2 - w^2 is a perfect square} <= 4 tau(|yz|).
 (Hz) A horizontal mixed side. Both side cells are label cells of distinct labels in the same row, and G <= h^{o(1)}.
 (S6) The six-cell collisions of allowed triangles, as in T2 (16).
 No support with three or more labels has a side made of two sea points. A support whose side is a label's own vertical double is a two-label event of its diagonal labels, namely a vertical rival.

THEOREM 1 (direct third moment; PROVED). Uniformly in e in Z ∩ C_w,
 I_3(e; Z ∩ C_w) <= C ell U^2 Lambda^2 M'(w) + C U^2 w Lambda M(w) + C U h Lambda^2 + U^2 h^{-1+o(1)}.
Without weight classes, I_3(e; Z) <= C U^2 (ell Lambda^2 + v(e) Lambda) + C U h Lambda^2.

THEOREM 2 (four-label events have codimension one; PROVED). Uniformly in e in Z, I_4(e; Z) <= U^3 h^{-1+o(1)}.

PROPOSITION 3 (the three-label order is sharp; PROVED). Call Z rich if every odd row r in [h/3, 2h/3] is the odd row of at least c1 |Z|/h labels of Z. The full label set is rich, and so is any union of diagonals with |T| <= h/4. Let Z be rich, let 1 <= q0 <= h^{1/2}, and let e have odd row in [2h/5, 3h/5]. Then the T3 geometries with vertex at e, label offsets in q0 Z and |offsets| <= h^2/(400 q0) number at least c c1^2 |Z|^2 Lambda^2/q0^2. In particular I_3(e; Z) >= c |Z|^2 Lambda^2. So T1's Cauchy-Schwarz budget (nQ) Lambda^4 for k = 3, with n of order Q, overcounts the true Q^2 Lambda^2 by a factor of Lambda^2.

THEOREM 4 (the local-lemma price of the higher-arity part; PROVED modulo the audited T1/T2/Theorem E inputs). In T1 and in Theorem E, the term sqrt(n_w Delta h) sqrt(A(w)) of N_w (T1 (8), Theorem E (E4)) can be replaced by
 H(w) = C ell^{1/2} [Delta h Lambda M'(w)^{1/2} + Delta h (w Lambda M(w))^{1/2} + Delta^{1/2} h Lambda + Delta h h^{-1/3+o(1)}],
and the product-form local lemma still certifies every class block. Moreover sum over w of H(w) <= C (Delta h Lambda ell^{3/2} + h^2). So the higher-arity part costs Lambda^{beta_3} per relocated label, up to ell^{3/2}, with beta_3 = 1. For the four-label part alone the price is beta_4 = 0. Both are below Lambda^2. T1's total stays C h^2 Lambda^2 ell^C, because the pair budget B(w) is unchanged.

PROPOSITION 5 (first-moment deletion and spread placements; PROVED). Call a random placement of Z into N slots K-spread if, for distinct labels, P(x_e = xi_1, x_f = xi_2, x_g = xi_3) <= (K/N)^3, and likewise (K/N)^4 for four labels. Independent uniform slots are 1-spread. Then
 E[#three-label events] <= C K^3 ell Lambda^2 U^3/N^2 and E[#four-label events] <= K^4 U^4 h^{-1+o(1)}/N^3.
Delete one label of each event. Every other event of E stays absent, because T1's events depend only on the positions of their own labels (they are defined with all other slots empty). In expectation at most delta |Z| labels are deleted once N >= C K^{3/2} (ell/delta)^{1/2} Lambda U. The deleted labels are placed again in a new block of the same type, so the widths form a geometric series. No weight classes are needed for this step.

PROPOSITION 6 (floor for class P at k = 3; PROVED for blocks without weight classes). Let the block be of class P as in the amended class P of audit_relocation_price_floor.md: i.i.d. uniform slots spaced q0 <= h^{1/2}, T1's event system, and a certificate that depends only on (P(A), the shared-label dependency graph). Suppose Z is rich and W >= h^2, with the block inside the board. Then every such certificate needs W >= c Lambda |Z|. First-moment deletion that keeps (1 - delta)|Z| labels needs W >= c Lambda |Z| delta^{-1/2}. So beta_3 = 1 is exact for these methods.

REMARK 7 (HEURISTIC, unproved). Consider a random sequential greedy placement, in which each new label takes a uniformly random slot that creates no event with the labels already placed. Suppose the earlier positions behave like independent uniform ones. Then the fraction of slots blocked by triples is about 1 - exp(-lambda_3), where lambda_3 = I_3/N^2, which is about Lambda^2/m^2. Greedy then survives while lambda_3 <= ln N, about 2 Lambda. This gives a heuristic price of m about Lambda^{1/2} for the higher-arity part.

ANSWER TO THE TARGET.
- True count: I_3 is of order U^2 Lambda^2 per label, up to ell and private v(e) terms, and the T3 right angles carry it. I_4 <= U^3 h^{-1+o(1)}.
- Smallest m: Lambda, up to ell^{1/2}, by the local lemma or by deletion. This is sharp for class-P certificates on blocks without weight classes. Lambda^{1/2} is heuristic for greedy placement.
- Proved price: beta_3 = 1, below Lambda^2.
- Consequence: in T1's accounting (t1_cost_decomposition Theorem A) the higher-arity source drops from Lambda^2 to Lambda. T1's Lambda^2 now comes only from pair events: rivals (Lambda by Lemma V, unweighted), the label-sea Lemma F family (floor Lambda^2 in class P by Theorem R), and the private w Lambda term. At beta = 1 the higher-arity part alone would allow exponent min_a E(a)/(1+a) = 0.910. The exponent theta* = 1.4967 does not move, because the pairs still cost Lambda^2 in class P.

## Proofs

0. ELEMENTARY DIVISOR INPUTS. These are used uniformly in the constant terms, with tau_+(0) = 1 and every coefficient a, b in {±2, ±4}.
(D1) Let phi(i) = a i + u with |u| <= 3h, and let i run over an interval of length <= h. Then sum tau_+(|phi(i)|) <= C h Lambda, because the values are distinct and of size <= 7h, so Dirichlet applies. Also sum tau(phi(i)^2) <= C h Lambda^2, because tau(n^2) = sum over d | n of 2^{omega(d)}, so sum over n <= x of tau(n^2) <= x prod over p <= x of (1 + 2/(p-1)), which is << x log^2 x by Mertens.
(D2) Let D = av - bu != 0. Then sum over i <= h of tau(|ai+u|) tau(|bi+v|) <= C h Lambda^2 sigma_{-1}(|D|) + C h <= C h Lambda^2 ell.
 Proof. Use tau(n) <= 2 #{d | n : d <= sqrt n} with n <= Ch, and put D0 = sqrt(Ch). If d1 | ai+u and d2 | bi+v, then g = gcd(d1, d2) divides b(ai+u) - a(bi+v) = -D. The i satisfying both conditions lie in one class modulo lcm(d1/gcd(a,d1), d2/gcd(b,d2)), which is at least d1 d2/(16 g). So there are at most 16 h g/(d1 d2) + 1 of them. Summing over d1, d2 <= D0 with g | D gives at most 64 h sum over g | D of (1/g)(1 + log D0)^2 + 64 D0^2. Finally sigma_{-1}(n) << loglog n (Gronwall) <= C ell for n <= Ch.
(D3) (LEMMA C1) Let pi be an endpoint and let |u| <= 2h with u not in S. Then
 sum over f in Z ∩ C_w of tau_+(|rho_pi(f) - u|) <= C ell Delta h Lambda M'(w) + C h Lambda.
 Proof. The unweighted sum is <= C Delta h Lambda by (D1) on each diagonal. Use 1_{C_w}(f) <= 2 v(f)/w and expand v(f) = 1 + sum over r in f and t in S of tau(|r - t|).
 - Same-endpoint products: on each diagonal they are pairs of distinct forms with D = 2(u - t) != 0, since u is not in S. So (D2) gives C h Lambda^2 ell.
 - Other-endpoint products: the forms coincide only when T = ±(t - u), which is at most 6 diagonals. On those diagonals use the unweighted bound C h Lambda.
 So the sum is <= min(C Delta h Lambda, (2/w) C Delta h Lambda^2 ell) + 6 C h Lambda.
 If u is in S, then tau(|rho_pi(f) - u|) <= v(f) <= w. This is the private case, handled in step 2.
(D4) Two inputs are quoted from audited notes: n_w <= C Delta h M(w) (Theorem E (E1), with Q replaced by Delta h), and sum over e in Z of v(e) <= C U Lambda (which also follows from (D1)).

1. LEMMA 0. Take a support with k >= 3 labels.
- Three-corner type: there are three corners, and each of the k = 3 labels needs at least one, so each label supplies exactly one. A right angle at A with corners B and C has X_B X_C = -(y_B - y_A)(y_C - y_A). Both legs are nonzero, because a zero vertical leg forces an axis rectangle or two corners in one column. So G <= 2 tau(|u1 u2|) for each choice of vertex and endpoints.
- Four-cell types: the side AB and the diagonal CD have two cells each. If AB has two sea cells, only two cells remain for at least three labels, which is impossible.
- Vertical side: AB is a label double, at column x_g. The rectangle R1 has its far side at x_g + X', and X' = (x_C + x_D)/2 - x_g is free. So the support exists for every position of g, and the event depends only on the diagonal labels. It is a vertical rival of that pair, already in B(w).
- Horizontal side: a label row is never a sea row (bulk rows), and the side cannot be two sea cells, so both side cells are labels in one row. They lie in distinct columns, so they belong to distinct labels. (N) gives (X - X')(X + X') = d^2 with d != 0, so G <= 4 tau(d^2) <= h^{o(1)}.
- Nonhorizontal, nonvertical side: (P) reads X S = -yz, with X = X_B - X_A != 0 and S = X_C + X_D - X_A - X_B. (N) reads X'^2 = X^2 + y^2 - w^2, with X' = X_D - X_C. So X divides yz and X^2 + y^2 - w^2 must be a perfect square. The pair (X, sign of X') then fixes all relative columns, which gives the bound in (M). Also z = 0 forces S = 0, which makes R1 degenerate, so z != 0.
- Six-cell collisions are T2's (15) and (16).
The completeness of this list is T2 Section 2 together with compatible Section 3, both audited.

2. THEOREM 1. Fix e, with cell rows alpha (or a and b), in C_w. The other labels are f, with cell row gamma (or c and d), and g, with cell row rho (or rho and rho'). Bound tau(|yz|) by tau(|y|) tau(|z|), except where noted. In each role, first sum the label g unrestricted, using (D1) or (D2), uniformly in everything else. Then sum the label f over C_w, using (D3) or n_w. Where the roles of f and g are mirror images, swap them.
(a) T3, vertex at e: tau(gamma - alpha) tau(rho - alpha). Summing over g gives C U Lambda by (D1). Summing over f in C_w with u = alpha (D3) gives C ell U Lambda M' + C h Lambda.
 T3, vertex at f: tau(alpha - gamma) tau(rho - gamma). This is the same: g first, then (D3) for f.
 T3, vertex at g: the mirror image.
(b) Pattern (1,1,1) plus a sea point s.
 - Side {alpha, s}: tau(y) <= v(e) <= w. Then Sum_g tau(z) <= C U Lambda and Sum over f in C_w of 1 is n_w <= C U M(w). This gives C U^2 w Lambda M(w).
 - Side {gamma, s} or {rho, s}: tau(y) <= v(f) or v(g), which is <= w, and the bound is the same.
 - Side {alpha, gamma}: z = rho + s - alpha - gamma. Sum over g with (D1), then (D3) for f.
 - Side {alpha, rho}: the mirror image.
 - Side {gamma, rho}: y = rho - gamma and z = alpha + s - gamma - rho are two forms in i_g with D = 2(alpha + s - 2 gamma). So (D2) gives C U Lambda^2 ell, then n_w <= C U M(w).
 On the slice 2 gamma = alpha + s, which holds for at most Delta labels f, the two forms coincide. There tau(y^2) and (D1) give C Delta U Lambda^2 <= C U h Lambda^2.
(c) Pattern (2,1,1).
 - e is the double:
   - Sides {a or b, gamma}: g first, then (D3).
   - Side {gamma, rho}, diagonal {a, b}: the two forms in rho coincide only if 2 gamma = a + b. But a + b is odd, so this never happens. Then (D2) and n_w.
 - f is the double:
   - Sides {alpha, c} and {alpha, d}: z = rho - alpha ± T_f, so g first, then (D3).
   - Side {alpha, rho}, diagonal {c, d}: the forms coincide only if c + d = 2 alpha, which parity forbids. Then (D2) and n_w.
   - Sides {c, rho} and {d, rho}: the forms coincide only on the slice c = alpha ± T_f, which is one i_f per diagonal. Then (D2), n_w and the slice bound.
 - g is the double:
   - Side {alpha, rho}: y depends only on g, and z = gamma - alpha ± T_g depends only on f and T_g. Sum i_g by (D1), then f by (D3) with u = alpha ∓ T_g. If u is in S, which happens for at most 6 diagonals T_g, the private bound gives C U h w Lambda M(w), which is <= C U^2 w Lambda M(w).
   - Side {gamma, rho}: the same argument.
   - Side {alpha, gamma}, diagonal {rho, rho'}: z has coefficient 4 in i_g, so g first, then (D3).
 - A side consisting of a label's own double is vertical, so it is excluded.
(d) Hz roles: one label is confined to a row, which leaves at most Delta choices, and G <= h^{o(1)}. This gives Delta U h^{o(1)} = U^2 h^{-1+o(1)}.
(e) S6 roles: (Delta h)^2 h^{-1+o(1)}, quoted from Theorem E (E3) and T2 (16).
Summing the boundedly many roles proves the classed bound. The unclassed bound is the same proof with 1_{C_w} <= 1 and v(f) <= v_max replaced by the role's own private label. Every private factor there is tau(|r - t|) for a cell r of one label, and the sum over e uses (D4).

3. THEOREM 2. M roles, pattern (1,1,1,1). e has one fixed cell and the other three cells come from f, g and q.
- The map (A_y, B_y, C_y, D_y) -> (y, z, w) has kernel spanned by (1,1,1,1). So once e's cell is fixed, (i_f, i_g, i_q) -> (y, z, w) is injective into |y|, |w| <= h, |z| <= 2h, for each T-tuple.
- It suffices to bound Sigma := the sum over that box of #{X != 0 : X | yz, X^2 + y^2 - w^2 a square}. Put R = w^2 - y^2.
- (i) R = 0, that is w = ±y. The sum is at most Sum_y 2 tau(y) Sum_z tau(z) <= C h^2 Lambda^2.
- (ii) R != 0. Then X lies in sol(R) = {X : X^2 - R is a square}, and |sol(R)| <= 2 tau(|R|). Also #{z : X | yz} <= 4h gcd(X, y)/|X| + 1. The "+1" part is at most Sum over (y, w) of 2 tau(|w - y|) tau(|w + y|) <= C h^2 Lambda^2.
- The main part is 4h Sum over (y, w) of Sum over X in sol(R) of gcd(X, y)/|X|. Exchange the sums. For fixed (y, X), the number of w with X in sol(w^2 - y^2) is at most r_2(X^2 + y^2) <= 4 tau(X^2 + y^2) <= h^{o(1)}, because |X| <= h^2.
- So the main part is <= h^{1+o(1)} Sum over |y| <= h of Sum over d | y of d Sum over d | X, |X| <= h^2 of 1/|X| <= h^{1+o(1)} Sum_y tau(y) Lambda = h^{2+o(1)}.
- So each T-tuple contributes h^{2+o(1)}, and the Delta^3 tuples give Delta^3 h^{2+o(1)} = U^3 h^{-1+o(1)}.
Hz roles give Delta U^2 h^{o(1)} = U^3 h^{-1+o(1)}. S6 roles give U^3 h^{-1+o(1)} (quoted). There are no T3 roles at k = 4.
Check: k4_integrality.py shows Sigma/(sum over the box of tau(|yz|)) times h equal to 3.98, 4.55, 5.07 and 5.41 at h = 20, 40, 80 and 120. That is about Lambda^{O(1)}/h, as proved.

4. PROPOSITION 3. Put Y = floor(h/(40 q0)). Take f's odd row alpha + 2 q0 U1 and g's odd row alpha - 2 q0 V1, with 1 <= U1, V1 <= Y. These rows are odd and lie in [h/3, 2h/3], so there are at least c1 |Z|/h choices of f and of g for each.
- Take X_f = 2 q0 X1 and X_g = 2 q0 X2 with X1 X2 = U1 V1 and X1 != X2. Then X_f X_g = -(gamma - alpha)(rho - alpha). The fourth corner has row alpha + 2 q0 (U1 - V1), which is in the grid. There is no sea corner, so the configuration is a forbidden three-black tilted rectangle; if the fourth corner is also black, it is hidden and still forbidden.
- Count the pairs (X1, X2) with the injective map (alpha', beta, gamma', delta) -> (U1, V1, X1, X2) = (alpha' beta, gamma' delta, alpha' gamma', beta delta), restricted to gcd(beta, gamma') = 1. It is injective because alpha' = gcd(U1, X1).
- So the count is >= Sum over coprime (beta, gamma') of floor(Y/beta) floor(Y/gamma') >= (Y^2/4)(1 - Sum_p p^{-2}) H_Y^2 >= 0.136 Y^2 log^2 Y. Check: t3_count.py found this count exactly equal to Sum over u, v <= x of tau(uv), with ratio to x^2 log^2 x between 0.84 and 0.75 for x = 50 to 400.
- The cases X1 = X2 force U1 V1 to be a square, and there are at most C Y log^2 Y of them.
- Multiplying, the count is >= c c1^2 (|Z|/h)^2 Y^2 Lambda^2 >= c' |Z|^2 Lambda^2/q0^2, since log Y >> Lambda when q0 <= h^{1/2}.

5. THEOREM 4. The events of a class block are:
- pairs: incident sum <= B(w)/N (T2 (10), unchanged);
- triples: I_3/N^2;
- quadruples: I_4/N^3;
- coincident slots: n_w/N.
Each event A on k labels has P(A) <= N^{-(k-1)}. Take N_w = C0 (B(w) + H(w) + n_w + 1), where H(w) >= sqrt(I_3^max) + (I_4^max)^{1/3} by Theorems 1 and 2. Then every label's incident sum is at most 4/C0 <= 1/32. Take x_A = 2 P(A). Each event has at most 4 labels, so the product over B ~ A of (1 - x_B) is at least 1 - 4(2/32) >= 1/2, and the local lemma (T2 (17)) applies. Blocks are separated as in T1 and (E5), so there are no cross-block events.
Summing H(w) over the classes:
- Sum over w of M'(w)^{1/2} << ell: there are O(ell) classes with w <= Lambda, and a geometric tail above.
- Sum over w of (w M(w))^{1/2} << Lambda^{1/2} ell (T1 (10)).
- With dyadic classes up to Lambda^3 and coarse groups above (E5), there are O(ell) blocks. So the Delta^{1/2} h Lambda terms sum to at most ell Delta^{1/2} h Lambda <= Delta h Lambda ell.
- Coarse groups (W, W^{4/3}] give the same bounds, with private term (Delta h)^2 Lambda^4 W^{-2/3}, whose root is Delta h Lambda^2 W^{-1/3} <= Delta h Lambda.
- In T1's original O(log h) dyadic classes these terms are at most h^{3/2} Lambda^2, which is << h^2.

6. PROPOSITION 5. Each event (J, geometry) has probability <= N (K/N)^k, by summing over e's slot. So
 E[#three-label events] <= (K^3/(3 N^2)) Sum_e I_3(e; Z) <= C K^3 U^2 (ell Lambda^2 |Z| + Lambda Sum_e v(e)) / N^2 + C K^3 |Z| U h Lambda^2/N^2,
which is <= C K^3 ell Lambda^2 U^3/N^2 by (D4). The four-label bound follows the same way from Theorem 2.
Monotonicity: an event of E is the event that J's labels realise a geometry. Supports that use empty-slot sea points count with all other slots empty. So after deletions, any support in the final configuration is an event of a subset of the survivors. That event already occurred in the original placement, and one of its labels was deleted.

7. PROPOSITION 6.
- Every geometry of Proposition 3 has |offsets|/q0 <= N/4 and its fourth corner inside the block, because W >= h^2. So it has probability >= (N/2)/N^3 = 1/(2N^2) when e's slot lies in the middle half.
- Hence the incident sum of e is >= c |Z|^2 Lambda^2/(q0^2 N^2).
- All events containing e share x_e, so they form a clique. The clique case of Shearer, as in Theorem R (b), shows that a (P, G)-certificate needs this sum to be < 1. Hence N > c |Z| Lambda/q0, that is W > c Lambda |Z|.
- Rich sets have at least c1 |Z|/10 labels with odd row in [2h/5, 3h/5]. So E[#events] >= c |Z|^3 Lambda^2/(q0^2 N^2), which gives the bound for deletion.

8. REMARK 7. This is heuristic only. The excluded-fraction computation is the one stated. The reason it is not proved is in Gaps.

9. CONSEQUENCES. Theorem A of t1_cost_decomposition lists sources (i), (ii) and (iii) and a higher-arity budget at Lambda^2. Theorem 4 lowers the higher-arity budget to Lambda ell^{3/2}. The exponent table of relocation_price_floor gives theta(1) = 0.9101 = min_a (1 + 3^a)/(2(1 + a)), at a about 0.45. So the higher-arity part allows that exponent. The binding cost stays the pair family of Lemma F, which Theorem R prices at Lambda^2 in class P.

## External results used

- Dirichlet's divisor bound: sum over n <= x of tau(n) <= x(1 + log x).
- The identity tau(n^2) = sum over d | n of 2^{omega(d)} with Mertens' product: sum over n <= x of tau(n^2) << x log^2 x.
- tau(n) <= 2 #{d | n : d <= sqrt n}, the elementary device behind (D2).
- Gronwall: sigma(n)/n << loglog n.
- The divisor bound tau(n) = n^{O(1/loglog n)}.
- r_2(n) <= 4 tau(n).
- Sum over primes of p^{-2} < 0.4523.
- Lovasz local lemma, product (asymmetric) form, as in T2 Section 7.
- The clique case of Shearer's criterion, used exactly as in Theorem R(b) of relocation_price_floor.md (elementary: disjoint events with total probability >= 1 cover the space).
- Internal inputs that are audited: T1 (3), (5), (7), (9), (10); T2 Sections 2, 4 and 6 with (10) and (16); compatible_profile_threshold Section 3 (role analysis); Theorem E (E1), (E3) six-cell count and (E5) coarse groups; class P (amended) and Theorem R of relocation_price_floor and its audit.

## Checks

I wrote two scripts in my script folder and ran each once with py, in well under 60 seconds. They are sanity checks, not proofs. I did not modify any repository file, and I ran no git command. I used no web source.

(1) k4_integrality.py counts four-cell supports with the integrality condition on full boxes |y|, |w| <= h, |z| <= h. It compares the true count, sum over the box of #{X : X | yz, X^2 + y^2 - w^2 a square}, with T1's bound tau(|yz|).

| h | true/tau | (true/tau) * h | true/(h^2 Lambda^2) |
|---|---|---|---|
| 20 | 0.199 | 3.98 | 17.3 |
| 40 | 0.114 | 4.55 | 19.8 |
| 80 | 0.063 | 5.07 | 22.1 |
| 120 | 0.045 | 5.41 | 23.8 |

The ratio decays like Lambda^{O(1)}/h, which is the codimension-one saving of Theorem 2.

(2) t3_count.py compares sum over u, v <= x of tau(uv) with the coprime-quadruple count of Proposition 3, for x = 50, 100, 200 and 400. The two counts are exactly equal. Their ratio to x^2 log^2 x is 0.843, 0.807, 0.774 and 0.753. This confirms that the lower-bound map is injective and the order is log^2.

I re-derived by hand: (D2) including the class count mod lcm; Lemma C1; every k = 3 role and its summation order, with the coincidence slices and their parity exclusions; the injectivity of (rows) -> (y, z, w) at k = 4; the class sums of H(w); the local-lemma constants; and min_a (1 + 3^a)/(2(1 + a)) = 0.910.

I read, from the 2026-11-09 full_problem_push folder: safe_triangle_pair_first_moment.md, compatible_profile_threshold.md, two_moment_threshold_refinement.md and sharper_polylogarithmic_threshold.md. From the 2026-11-13 folder I read t1_cost_decomposition.md, relocation_price_floor.md and their audits, plus the higher-arity parts of polylog_relocation_diluted.md and its audit.

## Gaps

- Nothing here is audited. All proofs were re-read only by me.
- Lemma 0 relies on the completeness of T1/T2's forbidden-support list (T2 Section 2, compatible Section 3), which is audited. I derived the k >= 3 sublist myself: no sea-sea sides, vertical sides are two-label rivals, horizontal sides are confined to a row, and z != 0.
- Two inputs are quoted without re-derivation. The six-cell bound (Delta h)^{k-1} h^{-1+o(1)} comes from Theorem E (E3) and T2 (16); the original was checked by inspection, and its audit agreed. The class-size bound n_w <= C Delta h M(w) comes from (E1), which is audited.
- Proposition 6, the floor for class P at k = 3, is proved only for blocks without weight classes, for rich Z and for W >= h^2. With T1's weight classes, the lower bound for the restricted count sum over f, g in C_w is not proved. It is plausible, because the class-weight forms are independent of the geometric forms.
- Remark 7 (price Lambda^{1/2} for random greedy placement) is heuristic. One obstacle: pairs of labels that sit close together, |x_f - x_e| = q0 t with t small, have codegree about U Lambda/t in the three-label system. That breaks the near-independence the heuristic assumes and the linear or low-codegree hypotheses of known sparse-hypergraph colouring theorems. I checked none of those theorems.
- Proposition 5 combines with a pair method only if that method's output is K-spread with K polylogarithmic. The greedy pair heuristic at price Lambda leaves a fraction of about h^{-c} of the slots free, so it gives K = h^{c}. So no combined method at beta = 1 is proved; the higher-arity part is just not the obstacle.
- For k = 3, the integrality condition (X^2 + y^2 - w^2 a square) of type (M) is not used. That is harmless, because the T3 family already has full order Lambda^2. The same integrality idea for the two-label two-sea supports R1 and R2 (the gap of relocation_price_floor) is not done here. Those roles have no free translation direction, so the method of Theorem 2 does not apply directly.
- The exponent theta* = 1.4967 is unchanged. This note removes the higher-arity part as a Lambda^2 source but does not lower the pair price in class P.

## Missing estimate

To lower the relocation exponent below theta* = 1.4967, the binding estimate is still a pair estimate. One needs a placement outside class P that avoids the Lemma F family (same-parity label points at integral distance, with sea points on empty slots) at o(Lambda^2) per label. That placement must also be K-spread with K = Lambda^{O(1)} in the sense of Proposition 5, so that the three-label events can be removed afterwards at price K^{3/2} Lambda. Alternatively, one needs a single sequential or nibble analysis that handles pairs and triples together. On the higher-arity side, the remaining question is whether a sequential or semi-random placement beats Lambda for the T3 family. That needs control of the codegree of close label pairs, which is about U Lambda/t at slot distance t.

## Next steps

- Audit Theorems 1 and 2 and Proposition 6. Each is short and elementary given (D1) to (D3). The role list of step 2 is the main thing to check.
- If the audit passes, update t1_cost_decomposition Theorem A and consolidated_board_v3 (H2b and the heavy term): the higher-arity budget becomes C ell^{3/2} Delta h Lambda + C h^2. Also add a ledger row: three- and four-label events cost Lambda per label, and four-label events have codimension one.
- Apply the integrality method of Theorem 2 to the two-label nonhorizontal two-sea supports R1 and R2, which is the open gap of relocation_price_floor. A codimension-one bound there would show that the Lemma F horizontal family alone carries the label-sea source (ii).
- Prove the class-restricted lower bound: sum over f, g in C_w of the T3 count >= c n_w^2 Lambda^2 for the dominant classes. That would make beta_3 = 1 exact for T1's own construction.
- Try to make Remark 7 rigorous for the T3 family. First forbid label pairs at slot distance below epsilon m, which is a cheap pair constraint, to cap the codegrees. Then run a semi-random (nibble) analysis on the three-label system. The target is m of about Lambda^{1/2 + o(1)} for the higher-arity part.
- Explore the joint question: is there a pair method at price below Lambda^2 that is Lambda^{O(1)}-spread? If so, Proposition 5 adds the higher-arity part at no extra exponent.

