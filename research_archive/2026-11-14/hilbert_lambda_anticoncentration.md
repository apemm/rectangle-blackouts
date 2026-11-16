# Anti-concentration for the angle and mixed families

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (partial, with barriers): no anti-concentration bound for Lambda3 and Lambda4 at small stride. A dense barrier configuration shows that pairwise Hilbert locality, column divisibility and the normal forms cannot bound the induced density below 1.5(m - 1) with m - 1 >= 12(h-1)/(M^3 S^4) - 2, so locality-only methods cannot beat the S^4 thresholds. Also: a mixed-arity choice lemma with explicit M (M > 8 B_P + B_Lambda3 + B_Lambda4), four elementary Hilbert lemmas (one, exact translation atoms at gap 4^k, refutes every pointwise equidistribution hypothesis and explains the census hubs), and a reduction to one joint estimate. Audited in audit_hilbert_g_and_lambda.md (correct with fixable gaps).

# Result

## Status

partial

## Summary

The anti-concentration bound for Lambda3/Lambda4 is not proved. New results: (1) a dense barrier configuration shows that pairwise Hilbert locality, column divisibility and the normal forms cannot bound the induced (criterion-(8)) density below 1.5(m-1), with m-1 >= 12(h-1)/(M^3 S^4) - 2; so locality-only methods cannot beat the S^4 thresholds even on induced averages. (2) A mixed-arity choice lemma with explicit M (M > 8B_P + B_Lambda3 + B_Lambda4). (3) Four elementary Hilbert lemmas; one of them (exact translation atoms at gap 4^k) refutes every pointwise equidistribution hypothesis and explains the census hubs. (4) A reduction of the target to one joint estimate. (5) Data: at fixed S the mean degree and the peeling degeneracy both grow, consistent with log^2 h.

## Statements

Setting (full-grid Hilbert core, as in hilbert_angles_mixed_thresholds.md). S = 2^e >= 8, K = S^2/2. Label e = (i,j) has rank r_e in the recursion-(2) Hilbert order of the q-square and slot sigma_e = M r_e + xi_e, with column S sigma_e and points (S sigma_e, 2i+1) and (S sigma_e, 2j+2). A Lambda3 constraint is a 5-tuple (v, f, g, delta_f, delta_g) in which the vertex V is a point of v, F is the same-parity point of f and G the other-parity point of g. It forbids xi_f - xi_v = delta_f together with xi_g - xi_v = delta_g whenever these make (V,F,G) a tilted cross-parity right angle with its fourth corner in the strip. Theorem 1 of the angles note gives the normal form F - V = lambda(Sa, S^2 b), G - V = c(-Sb, a). Lambda4 constraints are defined the same way from Theorem 2(b),(c). "Candidate" means over all choice vectors.

THEOREM A (mixed-arity choice lemma; PROVED). Let Z be a finite label set and give each z a choice xi_z in {0,...,M-1}. A constraint E is a label set J_E (2 <= |J_E| <= 4) with a forbidden set Phi_E of choice vectors on J_E. Its multiplicity m_E is the largest number of values of one label that complete a forbidden vector once the other labels of J_E are fixed. For U in Z put w_U(z) = sum of m_E over E with z in J_E inside U, and
  B = max over nonempty U of (1/|U|) * sum over E with J_E inside U of |J_E| m_E.
(a) If every nonempty U has a label z with w_U(z) <= M-1, then some choice avoids every constraint. In particular B < M suffices.
(b) Every P, Lambda3 (including the two-label case f = g) and Lambda4 constraint written as a pattern of choice differences has m_E = 1. B is subadditive over families. By (7) of the local factor budget note, B_P <= 8 calB(M). So
  M > 8 calB(M) + B_Lambda3(M) + B_Lambda4(M)
gives a choice avoiding P, Lambda3 and Lambda4 together. This extends criterion (8) to arities 3 and 4.
(c) Fix one role (vertex, near or far). If each label plays that role in at most D Lambda3 constraints, then B_Lambda3 <= 3D.
(d) (LLL form; Lemma 5 on file, recounted.) Let deg_k(z) be the number of k-label constraints at z. If M >= 2 and deg_2(z)/M + deg_3(z)/M^2 + deg_4(z)/M^3 <= 1/16 for every z, a good choice exists. For example M >= max(2, 48 Delta_2, sqrt(48 Delta_3), (48 Delta_4)^(1/3)) works, where Delta_k = max_z deg_k(z).

THEOREM B (dense barrier for the induced criterion; PROVED, and checked exactly). Let S = 2^e >= 8, M >= 1, and let a be odd with gcd(a,M) = 1 and a >= M((MK+1)^2 + 9)/4. Let m be the largest integer with ((m-1)MK + 1)^2 < 4((m-1)a/M - 2). Put i0 = (m-1)MK, j0 = i0 + (a-1)/2 and h = a + 1 + 2(m-1)MK (any larger h also works). Take 2m labels, p = 0..m-1:
  P_p = (i0 - pMK, j0 - pMK) at slot pa,  g_p = (i0 - pMK + 1, j0 - pMK) at slot pa + M,
with rank = floor(slot/M) and xi = slot mod M. Then:
 (i) ranks and coordinates are distinct. Every pair satisfies the dyadic locality of Lemma 0 and the Hilbert inequality (1), max(Delta_i^2, Delta_j^2) < 16 Delta_r. Every column is S times a slot.
 (ii) For every ordered p != q, take V = odd point of P_p, F = odd point of P_q and G = even point of g_p. This is a tilted cross-parity right angle with normal form lambda = q - p, (a, b, c) = (a, -M, 1), and its fourth corner lies in rows [1, h].
 (iii) In U = all 2m labels, these m(m-1) constraints have distinct label triples. Every label lies in at least m-1 of them, so min_z w_U(z) >= m-1 and the weighted density is 1.5(m-1). Moreover m - 1 >= 12(h-1)/(M^3 S^4) - 2 when a is taken as large as h allows.
CONSEQUENCE. Suppose an argument bounds B_Lambda3, the degeneracy or the per-label degree using only pairwise locality (Lemma 0 or (1)), column divisibility and the Theorem 1 arithmetic. Then that argument cannot beat about 12h/(M^3 S^4). The peeling criterion then needs M^4 S^4 >= 12(h-1)(1 - o(1)), and the LLL form needs about M^5 S^4 >= h. In width S M this is no better than the threshold theorem (M S^4 >= 16(h-1) at M = 1). Proposition 4 on file defeated only per-label bounds; this configuration also defeats induced averages, because it uses heavy near pairs (P_p, g_p) with codegree m-1 and every far pair in both directions. I do not claim it is a subconfiguration of the actual Hilbert order.

LEMMA H1 (interval hitting; PROVED). For any rank interval J of length L >= 1 and any integer i0, #{s in J : H(s)_1 = i0} <= 4 sqrt(L). The same holds for the second coordinate.
LEMMA H2 (gap-averaged anti-concentration; PROVED). Let T be a set of gaps inside an interval of length L. For every integer D, the sum over t in T of #{r : H(r+t)_1 - H(r)_1 = D} is at most 4 sqrt(L) q^2. So the average frequency over a window of gaps of length L ~ t is <= 4/sqrt(t).
LEMMA H3 (exact translation atoms; PROVED). Let q = 2^n. For every 0 <= k <= n-2, exactly half of the aligned blocks of length 4^(k+1) have an axis-preserving orientation. In each such block, every rank r of its second quarter satisfies H(r + 4^k) - H(r) = ±(2^k, 0), the same vector for the whole quarter. Hence at least q^2/8 ranks satisfy H(r+4^k)_1 - H(r)_1 = ±2^k and H(r+4^k)_2 = H(r)_2, and one sign occurs for at least q^2/16 ranks. The same holds with the coordinates swapped.
 COROLLARY. No hypothesis of the form "#{r : H(r+t)_1 - H(r)_1 = D} <= C q^2/sqrt(t) for all t, D" holds: at t = 4^k it fails by a factor >= 2^k/(16C). The census hubs (far labels shared by vertices at rank offset ±S^4/4 with Delta_i = ±K) are these atoms at k = 2e-1. There the f-match of a Lambda3 angle is automatic.
LEMMA H4 (residue equidistribution of near-pair rows; PROVED). For odd c >= 1 and d >= 1 with dc <= q^2/4, put Y2(r,d) = 2H(r+d)_2 + 1 - 2H(r)_1. Then #{r : c divides Y2(r,d)} <= 5q^2/c + 8q sqrt(dc).

PROPOSITION G (Gaussian form and codegrees; PROVED). Write vectors as x + iy and put z = a + iSb. A cross-parity label right angle is exactly F - V = lambda S z, G - V = i c z, and then F - G = z(lambda S - ic). Consequences:
 - codeg(f,g) <= 4(2M-1) max{tau(n)^2 : n <= 2 S^2 M^2 h^4} = M h^(o(1));
 - codeg(v,f) <= 2(2M-1)[1 + 16(8 sqrt(32h/(M^2 S^4) + 1) + 1)/(M S^4)], which is <= 4(2M-1) when h <= M^2 S^4 (M S^4/1300)^2;
 - codeg(v,g) <= 4M Lambda_max, with Lambda_max = 64(h-1)/(M S^4).
So, up to divisor factors, only the near pair (v,g) can carry many constraints. Theorem B uses exactly that.

PROPOSITION T (deep tiles; PROVED for the full-grid normal forms). Let a tile be a square [i0, i0+l) x [j0, j0+l) with |j0 - i0| <= l. Then Lambda3 and Lambda4(b) are empty in it when M S^4 >= 16(4l - 1), and Lambda4(c) is empty when sqrt(M) S^4 >= 128 sqrt(2)(4l - 1).

CONDITIONAL MEAN BOUND (computation, PROVED given HJ). Hypothesis HJ: for all odd c, b != 0, lambda >= 1, xi and dyadic A, the number of vertex labels v satisfying all of the following is at most C_J q^2 sqrt(M A/lambda)/h:
 - g = owner of slot sigma_v - bc has c dividing Y2 = Y(G) - Y(V);
 - a = Y2/c lies in [A, 2A) and gcd(a,b) = 1;
 - f = owner of slot sigma_v + lambda a has i_f - i_v = lambda K b.
Under HJ, the mean number of Lambda3 candidate constraints per label is <= C C_J M (log(64h/(M S^4)))^2/S^2. HJ gives only a mean, not the induced bound that Theorem A needs.

NOT PROVED: the target. No bound c0 + c1 (log h)^beta/S^gamma on B_Lambda3 or B_Lambda4 (or on the per-label maximum) at S >= 6272 or at the strides S_k. True growth: heuristically, and supported by the census at S = 2, 4, 8, the mean candidate degree at fixed S grows like A(S)(log(16h/(M S^4)) - c)^2, and the peeling degeneracy tracks about 0.6 times the mean once the mean is large. If that is right, no counting criterion gives bounded M at fixed sigma in H7. At S_k >= 6272 sigma0 with sigma0 = C log h, the heuristic predicts B_Lambda3 = O(C^-2), and Theorem A would then need only M = c0 + 2 for this part.

## Proofs

THEOREM A. (a) Peel: put U_1 = Z and choose z_1 in U_1 with w_{U_1}(z_1) <= M-1. Then put U_2 = U_1 \ {z_1}, and so on. Assign choices in reverse order z_n, ..., z_1. For any constraint E, let z_k be its label of smallest index. Then J_E lies inside U_k, and when z_k is assigned, every other label of J_E is already assigned. So E forbids at most m_E values of xi_{z_k}. The constraints checked at z_k forbid at most w_{U_k}(z_k) <= M-1 < M values in total, so an allowed value exists. Every constraint is checked at its first label, so none is violated. For the sufficient condition: the average of w_U over U is (1/|U|) times the sum over E inside U and z in J_E of m_E, which is <= B < M. The values are integers, so the minimum is <= M-1.
(b) For a difference pattern (delta's fixed), fixing all choices but one determines that one, so m_E = 1. Subadditivity: the max of a sum is at most the sum of the maxima. From (7), |E_P(U)| <= 4 sum over e in U of F^-_U(e;M), so the sum over E in E_P(U) of |J_E| m_E <= 8 |U| calB(M). Add the families.
(c) Charge each constraint to its label in the fixed role. Then |E(U)| <= D|U|, and the weighted sum is 3|E(U)|.
(d) A pattern constraint on k labels has at most M forbidden vectors: xi_v is free and the rest are determined. Each vector has probability M^-k, so mu_z <= deg_2/M + deg_3/M^2 + deg_4/M^3. Apply Lemma 5. Each term <= 1/48 gives a sum <= 1/16.

THEOREM B. Write n = q - p.
(i) Ranks: floor(pa/M) and floor(pa/M) + 1. Because a >= 3M, the P-ranks differ by at least 2 and the g-ranks interleave without collisions. The script checked this for every case. Put f(n) = (nMK + 1)^2 - 4(na/M - 2). It is a convex quadratic, f(1) < 0 by the lower bound on a, and f(m-1) < 0 by the choice of m. So f(n) < 0 for 1 <= n <= m-1.
 - (P_p,P_q) and (g_p,g_q): the rank distance is t >= |n|a/M - 1, and both coordinate differences are |n|MK. So D^2 < (|n|MK+1)^2 < 4(|n|a/M - 2) < 4t.
 - (P_p,g_p): t = 1 and D is 1 or 0.
 - (P_p,g_q), n != 0: t >= |n|a/M - 2, Delta_i = |nMK - 1| <= |n|MK + 1 and Delta_j = |n|MK. So D^2 < 4t again.
 D^2 < 4t implies Lemma 0: if |D| >= 2^mu with mu >= 1, then 4^mu <= D^2 < 4t, so t > 4^(mu-1). It also implies (1), since D^2 < 16t.
(ii) V = (S pa, 2(i0 - pMK) + 1), F = (S qa, 2(i0 - qMK) + 1) and G = (S(pa + M), 2(j0 - pMK) + 2). So F - V = n(Sa, -M S^2), using 2MK = M S^2, and G - V = (SM, 2(j0 - i0) + 1) = (SM, a). The dot product is n(S^2 M a - M S^2 a) = 0. All four components are nonzero, V and F are odd and G is even. The normal form has b = -M and c = 1, with gcd(a,M) = 1 and a, c odd. The fourth corner has row 2(i0 - qMK) + 1 + a, which lies between 1 and 2i0 + 1 + a = 2j0 + 2 <= h. All label rows lie in [1, h].
(iii) Each pair (p,q) gives the triple {P_p, P_q, g_p}, and p and q can be read back from it, so the triples are distinct. P_p is the vertex for m-1 values of q and the far end for m-1 values, and g_p is the near end m-1 times. The weighted sum is 3m(m-1) over 2m labels. Size of m: put n = m-1. f(n) < 0 holds when n M^2 K^2 + 2MK + 9 <= 4a/M, so m - 1 >= floor((4a - 2M^2 K - 9M)/(M^3 K^2)). Some a ≡ 1 (mod 2M) is odd, coprime to M, and at least (h-1)/(1 + 8/(M^2 K)) - 2M >= 0.8(h-1) - 2M, because K >= 32. Then (4a - ...)/(M^3 K^2) >= 12.8(h-1)/(M^3 S^4) - 0.1 - 8/(M^2 K^2), which gives the bound. The consequence follows from Theorem A: on U every w_U(z) >= m-1, so M >= m is needed. Every per-label degree is also >= m-1, so the LLL needs m-1 <= M^2/48.

LEMMA H1. Let 4^k be the least power of 4 that is >= L. J meets at most two aligned blocks of length 4^k (one if 4^k > q^2). Each block is a dyadic square of side 2^k (placement note, Section 1), which has at most 2^k cells with first coordinate i0. If k = 0, then L = 1 and the count is <= 1. If k >= 1, then 4^(k-1) < L, so 2^(k+1) < 4 sqrt(L).
LEMMA H2. Exchange the sums. For each r, the ranks r + t with t in T lie in an interval of length L. Apply H1 to that interval, then sum over the q^2 values of r.
LEMMA H3. By (2), the quarters of H_{2Q} are images of H_Q under maps with linear parts T (transpose), I, I and A: (x,y) -> (-y,-x). By induction, every aligned block of the core is the image of a standard curve under an isometry whose linear part lies in the Klein group {I, T, A, R180}, where R180 = TA. Call I and R180 axis-preserving (class P) and T and A axis-swapping (class Q). A child's linear part is the parent's times T, I, I, A, so every parent has exactly two class-P children and two class-Q children. So at every level below the top, exactly half the blocks are class P. In H_{2Q}, the second and third quarters are (x, y+Q) and (x+Q, y+Q) of the same list. So H_{2Q}(s + Q^2) - H_{2Q}(s) = (Q, 0) on the second quarter. In a class-P block of length 4^(k+1), with Q = 2^k, this vector becomes L(2^k, 0) = ±(2^k, 0). Count: (4^(n-k-1)/2) * 4^k = q^2/8 ranks. Pigeonhole gives one sign for at least q^2/16 of them. Corollary: H2 bounds the average over gaps by 4/2^k near t = 4^k, while H3 gives one gap with frequency >= 1/16. For the hubs: with k = 2e-1, 4^k = S^4/4 and 2^k = K, so lambda|b| = 1. The far end f = H(r_v + 4^k) has Delta_i = ±K = lambda K b exactly.
LEMMA H4. Let 4^k be the least power of 4 that is >= dc, so 2^k <= q. Count the r with r and r+d in the same aligned 4^k-block B. B has index (beta1, beta2) in [0, Q')^2 with Q' = q/2^k, corner (2^k beta1, 2^k beta2), linear part L_B and local position s. Then Y2 = 2^(k+1)(beta2 - beta1) + 1 + 2 phi_{L_B}(s), where phi depends only on (L_B, s). Since 2^(k+1) is invertible mod the odd c, c | Y2 is equivalent to beta2 - beta1 ≡ gamma(L_B, s) (mod c). For fixed (L, s), this has <= Q'(Q'/c + 1) solutions. Summing over the 4 linear parts and the 4^k values of s gives <= 4q^2/c + 4q 2^k. The r with r + d outside B number <= d per block, so <= dq^2/4^k <= q^2/c. With 2^k < 2 sqrt(dc), the total is <= 5q^2/c + 8q sqrt(dc).

PROPOSITION G. With z = a + iSb: lambda S z = lambda(Sa + i S^2 b), which is F - V, and icz = -cSb + iac, which is G - V. Subtracting gives F - G = z(lambda S - ic).
 - (f,g): fix the labels f and g and delta = xi_g - xi_f (2M-1 values). Then w = F - G is fixed, with N(w) <= (S M q^2)^2 + h^2 <= 2 S^2 M^2 h^4. Each V comes from a Gaussian divisor z of w, and then c = -Im(w/z) and V = G - icz. The number of divisors is <= sum over m dividing N(w) of r_2(m) <= 4 tau(N(w))^2.
 - (v,f): fix delta_f (2M-1 values). Then (lambda, a, b) is fixed. Locality gives |j_g - j_v| < 4 sqrt(|bc|/M + 1), so |ac - span_v| < tau0 = 8 sqrt(|bc|/M + 1) + 1, with span_v = 2(j_v - i_v) + 1. The odd c lie in an interval of length 2 tau0/|a|, so there are at most tau0/|a| + 1 of them. Use |a| > M S^4/16, b^2 <= 64|a|/(M S^4) and |c| <= h/|a|; these give |bc|/M < 32h/(M^2 S^4). For each c, the label g takes at most 2 values as xi_v varies, and delta_g is determined by r_g.
 - (v,g): fix xi_v (M values), the sign of lambda and |lambda| <= Lambda_max. Then f is determined, giving 4M Lambda_max.
PROPOSITION T. Cross-parity rows 2i+1 and 2j'+2 of tile labels differ by |2(j'-i) + 1| <= 2(|j0 - i0| + l - 1) + 1 <= 4l - 1. Theorem 1(iii) needs |a| <= |ac| = |Y2|, Theorem 2(b) needs |a| <= |c_row - b_row|, and Theorem 2(c) needs |Y| with Y odd.
CONDITIONAL MEAN. Sum the HJ bound over the parameters:
 - lambda <= 128A/(M S^4 b^2), so sum over lambda of lambda^(-1/2) <= 16 sqrt(2A/M)/(S^2|b|);
 - dyadic A <= h/c, so the sum of A/h is <= 2/c;
 - odd c <= 16h/(M S^4), and 1 <= |b| <= 8 sqrt(2h/(M S^4)).
This gives <= 32 sqrt(2) C_J q^2 (sum over c of 1/c)(sum over b of 1/|b|)/S^2 per (xi, parity). Multiply by 2M and by 3 roles, then divide by the number of labels, which is about q^2.

## External results used

- Asymmetric Lovasz local lemma, used only through Lemma 5 of hilbert_angles_mixed_thresholds.md. If each event A has x_A in [0,1) with P(A) <= x_A times the product of (1 - x_B) over its dependency neighbours, then with positive probability no event occurs. Standard; not looked up.
- r_2(m) <= 4 tau(m), the number of representations of m as an ordered sum of two squares, used to count Gaussian integers of norm m. Standard.
- The divisor bound tau(n) = n^(O(1/log log n)), used only to read the (f,g) codegree as M h^(o(1)). Standard.
- Internal, audited: the recursion (2) and inequality (1) of continuation_hilbert_placement.md; (7) and (8) of continuation_hilbert_local_factor_budget.md.
- Internal, not audited: Lemma 0, Theorems 1 and 2 and Lemma 5 of hilbert_angles_mixed_thresholds.md. Lemma 0 and Theorem 1 were re-derived in hilbert_round1_synthesis.md U4. I used the Theorem 1 normal form and re-checked it on the Theorem B instances.
- No web sources.

## Checks

All scripts are in the script folder scripts_hb2_lambda/. I ran them one at a time with py, each under 60 s. angles.py is copied unchanged from scripts_hb1_angles_mixed. The repository was not touched.

(1) barrier2.py checks Theorem B in exact integer arithmetic. For (S, M, a) = (8,1,200001), (8,2,200001), (8,3,200003) and (16,1,2000001), the values of m are 782, 98, 29 and 489, against predictions 16a/(M^3 S^4) of 781.3, 97.7, 28.9 and 488.3. All ranks and coordinates are distinct. Every pair satisfies Lemma 0 and (1). All m(m-1) claimed triples are tilted right angles with the fourth corner in the strip (610742, 9506, 812 and 238632). The minimum degree is m-1, and the weighted density is 1.5(m-1).

(2) hlemmas.py checks the lemmas on q = 256.
 - H1: the worst counts over L = 1..5000 are 1, 3, 6, 16, 32, 64 and 96, against 4 sqrt(L) = 4, 6.9, 12.6, 28.3, 56.6, 126.5 and 282.8.
 - H3: the fraction of r with H(r+4^k) - H(r) = ±(2^k, 0) is 0.5, 0.3, 0.217, 0.176, 0.154, 0.153 and 0.138 for k = 0..6. It is always >= 1/8, while 4/2^k is 0.0625 at k = 6.
 - H4: the frequency of c | Y2 is within 3% of 1/c for d = 1, 4, 30 and c = 3..81, and always below 5/c + 8 sqrt(dc)/q.

(3) degen.py computes the Lambda3 candidate constraints over all choice vectors, enumerated as in cand.py, with exact peeling degeneracy d*. Theorem A's greedy needs M >= d* + 1.

| S | h | M | mean deg | max deg | d* |
|---:|---:|---:|---:|---:|---:|
| 8 | 512 | 1 | 0.004 | 2 | 1 |
| 8 | 1024 | 1 | 0.048 | 5 | 1 |
| 8 | 1024 | 2 | 0.010 | 5 | 2 |
| 8 | 2048 | 1 | 0.153 | 8 | 3 |
| 8 | 2048 | 2 | 0.100 | 10 | 3 |
| 8 | 2048 | 3 | 0.033 | 8 | 2 (greedy succeeds at M = 3) |
| 4 | 256 | 1 | 1.16 | 11 | 3 |
| 4 | 512 | 1 | 2.17 | 17 | 6 |
| 4 | 256 | 2 | 1.09 | 13 | 4 |
| 4 | 512 | 2 | 2.65 | 23 | 5 |
| 2 | 64 | 1 | 10.6 | 30 | 6 |
| 2 | 128 | 1 | 16.7 | 40 | 9 |
| 2 | 256 | 1 | 24.1 | 58 | 14 |
| 2 | 128 | 2 | 26.0 | 65 | 16 |
| 2 | 256 | 2 | 37.5 | 88 | 23 |
| 2 | 128 | 4 | 22.5 | 56 | 16 |

At S = 2 and M = 1, sqrt(mean) is linear in ln h (3.26, 4.09, 4.91, slope 1.19). So mean = 1.42(ln h - 1.42)^2, a log^2 law with an offset. d*/mean is 0.57 to 0.61 in the dense cases. The candidate counts do not fall as M grows. The S-dependence is weaker than S^-2 in this range. The run at S = 4, h = 1024 timed out at 60 s and is omitted.

By hand I checked the Theorem B algebra, the convexity step and the size of m; the Klein-group child count in H3; the block count in H4; and the Gaussian identity and the three codegree bounds.

## Gaps

- The target is not proved. I have no bound c0 + c1 (log h)^beta/S^gamma on the induced density B_Lambda3 or B_Lambda4, on the degeneracy, or on the per-label maximum, at S >= 6272 or at the strides S_k. Theorem B shows that no proof from pairwise locality, divisibility and the normal forms can give one. Some property of the actual Hilbert order is needed.
- Hypothesis HJ (joint equidistribution of the near-pair divisibility and the far-pair exact hit) is unproved. Lemmas H2 and H4 control each condition alone. The coupling is the obstacle: a = Y2/c is tied to the vertex's span, so for a fixed vertex only the AP of gaps lambda*a/M is free. H3 shows that pointwise versions fail.
- Even HJ gives only a mean. Criterion (8) and Theorem A need B, a maximum over induced subsets. That needs a Hall-type or per-role maximum version, which I cannot state as a frequency.
- The claimed true growth, a mean candidate degree of about A(S) log^2 h at fixed S, is heuristic plus census data at S = 2, 4, 8 and h <= 2048. No rigorous lower bound shows growth. The translation atoms (H3) contribute only O(M/S^4) to the mean, so they cannot provide one.
- Theorem B is not claimed to embed in the actual Hilbert order, and I did not test whether the actual order contains dense near-pair stars.
- Lambda4: Theorem A covers it with m_E = 1, and Proposition T covers deep tiles. I did not construct a Lambda4 analogue of Theorem B or derive its heuristic incidence.
- Everything is written for the full-grid placement with S = 2^e. The H7 versions (S = 6272 sigma, row step 28, G = 2^(2v2(S)) 7^(2v7(S)) dividing Y1, locality constant 16*28^2) are analogous but not written out. Proposition T in H7 tiles would use the unaudited Lemma S3(c) thresholds.
- The census at S = 2 and 4 counts only cross-parity angles; same-parity angles also exist there. At S = 8 the census does not reach the asymptotic regime (M S^4/(16h) >= 0.125). Nothing here is audited.

## Missing estimate

The target B_Lambda3 <= c0 + c1 (log h)^2/S^2 (with Lambda4 likewise) needs an induced, Hall-type bound that uses the actual Hilbert order beyond pairwise locality, since Theorem B rules out locality-only proofs. The cleanest sufficient statement is a per-role maximum. For every vertex label v, the number of pairs (x2, lambda) satisfying all of the following must be <= c0 + c1 (log h)^2/S^2:
 - g = owner of slot sigma_v + x2 gives (a, b, c) from G - V;
 - lambda <= 64|a|/(M S^4 b^2);
 - the label at slot sigma_v + lambda*a has i-coordinate exactly i_v + lambda*K*b.
This is an anti-concentration statement for the Hilbert curve along the rank progressions r_v + floor((lambda*a + xi)/M), whose step a is tied to v's own span. It must hold uniformly in v.
 - Lemma H3 shows it must tolerate atoms at gaps near powers of 4.
 - Lemma H2 shows it holds on average over gap windows.
 - Lemma H4 shows the near-pair divisibility has frequency about 1/c.
The missing piece is the joint version (HJ, for the mean) and then its uniform-in-v strengthening (for B). With uniform strides at fixed sigma (H7), the data and heuristic say even the mean grows like log^2 h, so bounded M by counting is not expected there. At S_k ~ sigma0 log h it would give bounded M.

## Next steps

- Attack HJ with a two-scale block decomposition. At scale 4^k ~ lambda*a/M, a vertex's a depends on its block corner's span, which is equidistributed mod c and along APs by H4's argument. Reduce the far exact hit to the Hilbert curve along an AP of step about 2^(k+1) lambda/(cM) inside 4^k-blocks. That is a 4-automatic question, and it may be tractable through the orientation automaton.
- Test the uniform-in-v statement directly on the Hilbert curve alone, with no rectangles: compute max over v and (a,b) of #{lambda : i(H(r_v + lambda a)) = i_v + lambda K b} for q up to 2^12. This shows whether per-vertex counts grow like log or like a power.
- Use Proposition G structurally: only near pairs (v,g) can be heavy. Convert near pairs with codegree above kappa into P-type pair constraints. The remaining Lambda3 hypergraph has all codegrees at most max(kappa, M h^(o(1))). Then see whether the LLL form (M about sqrt(Delta_3)) or a nibble on this nearly linear hypergraph beats peeling.
- Build the Lambda4(b) and (c) analogues of Theorem B, and a faster enumerator (numba or C), to push the S = 4 and 8 census to h = 8192 and test whether d* stays near 0.6 times the mean.
- Write out the H7 versions (row step 28, G-divisibility) of Theorems B, H4 and Proposition T, and pass Theorems A, B and H1-H4 to an auditor. All of them are short.

