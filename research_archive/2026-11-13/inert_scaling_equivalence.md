# The estimate (E) is equivalent to bounded chromatic numbers

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Not audited yet.

# Result

## Status

obstruction

## Summary

(E) is equivalent to a much stronger statement: every diagonal graph G_T(h), at every height, has chromatic number at most C. The reason is that an inert prime q (q = 2, 3 mod 5) gives S_{qT}(qh) = q S_T(h) exactly, so k stays fixed while log h grows. Even (E) restricted to rich diagonals forces chi to be bounded on rich diagonals. The random model and the data both point the other way, so (E) is very likely false and is the wrong per-diagonal target. A multiscale version of (E) is consistent with these embeddings, and its total is about 1.05h numerically.

## Statements

NOTATION. These follow the setting. Q(T,d) = 20d^2 + 4Td + T^2. For real x > 0, S_T(x) = { d != 0 : Q(T,d) = L^2, 0 < L < x }. n_T(h) = |I_T|. D_T(h) = { |d| : d in S_T(h), |d| < n_T(h) }, k_T = |D_T(h)|, and G_T(h) is the distance graph of D_T(h) on I_T. Explicitly n_T(h) = floor(h/2) - (T-1)/2 for T > 0 and ceil(h/2) - (|T|+1)/2 for T < 0. An INERT prime is a prime q = 2 or 3 mod 5. rho(n) = prod over p^a || n of (2a+1).

THEOREM A (parametrization) [proved]. For odd T and real h > 0, the map (g,x,y) -> d = gxy/2 is a bijection from R_T(h) = {(g,x,y) in Z^3 : g >= 1, y >= 1, x != 0, gcd(x,y) = 1, gxy even, g(y^2 - xy - x^2) = T, g(x^2+y^2) < h} onto S_T(h). The corresponding L is g(x^2+y^2). Exactly one of x, y is even. Every d in S_T has |d| >= sqrt(|T|/12).

LEMMA B (divisibility) [proved]. (i) If q >= 1 divides T, then S_T(h) ∩ qZ = q S_{T/q}(h/q). (ii) If q is an inert prime dividing T, then S_T(h) = q S_{T/q}(h/q): every distance is a multiple of q.

LEMMA C (embedding) [proved]. Let q >= 1 be odd, T' odd, h' >= 2 with n_{T'}(h') >= 1, T = qT' and h = q(h'+2). Then G_{T'}(h') is isomorphic to a subgraph of G_T(h). So chi(G_T(h)) >= chi(G_{T'}(h')) and k_T(h) >= k_{T'}(h'). Also chi(G_T(h)) is nondecreasing in h.

LEMMA D (bounded k on the scaled family) [proved]. In the setting of Lemma C:
(a) If q is an inert prime, k_T(h) <= |S_{T'}(h'+2)|.
(b) If q is any odd prime, k_T(h) <= K(T',h') := |S_{T'}(h'+2)| + 4 rho(T') (1 + 2.078 log(3.618 (h'+2)/|T'|)).
Neither bound depends on q.

THEOREM E (equivalence) [proved]. For a constant C > 0 the following are equivalent:
(E_C) chi(G_T(h)) <= C (1 + k_T(h)/log h) for every h >= 2 and every diagonal T.
(U_C) chi(G_T(h)) <= C for every h and every diagonal T.
So (E) of (missing estimate (E)) holds iff the chromatic numbers of all diagonal graphs, at all heights, are uniformly bounded. If some diagonal has chi(G_{T'}(h')) > C, then (E_C) fails along the explicit family T = qT', h = q(h'+2), q inert, q -> infinity, where k_T stays bounded.

COROLLARY F (rich version) [proved]. Suppose chi(G_T(h)) <= C(1 + k_T/log h) holds only for the diagonals with k_T >= log h. Then every (T',h') with k' := k_{T'}(h') >= log(6(h'+2)) satisfies chi(G_{T'}(h')) <= C (1 + K(T',h')/(k' - log 2)). On the computed rich diagonals K(T',h') is about 3k'. So (E) even on rich diagonals forces bounded chi on rich diagonals.

LEMMA G (finite ratio bound) [proved]. Let E be a subset of {1,...,n-1} with |E| = k >= 1, and suppose sum_{d in E} cos(2 pi d theta) >= -lambda for all theta. Then the distance graph of E on n consecutive integers has independence number at most 6.63 n lambda/k, so its chromatic number is at least k/(6.63 lambda).

LEMMA H (blocks) [proved, elementary]. For every B >= 1, chi(G_T(h)) <= ceil(n_T/B) chi(distance graph of D_T ∩ [1,B) on I_T). With the parity Riesz lemma of continuation_arc_parity_riesz.md: if D_T ∩ [1,B) satisfies the even-relation condition (6) at cap m(|D_T ∩ [1,B)|), then chi(G_T(h)) <= 4 ceil(n_T/B).

PROPOSITION I (stripping a large prime) [proved, assuming the large prime corollary = Corollary 4.1(1) of three_term_relations.md, which is still under audit]. If p is a prime dividing T with p >= 19 h^(2/3), then chi(G_{T/p}(floor(h/p) - 2)) <= chi(G_T(h)) <= 3 chi(G_{T/p}(ceil(h/p) + 3)). The lower bound is unconditional, by Lemma C.

NOT PROVED: (U) false, that is sup chi(G_T(h)) = infinity. So (E) is not disproved, only shown equivalent to (U). Also not proved: sum_T chi(G_T) = o(h log h/log log h), and the corrected multiscale target below.

CORRECTED TARGET (conjecture, compatible with Lemmas B and C): (E_ms) chi(G_T(h)) <= C max over q | T, q <= h/3, of (1 + K_q/log(h/q)), where K_q = #{delta in D_T : q | delta}. q = 1 gives (E).

## Proofs

Status labels: [proved] means a complete argument that I re-read line by line, with no independent audit. [computed] means a sanity-check script.

1. THEOREM A [proved]
(Converse direction.) Take (g,x,y) in R_T(h) and put d = gxy/2. Then T = g(y^2 - xy - x^2) and
Q(T,d) = g^2 [5x^2y^2 + 2xy(y^2 - xy - x^2) + (y^2 - xy - x^2)^2].
Expand (y^2 - xy - x^2)^2 = y^4 - x^2y^2 + x^4 - 2xy^3 + 2x^3y. Then add 2xy^3 - 2x^2y^2 - 2x^3y and 5x^2y^2. The total is y^4 + 2x^2y^2 + x^4. So Q(T,d) = (g(x^2+y^2))^2, with L = g(x^2+y^2) in (0,h). Also d != 0 and d is an integer because gxy is even. So d is in S_T(h).

(Main direction.) Let d be in S_T(h) with L > 0. L and T are odd, so t' := (L - T - 2d)/2 is an integer. Then L = T + 2d + 2t', and
L^2 = T^2 + 4Td + 4d^2 + 4t'(T + 2d + t').
Setting this equal to T^2 + 4Td + 20d^2 gives t'(T + 2d + t') = 4d^2. Put t'' = T + 2d + t'. Then t' t'' = (2d)^2 > 0 and t' + t'' = L > 0, so both are positive. Let g = gcd(t',t''). Then g^2 divides 4d^2, so g divides 2d, and t'/g, t''/g are coprime with square product (2d/g)^2. So each is a square: t' = gx^2 and t'' = gy^2 with y >= 1 and gcd(x,y) = 1. Choose the sign of x so that 2d = gxy. Then T = t'' - t' - 2d = g(y^2 - x^2 - xy) and L = t' + t'' = g(x^2+y^2) < h. Also gxy = 2d is even and x != 0.

(Uniqueness.) d determines L > 0, then t' and t'', then g, then x^2 and y^2, then the sign of x. So the map is a bijection.

(Parity.) T is odd, so g is odd and y^2 - xy - x^2 is odd. If x and y were both odd, gxy would be odd. So exactly one of x, y is even.

(Lower bound on |d|.) |y^2 - xy - x^2| <= x^2 + |xy| + y^2 <= 3x^2y^2 because |x|, |y| >= 1. So 4d^2 = g^2x^2y^2 >= g|T|/3 >= |T|/3.

[computed] param_check.py compares Theorem A with the definition by brute force at h = 150, 301 and 400 (every odd |T| < h; 204, 472 and 654 pairs (T,d)). It finds 0 mismatches and 0 violations of |d| >= sqrt(|T|/12).

2. LEMMA B [proved]
(i) If q | T and q | d, then q^2 divides Q(T,d) = L^2, so q | L. Hence Q(T/q, d/q) = (L/q)^2 with 0 < L/q < h/q. Conversely, Q(T, qd') = q^2 Q(T/q, d') by homogeneity.
(ii) Let q be inert. By quadratic reciprocity, (5/q) = (q/5) = -1. Reduce Q(T,d) = L^2 modulo q: 5(2d)^2 = L^2 mod q. If q did not divide d, then 5 = (L (2d)^(-1))^2 mod q, which contradicts (5/q) = -1 (q is odd). So q | d, and (i) applies.
[computed] scaling_check.py confirms that for q = 3, 7, 10007, 100003 (all inert), k_{qT'}(q(h'+2)) = k_{T'}(h') for T' = 1045, -1045, 6061, 11 (the last with one extra distance coming from height h'+2).

3. LEMMA C [proved]
Let T' > 0. Then n' = n_{T'}(h') <= (h' - T' + 1)/2, and
n_T(h) = floor(q(h'+2)/2) - (qT'-1)/2 >= q(h'+2-T')/2,
so n_T(h)/q > n'.
Let T' < 0. Then n' <= (h' - |T'|)/2, and
n_T(h) >= (q(h'+2-|T'|) - 1)/2,
so again n_T(h)/q > n'.
Let c' and c be the left ends of I_{T'}(h') and I_T(h), and map c' + t to c + qt for 0 <= t < n'. Since qt <= q(n'-1) < n_T, the image lies in I_T. Suppose |t - t'| = |d'| with d' in S_{T'}(h') and |d'| < n'. Then qd' is in S_T(h) by homogeneity (L = qL' < h), and q|d'| < q n' < n_T. So |qd'| is in D_T(h), and every edge is preserved. The map is injective, so the distinct q·delta are distinct elements of D_T, which gives k_T >= k'.
(Monotonicity in h.) A and K are nondecreasing in h, so I_T(h) is contained in I_T(h+1). S_T(h) is contained in S_T(h+1), and the cap n_T grows. So G_T(h) is a subgraph of G_T(h+1).

4. LEMMA D [proved]
(a) By Lemma B(ii), S_T(q(h'+2)) = q S_{T'}(h'+2), and k_T <= |S_T|.
(b) By Theorem A, S_T(h) is in bijection with the triples (g,x,y).
- Triples with q | g correspond, through g' = g/q, to R_{T'}(h'+2). There are |S_{T'}(h'+2)| of them.
- For triples with q not dividing g: since g | qT' and gcd(g,q) = 1, g divides T'. Put N = qT'/g and beta = x + y phi in Z[phi]. Then N(beta) = x^2 + xy - y^2 = -N, and beta is primitive (no rational prime divides it, because gcd(x,y) = 1).
  - Size bound. |x + y phi| <= sqrt(1 + phi^2) sqrt(x^2+y^2) by Cauchy-Schwarz, and the same holds for the conjugate. So |beta|, |beta'| <= Y with Y^2 = 3.618 h/g.
  - Ideals. A primitive ideal of norm |N| has no factor (p) at a split prime, so it is P^a or P'^a there. It cannot exist if an inert prime divides N, and it is (sqrt5)^a with a <= 1 at 5. So there are at most 2^omega(N) <= 2·2^omega(T'/g) such ideals.
  - Generators. The generators of one ideal are ±phi^n beta_0, and |beta'| = |N|/|beta| <= Y forces |beta| into [|N|/Y, Y]. That leaves at most 1 + log(Y^2/|N|)/log phi values of n, and two signs.
  - Here Y^2/|N| = 3.618 (h'+2)/|T'|, which does not depend on q, and 1/log phi = 2.078.
  - Summing over g | T' with sum_{m | T'} 2^omega(m) = rho(T') gives the bound.
[computed] At split q = 101 and 1009, k_{qT'} = 53, 52, 109, 109 and 13, against k' = 17, 17, 35 and 3, so about 3k'. That is far below K (1303, 1303, 1610, 107).

5. THEOREM E [proved]
(U_C) implies (E_C) trivially. For the converse, assume (E_C) and fix a diagonal (T',h'). There are infinitely many inert primes: N = 5·prod(p_i) + 2 is odd and = 2 mod 5, so it has a prime factor = 2 or 3 mod 5 outside any finite list.
For an inert prime q, put T = qT' and h = q(h'+2). Then T is odd and |T| < h. By Lemmas C and D(a),
chi(G_{T'}(h')) <= chi(G_T(h)) <= C (1 + |S_{T'}(h'+2)|/log(q(h'+2))).
The numerator is fixed. Letting q -> infinity gives chi(G_{T'}(h')) <= C.
The same argument shows: if one diagonal has chi(G_{T'}(h')) = X, then at every height of the form q(h'+2) some diagonal with bounded k has chi >= X. So the best constant in (E) is at least sup chi.

6. COROLLARY F [proved]
Let X = e^(k')/(h'+2), which is >= 6 by hypothesis. By Bertrand's postulate there is a prime q in (X/2, X], and q >= 5 is odd. Put T = qT' and h = q(h'+2).
- Then log h <= k' <= k_T by Lemma C, so T is rich.
- Also log h > k' - log 2.
- Lemma C gives chi(G_{T'}(h')) <= chi(G_T(h)).
- (E) on T and Lemma D(b) give the bound.
Discussion (not part of the corollary): for a rich T' the classes added by q are the orbits of T' shifted by ±log|pi_q/pi_q'|, so K is about 3k'. The random model predicts chi of order k/log n on rich diagonals, which is unbounded. So the rich-only version of (E) is just as implausible as (E).

7. LEMMA G [proved]
Let A be an independent set, F(theta) = |sum_{a in A} e(a theta)|^2 >= 0, and P(theta) = lambda + sum_{d in E} cos(2 pi d theta) >= 0. Expanding, the integral of FP over [0,1] equals lambda|A| + sum_{d in E} r_A(d) = lambda|A|, since r_A(d) = 0 on E.
For |theta| <= 1/(8n), center A at m = (midpoint of the interval). Then |F|^(1/2) >= sum cos(2 pi (a-m) theta) >= |A| cos(pi/8). Also P(theta) >= lambda + k cos(pi/4) because d < n.
Integrating over that window of length 1/(4n): lambda|A| >= (1/(4n)) (0.853 |A|^2)(k/sqrt2). So |A| <= 6.63 n lambda/k.
[computed] hoffman.py, h = 10^5, top 12 diagonals (k = 61 to 71): lambda/k = 0.33 to 0.44, including the Taylor grid error pi^2 k dmax^2/(2N^2). So the lemma gives nothing at this size. A random set predicts lambda/k of about sqrt(2 ln N/k), roughly 0.55 here. The lemma would give chi >= c sqrt(k/log n), unbounded, if one could prove lambda = O(sqrt(k log n)) for a family of rich diagonals. That is the missing input for disproving (U).

8. LEMMA H [proved]
Color i by the pair (floor((i - c)/B), color of i in a proper coloring for D_T ∩ [1,B)). Two vertices with the same first coordinate differ by less than B, so a distance >= B never joins them. The second coordinate handles the smaller distances. The 4-arc version uses the lemma of continuation_arc_parity_riesz.md, Section 2, with delta = 1/4.
[computed] blocks_arcs.py, h = 10^5, T = 30305, 32395, 1045, 6061: the arc numbers are M_T = 14, 12, 14, 13 (about 2.2 k/ln h, 0.8 k/ln k). The block bound 4 ceil(n/B*) is 56, 40, 808, 164, so blocks are useless at this height.

9. PROPOSITION I [proved, modulo the large prime corollary]
- Lower bound: Lemma C with T' = T/p, h' = floor(h/p) - 2, and monotonicity in h.
- Upper bound, step 1 (prime-to-p distances): the large prime corollary(1) 3-colors the distances prime to p with i -> floor(3 frac(N i/p)).
- Upper bound, step 2 (multiples of p): by Lemma B(i) the distances divisible by p are p·{|d'| : d' in S_{T/p}(h/p), p|d'| < n_T}. Their graph is a disjoint union, over the residues mod p, of graphs on intervals of length <= ceil(n_T/p). With h* = ceil(h/p) + 3 one checks ceil(n_T/p) <= (h/p - |T/p| + 3)/2 <= n_{T/p}(h*), and S_{T/p}(h/p) is contained in S_{T/p}(h*). So each piece is a subgraph of G_{T/p}(h*).
- Upper bound, step 3: color each vertex by the pair (step-1 color, step-2 color), which gives 3 chi(G_{T/p}(h*)).
This is the upper-bound twin of the lower bound in Lemma C, and it shows that the large prime corollary's threshold p >= h^(2/3) is the natural one.

10. WHY THE TOTAL IS NOT AFFECTED, AND THE CORRECTED TARGET
Each scaled family uses one offset per (T', h') at each height, so it says nothing against sum_T chi(G_T) = O(h). Any per-diagonal target must respect Lemma C (G_T(h) contains G_{T/q}(h/q - 2) for every q | T) and Lemma B(ii) (inert primes can be stripped). (E_ms) is the smallest change of (E) that does.
[computed] multiscale_total.py, h = 4000, 16000, 64000:
- sum_T max(1, k_T/ln h) = 1.022h, 1.028h, 1.033h.
- The (E_ms) right sides (without C) sum to 1.032h, 1.041h, 1.050h.
- The maximum sits at some q > 1 on 192, 962 and 4362 diagonals.
So (E_ms) is consistent with a linear total at these heights. Its total is not proved to be O(h), even conditionally. A crude bound gives O(h log log h).

11. CLIQUES (side computation)
[computed] cliques.py and cliques_top.py:
- Clique-number histogram at h = 2000: 1:817, 2:908, 3:244, 4:28, 5:2.
- At h = 20000: 1:7374, 2:9687, 3:2658, 4:270, 5:10.
- On the 400 richest diagonals at h = 10^5 the maximum is 5.
- Every K5 found has the shape {0, a, b, c, b+c-a}, for example T = -1045: {0,35,209,260,434} and T = -30305: {0,1015,6061,7540,12586}.
Cliques do not look like a route to proving (U) false.

## External results used

- Quadratic reciprocity: (5/q) = (q/5), so 5 is a non-residue modulo every prime q = 2, 3 mod 5. Used in Lemma B(ii).
- Bertrand's postulate: there is a prime in (X/2, X] for X >= 2. Used in Corollary F.
- Arithmetic of Z[(1+sqrt5)/2]: PID, units ±phi^n, decomposition of rational primes. Used in Lemma D(b), as in items (O1) to (O5) of three_term_relations.md.
- From the archive: the parity Riesz lemma (continuation_arc_parity_riesz.md, Section 2), used in Lemma H; Proposition 1 of arc_classes_monotone_partition.md, through the definitions; and the large prime corollary (Corollary 4.1 of three_term_relations.md, under audit), used only in Proposition I.

## Checks

All scripts are in scripts_bohr_rich/. Each was run with py, under 60 s and well under 1 GB. The shared enumerator is common.py, which builds D_T(h) from Theorem A.
- param_check.py: Theorem A against brute force at h = 150, 301, 400: 0 mismatches.
- scaling_check.py: the Lemma C embedding holds in every case tested. For inert q, k_{qT'} = k'; for split q, about 3k'.
- cliques.py and cliques_top.py: clique numbers are at most 5.
- hoffman.py: lambda/k is 0.33 to 0.44 at h = 10^5.
- blocks_arcs.py: M_T is 12 to 14 for k of about 70.
- multiscale_total.py: the totals are about 1.03h for (E) and 1.05h for (E_ms).
The earlier run's salvage (the logs of an earlier run) contained only file reads and no computed data. The prior scripts folder was empty.

## Gaps

- (U) false, that is sup over h and T of chi(G_T(h)) = infinity, is not proved. So (E) is not disproved, only shown equivalent to (U). The heuristic against (U) is the random model plus the computed lambda/k values. A proof needs a uniform-in-theta lower bound on sum_{d in D_T} cos(2 pi d theta) for some family of rich diagonals (Lemma G), or a growing clique or odd-structure family. Clique numbers stay at most 5 up to h = 10^5.
- Proposition I's upper bound depends on the large prime corollary (Corollary 4.1(1) and Proposition 4 of three_term_relations.md), which is still under audit.
- Corollary F's use of K(T',h') is about 3k' only on the computed diagonals. I did not prove K = O(k') in general, so the rich-only implication 'bounded chi on rich diagonals' is rigorous only in the form with K(T',h')/(k' - log 2).
- Standard facts used without re-proof: quadratic reciprocity for (5/q), Bertrand's postulate, and the arithmetic of Z[phi] (units ±phi^n, the decomposition of rational primes, at most 2^omega(N) primitive ideals of norm N).
- The corrected target (E_ms) is a conjecture. Its total is only numerically about 1.05h for h <= 64000, with no proof that it is O(h).
- No new bound on sum_T chi(G_T(h)). The best total is still O(h log h/log log h) from the local sparsity bound.
- No independent audit of any proof in this report.

## Missing estimate

To disprove (E), and with it the rich-only version: a family of diagonals (T,h) with k_T/log n_T -> infinity and lambda_T := -min_theta sum_{d in D_T} cos(2 pi d theta) = o(k_T). Lemma G then gives chi(G_T(h)) >= k_T/(6.63 lambda_T) -> infinity, so (U) fails, and by Theorem E so does (E). For the linear total, the per-diagonal statement to aim at is the multiscale (E_ms), or directly sum_T chi(G_T) = O(h). Both still need joint control of about log(h/q) distances under one rotation on primitive rich diagonals.

## Next steps

- Drop (E) as the per-diagonal target for the linear total. Use (E_ms), or the total sum_T chi = O(h) directly. Record Theorem E in the ledger so later attacks do not try to prove (E) for all T.
- Try to prove (U) false. Look for a family of rich diagonals where the exponential sum over D_T can be bounded uniformly in theta, for example T with all split prime factors near h^(1/w) and U = log(h/T) bounded. Then apply Lemma G.
- Audit the large prime corollary (Proposition 4). With Proposition I it gives the two-sided reduction for diagonals with a prime factor of at least 19 h^(2/3). Check whether its threshold extends to divisors with j prime factors.
- Since inert primes can be stripped exactly (Lemma B(ii)), restrict any future per-diagonal analysis to inert-free T, and track the convolution over inert multiples separately when summing.
- Test (E_ms) numerically against arc numbers M_T at h = 10^5 on diagonals where the maximum sits at q > 1, about 7 percent of them.

