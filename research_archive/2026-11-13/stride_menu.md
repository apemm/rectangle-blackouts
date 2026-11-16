# A menu of strides for the monotone partition

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Two independent derivations of the same idea. Not audited yet.

# Derivation 1: general strides (mu, nu)

## Status

partial

## Summary

A finite menu of strides proves sum_T min_F (k_T + 1) = O(h (log h)^(c_F - 1)), where c_F - 1 = sqrt(3)/2 ~ 0.866 for two strides and tends to sqrt(3) - 1 ~ 0.732. This bounds the class count and the scaffold width, with no dependence on the three-term theorem or the local sparsity bound. Bounded cost forces a finite menu, and no finite menu keeps every k_T bounded. Heuristically, a growing menu still costs h (log h)^0.57.

## Statements

Notation. A stride is f = (mu, nu) with 4 | mu and nu >= 1. Put D = mu^2 + 4nu^2 and K_f = Q(sqrt D), and let chi_f be the Kronecker character of K_f. The diagonal T, s = (T-1)/2, uses the slots i = r + nu t of I_T, one residue r mod nu at a time. Label (i, i+s) goes to column mu t + B, with odd point row 2i+1 and even point row 2i+2s+2. A P conflict between t and t - m is (mu m)^2 + (T - 2nu m)^2 = L^2 with 0 < L < h. In Q(sqrt D) this reads X^2 - D L^2 = -mu^2 T^2 with X = Dm - 2nuT. Let k_T^f be the number of distinct |m|, with 1 <= |m| < ceil(|I_T|/nu), that satisfy this. The base stride (4,1) recovers S_T and k_T. Put g_f(T) = prod over p | T with chi_f(p) = 1 of (2 v_p(T) + 1).

(1) What survives. All items are proved and self-checked, with no independent audit.
 (1a) Proposition 1 holds for any subset of one residue progression of one diagonal, provided v2(nu) <= 2 v2(mu) - 2 (true for every nu with v2(nu) <= 2). Such a subset has slope 1 in label space, and it is P-free when the subset is independent in the distance graph with distance set {|m|}. An arc colouring with ||theta m|| >= 1/M works. It has no tilted right angle. The 2-adic condition is sharp: (mu, nu) = (4, 8), T = 17 has the right angle with vertex (0,18) and ends (4,17), (4,34) [checked by brute force].
 (1b) The 36h argument. If blocks are more than 36h apart, a tilted right angle with an end outside the vertex's block has a leg of slope > 36 inside that block. A leg between two points of the same parity in one block has slope 2nu/mu. So for nu < 18 mu no (E;E,E) or (O;O,O) angle crosses blocks.
 (1c) The mod-p reduction holds inside one stride region. Take all columns divisible by 4, every column satisfying x ≡ lambda_f i (mod p) with lambda_f = mu/nu mod p, p prime, p > max(D h, 36h + mu h/(2nu)), and v2(nu) <= 1. Then every tilted right angle among label points has an even vertex and an even end. Combined with (1a) and (1b), the only type left in a region is (E; O end in the vertex's block, E end in another block). For the base stride this is exactly the open type in Section 8 of the 12 November note, so the menu leaves it where it was.
 (1d) The reduction fails across strides, because different fields mean different slopes mu/nu and therefore different lambda_f. Separating the regions by more than h^2/4 columns removes every tilted right angle and every P conflict between regions, at an extra width of |F| h^2/4.
 (1e) The universal blocker survives: S_1^f is never empty in the tested cases. For example, S_1^(8,1) contains -3 and 5 (24^2 + 7^2 = 25^2 and 40^2 + 9^2 = 41^2), so T·S_1^f ⊆ S_T^f. The reflection m <-> 4nuT/D - m exists exactly when D | 4nuT. For the base stride that condition is 5 | T.

(2) THEOREM [proved, self-checked]. Let F be a finite set of strides, none with D_f a perfect square, and n = |F|. Put lambda = ln 3/(2n) and
  c_F = sqrt3 · sum over S ⊆ F with chi_S = prod_{f in S} chi_f principal of cosh(lambda)^(n-|S|) sinh(lambda)^|S|.
Then for h >= 3,
  sum over odd |T| < h of min_{f in F} (k_T^f + 1) <= C_F h (log h)^(c_F - 1).
Suppose the squarefree parts of the D_f are multiplicatively independent modulo squares, as in {5, 17, 37, 13} from (4,1), (8,1), (12,1), (4,3). Then c_F = ((1 + 3^(1/n))/2)^n, and the exponent c = c_F - 1 is 1 for n=1, sqrt3/2 = 0.866 for n=2, 0.821 for n=3, 0.798 for n=4, and sqrt3 - 1 = 0.732 in the limit. For every menu c_F >= sqrt3, and no multiplicative majorant of min_f g_f does better (minimax plus Jensen).
 Lemma A: k_T^f <= tau(mu^2) g_f(T) (1 + 2.08 log^+(4h^2 D/(mu^2 T^2))).
 Lemma B (Halberstam-Richert type, proved here): if G is multiplicative with 0 <= G(p^v) <= 2v+1, then sum_{n<=x} G(n) <= C x (log x)^(-1) exp(sum_{p<=x} G(p)/p).

(3) Classes and width [proved for the label scaffold only]. Each diagonal T takes the stride f(T) that attains the minimum. Each residue class is coloured greedily with at most 2k+1 colours, or with arcs, M <= 2k+1. The number of classes is then at most 2 max_F nu_f · C_F h (log h)^(c_F - 1). Every class has the properties of (1a). With F = {(4,1), (8,1)} (nu = 1, spacing about 40h per class, as in the base scaffold) this gives O(h (log h)^0.866) classes. The scaffold width is O(h^2 (log h)^0.866) + h^2/2. That beats the O(h log h) arc total and, asymptotically, the local sparsity bound's O(h log h / loglog h), with no use of the three-term theorem, the local sparsity bound or AKS. It is not a bound on m_h, because the (E;O,E) cross-block type, the mixed collisions and the sea stay open.

(4) [(4a) and (4b) proved, (4c) heuristic.]
 (4a) If every stride used has nu_f <= C and block width ratio mu_f/nu_f <= C, then mu_f <= C^2, so a bounded-cost menu is finite.
 (4b) For every finite F, max over |T| < h of min_f k_T^f tends to infinity. So no bounded-cost menu makes every diagonal poor in the sense of bounded k.
 (4c) Model the splitting of T's primes in a growing family of fields as independent. If the number of strides of cost <= X is X^gamma, the best total of cost × (k+1) is h (log h)^(theta) with theta = (2/(1+3^(-gamma)))^(1/gamma) - 1. That is 0.604 for gamma = 1/2, 0.570 for the full family gamma = 2/3, and 0.5 for gamma = 1. It is never linear. Whether chi (rather than k) can be bounded is untouched: scaling families raise k but not chi.

## Proofs

PROOF OF (1a). The odd points satisfy (mu t, 2(r+nu t)+1) and the even points (mu t, 2(r+nu t)+T+1), so both lie on parallel lines with direction (mu, 2nu), at vertical distance T (odd). Vectors from a vertex:
- Along-along: (mu d1, 2nu d1)·(mu d2, 2nu d2) = D d1 d2, which is nonzero.
- Along-across: d1 (D d2 ± 2nu T). This is zero only if D d2 = ∓2nu T. Write v2(D) = v2(mu^2 + 4nu^2). If 2v2(mu) ≠ 2 + 2v2(nu), then v2(D) = min(2v2(mu), 2 + 2v2(nu)). Otherwise v2(D) > 2v2(mu). Either way v2(D) > 1 + v2(nu) = v2(2nuT) when v2(nu) <= 2v2(mu) - 2, so the product is nonzero.
- Across-across: D d1 d2 + 2nuT(d1 + d2) + T^2, which is odd.
A vertical leg (the double itself) forces the other leg to be horizontal, so the angle is axis-aligned. P-freeness is the definition of the distance graph. The arc union bound gives P(||theta m|| < 1/M) = 2/M for each integer m ≠ 0, so M = 2k+1 suffices.

PROOF OF (1b). Write the legs as (X1, Y1), (X2, Y2) with X1X2 = -Y1Y2 and |Yi| < h. If both ends lie outside the vertex's block, |X1X2| > (36h)^2 > |Y1Y2|, which is impossible. If one end Z lies outside, then |X_W| = |Y_W Y_Z|/|X_Z| < h/36 and |Y_W|/|X_W| = |X_Z|/|Y_Z| > 36. Same-parity legs in a block have slope 2nu/mu < 36.

PROOF OF (1c). Columns are even and x ≡ lambda i (mod p), with lambda nu ≡ mu.
- (O;O,O): the dot product is ≡ nu^(-2) D Δ1 Δ2 (mod p). Since p > D, p | Δ1 or p | Δ2, so Δ = 0 (|Δ| < h < p). That leg is horizontal and the angle is axis-aligned.
- (O;O,E): the dot product is ≡ nu^(-2) Δ1 B with B = mu^2 (i2 - i0) + 2nu^2 (2j2 + 1 - 2i0). Here v2(mu^2(...)) >= 4 > 1 + 2v2(nu) = v2(second term), so B ≠ 0. Also |B| <= D h/2 < p. Hence Δ1 = 0 and the angle is axis-aligned.
- (O;E,E) and (E;O,O): dx1dx2 is even and dy1dy2 is odd, so the dot product is odd.
- The remaining types are (E;E,E) and (E;O,E). (E;E,E) is collinear inside a block and excluded across blocks by (1b). For (E;O,E), any crossing forces a steep in-block leg. An in-block E-E leg is not steep, so the steep leg must be V->O inside the block, with the E end outside.
For nu = 1 the placement x = mu i + 4pc realises the reduction at spacing 4p.

PROOF OF (1d). Assume regions are G > h^2/4 apart. A crossing tilted angle needs an in-block leg with |X_W| >= mu >= 4 (an X_W of 0 makes the angle axis-aligned). Then |Y_W Y_Z| = |X_W X_Z| > 4G >= h^2, which is impossible.

PROOF OF LEMMA A. Each counted m gives α = X + L sqrt D ∈ Z[sqrt D] ⊆ O_K with N(α) = -N, where N = mu^2 T^2. Distinct m give distinct α. Since α α' < 0, |α| + |α'| = 2L sqrt D < 2h sqrt D, so N/(2h sqrt D) < |α| < 2h sqrt D. All generators of one ideal are ±α0 η^k, with η the fundamental unit of O_K and log η >= log((1+sqrt5)/2) = 0.4812. The sign is fixed by L > 0. So each ideal of norm N contributes at most 1 + log(4h^2 D/N)/0.4812 values of α. The number of ideals is r_K(N) = sum_{d|N} chi_f(d). r_K(mu^2 T^2) <= tau(mu^2) r_K(T^2), checked prime by prime: at a split p, a+b+1 <= (a+1)(b+1). At an inert p, T^2 has even exponent, so r = 1. At a ramified p, r = 1. Finally r_K(T^2) = g_f(T).

PROOF OF LEMMA B. First, sum_{p^v <= y} G(p^v) log p^v <= C1 y. For v = 1 this is at most 3 θ(y) <= 3y log 4. The terms with v >= 2 contribute O(sqrt(y) log^3 y). Writing n = p^v m with p not dividing m gives
  sum_{n<=x} G(n) log n <= C1 x sum_{m<=x} G(m)/m.
Also sum_{n<=x} G(n) log(x/n) <= x sum_{n<=x} G(n)/n. Adding, S(x) log x <= (C1 + 1) x sum_{m<=x} G(m)/m. The last sum is at most prod_{p<=x} (1 + sum_v G(p^v) p^(-v)) <= exp(sum_{p<=x} G(p)/p + O(1)). The same inequality is in Halberstam and Richert, "On a result of R. R. Hall", J. Number Theory 11 (1979), and in Tenenbaum's book (Ch. III.3). I did not check those references against the source, but the proof above does not depend on them.

PROOF OF THE THEOREM. Let G = prod_f g_f^(1/n), which is multiplicative, at least min_f g_f, and has G(p^v) <= 2v+1. For p not dividing ∏Δ_f, G(p) = 3^(s(p)/n) = sqrt3 · prod_f (cosh λ + chi_f(p) sinh λ) = sqrt3 · sum_S cosh^(n-|S|) sinh^|S| chi_S(p). Principal chi_S contribute loglog x + O(1) by Mertens. Nonprincipal real chi_S contribute O(1), because sum_p chi(p)/p converges (Dirichlet, L(1,chi) ≠ 0). The finitely many p dividing ∏Δ_f contribute O(1). So sum_{p<=x} G(p)/p = c_F loglog x + O_F(1), and by Lemma B, S(x) <= C x (log x)^(c_F - 1). By Lemma A, min_f k_T^f <= C_F (1 + log(h/|T|)) G(|T|). Partial summation: sum_{t<h} G(t) log(h/t) = ∫_1^h S(u) du/u <= C h (log h)^(c_F - 1), since c_F >= 1. Adding h for the +1 terms finishes the proof.
 The bound c_F >= sqrt3 follows because the S = ∅ term is sqrt3 cosh^n λ >= sqrt3. For the minimax claim: a multiplicative function depending on the splitting pattern that majorises min_f g_f must have log G(pattern) >= sum_f w_f [splits in f] log 3 for some weights w in the simplex (LP duality). Then E 3^(<w,ε>) >= 3^(<w, Eε>) = sqrt3, because each field splits half of the primes.

PROOF OF (3). Greedy colouring of a distance graph with k distances uses at most 2k+1 colours, since every vertex has at most 2k neighbours. Each residue class is one class family, which gives the factor nu. The width is at most (classes × max_f spacing) + |F| h^2/4.

PROOF OF (4b). Fix C. For each f, Pythagorean counting shows sum_{|T|<h0} k_T^f >= c_f h0 log h0. The count uses z = c(a+bi)^2 with mu | c, gcd(a,b) = 1, ab ≠ 0, |z| < h0/C', with bounded multiplicity. So some odd T_f has at least C+1 solutions with L < h0. Put T = prod_f T_f and g = T/T_f. Scaling gives (mu gm)^2 + (T - 2nu gm)^2 = (gL)^2, so g·S_{T_f}^f(h0) ⊆ S_T^f(h) once h >= C'' h0^(n+1), and the slot range holds there too. Hence min_f k_T^f >= C+1.

DERIVATION OF (4c) [heuristic]. Model the number w of prime factors of T as Poisson with mean loglog h. Among N = cost^gamma strides the best splitting fraction α costs 2^(w(1-H(α))/gamma) for the value 3^(αw). Minimising over α gives κ = (1/gamma)(ln 2 - ln(1 + 3^(-gamma))) and E e^(κw) = (log h)^(e^κ - 1). The same large-deviation computation for a fixed menu reproduces c_F - 1, so the bound in (2) is expected to be sharp up to constants.

SANITY CHECKS (all under 10 s). Lemma A had no violations over all T for the strides (4,1), (8,1), (12,1), (4,3) at h = 1000, 4000, 16000. The value of sum_T min(k+1)/h was:
- single stride (4,1): 2.72, 3.12, 3.51
- menu {(4,1),(8,1)}: 1.405, 1.532, 1.658
- all four strides: 1.089, 1.134, 1.189
The right-angle brute force agreed with (1a), including the (4,8) counterexample. The region test of (1c) at h <= 20 found no right angles at all, so it says nothing about the mod-p step: cross-block angles only appear for h > 144.

## External results used

- Dirichlet: L(1,chi) ≠ 0 for real nonprincipal chi, so sum_p chi(p)/p converges. Textbook result; I did not look it up.
- Mertens' theorem, and Chebyshev's bound theta(y) <= y log 4.
- Optional reference for Lemma B: Halberstam and Richert, J. Number Theory 11 (1979), and Tenenbaum, Ch. III.3. Not checked against the source, and not needed.

## Checks

I checked Lemma A at h = 1000, 4000 and 16000 and compared menu totals. I brute-forced the right-angle claims of (1a) for 9 cases, including a counterexample to the 2-adic condition. The (1c) region test came out vacuous: there were no angles at the small h I tested. I computed S_1^f for 5 strides. The scripts are scripts_stride_menu/kmenu.py, rightangle.py, modp_region.py and s1.py. The earlier run left no computed data.

## Gaps

- None of these proofs has an independent audit. Each was re-read line by line by me only.
- The Halberstam-Richert and Tenenbaum references are not checked against the source. Lemma B is proved in full, so nothing depends on them.
- The cross-block type (E; O in-block, E in another block), the mixed four-point collisions and the sea are untouched, so there is still no bound on m_h.
- Combining the menu with the local sparsity bound's local-sparsity argument would give O(h (log h)^(c_F-1)/loglog h). That needs an the three-term theorem-type three-term bound in each field Q(sqrt D_f), which I have not proved.
- (4c) and the sharpness of c_F are heuristic. They assume independent splitting and ignore class-group and congruence effects.
- Whether chi(G_T^f), rather than k_T^f, can be bounded for every T is open.

## Missing estimate

To reach O(h) classes, the menu would need either cost that grows faster than any power of the number of available fields, or chromatic cancellation (the missing estimate's estimate (E)) on top of the menu. Counting k alone stops at h (log h)^(sqrt3 - 1) for any fixed menu and at about h (log h)^0.57 (heuristic) for a growing one.

## Next steps

- Prove an the three-term theorem-type three-term bound in Q(sqrt 17), so that the menu {(4,1),(8,1)} and AKS together give O(h (log h)^0.866/loglog h).
- Audit Lemma A and the theorem independently, then add them to the ledger as a menu row.
- Attack the remaining cross-block type (E;O,E). It is the same obstruction for every stride.

# Derivation 2: even strides, scaffold lemma, private blocking for every bipartition

## Status

partial

## Summary

A menu of strides (one stride per diagonal, with one quadratic field per stride) splits the labels into h + O(h (log h)^0.785) monotone, P-free classes without right angles. This beats the h log h / log log h of (local sparsity bound), and the exponent can be pushed down to sqrt3 - 1 + eps. I also prove that private blocking costs c h^2 log^2 h for every bipartition and every common sea alphabet. m_h = O(h^2) is not proved, and neither is any new bound on m_h.

## Statements

NOTATION. h >= 4. A = ceil(h/2), K = floor(h/2). The label (i,j) has odd row 2i+1, even row 2j+2 and offset T = 2(j-i)+1. Its diagonal slots are I_T, n_T = |I_T|, s_T = (T-1)/2. phi = (1+sqrt5)/2. tau = number of divisors.

STRIDE s = 2 sigma (sigma >= 1 an integer), Delta_sigma = sigma^2 + 1. A stride-s block puts the label (i,j) at column s*i. Define
 S_T^(sigma) = { d != 0 : s^2 d^2 + (2d+T)^2 = L^2 for an integer 0 < L < h },
 D_T^(sigma) = { |d| : d in S_T^(sigma), |d| < n_T }, k_T^(sigma) = |D_T^(sigma)|,
 G_T^(sigma) = the graph on I_T with i ~ i' iff |i-i'| is in D_T^(sigma).
sigma = 2 (stride 4) is the setting of the 12 and 13 November notes. There Q = 20d^2 + 4Td + T^2.

PROPOSITION 1' (any even stride). Let s be even. Place an independent set C of G_T^(sigma) in a stride-s block. Then C is monotone with slope 1, has no rival pair, and has no right angle among its black points, tilted or axis-aligned.

LEMMA 2 (ideal count). Let K_sigma = Q(sqrt Delta_sigma), and let g_sigma(T) be the product of (2e+1) over the prime powers p^e || T with p not dividing Delta_sigma and (Delta_sigma/p) = 1. Then for every odd T with 0 < |T| < h,
 k_T^(sigma) <= |S_T^(sigma)| <= 2 tau(sigma^2) g_sigma(T) (1 + 2 log(3h/|T|)/log phi).

LEMMA 3 (mean value). There is an absolute C such that every multiplicative F with 0 <= F(p^e) <= 2e+1 satisfies sum_{n<=x} F(n) <= C (x/log x) exp(sum_{p<=x} F(p)/p) for x >= 2.

THEOREM S (stride menu). Let sigma_1, ..., sigma_m >= 1 be such that no product of a nonempty subset of Delta_{sigma_1}, ..., Delta_{sigma_m} is a perfect square. For example sigma in {1,2,4,6,10} gives Delta in {2,5,17,37,101}, all prime, and strides {2,4,8,12,20}. Put beta_m = ((1 + 3^(1/m))/2)^m - 1. Then there is a C = C(sigma_1..sigma_m) with, for all h >= 4,
 sum over odd T, |T| < h, n_T >= 1, of min_i chi(G_T^(sigma_i)) <= sum_T min_i (k_T^(sigma_i) + 1) <= h + C h (log h)^(beta_m).
Values: beta_1 = 1, beta_2 = 0.866, beta_3 = 0.821, beta_5 = 0.785, beta_10 = 0.758. beta_m decreases to sqrt3 - 1 = 0.732, and a valid menu exists for every m with no conjecture needed.
COROLLARY. The labels split into at most h + C h (log h)^0.785 classes. Each class lies in one diagonal T and carries one stride s_T from {2,4,8,12,20}. Placed at that stride, each class is monotone, P-free and has no right angle (Proposition 1'). The previous bounds were O(h log h) (greedy, 12 November) and O(h log h / log log h) (the local sparsity bound, which needs the AKS theorem). Theorem S does not use (three-term theorem) or AKS.

LEMMA 4 (stride-s scaffold). Fix an even s, a prime p > max(20h, (s^2/2 + 4)h), and the classes of one stride s. Put class c at columns s(i + p c). Then every tilted right angle among the label points has an even vertex V, an odd end P in the block of V at slot distance t1 with 0 < |t1| < 2h^2/(s^2 (p - A)), and an even end Q in another block, with s^2 t1 t2' = 2 c2 (T0 - 2 t1). Here T0 is the offset of V's label, t2' is the column difference V to Q divided by s, and c2 = j_Q - j_V. This is the same open (E;O,E) family as at stride 4.

THEOREM A (private blocking fails for every bipartition and every common alphabet). Take h large, any balanced bipartition (A,B) of the rows, and any nonempty sea alphabet Sigma (a set of rows). Suppose each edge e of K_{A,B} has a prescription S_e, a subset of Z \ {0} with letters in Sigma, such that the double e at column 0 together with S_e is valid in the infinite strip for every completion of the other columns by single black points in rows of Sigma. Then sum_e |S_e| >= c h^2 (log h)^2, with c > 0 absolute. This extends ledger T11 (even h, alphabet {1,h}, parity bipartition) to all heights, all bipartitions and all common alphabets.

NOT PROVED: m_h = O(h^2); any bound m_h = o(h^2 log^2 h); any lower bound above q_h.

## Proofs

[P1'] Proof of Proposition 1'. The odd points (s i, 2i+1) and the even points (s i, 2i+T+1) lie on two lines of direction (s,2), and the even line is the odd line shifted by (0,T). There are three kinds of leg.
- Along a line: (s d, 2d). Two such legs have dot product (s^2+4) d1 d2, which is not 0.
- Along against across: across legs are (s d2, 2 d2 +- T), including d2 = 0. The dot product is d1((s^2+4) d2 +- 2T). Since s is even, s^2 + 4 = 0 mod 4 and 2T = 2 mod 4, so the bracket is 2 mod 4 and not 0.
- Two across legs from one vertex: both ends lie on the other line, so the signs agree. The dot product is s^2 d1 d2 + (2d1 +- T)(2d2 +- T), which is odd.
So no right angle exists. Monotonicity is j = i + s_T. Rival pairs: the odd point of slot i' and the even point of slot i, with d = i - i', are at horizontal distance s d and vertical distance 2d + T. By the rival lemma (sec5, Lemma rival) a rival pair needs (s d)^2 + (2d+T)^2 = L^2 with L odd and L < h, so d is in S_T^(sigma) and |d| < n_T. Independence in G_T^(sigma) excludes this. []

[L2] Proof of Lemma 2. Put X' = 2 Delta d + T and Delta = Delta_sigma. Then s^2 d^2 + (2d+T)^2 = L^2 is equivalent to X'^2 - Delta L^2 = -sigma^2 T^2. So alpha = X' + L sqrt(Delta), an element of Z[sqrt Delta] inside O_K, has norm -n with n = sigma^2 T^2. The map d -> alpha is injective. Also |X'| < sqrt(Delta) h, so |alpha| and |alpha'| are less than Y = 2 sqrt(Delta) h. The number of ideals of norm n is a_K(n) = sum over d | n of chi_K(d). An ideal (alpha) has generators +-eps^k alpha0, where eps >= phi (no real quadratic unit above 1 is smaller than phi). The conditions |alpha| < Y and |alpha'| = n/|alpha| < Y allow at most 1 + log(Y^2/n)/log eps values of k. Since Y^2/n <= 8h^2/T^2 < (3h/|T|)^2, this gives |S_T| <= 2 a_K(n)(1 + 2 log(3h/|T|)/log phi). Prime by prime, a_K(p^(2a+2e)) <= (2a+1) a_K(p^(2e)): for a split prime, 2a+2e+1 <= (2a+1)(2e+1), and otherwise the value is 1. Hence a_K(sigma^2 T^2) <= tau(sigma^2) a_K(T^2), and a_K(T^2) = g_sigma(T) (T is odd; inert and ramified primes give 1). []

[L3] Proof of Lemma 3. Write each n <= x as n = p^v m with p^v || n. Then F(n) = F(p^v) F(m). Summing log n = sum of log p^v over p^v || n gives sum_{n<=x} F(n) log n <= sum_{m<=x} F(m) Phi(x/m), where Phi(y) = sum_{p^v<=y} (2v+1) v log p. The Chebyshev bound theta(y) <= y log 4 gives Phi(y) <= 3 y log 4 + log 4 * y^(1/2) * sum_{v<=log_2 y} 3v^2 <= C1 y. Also sum F(n) log(x/n) <= x sum F(n)/n, because log t <= t. So S(x) log x <= (C1 + 1) x sum_{n<=x} F(n)/n. Finally, sum_{n<=x} F(n)/n <= prod_{p<=x} (1 + F(p)/p + sum_{e>=2} (2e+1) p^(-e)) <= exp(sum_{p<=x} F(p)/p + C2). []

[S] Proof of Theorem S. Put F(p^e) = (2e+1)^(N(p)/m), where N(p) is the number of i with p not dividing Delta_i and (Delta_i/p) = 1. Put F(2^e) = 0. The geometric mean bounds the minimum, so min_i g_{sigma_i}(T) <= prod_i g_{sigma_i}(T)^(1/m) = F(|T|). By Lemma 2,
 min_i k_T^(sigma_i) <= C3 (1 + log(3h/|T|)) F(|T|), with C3 = max_i 2 tau(sigma_i^2) (1 + 2/log phi).
Now compute sum_{p<=x} F(p)/p. For p not dividing 2 prod Delta_i, 3^(1[chi=1]/m) = a + b chi with a = (1 + 3^(1/m))/2, b = (3^(1/m) - 1)/2. So F(p) = sum over subsets U of a^(m-|U|) b^|U| psi_U(p), with psi_U(p) = (D_U/p) and D_U = prod_{i in U} Delta_i. For U nonempty, D_U is not a square by hypothesis. So p -> (D_U/p) agrees, for p not dividing 2 D_U, with a nonprincipal real Dirichlet character, and sum_{p<=x} psi_U(p)/p = O_U(1). With Mertens, sum_{p<=x} F(p)/p = a^m log log x + O(1), and Lemma 3 gives sum_{t<=x} F(t) <= C4 x (log x)^(a^m - 1) for x >= 3. Partial summation follows: sum_{t<=h} F(t) log(3h/t) = integral from 1 to 3h of S(min(u,h)) du/u <= C5 h (log h)^beta_m. Each odd |T| occurs with two signs, and S_{-T} = -S_T. The number of diagonals is at most h - 1, and chi <= k + 1 by greedy colouring in increasing order. This proves the bound.
Menus for every m: take primes p_1 < p_2 < ..., all = 1 mod 4, with p_i larger than every prime factor of the earlier Delta's. Choose 1 <= sigma_i < p_i with p_i | sigma_i^2 + 1. Since sigma_i^2 + 1 < p_i^2, the prime p_i divides Delta_{sigma_i} exactly once and divides no earlier Delta. In any subset U the largest index contributes an odd power of its prime, so D_U is not a square. The sequence a^m = exp(m log(1 + (ln 3)/(2m) + O(m^-2))) decreases to sqrt3. []
Proof of the Corollary. Colour each diagonal properly in G_T^(sigma) for the sigma that attains the minimum, and apply Proposition 1'.

[4] Proof of Lemma 4. Write each leg mod p. With all three points odd, the dot product is (s^2+4) Di1 Di2 mod p. With an odd vertex, an odd end and an even end it is Di1((s^2+4) Di2 + 2 T2) mod p, where |bracket| < (s^2/2 + 4) h < p and the bracket is 2 mod 4. Since |Di| < A < p, in both cases one leg is horizontal, so the other leg is vertical and the angle is axis-aligned. The types (O;E,E) and (E;O,O) have an odd dot product. The gap between blocks exceeds s(p - A) > h. If both ends leave V's block, |X1 X2| > h^2 > |Y1 Y2|, which is impossible. If one end is in V's block on V's own line, its leg is (s Di, 2 Di), and perpendicularity forces |X2| = 2|Y2|/s < h, also impossible. If both ends are in V's block, Proposition 1' applies. So the remaining case is P odd in the block and Q outside it. Then t1 != 0, because a vertical leg would force an axis-aligned angle. The equation follows from (s t1, 2t1 - T0) . (s t2', 2 c2) = 0 together with |t2'| > p - A, |c2| < h/2 and |T0 - 2t1| < 2h. []

[A] Proof of Theorem A. Fix g in Sigma. Let y be a row of the same parity as g with y != g, and put k = |y - g|/2. Take y > g; the other case is a reflection. For uv = k^2 with u < v, the points E = (v-u, g) and F = (0, y) form a diagonal of a tilted rectangle whose other diagonal is W = (-u, g+k), Z = (v, g+k): both diagonals have midpoint ((v-u)/2, g+k), and (v-u)^2 + 4k^2 = (u+v)^2. The axis rectangle on (-u, g), (v, g), W, Z has the same white presentation {W, Z} when the columns -u, v-u and v carry the letter g. W and Z stay white, since their columns are singleton columns with letter g, which is not g+k. This completion is allowed because g is in Sigma. So for every member H = {-u, v-u, v} of this family, S_e must give some column of H a letter other than g. The family has (tau(k^2) - 1)/2 members, and a column lies in at most 2 of them (the argument of T11, section 1). So at least (tau(k^2) - 1)/4 columns of S_e carry a letter other than g. The two points of a double can share such columns, so |S_e| >= (1/2)(b_y + b_y') with b_y = (tau(k_y^2) - 1)/4. In a balanced bipartition every row has degree at least floor(h/2). On the longer side of g the rows of g's parity reach every k <= (h-1)/4. Hence sum_e |S_e| >= (floor(h/2)/8) sum_{k<=(h-1)/4} (tau(k^2) - 1) >= c h^2 log^2 h, by T11 (12): sum_{k<=X} tau(k^2) >= c X log^2 X. []

WHAT EACH FREEDOM GIVES (short).
- Different strides: they help where the 12 and 13 November notes were stuck. The distance set of a diagonal is governed by the primes of T that split in Q(sqrt(sigma^2+1)), so a diagonal that is rich for stride 4 (many primes = +-1 mod 5) is usually poor for another stride. Theorem S proves this on average. Strides do not touch the tau(T) log load of the 13 November note, which comes from the divisors of T.
- Separated regions: these are what make a menu affordable. Put the classes of each stride in their own region. Regions sit more than 2W_h apart and do not interact, so the overhead is O(m h^2). Inside a region, Lemma 4 shows that a uniform stride keeps every gain of the one-prime scaffold. Alone, regions give only subadditivity.
- Bipartition and a common sea: under private (universal-completion) blocking, Theorem A shows they cannot beat log^2 h, at any height. So T1 is optimal for that architecture up to (log log h)^C.
- Rows of the singleton columns: Theorem A fails as soon as different doubles see different alphabets. A double whose rows are y, y' and whose local sea rows are at distances 2k with tau(k^2) small has almost no family. The cost then moves to transitions between seas. I did not bound transitions, so this freedom is neither ruled out nor used.

CONDITIONAL CONSEQUENCE (not a theorem). Suppose that each class block of the stride regions can be completed, at O(1) extra blocks per class, against the remaining families: the cross-block (E;O,E) angles of Lemma 4, mixed quadruples, and the sea (a row-1 sea is free inside blocks, by the 12 November section 7). Then the width is O(h * number of classes) = O(h^2 (log h)^0.785). None of these three items is proved here.

## External results used

- Quadratic fields: the number of ideals of norm n is sum_{d|n} chi_K(d); units are +-eps^k with eps >= phi; splitting of odd p not dividing Delta by the Legendre symbol (Delta/p). Textbook, for example Hardy and Wright chapters XIV and XV.
- Chebyshev: theta(y) <= y log 4. Mertens: sum_{p<=x} 1/p = log log x + O(1). Dirichlet: sum_{p<=x} chi(p)/p = O(1) for a nonprincipal character (Apostol, Introduction to Analytic Number Theory, chapter 7).
- Repository: the rival lemma and the 2W_h + 1 locality (papers/extremal/sections/sec5_threshold.tex); ledger T11 (its section 1 incidence argument and the divisor sum (12)); Proposition 1 and section 7 of research_archive/2026-11-12/arc_classes_monotone_partition.md; sections 2 and 3 of research_archive/2026-11-11/quadratic_threshold_reattack.md, which Lemma 4 generalizes to stride s.

## Checks

Script folder: scripts_architecture/. All runs take under 60 s with py.
(1) stride_sets.py computes k_T^(sigma) from Pythagorean triples. At stride 4 and h = 16384 it gives sum k_T = 41271, which matches the 12 November report and wf1. Sums sum_T k_T for strides 4, 2, 8, 12, 20, and then sum_T min_s k_T:
 h = 1024: 1763, 1328, 775, 1100, 704; min 72.
 h = 4096: 8707, 6645, 3982, 5592, 3658; min 408.
 h = 16384: 41271, 31628, 19400, 27060, 17990; min 2280.
 h = 65536: 191224, 147047, 91946, 127568, 85547; min 11668.
 h = 262144: 868596, 669813, 424337, 586806, 396008; min 56798.
So the class bound sum_T (min k + 1) is 1.14h at h = 16384 and 1.22h at h = 262144. The stride-4 arc classes of 12 November give 2.21h at h = 16384.
(2) check_prop1_bound.py: brute force finds no right angle in any full diagonal block for strides 2 to 12 at h = 12, 17, 24. It also checks |S_T| against the bound of Lemma 2 for sigma in {1,2,4,6,10} at h = 20000: the largest ratio is 0.067.
(3) check_classes.py builds the stride-menu partition and checks every class from the definitions (exact rival-pair test of Lemma rival, all right angles) at h = 24, 41, 64, 99, 100, 121: no violations. A first run at odd h looped over even T, which was a script bug. I fixed it and reran.

## Gaps

- The target is not reached. m_h = O(h^2) is not proved, and no bound o(h^2 log^2 h) on m_h is proved. Theorem S improves only the monotone P-free partition, which is one ingredient.
- The block architecture still has three unproved pieces: the cross-block (E;O,E) angles (Lemma 4 isolates them, for every stride), mixed quadruples between blocks, and a sea that fits the blocks (the row-h family of the even points, and the gap columns).
- Theorem A covers only private prescriptions under universal completion with one common alphabet. It says nothing about per-double alphabets or about the cost of a transition between two seas. I did not bound that cost.
- Theorem S uses standard facts that I cite and do not re-prove: ideal counts a_K(n) = sum_{d|n} chi_K(d) and the unit group in real quadratic fields; Chebyshev's bound theta(y) <= y log 4; Mertens' theorem; sum_{p<=x} chi(p)/p = O(1) for a nonprincipal real character (Dirichlet). C depends on the menu and is not explicit.
- The geometric-mean step makes beta_m the true exponent of the minimum in a random model (a large-deviation computation, not a theorem), so this method cannot go below sqrt3 - 1. The data suggest the real sum is much smaller.
- No independent audit. I re-read every proof above line by line. Proposition 1' and Lemma 4 are short case checks. Lemma 3 is the standard Halberstam-Richert-type argument, written out in full.

## Missing estimate

For the full architecture: in a stride-s region, each class block must survive the (E;O,E) family s^2 t1 t2' = 2 c2 (T0 - 2t1), with 0 < |t1| < 2h^2/(s^2(p-A)), together with mixed quadruples and the sea, at O(1) extra blocks per class. For the partition alone, going below (log h)^(sqrt3 - 1) needs the true minimum over strides rather than the geometric mean, or a per-stride local-sparsity bound (the analogue of the three-term theorem) followed by AKS.

## Next steps

- Audit Theorem S, Lemmas 2 to 4 and Theorem A by hand.
- Redo the 13 November partial power-of-two rule (Lemma 1, Corollary 2) for stride s. The equation becomes s^2 t1 t2' = 2 c2 (T0 - 2 t1), so a larger stride shrinks the dangerous t1 range by s^2.
- Prove the stride-s analogue of the three-term theorem (three-term relations in Z[sqrt(sigma^2+1)]). Combined with AKS it would give h (log h)^beta / log log h.
- Bound the cost of a transition between two binary seas. If it is O(h), per-region sea rows defeat Theorem A's mechanism and may lower the log^2 h of T1.
- Compute exact chromatic numbers of min-stride G_T on rich diagonals to see how far below k_T + 1 they are.

