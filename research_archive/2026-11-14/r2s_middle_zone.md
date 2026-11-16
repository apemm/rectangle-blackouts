# R2s multiplicity in the middle zone

15 November 2026. Problem 001. Continues continuation_gap_mixing_audit.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (partial): the middle zone is not settled, with neither a bound of M - 1 nor a construction. New: an exact identity for any two solutions on one curve, a proof that same-arc doubles have no polynomial family other than the +-V partner, and a reduction of heavy pairs, free of Hilbert geometry, to counting row doubles. Not audited yet.

# Result

## Status

partial

## Summary

R2s middle zone not settled: neither a bound of M - 1 nor a construction. Three new results: an exact identity for any two solutions on one curve; a proof that same-arc doubles have no polynomial family other than the ±V partner; and a Hilbert-free reduction of heavy pairs to counting row doubles.

## Statements

Setting: design H7, sigma a power of 2, S = 6272 sigma. A curve is one label pair, one role, one side owner and one sea s. It fixes m and delta != 0, with N = delta(2m - delta) != 0 and K = 2 m delta = N + delta^2. As in Theorem A of hilbert_residual_families.md, a solution of the curve is a signed divisor g = V - U of N for which D := N/g - g = 2U is nonzero and divides K. Its column offset is X = -(g + K/D)/2. A constraint is a solution with X in the pair's window that passes the archive tests: S | X, the Hil forms, sea types, strip, and e1, e2 != 0.

THEOREM 1 (two-solution identity; proved). Take two solutions g1 != g2 of one curve. Put u = g2 - g1, J = X1 - X2, G = g1 g2 and r = N/G. Then
 (I1) 2J = u [1 + K(N + G) / ((N - G)^2 - N u^2)],
or equivalently
 (I2) N Q(r) = u r (L r - delta^2), with L = u^2 - 2uJ - delta^2 and Q(r) = u(2r^2 - r + 1) - 2J(r - 1)^2.
Also J - u = u [delta^2(1 + 1/r) + G(3 - 1/r) + u^2] / (2[N(1 - 1/r)^2 - u^2]).

COROLLARY 1a (same arc; proved). If both solutions lie on one arc of the map g -> X, then |u| <= 2|J| when N > 0 and |u| <= (16/7)|J| when N < 0. In a window of the H7 board, |J| <= 2(M-1)S.

COROLLARY 1b (deep inner arc; proved, given the lattice fact 14 | g). Take N > 0 and two constraints on the inner arc in one window with (N - G)^2 > N u^2. Then J != u and J - u lies in 14Z. Hence 28[(N - G)^2/N - u^2] <= |u|(2 delta^2 + 3G + u^2). This is a self-contained proof of the order of Theorem 2's inner small-|X| zone. It does not enlarge that zone.

THEOREM 2 (no polynomial families of same-arc doubles; proved). Fix delta != 0 and J. Let g1(t), g2(t), N(t) be polynomials in Q[t], with N non-constant and g1 != g2. Suppose that for infinitely many integers t the values are two solutions of the curve (N(t), delta) with X1 - X2 = J. Suppose also that u(t) = g2 - g1 is bounded on that set, which holds automatically when the two solutions are on one arc (Corollary 1a). Then r = N/(g1 g2) is identically -1 and J = u/2. In that case the two solutions are (U, V) and (U, -V), the ±V partners of Theorem 1(a) of r2s_single_pair_multiplicity.md, which Theorem 1(c) there excludes in-window for 2 <= M <= 2731 sigma^3 (unaudited). So no polynomial or Gaussian-integer family, of any degree, gives two distinct |U| on one arc of one curve in one window.

LEMMA 3 (heavy pairs reduce to Hilbert-free row doubles; proved). Fix a role rho, a row y of that parity in a block, an offset delta in 28Z \ {0} and a rank gap D0 != 0. Call (y, delta, D0) a rho-double if the curves of the row pair (y, y + delta) (both side owners, all live seas) together give at least ceil(M/2) distinct constraint values in the window S[M D0 - (M-1), M D0 + (M-1)]. This is a Hilbert-free condition. Then:
 (a) if a pair (e, f) carries at least M distinct R2s constraints, then for some role rho, (row_rho(e), delta_rho, r_f - r_e) is a rho-double;
 (b) every label e lies in at most A2^odd(a_e) + A2^even(b_e) such heavy pairs. Here A2^rho(y) counts the triples (delta, D0, direction) with a rho-double at row y as first row (partner at rank r_e + D0) or as second row (partner at rank r_e - D0).
So the heavy-pair graph of a block has degeneracy D_B <= max_y A2^odd(y) + max_y A2^even(y). This bound depends only on rows and needs no Hilbert input.

NOT PROVED: a bound of M - 1 on distinct R2s constraints per pair, or any tau-free per-pair bound below the trivial 2M - 1. Also not proved: Theorem 2 when u is unbounded (doubles on two different arcs, or on two different curves of one row system). No label pair with more than M - 1 R2s constraints was constructed.

## Proofs

CONVENTIONS. Theorem A of hilbert_residual_families.md (audited) gives the solutions: g1 g2 = N with g1 = g2 (mod 2), U = (g2 - g1)/2, V = (g1 + g2)/2, T = -2 m delta/(g2 - g1) and X = (T - g1)/2. With g = g1 and D = g2 - g1 = 2U, we get T = -K/D and X = -(g + K/D)/2. Also U | m delta is equivalent to D | K. check_identity.py confirms symbolically that this X equals (U + T - V)/2.

PROOF OF THEOREM 1.
- Write D_i = (N - g_i^2)/g_i. Then K/D_i = K g_i/(N - g_i^2), so -2X_i = g_i + K g_i/(N - g_i^2).
- Hence 2J = 2X1 - 2X2 = u + K[g2(N - g1^2) - g1(N - g2^2)] / ((N - g1^2)(N - g2^2)).
- The bracket equals (g2 - g1)(N + g1 g2) = u(N + G).
- The denominator equals N^2 - N(g1^2 + g2^2) + G^2. Since g1^2 + g2^2 = u^2 + 2G, this is (N - G)^2 - N u^2. That gives (I1).
- For the J - u form, subtract u from (I1) and use K(N + G) - (N - G)^2 = 3NG - G^2 + delta^2(N + G). Then divide the numerator and denominator by N, with G/N = 1/r.
- (I2) is the same identity cleared of denominators. check_identity.py verifies both forms symbolically, and verifies (I2) numerically on 17 random curves that have two integer-X factorizations.

PROOF OF COROLLARY 1a. Write R(g) = T = Kg/(g^2 - N). Then F(g) := X = (R(g) - g)/2 and F' = (R' - 1)/2, with R' = -K(g^2 + N)/(g^2 - N)^2.
- N > 0. Then K > 0 and R' < 0, so |F'| > 1/2 on every arc.
- N < 0. Then K < 0 and R' = |K|(g^2 - |N|)/(g^2 + |N|)^2 <= |K|/(8|N|). The maximum is at g^2 = 3|N|. Since |K| < |N| (K/N lies in (0,1)), R' < 1/8 and |F'| > 7/16.
- Apply the mean value theorem on the arc.

PROOF OF COROLLARY 1b.
- On the inner arc, |g_i| < sqrt N and the g_i have one sign, so G > 0 and r > 1. The numerator bracket of J - u is then positive. With (N - G)^2 > N u^2, the denominator is positive too, so J - u is nonzero with the sign of u.
- J lies in SZ, and 14 | S. By the lattice fact 14 | g (r2s note: T is even, 7 | X and 7 | delta), u lies in 14Z. So |J - u| >= 14.
- Insert this into the formula, using 1/r < 1.

PROOF OF THEOREM 2.
- Step 0. u is a polynomial bounded on an infinite set of integers, so u is a nonzero constant. Both sides of (I2) are rational functions of t that agree at infinitely many t, so (I2) holds in Q(t). Put G = g1(g1 + u). It is a nonzero polynomial, and r = N/G lies in Q(t). Integrality: h1 = N/g1 = r g2 and h2 = N/g2 = r g1 are integers at every t in the set. Below, ∂ denotes the degree at infinity of a rational function (degree of numerator minus degree of denominator).
- Case (i): r is constant, r0. Then N Q(r0) = u r0 (L r0 - delta^2) has a non-constant left side unless Q(r0) = 0. So Q(r0) = 0 and L r0 = delta^2.
  - Solving Q(r0) = 0 for J and substituting gives L r0 - delta^2 = -(r0 + 1)[delta^2 (r0 - 1)^2 + u^2 r0^2]/(r0 - 1)^2 (check_identity.py; Q(1) = 2u != 0). The bracket is positive, so r0 = -1.
  - Then Q(-1) = 4u - 8J = 0, so J = u/2. Also N = -g1 g2, so h1 = -g2 and h2 = -g1. This gives U1 = -(g1 + g2)/2 = U2 and V1 = (g1 - g2)/2 = -V2, the ±V partner.
- Case (ii): r is non-constant. From (I2), G = u(L r - delta^2)/Q(r) and N = rG.
  - (ii-a) ∂r > 0.
    - If u != J, then Q(r) has degree 2∂r (its leading coefficient is 2(u - J) != 0), and L r - delta^2 has degree at most ∂r. So ∂G < 0, which is impossible for a nonzero polynomial.
    - If u = J, then Q = u(3r - 1) and L = -(u^2 + delta^2). So G = -(u^2 + delta^2)/3 - (u^2 + 4 delta^2)/(3(3r - 1)). The last term is a nonzero rational function of negative degree, so G is not a polynomial.
  - (ii-b) ∂r < 0, so r -> 0. Then L r - delta^2 -> -delta^2.
    - If u != 2J, then Q(r) -> u - 2J != 0. So G is bounded, hence constant, and ∂N = ∂r < 0. That contradicts N being a non-constant polynomial.
    - If u = 2J, then Q = u r(r + 1). So N = (L r - delta^2)/(r + 1) -> -delta^2 is bounded, hence constant. Contradiction.
  - (ii-c) ∂r = 0, with r -> r_inf != 0. Here r_inf = alpha/beta is rational.
    - If Q(r_inf) != 0, then N = u r(L r - delta^2)/Q(r) is bounded, so it is constant. Contradiction. So Q(r_inf) = 0. If g1 were constant, then G and hence N = rG would be bounded. So |g1(t)| -> infinity.
    - Simple root (this includes the case u = J, where Q is linear with Q' = 3u). Put eps = r - r_inf. (I2) gives eps = O(1/|N|). Since g2 = N/(r g1), we get eps g2 = O(1/|r g1|) -> 0. The integer beta h1 - alpha g2 = beta g2 eps tends to 0, so it vanishes for all large t in the set. Then h1 = r_inf g2 identically, which forces r = r_inf, a contradiction.
    - Double root. The discriminant u(16J - 7u) is 0, so J = 7u/16, r_inf = -1/3 and Q = (9u/8)(r + 1/3)^2. With w = 3r + 1 -> 0, we have G = 8(L r - delta^2)/w^2, and L r_inf - delta^2 = -u^2/24 - 2 delta^2/3 != 0. So w^2 G tends to a nonzero constant. The integers 3h1 + g2 = w g2 and 3h2 + g1 = w g1 are values of rational functions with finite nonzero limits. They are therefore eventually constant, so they are constant identically. Then g1/g2 is constant with g2 = g1 + u, so g1 is constant. Contradiction.
- All cases end in the ±V partner. ∎

PROOF OF LEMMA 3.
- Every archive test of an R2s constraint depends only on the curve (role rows, delta, s, side owner) and on X: S | X, weak Hil, the M-dependent Hil form, types, strip, and e1, e2 != 0. Window membership depends on M dr. Hilbert locality is a property of an actual pair and holds automatically. So the constraints of (e, f) in role rho are a function of (row_rho(e), row_rho(f), r_f - r_e) alone. This is the basis of Theorem D.
- (a) The two roles share the at least M distinct values, so one role carries at least ceil(M/2) of them.
- (b) Given e and a rho-double with e's row as first row, f must be the label of rank r_e + D0. That rank is unique because Hilbert ranks are a bijection on the padded square. As second row, f is the label of rank r_e - D0. So each counted triple gives at most one heavy partner. A graph of maximum degree D has degeneracy at most D. ∎

WHAT THIS SETTLES AND WHAT IT DOES NOT.
- Same-arc doubles. Two distinct |U| on one arc of one curve in one window can only be sporadic integer points: Theorem 2 excludes every polynomial or Gaussian-integer family. This decides, negatively, the archive's next step "look for polynomial families with two solutions on one curve" for same-arc doubles at fixed delta. I also derived by hand an identity for the classical rho = 2 configuration (N = 2 g1 g2, family A below). It satisfies (I2) at r = 2 with Q(2) = 7u - 2J.
- Family A. In it, two solutions with X-difference J satisfy 7t + e = 2J, where t = g2 - g1 and e = Q/D - Q/(D+3t) is a difference of codivisors of Q = 4t^2 + delta^2. So at M = 3 it forces |t| <= 7168 and is a finite list. I did not enumerate it, because the brief limits computation to checks.
- Per-pair bound. A per-pair bound of M - 1 does not follow from per-curve or per-arc arguments. A pair has two independent row systems (odd and even), and each has up to 4 live curves and up to 3 arcs per curve. Any tau-free per-arc bound c gives at most 24c per pair, which is never below the trivial 2M - 1.
- Construction. A pair with at least 3 constraints at M = 3 needs, by Lemma 3(a), a row-system double. That double must be a sporadic same-arc double (no family, by Theorem 2), a cross-arc double, or two curves of one row system hitting one window. None is known. The archive census found no same-curve double for |X| <= 1500 S.

HEURISTIC (labelled; not proved). This assumes values of the (X,Y) form phi_delta(X,Y) = (X - Y)((X + Y)^2 + delta^2)/Y are equidistributed. The probability that a curve with one admissible constraint at X has a second admissible point at a fixed offset J is about Y^2/|X|^3 per admissible Y. Summed over X in SZ, that is about (tau_bar/S) log(X_max) per (delta, J), before the residue and type filters. The expected total number of same-curve doubles therefore grows at most like log h, with a small constant. Once a rho-double exists at a row y, the Hilbert freedom in the other coordinate typically realizes it on many label pairs of that row. Order Q kappa/sqrt(D0) is a heuristic count, not proved. So heavy pairs, if they exist, would concentrate on a few rows, and Lemma 3(b) bounds their degree by the row counts A2.

## External results used

- None. No published theorem was used, and no web source was consulted.
- Internal and audited: Theorem A, the exact form of R2s (hilbert_residual_families.md); Theorem D, row-only dependence of R2s arithmetic.
- Internal and unaudited: the lattice fact 14 | g, and Theorem 1(c) (±V partner excluded in-window for 2 <= M <= 2731 sigma^3) of r2s_single_pair_multiplicity.md; H7 tools (Al), (Bulk), (Hil) and the M-dependent Hil form.

## Checks

Script folder: scripts_gm2_r2s_middle/ (under 50 KB). All scripts use relative paths and were run with py.
- check_identity.py (under 10 s): verifies symbolically that (I2) holds identically, that X = -(g + K/D)/2 agrees with Theorem A's (U + T - V)/2, and the factorization L r0 - delta^2 = -(r0+1)[delta^2 (r0-1)^2 + u^2 r0^2]/(r0-1)^2 at Q(r0) = 0. It also checks (I2) numerically on 17 random curves (delta in 28Z, |m| in [1e5, 1e7]) that have two integer-X factorizations, with no failures.
- check_ju.py (under 5 s): verifies the closed form of J - u symbolically.
- star.py (under 5 s): the (a,b,c,d) form of the window equation, (abcd + delta^2)(c - b)(a + d) = (cd - ab)(bd - ac)(2J - a(c - b)). With c = b + t it factors as bc q(d) = t(L d - a delta^2), where q(d) = u(2d^2 - ad + a^2) - 2J(d - a)^2 and u = at. This is (I2) with r = d/a.
- lines.py first stage and lines2.py (under 50 s): the coefficient conditions for lines on the two-point surface. These were exploratory only and support no claim.
- lines.py second stage: stopped after it ran past 60 s (see gaps).
By hand: (I1), the derivative bounds of Corollary 1a, every case of Theorem 2 (including the double root J = 7u/16, r_inf = -1/3, and the value L r_inf - delta^2 = -u^2/24 - 2 delta^2/3), and Lemma 3. I ran no census and no search for constructions. Neither repository was touched, and I ran no git command.

## Gaps

- The target is not settled. No bound of M - 1 on R2s constraints per pair is proved, and no pair with more than M - 1 constraints is constructed.
- Theorem 2 needs u = g2 - g1 bounded, which holds for two solutions on one arc. Doubles on different arcs of one curve are not covered: there u is unbounded and the degree argument does not close. Neither are doubles from two different curves of one row system (side e versus side f, or seas L versus F), or doubles with delta varying along the family.
- Theorem 2 excludes polynomial families only. Sporadic same-arc doubles (isolated integer points) are not excluded. Corollary 1b excludes them only in the deep inner zone, which Theorem 2 of the r2s note already covered.
- Lemma 3 reduces heavy-pair degeneracy to the Hilbert-free row counts A2^rho(y). No bound on A2 is proved, so tile separation (Theorem T, conditional on hypothesis (A)) cannot yet be applied.
- Inputs used but not re-derived: Theorem A and Theorem D of hilbert_residual_families.md (audited, correct with fixable gaps); the lattice fact 14 | g and Theorem 1(c) of r2s_single_pair_multiplicity.md (unaudited). Corollary 1b uses 14 | g. The ±V exclusion for 2 <= M <= 2731 sigma^3 is Theorem 1(c). H7's unaudited inputs (AP4, S1-S6, N1) are inherited.
- The heuristic count (log h growth, Hilbert realization on many pairs of a row) is not proved. Its constants are not computed.
- Rule breach, disclosed: the second stage of lines.py (sympy solve for lines on the two-point surface) ran past 60 seconds in the background. I stopped it, and its output is not used. My hand case analysis of lines was incomplete for the branch c != 1, so I claim nothing about lines beyond Theorem 2.
- Nothing here is audited.

## Missing estimate

One Hilbert-free arithmetic estimate would settle what bounded M can do. Fix a role rho and a row y of a block. Bound A2^rho(y): the number of (delta, D0, direction) for which the curves of the row pair (y, y + delta) give at least ceil(M/2) distinct admissible constraint values in the window S[M D0 - (M-1), M D0 + (M-1)]. Bound it uniformly in y and h, ideally by 0 outside an explicit finite set of rows. By Lemma 3, a uniform bound A gives heavy-pair degeneracy at most 2A per block. Tile separation then removes heavy pairs at a factor of at most 2A + 1. Theorem 2 removes the same-arc single-curve part of A2 for all polynomial families. What remains: (i) sporadic same-arc points, which by (I2) are the integer points with N Q(r) = u r(L r - delta^2), |u| <= 2|J|, |J| <= 2(M-1)S; (ii) cross-arc doubles; (iii) two curves of one row system (seas L and F, sides e and f) meeting one window.

## Next steps

- Have a second reader audit Theorem 1 (the two-line derivation of (I1)) and Theorem 2 (cases i, ii-a, ii-b, ii-c, including the double root). They are short and self-contained.
- Extend Theorem 2 to doubles on two arcs of one curve. Here u is unbounded, but h1 = r g2 and h2 = r g1 are still integers. Try the same degree-at-infinity argument on (I2) with u = g2 - g1 non-constant.
- Treat two curves of one row system: the side-e and side-f curves (m, delta) and (m - delta, -delta) have N' = -N, and the L and F curves differ by m_F - m_L = F - L. Derive the analogue of (I1) for two curves and repeat Theorem 2.
- As an exact finite certificate on a fixed system (allowed by the rules): enumerate family A at M = 3, sigma = 1. It is finite: |t| <= 7168, 7 | t, delta in the strip list. This decides whether the rho = 2 sporadic doubles exist at all.
- Feed Lemma 3 into the gap-mixing synthesis. Heavy R2s pairs become a row-indexed bad set whose degeneracy is at most max A2^odd + max A2^even, ready for tile separation once A2 is bounded.

