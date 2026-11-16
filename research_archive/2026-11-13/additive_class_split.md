# An additive class split against the ratio graphs

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: on every light diagonal, at most 10B classes independent in G_T, R_IV and the homogeneous R_FF, after removing O(h^2/B) labels. R_IV is a sub-family of the same nodal cubic as R_FF. Removal by back-degree cannot reach O(h^(2-delta)) (heuristic). Not audited yet.

# Result

## Status

partial

## Summary

Additive class split, proved: on every light diagonal, at most 10B classes independent in G_T, R_IV and the homogeneous R_FF, after removing O(h^2/B) labels. This needs no bound on chi(R_IV) or chi(R_FF). It reaches the polylog-relocation target. It does not reach O(h^(2-delta)), and a smooth-values heuristic shows that no removal-by-back-degree method can.

## Statements

Setting. L** of full_layout_junctions.md, with SAW, or SAW* where noted. Lambda = log h, ell = loglog h, B = ceil(Lambda^1.4967), kappa_T = k_T^(2) = |D_T|. On a light diagonal T and a type tau, I(T,tau) is the set of non-exceptional slots i, in increasing order. Each label at slot i has:
- u(i) = (2i+1-r0)/2, which is odd;
- for each SAW (or SAW*) filler row Y_o, o = 0..3, the odd depth delta_o(i) = Y_o - (2i+1) and the even depth delta'_o(i) = Y_o - (2i+1+T).
The forms U(a,b) = (a-4b)(a^2+b^2) and V(a,b) = a^3 - 4a^2 b - 3ab^2 + 4b^3 are as in saw_residual_families (iii-b). Write U' = U/gcd(U,V) and V' = V/gcd(U,V).

LEMMA 1 (explicit R_FF; proved from the cubic of (iii-b)). Take a homogeneous two-label, two-filler quadruple inside a class: side {L1,F1}, diagonal {L2,F2}, F1 and F2 in one row Y, L2 - L1 = (4t, 2t) with t != 0, and depths Y_k = Y - y(L_k) > 0. Then Y2/Y1 = V(a,b)/U(a,b) for coprime integers (a,b) with b > 0 and a/b = P/(2t), where P = X1 - X2. Hence Y1 = mu|U'| and Y2 = mu|V'| for some integer mu >= 1. The thick case d < 0 of (iii-b) is exactly t < 0 (L2 deeper, |U'| < |V'|). The d > 0 case has |t| <= 86, by the bound 2d <= H0 of (iii-b). This holds for Fo/Fo and Fe/Fe alike.

LEMMA 2 (content; proved). For coprime (a,b), gcd(U,V) divides 40.

LEMMA 3 (unification; proved, exact identity). Put (a,b) = (4be - 2al, be). Then U = -2 al F and V = -2C, where F and C are the forms of R_IV in ratio_graph_r_iv.md. So rho_lambda = p/q = V/U. Every R_IV generator is a point of the same nodal cubic, with m = a/b in (2,4), a = 2 mod 4, b odd and v2(a-2b) >= 3. The sea row plays the role of the filler row. Example: the first k=4 edge (349,749) is (al,be) = (1,5), which maps to (a,b) = (18,5).

LEMMA 4 (first moments; proved).
(a) S_IV := sum_lambda 1/p_lambda <= (5/4)(pi^2/8 - 1 - 1/9) < 0.154. Numerically it is about 0.0043. Also sum over odd u <= U of b_IV(u) <= (U/2) S_IV + (5U)^(2/3)/32, where b_IV(u) := #{lambda : p_lambda | u}.
(b) S_U := sum over coprime (a,b) with b > 0 and U != 0 of 1/|U(a,b)| <= 2(34 zeta(3) + pi zeta(2)) < 92.1. For every H, sum over delta = 1..H of b_U(delta) <= 40 H S_U, where b_U(delta) := #{(a,b) : |U'(a,b)| divides delta}.

THEOREM 5 (additive class split; proved, modulo the cited unaudited inputs). Fix an integer D >= 1. For every light (T,tau), let E_{T,tau} be the set of slots i with b_IV(u(i)) >= D, or with b_U(delta) >= D for one of the eight depths delta in {delta_o(i), delta'_o(i)} that is >= 1. Colour I(T,tau) \ E greedily in increasing i, against the union of four graphs:
- G_T;
- R_IV (pairs {q m, p m} of u-values);
- R_FF^- (pairs with 0 < delta(i) < delta(i') and delta(i')/delta(i) = V/U for some shape, over all eight depth maps);
- R_FF^+ (all pairs with 0 < |i - i'| <= 86).
Then:
(i) the number of classes is at most kappa_T + 9D - 3 <= B + 9D - 4. For D = B this is at most 10B;
(ii) every class is independent in G_T, so Proposition R and J4 apply. Every class is also free of family IV and of every homogeneous Fo/Fo and Fe/Fe quadruple, d < 0 and d > 0;
(iii) sum over all light (T,tau) of |E_{T,tau}| <= C_E h^2/D + O(h^(5/3)/D), with C_E <= S_IV/2 + 20160 S_U < 1.9 * 10^6. This constant is crude. Without congruences, the measured mean back-degree of the superset graphs is about 4.
(iv) Structure of E: whether a label is in E is decided by its odd row alone (u and the odd depths), or by its even row together with i mod 16 (the even depths). E is therefore contained in O(1) families of the form 'all light labels through a set of O(h/D) rows'.

COROLLARY 6 (CONDITIONAL). Replace (P3) of L** by Theorem 5 with D = B, and put E into the relocation set (P5). Use SAW*, so that Feo is empty. Then (O1) is no longer needed: the psi split and the factor X disappear. The region width becomes < 409600 B h^2 + O(h). Assume (O2), (O3) without (iii), and (U1) to (U3), and assume:
(Rel_rho) the label set E can be relocated in width C|E| Lambda^rho ell^C + C h^2 ell.
Then M <= C h^2 Lambda^(max(1.4967, rho - 1.4967)) ell^C1. This beats T1 for rho < 3.49 and keeps the exponent 1.4967 for rho <= 2.99. In general the trade-off is classes B + 9D against removal h^2/D. The paper's Proposition partial alone (cost c0 n tau*(h)^2) does NOT suffice: it gives h^2 tau*^2/B.

PROPOSITION 7 (obstruction for removal by back-degree; HEURISTIC, rigorous under (SV_theta)). Hypothesis (SV_theta): >> Z^2 pairs (al,be) <= Z of the R_IV lattice have C(al,be) Z^theta-friable. Under (SV_theta) with theta < 2/A, #{odd u <= U : b_IV(u) >= (log U)^A} >= U exp(-O((log U)^(A theta/2))). Under the Dickman-rate heuristic this holds for every theta > 0, that is, U exp(-(log U)^eps) for every eps. So with D polylogarithmic, the set {b >= D} has h^(2-o(1)) labels, far more than h^2 Lambda^O(1)/tau*(h)^2. Removal by back-degree therefore cannot reach O(h^(2-delta)), or the tau*^2 relocation, at any polylog colour cost. The same holds for R_FF, which contains the R_IV ratios (Lemma 3).

PROPOSITION 8 (reduction for the tau*^2 regime; proved implication). R_cub^(<=Y) is the ratio graph on the positive integers with edges {mu|U'|, mu|V'|} over the shapes with |U'| <= Y. It contains every R_IV edge with q_lambda <= Y. Suppose chi(R_cub^(<=Y)) <= X. Take the product colouring (psi_0(u), psi_1(delta_1), ..., psi_8(delta_8), greedy colour of G_T, the large shapes and R_FF^+). This gives at most X^9 (B + 9D) classes after removing O(h^2 Y^(-1/3)/D) labels. With Y = tau*(h)^6 the paper's Proposition partial then suffices. The near goal needs X <= (log Y)^((0.5-c)/9).

PROPOSITION 9 (inhomogeneous two-filler-row family; closed form proved, count open). With w = delta_F - 2t, where delta_F = y_F2 - y_F1 is the filler-row gap, the cubic of (iii-b) is exactly (P - 8t)(P^2 + w^2) = 8t Y1 (P + 2w). Hence s := P + 2w divides N(t) = 10(delta_F - 2t)^2(delta_F + 2t), and t divides G(s) = (s - 2 delta_F)((s - 2 delta_F)^2 + delta_F^2). For delta_F = 0 this is the scaling-invariant thick family. For delta_F != 0, the count per class line and filler-row pair (superset, no congruences) is 282, 603 and 941 at h = 1000, 3000 and 8000, which suggests about h^0.5. Compare the homogeneous count of about 1.45h. No proof.

## Proofs

0. INPUTS. I use these inputs without re-auditing them:
- sea_census_rigid B4: two odd label points of one class form a fatal M2c iff their u-values are an R_IV edge. Unaudited; I use only the 'only if' direction.
- saw_residual_families (iii-b): the cubic P^3 - 8tP^2 + ((Y1-Y2)^2 - 8tY1)P - 8t(Y2^2 - Y1^2) = 0 for side {L1,F1} and diagonal {L2,F2}; the fact that only these two-label shapes occur inside a class; and the d > 0 bound 2d <= H0 <= 87. Unaudited. I re-derived the factorisation below.
- The audited definition k_T = |D_T|, with G_T the distance graph with distance set D_T.
- J4 (classes of one diagonal never meet; unaudited).
Every graph below is a SUPERSET of the fatal pairs. Colouring a superset properly is enough.

1. LEMMA 1. Put Y2 = Y1 + w, with w = (y_F2 - y_L2) - (y_F1 - y_L1) = delta_F - 2t. Then (Y1 - Y2)^2 = w^2 and Y2^2 - Y1^2 = w(2Y1 + w), and the cubic becomes
 P^3 - 8tP^2 + w^2 P - 8t w^2 - 8tY1(P + 2w) = (P - 8t)(P^2 + w^2) - 8tY1(P + 2w).
This identity was also checked by script on random integers, and it gives Proposition 9.
In the homogeneous case delta_F = 0 we have w = -2t. If P = 4t, the left side is -80t^3 != 0, so P != 4t. Put m = P/(2t), which is rational because t != 0. Then
 Y1 = t(m-4)(m^2+1)/(2(m-2)) and Y2 = Y1 - 2t = t(m^3 - 4m^2 - 3m + 4)/(2(m-2)).
So Y2/Y1 = V(m,1)/U(m,1) = V(a,b)/U(a,b) with m = a/b, gcd(a,b) = 1 and b > 0. U(a,b) != 0, because Y1 > 0. From Y1 V' = Y2 U' and gcd(U',V') = 1, we get |U'| | Y1, so Y1 = mu|U'| and Y2 = mu|V'|.
Signs: d < 0 means t < 0, so Y2 > Y1. For a given shape (a,b), the shallower label L1 determines the deeper label L2 uniquely.
In the units of the note, P = 4p, t = 2d and Y_k = 4u, 4v. This recovers F(p,u,v) and the note's parametrisation; I checked by hand that F(md, U, V) = 0.

2. LEMMA 2. gcd(U,V) = gcd(U, U - V), and U - V = 4b^2(a - 2b). Let l be an odd prime dividing both.
- If l | b, then U = a^3 != 0 mod l. Contradiction.
- So l | a - 2b. Then U = (-2b)(5b^2) = -10b^3 mod l, which forces l = 5.
- With a = 2b mod 5, a - 4b is a 5-adic unit. If v5(a-2b) >= 2, then a^2 + b^2 = 5b^2 mod 25 has v5 exactly 1. So min(v5(U), v5(a-2b)) <= 1.
2-part:
- b even: U is odd.
- a and b odd: v2(U) = 1.
- a even and b odd: if v2(a) = 1, then v2(U) = 1; if v2(a) >= 2, then v2(4b^2(a-2b)) = 3.
So gcd(U,V) | 8 * 5 = 40. (rff_shapes.py: every gcd over |a| <= 2400 and b <= 400 lies in {1,2,4,5,8,10,20,40}.)

3. LEMMA 3. Expand with a = 4be - 2al and b = be. Then a - 4b = -2al and a^2 + b^2 = 4(al - 2be)^2 + be^2 = F, so U = -2al F. Expanding V term by term gives -8al^3 + 32al^2 be - 26 al be^2 - 8be^3 = -2C. The condition 0 < al < be is equivalent to 2 < a/b < 4. unify.py checked the identity and V/U = p/q on 16182 generators.

4. LEMMA 4.
(a) Sea_census B4 gives the form of p and the bound on g:
- C(al,be) = al F + 4(be - al)be^2 >= al be^2 + 4(be - al)be^2 = be^2(4be - 3al) > be^3, because F >= be^2;
- g | gcd(F, be - al), and F = 5be^2 mod (be - al), so g | 5. Hence p_lambda >= be^3/5.
- For each odd be >= 5 there are at most (be-1)/4 admissible al, since al = be mod 4 and al < be.
So S_IV <= sum over odd be >= 5 of (5/4)/be^2 = (5/4)(pi^2/8 - 1 - 1/9).
The number of odd multiples of p up to U is at most U/(2p) + 1/2. Also #{lambda : p_lambda <= U} <= (5U)^(2/3)/16. Summing over lambda gives the bound.
(b) Substitute k = a - 4b != 0, a bijection with b fixed. Then |U| = |k|(17(b + 4k/17)^2 + k^2/17). A sum over unit-spaced points of a unimodal function is at most 2 max + integral, so sum over b of 1/(17y_b^2 + k^2/17) <= 34/k^2 + pi/|k|. Hence S_U <= sum over k != 0 of (34/|k|^3 + pi/k^2) = 2(34 zeta(3) + pi zeta(2)).
Next, #{delta <= H : |U'| | delta} <= H/|U'| <= 40H/|U| by Lemma 2. Sum over shapes.
The same computation gives the tail sum over |U| > W of 1/|U| << W^(-1/3) (split at |k| = (17W)^(1/3)). Proposition 8 uses this.

5. THEOREM 5.
(i) Greedy colouring in a fixed linear order uses at most max(back-degree) + 1 colours, and back-degrees of a union in one order add. In the order of increasing i:
- G_T: the earlier neighbours of i are i - d for d in D_T, so there are at most k_T = kappa_T <= B - 1.
- R_IV: u(i) increases with i. An edge {q m, p m} has q < p, so its later end is p m. The earlier neighbours of u are u q/p over the lambda with p_lambda | u, so there are at most b_IV(u) <= D - 1 off E.
- R_FF^-, for each of the eight depth maps: depth decreases as i increases, so the later end of a pair is the shallower label L1, at depth mu|U'|. Each shape with |U'| | delta gives at most one earlier neighbour, so there are at most b_U(delta) <= D - 1 off E. Eight maps give 8(D-1).
- R_FF^+: a class lies in one residue class mod 16. So at most floor(86/16) = 5 earlier labels lie within slot distance 86.
The total is kappa_T + 9(D-1) + 5, so at most kappa_T + 9D - 3 colours are used.
(ii) Each colour class is independent in the union, and so in G_T, which is hereditary. By J4, classes of one diagonal never meet, so the only family IV and Fo/Fo/Fe/Fe quadruples that matter lie inside one class. By B4 and Lemma 1, each of them is an edge of the union.
(iii) Markov: |E_{T,tau}| <= (1/D) sum over i in I(T,tau) of [b_IV(u(i)) + sum over the eight maps of b_U(delta(i))]. Fix T and sum over the types.
- Each odd u arises from at most two slots, one per value of r0. By Lemma 4(a), the R_IV part is <= (h/2) S_IV + O(h^(2/3)).
- For one depth map, delta(i) = Y_o(i mod 32) - 2i - 1 (- T). Y_o takes values in a window of width 63, since T* is in [h-63, h], so the map i -> delta(i) is at most 63-to-1. By Lemma 4(b), each map contributes <= 63 * 40 h S_U.
Summing over at most h light diagonals gives (iii).
(iv) b_IV(u(i)) depends only on y = 2i+1, because r0 depends on i mod 16 and so on y. delta_o depends on y, and in SAW* also on T mod 4. delta'_o = Y_o(i mod 16) - (2j+2) depends on the even row and on i mod 16.

6. COROLLARY 6. J4's width count: at most 2 diagonals per residue mod 2^nu and at most 10B classes per (T, type) give m_c < 40KB and width < 3200 B h^2 per type, hence < 409600 B h^2 + O(h) over 128 types. Everything else is Theorem J6's assembly with X = 1, plus the relocation term. With |E| <= C_E h^2/B, (Rel_rho) costs C h^2 Lambda^(rho - 1.4967) ell^C. Under the paper's Proposition partial the cost is instead c0 C_E h^2 tau*(h)^2/B, and tau*(h)^2 = exp((4 ln 2 + o(1)) ln h/lnln h) is larger than any power of Lambda.

7. PROPOSITION 7. Take Z with c(theta) Z^2 >= (log U)^A, and let Lambda_0 be the corresponding set of lambda with Z^theta-friable p_lambda. Since p_lambda <= 37 Z^3, the lcm N of these p_lambda satisfies log N <= pi(Z^theta) log(37 Z^3) = O(Z^theta) = O((log U)^(A theta/2)). Every odd multiple u = N m <= U has b_IV(u) >= |Lambda_0| >= (log U)^A, and there are at least U/(2N) - 1 of them. If A theta/2 < 1, then N = exp(o(log U/loglog U)), which is >> U/tau*(U)^2. For the record, the hypercube {N prod_{lambda in S} rho_lambda : S subset of Lambda_0} also shows that the degeneracy of R_IV on [1,U] is unbounded. Its chromatic number there is 2, so this is a failure of the degeneracy method, not a lower bound on chi.

8. PROPOSITION 8. An edge of a small shape gets distinct psi_j colours. Any other edge (G_T, the large shapes, R_FF^+) gets distinct greedy colours by section 5. The removal applies Markov to the large shapes only: S_IV^(>Y) <= 5/(8(Y-1)) and S_U^(>Y) << Y^(-1/3), so the removal is O(h^2 Y^(-1/3)/D). With Y = tau*^6, c0 tau*^2 * h^2 Y^(-1/3)/D = O(h^2/D).

9. PROPOSITION 9. The identity is in section 1. Reduce mod s: P = -2w gives (-2w - 8t) 5w^2, and w + 4t = delta_F + 2t. Reduce mod t: P = s - 2 delta_F and w = delta_F. The counts are from inhom.py, which enumerates the divisors s of N(t) for |t| <= h/2 and keeps the solutions with 1 <= Y1, Y2 <= h.

## External results used

- None beyond standard facts: zeta(2) = pi^2/6, zeta(3) < 1.2021, and the sum over odd n >= 5 of 1/n^2 = pi^2/8 - 1 - 1/9. Proposition 7 refers only in a general way to friable-value results for binary cubic forms (Balog-Blomer-Dartyge-Tenenbaum type). No exponent from them is used, and that proposition is labelled heuristic for this reason.
- Repository notes used as inputs (unaudited unless marked): ratio_graph_r_iv.md (definitions, Corollary 3), sea_census_rigid.md B4, saw_residual_families.md (iii-a), (iii-b) and the definition of SAW*, heavy_light_split.md Theorem 3 and Proposition R (audited), stride_menu.md k_T = |D_T| (audited), full_layout_junctions.md (P3) to (P7), J4 and J6, and t1_cost_decomposition.md Theorem E (for the comparison only).

## Checks

Each script ran with py in under 5 s, one at a time, all in the script folder. The repository was only read.
(1) riv_backdeg.py, U = 5e6. 4312 lambdas with v2(be-al) >= 2. The smallest edge is (349,749), which matches B4. p >= be^3/5 holds on every lambda. Mean b_IV over odd u is 0.00413, equal to the partial S_IV = 0.00425 as predicted. The maximum b_IV is 2 (at u = 409703). #{b >= 2} = 14 and #{b >= 3} = 0. So for h <= 10^7, R_IV costs at most 2 extra classes and no removal.
(2) rff_shapes.py, |a| <= 2400, b <= 400. Every gcd(U,V) divides 40. F(md, U, V) = 0 holds on every shape. The partial S_U is 1.26, well inside the proved bound. The smallest d<0 shapes are 5:7 (T2, m = 3), 13:31, 53:101 (the note's shape, (a,b) = (7,2)), ... and 109:181 = (10,3), which is the k = 3 R_IV generator, as Lemma 3 predicts. Depth back-degree for delta <= 1e6: mean 0.50, max 14.
(3) unify.py: U = -2 al F, V = -2C and V/U = p/q on 16182 generators. (349,749) comes from (a,b) = (18,5).
(4) combined.py: the total superset back-degree (R_IV + 8 R_FF maps, no congruences) on a sample diagonal has mean 3.94 and max 15 (h = 200001, T = 1001), and mean 4.00 and max 20 (h = 1000001, T = 3). So Theorem 5 with about 25 extra classes needs no removal at any computable h.
(5) inhom.py: the closed form (P - 8t)(P^2 + w^2) = 8t Y1 (P + 2w) matches the original cubic on 2000 random cases. Solution counts per class line and filler-row pair: delta_F = 0 gives 1338, 4222 and 11606 at h = 1000, 3000 and 8000 (linear). delta_F = 16 gives 331, 603 and 941 (about h^0.5). The values at 3000 for +-8, +-16 and +-24 are 480 to 676.
These are sanity checks. The statements rest on the proofs.

## Gaps

- Nothing here has had a second reader. Lemmas 1 to 4 and Theorem 5 are short and elementary, and a check by hand is owed.
- Theorem 5 rests on unaudited inputs: the B4 characterisation of family IV (only the direction 'fatal implies R_IV edge' is used), the (iii-b) cubic and its d > 0 bound 2d <= H0, and J4. The Lemma 1 factorisation was re-derived here from the (iii-b) cubic, not from Lemma mixedeq directly.
- Corollary 6 is conditional on (Rel_rho), a relocation of the specific set E (O(1) families of 'all light labels through O(h/D) rows', about 2*10^6 h^2/B labels) at Lambda^rho ell^C per label with rho < 3.49. No proved relocation does this: the paper's Proposition partial costs tau*(h)^2 per label, which is too much. Theorem E covers only whole diagonals, and E is made of whole rows, which is the T25-star situation, where geometric factors sit on a constant row.
- The O(h^(2-delta)) target is not met. Proposition 7 shows that removal by back-degree cannot meet it, but only heuristically: it needs friable values of the cubic form C at the rate (SV_theta) with theta < 1.336. I did not check which friability exponent is proved for binary cubic forms, so Proposition 7 is labelled heuristic.
- Proposition 8 needs chi(R_cub^(<=Y)) <= (log Y)^0.055 at Y = tau*(h)^6. That is open, and it is essentially as hard as chi(R_IV) < infinity. The product over nine row-relative graphs (the sea row and 4 filler rows x 2 parities) is the cost driver.
- Inhomogeneous two-label quadruples (fillers in two different rows, delta_F in {+-8, +-16, +-24}) are not covered by Theorem 5. Proposition 9 gives the exact closed form and two necessary divisibilities, s | N(t) and t | G(s). The numerics suggest about h^0.5 quadruples per class (harmless), but there is no proof. The crude bound sum_t tau(N(t)) gives only h polylog per class.
- Cross-block two-label quadruples ((iv) of saw_residual_families) are not addressed.
- Feo in SAW is not absorbed. Its graph F_T has degree up to divisor counts of f'(20f' - T), and the measured mean grows (0.0138 to 0.127 from h = 401 to 20481), so the Markov removal would exceed the 0.51 target. Corollary 6 therefore assumes SAW*, for which the full lcd census was never rerun (unaudited carry-over claim of saw_residual_families).
- Constants are crude: C_E < 1.9e6 from the 63-to-1 depth map and the 40 x 92.1 shape sum. The measured superset mean back-degree is about 4.

## Missing estimate

For the near goal through Corollary 6, one of these is needed.
(A) (Rel_rho) for the row-structured set E: relocate the light labels that meet a set of O(h/B) rows (odd rows, and even rows paired with i mod 16) at cost Lambda^rho ell^C per label, with rho < 3.49, plus O(h^2 ell). A weighted version of Theorem E for row stars would do. The obstacle is the geometric factor that sits on the constant row of a star.
(B) Without new relocation: chi(R_cub^(<=Y)) <= (log Y)^0.055 at Y = tau*(h)^6, where R_cub is the single nodal-cubic ratio graph {mu|U'|, mu|V'|}, which contains R_IV (Lemma 3). Then the paper's Proposition partial suffices (Proposition 8).
The O(h^(2-delta)) version cannot come from removal by back-degree (Proposition 7, heuristic). It needs a colouring that uses colour repetition among back-neighbours, such as real potentials psi on the primes with |psi(V/U)| in [1, M] over all small shapes.
Also open: an O(h^(1-delta)) count per class for the inhomogeneous family, that is, #{(t,s) : |t| <= h, s | 10(delta_F - 2t)^2(delta_F + 2t), t | (s - 2delta_F)((s - 2delta_F)^2 + delta_F^2), 1 <= Y1, Y2 <= h}.

## Next steps

- Audit Lemmas 1 to 4 and Theorem 5 by hand (about a page). If they pass, add ledger rows: 'R_FF homogeneous = ratio graph V/U of the nodal cubic, content | 40'; 'R_IV is the sub-family (a,b) = (4be - 2al, be) of the same cubic'; 'additive class split: kappa_T + 9D - 3 classes after removing O(h^2/D) labels'.
- Replace (P3) of full_layout_junctions.md by Theorem 5, and drop (O1) from Theorem J6 in favour of the relocation hypothesis (Rel_rho). Switch L** to SAW* so that Feo is empty, and rerun the lcd census on SAW* at h of about 400 to 650.
- Check whether the parallel route's polylog relocation accepts row-structured sets (all light labels through O(h/B) rows). If it needs small row degree, test whether Theorem E's sums (E2) to (E5) survive for row stars, with the geometric factor on the varying endpoint only.
- Try to prove Proposition 9's count. The two divisibilities s | N(t) and t | G(s) give, through H = N(t) - G(s) - 10 delta_F^3, the relation lcm(t,s) | H(t,s). Bound the solutions by size regimes (|s| << |t|, |s| ~ |t|, |s| >> |t|) together with this relation.
- For route (B), run the LP potential (lp.py) on the unified graph R_cub, restricted to the shapes of height <= Y, and see how M(Y) grows. A growth like log Y would give X(Y) ~ log Y. Note that Proposition 8 needs (log Y)^0.055 because the colouring is a product over nine graphs, so first look for one potential that works for all nine rows.

