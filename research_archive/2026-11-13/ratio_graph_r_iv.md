# The ratio graph R_IV is not bipartite

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: R_IV has an odd cycle (exact certificate), so chi(R_IV) >= 3. Removing a sparse set of rows cannot lower its chromatic number, by dilation invariance. Family IV exists only because the stride is (4,1); stride (8,1) removes it inside classes. Not audited yet.

# Result

## Status

partial

## Summary

R_IV is not bipartite (exact certificate), so chi(R_IV) >= 3. Removing a small set E of u-values cannot lower its chromatic number, because R_IV is invariant under odd dilation. Family IV is a 2-adic tie that exists only because the stride is (4,1). With stride (8,1), the same 2-adic law empties every inside-class label-label shallow M2c. At stride 4, no choice of sea-row residue removes family IV without reopening the X2 and M1C congruences.

## Statements

Notation. R_IV^(k) is the graph of sea_census_rigid B4 on odd positive integers: an edge (q m, p m) for every odd m and every odd coprime lambda = (al, be) with 0 < al < be and v2(be - al) >= k - 2. Here F = 4(al - 2be)^2 + be^2, g = gcd(F, be - al), q = al F/g, p = (al F + 4(be - al)be^2)/g, and rho_lambda = p/q.

THEOREM 1 (proved; the certificate is computer-generated and was checked twice in exact integer arithmetic). For k = 3 and for k = 4, R_IV^(k) contains an odd cycle, so chi(R_IV^(k)) >= 3.
- k = 3: there are integers n_lambda on 136 pairs with be <= 137 such that prod rho_lambda^(n_lambda) = 1 and sum n_lambda = 1346296287, which is odd.
- k = 4: there are integers n_lambda on 184 pairs with be <= 285, all with v2(be - al) >= 2, such that prod rho_lambda^(n_lambda) = 1 and sum n_lambda = -230102255637681761, which is odd.
Computed but not certified: at the group level, no odd relation exists among the pairs with be <= 133 (k = 3) or with be <= 281 (k = 4). The odd cycle produced has astronomically large vertices (more than 10^(10^9) digits). So it does not contradict the earlier numerics, which found R_IV bipartite on [1, 2*10^6].

LEMMA 2 (dilation; proved). If u ~ v in R_IV^(k), then m u ~ m v for every odd m.

COROLLARY 3 (the E-weakening is void; proved). Let F be a finite subgraph of R_IV^(k) with vertex set V_F and largest vertex U_F. Let N be the number of odd m <= X/U_F with m = m0 (mod 2^k), for any fixed odd m0. Let E be a set of odd integers with |E| |V_F| < N. Then (R_IV^(k) ∩ [1, X]) \ E, restricted to the residue class of m0 U_F mod 2^k, contains a copy of F. Consequently:
(a) "O(1) colours on R_IV ∩ [1, X] after removing some E with |E| = O(X^(1-delta)), for every X" holds iff chi(R_IV) < infinity (de Bruijn–Erdős).
(b) For every psi-split there is an X_0 such that, for X >= X_0, psi needs at least 3 colours on every residue class, even after relocating o(X) u-values. A 2-colour psi split is therefore impossible for large h.
(c) For each diagonal T, the number of classes is at least chi(F) whenever the slot range satisfies |I_T| >= 2^k U_F |V_F| (|E_T| + 1). So in the stride-4 L* sea, an O(1)-per-label sea with classes free of R_IV edges needs chi(R_IV) < infinity.
(Had the E-route worked, it would have relocated h|E| = O(h^(2-delta)) labels, at width O(h^(2-delta) tau*(h)^2) = o(h^2). Corollary 3 shows the weakening gains nothing.)

THEOREM 4 (2-adic tie law for M2c; proved, any stride). Take an M2c with A and C shallow in sea row r (shallow means column != 0 mod 4) and B and D deep (columns = 0 mod 4). Use the data of block_sea Theorem 2: e = (y_D - y_B)/2 > 0, Delta = x_D - x_B, u2 = y_B - r != 0, n1, z = -e u2/n1. Put
- a = v2(e), b = v2(n1), c = v2(u2), zeta = v2(z), which lies in {0, 1}, and delta = v2(Delta), which is >= 2.
If a >= 4 and c is in {0, 1}, then delta = b + 1 = a + c - zeta + 1. In particular delta - a is in {c, c+1}.

COROLLARY 5 (inside a class; proved). Take stride (mu, nu): label t is at column mu t + B_c, with odd row 2(r + nu t) + 1. Inside a class, delta - a = tau := v2(mu) - v2(nu). Theorem A of sea_row3_split forces c = 1 for label points of the sea row's parity and c = 0 for the other parity. Then, with classes split so that a >= 4:
(i) Stride (4,1) (tau = 2): the only possibility is (c, zeta) = (1, 0), which is exactly family IV (B3(ii), B4). Even-even inside-class M2c is empty for a >= 4.
(ii) Any stride with tau >= 3, for example (8,1), (16,1) or (16,3): no label-label M2c with shallow A and C exists inside a class, for either parity, with the i mod 16 split. FAMILY IV DISAPPEARS.
(iii) Stride (8,1) across classes, with columns 8(i + M_c): an M2c needs v2(DM) in {a-3, a-2, a-1}. This is a rare coincidence of the same kind as C3 of sea_census_rigid. No count is proved.

PROPOSITION 6 (no-go at stride 4 for the sea-row residue; proved at the level of the necessary conditions). In a stride-(4,1) region with one shallow sea row r, let c = v2(y - r) for the label rows y of the parity of r (c >= 1).
- If c = 1, the family-IV tie (c, zeta) = (1, 0) is open.
- If c >= 2, every such label point meets the X2 vertex congruence y_V = r (mod 4) and the M1C congruence of sea_row3_split Theorem A(a),(c). With c = 2, the tie (2, 1) of Theorem 4 is also open.
So no choice of sea row per region kills family IV without reopening the X2 and M1C sources, whose load sea_row3_split removed (load log(h/160)/(20 chi) per label). The same holds for any single row that carries the odd-offset (zeta = 0) shallow cells.

NOT PROVED: chi(R_IV) < infinity, or = infinity. The stride-(8,1) versions of the stride-dependent results.

## Proofs

1. THEOREM 1.
(a) Reduction to a group relation. Take integers n_lambda with prod rho_lambda^(n_lambda) = 1 and sum n_lambda odd. Put
 u0 = prod_{n>0} q_lambda^(n_lambda) · prod_{n<0} p_lambda^(|n_lambda|),
which is odd. Walk from u0 as follows:
- First take every positive step, u -> u p_lambda/q_lambda, n_lambda times each. Before each step, the q-factors still unused divide the current u, so the step is the edge (q m, p m) with m = u/q odd.
- Then take every negative step, u -> u q_lambda/p_lambda. The p-factors placed in u0 for these steps are still present.
The walk returns to u0 · prod rho^(n) = u0. Its length is sum |n_lambda|, which has the parity of sum n_lambda, so it is odd. A closed walk of odd length contains an odd cycle.
(b) Construction. scripts f2sys.py, oddrel.py and exactrel.py:
- Enumerate the pairs lambda with be <= B and factor p and q.
- Peel repeatedly every lambda that has a prime appearing in no other remaining lambda. Such a lambda has n_lambda = 0 in every relation.
- Decide 2-adically whether an odd relation exists: solve [M; 1^T] n = (0; 1) over Z_2 by Smith elimination mod 2^31. The pivot valuations were at most 2, so the precision is ample.
- Compute the rational kernel, 2-saturate it (replace any combination that is = 0 mod 2 by its half until none is), and take a basis vector with odd sum.
(c) Check. verify_cert.py is independent code: no sympy, plain trial division. For every lambda it recomputes q and p from (al, be) and asserts parity, coprimality, 0 < al < be, gcd(p, q) = 1 and v2(be - al) >= k - 2. It then adds n_lambda times the exponent vectors.
- oddrel_137.json: 136 pairs; all 133 prime exponents cancel; the sum is odd.
- oddrel_291.json: 184 pairs; all 181 prime exponents cancel; the sum is odd.
Exponent cancellation is equivalent to prod rho^(n) = 1, because p and q are positive.

2. LEMMA 2 AND COROLLARY 3. The edge set is {(q m, p m) : m odd}, and m -> m m' preserves it.
Copies m·F for odd m <= X/U_F with m = m0 (mod 2^k) lie in [1, X]. Each copy is in the residue class m0 U_F times the class of F; R_IV edges preserve u mod 2^k, since v2(t) >= k.
A point u of E lies in at most |V_F| copies, since u = m w determines m for each w in V_F. So if |E||V_F| < N, some copy misses E. Its chromatic number is chi(F), which gives the lower bound.
(a) The implication from the right is trivial. For the other direction, if chi(R_IV) = infinity, then de Bruijn–Erdős gives finite F of every chromatic number. Copies of F avoid any E with |E| = o(X).
(b) Apply this to the odd cycle of Theorem 1.
(c) Classes on one diagonal must be R_IV-independent. The u-values of one region of T run over a full residue class of I_T.

3. THEOREM 4. From the audited M2c equations (block_sea Theorem 2, rewritten in sea_census_rigid proof 4):
 (I1) e u2 = n1(Delta + w) = -n1 z;
 (I2) (Delta - 2n1) w = e^2 + n1^2.
- Neither w nor Delta - 2n1 is 0, because the right side of (I2) is positive.
- (I1) gives a + c = b + zeta, so b = a + c - zeta.
- v2(e^2 + n1^2) is 2 min(a, b) if a != b, and 2a + 1 if a = b (odd parts e', n' give e'^2 + n'^2 = 2 mod 8).
- Suppose delta != b + 1. Then v2(Delta - 2n1) = min(delta, b + 1) <= b + 1, so v2(w) >= v2(e^2 + n1^2) - (b + 1).
- Since z = -(Delta + w) and zeta <= 1 < 2 <= delta, we need v2(w) < delta, and then zeta = v2(w). If v2(w) > delta, then zeta = delta >= 2. If v2(w) = delta, then zeta > delta.
Case check, with a >= 4:
- (c, zeta) = (1, 0): b = a + 1, so v2(w) >= 2a - a - 2 = a - 2 >= 2. Contradiction.
- (c, zeta) in {(0, 0), (1, 1)}: b = a, so v2(w) >= 2a + 1 - a - 1 = a >= 4. Contradiction.
- (c, zeta) = (0, 1): b = a - 1, so v2(w) >= 2a - 2 - a = a - 2 >= 2 > 1. Contradiction.
Hence delta = b + 1 = a + c - zeta + 1. []

4. COROLLARY 5.
- Inside a class (one region, one block): Delta = mu Δt and y_D - y_B = 2 nu Δt, so e = nu Δt and delta - a = v2(mu) - v2(nu).
- Theorem 4 needs tau = c - zeta + 1.
- For (4,1), tau = 2. With c = 1 this forces zeta = 0, which is the family of B3(ii)/B4. With c = 0 it would need zeta = -1, which is impossible.
- For tau >= 3 there is no admissible (c, zeta) in {0,1}^2.
- For (8,1) across classes: Delta = 8(e + DM), so delta = 3 + v2(e + DM). Theorem 4 then gives v2(e + DM) = a + c - zeta - 2 <= a - 1 < a = v2(e). So v2(DM) = v2(e + DM), which lies in [a-3, a-1].
Brute-force check (stride_m2c.py): all inside-class M2c with B = (0, y_B), D = (s e, y_B + 2e), e = 0 mod 16, rows with y_B != r (mod 4), sea row 1. Every hit was re-checked from the mixed-quadruple definition.
- Slope s = 4, H = 2400: exactly one hit, y_B = 699, y_D = 1499. This is the IV edge (349, 749).
- Slope s = 8, H = 7000: 0 hits, for both parities.
- Controls with k = 3 or with c = 2 show the predicted survivors: a = 3 even-even (stride 8, y_B = 230), and c = 2 (y_B = 149).

5. PROPOSITION 6.
- Label rows of the parity of r have c >= 1.
- c = 1 is the tie of Corollary 5(i).
- For c >= 2: y = r (mod 4) is exactly the X2 vertex condition (Theorem A(a)) and the M1C condition (Theorem A(c)). These are stride-free, since they concern deep points in columns = 0 mod 4.
- The same algebra applies to any row r carrying the odd-column (zeta = 0) shallow cells. The X2 derivation with E at an odd offset (4 a gamma = f g, a odd, g odd) again forces f = y_V - r = 0 mod 4.

## External results used

- de Bruijn–Erdős theorem: an infinite graph is k-colourable iff all its finite subgraphs are (standard; used only in Corollary 3(a)).
- Internal and audited: block_sea_classification Theorem 2 (the M2c equations and converse), and the equations (I1), (I2) as rewritten in sea_census_rigid proof 4.
- Internal, cited: sea_row3_split Theorem A (vertex congruences, unaudited), stride_menu (1c) (the p > max(Dh, 36h + mu h/2nu) reduction, unaudited), and sea_census_rigid B3/B4.

## Checks

All scripts are in the matching scripts_ folder of this directory. Each ran with py in under 60 s, and the repository was not touched.
- f2sys.py: no completely multiplicative F_2 colouring exists for be <= 251 (145 inconsistent rows on the 808-row core). This is subsumed by Theorem 1.
- oddrel.py: the Z_2 odd-relation test. k=3: none for be <= 133, present from be = 137. k=4: none for be <= 281, present at 291.
- exactrel.py writes the certificate files oddrel_137.json and oddrel_291.json, and verify_cert.py re-checks them independently (all exponents cancel, odd sums).
- zsys.py: integer relations exist from be ~ 135 on: rank deficit 4 at be <= 137, 273 at be <= 251, 1161 at be <= 401.
- lp.py (numerical): the least M for which some additive real potential psi on primes has 1 <= psi(rho) <= M on the core. M is 1.38, 2.15, 2.69, 3.28, 3.62, 3.84 at be <= 137, 201, 251, 301, 351, 401. It grows, so one-dimensional real-potential colourings degrade.
- bohr.py (crude local search, numerical): the best single-character Bohr epsilon is 0.163, 0.139, 0.108, 0.088, 0.071 at be <= 137, 201, 251, 301, 401.
- The ratio of core rows to core primes grows: 1.03, 1.34, 1.51, 1.66, 1.76, 1.87.
- stride_m2c.py: the stride 4 vs stride 8 brute force of Corollary 5.

## Gaps

- chi(R_IV) < infinity is still open. Theorem 1 only gives chi >= 3, and the numerics (below) weakly suggest that the natural colourings degrade as be grows.
- Theorem 1 rests on a computer certificate. It was checked by two independent codes in exact integer arithmetic, but not by hand. The thresholds 'no odd relation for be <= 133 (k=3) and be <= 281 (k=4)' were computed mod 2^31 and are not certified.
- Theorem 4 and Corollary 5 are not independently audited. They rest only on the audited M2c equations (I1), (I2) and on the shallowness condition v2(z) <= 1.
- Proposition 6 is a statement about necessary conditions. That the X2 load really returns when c >= 2 is cited from sea_row3_split and cross_class_sea, not re-proved here. Multi-row shallow patterns that mix rows inside one tilted configuration were not analysed.
- Stride (8,1) removes family IV inside classes, but these stride-dependent results must be re-derived: (i) G_T becomes (T+2d)^2 + 64d^2 = L^2, so Gamma moves from Q(sqrt5) to Q(sqrt17), and chi(Gamma^(8,1)) < infinity is open (the round-6 split-prime theorem used Q(sqrt5) Pisot identities); (ii) rigid Theorem C (stride menu (1c) reduces it to the (E;O,E) cross-block type with p > 68h); (iii) mixed_quadruples Theorems 1-4 and the I.2/II thresholds; (iv) the deep layer, which now also fills the columns = 4 mod 8 inside blocks, together with deep_layer A3.
- The width factor for stride (8,1) (about 68/20 = 3.4 from p > 68h) is taken from stride_menu (1c) and was not re-checked.
- Cross-class odd-odd M2c at stride (8,1) reduces to v2(DM) in [a-3, a-1]. Like C3 at stride 4, it has no proved count.

## Missing estimate

One of these two is needed.
(A) Stay at stride 4: chi(R_IV) < infinity. By Corollary 3, nothing weaker helps: neither relocation nor polylog colours. By Theorem 1, the colouring needs at least 3 colours. The question is the chromatic number of the Cayley graph of Q^* with generators p/q, the values of the sextic form al·F·C (C = 4al^3 - 16al^2 be + 13 al be^2 + 4be^3). Its relations come from smooth values of these forms, and the numerics suggest that one-character colourings degrade.
(B) Switch rigid regions to stride (8,1), which removes family IV outright (Corollary 5(ii)). The cost moves to: chi(Gamma^(8,1)) < infinity over Q(sqrt17); rigid Theorem C, mixed_quadruples 1-4 and the deep layer at slope 4; and a count for cross-class M2c with v2(DM) in [a-3, a-1].

## Next steps

- Audit Theorem 4 (about ten lines). Then add ledger rows: 'R_IV^(3) and R_IV^(4) are not bipartite (certificate)'; 'E-relocation does not lower chi(R_IV) (dilation)'; 'family IV is the 2-adic tie tau = c - zeta + 1; strides with v2(mu) - v2(nu) >= 3 have no inside-class shallow label-label M2c'.
- Decide between routes (A) and (B). For (B): port the round-6 split-prime Bohr theorem to Q(sqrt17) (unit 4 + sqrt17, norm -1, Pisot). Redo rigid Theorem C for the (E;O,E) cross-block type at (8,1), and redo mixed_quadruples Theorems 1-4 at slope 4.
- For (A): test chi(R_IV) = infinity through the Hoffman bound on finite truncations, 1 + 2m/(-min_theta sum_lambda 2cos 2pi theta(rho_lambda)). Also look for short odd relations (LLL on y-smooth lambda with a faster lattice library) to find the smallest odd cycle and the first h at which a 2-colour psi split fails.
- Count cross-class M2c at stride (8,1) under a mod-64 window version of (Hs), as C3 does at stride 4.

