# The per-tile hypothesis (G) for the P family

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: (G) for P is still unproved, and no counterexample was found. The partner-offset lemma holds only in normalized form (each value fewer than 24 sqrt(D) times over D consecutive gaps), and over labels at a fixed gap 4^m it fails by a factor of order sqrt(d) through an exact identity on transposed quarters, so it cannot give (G) through criterion (8). Proved: the global-average case of (G) on every tile after a random diagonal shift, mean P degree at most about 2980 (k+1)(1 + ln(4h)/2)/S_k. Audited in audit_hilbert_g_and_lambda.md (correct with fixable gaps).

# Result

## Status

partial

## Summary

Hypothesis (G) for P is still unproved, and I found no counterexample. The partner-offset lemma holds only in normalized form: each value appears fewer than 24 sqrt(D) times over any D consecutive gaps. Over labels at a fixed gap 4^m it fails by a factor of order sqrt(d), through an exact identity on transposed quarters. Even its true form adds nothing to the window bound (13), so it cannot give (G) through criterion (8). What I proved toward (G) is its U = V case on every tile after a random diagonal shift: mean P degree at most about 2980 (k+1)(1 + ln(4h)/2)/S_k. No new width follows.

## Statements

Setting. Full-grid convention: label e = (i_e, j_e), odd row 2i_e+1, even row 2j_e+2, T_e = j_e - i_e. H = H_Q is the Hilbert order of recursion (2) in continuation_hilbert_placement.md. For labels e, f the two cross-parity gaps are Y1(e,f) = |2(j_f - i_e) + 1| and Y2(e,f) = |2(j_e - i_f) + 1|. Placement: x_e = S(M r_e + xi_e). A level-k tile is an aligned square of side l = n 2^(-k) (a power of two) on the diagonal or next to it. It keeps the labels with l/2 <= |T| < l, and the final level keeps those with |T| < l. Its candidate P multigraph has one constraint for each (pair, delta, role) whose vector (S(Md+delta), Y) has integral length L <= h-1. I drop the strip test, which only enlarges the family. Write lambda_k = (k+1) log h / S_k.

THEOREM A (normalized multiplicity of partner offsets; proved). For every interval I of D >= 1 consecutive ranks, each coordinate c in {1,2} and each integer v:
 #{s in I : H(s)_c = v} < 12 sqrt(D).
So for every label e, each side (partner rank r_e + d or r_e - d), each role and each odd y, over any interval I of D consecutive gaps d:
 #{d in I : Y_role(e, H(r_e +- d)) = y} < 24 sqrt(D).
On I = [D, 2D) the values lie in a set of at most 8 sqrt(2D) + 1 odd numbers, so their average multiplicity is at least sqrt(D)/12.4. The maximum is therefore within a factor 300 of the average. The bound is sharp up to the constant: an aligned block of 4^m ranks gives multiplicity exactly 2^m = sqrt(D). The literal claim "bounded multiplicity as d varies" is false, because some value always has multiplicity at least sqrt(D)/12.4. Bounded multiplicity relative to the window width is the true form. It holds on every interval, so at every scale.

THEOREM B (exact identities on Hilbert quarters; proved). (i) Orientation: every aligned rank block of length 4^(m+1), with square O + [0,2q)^2 and q = 2^m, is traversed as s -> O + g(H_2q(s - beta)) with g in the Klein group V = {id, swap, antiswap, rot180} of the square. (ii) Transposition identity: for every such block there are c1, c2 in {-q, 0, q} such that, for every rank r in its first quarter,
 j_{r+q^2} - i_r = (O2 - O1) + c1 and j_r - i_{r+q^2} = (O2 - O1) + c2.
So both cross-parity gaps between r and r + q^2 are constant on the quarter, and both are congruent to +-1 mod 2q, since O2 - O1 is a multiple of 2q. (iii) Translation identity: H(r + q^2) - H(r) is one constant vector in {(+-q,0), (0,+-q)} for every r in the second quarter. (iv) Over labels at a fixed gap, partner gaps are not equidistributed. Take d = 4^m with 2 sqrt(d) <= l. In H_l, some t has #{r : j_{r+d} - i_r = t} >= l sqrt(d)/8. In a level-k tile with 16 sqrt(d) <= l, some t has at least l sqrt(d)/128 retained pairs (r, r+d) with that value. The trivial upper bound is (8 sqrt(d) + 1) l, so the maximal fiber has order l sqrt(d), while equidistribution predicts O(l). At these gaps the pair law sits on the index-q sublattice Y = +-1 mod 2q. So the H-EQ hypothesis of hilbert_p_height_independent_cores.md is false when stated for each gap d. It can hold at most averaged over d.

THEOREM C (the U = V case of (G), with a random diagonal shift; proved). Let S = 2^s >= 4 and l >= 16 sqrt((h-1)/(SM) + 1) + 2. Place the tile in a Hilbert square of side 2l, with label (i, j) in cell (i - I0, j - J0 + J) and J uniform in {0, ..., l-1}. This keeps a subset of cells with its original ranks, so the T3 conventions apply. It costs a factor 4 in tile width. Let mu_J be the mean weighted P degree (2|E_J|/N). Then
 E_J[mu_J] <= 256 V_R/l, where V_R = #{(q', Y): Y odd, Y in R, (S q')^2 + Y^2 = L^2, L <= h-1}.
Here R = [l/2, 3l] for levels k < K, and R = [1, 3l] for the final level. Moreover, with K1 = floor(4(h-1)/S^2),
 V_R <= (beta0/S)(3.87 + 0.71 ln+(h/(2 beta0)))(1 + ln+(K1)/2) + (2 sqrt(h)/S)(1 + sqrt(K1)), with beta0 = 3l.
So some shift J has
 mu_J <= (768/S)(3.87 + 0.71 ln+(h/(6l)))(1 + ln+(4h/S^2)/2) + (512 sqrt(h)/(l S))(1 + 2 sqrt(h)/S).
For level k in a full-grid block of side n >= h/2 (so ln(h/6l) <= k ln 2):
 mu_J <= 2980 (k+1)(1 + ln(4h)/2)/S_k + o(1).
At the final level the main term is C (log log h)(log h)/S_K. So every tile has a shift whose global mean P degree, and hence whose global average of F^- (at most mu/2), has the form of (G). The shift is chosen per tile. The same-parity exclusion and all per-core statements of T3 hold for every J. H7 version (remark, not written in full): with row step 28, Y_J = |C - 28J| is still injective up to sign. Take beta0 = 30l, and count with the 2-part S/49 of S = 6272 sigma (sigma a power of two). Only the constants change, by a factor of at most about 500.

PROPOSITION D (why the lemma cannot give (G) through (8); proved as a statement about the method, with (3) heuristic). (1) Criterion (8) needs max over U of avg_{e in U} F^-_U(e). The only per-vertex tool is b^- <= 4F^-. The best per-label bound that Theorem A gives, at scale D, is the sum over y in the window of min(24 sqrt(D) N*_D(y), 2 rho_D(y)), which is at most 2 times the number of vectors in the window. That is the window count behind (13). Theorem A limits how often the partner curve visits one value y. It does not limit whether a visit lands on one of the few gaps where y has a leg, and one such gap per y already reaches the trivial bound. So Theorem A adds nothing to (13). (2) By Theorem B(iv), no per-gap averaging over labels works without randomization. (3) Heuristic: even in the random-row model, the maximum P degree over the l^2/4 labels of a tile grows like ln(l^2)/ln ln(l^2). So the vertexwise criterion (5), and any max-degree argument, cannot give bounded M. (G) is a statement about induced subgraphs, or equivalently about an orientation with out-degree at most c0 + c1 lambda_k. Theorem C proves only the case U = V, and the K_t example in the budget note shows that U = V does not imply (8).

STATUS OF (G). Unproved for P, and not refuted. The structures of Theorem B give only perfect matchings between quarters at gap 4^m: at most one constraint per level and per label from the exact gap. A 2-adic computation via T1 suggests that legs are at most about twice as dense on Y = +-1 mod 2q as on average. This is heuristic. So these structures do not break (G). I give no "true bound", because I proved no upper bound below the window bound (13). Unconditionally, P on a tile still needs M = (h/S_k)^(1/3) h^(o(1)). The C4 width h^2 log h stays conditional on (G) and the H7 audits.

## Proofs

1. PROOF OF THEOREM A.
Let I = [a, a+D). For each m, let B_m be the set of aligned rank blocks of length 4^m that lie inside I and whose parent (length 4^(m+1)) does not. Every rank of I lies in exactly one maximal aligned block inside I, so the union of the B_m partitions I. The parent of a block in B_m meets I but is not inside it, so it contains a boundary pair of I: either (a-1, a) or (a+D-1, a+D). At most two parents qualify at each level. Each has four children, and at most three of them are inside I, since otherwise the parent would be inside I. So |B_m| <= 6, and B_m is empty unless 4^m <= D. Let m* be the largest m with 4^m <= D. By the placement note, every aligned block of length 4^m is a dyadic square of side 2^m. It has exactly 2^m or 0 cells with c-th coordinate v. So the count is at most 6 * sum_{m <= m*} 2^m < 12 * 2^{m*} <= 12 sqrt(D).
For role 1 on the upper side, Y1(e, H(r+d)) = y holds exactly when j_{r+d} lies in {i_e + (y-1)/2, i_e - (y+1)/2}. These are two values of the second coordinate along the rank interval r + I of length D, so the count is below 24 sqrt(D). Role 2 constrains the first coordinate of the partner in the same way, and the lower side is the same. For I = [D, 2D), locality (1) gives |z| < 4 sqrt(2D) for the coordinate offset z, so there are at most 8 sqrt(2D) + 1 values and the average multiplicity is at least D/(8 sqrt(2D) + 1) >= sqrt(D)/12.4. Sharpness: if a + D lands on an aligned block of length D = 4^m, every row of that 2^m-square is visited 2^m times. QED.

2. PROOF OF THEOREM B.
(i) Induct from the top square, whose orientation is id. Suppose a block of side 2s is traversed as O + g(H_2s(.)) with g in V. By recursion (2), its children are traversed as O + g(o_t + g_t(H_s(.))), with g_t in {swap_s, id, id, antiswap_s} and o_t in {(0,0), (0,s), (s,s), (s,0)}. The composite is an isometry of Z^2 that maps [0,s)^2 onto the child square. Its linear part is the product of linear parts in {I, P, -P, -I}, with P the coordinate swap. An affine isometry with linear part A that maps [0,s)^2 onto O' + [0,s)^2 is O' + g_A with g_A in V. So every child is traversed with an orientation in V.
(ii) In the canonical H_2q, rank rho < q^2 sits at P1 = (y, x) and rank rho + q^2 at P2 = (x, y+q), where (x, y) = H_q(rho). For each g, compare second(g P2) - first(g P1) and second(g P1) - first(g P2):
 id: (y+q) - y = q, and x - x = 0.
 swap, with g(u,v) = (v,u): x - x = 0, and y - (y+q) = -q.
 antiswap, with g(u,v) = (2q-1-v, 2q-1-u): (2q-1-x) - (2q-1-x) = 0, and (2q-1-y) - (q-1-y) = q.
 rot180, with g(u,v) = (2q-1-u, 2q-1-v): (q-1-y) - (2q-1-y) = -q, and (2q-1-x) - (2q-1-x) = 0.
Adding the origin O gives j_{r+q^2} - i_r = O2 - O1 + c1 and j_r - i_{r+q^2} = O2 - O1 + c2, with c1, c2 in {0, +-q}. Since 2q | O1, O2, the value t is a multiple of q, so 2t + 1 = 1 mod 2q.
(iii) Canonically, quarter 2 to quarter 3 is the translation (x, y+q) -> (x+q, y+q), by (q, 0). The orientation maps this to A(q, 0), which lies in {(+-q, 0), (0, +-q)}.
(iv) Full square H_l, d = q^2, 2q <= l. The first quarters hold l^2/4 ranks. On each quarter, t = j_{r+d} - i_r is a multiple of q in (-l, l), so t takes at most 2l/q values. By pigeonhole some t has at least (l^2/4)/(2l/q) = lq/8 ranks. Tile, diagonal case: take the corner {b - a >= l/2} in local coordinates and the aligned 2q-blocks that lie fully inside it. Their block offsets o run over the multiples of 2q in [l/2 + 2q, l - 2q]. Offset o carries (l - o)/(2q) blocks. Summing, there are at least (l/(4q) - 1)^2/2 >= l^2/(128 q^2) blocks when 16q <= l. Their first quarters hold at least l^2/128 ranks, and both members of each pair are retained. The t values are multiples of q in an interval of length below l/2 + 4q <= l, so there are at most l/q of them. Hence some fiber is at least lq/128. Off-diagonal tiles give the better constant lq/24 in the same way. Upper bound: j_{r+d} - i_r = T_r + (j_{r+d} - j_r) with |j_{r+d} - j_r| < 4 sqrt(d), so T_r lies on one of at most 8 sqrt(d) + 1 diagonals, each with at most l cells. QED.

3. PROOF OF THEOREM C.
(a) Shift averaging. Cell c holds the label (c1 + I0, c2 + J0 - J). Fix an earlier rank rho in [0, 4l^2), a gap d, a delta and a role. For role 1, with c = H(rho) and c' = H(rho + d):
 Y1 = |2(c'_2 - c_1 + J0 - I0 - J) + 1|.
For role 2:
 Y2 = |2(c_2 - c'_1 + J0 - I0 - J) + 1|.
Each inner value is strictly monotone in J, so each target y occurs for at most 2 values of J. Retention of the earlier label gives |T_e| in [l/2, l). Locality gives |z| < 4 sqrt(d), and d <= (h-1)/(SM) + 1 because S(M(d-1)+1) <= X < h. With the hypothesis on l, this gives Y in [l/2, 3l], and Y in [1, 3l] at the final level. So the pair (rho, d, delta, role) is a constraint for at most 2 |Y(Md+delta) and R| values of J. Each q' comes from at most 2 slots (d, delta). Hence
 sum_J |E_J| <= 4l^2 * 2 roles * 2 * 2 V_R = 32 l^2 V_R, so E_J|E_J| <= 32 l V_R.
A diagonal tile retains N = (l/2)(l/2+1) >= l^2/4 labels, and off-diagonal tiles retain at least that many, so E_J[mu_J] <= 64 l V_R/N <= 256 V_R/l. This counts (pair, delta, role) triples, an upper bound for the deduplicated multigraph of the budget note.
(b) Vector count via T1. By T1, the vectors correspond to triples (k, e', O): k odd, e' >= 1, O odd, gcd(e', O) = 1, E = S e'/2, Y = k|E^2 - O^2|, L = k(E^2 + O^2). Drop the coprimality condition and the lower end of R. Fix k and put b = beta0/k and c = h/k. For fixed e', the admissible O lie in one interval [sqrt(max(0, E^2 - b)), sqrt(E^2 + b)], cut down by O^2 <= c - E^2. Its length l(E) satisfies:
 l(E) <= 2b/(sqrt(E^2+b) + sqrt(E^2-b)) <= sqrt(2) b/E if E^2 >= 2b;
 l(E) < sqrt(3b) otherwise.
An interval of length l contains at most l/2 + 1 odd numbers. Summing over e' with E^2 < c:
 - e' with E^2 < 2b: at most 2 sqrt(2b)/S of them, contributing at most sqrt(6) b/S < 2.45 b/S;
 - e' with E^2 >= 2b: at most (sqrt(2) b/S) * sum 1/e' <= (sqrt(2) b/S)(1 + ln+(c/(2b))/2). In both sub-cases, the ratio of the e' endpoints is at most sqrt(c/(2b));
 - the +1 terms: at most 2 sqrt(c)/S.
So N_k <= (b/S)(3.87 + 0.71 ln+(c/(2b))) + 2 sqrt(c)/S, where c/(2b) = h/(2 beta0) does not depend on k. A vector needs k(S^2/4 + 1) <= L <= h - 1, so k <= K1. Over odd k <= K1, sum 1/k <= 1 + (ln K1)/2 and sum k^(-1/2) <= 1 + sqrt(K1). This gives the stated V_R bound. Multiplying by 256/l with beta0 = 3l and K1 <= 4h/S^2 gives the mu_J bound. For level k: n >= h/2 gives h/(6l) <= 2^k/3, so 0.71 ln+(h/6l) <= 0.49k. Also 768(3.87 + 0.49k) <= 2980(k+1). The error term is at most 1024 log h/S^2 + o(1) when l >= h/(2 log h). QED.

4. PROOF OF PROPOSITION D.
(1) Fix e, a role, a side and a dyadic D. Write rho_D(y) for the number of legs Sq' of y with q' in [M(D-1), M(2D+1)], and N*_D(y) for the largest number of such legs in one slot window. Then
 sum_{d in [D,2D)} #{delta} = sum_y sum_{d : Y_d = y} N(d, y).
Each leg lies in at most 2 windows, so the inner sum is at most min(24 sqrt(D) N*_D(y), 2 rho_D(y)). The second term already gives the trivial bound 2 times the number of vectors in the window. Theorem A only improves the first term, which is not the minimum whenever y has at least one leg. Summed over D, this is the window count of (13). Theorem A constrains the multiset of visited values. It does not constrain their position relative to the sparse leg set, and only that position separates the truth (about 2 rho-bar_D) from the window count (about 16 sqrt(2D) rho-bar_D).
(2) is Theorem B(iv).
(3) Heuristic. With degrees roughly Poisson with bounded mean over about l^2/4 labels, the maximum is (1 + o(1)) ln(l^2)/ln ln(l^2).
(4) By (4) and (7) of the budget note, F^-_U <= b^-_U, so the global average of F^- is at most mu/2, and Theorem C bounds that. The K_t example shows that a bound on the global average alone cannot replace the maximum over U.

5. HEURISTIC REMARK ON THEOREM B (not a proof).
For primitive vectors (k = 1) with 2q | E^2, T1 gives Y = E^2 - O^2 = -O^2 or Y = O^2 - E^2 = O^2 (mod 2q). So Y = +-1 (mod 2q) exactly when O = +-1 (mod q), which happens for a 4/q share of odd O. For a random odd Y the share of +-1 (mod 2q) is 2/q. So the bias is a factor of about 2, not sqrt(d). The concentration in B(ii) therefore changes edge counts at gap 4^m by a bounded factor in the random-row model, and it does not refute (G).

6. CONSEQUENCE FOR THE ROUTE.
(G) for P is equivalent to the induced statement (II), up to the factor 8 between (8) and degeneracy (B <= D and D <= 8B). (II) says: for every tile and every U, |E(U)| <= (a0 + a1 lambda_k)|U|, and at the final level the same with (log h)^2/S_K. Theorem C is (II) for U = V, for a suitable shift. Nothing here proves (II) for general U. So C4 remains conditional and the width bound is unchanged: the best proved bound is still (log h)^(1.3108172 + eps).

7. A FIRST-MOMENT-ONLY ROUTE (remark; analysis of a scheme, not proved).
Re-place every label that has an edge in a fresh tile with a fresh shift, and repeat with M = 1. Suppose this is controlled only by bounds E_J|E_J(B)| <= theta |B| for arbitrary fixed sets B. Then it needs about ln N/ln(1/theta) rounds, each costing a full tile of width about S l^2. Since theta is of order lambda, this gives S times the number of rounds at least of order (log h)^2, so b = 2. Beating b = 2 by first moments alone would need B-dependent decay, about lambda |B|^2/N, which fails for sets concentrated on bands. So some control of induced subgraphs, or of second-order structure, is needed for b = 1.

## External results used

- Euclid parametrization of primitive Pythagorean triples (standard), used only through the archive's T1 normal form.
- No published theorem was cited or fetched. Shiu's theorem is mentioned only to explain why it does not give the needed short-band count; it is not used.

## Checks

Three sanity scripts, each under 60 s, in scripts_hb2_g_p/ (none touches either repository):
- check_fiber_transpose.py builds H_256 by recursion (2) and checks locality (1) on 20000 random pairs. Theorem A: across D from 1 to 16384 and sampled intervals, the largest multiplicity over sqrt(D) is 2.16, against the proved 12. Theorem B(ii): for every m <= 6 and every aligned 4^(m+1) block, both cross-parity offsets are constant on the first quarter with c in {0, +-q}, with zero failures. Theorem B(iv) in the full square: the largest fiber of j_{r+d} - i_r at d = 16, ..., 4096 is 0.50 to 0.79 times q sqrt(d) with q = 256, against the proved 1/8, while the mean nonzero fiber stays near 131 (about q/2).
- An inline check of B(iii): H(r + q^2) - H(r) is constant on every second quarter and lies in {(+-q,0), (0,+-q)} (zero failures, m <= 6).
- check_VR.py compares the exact V_R (T1 enumeration with coprimality) with the proved bound at 8 settings (S in {16, 32, 64}, h in 2^16..2^20, l from h/32 to h/8). The ratio of exact to bound is 0.21 to 0.25 in every case.
- check_shift_tile.py takes h = 2^12, S = 8, M = 3, a diagonal tile with l = 512, and the shifted 1024-square, with 14 sampled shifts. The exact weighted P mean degree is 4.47 to 4.80, against the proved bound 256 V_R/l = 244.5 (V_R = 489). The bound holds, with slack of about 50.
By hand I checked the orientation induction, the four orientation cases, the decomposition into at most 6 blocks per level, the injectivity of Y in J, the slot multiplicity 2, and the N_k lattice estimates with their constants.

## Gaps

- The target is not reached: hypothesis (G) for the P family (weighted degeneracy, or the induced average of criterion (8), at most c0 + c1 (k+1) log h/S_k on each tile) is unproved for every tile level. No counterexample was found either.
- Theorem C proves only the U = V case (the global mean degree), averaged over a random diagonal shift. It needs the 2l-square shifted tile (factor 4 in width), which is a design change C4 has not yet absorbed. It says nothing about induced subgraphs, where the band heuristic places the danger (the final-level band Y in [h^0.6, h^0.7]).
- The lattice-point count in Theorem C has an error term of about 4h/S^2. That is too large to extend the shift-averaged bound to short bands (width below about h/S). Bands need a short-interval divisor or lattice count with the 2-adic condition.
- The H7 version of Theorem C (row step 28, S = 6272 sigma, physical gap range up to about 30l, 2-part S/49) is sketched in a remark, not written out. It also assumes sigma is a power of two.
- Theorem B(iv) gives explicit fiber lower bounds, but I did not quantify near-transposition gaps (d = 4^m + d' with small d'), where the concentration persists at width about 8 sqrt(|d'|).
- Proposition D(3) (unbounded maximum degree) and the 2-adic bias remark are heuristic, based on the random-row model.
- I proved no unconditional per-tile degeneracy bound below the window bound (13). Unconditionally, P on a tile still needs M = (h/S_k)^(1/3) h^(o(1)).
- Nothing here is audited. The proofs of Theorems A, B and C are short, and I checked the key identities numerically (see checks), but no second reader has derived them.

## Missing estimate

Induced incidence bound (II): for every level-k tile and every subset U of its retained labels, the candidate P multigraph has |E(U)| <= (a0 + a1 (k+1) log h/S_k)|U|. At the final level the same holds with (log h)^2/S_K. Equivalently, the constraints can be oriented with out-degree at most a0 + a1 lambda_k. By Theorem C this holds for U = V after a random shift. The first intermediate target is the shift-averaged bound for every band of diagonals of width at least h^(1/2+eps). It needs a short-interval count of T1 triples (k, e', O) with k|E^2 - O^2| in an interval of that length, sharper than the lattice error 4h/S^2. A second-order input (pair correlations of edges, or a bound on short cycles and small dense cores) is then still needed to pass from bands to arbitrary U.

## Next steps

- Prove a short-interval version of the V_R count: T1 triples with Y in an interval of length h^(1/2+eps), with the 2-adic condition and the restricted divisor range u >= Y^2/(2h). This extends Theorem C to all bands of width at least h^(1/2+eps), including the final-level band [h^0.6, h^0.7], and would make Statement D's band density rigorous in the shifted model.
- Bound the shift-averaged number of cherries (paths of length 2) and of short cycles in a tile graph. Small dense cores would show up there first, and a bound would be the first second-order input toward (II).
- Run a census of shifted level-k tiles with row step 28 and S near 6272 (h7 design). Measure degeneracy by band, and test whether the near-transposition gaps d = 4^m + d' raise the density.
- Fold the factor-4 shifted tile of Theorem C into the C4 bookkeeping. Per-tile shifts are independent, and every per-core theorem holds for every shift.
- Ask an independent reader to audit Theorems A to C, in particular the Klein-group orientation induction and the constants of the N_k lattice count.

