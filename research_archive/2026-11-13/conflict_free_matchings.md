# Conflict-free hypergraph matchings and the pair price

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (obstruction to a method): the published conflict-free matching theorems need two vertices of the conflict graph to share at most D^(1-beta) neighbours. The Pythagorean (3,4) lines break this by a polynomial factor for every choice of slot lists (Theorem L), so these theorems give at most an O(log Lambda) gain over the local lemma. No price below Lambda^2 ell^C is proved. Not audited yet.

# Result

## Status

obstruction

## Summary

Obstruction: the published conflict-free matching theorems cannot lower the relocation price exponent below 2 in a T1-type block. Both theorems require that two vertices of the conflict graph share at most D^(1-beta) neighbours. The Pythagorean (3,4) lines from Proposition 2 of pair_families_dp_colouring.md make that fail by a polynomial factor. Theorem L proves this for every choice of slot lists: the hypothesis forces D <= max(2^16 m^3, (192m)^(1/beta)), so log D = O(log m). The gain over the local lemma is then at most O(log Lambda). With random or full lists the best possible price is c Lambda^2/log Lambda. No price below Lambda^2 ell^C is proved.

## Statements

SETTING S (a T1-type block, as in pair_families_dp_colouring.md "Setting": a T2 block, or a Theorem E or Theorem D class block).
- Slot columns are 7j for j in [0, N). Every empty slot, and every period-zero column of the flanking separations, holds the filler row F.
- There are n labels, all in one profile and block type. Odd rows agree mod 14, and so do even rows. Every label row is a bulk row, so F is not a label row and a midpoint row is never F.
- A label is determined by its pair (odd row a, even row b). This holds in T1 and Theorem E, where f_{T,i} has rows (2i+1, 2i+T+1).
- E is T2's event system. Write m = N/n (slots per label) and assume N >= h/8 + 1.

ENCODING (the natural one for both theorems).
- The host is a bipartite graph G with parts A = labels and B = slots, so r = 2. Its edges are the options (e, j), j in L(e), for lists L(e) of slots. Full lists, random lists, residue-restricted lists (for example the mod-p column rule) and arbitrary lists are all allowed.
- The configuration (conflict) hypergraph H has V(H) = E(G). It contains every two-label event {(e,j), (f,j')} of E with e != f and j != j', and optionally the three- and four-label events.
- Coincidences need no conflicts, because a matching uses each slot at most once.
- An H-avoiding A-perfect matching is exactly an injective centre map that avoids E. By Statement 0 of pair_families, it is all the layout needs.

THEOREM L (line obstruction; PROVED for arbitrary lists, from Theorem C (C2) of pair_families, whose (3,4) part I re-derived). Suppose every label has G-degree >= D_A and every slot has G-degree <= D_B <= 2 D_A. If D_A > 2^18 m^3, then H contains two options u, v, with distinct labels and distinct slots, that have more than D_A/(192 m) common neighbours in the 2-uniform part of H. If D_B <= D_A, the threshold 2^16 m^3 suffices.

COROLLARY DP (Delcourt-Postle, arXiv:2204.08981v4, Theorem 1.16, with r = 2).
- Suppose its hypotheses hold for (G, H) in setting S with parameters (g, beta, alpha, D). Then D <= max(2^16 m^3, (192 m)^(1/beta)), so ln D <= lambda_beta(m) := max(16 ln 2 + 3 ln m, (ln 192 + ln m)/beta).
- Its pair hypothesis then reads Delta_2(H) <= alpha lambda_beta(m) D.
- (a) Full lists, G = Z x [N]: the slot degree is n <= D, so the theorem applies only if m >= min(2^(-16/3) n^(1/3), n^beta/192). That price is polynomial in h.
- (b) Any lists: Theorem 1.16 certifies only pairs (G, H) with Delta_2(H)/D <= alpha lambda_beta(m) = O_beta(log m). The T2 local lemma already works at Delta_2(H)/D = O(1). So the theorem gains at most a factor O_beta(log m) = O_beta(log Lambda) when m is polylogarithmic.
- (c) Random lists, each label taking an independent uniform D_A-subset: in expectation, the average H-degree of an option is (D_A/N) times the full-list average, which by Proposition 1(c) of pair_families is at least c n Lstar/7. So the theorem needs m lambda_beta(m) >= c Lstar/alpha. In the main Theorem E classes, Lstar >= c c1 Lambda^2, which gives m >= c_beta Lambda^2/log Lambda. The price exponent stays 2.

COROLLARY GJKKL (Glock-Joos-Kim-Kuhn-Lichev, arXiv:2205.05564v1, Theorems 3.1 to 3.4).
- Condition (C5) is the same common-neighbourhood bound, with d^(1-eps). By Theorem L with D_A = (1-eps)d (or (1-d^(-eps))d) and D_B = d, we get d <= max(2^18 m^3, (192m/(1-eps))^(1/eps)).
- Theorem 3.1 also needs at most exp(d^(eps^2/ell)) vertices, that is, d >= (ln(n+N))^(ell/eps^2).
- Both together force m >= min(2^(-6) (ln N)^(ell/(3 eps^2)), (1-eps)(ln N)^(ell/eps)/192). For eps <= 1/3 this is at least c Lambda^(3 ell), and ell >= 2. I expect eps_0 < 1/3, but the paper gives no explicit eps_0.
- Separately, (C2) together with 1/mu^(Gamma ell) <= d^(eps^2) caps the pair degree at Gamma d <= eps^2 d ln d/(ell ln(1/mu)), which is again O(log m) d.
- So GJKKL gives no price below Lambda^2 either.

PROPOSITION T (a second, independent failure in the natural encodings; PROVED for full lists). Take full lists and two options (e, j), (f, j+1) with odd rows alpha and gamma = alpha + 14, where 2h/7 <= j <= N - 2 - 2h/7. These two options lie in at least n - M0 - 2 three-label events of E (type T3, right angle at e). Here M0 is the largest number of labels sharing an odd row. So Delta_{3,2}(H) >= n - M0 - 2. Theorem 1.16 needs Delta_{3,2}(H) <= D^(1-beta), and GJKKL (C3) needs <= d^(1-eps), with D, d <= N. For random lists of density p, the codegree is about p(n - M0) = D/m. Each fails by a factor D^beta/m.

PRICE PROVED: none. The route gives no price Lambda^beta with beta < 2. The relocation price stays Lambda^2 ell^C (T2, Theorem E), and theta* = 1.4967429 is unchanged. The near goal (a full board in width h^2 (log h)^(2-c)) is not reached by this route. Labels left unplaced: DP's theorem is A-perfect, so it would leave none, and GJKKL's would leave a fraction mu that the old Lambda^2 method could absorb. That accounting is moot, because neither theorem applies.

## Proofs

0. INPUT: THE (3,4) LINES. I re-derived Theorem C (C2) of pair_families.
- Take labels f, g whose odd rows c_f != c_g lie in the same class a* mod 28. Put k = (c_g - c_f)/28, and put the two labels at slots j_f and j_g = j_f + 3k, both in [0, N).
- Then X = 21k, y = 28k and L = 35|k|.
- (X - L)/2 and (X + L)/2 are -7k and 28k for k > 0 (mirrored for k < 0), so u-+ = x_f - 7k and x_f + 28k are multiples of 7.
- They lie within 2h columns of x_f. So they are core slots or period-zero separation columns, and both hold F when empty.
- y is even and nonzero. The midpoint row c_f + 14k is a bulk row, so it is not F, and F is not in {c_f, c_g}.
- So by Lemma F (relocation_price_floor.md, audited) the pair is a two-label event of E. It is T2's horizontal two-sea role, and the two options are disjoint in G.
- No interior condition is needed, because both options exist. The same holds for even rows.
- Option (f, j) lies on the odd line with index j0 = j - 3(c_f - a*)/28. On a line, the row fixes the slot, so options at distinct points of a line have distinct rows, labels and slots. Any two of them form an H-edge. j0 ranges over an interval of length at most N + 3h/28 + 1 <= 2N.
- Sanity script line_common.py: the algebra checks out, and in a random-list toy the mean line size is about D/m, as predicted.

1. PROOF OF THEOREM L. Let t be the maximum common 2-degree of H over pairs of disjoint options.
- Pick a class A* of odd rows mod 28 and a class B* of even rows mod 28 such that the set Z* of labels in both has |Z*| >= n/4. There are 4 combinations. Z* has at least n D_A/4 options.
- A "point" is a pair (slot, row), and its weight is the number of options of class labels there.
- Line dichotomy. Take an odd line with at least 3 occupied points, and put u and v at its two lightest points. Every option w at another point is H-adjacent to both, so t >= s - s_1 - s_2 >= s/3, where s is the line total. So such a line carries at most 3t options. A line with at most 2 occupied points carries fewer than 2 s0 options at points of weight below s0.
- So, over both parities, the options of Z* whose odd point or even point has weight below s0 number at most 2 x 2N(3t + 2 s0) = 12 m n t + 8 m n s0.
- Big-big options. Fix a slot j with label set L_j, where |L_j| <= D_B. Let O_j be the set of odd rows carried by at least s0 labels of L_j, so |O_j| <= D_B/s0, and let E_j be the same for even rows. Labels are injective in (a, b), so the options at j whose odd point and even point both have weight >= s0 number at most |O_j||E_j| <= D_B^2/s0^2. Summed over slots, there are at most m n D_B^2/s0^2 of them.
- Put s0 = D_A/(64 m) and suppose t <= D_A/(192 m). Then 12 m n t <= n D_A/16 and 8 m n s0 = n D_A/8, so at least n D_A/16 options are big-big.
- Hence n D_A/16 <= m n D_B^2 (64m)^2/D_A^2, that is, D_A^3 <= 2^16 m^3 D_B^2. This gives D_A <= 2^18 m^3 if D_B <= 2D_A, and D_A <= 2^16 m^3 if D_B <= D_A. The contrapositive is Theorem L.
- Both parities are needed. With odd lines alone, labels sharing an odd row could stack at one slot. The even lines rule that out, because a label is fixed by (a, b).
- Under the mod-p rule each point holds at most one option, and the even lines alone give t >= D_A/(8m) - 2.

2. COROLLARY DP. In Theorem 1.16, A-degrees are >= (1 + D^(-alpha)) D and B-degrees are <= D. So Theorem L applies with D_A >= D >= D_B.
- If D > 2^16 m^3, then t > D/(192m). The hypothesis t <= D^(1-beta) then forces D < (192m)^(1/beta). This gives the bound on ln D, and the pair hypothesis becomes Delta_2(H) <= alpha D lambda_beta(m).
- (a) With full lists, D >= n, because B-degrees equal n.
- (c) Every option has exactly D_A/N chance per slot. Write e2 for the number of 2-edges. Then E[e2] = (D_A/N)^2 e2_full, and |E(G)| = n D_A. So E[2 e2/|E(G)|] = (D_A/N) x avg_full >= (D_A/N) c n Lstar/7 = c D_A Lstar/(7m).
- Delta_2(H) is at least the average degree. Combining with Delta_2(H) <= alpha D_A lambda_beta(m) gives m lambda_beta(m) >= c Lstar/(7 alpha), and Lstar >= c c1 Lambda^2 holds in the main Theorem E classes (Proposition 1(c)).
- (b) is a restatement.

3. COROLLARY GJKKL.
- (C5) bounds the common neighbourhood of disjoint host edges, which is exactly t, by d^(1-eps). Theorem 3.1 needs every degree between (1 - d^(-eps)) d and d, and Theorem 3.4 between (1 - eps) d and d. So Theorem L applies with D_A = (1-eps)d and D_B = d <= 2 D_A.
- The vertex count is n + N <= exp(d^(eps^2/ell)), which gives the lower bound on d. Combining the two bounds gives the bound on m.
- The Gamma bound follows from 1/mu^(Gamma ell) <= d^(eps^2), since that means Gamma ell ln(1/mu) <= eps^2 ln d.

4. PROPOSITION T. Put A = (7j, alpha), B = (7j + 7, alpha + 14), and give each other label g with odd row rho != alpha the point C = (7j - 2(rho - alpha), rho).
- Same-parity rows agree mod 14, so 7 divides rho - alpha and C lies on a slot. The slot offset is 2(rho - alpha)/7, which is in range by the margin.
- (B - A).(C - A) = 7(-2(rho - alpha)) + 14(rho - alpha) = 0, so the angle at A is right.
- The fourth corner B + C - A is at a period-zero column in the bulk row rho + 14 <= h. With all other slots empty it is white. So {A, B, C} is a three-black tilted rectangle with the right angle at a label point. That is a forbidden type-T3 event of T2 Section 2, not an allowed (high-sea-rooted) triangle.
- The three slots are distinct, so each triple is a matching. Excluding e, f and the at most M0 labels with rho = alpha gives at least n - M0 - 2 three-label events. Bulk rows keep rho + 14 <= h.

5. Remark (sketch): putting lines into the host as vertices does not help. If the lines are host vertices with capacity 1, an option's edge has size 2 plus the number of lines through it. By Proposition 4 of pair_families, the average option lies on at least c Lstar, about Lambda^2, nontrivial lines. Both theorems need r bounded as D grows. If only the directions with |q| < Q0 become vertices, the line argument of step 1 still applies to each remaining direction, with constants polynomial in |q|, so D^beta = O_r(m^(O(1))) again.

## External results used

- Delcourt and Postle, arXiv:2204.08981v4 (24 August 2026), Theorem 1.16. Hypotheses, in my words. Fix integers r, g >= 2 and beta in (0,1); then D_beta and alpha > 0 exist such that the following holds for D >= D_beta. G = (A, B) is a bipartite r-bounded multi-hypergraph, with exactly one A-vertex per edge and codegrees <= D^(1-beta). Every A-vertex has degree >= (1 + D^(-alpha)) D, and every B-vertex has degree <= D. H is a g-bounded configuration hypergraph: V(H) = E(G), and its edges are matchings of size >= 2, so conflicts of size 2 are allowed. Its maximum i-degree is <= alpha D^(i-1) log D for 2 <= i <= g, and Delta_{k,l}(H) <= D^(k-l-beta) for 2 <= l < k <= g. The maximum 2-codegree of G with H is <= D^(1-beta); this is the number of size-2 edges of H containing an edge e and an edge at a vertex v outside e. The maximum common 2-degree of H is <= D^(1-beta); this is #{w : uw, vw in E(H)}. Conclusion: an H-avoiding A-perfect matching exists. The theorem puts no bound on the number of vertices.
- Glock, Joos, Kim, Kuhn, Lichev, arXiv:2205.05564v1, Section 3. C is (d, ell, Gamma, eps)-bounded if: (C1) 2 <= |C| <= ell for every conflict; (C2) the sum over j of Delta(C^(j))/d^(j-1) is <= Gamma, and at most Gamma sizes occur; (C3) Delta_{j'}(C^(j)) <= d^(j-j'-eps) for 2 <= j' < j <= ell; (C4) for every host edge e and vertex v, the 2-conflict partners of e containing v number <= d^(1-eps); (C5) any two disjoint host edges have <= d^(1-eps) common 2-conflict partners. Theorem 3.1: k >= 2, eps < eps_0(k), d >= d_0, 1/mu^(Gamma ell) <= d^(eps^2), at most exp(d^(eps^2/ell)) vertices, every degree in [(1 - d^(-eps)) d, d], and Delta_2 <= d^(1-eps). Conclusion: a C-free matching of size (1 - mu) n/k. Theorem 3.3 adds trackable test functions, with conditions (W1) to (W4). Theorem 3.4 allows degrees in [(1 - eps) d, d], with uncovered fraction sqrt(eps).

## Checks

I read in full: pair_families_dp_colouring.md, higher_arity_true_counts.md, relocation_price_floor.md and its audit, relocation_price_exponent.md, and safe_triangle_pair_first_moment.md (T2). I read the statements and the Theorem E part of t1_cost_decomposition.md. I did not re-read the T2 audit files; I relied on their verdicts as quoted in the notes I read.

Web: the alphaXiv full-text extraction of GJKKL arXiv v1 (pages 8 to 11 and 43 to 51) and of DP arXiv v4 (pages 1 to 21). The arXiv PDF itself was password-protected. I quoted the hypotheses from these readings, and no paper or its text was saved in script folder.

By hand: the (3,4) Lemma F geometry; the line indexing and its range; the dichotomy and big-big counting with the constants 2^16, 2^18 and 192; the T3 right-angle identity and the slot and range conditions of Proposition T; and the corollary arithmetic.

One sanity script, scripts_cfm/line_common.py, ran with py -I in about 1 s. It confirmed the algebra (X = 21k, y = 28k, L = 35|k|, u+- multiples of 7, the T3 dot product 0). On random lists it found mean (3,4)-line sizes of 8.7, 34, 18.4 and 38.3, against D/m = 10, 40, 20 and 40, with maximum common line-neighbourhoods of 18 to 58. That agrees with the D/m scaling.

The repository was only read. I ran no git command and wrote no report file.

## Gaps

- Theorem L relies on Theorem C (C2) of pair_families_dp_colouring.md, which is unaudited. I re-derived its (3,4) part myself: the Lemma F check, the u+- columns, the midpoint and the line indexing. Lemma F itself is audited.
- Theorem L needs the (3,4) Lemma F events of both parities in H. A method that keeps the odd-parity events out of H and kills them some other way, without making each point hold at most one option, gets only D <= 32 m M0 from the even lines. I did not close that case. The mod-p rule is covered, because it makes each point hold at most one option.
- Corollary DP(c) is stated in expectation. A high-probability version needs a standard concentration argument, which I did not write out. The Lambda^2/log Lambda figure is a ceiling on what DP can give. I did not prove that DP actually reaches it: the codegree hypotheses for the M-type and h^(o(1)) roles at D = Lambda^C are unchecked, and so is the cross-direction triangle count (IT).
- GJKKL: I read only arXiv v1 (the only arXiv version). I did not read the published J. London Math. Soc. version. eps_0 is not explicit, so the Lambda^(3 ell) bound assumes eps <= 1/3. The Gamma-based O(log m) cap does not need that assumption.
- DP: I read arXiv v4 (24 August 2026) through extracted text, not line by line. Theorem 1.16's alpha depends on (r, g, beta) and is not explicit.
- Proposition T is proved only for full lists. For random lists, the D/m codegree is an expectation estimate. For arbitrary lists I have no lower bound on Delta_{3,2}.
- Theorem D class blocks are covered by the stated Setting (copied from pair_families). I did not read polylog_relocation_diluted.md (D4) myself.
- Small blocks (N < h/8) are not covered. They cost O(h^2) and do not matter for the exponent.
- The obstruction is to a method: theorems whose hypotheses are degree, codegree or common-degree bounds on (G, H). It is not a lower bound on the relocation price, and it does not exclude a bespoke nibble that treats lines as capacity-1 resources.

## Missing estimate

To get a price of Lambda^(1+o(1)) by this route, two things are needed, and neither exists in the published literature I checked.
(1) A conflict-free A-perfect matching theorem for bipartite hosts in which the 2-conflicts split as H_lines + H_rest. H_lines must be an edge-disjoint union of cliques, each meeting each label's star at most once, with an unbounded number of lines through each option (about Lambda^2 of them, Proposition 4). Only H_rest would have common 2-degree at most D^(1-beta). The pair degree may be up to alpha D log D, with D >= h^c. Equivalently: a nibble for hypergraphs with edges of size about Lambda^2 >> log D, where only the label side must be covered.
(2) The (3,2) codegree hypothesis must be replaced by a label-aware one. Two chosen options kill about D/m options, but at most O(1) per third label (Proposition T), and the theorem must tolerate that. Then the new codegree condition must be verified, which needs (IT): non-collinear integral triangles through an option number at most D(o)^2 h^(-c).
Once (1) and (2) hold, the price is about Lambda ell^C, and Theorem P gives exponent theta_E(1) = 0.9101 with Theorem DC. Without them, conflict-free matchings give at most a factor O(log Lambda), which is invisible in the exponent.

## Next steps

- Audit Theorem L. It is one page: the line dichotomy, the big-big count |O_j||E_j| <= D_B^2/s0^2 and the constants. Audit Theorem C (C2) with it. If both pass, add a ledger row: conflict-free matching theorems (DP 1.16, GJKKL 3.1 to 3.4) gain at most O(log m) over the local lemma in T1-type blocks; method obstruction, next to Theorem R and Corollary C3.
- Close the open case of Theorem L, where odd-parity Lemma F events are kept out of H by a device other than the mod-p rule. Either show that stacking by odd row is self-defeating through another family (the even lines plus the Hz events), or record it as a loophole.
- Do not spend effort on further hypothesis-checking of DP or GJKKL in this encoding. The ceiling is Lambda^2/log Lambda.
- If the route is pursued, write the line-nibble directly (Missing estimate (1)). Treat each line as a capacity-1 resource, and track list sizes and line loads, with McDiarmid concentration and Lipschitz constants mu_ef <= h^(o(1)). First test numerically on a toy block whether random greedy succeeds at N of about D/ln N. Then compute (IT) on a real T2 profile block.

