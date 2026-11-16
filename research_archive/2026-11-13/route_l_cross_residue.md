# Route L: cross-residue pairs and the load balance

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (obstruction): Route L is blocked by the S5 cell. Even label points in different blocks, with different j-residues and so different kappa mod l, form Pythagorean A2 pairs that no congruence kill removes, by a conservation lemma for rules of the form n(c) = kappa(rho_c) mod 2^E l. The count of such pairs is heuristic. (Bal) is false as stated, but a removal form (Bal') is proved. (Pc) is proved for the first moments and Proposition 1(c), reduced for Lemma L-adic, and false for Proposition 1(d). Not audited yet.

# Result

## Status

obstruction

## Summary

Route L is blocked by the S5 cell, not by (Bal). Pairs of even label points in different blocks, with different j-residues and so different kappa mod l, form A2 pairs (Lemma A2 Pythagorean pairs). These are fatal. No congruence argument kills them. The heuristic count is about h^2 Lambda^2/(Q g), and I prove a conservation lemma: any congruence kill of S5 inside the rule family n(c) = kappa(rho_c) (mod 2^E l) removes the averaging. (Bal) is false as stated, but I prove a variant, (Bal'), in which a few diagonals are removed. (Pc) is proved for the first moments and for Prop 1(c), reduced for Lemma L-adic (i) and (ii), and false for Prop 1(d).

## Statements

Notation. A type tau = (iota, sigma). Q = 2^aQ > 32. A piece (s, r) is the part of diagonal s with i = r (mod Q), where r = iota (mod 32). Its j-residue is rho = r + s (mod Q). R_tau is the set of j-residues = iota + sigma (mod 16), so |R_tau| = Q/16, and each diagonal has n = Q/32 pieces (those with rho = iota + s mod 32). Route L rule: n(c) = kappa_rho (mod 16l) with kappa_rho = kappa (mod 16). For two classes c, c': Dn = Ds - p Dt, Delta kappa = kappa_rho' - kappa_rho, Delta rho = rho' - rho, d = v2(Delta rho). For pairs with different rho, 4 <= d <= aQ - 1. g(s) = B0 + 1 + 4 w_s with w_s = |D_T ∩ QZ| is the number of classes reserved for each piece of s. B1 is the threshold on w: a diagonal is heavy when w_s >= B1/4.

R1 (constraints on the assignment; PROVED). (a) If |kappa_rho| <= 7.5h, piece (s, rho) lies in the residue class mod 16l labelled by the integer X = s - kappa_rho. Then load(X) = sum over rho in R_tau of g(X + kappa_rho) 1[rho = iota + X + kappa_rho (32)], and the width per type is 64pl max_X load(X) + O(h^2). (b) Within the current kills, kappa must be a function of (tau, rho) only. (c) The remaining constraints: kappa_rho = kappa (mod 16) ([F1]), |kappa_rho| <= 7.5h, and kappa chosen before (l, p). Otherwise kappa is free. List scheduling is therefore blocked: the jobs come in |R_tau| rigid groups, and each group moves by one common translate.

R2 ((Bal) as stated does not follow from (Eq); PROVED). Put c = Q/512. Let the level set {w = W} be a uniformly random set of diagonals of density pi = Lambda^(-gamma), with gamma > q and c <= (2 - o(1)) Lambda/(gamma ell) - 2. Then, with probability 1 - o(1), every admissible choice of (kappa_rho) has some X with load(X) >= 4W ceil(c/2). For W near B1, "max piece + average" is O(B0 Q + W + Lambda), so the ratio grows like Q/1024.

R3 ((Bal'), the removal form of (Bal); PROVED). Fix eps in (0, 1/4] and put T = max(3, ceil(4/eps)). Take kappa_rho independent and uniform on (kappa + 16Z) ∩ W_rho, where the W_rho are disjoint consecutive windows of length about 15h/|R_tau| in [-7.5h, 7.5h). Then remove, and send to Theorem E, every light diagonal lying in an overloaded level-residue pair (defined in the proof). With probability >= 1/2 jointly over the 512 types, the number of removed diagonals is <= C ell h Lambda^(-3). After removal, every type has
 max_X load(X) <= (B0+1)(Q/240 + 2) + 4T B1 + (44 + 80 ell Lambda^eps) mu_w, where mu_w <= (Q/(15h)) sum_s w_s.
 Under the first moment of (Eq), mu_w = O(Lambda). The removed diagonals cost o(h^2) through Theorem E.
 So M <= C h^2 (B0 Q/240 + B0 + T B1 + ell Lambda^(1+eps)) for the light part, and the Route L arithmetic is unchanged: 1.2493 with Bad_split and 1 without, under (Eq) and (Pc).

R4 (first moments; PROVED, given Theorem U of uniformity_first_moments.md). For every class datum made of pieces, every kappa_rho with |kappa_rho| <= 7.5h and kappa_rho = kappa (mod 16), and every stacking order fixed before (l, p):
 - the bounds of Theorem U hold multiplied by |R_tau| = Q/16 for the l-type and both-type families: A4 (I.2 and II), B7 even-even, D18;
 - they hold unchanged for the p-type families: B7 odd-odd, D8, D17.

R5 (Prop 1(c), II(-1,-1) with Sigma != 0; PROVED). Between classes of different j-residue it is empty, by a 2-adic argument that uses the i-residues mod Q of both classes. This includes two pieces of one diagonal.

R6 (Lemma L-adic (i), even-even Pc; PROVED reduction). Pairs with d = 4 are empty. Every survivor (d >= 5) is a parked triple, never fatal. Its white corner W cannot coincide with that of an intra-class odd Pc triple, an SLF-Pc triple or an FFo triple. OPEN: two cross-rho even-even Pc triples sharing W.

R7 (Lemma L-adic (ii), Fee; PROVED reduction). Pairs with d in {4, 5, 6} are empty. Every survivor (d >= 7) is parked: W lies in a filler column at slot offset alpha, with alpha != 0 (mod Q), and W is never black. OPEN: V3 cells Fee/FFo and Fee/Fee at a deep-column W.

R8 (J4). J4 holds between classes of one piece (|Dt| >= 16l). It fails between two pieces of one diagonal, which can be 64p columns apart. The cells above (R4 to R7, (E;O,E) by rigid Theorem 2(d), and S5) all allow Ds = 0. Cells outside the (Pc) list that relied on J4 were not re-checked.

R9 (Prop 1(d), S5, cross-block even-even A2 pairs: a REAL OBSTRUCTION). Notation: δ = slot difference, ε = Dj.
 (a) Local criterion (PROVED). Let δ, ε = 0 (mod 16), ε != 0, Dn = ε - δ, d = v2(ε), a = v2(Dn). If 4δ^2 + ε^2 is a square, then a = d or a <= d - 3. Every such pattern is solvable 2-adically. For a prime l with (5/l) = -1 and l > |ε|: l | Dn gives no solution (this is Prop 1(d)), and Dn ≢ 0 (mod l) is solvable l-adically.
 (b) Fatality (PROVED from the audited Lemma A2 and (B5)-(B6)). Take an A2 pair of even label points of R_tau with |δ| <= h^2/8 - h whose witness slots hold no label. Then both witnesses are offset-0 fillers in row T*_tau - 24, and the four points form a mixed quadruple, which is a violation.
 (c) No congruence kill (PROVED). For cross-rho pairs under the Route L rule, the pattern a = d is compatible with every congruence the layout supplies: mod Q, mod 16l, mod p, and the type residues.
 (d) Reduction (PROVED) and count (HEURISTIC). For blocks at offset Dt, the S5 label pairs correspond exactly to solutions of X^2 - 20y^2 = -16 Dn^2 with X = 10Di + 8pDt + 2Ds, Di = r' - r (mod Q) and |Di| < A. Heuristic: about c Lambda^2/(Q g) S5 pairs per label, with c of order 1e-4. At the Route L optimum (Q g of order Lambda^1.249) this is about h^2 Lambda^0.75 pairs in all, which is not O(h^(2-delta)). Relocating them at the price floor of c Lambda^2 per label costs more than T1.

R10 (conservation lemma; PROVED). Consider any region with rule n(c) = kappa(rho_c) (mod 2^E l), E >= 4, kappa fixed before (l, p), and classes that are pieces. Suppose S5 is excluded by congruences for all pairs. Then the pieces of any diagonal s occupy at most 2^(E-2) residues mod 2^E l, so width >= 16 p l C_tau(s) - 4p 2^E l, where C_tau(s) is the number of classes of s in tau. This is at least a quarter of the rigid price of Prop 4. For E = 4 (Route L itself) every diagonal sits in one residue class mod 16l, so there is no spreading at all. Small-case search finds the true maximum to be 2^(E-3).

COROLLARY (the Route L exponent under what is proved). No exponent below theta* = 1.4967429 (Prop 3). Under (Eq), (Bal') [proved], R4 to R8, the two open V3 cells, and the extra hypothesis (S5'), "cross-rho S5 pairs hit O(h^(2-delta)) labels", the Route L arithmetic gives 1.2493 with Bad_split and 1 without it. But (S5') contradicts the heuristic of R9(d). By R10, no congruence-based kill within the rule family can supply it: there the averaging is lost, and the width returns to the rigid max-priced form, whose best proved exponent is theta*.

## Proofs

0. FACTS USED THROUGHOUT (Route L rule, one type tau).
 (F0) The placement rule is p t = s - kappa_rho - b (mod 16l). For two classes, p Dt = Ds - Delta kappa (mod 16l), so Dn - Delta kappa = Ds - Delta kappa - p Dt lies in 16lZ.
 - If Dn = Delta kappa, then p | Ds - Delta kappa. With |kappa| <= 7.5h, |Ds - Delta kappa| < 16h < p, so Dt = 0 and the two classes are equal (one class per position).
 - So for distinct classes, 0 != Dn - Delta kappa. Locality gives |Dn| <= h^2/8 + h, so |Dn - Delta kappa| < (1.04h)^2 for h >= 30.
 (F1) Every label of a class has i = r_c and j = rho_c (mod Q). So:
 - two labels of one class have Di = 0 (mod Q);
 - labels of classes c, c' have Dj = Delta rho and Di = r' - r (mod Q);
 - kappa_rho = kappa (mod 16) keeps [F1]: every label slot is rho_tau (mod 16), i = iota (mod 32), M_c = M_c' (mod 16) (R1 of v3), and Dn = 0 (mod 16).

1. R1.
 (a) Write X = s - kappa_rho. Then |X| < 8h < 8l·... more precisely |X| < 8h <= 8.32h <= 8l, so the residue p t (mod 16l) = X + b identifies the integer X. The pieces at one residue are exactly those with s - kappa_rho = X. They are stacked in periods t = t0 + 16l k, and the width is 4p · 16l · max load plus the margins.
 (b) Take two classes with the same rho on different diagonals, or on one piece.
 - (E;O,E): Theorem 4(c) separates only different j-residues.
 - S5: R9(a) leaves the pattern a = d open whenever v2(Dj) is not pinned below v2(Dn). For same-rho classes, v2(Dj) >= aQ can be arbitrary.
 - So the only available kill is l | Dn (Prop 1(b), (d), L-adic), which forces kappa_rho = kappa_rho' (mod l).
 (c) The constraints come from:
 - [F1], from (B5);
 - (a) and (F0), for |kappa| <= 7.5h;
 - Theorem U, whose template needs everything except (l, p) fixed first.
 Nothing else in (B0)-(B10) involves kappa. Types are separate regions, so each type chooses its own kappa.

2. R2. Index X over the <= h + 1 integers = sigma - kappa (mod 16) with |X| < 8h. Put I_rho = {s in the type : s = rho - iota (mod 32)}, so |I_rho| is about L0/2 with L0 about h/16. Put A_X = {rho : X + kappa_rho in I_rho}. Fix a vector kappa.
 - sum_X |A_X| = sum_rho |I_rho|, about |R_tau| L0/2. So the mean of |A_X| is c = Q/512, and |A_X| <= |R_tau|.
 - Hence #{X : |A_X| >= c/2} >= (|R_tau| L0/2 - (h+1)c/2)/|R_tau| >= L0/4 - 1.
 - The point sets P_X = {X + kappa_rho : rho in A_X} and P_X' meet only if X - X' lies in {kappa_rho' - kappa_rho}, a set of at most |R_tau|^2 values. Greedy selection therefore gives a family G of good X with pairwise disjoint P_X and |G| >= (L0/4 - 1)/(|R_tau|^2 + 1), which is of order 4h/Q^2.
 - For S random of density pi, the events "ceil(c/2) given points of P_X lie in S" are independent over X in G, each with probability >= pi^(ceil(c/2)). So P(max_X |S ∩ P_X| < c/2) <= exp(-|G| pi^(c/2+1)).
 - There are at most h^|R_tau| vectors kappa. The union bound gives failure probability <= exp(|R_tau| Lambda - |G| Lambda^(-gamma(c/2+1))).
 - gamma(c/2+1) ell <= (1-o(1)) Lambda gives Lambda^(-gamma(c/2+1)) >= h^(-1+o(1)). Since Q <= Lambda^C, |G| Lambda^(-gamma(c/2+1)) >= h^(o(1)) and is >> |R_tau| Lambda, so the failure probability is o(1).
 - At any X with |S ∩ P_X| >= c/2, load(X) >= 4W c/2.
 - The level-set model changes positions only. (Eq) constrains only the counts #{w >= M} and the first moment, so it cannot exclude it. With gamma > q, mu_w is about Q pi W/240 = o(W).

3. R3.
 - Levels: S_k = {light s : 2^k <= w_s < 2^(k+1)}, 0 <= k <= k_max with 2^(k_max) < B1/4. r_k(X) = #{rho : X + kappa_rho in S_k ∩ I_rho}.
 - kappa_rho is uniform on the m_w/16 points of W_rho ∩ (kappa + 16Z). So P(X + kappa_rho in S_k) <= 16 |S_k ∩ (X + W_rho)|/m_w. The X + W_rho are disjoint, so E r_k(X) <= lambda_k := 16 |S_k| / m_w = |S_k| Q (1+o(1))/(15h).
 - r_k(X) is a sum of independent Bernoulli variables, so P(r >= t) <= (e lambda/t)^t. For t >= 2e lambda, E[r 1(r >= t)] <= (t+1)(e lambda/t)^t.
 - Thresholds: t_k = T if lambda_k <= Lambda^(-eps); otherwise t_k = ceil(max(2e lambda_k, 9 ell)).
 - Removal: for every (X, k) with r_k(X) > t_k, remove the diagonals of S_k hit at X, from every type. Removal only lowers loads.
 - Expected removals per level are at most (h+1) times (T+1)Lambda^(-4) in the first case. In the second case they are at most (h+1)(t+1)2^(-t) <= (h+1) 2^(-4.5 ell) <= (h+1) Lambda^(-3.1).
 - There are at most 3 ell levels, so E[removed] <= 512 · 3 ell (T+1)(h+1) Lambda^(-3). By Markov, it is at most twice that with probability >= 1/2. Theorem E prices each diagonal at h Lambda^2 ell^C, so the total cost is h^2 Lambda^(-1) ell^C = o(h^2).
 - Flat part (deterministic): #{rho : (X + W_rho) ∩ [-h/2, h/2] != empty} <= h/m_w + 2 = Q/240 + 2.
 - w-part after removal (4w < 2^(k+3)):
 - levels with lambda_k <= Lambda^(-eps) contribute <= 8T · 2^(k_max+1) <= 4T B1;
 - the other levels satisfy 2^k < 2^k lambda_k Lambda^eps, so they contribute <= sum 2^(k+3)(2e lambda_k + 9 ell + 1) <= (16e + (72 ell + 8)Lambda^eps) sum_k 2^k lambda_k;
 - and sum_k 2^k lambda_k <= (Q/(15h)) sum_s w_s = mu_w.
 - (Eq)'s first moment, sum_T Q|D_T ∩ QZ| <= C h Lambda, gives mu_w <= C Lambda.
 - Every choice here uses w and random bits only, before (l, p), so K6 holds. The removed set goes to Theorem E, which does not use (l, p) (Lemma U3 and block_layout_n1).
 - Exponents: max(q + b0, b1, 1 + eps) as in Route L section 7. With E > 1 + eps, the optimum 1.2493 is unchanged.

4. R4. Replace U1(a) by (F0). U1(b) and U1(c) hold with the stacking map: a slot gives (i, t), and t gives the class through (X, k), fixed before (l, p).
 - In template U2, the anchor L0 fixes its class and hence rho0. The partner's rho2 is not fixed by the shape.
 - Realisation needs 16l | Delta - (kappa_rho2 - kappa_rho0) for some rho2 in R_tau. Each value is a fixed nonzero integer below (1.04h)^2 by (F0), so it has at most one admissible l.
 - Hence: in the l-type case, the realising pairs number <= |R_tau| #P; in the both case, <= |R_tau|; the p-type case is unchanged.
 - The uniqueness step of U2 is unchanged. So every bound of Theorem U gains at most the factor Q/16 <= Lambda^C, which still gives h^(2-delta').
 - The deterministic exclusions that Theorem U imports (Dx = 0 mod 64, Dy = 0 mod 32 or 64, b != 0 by G_T-independence) use only (F1).

5. R5. In II(-1,-1) (sea_census B1, re-derived from cross_class_sea L0): A, B are even, C, D are odd, d = iC - iA, d' = iD - iB, U = B - A = (4(Dj - Dn), 2Dj), and U.2n = 0 gives Dj(5 Sigma - S) = 4 Sigma Dn with Sigma = d + d' and S = s0 + s' + 1.
 - A and C lie in one block, hence in one class, so Q | d by (F1). Likewise Q | d'. So v2(Sigma) >= aQ (Sigma != 0).
 - S is odd (s0 = s' mod 16) and Sigma is even, so 5 Sigma - S is odd.
 - Dj = Delta rho (mod Q) gives v2(LHS) = d <= aQ - 1, while v2(RHS) >= 2 + aQ + 4. Contradiction.
 - If Dn = 0, then the RHS is 0 but the LHS is nonzero.
 - The argument holds for Ds = 0. Same-rho pairs keep the l-adic proof (Delta kappa = 0).

6. R6. The equation (v3 A(ii), L-adic (i)) is 2(Dj - Dn)a = f Dj with f odd.
 - With v2(Dj) = d, a solution needs v2(Dn) = d - 1 - v2(a) < d. Since v2(Dn) >= 4, d = 4 is impossible.
 - Pc is always parked (block_sea (Pc)).
 - W = G + (a, -f) has row(W) - r0 = g = 2Dj, with v2 = d + 1 in [6, aQ]. Also x_W = x_E (mod 4), so W lies in a shallow column.
 - Compare the other parked shallow-column triples (v3 Theorem B):
 - intra-class odd Pc has row(W) - r0 = 2t with t = Di in one class, so Q | t and v2 >= aQ + 1;
 - SLF-Pc has v2(g) = 3;
 - FFo has a deep W.
 - Theorem A(i), A(ii) odd-odd and mixed parity, and A(iii) use only mod 4, mod p and parity, so they are unchanged.

7. R7. The equation (v3 Theorem B, L-adic (ii)) is 8 alpha delta = -d0 eta with d0 odd, eta = Dj, delta = Dj - Dn, and V - E1 = (4 alpha, d0).
 - If v2(Dn) >= v2(eta), then 3 + v2(alpha) + v2(delta) > v2(eta), which is impossible. So v2(Dn) = v2(eta) - 3 - v2(alpha) >= 4, which needs d >= 7.
 - Survivors: v2(alpha) <= aQ - 8 and alpha != 0. W = E2 + (4 alpha, d0) sits at slot n_E2 + alpha with |alpha| < h/600, so it lies inside E2's block or the gap.
 - Its i-residue is != r' (mod Q), so it is not a label of E2's class. It is a filler column whose single point is in row y_V, because n_W = n_V (mod 16) and so both have the same offset.
 - row(W) = y_V + 2 eta != y_V, and it is odd. So the triple is parked and W is white.

8. R8. Classes of one piece share (s, rho), so Dt is in 16lZ \ {0}. Across pieces of one diagonal, Dt = -p^(-1) Delta kappa (mod 16l) can be 16. The proofs of R4 to R7, rigid Theorem 2(d) and R9 never assume Ds != 0.

9. R9.
 (a) 2-adic part.
 - If a < d, then v2(δ) = a and 4δ^2 + ε^2 = 2^(2a+2)(δ'^2 + 2^(2(d-a-1)) u^2), with δ', u odd. For d - a = 1 the bracket is 2 (mod 8), for d - a = 2 it is 5 (mod 8): neither is a square. For d - a >= 3 it is 1 (mod 8), a 2-adic square.
 - If a = d, then δ = ε - Dn has v2 >= d + 1, and the bracket u^2 + 4δ^2/2^(2d) is 1 (mod 8), a square.
 - If a > d, then v2(δ) = d and the bracket is 5 (mod 8).
 l-adic part:
 - If l | Dn, then L'^2 = 5ε^2 (mod l) with (5/l) = -1. So l | ε, which is impossible since 0 < |ε| < l.
 - If Dn = Delta (mod l) with Delta != 0, then ε = 0, L' = 2Delta is a smooth point of the conic 4(ε - Delta)^2 + ε^2 = L'^2 over F_l, and Hensel's lemma lifts it.
 (b) Slots of R_tau are rho_tau (mod 16), so δ = 0 (mod 16). Also ε = Dj = 0 (mod 16). Then L'^2 = 0 (mod 256), so L' = 0 (mod 16) and L = L'/2 = 0 (mod 8).
 - Hence n_A = n_C + (δ - L)/2 = n_C (mod 4) and n_B = n_A + L = n_C (mod 4).
 - (B6) puts a filler at offset 0 in row T* - 24 in every label-free deep column. Kept labels have rows <= T* - 321, so (y_C + y_D)/2 != T* - 24.
 - Lemma A2 (deep_layer_bh16, audited) then gives a mixed quadruple, spanning 4L <= 2W_h columns.
 (c) Use (a) with a = d, which no datum of (F0) or (F1) excludes. Mod p, δ = Di and ε = Di + Ds, so 4Di^2 + (Di + Ds)^2 = L'^2 imposes no condition on the free Ds.
 (d) Write P = pDt and S = Ds, and f(Di) = 4(Di+P)^2 + (Di+S)^2. Then 20 f = (10Di + 8P + 2S)^2 + 16(P - S)^2, which is the norm equation stated in R9(d).
 Heuristic: let r2(Dn) be the number of ideals of norm 16 Dn^2. Their generators must fall in a window of relative size about A/(p|Dt|). Summing over |Dt| <= h/320 and over the classes gives the per-label rate stated in R9(d), about c Lambda^2/(Q g), up to the factor log^2(h/10^4) in the admissible divisor range f1 <= h/608.

10. R10.
 - Index the pieces of s by u, with rho = rho0 + 32u. Give each a class K = kappa mod l and lambda = kappa mod 2^E = kappa0 + 16f, f in Z/2^F, F = E - 4.
 - By R9(a), a congruence kill of S5 for pieces with K != K', alpha = v2(Du) and d = 5 + alpha needs the forced valuation v = 4 + v2(Df) to satisfy v in {d-2, d-1} or v >= d+1 (visible, v < E), or Df = 0 with d + 1 <= E. In every option beta := v2(Df) >= alpha - 1. Also K != K' forces alpha <= F.
 - Pieces with equal rho mod the finest known 2-power must share K, because v2(Dj) is not pinned there.
 - Claim: N = #{(K, f)} <= 2^(F+2). If there is a single K, then N <= 2^F. Otherwise, for each leaf x let k(x) be the least k such that the ball B(x, k) = {z : v2(z - x) >= k} lies in K(x). By minimality there is y with K(y) != K(x) and v2(x - y) = k(x) - 1 <= F, so k(x) <= F + 1.
 - Every z in B(x, k(x)) has v2(z - y) = k(x) - 1, by the ultrametric property. So f(z) = f(y) mod 2^(k(x)-2), and B(x, k(x)) carries at most 2^(F - k(x) + 2) values of f.
 - For z in B(x, k(x)), k(z) = k(x). So these balls partition the leaves, and sum 2^(-k_B) <= 1. Hence N <= 2^(F+2) sum 2^(-k_B) <= 2^(E-2).
 - Pieces of s with equal (K, lambda) share s and kappa mod 2^E l, hence one residue mod 2^E l, and must be stacked. So some residue holds >= C_tau(s)/2^(E-2) classes, and width >= 4p 2^E l (C_tau(s)/2^(E-2) - 1).
 - For E = 4, F = 0, the finite valuation options are empty and Df = 0 needs d <= 3, so K is constant on all pieces.
 - Why every pair must be killed: kappa precedes (l, p). For generic p, every pair of residues has pieces of some diagonals within reach. The only way out is to tie p to l, which breaks the both-type first moments.

## External results used

- Tail bound P(X >= t) <= (e mu/t)^t for sums of independent Bernoulli variables with mean <= mu (standard Chernoff/Poisson form).
- Every smooth conic over F_l has F_l-points; Hensel's lemma for lifting a smooth point.
- Repository inputs used as audited or proved: Lemma A2 of deep_layer_bh16 (audited A10); threshold_families Prop 1(d) and sawtooth Lemma 4(b) (audited); rigid_layout Theorem 4(c) and Theorem 2(d); v3 Theorems A and B; block_sea (Pc) parked; sea_census B1 (C3 equation); uniformity_first_moments Theorem U and Lemmas U1-U3 (not audited); consolidated_board_v2 (B5), (B6), [F1]; relocation_price_floor Theorem R (not audited), only for the price remark.

## Checks

Script folder scripts_pc/. Each script ran with py in under 35 s. The repository was only read.
- s5_local.py: 3488 integer solutions of 4δ^2 + ε^2 = square with δ, ε = 0 mod 16 (ε < 4000). 0 violations of the criterion "v2(Dn) = v2(ε) or <= v2(ε) - 3"; every pattern v2(Dn) = v2(ε), d = 4..10, occurs. l-adic check: 52976 (solution, l) pairs with (5/l) = -1 and l > |ε|, none with l | Dn.
- conserve.py (exhaustive) and conserve2.py (local search): maximal N. The strict rule gives exactly 2^F. The relaxed rule gives 2^(F+1) for (D, F) up to (6, 4), inside the proved 2^(F+2).
- s5_sim.py: Route L model region at h = 20000, Q = 256, 16 j-residues, 6000 sampled blocks (234766 labels). 0 S5 pairs, the same as the L***-like control. The expected count is below 1, because admissible f1 <= h/608 leaves only f1 in {16, 32}. This explains why S5 cannot be seen at accessible heights; it is not evidence against R9(d).
- By hand: (F0); the R5 valuations; the R6 and R7 row and offset arguments; the norm identity 20f = X^2 + 16Dn^2; the R3 constants; the ball-lemma induction.

## Gaps

- R9(d) is heuristic: I have no rigorous lower bound on the number of cross-rho S5 pairs in an actual Route L board. A proof would need equidistribution, on average over Dt, of generators of norm -16 Dn^2 in short windows (the reduction is proved). The constant is tiny (admissible f1 <= h/608): at h = 2e4 the count is about 0.7 in the model, and my simulation found 0.
- R10 covers only rules of the form n(c) = kappa(rho_c) (mod 2^E l) with kappa fixed before (l, p). Not ruled out: (i) a deep layer whose witness rows differ between pieces, for example a piece-dependent sawtooth phase (it conflicts with R1, M_c = M_c' mod 16, used by the Foo filler-vertex kill and v3 Prop D); (ii) LLL-type reassignment of periods after (l, p), though the heuristic rate per label grows like Lambda^0.75; (iii) layouts that tie p to l (these break the both-type first moments).
- R10 constant: proved N <= 2^(E-2); exhaustive and local search give 2^(E-3) (D <= 6, F <= 4).
- R6 and R7 leave V3 cells open: cross-rho ee-Pc/ee-Pc at a shallow W, and Fee/FFo and Fee/Fee at a deep W.
- R8: cells outside the (Pc) list that the obstruction table dismissed through J4 or through 'distinct residues mod 16l' were not re-checked for two pieces of one diagonal.
- R3 uses the first moment of (Eq) for mu_w = O(Lambda). Without it, mu_w enters the width directly. R2 shows (Bal) itself is not implied by (Eq); (Bal) for the true w is open but not needed.
- R4 rests on Theorem U (not audited). R5 rests on the C3/B1 equation (re-derived in sea_census, not audited). R9(b) rests on the audited Lemma A2 and on (B5)-(B6).
- Nothing here is audited. The corollary does not give a lower bound for m_h, or for the rigid family: chi- or type-restricted heaviness might decay faster than kappa-heaviness (open).

## Missing estimate

To revive Route L, one of these is needed. (1) A non-congruence kill of cross-rho S5 pairs. The concrete form: a filler rule under which the two witness columns n_C - f1/4 and n_D + f1/4 of pieces with different kappa mod l never share a black row, compatible with R1 and the SAW* lemmas. (2) A proof that the norm-equation solutions X^2 - 20y^2 = -16Dn^2 in the windows of R9(d) are rarer than equidistribution predicts. Both look unlikely. R10 shows that no rule n(c) = kappa(rho_c) (mod 2^E l) can do it by congruences, and gains a factor at most 2^(E-2) relative to... in fact no averaging gain at all, only a constant. Otherwise the exponent question returns to the rigid family: the decay of #{T : chi(G_T[tau]) >= Lambda^x}, or of the type-restricted count, against the kappa-count.

## Next steps

- Record in the ledger that Route L fails at the S5 cell (threshold_families Prop 1(d) for pairs with different j-residues). Downgrade the heavy note's Route L row from '1.2493 under (Pc), (Eq), (Bal)' to 'blocked by S5; (Bal') proved; R4/R5 proved'.
- Have a second reader audit R9(a)-(c), R10 (the ball lemma) and R3. Each is about a page.
- If Route L is kept alive: test a piece-dependent sawtooth phase against the R1-based kills (Foo filler vertex, v3 Prop D, three_label Q3) before anything else. It is the only S5 escape found.
- Optional: turn R9(d) into a theorem through the norm-equation reduction, averaging over Dt and l to get a lower bound for S5 in Route L layouts.
- Reuse R4, R5 and R3 elsewhere: R4 lets any later layout use per-class kappa in the first-moment families; R3 is a general removal-form balancing lemma for sums of rigid translates.
- Return effort to the rigid family: the type-restricted or chi heavy counts (the open half of Theorem 2), and hypotheses (F) and (NR).

