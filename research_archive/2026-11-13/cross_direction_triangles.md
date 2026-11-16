# The cross-direction triangle count

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: triangles of integral-distance pairs with a long, flat edge are power-sparse, with codegree at most C Delta_Z h^(1-a/2+eps), by Heath-Brown's Theorem 15 on a quartic curve. Unconditionally T(o) = o(D^2). The full bound T(o) <= D^2 h^(-c) reduces exactly to one open estimate (MT) on round integral triangles, lattice points at integral distance from both 0 and w in a disc of radius about h^(1+a). Not audited yet.

# Result

## Status

partial

## Summary

Proved: triangles with a long (flat) edge are power-sparse. For the edge o-o1 with column offset at least h^(1+a), codegree <= C Delta_Z h^(1-a/2+eps), via Heath-Brown's Theorem 15 on a quartic curve. Not proved: the full bound T(o) <= D^2 h^(-c). It reduces exactly to one open estimate (MT) about "round" triangles, those with all edge slopes within h^(+-a). Proved unconditionally: T(o) <= C a^2 B^2 + o(B^2), where B = Delta_Z h Lambda^2, so T(o) = o(B^2) and T(o) = o(D^2) for options with D of order B. Numerics up to h = 3200 are consistent with (MT) but cannot tell a power saving from a polylog one.

## Statements

SETTING. Take a T1-type block (T2, Theorem E or Theorem D class block). Each label f has a diagonal T_f, an odd row a_f and an even row b_f = a_f + T_f. All rows lie in [5000, h-5000]. A label is determined by its diagonal together with either of its rows, since f = f_{T,i}. Let Delta_Z be the number of distinct diagonals among the labels. Slots are the columns 7j, with N slots, and n = |Z|. The option (f, j) has, in parity pi, the point (7j, rho_pi(f)).

Define
 P_h = {(X, y) in Z^2 : X != 0, 0 < |y| < h, X^2 + y^2 a square}.
By Lemma F and Proposition 2, an H_F edge (e, j) ~ (f, j') in parity pi forces z = (7(j'-j), rho_pi(f) - rho_pi(e)) to lie in P_h. Only this necessary condition is used, so every count below is an upper bound. Note |X| <= (y^2 - 1)/2 automatically.

For w in Z^2 \ {0}, define the focal count
 I(w) = #{z in P_h : z - w in P_h}.
"Flat" means |X| >= h^(1+a) and "moderate" means |X| < 2h^(1+a). T(o) is the number of unordered pairs {o1, o2} in N_F(o) with o1 ~_F o2, not all three on one line of Proposition 2, with the parities of the three edges arbitrary.

LEMMA 1 (reduction; proved). Let o = (e, j0) and o' = (f, j1) be options with j1 != j0. Put z1 = (7(j1 - j0), a_f - a_e). Then
 #{o2 : o2 ~_F o and o2 ~_F o'} <= sum over (pi02, pi12) in {odd, even}^2, and over the diagonals T of Z, of I(z1 - (0, tau)).
Here tau = tau(pi02, pi12; T_e, T_f, T) is an explicit integer combination of T_e, T_f and T with |tau| <= 2h. So codeg_F(o, o') <= 4 Delta_Z max over tau of I(z1 - (0, tau)). For a single fixed vertex,
 T(o) <= sum over o1 in N_F(o) of codeg_F(o, o1).

LEMMA 2 (focal parabolas; proved). Every z = (X, y) in P_h lies on the parabola X = sigma (y^2 - delta^2)/(2 delta), with sigma = sgn X and delta = L - |X|. Here 1 <= delta < |y| and delta divides y^2. Equivalently y = delta* u and X = sigma kappa (u^2 - mu^2)/2, where delta = kappa mu^2 with kappa squarefree and delta* = kappa mu. Also delta < y^2/(2|X|), so flat vectors have delta < h^(1-a).

THEOREM A (flat focal vectors; proved, using Heath-Brown 2002, Theorem 15). For every w != 0, every a in (0, 1] and every eps > 0,
 I_flat(w) := #{z in P_h : z - w in P_h, max(|X_z|, |X_z - W_x|) >= h^(1+a)/2} <= C_eps h^(1 - a/2 + eps).
In particular, if |W_x| >= h^(1+a), then I(w) <= C_eps h^(1 - a/2 + eps).

LEMMA 3 (moderate mass; proved). #{z in P_h : |X_z| < 2h^(1+a)} <= (24/pi^2) a h Lambda^2 + C h Lambda. For comparison, |P_h| <= (12/pi^2) h Lambda^2 + C h Lambda, with Lambda = log h.

THEOREM B (codegrees; proved). Take options o != o' in different slots, with w as in Lemma 1.
(B1) codeg_F(o, o') <= 4 Delta_Z [C_eps h^(1-a/2+eps) + min(I_mod, (24/pi^2) a h Lambda^2 + C h Lambda)]. Here I_mod counts z with both z and z - w moderate. If |X1| >= h^(1+a), the I_mod term is absent. This bound includes the collinear common neighbours.
(B2) Common neighbours that use one coincidence edge, namely (g, j0) or (g, j1) H_F-adjacent to the other option, number at most 4 Delta_Z tau(X1^2) <= Delta_Z h^(O(1/loglog h)).
(B3) Unavoidable cliques. Options in the same slot have at least n - 2 common neighbours (C1). Options on one line of direction v have at least s_v - 2. These must be handled as slot and line constraints, not as codegrees.

THEOREM C (triangles; proved). For every option o, every a in (0, 1] and every eps > 0,
 T(o) <= 4 C_eps Delta_Z h^(1 - a/2 + eps) D_F(o) + (1/2) D_mod(o)^2,
 D_mod(o) := #{o1 in N_F(o) : |X1| < 2h^(1+a)} <= 2 Delta_Z ((24/pi^2) a h Lambda^2 + C h Lambda).
Triangles with one coincidence edge number at most 4 Delta_Z max tau(X^2) D_F(o).

COROLLARY C'. Put B = Delta_Z h Lambda^2, so that D_F(o) <= C B. Then
 T(o) <= C B^2 (a^2 + Lambda^(-2)) + C_eps B^2 h^(-a/2+eps).
So for every fixed a, T(o) <= C a^2 B^2 when h >= h0(a), and T(o) = o(B^2). For an option with D(o) >= c0 B, T(o) = o(D^2). The flat part alone satisfies T_flat(o) <= D^2 h^(-a/2+eps)/rho whenever n >= rho Delta_Z h, using D >= n - 1.

CONDITIONAL THEOREM D (the target). Suppose the following estimate holds.
 (MT_pt)(a, c): I_mod(w) <= C h^(1-c) for all w != 0 with |W_x| < 2h^(1+a) and |W_y| < 3h.
Then for non-collinear options in different slots,
 codeg_F(o, o') <= 4 Delta_Z (C_eps h^(1-a/2+eps) + C h^(1-c)),
and in a block with n >= rho Delta_Z h,
 T(o) <= D(o)^2 h^(-min(c, a/2 - eps))/rho.
The averaged form suffices for T(o) alone.
 (MT_avg): Sigma_mod(tau) := #{(z1, z2) : z1, z2, z2 - z1 + (0, tau) in P_h, |X1|, |X2| < 2h^(1+a)} <= C h^(2-c), uniformly in |tau| <= 2h.
Under (MT_avg), T(o) <= 8 Delta_Z^2 h^(2-c) <= D^2 h^(-c)/rho^2. In Theorem E main classes, rho >= Lambda^(-10)/C.

THE TARGET D^2 h^(-c) IS NOT PROVED. It is equivalent, within this method, to (MT). (MT) is a statement about lattice points at integral distance from both 0 and w inside a disc of radius about h^(1+a). That is the "round integral triangle" problem.

## Proofs

0. Conventions. S(y) = {X != 0 : X^2 + y^2 = square}. Each X in S(y) comes from a factorization y^2 = (L - |X|)(L + |X|) together with a sign, so |S(y)| <= tau(y^2). Likewise S'(X) = {y != 0 : X^2 + y^2 = square} has |S'(X)| <= tau(X^2).

1. LEMMA 1.
- Let o2 = (g, j2) be H_F-adjacent to o in parity pi02 and to o' in parity pi12.
- Put z2 = (7(j2 - j0), rho_pi02(g) - rho_pi02(e)) and z' = (7(j2 - j1), rho_pi12(g) - rho_pi12(f)). By Proposition 2, both lie in P_h, because all rows are in [5000, h-5000], so every |y| < h.
- The columns are consistent: 7(j2 - j1) = 7(j2 - j0) - 7(j1 - j0).
- For the rows, write rho_even = rho_odd + T. Then
 z' = z2 - z1 + (0, tau), tau = [rho_pi12(g) - rho_pi02(g)] - [rho_pi12(f) - a_f] + [rho_pi02(e) - a_e].
 Each bracket is 0 or ±(the label's diagonal), so |tau| <= 2h.
- Fix (pi02, pi12, T_g). Then z2 determines j2 and rho_pi02(g), and with T_g it determines g. So o2 -> z2 is injective into {z in P_h : z - w in P_h} with w = z1 - (0, tau). Also w != 0, because its first coordinate is 7(j1 - j0) != 0.
- Summing over the 4 parity pairs and the Delta_Z diagonals gives the codegree bound.
- Every triangle at o is counted in sum over o1 of codeg(o, o1).

2. LEMMA 2.
- From L^2 - X^2 = y^2 we get (L - |X|)(L + |X|) = y^2, so delta = L - |X| >= 1 and delta divides y^2.
- delta^2 < delta(L + |X|) = y^2, so delta < |y|. And |X| = (y^2/delta - delta)/2.
- delta | y^2 holds if and only if delta* | y, because v_p(y) >= ceil(v_p(delta)/2) for every p, and delta* = prod p^ceil(v_p/2) = kappa mu.
- With y = kappa mu u we get y^2/delta = kappa u^2, and so X = sigma kappa (u^2 - mu^2)/2.
- Finally delta = y^2/(L + |X|) < y^2/(2|X|).

3. THEOREM A.
(i) The flat side. Let z = (X, y) and z' = z - w = (X', y'), with X - X' = W_x. Let m = max(|X|, |X'|) >= h^(1+a)/2.
- Case 1: |X| = m. Then delta(z) < y^2/(2|X|) <= h^2/h^(1+a) = h^(1-a).
- Case 2: |X'| = m. Then z' is flat with delta(z') < h^(1-a), and z = z' + w. This is Case 1 with w replaced by -w and the roles swapped.
- So it suffices to bound, for fixed sigma and fixed delta < Delta := h^(1-a), the number of u with z(u) - w in P_h.
- Here z(u) = (sigma kappa (u^2 - mu^2)/2, kappa mu u), and |u| <= U := max(1, h/delta*).

(ii) The curve. Put A(u) = sigma kappa (u^2 - mu^2)/2 - W_x and B(u) = kappa mu u - W_y. The condition says 4G(u) := (2A)^2 + (2B)^2 = v^2 with v = 2|z - w| an integer. So
 F(u, v) = v^2 - 4G(u) is in Z[u, v],
 4G has degree 4, with leading coefficient kappa^2 != 0.

(iii) Absolute irreducibility. v^2 - 4G is reducible over C only if 4G is a square in C[u]. Over C every constant is a square, so this means every root of G has even multiplicity. Now 4G = 4(A + iB)(A - iB), with A and B real.
- The discriminant of A + iB = (sigma kappa/2)u^2 + i kappa mu u + (-sigma kappa mu^2/2 - W_x - iW_y) is
 -kappa^2 mu^2 + 4(sigma kappa/2)(sigma kappa mu^2/2 + W_x + iW_y) = 2 sigma kappa (W_x + iW_y).
 It is nonzero because w != 0. So A + iB has distinct roots r1 and r2, and A - iB has the roots conj(r1) and conj(r2).
- All four multiplicities can be even in only two ways:
 - r1 and r2 both real. Then B vanishes at two distinct points, but B is linear with B != 0.
 - r2 = conj(r1). Then A + iB is a real multiple of a real quadratic, which forces B = 0.
 Both are impossible. So F is absolutely irreducible of degree 4. Its homogenization F(s, u, v) = v^2 s^2 - 4 s^4 G(u/s) is an absolutely irreducible ternary quartic form.

(iv) Heath-Brown's Theorem 15. Each u gives the primitive zero (1, u, v). Use the box |s| <= 1, |u| <= U and |v| <= V. Here V <= 2(|X| + |W_x| + 2h) is a polynomial in h, because |X|, |W_x| < h^2.
- The monomials u^4 (coefficient kappa^2) and v^2 s^2 occur, so T >= max(U^4, V^2).
- If U <= V, then exp(log U log V / log T) <= exp(log U log V / (2 log V)) = U^(1/2).
- If V < U, then T >= U^4 gives exp(log V log U / (4 log U)) = V^(1/4) <= U^(1/2).
- In both cases the number of u is << h^eps U^(1/2). The hypothesis T >= (P1 P2)^d = P2^4, needed in the Browning-Heath-Brown form, holds in both cases.

(v) Summation. Write delta = kappa mu^2. Then
 sum over delta < Delta of (delta*)^(-1/2) <= sum over mu of mu^(-1/2) * 2(Delta/mu^2)^(1/2) = 2 zeta(3/2) Delta^(1/2).
So
 I_flat(w) <= 4 C_eps h^eps sum over delta < Delta of ((h/delta*)^(1/2) + 1) << h^eps (h^(1/2) Delta^(1/2) + Delta) << h^(1 - a/2 + eps).
The factor 4 counts the two cases and the two signs sigma.

4. LEMMA 3.
- For |X| < 2h^(1+a): L + |X| <= 2|X| + |y| < 5h^(1+a), so delta > y^2/(5h^(1+a)). Hence |y| < min(h, (5h^(1+a) delta)^(1/2)), with delta* | y.
- Counting signs of X and y:
 # <= 4 sum over delta < h of 2 min(h, (5h^(1+a) delta)^(1/2))/delta*.
- First, for delta >= Z1 := h^(1-a)/5, use the bound h. Here
 sum over delta < Z of 1/delta* = sum over mu of mu^(-1) ((6/pi^2) log(Z/mu^2) + O(1)) = (3/(2 pi^2)) (log Z)^2 + O(log Z).
 This uses sum over squarefree kappa <= x of 1/kappa = (6/pi^2) log x + O(1). So the range Z1 <= delta < h contributes at most
 8h (3/(2 pi^2)) ((log h)^2 - (log Z1)^2) + O(h Lambda) <= (24/pi^2) a h Lambda^2 + O(h Lambda).
- Second, for delta < Z1, (delta^(1/2))/delta* = kappa^(-1/2), and sum over kappa mu^2 < Z of kappa^(-1/2) <= 2 Z^(1/2)(1 + log Z^(1/2)). This part is at most 8 sqrt5 h^((1+a)/2) * 2 Z1^(1/2) Lambda <= C h Lambda.
- The bound for |P_h| is the same computation with every delta < h.

5. THEOREM B.
(B1) Split the z counted by I(w) into two sets:
- those where z or z - w has |X| >= h^(1+a)/2, at most C_eps h^(1-a/2+eps) by Theorem A;
- those where both are moderate, at most I_mod(w), which is at most #moderate P_h (Lemma 3).
Then apply Lemma 1. If |W_x| >= h^(1+a), one of |X_z| and |X_z - W_x| is >= h^(1+a)/2, so the second set is empty.
(B2) Take o'' = (g, j0), H_F-adjacent to o' at column offset X = 7(j0 - j1) != 0. Then rho_pi(g) - rho_pi(f) lies in S'(X), which has at most tau(X^2) elements. Each (pi, T_g, row) gives at most one label. So there are at most 2 Delta_Z tau(X^2) such o'', and the same number in slot j1. Finally tau(X^2) <= h^(O(1/loglog h)), because X < h^2.
(B3) This is Theorem C (C1) and Proposition 2 of pair_families_dp_colouring.md.

6. THEOREM C.
- The column offsets satisfy X' = X2 - X1 exactly. Let M = max(|X1|, |X2|, |X'|). The largest of the three is at most the sum of the other two, so the second largest is at least M/2.
- If M >= 2h^(1+a), at least two of the three edges have |X| >= h^(1+a), and one of these two edges is at o, say o-o1. Then max(|X2|, |X2 - X1|) >= |X1|/2 >= h^(1+a)/2, so o2 is counted by 4 Delta_Z I_flat(w) (Lemma 1 and Theorem A). Summing over o1 in N_F(o) gives the first term.
- If M < 2h^(1+a), then both o1 and o2 lie in N_mod(o). These triangles number at most D_mod(o)^2/2.
- D_mod(o) <= 2 Delta_Z #moderate P_h: there are 2 parities, Delta_Z diagonals, and z determines the label (Lemma 1's injectivity argument).
- Coincidence-mixed triangles at o number sum over j of nu_j^2 <= D_F(o) max nu_j, where nu_j = #{f : (f, j) ~_F o} <= 2 Delta_Z tau(X_j^2), as in (B2).

7. COROLLARY C'.
- D_F(o) <= 2 Delta_Z |P_h| <= C B.
- Insert Lemma 3 into Theorem C:
 (1/2) D_mod^2 <= C Delta_Z^2 h^2 (a Lambda^2 + Lambda)^2 <= C B^2 (a^2 + Lambda^(-2)),
 and the first term is <= C_eps B^2 Lambda^(-2) h^(-a/2+eps).
- For fixed a, take eps = a/4. Then limsup T(o)/B^2 <= C a^2 for every a > 0, so T(o) = o(B^2).
- The flat part: T_flat <= 4 C_eps Delta_Z h^(1-a/2+eps) D, and Delta_Z h <= (n - 1)/rho * (1 + o(1)) <= D/rho * (1 + o(1)).

8. CONDITIONAL THEOREM D.
- By (B1) with (MT_pt), the codegree of a non-collinear pair is at most 4 Delta_Z (C_eps h^(1-a/2+eps) + C h^(1-c)).
- Then T(o) <= D_F(o) * max codeg <= D * 4 Delta_Z * C h^(1 - min(c, a/2 - eps)), and Delta_Z h <= C D/rho.
- Under (MT_avg): T_mod(o) <= sum over (pi01, pi02, pi12, T_f, T_g) of sum over z1 moderate of I_mod(z1 - (0, tau)) <= 8 Delta_Z^2 max over tau of Sigma_mod(tau).

## External results used

- Heath-Brown, 'The density of rational points on curves and surfaces', Ann. of Math. 155 (2002), Theorem 15, in the form restated by Browning and Heath-Brown, 'Plane curves in boxes and equal sums of two powers', Math. Z. 251 (2005), arXiv math/0506497 (read on ar5iv). Hypotheses in my words: F is in Z[x1, x2, x3], an absolutely irreducible form of degree d. Count primitive integer zeros with |x1| <= 1, |x2| <= P2, |x3| <= P3, where 1 <= P2 <= P3. T is the largest value of 1^e1 P2^e2 P3^e3 over the monomials x1^e1 x2^e2 x3^e3 that occur in F with nonzero coefficient. Conclusion: the count is << P3^eps exp(log P2 log P3 / log T), with the constant depending on d and eps. The same formula is Browning-Heath-Brown Theorem 1 with P1 = 1, under its hypothesis T >= (P1 P2)^d. Used in Theorem A with d = 4 and T >= P2^4.
- Heath-Brown (2002), Corollary 2, read verbatim on ar5iv of arXiv math/0405392. Let q be an integral ternary quadratic form with matrix M, Delta = |det M| != 0, and Delta0 the highest common factor of the 2x2 minors of M. Then the number of primitive zeros in |x_i| <= R_i is <<_eps {1 + (R1 R2 R3 Delta0^2/Delta)^(1/3+eps)} d3(Delta). I used it only to explain why the conic route fails: the '1 +' term per conic.
- Goenka, Moore, White, arXiv 2304.03920, Lemma 3.1, read through a summary of the HTML. The number of non-congruent lattice triangles with a given perimeter p is O(p^(1+O(1/loglog p))). Cited only to show that the published bounds give X^(2+o(1)) lattice Heronian triangles with sides <= X, which is not enough for (MT).
- Elementary inputs:
  - tau(n) <= exp(C log n / loglog n);
  - sum over squarefree kappa <= x of 1/kappa = (6/pi^2) log x + O(1);
  - sum over kappa <= x of kappa^(-1/2) <= 2 sqrt x, and zeta(3/2) < 2.62;
  - the factorization of Pythagorean triples, L^2 - X^2 = y^2.
- Internal notes:
  - pair_families_dp_colouring.md: Proposition 2 (lines; the necessary condition z in P_h), Theorem C (C1), and Proposition 1(c);
  - relocation_price_floor.md: Lemma F;
  - safe_triangle_pair_first_moment.md Section 1: bulk rows in [5000, h-5000], and labels f_{T,i} determined by (T, row).

## Checks

I re-derived by hand:
- Lemma 1, including the formula for tau and the injectivity o2 -> z2;
- the parabola parametrization (delta* = kappa mu, delta | y^2 iff delta* | y);
- the discriminant 2 sigma kappa (W_x + iW_y) of A + iB, and the root-multiplicity case analysis for absolute irreducibility;
- the Heath-Brown Theorem 15 exponent computation in both orderings of (U, V);
- sum over delta < Delta of (delta*)^(-1/2) <= 2 zeta(3/2) Delta^(1/2);
- sum over delta < Z of 1/delta* = (3/(2 pi^2))(log Z)^2 + O(log Z), and the Lemma 3 split;
- the second-largest-offset argument in Theorem C;
- (B2).

Web, used only to read the theorems I cite:
- Heath-Brown, arXiv math/0405392, read on ar5iv: Corollary 2 verbatim, and Theorem 3 with the definitions of T and V. Theorem 15 is not in the arXiv numbering, and the PDF was password-protected.
- Browning-Heath-Brown, arXiv math/0506497, read on ar5iv: Theorem 1, and the restatement of Heath-Brown Theorem 15 for P1 = 1.
- Goenka-Moore-White, arXiv 2304.03920: a summary of Lemma 3.1 and Proposition 3.2.
No paper or paper text was saved.

Numerics, run as sanity checks only. Each script used py, ran in under 20 s and well under 1 GB. The scripts are in scripts_triangles/: tri_count.py, tri_structure.py, tri_focal.py, tri_sample.py.

(1) Sigma(0) = #{(z1, z2) in P_h^2 : z2 - z1 in P_h, non-collinear}, exact, both orientations. Lambda = ln h.

| h | Sigma(0) | Sigma/h^2 | Sigma/(h Lambda^4) | share with an edge |X| >= h^1.25 |
| --- | --- | --- | --- | --- |
| 100 | 7728 | 0.77 | 0.17 | 12% |
| 200 | 36816 | 0.92 | 0.23 | 11% |
| 400 | 152112 | 0.95 | 0.30 | 9% |
| 600 | 329568 | 0.92 | 0.33 | 8.6% |
| 800 | 567840 | 0.89 | 0.36 | 8.3% |

The local exponent is 2.05 from 200 to 400 and 1.90 from 400 to 800, and it is falling. |P_h|^2/Sigma takes the values 228, 314, 474, 616 and 749 at h = 100, 200, 400, 600 and 800. For tau in {14, 84, h/2} the counts have the same order.

(2) Sampled I(w) means, 150 random w per class. "Moderate" means |W_x| <= h; "flat" means |W_x| >= h^1.5.

| h | moderate mean | moderate mean * Lambda^2/h | moderate max | flat mean | flat max |
| --- | --- | --- | --- | --- | --- |
| 200 | 19.8 | 2.78 | 58 | 0.23 | 4 |
| 400 | 35.7 | 3.20 | 86 | 0.31 | 4 |
| 800 | 61.6 | 3.44 | 176 | 0.23 | 8 |
| 1600 | 83.9 | 2.85 | 270 | 0.36 | 8 |
| 3200 | 124.9 | 2.54 | 356 | 0.39 | 6 |

So flat focal vectors have I(w) = O(1) in practice, far below Theorem A's h^(1 - a/2). Moderate ones carry almost all triangles, which confirms that (MT) is the crux. The moderate mean grows like Lambda^3.5 to Lambda^4, or like h^0.5. The data cannot separate these.

(3) Structure of the solutions (tri_focal.py). They come in pairs under z -> w - z. Many lie on lines through 0 in short Pythagorean directions, such as 21(4,-3), 35(4,3) and 111(4,3). Primitive triangles of vertical extent in [2^k, 2^(k+1)) number 156, 840, 3804 and 8100 for k = 4 to 7.

The repository was only read. No git command was run, and no file was written outside the script folder.

## Gaps

- The target T(o) <= D^2 h^(-c) is NOT proved. It holds for triangles that have one flat edge (Theorem A, Theorem C). The remaining triangles are the round ones: all three edges have |X| < 2h^(1+a) and |y| < h, so every slope lies within about h^(+-a). These carry a fraction of the degree of about 2a (Lemma 3), which is not power-small. Bounding them is exactly (MT_pt) or (MT_avg).
- (MT) is a two-point integral-distance problem: lattice points z with |z| <= R = 3h^(1+a) and both |z| and |z - w| integral. We need at most R^(1-c') of them, pointwise or on average over w in P_h. Every tool I tried fails here, each for a different reason.
  - Confocal hyperbolas give up to h^(o(1)) points on each of 2|w| conics, so the bound is |w| h^(o(1)), trivial for |w| about h.
  - Fixing the parabola parameter delta and applying Heath-Brown Theorem 15 gives U^(1/2) per curve. That saves nothing for the about h parabolas holding O(1) points each, which are the round vectors.
  - Heath-Brown Corollary 2 on the conic Q(t1, t3) = c^2 for a fixed pair of directions has a '1 +' term for each direction pair. Summed over the about h^2 pairs, that is trivial.
  - The Heronian reduction needs a power saving for lattice Heronian triangles with sides <= X. The only published count I found (Goenka-Moore-White, arXiv 2304.03920, Lemma 3.1, read through a summary) gives p^(1+o(1)) per perimeter, hence X^(2+o(1)). That is not enough.
- Heath-Brown's Theorem 15 is used in the form restated by Browning and Heath-Brown, Math. Z. 2005 (arXiv math/0506497), read on ar5iv. Heath-Brown's own PDF was password-protected in this environment, so I could not read the original statement. Our application satisfies T >= P2^4 = (P1 P2)^d, which is the hypothesis of Browning-Heath-Brown Theorem 1 with P1 = 1. That theorem gives the same formula, so either version suffices. I did not check how the implied constant depends on d and eps beyond 'depends on d and eps'.
- Corollary C' (T = o(B^2)) is only qualitative. The h^eps of the determinant method blocks taking a of order loglog h/log h. Turning o(B^2) into o(D^2) needs D(o) >= c0 B. That holds only in row-dense blocks (n >= rho Delta_Z h with rho constant), not in sparse T1 weight classes, where n/(Delta_Z h) can be as small as Lambda^(-10).
- Only the necessary condition z in P_h of Lemma F is used: no mod-7 slot condition, no parity of t, no label-row density. So every bound is uniform over label sets but does not exploit them. The other T2 pair families (rivals, two-sea supports R1 and R2, sea triangles) are not in H_F. Their codegrees and their mixed triangles with H_F are not analysed.
- The numerics cannot separate Sigma(0) of order h Lambda^C from h^(2-c), or a polylog from a small power for the moderate mean of I(w). The largest sampled moderate I(w) grows roughly like h^0.65 from h = 200 to 3200, over 150 samples per h. That is below the h^(1-c) that (MT_pt) needs, but it is not evidence of a uniform bound.
- Nothing here is audited.

## Missing estimate

(MT), the round-triangle estimate. For some a, c > 0, uniformly in w != 0 with |W_x| < 2h^(1+a) and |W_y| < 3h:
 #{z in Z^2 : 0 < |y_z|, |y_z - W_y| < h; 0 < |X_z|, |X_z - W_x| < 2h^(1+a); |z| and |z - w| integers} <= C h^(1-c).
This is the pointwise form, needed for codegrees. For the triangle count T(o) alone, the averaged form suffices:
 #{(z1, z2) : z1, z2, z2 - z1 + (0, tau) all of integral length, with these box constraints} <= C h^(2-c), uniformly in |tau| <= 2h.
In the case tau = 0, this is a power-saving count of lattice triangles with integral sides, one vertex at the origin, and diameter at most about h^(1+a), against the trivial h^(2+o(1)). Equivalently, by Heron's formula, it is a count of integral points on (x+y+z)xyz = square, a singular del Pezzo double plane, in a box. Combined with Theorem A, (MT) yields the target: T(o) <= D^2 h^(-min(c, a/2-eps))/rho, and non-collinear codegree <= D h^(-min(c, a/2-eps))/rho.

## Next steps

- Audit Theorem A. The critical steps are the discriminant 2 sigma kappa (W_x + iW_y), the absolute-irreducibility case analysis, and the Theorem 15 exponent in both orderings. Have someone with access to Heath-Brown 2002 confirm the exact hypotheses of Theorem 15. If they differ, the fallback is Browning-Heath-Brown Theorem 1 with P1 = 1, whose hypothesis T >= P2^d we satisfy.
- Attack (MT_avg) at tau = 0 through Heron's formula. Count integral points of (x+y+z)xyz = W^2 with x, y, z <= X, and look for any power saving over X^2. Two routes: an upper-bound version of Manin-type counting for this singular degree-2 del Pezzo surface (with 6 A1 points), or a conic-bundle count that averages Pell solution counts over the discriminant. Check the literature for upper bounds for this specific surface.
- Repeat the numerics in C at h up to 10^4 or more: Sigma(0), the moderate mean and max of I(w), restricted to round w. This should decide whether the local exponent of Sigma tends to 1 (polylog codegree, consistent with (MT)) or stays near 2 - c. If Sigma is of order h^2/Lambda^C, then (MT_avg) is false. In that case the cross-direction triangles are only polylog-sparse, and a line-nibble can save at most a power of Lambda.
- If (MT) stalls, check what a nibble actually needs. It may tolerate T(o) <= D^2/Lambda^C: compare the Lambda^(-C) density against lambda = D/N being about ln N. Theorem C already gives T <= C a^2 B^2 + o(B^2). A Lambda-power version would need a determinant-method bound without the h^eps loss.
- Add the other T2 pair families (rivals, two-sea R1 and R2) to the codegree analysis. Prove the class-restricted version, using actual label rows rather than all rows, so that the results apply to sparse weight classes with rho < 1.

