# A one-sided reduction of the window bound

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: W_N(h) <= 3 W_O(h), where W_O is the width of windows with no one-sided right angle. Structure lemmas for those windows. No bound on W_O is proved. Not audited yet.

# Result

## Status

partial

## Summary

Not proved: W_N(h) <= C h, and not proved: W_N(h) < q_h. Proved: a reduction W_N(h) <= 3 W_O(h) to a one-sided problem with no boundary escapes, and structure lemmas for that problem. Computed: W_O(h) is about h for h <= 18 in a two-walk model. Also shown: single-class and bounded-slope arguments cannot work.

## Statements

Notation. An N-window of width w is as in lower_bound_windows.md (P3): P is a subset of [1,w] x [1,h] with two points per column, the column row pairs are distinct edges of K_{A,B} for a balanced bipartition, and no tilted rectangle of the h x w grid has 3 or more corners in P. A ONE-SIDED RIGHT ANGLE in P is three points V, X, Y of P with (X-V).(Y-V) = 0 and X, Y strictly on the same horizontal side of V (x_X, x_Y > x_V, or both < x_V). Such an angle is automatically tilted. P is OSRAF if it has none. An OSRAF window of width K is a set with two points per column in [1,K] x [1,h], with distinct K_{A,B} row pairs, that is OSRAF. There is no condition on fourth corners. W_O(h) is the largest width of an OSRAF window over all balanced bipartitions.

PROVED (by hand, proofs below):

(T1) One-sided reduction. Let P be an N-window of width w, and let [alpha, beta] be a block of consecutive columns with 2 beta - alpha <= w and 2 alpha - beta >= 1. Then P restricted to the block is an OSRAF window. Taking alpha = L, beta = 2L-1, L = floor((w+2)/3) gives W_N(h) <= 3 W_O(h). Hence m_h >= q_h + floor((q_h - 1)/(3 W_O(h))). If W_O(h) <= C h, then m_h >= q_h + floor((q_h-1)/(3Ch)), about q_h + h/(12C). If W_O(h) < q_h/3, then m_h >= q_h + 1.

(T2) 45-degree path decomposition of OSRAF windows, for every width K. Let Gamma be the bipartite multigraph whose vertices are the 2(K+h-1) diagonals and antidiagonals meeting [1,K] x [1,h] and whose edges are the points of P. Then:
(a) Gamma is a forest.
(b) Every point has at most one occupied 45-degree ray to the right (NE or SE) and at most one to the left.
(c) Each component is an x-monotone path, with consecutive points on a common 45-degree line and at most one point per column.
(d) #components + #empty lines = 2h - 2, exactly.
(e) #components equals the number of points whose two left 45-degree rays are both empty, and also the number whose two right rays are both empty. Hence all but at most 2h-2 points have exactly one occupied left ray, and all but at most 2h-2 have exactly one occupied right ray. At most 2h-3 of the 2(K+h-1) lines are empty.
For the parity bipartition each colour class e (x+y = e mod 2) has one point per column and satisfies #comp_e + #empty_e = Lambda_e - K, where Lambda_e is in {K+h-2, K+h-1, K+h}.
By (T1), the same holds for the middle third of every N-window.

(T3) General directions. For primitive e = (c,d), c, d >= 1, with c <= min(K,h) and d <= min(K,h), the analogous graph Gamma_e (lines of directions (c,d) and (d,-c)) of an OSRAF window is a forest of x-monotone paths. Each point has at most one occupied right ray among (c,d), (d,-c), and at most one occupied left ray. Moreover #comp_e + #empty_e = (c+d-2)K + (c+d)h - 2cd. For c+d >= 3 the right side exceeds K, so this identity has no slack.

(T4) Domino rays. If V and W = V + (1, delta) are in P, delta != 0, then V + t(|delta|, -sgn delta) is not in P and W - t(|delta|, -sgn delta) is not in P, for all t >= 1. Equivalently, with lambda(x,y) = x + delta y: V is the rightmost point of P on its lambda-level line, and W is the leftmost point on level lambda(V) + 1 + delta^2.

(T5) Square rule. If X, Y are in P, X - Y = (p,q), |q| > |p|, p = q mod 2, and M = (X+Y)/2, then M + (q,-p)/2 and M - (q,-p)/2 are not in P. In words: in a tilted lattice square, if both corners of the steep diagonal are in P, then neither corner of the shallow diagonal is.

(T6) A single class is unconstrained. The graph of every f: [1,K] -> [1,h] with |f(x+1) - f(x)| <= 1 is OSRAF, for every K. So for the parity bipartition, no condition internal to one colour class (all slopes included) bounds W_O. A proof must use right angles that meet both points of some column, that is, cross-class right angles.

(T7) Obstruction to the suggested local counting. In any window of width w the rows have mean degree 2w/h, so the mean gap between recurrences of a row is about h/2, independent of w. The same holds at saturation (degree h/2 spread over q_h = h^2/4 columns). The number of local configurations per column, at any bounded scale, is therefore the same for w = 2h as for w = q_h. Only the distinct-pairs condition sees w. One-row Thales and square counts sit exactly at the threshold: a gap of h/2 equals the largest reflection half-width h/2. For example, at saturation a middle row with the full forbidden set of even distances (interval bipartition, m = h/2) is forced only to be a near arithmetic progression of difference h in each parity class, with total slack h-1 and no contradiction. So a proof of W_N(h) = O(h) cannot be a local density count. It must be a rigidity or aperiodicity statement over length about h that the distinct pairs then contradict.

COMPUTED (exhaustive Python DFS unless marked; scripts in the script folder; each run under 60 s):
(K1) N-windows forbidding only some slope families, parity bipartition. Only 45-degree and (1,2) sides: widths 6, 7, 9, 12, and >= 15 (timeout) for h = 6..10. Only sides with max(c,d) <= 3: 9 (h=8), 9 (h=9), >= 13 (h=10). The full family reproduces W = 6 (h=6) and 8 (h=8); 542 rectangles on the 8 x 9 grid, as in the audit. So bounded slopes cannot prove W_N(h) <= h.
(K2) W_O. All bipartitions: 5, 5, 7, 9 for h = 5, 6, 7, 8 (W_O(8) = 9 > W_N(8) = 8, attained only by parity). Parity: 3 (h=4), 9 (h=9), 9 (h=10); >= 11 (h=11) and >= 12 (h=12), timeouts.
(K3) Two-walk model (parity, both classes +-1 walks, distinct pairs, OSRAF), complete searches: 5, 9, 9, 11, 14, 16, 20 for h = 6, 8, 10, 12, 14, 16, 18.
(K4) Annealing does not find width-10 N-windows at h = 10 (best cost 1 over 4 x 10^5 moves), so width-h windows are isolated structured objects. Heuristic only.

NOT PROVED: W_N(h) <= C h; W_N(h) < q_h; W_O(h) <= C h; W_O(h) < q_h/3; any m_h >= q_h + 1 for large h.

## Proofs

(T1). Let V, X, Y be in P in columns alpha..beta, forming a one-sided right angle. Put u = X-V and v = Y-V. Then u_x v_x > 0 and u.v = 0, so u_y v_y = -u_x v_x < 0, and in particular u_y, v_y != 0: both legs are tilted. Let F = X + Y - V; then {V, X, F, Y} is a tilted rectangle. Say u_y > 0 > v_y. Then y_F = y_X + v_y < y_X <= h and y_F = y_Y + u_y > y_Y >= 1. If both legs point right, x_F = x_X + v_x > x_X >= 1 and x_F <= 2 beta - alpha <= w. If both point left, x_F < x_X <= w and x_F >= 2 alpha - beta >= 1. So F is in the grid and the rectangle has 3 or more corners in P, which contradicts the N-window condition. The restricted set has two points per column and distinct pairs, and OSRAF is invariant under translation, so it is an OSRAF window of width beta - alpha + 1. With alpha = L and beta = 2L - 1: 2 beta - alpha = 3L - 2 <= w iff L <= (w+2)/3, and 2 alpha - beta = 1. So floor((w+2)/3) <= W_O(h), and therefore w <= 3 W_O(h). The bound on m_h is (P3) of lower_bound_windows.md (audited) with W_N(h) <= 3 W_O(h). For W_N < q_h it suffices that 3 W_O(h) < q_h.

(T2). (b) NE and SE rays from V both occupied give X = V + s(1,1) and Y = V + t(1,-1), with s, t >= 1 and both strictly to the right: a one-sided right angle. The left rays are symmetric. (a) Take a cycle of Gamma and its leftmost point V (any point of least x). Its two cycle neighbours lie on its diagonal and on its antidiagonal, and they are distinct from V. A 45-degree line meets each column once, so both neighbours are strictly to the right, which contradicts (b). (c) Join each point to the nearest point of P on each of its four rays. Within a component of Gamma this graph is connected, because consecutive points on each line are joined. By (b) it has maximum degree 2. A cycle in it would have a leftmost point with two right neighbours, on two different right rays, which contradicts (b). So it is a path, and each step goes strictly right. (d) The diagonals x - y = c, 1-h <= c <= K-1, and the antidiagonals x + y = s, 2 <= s <= K+h, give K+h-1 lines each. A forest has #edges = #vertices - #components, so 2K = 2(K+h-1) - #empty - #comp. (e) The leftmost point of a path-component has no left neighbour, so both of its left rays are empty. Every other point has its path predecessor on a left ray. Hence #comp counts the points with both left rays empty, and likewise both right rays. #comp >= 1 gives #empty <= 2h-3. Per class: the c-range and the s-range each consist of N = K+h-1 consecutive integers, and class e uses the lines whose parameter is congruent to e mod 2. So Lambda_e is N or N +- 1. Class e has K points, and the same forest argument gives #comp_e + #empty_e = Lambda_e - K.

(T3). Right rays from V are along (c,d) and (d,-c), and (c,d).(d,-c) = 0, so both occupied gives a one-sided right angle. Both directions have nonzero horizontal part, so each line meets each column at most once. The proofs of (a) to (c) carry over word for word. Lines of direction (c,d) meeting [1,K] x [1,h] number Kd + ch - cd (P5 of lower_bound_windows.md, audited, valid for c <= K and d <= h). By the reflection x -> x, y -> h+1-y, lines of direction (d,-c) number Kc + dh - cd. The forest identity gives #comp + #empty = (c+d)(K+h) - 2cd - 2K.

(T4). (1,delta).t(|delta|, -sgn delta) = t(|delta| - delta sgn delta) = 0. Both legs from V point right, so V + t(|delta|, -sgn delta) in P would give a one-sided right angle at V. At W the legs are V - W = (-1, -delta) and -t(|delta|, -sgn delta), with dot product t|delta| - t delta sgn delta = 0, and both point left. lambda is constant along (|delta|, -sgn delta) because |delta| - delta sgn delta = 0. lambda(W) - lambda(V) = 1 + delta^2.

(T5). Put Y = 0, X = (p,q), and say q > |p| (the case q < -|p| is symmetric). Z+ = ((p+q)/2, (q-p)/2) and Z- = ((p-q)/2, (p+q)/2) are lattice points because p = q mod 2. They are the other two corners of the square with diagonal XY, so (X - Z).(Y - Z) = 0. x(Z+) = (p+q)/2 exceeds both p and 0, because q > p and q > -p. x(Z-) = (p-q)/2 is below both 0 and p for the same reasons. So X and Y lie strictly on one side of Z+, and strictly on one side of Z-. A right angle at Z+ or at Z- would be one-sided.

(T6). Suppose X - V = (a,b) and Y - V = (c,-e) with a, c >= 1 (both right), b, e >= 1 (one leg up, one down, as forced by orthogonality), and ac = be. The Lipschitz condition gives b <= a and e <= c, so be <= ac, with equality only if b = a and e = c. Then f(x+i) = f(x) + i for i <= a and f(x+i) = f(x) - i for i <= c, which contradicts each other at i = 1. Both-left is symmetric. A +-1 walk keeps x + f(x) fixed mod 2, so it is a valid parity class.

(T7). Mean degree: the degrees sum to 2w over h rows. The threshold statement: the vertical-diagonal rival forbids black (x, m) and (x + 2k, m) when rows m - k and m + k are in different parts (square condition of lower_bound_windows.md, Next steps). If this holds for every k <= h/2 - 1, each parity class of row m has gaps >= h, so it has at most h/4 points in q_h = h^2/4 columns (h = 0 mod 4). That equals the degree h/2 split over two classes, with slack (h^2/4 - 1) - (h/4 - 1)h = h - 1. This is an observation, not used elsewhere.

Computations (K1) to (K4): famwin.py (rectangle generator by side direction (c,d), c, d >= 1, with count-based pruning) reproduces the audited width counts and the 542 rectangles on the 8 x 9 grid. osraf.py and twowalk.py check every triple with the new point as vertex or as a leg endpoint. check.py, written separately from the definition, rechecks the reported windows: the h = 8 (width 9), h = 10 (width 9) and h = 12 (width 12) OSRAF windows have distinct K_{A,B} pairs and 0 one-sided right angles (and 28, 5, 21 N-window violations). The cyclic staircase at h = 6 has 0 N-window violations and 4 one-sided right angles, which confirms that OSRAF and N-window are different conditions.

## External results used

- lower_bound_windows.md (audited): (P3) m_h >= q_h + floor((q_h-1)/W_N(h)), used in (T1); (P5) line counts qd + ch - cd, used in (T3); the square or rival condition, used only in the (T7) remark.
- window_conjecture_h9_h11.md: computed W_N(h) = h for h <= 11, used only for comparison with (K2).
- No published external theorem is used.

## Checks

Script folder: the matching scripts_ folder of this directory. Scripts: famwin.py (family-restricted N-windows), osraf.py and osraf_all.py (one-sided windows, all bipartitions up to reflection), twowalk.py (two-walk model), sa.py (annealing, heuristic only), check.py (definition-level checker). Sanity: famwin.py with the full family gives parity W = 6 at h = 6 and W = 8 at h = 8, with 542 rectangles on the 8 x 9 grid, matching the audit in lower_bound_windows.md. check.py independently confirms the reported OSRAF windows (0 one-sided right angles, distinct edges) and that the cyclic staircase is an N-window but not OSRAF. Every run took under 60 s and used little memory. The repository was not touched, and I ran no git commands.

## Gaps

- The target is not reached. W_N(h) <= C h and W_N(h) < q_h are both open, and so is any lower bound above q_h for large h.
- (T1) loses a factor 3 and needs a bound on W_O, which is open. Computation suggests W_O(h) = h + O(1), but W_O(h) <= C h is not proved, nor even W_O(h) < q_h/3.
- (T2) and (T3) are exact identities with no slack (45 degrees) or no content (c+d >= 3). I found no combination of two direction families that yields an inequality.
- The computations are Python DFS runs without proof logs. (K2) at h = 11, 12 and (K1) at h = 10 are lower bounds from runs that timed out. (K2) for all bipartitions covers h <= 8 only. (K3) is a restricted model (both classes +-1 walks), not the general problem.
- (T7) is a heuristic obstruction: it shows why local counts cannot work, but it is not a theorem that no counting argument exists. The rival-rule computation in it is for one special bipartition.
- I did not verify the PAYOFF computation for heavy_light_split.md, because it is not part of this route.

## Missing estimate

One-sided window bound: there is an absolute C such that every OSRAF window of height h (two points per column, distinct K_{A,B} row pairs, no right angle V, X, Y with X and Y strictly on the same horizontal side of V) has width at most C h. By (T1) this gives W_N(h) <= 3Ch and m_h >= q_h + floor((q_h-1)/(3Ch)). The weaker estimate W_O(h) < q_h/3 for large h already gives m_h >= q_h + 1. By (T6) the proof must use cross-class right angles. By (T7) it must be a rigidity statement over length about h, not a local density count. The data suggest W_O(h) <= h + 2.

## Next steps

- Prove the linear bound in the two-walk model first (both parity classes are +-1 walks, (K3): W <= h + 2 up to h = 18). There the column-pair Thales circles and the domino rays of (T4) are explicit, and the self-avoiding diagonal walk (f0(x), f1(x)) in [1,h]^2 must be shown to stop after O(h) steps.
- Compute W_O(h) exactly for all bipartitions at h = 9..12 with a SAT encoding (one clause per one-sided right angle, at-most-once per edge, exactly two per column), with DRAT logs. If W_O(h) <= h + 2 continues, conjecture W_O(h) = h + O(1) formally.
- Look for a rigidity lemma in OSRAF: for example, after O(h) columns the pair sequence is determined by a bounded amount of data. With distinct pairs this bounds the width. Start from (T2)(e): almost every point has exactly one left and one right 45-degree neighbour.
- Reduce the factor 3 in (T1). Use the one-sided-right condition on the left part of the window and the one-sided-left condition on the right part, with leg-length bounds, to get W_N(h) <= W_O(h) + O(h).

