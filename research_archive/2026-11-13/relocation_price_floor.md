# The relocation price is sharp for this block type

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (obstruction): Theorem R. Every relocation block of the T1, Theorem D and Theorem E type costs at least c (log h)^2 per label. The type means independent uniform slots, one fixed sea row on empty slots, and certificates built from event probabilities and the dependency graph. One two-label family forces the cost: same-parity label points at integral distance, with the matching sea pair on empty slots. So better relocation of this type cannot lower the 1.4967 cap. This bounds a method, not m_h. Open loopholes: seas with many slot rows, the mod-p column rule, and heaviness measured by chi(G_T[tau]). Not audited yet.

# Result

## Status

obstruction

## Summary

Obstruction, proved: every relocation block of the T1 / Theorem D / Theorem E type costs at least c(log h)^2 per label. The cause is one fatal two-label family: same-parity label points at integral distance, with the matching sea pair on empty slots. So no price below Lambda^2 exists in that class. Theorems D and E are sharp up to (loglog h)^C, and the 1.4967 cap cannot be lowered by better relocation of this type. No new exponent.

## Statements

NOTATION. Lambda = log h. A label e has an odd point (row a_e) and an even point (row b_e) in one column x_e (a double). For a parity pi, rho_pi(e) is the row of e's pi-point.

CLASS P (the method of T1, T2 Section 7, Theorem E, Lemma M1, Theorem D, Theorem H).
- A block is W consecutive columns. Its slots are the columns in one residue class mod m (m >= 1), and N = W/m is the number of slots.
- A label set Z is placed as doubles on distinct slots. The slots are drawn independently and uniformly.
- Every other column holds one sea point. Every slot without a label holds a sea point in one fixed row s0, and s0 is not a row of any label of Z. In T1 this is the profile's period-zero row. Nothing is assumed about the other sea columns.
- The placement is certified from the event system E. E consists of the configurations of sets of centres that contain a forbidden support when all other slots are empty, which are T1's events.
- The certificate may be any criterion that uses only the probabilities P(A) and the dependency graph in which two events are adjacent when they share a label. This covers the local lemma in every form, Shearer's criterion, and alteration by the first moment.

LEMMA F (fatal family; PROVED, elementary). Take labels e != f and a parity pi. Let C = e's pi-point at (x_e, a) and D = f's pi-point at (x_e + X, c), with y = c - a != 0. Suppose X^2 + y^2 = L^2 for an integer L > 0. Suppose also that the columns u- = x_e + (X - L)/2 and u+ = x_e + (X + L)/2 hold black points A and B in one row s0, with s0 not in {a, c, (a+c)/2}. Then the blackout is invalid.

THEOREM R (the price of class P; PROVED). Let Z, m, N, W and s0 be as in class P, with N >= max(20, 2h/m). Fix a parity pi. Let M0 be the largest number of labels of Z sharing a pi-row. Put R1 = W/(2h) and R2 = |Z|/(m M0 Lambda^3). There are absolute constants c, C0 > 0 such that, if R1, R2 >= C0, then:
(a) The average over e in Z of the sum of P(A), over the two-label events A of E that contain e, is at least
 c |Z| ln(R2) ln(min(R1, R2^(1/3))) / W.
(b) Every certificate of class P needs this average to be at most 1. Hence
 W >= c |Z| ln(R2) ln(min(R1, R2^(1/3))).
(c) In a uniformly random placement with N >= 4|Z|, the expected number of pairs {e, f} that form a fatal configuration of Lemma F, with all labels present, is at least (c/2) |Z|^2 ln(R2) ln(min(R1, R2^(1/3)))/W. So alteration by the first moment also fails below this width.
(d) Variant: if the empty-slot rows are periodic in the slot index with period P_s, the same bounds hold divided by P_s.

COROLLARY R1 (Theorems D and E are sharp; PROVED modulo the definitions of T1 and Theorem E).
- Theorem E applied to Delta >= h^(c1) heavy diagonals uses total block width at least c c1 Lambda^2 |S|(1 - o(1)), where S is the set of relocated labels. Theorem E gives C(Delta h Lambda^2 ell^C1 + h^2 ell).
- Theorem D for a diluted set Y, with rho|D| >= log h, uses width at least c Lambda^2 |Y|(1 - o(1)). Theorem D gives rho|D| h Lambda^2 ell^C1 + h^2 ell.
- Lemma M1, and Theorem H for any Y with |Y|/M0 >= h^c, cost at least c Lambda^2 per label in this class.
So the relocation price beta of class P is exactly 2, up to powers of loglog h.

COROLLARY R2 (floor of the architecture; PROVED for the board as specified). Take the board L***U of heavy_diagonals_sharp Proposition 3: kappa-heaviness, B = Lambda^x classes per type, and (B7) rule 1 sending every non-exceptional label of a heavy diagonal to class-P blocks. Its heavy term is at least c h Lambda^2 H_d(B) = h^2 Lambda^(2 - phi(x) + o(1)), by Theorem R and the sieve lower bound of Theorem 2. So no class-P relocation lowers the exponent of Theorem N below theta* = 1.49674. This is a statement about this construction, not a lower bound on m_h.

LEMMA V (vertical rivals cost Lambda, not Lambda^2; PROVED, unweighted). Fix a label e and a multiset R of rows with multiplicity at most M_R. Then
 sum over c in R of #{X != 0 : X^2 + (c - a)^2 = L^2, 1 <= L <= h} <= 8 M_R h (1 + ln h).
So the true rival count per pair is O(Lambda) on average. T2's bound tau((c-a)^2) has average Lambda^2, so source (i) of t1_cost Theorem A overcounts by a factor Lambda.

LEMMA S (sorting removes the private Lambda^2; PROVED as an inequality, modulo Henriot Cor. 2 for K forms). Take K profile families with pairwise distinct sea rows and weights v_k. Then
 sum over labels of min_k v_k(e) << Q Lambda^(K(2^(1/K) - 1)) ell^(C_K).
So the private source (iii) of Theorem A costs at most Lambda^(1 + K(2^(1/K)-1)) per label (1.83 at K = 2, tending to 1.69) if each label goes to its best profile. Because the family of Lemma F is not private, this does not lower the price.

EXPONENT TABLE (if a relocation price Lambda^beta were available). With Proposition 3 the exponent is theta(beta) = min_x max(x, beta - phi(x), beta - x):
- beta = 2: 1.4968;
- 1.9: 1.4440;
- 1.8: 1.3903;
- 1.75: 1.3631;
- 1.69: 1.3301;
- 1.6: 1.2797;
- 1.5: 1.2225;
- 1.4: 1.1639;
- 1.2: 1.0415;
- 1.0: 0.9101.
Theorem R shows that no beta < 2 is available in class P.

## Proofs

1. PROOF OF LEMMA F.
- The setup. y = c - a is even because C and D have the same parity. X^2 + y^2 = L^2 then gives X = L (mod 2), so u- and u+ are integers.
- The rectangle R1. Put n2 = (a+c)/2 - s0, which is not 0. Let p = (u-, (a+c)/2) and q = (u+, (a+c)/2). Then A, B, q, p form an axis-aligned rectangle of positive area. Its rows are s0 and (a+c)/2, and both lie in the grid.
- The rectangle R2. The segment pq is horizontal. It has midpoint (x_e + X/2, (a+c)/2) and length L. The segment CD has the same midpoint and length L, and it is not horizontal because y != 0. Two distinct segments with a common midpoint and equal length are the diagonals of a rectangle. So p, C, q, D form a rectangle R2 of positive area, with rows a, c and (a+c)/2.
- R2 is tilted, because an axis-aligned rectangle has no horizontal diagonal. So R1 != R2.
- The support. The sea rows are not label rows, so A, B, C, D, p, q are six distinct points. Then C(R1) Δ C(R2) = {A, B, C, D}, which is black. By Lemma diff (sec2_prelim), R1 and R2 have the same presentation, so the blackout is invalid.
This is the horizontal-sea-side case of T2's role table, counted there as tau((c-a)^2).

2. PROOF OF THEOREM R.

(i) Parametrization. Let (r, s) satisfy:
- 1 <= s < r;
- gcd(r, s) = 1;
- r != s (mod 2).
Put q = 2mrs. Suppose y = rho_pi(f) - rho_pi(e) = qk with k != 0. Set X = m|k|(r^2 - s^2) and L = m|k|(r^2 + s^2). Then X^2 + y^2 = m^2 k^2((r^2 - s^2)^2 + 4r^2 s^2) = L^2.
- Both endpoints are slots. (X - L)/2 = -m|k|s^2 and (X + L)/2 = m|k|r^2, so u- = x_e - m|k|s^2 and u+ = x_e + m|k|r^2.
- With all other slots empty, both columns hold s0. So by Lemma F the event A(e, f, r, s) = {x_f - x_e = X} is an event of E. It depends only on x_e and x_f.
- Distinct (r, s) give distinct X/|y| = (r/s - s/r)/2, so the events for one pair are distinct.

(ii) Probability. Write j for slot indices. Restrict to j_e in [N/4, N/2).
- Then |k| < h/q gives X/m < h r/(2ms).
- Require r <= s R1. Then X/m <= h R1/(2m) = N/4.
- So P(j_e in [N/4, N/2) and j_f = j_e + X/m) >= (N/4 - 1)/N^2 >= 1/(5N).
- Both u-/m >= N/4 - h/(2m) >= 0 and u+/m < N/2 + N/4 hold, so u+- lie in the block.

(iii) Counting by Cauchy-Schwarz. Let A_c count the labels of Z whose pi-row is congruent to c mod q.
- Ordered pairs e != f with q | y number sum A_c^2 - |Z| >= |Z|^2/q - |Z|.
- Pairs with y = 0 number at most |Z|(M0 - 1).
- Pairs with (rho(e) + rho(f))/2 = s0 number at most |Z| M0.
- So N'_q, the number of pairs with q | y, y != 0 and s0 != (a+c)/2, satisfies N'_q >= |Z|^2/q - 2|Z| M0.

(iv) Summing. Let Acal be the set of (r, s) above with s <= R2^(1/3) and s < r <= min(s R1, R2^(2/3)). Then rs <= R2 and r <= s R1. The average over e of the incident sum is at least
 (1/|Z|) sum over Acal of N'_(2mrs)/(5N) >= (|Z|/(10W)) sum over Acal of 1/(rs) - (2M0/(5N)) |Acal|.
- The error term. |Acal| <= R2(1 + ln R2), so the error is at most 2|Z|(1 + ln R2)/(5W Lambda^3) <= |Z|/(W Lambda^2).
- The admissible r. For fixed s, the r coprime to s with r != s mod 2 form phi(s) residue classes mod 2s.
- One class. A class contributes sum of 1/r over r in (s, U] of at least (1/(2s)) ln(U/(3s)): compare with the integral of dt/(2s t) from r_1 <= 3s to U.
- One s. With U = min(s R1, R2^(2/3)) >= s min(R1, R2^(1/3)), the inner sum is at least (phi(s)/(2s))(ln min(R1, R2^(1/3)) - ln 3).
- All s. The sum over s <= S of phi(s)/s^2 is (6/pi^2) ln S + O(1), with S = R2^(1/3).
- So sum over Acal of 1/(rs) >= ((1/pi^2) ln R2 - C)(ln min(R1, R2^(1/3)) - ln 3).
For R1, R2 >= C0 this proves (a).

(v) Certificates, part (b). The events containing e all contain x_e, so they form a clique of the dependency graph. If their probabilities sum to at least 1, disjoint events with these probabilities can cover the probability space while keeping the dependency graph. Then no criterion that uses only (P(A)) and the graph can certify. This is the clique case of Shearer's theorem, and it is elementary. For the asymmetric local lemma it is direct:
- x_A >= P(A) and the product of (1 - x_B) over B ~ A is at most exp(-sum of P(B) over B containing e).
- So the conditions force x_A >= P(A) e^(lambda) at total incident sum lambda. Iterating diverges once lambda >= 1.
Some e has an incident sum at least the average. With (a) this gives (b).

(vi) Part (c). The other labels are independent of (x_e, x_f). So u- and u+ are both free with probability at least 1 - 2|Z|/N >= 1/2, and the configuration is then fatal with all labels present.

(vii) Part (d). Require P_s | k, that is q = 2mrs P_s. Then u+/m - u-/m = |k|(r^2 + s^2) = 0 (mod P_s), and the proof repeats with q multiplied by P_s.

3. PROOF OF COROLLARY R1.

(i) Theorem E fits class P. Theorem E (via T1, T2 Section 7) places each class C_w of each profile family in its own block:
- the slots are the N_w period-zero slots, so m is the profile period and s0 is its period-zero row;
- the slots are drawn independently and uniformly;
- the certificate is the product-form local lemma.
So Theorem R applies block by block.

(ii) Size of the blocks. Labels of distinct heavy diagonals with the same i share an odd row, so M0 <= Delta. The classes with |Z_w| >= |S| Lambda^(-10) hold all but O(ell Lambda^(-10))|S| labels, because there are O(ell) classes. For these classes:
- |S| >= Delta h/C gives R2 >= h Lambda^(-14)/m;
- N_w >= |Z_w| gives R1 >= m|Z_w|/(2h) >= Delta Lambda^(-10)/C >= h^(c1/2).
So W_w >= c c1 Lambda^2 |Z_w|. Summing over these classes gives the first item.

(iii) Theorem D. Y is independent across diagonals, so Chernoff gives M0 <= 2 rho|D| + 3 log h with high probability, and the same computation applies.

(iv) Lemma M1 and Theorem H. The same applies to their blocks whenever |Y|/M0 >= h^c. Any Y with |Y| >= h^(2c) has this property for one of the two parities, because |Y| <= (#odd rows used)(#even rows used).

4. PROOF OF COROLLARY R2. Under (B1') and (B7) rule 1, the non-exceptional labels of every diagonal with kappa_T >= B/4 go to Theorem E blocks.
- By Theorem 2 (sieve lower bound) there are H_d(B/4) >= h Lambda^(-phi(x) - o(1)) such diagonals.
- Each has at least h/2 - O(h^(1/2)) non-exceptional labels.
- By Corollary R1 their width is at least c h Lambda^2 H_d.
- The board's light width is proportional to B (t < 16l(B+1) per type).
So the exponent is at least min_x max(x, 2 - phi(x)) = theta*, and Proposition 3 attains it.

5. PROOF OF LEMMA V.
- The map. Send each counted (c, X) to the Pythagorean triple (|X|, |c - a|, L). Here c != a, because rival endpoints have opposite parity. A triple has at most 4 M_R preimages, from the signs and the multiplicity.
- Primitive triples with hypotenuse at most x correspond to coprime pairs (r, s) with r^2 + s^2 <= x, so there are at most x of them.
- So the number of triples with L <= h, legs ordered, is at most the sum over k <= h of 2h/k <= 2h(1 + ln h).

6. PROOF OF LEMMA S.
- min_k v_k <= product over k of v_k^(1/K).
- (1 + t1 + ... + t6)^(1/K) <= 1 + the sum of t_j^(1/K).
- Expanding gives at most 7^K terms. Each is a product of at most K factors tau(|r - s_k|)^(1/K), where the r are label rows and the s_k are distinct sea rows.
- On a diagonal these are distinct linear forms in i, apart from O(K^2) excluded diagonals.
- Henriot Cor. 2, with the Euler factor 1 + K(2^(1/K) - 1)/p at ordinary primes, gives the bound per diagonal; then sum over the diagonals.

7. EXPONENT TABLE. theta(beta) is computed by a grid minimization of max(x, beta - phi(x), beta - x), with phi as in heavy_diagonals_sharp. At beta = 2 it gives 1.49676.

## External results used

- Lemma diff and Definition valid, papers/extremal/sections/sec2_prelim.tex (two rectangles have the same presentation iff their symmetric difference is black).
- Clique case of Shearer's theorem (J. B. Shearer, Combinatorica 5 (1985) 241-245). It is used only for a clique, where it is elementary: disjoint events with total probability >= 1 can cover the space. I give that argument directly, so no theorem number is needed.
- Asymmetric Lovasz local lemma (product form), as in T2 Section 7.
- Standard asymptotic sum_{n<=x} phi(n)/n^2 = (6/pi^2) ln x + O(1).
- Parametrization of Pythagorean triples by coprime (r, s) of opposite parity (classical).
- Henriot, Nair-Tenenbaum bounds uniform in the discriminant, Corollary 2 with the 2014 erratum. Used only in Lemma S, as quoted in T2 (7).

## Checks

One script at a time, each with py in under 1 s. Scripts are in scripts_price/.
- barrier_check.py, geometry: for all 42 same-parity configurations with X, y < 60 and X^2 + y^2 square, R1 and R2 are genuine rectangles with symmetric difference {A, B, C, D}. There were 0 failures.
- barrier_check.py, counting: for m = 7, consecutive odd rows and slot offsets up to h^(3/2)/2, I computed the per-partner average number of offsets X in 7Z with 7 | y and X^2 + y^2 square, against Lambda^2. At h = 1000, 4000, 16000 and 64000 it was 0.54, 0.89, 1.30 and 1.77. Divided by Lambda^2 this is 0.0114, 0.0129, 0.0139 and 0.0145, roughly constant. Divided by Lambda it is 0.078, 0.107, 0.134 and 0.160, still growing. So the count grows like Lambda^2, as Theorem R predicts.
- theta_beta.py: theta(2) = 1.49676, matching theta*. The table values are as stated. The sorting exponent K(2^(1/K) - 1) is 0.828 at K = 2, 0.780 at K = 3 and 0.696 at K = 100.
- By hand: the identity (r^2 - s^2)^2 + 4r^2 s^2 = (r^2 + s^2)^2; u- = x_e - m|k|s^2 and u+ = x_e + m|k|r^2 are slots; the phi(s) admissible classes mod 2s; the error-term bound; and Corollary R1's R1, R2 bounds for Delta = h Lambda^(-0.5).
Read: heavy_diagonals_sharp, t1_cost_decomposition and its audit, polylog_relocation_diluted and its audit, consolidated_board_v2 (statement, (B0)-(B7), width section), rigid_layout_cross_block (Theorems 1-5 and Section 6), T1, T2, compatible_profile_threshold, sharper_polylogarithmic_threshold, and sec2_prelim. The repository was only read, and no git command was run.

## Gaps

- Theorem R is about a method class: independent uniform slots, one fixed row on empty slots, and certificates that use only event probabilities and the shared-label dependency graph. It is not a lower bound on m_h, and it does not show that no valid placement exists in such a block.
- Certificates that use more than (P(A), dependency graph) are not covered. Examples are arguments that condition on slot occupancy, or entropy compression with a different event structure.
- One loophole: empty slots carrying many different sea rows. Periodic slot rows of period P_s lose only a factor P_s (Theorem R(d)). For arbitrary K-row slot seas, a block-pigeonhole argument gives a loss of at most 2K, but only when the pair-difference counts decrease in |y|, which is not proved for unions of diagonals. Heuristically, Lambda^gamma slot rows trade the Lemma F family for private slot-row triangles whose average does not sort, with a best case of beta about 1.92. This needs a new profile theory with many slot rows, and its other families are not analysed.
- The mod-p-rule class (columns = 2 sigma i mod p, random period) is not covered. There the odd-odd half of Lemma F dies for every period layout: X = sigma y mod p would need (r/s - sigma)^2 = sigma^2 + 1 mod p, which is a nonsquare. The even-even half should still give Lambda^2. That needs equidistribution of Pythagorean legs mod p, which is not proved.
- Corollary R2 holds for the board as specified: kappa-heaviness, B classes allotted per type, and every heavy label relocated. If heaviness is measured by chi(G_T[tau]) and the light width by the largest chi, the floor depends on the unknown chi-heavy count ((Eq)) and on hypothesis (F).
- Corollary R1 reads the block structure of Theorems D and E (period-zero slots, independent uniform centres, product-form LLL) from T1/T2 and the polylog note. I did not re-derive their constructions.
- Lemma V is proved only for unweighted sums. The class-weighted version that T1's accounting needs (sum of the rival count times (v(f)/w)^s) is not done.
- Lemma S assumes K valid T1-type profile families with pairwise distinct sea rows. That is plausible from the candidate windows of filled_mod7 and Lemma AP, but not checked. It cites Henriot Cor. 2 for K forms as T2 (7) does. It does not lower the price, because of Theorem R.
- Two other sources of Theorem A look like overcounts: the non-horizontal two-sea supports R1 and R2, and the higher-arity Cauchy-Schwarz budget. For R1 and R2 the sea gap xi must satisfy xi^2 = X^2 + y^2 - (t-s)^2, an integrality condition T2 ignores. I did not prove either.
- Nothing here has been audited.

## Missing estimate

To get a relocation price Lambda^beta with beta < 2, a block must leave class P. It must exclude the Lemma F configurations deterministically, for both parities, at width o(Lambda^2) per label. Equivalently, its column law must give P(x_f - x_e = |y_ef|(r^2 - s^2)/(2rs)) = o(1/N) on average over pairs and over coprime (r, s) with r/s <= W/h, rs <= h^(1-o(1)).
- The mod-p rule does this for odd-odd pairs without rigidity.
- No known non-rigid mechanism does it for even-even pairs. A second congruence in j (2-adic or mod p') fixes each label's column modulo about h^2, which is the rigid layout, priced by the largest class count (Proposition 4).
- The other way out is an empty-slot sea with Lambda^gamma rows that still satisfies T1's profile properties.
Either way, the heavy diagonals keep price h Lambda^2 in every construction now on file.

## Next steps

- Audit Theorem R. It is short: Lemma F (a two-rectangle check), the (r, s) parametrization, one Cauchy-Schwarz count, and one harmonic sum over coprime pairs. Then audit Corollary R1 against the T2 Section 7 placement.
- If it passes, mark in consolidated_board_v2 and heavy_diagonals_sharp that the prices of Theorems D and E are optimal for their method. The exponent-table entries that rely on better relocation of this type are then excluded.
- Spend effort on absorbing heavy diagonals rigidly, not on relocation: hypothesis (F) (an independent set of density at least 1/K0 in Cay(Z, D_T)), (Eq) (2-adic counts of D_T), or a chi-based heaviness count. Theorem R shows the relocation side is closed in class P.
- Optional: prove the even-even barrier for the mod-p-rule class. That needs a lemma that the Pythagorean legs X = |y|(r^2 - s^2)/(2rs) are equidistributed modulo a prime p of size about h, on average over y and (r, s). It would close the last cheap non-rigid variant.
- Optional: test the row-diverse slot-sea loophole numerically. Count the Lemma F events and the private slot triangles for a toy block with Lambda^gamma slot rows, and check the heuristic best case beta of about 1.92 before building any profile theory.
- Write the weighted form of Lemma V to correct source (i) of Theorem A to O(Q Lambda ell^C). This changes no exponent but makes the accounting accurate.

