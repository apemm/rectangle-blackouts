# Choice rules that cannot handle every factor

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (obstruction): on the full-grid Hilbert placement, for every even S and every M, the factor-one family alone defeats every choice rule that, on some window of Hilbert levels, sees the label's rank digits only through an additive statistic in an abelian group of order at most the window length; the same holds for level-independent group automata and for rules that also read the exact diagonal T. Dyadic-sum, Gray-code, base-M digit and bounded T-reading rules all fail. The note concludes that a working rule has to read the rank at a scale tied to T, as the factor-one rule floor(r/d0) mod 2 does; its audit (audit_hilbert_choice_rule_obstruction.md) confirms the theorems but finds that conclusion to be an interpretation, not a proved statement.

# Result

## Status

obstruction

## Summary

I found no bounded-M rule that handles every factor at once. I did prove a strong negative result: on the full-grid Hilbert placement, for every even S and every M, factor one alone defeats every choice rule that, on some window of Hilbert levels, sees the label's digits only through an additive statistic in an abelian group of order at most the window length. The same holds for level-independent group automata, and for rules that also read the label's exact diagonal T. The proofs construct explicit translation atoms and diagonal atoms; each one is an actual factor-one P conflict whenever its two labels receive equal choices. This class contains every rule the target suggested except the base-M digit sum (which an atom search still beat) and rules whose rank scale depends on T. All three suggested rule types fail: dyadic-sum and Gray-code rules, base-M digit rules, and T-reading rules with bounded rank information. Any working rule has to read the rank at a scale tied to T, the way the factor-one rule floor(r/d0) mod 2 does. Not audited yet.

## Statements

SETTING. This is the full-grid placement of the placement note, with every label kept. Labels are (i,j) with 0 <= i < ceil(h/2) and 0 <= j < floor(h/2). Q = 2^n is the least power of two >= ceil(h/2). The rank is r = H_Q^{-1}(i,j) = sum_l d_l 4^l, with base-4 digits d_l (l = 0..n-1) in the archive's recursion (quadrant maps 0:(y,x), 1:(x,y+q), 2:(x+q,y+q), 3:(2q-1-y,q-1-x)). Columns are x_e = S(M r_e + xi_e), with S >= 2 even, M >= 1 and xi_e in {0..M-1}. A "choice rule" is any function xi of the label, and it may depend on h. A "conflict" is an actual in-strip P violation: two labels e, f and a cross-parity pair of their points with X^2 + y^2 = L^2, both completion rows in [1,h], and the owner label of the completion rows in a column other than the midpoint column. It is "factor one" when (L-|y|)/2 = 1. Write v2 for the 2-adic valuation. The 1/2-merged address mu(e) is the digit string with 1 and 2 identified. The 0/2-merged address nu(e) is the digit string with 0 and 2 identified. omega(e) is the terminal Hilbert orientation.

LEMMA A (translation atoms; proved). Let R = [lam_lo, lam_hi] with lam_lo >= 1. Let K be a nonempty subset of R with lam_hi + 5 <= 2 v2(S) + 2 v2(M) + 4 min K. Let h >= S^2 M^2 16^(lam_hi+1)/2. Then there are labels e, f with these properties. Their digits agree outside K. On K, e has digit 1 and f has digit 2. On R \ K both have digit 2. Also r_f - r_e = D := sum_{k in K} 4^k, i_f = i_e, and |j_f - j_e| = sum_{k in K} 2^k. For EVERY choice vector with xi_e = xi_f, the pair (e,f) is a factor-one conflict: X = SMD, y = X^2/4 - 1, L = X^2/4 + 1, completion rows 2 i_e and 2 j_f + 3, and owner g = (j_f + 1, i_e - 1).

LEMMA B (diagonal atoms; proved). Let K = [k_b, k_t] have even length, k_b >= 1, k_t + 3 <= 2 v2(S) + 2 v2(M) + 4 k_b, and h >= 2 S^2 M^2 16^(k_t+1). Then there are labels e, f with these properties. Their digits agree outside K. On K, e has digit 0 and f has digit 2. Also T_e = T_f (where T = j - i), nu(e) = nu(f), omega(e) = omega(f), r_f - r_e = D := 2 sum_K 4^k, and f - e = eps (2^(k_t+1) - 2^(k_b)) (1,1) with eps = +1 or -1. For every choice vector with xi_e = xi_f, (e,f) is a factor-one conflict.

THEOREM A (additive rules fail; proved). Assume R, Lambda (a nonempty subset of R), S, M satisfy lam_lo >= 1, lam_hi + 5 <= 2 v2(S) + 2 v2(M) + 4 min Lambda, and h >= S^2 M^2 16^(lam_hi+1)/2. Assume a choice rule xi satisfies condition (ADD). (ADD): there are an abelian group H with |H| <= |Lambda|, elements g_k in H for k in Lambda, and a function Phi such that xi(e) = Phi(b(e), sum_{k in Lambda, d_k(e)=1} g_k). This must hold for every label e whose digits are in {1,2} on Lambda and equal to 2 on R \ Lambda, where b(e) denotes the digits of e outside R. Then xi has a factor-one conflict at height h.

COROLLARY A1 (explicit class; proved). Let G be a finite abelian group and let P >= 1 and c >= 0 be integers. Put N = |G| P^2 and lam = max(c, 1, ceil((N+2)/3)). Every rule of the form
  xi(e) = F( d_0..d_{c-1}, mu(e), sum_l gamma_l(d_l(e)) in G, r_e mod P, i_e mod P, j_e mod P ),
with arbitrary gamma_l: {0,1,2,3} -> G and arbitrary F (both may depend on h), has a factor-one conflict at every h >= S^2 M^2 16^(lam+N)/2. Because F reads mu(e), it may use the whole orientation sequence, the terminal orientation, every digit 0 or 3, and T mod P. The corollary covers all of the following:
- popcount(r) mod m, which equals the sum over k of floor(r/2^k) mod 2, taken mod m (N = 1);
- sum_k floor(r/2^k) mod m (N = m);
- base-4 digit sums mod m;
- r mod P;
- floor(r/P1) mod P2;
- any fixed base-M digit of r;
- (i+j) mod P, (i-j) mod P and T mod P;
- the terminal orientation;
- and all functions of these.

COROLLARY A2 (Gray code; proved). Gray(r) mod P and popcount(Gray(r)) mod m, where Gray(r) = r XOR (r>>1), have factor-one conflicts at every h >= S^2 M^2 16^(lam+2N+1)/2, with N = P (respectively m) and lam = max(1, ceil((2N-1)/3)).

COROLLARY A3 (level-independent group automata; proved). Let G be any finite group, possibly nonabelian, of exponent m. Let gamma: {0,1,2,3} -> G be independent of the level, and set pi(e) = gamma(d_{n-1}) ... gamma(d_0) (or the reversed product). Every rule xi = F(mu(e), pi(e)) has a factor-one conflict at every h >= S^2 M^2 16^(k0+2m-1)/2, with k0 = ceil((2m+1)/3).

THEOREM B (rules reading the exact diagonal; proved). Let G, P, c and N = |G| P^2 be as above, and put lam = max(c, 1, ceil(2N/3)). Every rule
  xi(e) = F( T_e, nu(e), omega(e), d_0..d_{c-1}, sum_l gamma_l(d_l(e)) in G, r_e mod P, i_e mod P, j_e mod P ),
with F arbitrary, including an arbitrary dependence on T, has a factor-one conflict at every h >= 2 S^2 M^2 16^(lam+2N).

CONSEQUENCES (proved, given the above).
(1) Every rule that avoids all factor-one conflicts must satisfy xi_e != xi_f on every Lemma A pair and every Lemma B pair. So on every admissible window of levels it must fail (ADD) for every abelian group of order at most the window length. The factor-one theorem's rule meets this condition: on a Lemma A or Lemma B pair, q = MD, d0 = D, and floor(r/D) mod 2 flips. It reads the rank at the T-dependent scale d0(T).
(2) Our atom pairs belong to the factor-one family. The single-factor problem was solved with M = 2, but only by a component-aware rule. So any single rule for all factors must contain T-coupled, non-additive rank information at least as rich as that rule's.

NOT PROVED. I have no bounded-M rule for all factors, or even for any infinite set of factors. I have no impossibility result for these classes:
- T-coupled scale rules xi = F(T, floor(r/w(T)) mod P) with arbitrary w;
- level-dependent nonabelian automata;
- general finite automata;
- arbitrary rules (the bounded-M question stays open).
I have nothing for H7 blocks (row step 28, S = 6272 sigma), for retained-subset placements, or for randomized curves.

## Proofs

0. FATAL-PAIR CRITERION (archive). This is the criterion of continuation_hilbert_two_choice_obstruction.md Section 2 and continuation_hilbert_residue_obstruction.md Section 3, and the predicate used in their verifiers. Take labels e, f with x_f > x_e, and a cross-parity pair C, D of their points with X = x_f - x_e even, X^2 + y^2 = L^2, and integer completion rows lo, hi = (s -+ L)/2 in [1,h], where s is the sum of the two rows. Suppose the owner g (odd row and even row equal to lo and hi) is a label not in {e, f}, and x_g differs from the midpoint column x_m = (x_e+x_f)/2. Then the tilted rectangle {C, D, P = (x_m,lo), Z = (x_m,hi)} and the axis rectangle {P, Z, U = (x_g,lo), V = (x_g,hi)} are distinct. Their symmetric difference {C, D, U, V} consists of black label points, so their non-black corners coincide whatever the fillers. That is a violation.

1. DIGIT FORMULA (Lemma 1). The Klein group V = {id, swap, -id, -swap} acts on {0,1}^2 by (x,y) -> (x,y), (y,x), (1-x,1-y) and (1-y,1-x). Put
- L_0 = swap, L_1 = L_2 = id, L_3 = -swap;
- c_0 = (0,0), c_1 = (0,1), c_2 = (1,1), c_3 = (1,0);
- o_{n-1} = id and o_{l-1} = o_l L_{d_l}.
Claim: H_Q(r) = sum_l 2^l o_l(c_{d_l}).
Proof by induction on n. The recursion gives H_{2q}(d q^2 + r') = phi_d(H_q(r')) with phi_d(v) = q c_d + psi_d(v). Here psi_0 = swap, psi_1 = psi_2 = id, and psi_3(x,y) = (q-1-y, q-1-x), all acting on [0,q)^2. Since q - 1 - sum_{l<m} 2^l w_l = sum 2^l (1 - w_l) for w_l in {0,1}, a map psi of type g acts on sum 2^l w_l as sum 2^l g(w_l). V is abelian, so the order of composition is irrelevant.
Consequences:
(C1) Write tau(o,d) = b - a for (a,b) = o(c_d), so that T = sum_l 2^l tau(o_l, d_l). Then tau(o,0) = tau(o,2) = 0 for every o, because V preserves the diagonal {(0,0),(1,1)}. Also tau(o,1) = sigma(o) and tau(o,3) = -sigma(o), with sigma(id) = sigma(-swap) = 1 and sigma(swap) = sigma(-id) = -1. So at any level, digits 1 and 3 realize tau = +1 and -1 (both signs are available), and digits 0 and 2 realize tau = 0. Digits 0 and 2 can also realize either offset (0,0) or (1,1). They give o_{l-1} in {o_l, o_l swap}, and exactly one of these lies in {swap, -swap}.
(C2) L_1 = L_2, so changing digits 1 to 2 leaves every o_l unchanged. The change at level k is 2^k [o_k(1,1) - o_k(0,1)] = 2^k ell(o_k), with ell(id) = (1,0), ell(swap) = (0,1), ell(-id) = (-1,0) and ell(-swap) = (0,-1). For o in {swap, -swap}, ell(o) = (0, -sigma(o)).
(C3) Consider changing 0 to 2 on an even-length interval K. Inside K, both orientation sequences lie in the coset o_{k_t}{id, swap}, and their sequences agree below K because swap^|K| = id. The change at each level k in K is eps 2^k (1,1), with eps = +1 exactly when o_{k_t} is in {id, swap}.

2. PROOF OF LEMMA A. Set N0 = S^2 M^2 D^2/8. This is an integer, since 4 | S^2 and 16 | D^2. Its valuation is v2(N0) = 2v2(S) + 2v2(M) + 4 min K - 3 >= lam_hi + 2. Also N0 < S^2 M^2 16^(lam_hi+1)/72 <= h/32 <= 2^(n-4), so the binary digits of N0 lie in [lam_hi + 2, n - 5]. Choose the digits of e from the top down:
(a) At levels n-1, n-2, n-3, choose digits in {0,2} with offsets (0,0), (1,1), (0,0). This puts e in [Q/4, 3Q/8)^2.
(b) At level lam_hi + 1, choose a digit in {0,2} so that o_{lam_hi} is in {swap, -swap}.
(c) On R, put 1 on K and 2 elsewhere. Then o_k = o_{lam_hi} =: o for every k in R.
(d) At level 0, put tau = -1.
(e) At every other level l, put tau = bit_l(N0).
f is e with digit 2 on K.
By (C2), f - e = sum_K 2^k (0, -sigma(o)), so i_f = i_e and j_f - j_e = -sigma(o) D' with D' = sum_K 2^k. By (C1), T_e = N0 - 1 + sigma(o) D'. Hence j_f - i_e = T_e + (j_f - j_e) = N0 - 1, and r_f - r_e = D.
Now suppose xi_e = xi_f. Take C = (x_e, 2 i_e + 1) and D_pt = (x_f, 2 j_f + 2). Then X = SMD, X^2/4 = 2 N0, y = 2N0 - 1 = X^2/4 - 1, and L = X^2/4 + 1, so L^2 - y^2 = X^2. Also s = 2 i_e + 2 j_f + 3, and since L = 2(j_f - i_e) + 3 the completion rows are 2 i_e and 2 j_f + 3. The owner is g = (j_f + 1, i_e - 1).
Ranges: e and f lie in one aligned block of side 2^(lam_hi+1) inside [Q/4, 3Q/8)^2. Because Q/2 < ceil(h/2), Q/2 <= floor(h/2), and Q <= h, the labels e, f, g are in the grid, both completion rows are in [1,h] (2 i_e >= Q/2 and 2 j_f + 3 < 3Q/4 + 2 <= h), and X is even.
Genuineness: D is even, so x_m = S(M(r_e + D/2) + xi_e). Only the label u with rank r_e + D/2, and only when xi_u = xi_e, has column x_m. That label u lies in the same block, so |i_u - i_e| < 2^(lam_hi+1). But i_g - i_e = N0 >= 2^(lam_hi+2). So x_g != x_m for every choice vector, and g is not e or f since i_g != i_e = i_f. Step 0 now gives the violation. Finally, (L - y)/2 = 1.

3. PROOF OF LEMMA B. Here D = 2 sum_K 4^k, D' = 2^(k_t+1) - 2^(k_b), and N0 = S^2 M^2 D^2/8. Then v2(N0) = 2v2(S) + 2v2(M) + 4 k_b - 1 >= k_t + 2, and N0 < S^2 M^2 16^(k_t+1)/18 <= 2^(n-4). Choose the digits of e:
- the top three levels as in Lemma A;
- digit 0 on K;
- tau = +1 at the levels 0..k_b - 1;
- tau = -1 at level k_t + 1;
- tau = bit_l(N0) at the remaining levels.
f is e with digit 2 on K. By (C3), the orientations of e and f agree outside the interior of K. The digit-0 and digit-2 levels contribute tau = 0, so T_e = T_f = (2^(k_b) - 1) - 2^(k_t+1) + N0 = N0 - 1 - D', and f - e = eps D' (1,1). If eps = +1, use the odd point of e and the even point of f: y = 2(j_f - i_e) + 1 = 2(T_e + D') + 1 = 2N0 - 1. If eps = -1, use the even point of e and the odd point of f: y = 2(j_e - i_f) + 1 = 2N0 - 1. In both cases X = SMD and L = X^2/4 + 1. The completion rows are (2 i_e, 2 j_f + 3) in the first case and (2 i_f, 2 j_e + 3) in the second, and the owners are (j_f + 1, i_e - 1) and (j_e + 1, i_f - 1). The range and genuineness checks of Lemma A apply verbatim: the owner's first coordinate exceeds the pair's by N0 >= 2^(k_t+2). Also nu(e) = nu(f), and omega(e) = omega(f) because swap^|K| = id.

4. PROOF OF THEOREM A. Order Lambda as k_1 < ... < k_N and take the prefix sums s_0 = 0, s_t = g_{k_1} + ... + g_{k_t}. These are N+1 values in H, and |H| <= N, so s_t = s_t' for some t < t'. Put K = {k_(t+1), ..., k_t'}. It is nonempty, and its g-sum is zero. Lemma A applies, since min K >= min Lambda. Its e and f both satisfy the hypothesis of (ADD): their digits are in {1,2} on Lambda and equal to 2 on R \ Lambda, and they have the same b. The statistic is sum_K g_k = 0 for e and 0 for f. So xi_e = Phi(b, 0) = xi_f, and Lemma A gives the conflict. The construction does not loop back on itself: b depends on K, but g_k does not depend on b.

5. PROOF OF COROLLARY A1. Take R = Lambda = [lam, lam + N - 1]. The bound lam >= (N+2)/3, together with v2(S) >= 1, gives the valuation condition. Check (ADD) for labels with digits in {1,2} on R:
- The low digits are part of b, because lam >= c.
- mu(e) is a function of b.
- The G-statistic is constant(b) + sum_{K'} (gamma_k(1) - gamma_k(2)).
- The rank is r = r_0(b) - sum_{K'} 4^k.
- By (C2), with o_k = o(b) constant on R: i = i_0(b) - ell_1(b) sum_{K'} 2^k and j = j_0(b) - ell_2(b) sum_{K'} 2^k.
So H = G x Z/P x Z/P with g_k = (gamma_k(1) - gamma_k(2), -4^k, 2^k), and Phi(b, .) recovers every input of F. The size condition is |H| = N = |Lambda|. For popcount(r) mod m, the statistic is constant on R because popcount(1) = popcount(2), so H is trivial and N = 1.

6. PROOF OF COROLLARY A2. Take R = [lam, lam + 2N] and Lambda = {lam+1, lam+3, ..., lam+2N-1}. Digit 1 has bits (b_2k, b_2k+1) = (1,0), and digit 2 has bits (0,1). The neighbours of each level k in Lambda carry digit 2. Changing d_k from 2 to 1 changes Gray bit 2k-1 = b_2k-1 XOR b_2k = 1 XOR b_2k from 1 to 0, leaves bit 2k at 1, and changes bit 2k+1 = b_2k+1 XOR b_2k+2 from 1 to 0. These bit triples are disjoint for distinct k in Lambda. So Gray(r) = G_0(b) - sum_{K'} 5 * 2^(2k-1), and popcount(Gray(r)) = p_0(b) - 2|K'|. Both are additive. Apply Theorem A with H = Z/P (respectively Z/m). The valuation condition 3 lam >= 2N - 1 is the stated choice of lam.

7. PROOF OF COROLLARY A3. Take K = {k0, k0+2, ..., k0+2m-2} and R = [k0, k0+2m-2]. Lemma A applies, since 3 k0 >= 2m + 1 gives the valuation condition. The word of e on R is 1 2 1 2 ... 1 (length 2m-1), and the word of f is 2^(2m-1). Their products in G are (gamma(1)gamma(2))^(m-1) gamma(1) = (gamma(1)gamma(2))^m gamma(2)^(-1) = gamma(2)^(-1) and gamma(2)^(2m) gamma(2)^(-1) = gamma(2)^(-1). These are equal. The digits outside R are equal, so pi(e) = pi(f). The same holds for the reversed product, because the word is a palindrome. Finally mu(e) = mu(f).

8. PROOF OF THEOREM B. Let Lambda = [lam, lam + 2N - 1] and g_k = (gamma_k(2) - gamma_k(0), 2 * 4^k mod P, 2^k mod P) in H = G x (Z/P)^2. Take even prefix sums s_t = sum_{k < lam + 2t} g_k for t = 0..N. Two of them are equal, s_t = s_t', and K = [lam + 2t, lam + 2t' - 1] is an even-length interval with zero g-sum. The valuation condition k_t <= 4 k_b - 1 follows from lam >= 2N/3. Lemma B gives e and f. For them:
- T, nu and omega are equal;
- the low digits are equal (lam >= c);
- the statistic difference is sum_K (gamma_k(2) - gamma_k(0)) = 0;
- r_f - r_e = sum_K 2 * 4^k, which is 0 mod P;
- f - e = eps sum_K 2^k (1,1), which is 0 mod P.
So xi_e = xi_f.

9. CONSEQUENCE (1). Lemma A and Lemma B pairs are factor-one conflicts exactly when xi_e = xi_f. If xi_f - xi_e = delta != 0, X changes and y does not, so the pair is generally no longer Pythagorean. On a Lemma A or Lemma B pair, q = MD with M | q, so the component rule of the factor-one theorem uses d0 = D, and floor(r/D) mod 2 changes by exactly 1 across rank gap D.

10. RECORDED OBSTRUCTIONS.
- The two-choice (five-label, factors 1 and 245) obstruction already kills every M = 2 rule at S = 32 and h = 2048 * 2^k. So a successful rule needs M >= 3, and our theorems hold for every M.
- The P triangle at h = 4096 is an M = 1 odd cycle. At M = 1 every atom above is a conflict, and it imposes nothing on M >= 2.
- The archive's dyadic-residue P obstruction is an unsteered M = 1 Lemma A atom with |K| = 1 (Delta i = q there; the steering of step 2(b) makes Delta i = 0). Theorem A extends it to every M and to additive statistics.
- The dyadic-residue and orientation notes concern class rules for right angles at M = 1. They do not constrain P choice rules; Theorems A and B are their P analogue for choice rules.
- The height-independent cores defeat degeneracy certificates, not rules. They are SAT. The atoms here are single-edge rule obstructions, so the two results are complementary.

## External results used

- No published theorem is used. The zero-sum step is the elementary pigeonhole on prefix sums: any N elements of a group of order N have a nonempty consecutive block with zero sum. It is proved inline.
- From the audited archive I use the full-grid Hilbert placement and its recursion (continuation_hilbert_placement.md). I also use the fatal-pair (presentation) criterion of continuation_hilbert_two_choice_obstruction.md Section 2 and continuation_hilbert_residue_obstruction.md Section 3. Hypotheses: every label is kept; the owner is a label in a column different from the midpoint column; and both completion rows are integers in [1,h].

## Checks

All scripts are in scripts_hb3_struct_rule/. Every run used py -B, took under 60 s and used little memory. Nothing was imported from the archive, and the repository was not touched.

atoms.py: an iterative copy of the archive's Hilbert point and rank functions. They reproduce the archive labels (295029 -> (132,651), 1331100 -> (187,1549)) and are inverse to each other on random ranks. The script builds Lemma A atoms for K = {1}, {2}, {2,3,5}, {3,4} and Lemma B atoms for K = [1,2], [2,3], [2,5], [3,6], all at S = 32 and M = 3. For each it asserts the factor-one Pythagorean identity, completion rows in [1,h], the owner a label, the owner column different from the midpoint for every xi_g, and the rectangle geometry. It does this at h = 2^(n+1) and 2^(n+1) - 7, and in a separate run for every h in (2^19, 2^20] and every common xi. Observed: Delta i = 0 and Delta j = 2, 4, 44, 24 for A, and T_e = T_f for B. All pass.

rules_test.py: an atom search for explicit M = 3 rules. Every rule tested has an actual conflict:
- popcount(r) mod 3: K = {1}, h = 2^21.
- sum_k floor(r/2^k) mod 3, base-4 digit sum mod 3, r mod 3: K = {1,2,3}, h = 2^29.
- floor(r/3) mod 3: K = {1,4}, h = 2^33.
- base-3 digit sum mod 3, Gray(r) mod 3, popcount(Gray) mod 3, (i+j+r) mod 3: K = {1}, h = 2^21.
- (T + popcount r) mod 3: K = {1,2}, h = 2^25.
- floor(r/w(T)) mod 3 with w = rounded factor-one gap: K = {1}, h = 2^21.

class_test.py: random members of each theorem's class, with K chosen by the proofs' zero-sum argument, not by search:
- Theorem A with (|G|, P) in {(1,1), (2,1), (3,1), (5,1), (3,2), (2,3)}, three rules each;
- Theorem B with random hash rules reading T exactly, (|G|, P) in {(1,1), (2,1), (3,1), (2,2)};
- Corollary A3 with random S_3 automata (K = {5,7,...,15}, h = 2^77).
Every rule had xi_e = xi_f and a verified conflict.

core_rules.py: my own builder for the height-independent systems G_256^o. It reproduces the archive count of 48419 constraints for id; swap gives 48825. All rules above violate 22 to 25.5 percent of the constraints, against 24.3 percent for a random rule. This matches the archive's 25 to 27 percent at B = 1024. On these blocks T is small, so the T-aware rule reduces to r mod 3. The cores say nothing about rules.

## Gaps

- No bounded-M rule is found for all factors, or for any infinite set of factors. The target of the route is not reached on the positive side.
- I have no impossibility result for T-coupled scale rules xi = F(T, floor(r/w(T)) mod P) with w unbounded. The atoms are essentially unique per T, so a designer can tune w(T) to each atom. A computer search did beat the naive version with w = rounded factor-one rank gap: type A atom at K = {1}, h = 2^21. The exact component rule avoids all the atoms by design.
- There is no result for level-dependent nonabelian automata, for general (non-group) finite automata, or for arbitrary rules. The bounded-M question at fixed S stays open in both directions.
- All results are for the full-grid placement with every label kept and the standard Hilbert order. I did not check the H7 blocks (row step 28, S = 6272 sigma). The analogue needs y = b0 - a0 + 28(j_f - i_e) to match X^2/(4a) - a, which forces a = a0 - b0 (mod 28). It also needs an owner label in the block with residues (b0 + 1, a0 - 1). For retained subsets the owner may be missing. I did not treat randomized curves either. The method needs rank-consecutive translated children (here Q2 -> Q3) at the levels of the window.
- The fatal-pair criterion (Step 0) is the archive's presentation argument, taken from audited notes. My scripts recheck the geometry and the owner column, not a full board.
- The height thresholds are explicit but crude. Example: the theorem gives h >= 1.18e6 for popcount mod 3 at S = 32, but a conflict already exists at every h in (2^19, 2^20].
- Not independently audited. Lemma A, Lemma B and all instances of the theorems were checked by exact sparse computation (see checks).

## Missing estimate

On the obstruction side: to refute T-coupled scale rules xi = F(T, floor(r/w(T)) mod P), I need two or more atoms at the same T, or on nearby T-lines inside one rank window, whose rank gaps D_1, D_2 come from different factors a_1, a_2 sharing the same y = X^2/(4a) - a. Equivalently, a divisor-rich y with several representations X_u = (y^2/u - u)/2 that are all of the atom form S(M D + delta). On the positive side: a rule that, at every label, separates all the per-factor rank gaps d_a(T), about (2/(SM)) sqrt(a |2T+1|), simultaneously with M bounded, and that stays non-additive on every Hilbert window, as Theorems A and B require.

## Next steps

- Audit Lemma A, Lemma B, Theorems A and B and Corollaries A1 to A3, in particular the digit formula (Lemma 1) and the steering steps.
- Port Lemma A to the H7 blocks (row step 28, S = 6272 sigma, a = a0 - b0 mod 28, owner in the residue block (b0+1, a0-1)). This would show that additive rules also fail on the actual board design, not only on the full-grid scaffold.
- Attack T-coupled scale rules: search the full-grid candidate system for pairs of factor-a and factor-a' constraints on one T-line at nearby ranks with incompatible scale requirements. A family of such pairs would refute every rule of the form F(T, floor(r/w(T)) mod P).
- Positive side: test multi-scale T-coupled rules, for example xi = sum over a of floor(r/d_a(T)) mod M over the small factors, on full systems at h = 4096 to 16384 with the archive's band generator. Report the violated factor patterns.
- For this round's randomized-curve idea: check whether a randomized curve keeps rank-consecutive translated children at every level. If it does, Theorem A holds for it verbatim. If it does not, additive rules are no longer excluded by this method.

