# All-double windows and a lower bound at height 8

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: m_h >= q_h + floor((q_h - 1)/W_N(h)), and W_N(h) = h for h <= 8, so m_8 >= 17 = q_8 + 1. Proofs passed an audit. W_N was recomputed by a second program written from the definitions.

# Result

## Status

partial

## Summary

Not proved: m_h >= q_h + 1 for all h. Proved: the reduction m_h >= q_h + floor((q_h-1)/W_N(h)) to all-double windows without tilted corner triples; computed W_N(h) = h for h <= 8 (so m_8 >= 17); and explicit boards show that the 45-degree corner condition alone cannot exclude saturated boards (parity bipartition at h = 9, other bipartitions at h = 5, 6).

## Statements

Notation. Grid with h rows and m columns, q_h = floor(h^2/4), f(h,m) = largest valid blackout, m_h = least M with f(h,m) = m + q_h for all m >= M. An EQUALITY BOARD is a valid blackout of the h x m grid (h >= 4, m >= 4) with m + q_h points. By the paper's equality-structure theorem its columns are singletons or doubles, and the q_h double pairs are exactly the edges of K_{A,B} for a balanced bipartition (A,B) of the rows (the "parts"). A SATURATED BOARD is an equality board with m = q_h. m_h >= q_h + 1 holds iff no saturated board of height h exists.

PROVED (complete proofs in proof_outline).

(P1) In every equality board no tilted rectangle is fully black. If a tilted rectangle has exactly three black corners and (x, rho) is its white corner, then column x is a singleton column whose black row lies in the part that contains rho. Hence every tilted rectangle whose four corners lie in a block of consecutive double columns has at most two black corners.

(P2) Window principle. Let h >= 4 and k >= 2. If no equality board of height h (of any width) has k consecutive double columns, then m_h >= q_h + floor((q_h - 1)/(k - 1)).

(P3) For a balanced bipartition (A,B) of {1..h}, an N-WINDOW of width k is a set P of 2k points of the h x k grid with exactly two points in every column, whose k row pairs are distinct edges of K_{A,B}, such that every tilted lattice rectangle of the h x k grid has at most two corners in P. Let W_N(h) be the largest width of an N-window over all balanced bipartitions. Then for every h >= 4: m_h >= q_h + floor((q_h - 1)/W_N(h)). In particular W_N(h) < q_h implies m_h >= q_h + 1. (By the archive's cyclic staircase, W_N(h) >= h - 1 for all h >= 4 and W_N(h) >= h for even h, so this method gives at most about q_h + h/4.)

(P4) Parity decoupling. Let P have exactly two points in each column 1..k, with rows of different parity in each column. Split P by the parity of x + y into P_0 and P_1. Then each P_e has exactly one point per column, the four corners of a rectangle with sides of slopes +1 and -1 lie in one class, and so "every 45-degree rectangle of the grid has at most two corners in P" holds iff it holds for P_0 and for P_1 separately. A saturated board with the parity bipartition and no 45-degree corner triple is the same as a pair of functions phi_0, phi_1 : {1..q_h} -> {1..h}, phi_e(x) = x + e mod 2, whose graphs contain no three corners of a 45-degree rectangle of the grid, with x -> {phi_0(x), phi_1(x)} a bijection onto the pairs (odd row, even row).

(P5) Line counts. For coprime c, d >= 1 with c, d <= min(q, h), exactly q d + c h - c d lines of direction (c, d) (or (c, -d)) meet the q x h grid. So a set of 2q points is forced to have two points on a common line only for d = 1 and c < q/(h-1); and for every perpendicular pair of directions the number of lines exceeds 2q by (c+d-2) q + (c+d) h - 2cd >= 2h - 2.

(P6) Ray rules. If every 45-degree rectangle of the h x k grid has at most two corners in P and Z = (x,y) is in P with h <= x <= k - h + 1, then at most two of the four diagonal rays from Z meet P; if the two lower rays meet P first in rows a and c then a + c <= y; if the two upper rays meet P first in rows a and c then a + c >= y + h + 1.

(P7) Flow lemma. If L is a set of points (x,y), x integer, 1 <= y <= h, x + y even, with exactly one point on every line x - y = v (v even) and on every line x + y = u (u even), then the number of points of L in the cone {y - 1 >= |x - c - 1|} is the same for every even c; if L is periodic in x it equals the mean row of L, which is therefore an integer.

COMPUTED (exhaustive searches by scripts, no independent certificate).

(C1) W_N(h) = h for 4 <= h <= 8 (all balanced bipartitions). With (P3): m_5 >= 7, m_6 >= 10, m_7 >= 13, m_8 >= 17. Only m_8 >= 17 = q_8 + 1 is new. For the parity bipartition the largest N-window has width 4, 4, 6, 6, 8, 8 for h = 4..9.

(C2) For the parity bipartition the number of saturated boards in which every 45-degree rectangle has at most two black corners is 4, 0, 0, 0, 0, 14 for h = 4, 5, 6, 7, 8, 9. One of the 14 boards at h = 9 (black rows of columns 1..20): 12 34 18 47 29 36 89 56 58 25 45 69 14 16 49 67 38 23 27 78. None of the 14 is valid.

(C3) Saturated boards with no 45-degree corner triple exist for non-parity bipartitions: h = 5, A = {1,2}: 23 25 24 15 13 14; h = 6, A = {1,3,6}: 23 46 26 35 15 34 12 14 56.

NOT PROVED: m_h >= q_h + 1 for all h >= 4, or for all large h.

## Proofs

SETTING. Point (x,y) = column x, row y. Facts from the paper: (K1) two rectangles have the same presentation iff the symmetric difference of their corner sets is black (Lemma "diff"). (K2) equality structure (Theorem "equality structure", h >= 4, m >= 3). (K3) f(h,m) <= m + q_h. (K4) m_h exists, so an equality board of width m_h exists, and m_h >= q_h >= 4. The owner of an edge {r,s} of K_{A,B} is the double column with black rows r, s.

LEMMA 1 (axis owner). In an equality board let W = (x, rho) be white and let column x have a black point (x, s) with s in the part not containing rho. Then an axis-aligned rectangle has presentation {W}. Proof: {rho, s} is an edge of K_{A,B}; let z be its owner. z != x since (x, rho) is white. The rectangle with columns x, z and rows rho, s has corners W (white) and (x,s), (z,rho), (z,s) (black). In a double column one of the two black rows is in the part not containing rho, so the lemma applies to every white point of a double column.

LEMMA 2 (no fully black tilted rectangle; archive note hidden_rectangles_and_exact_hypergraph.md, proof repeated). Let h, m >= 4 and S valid. Suppose a tilted rectangle R with diagonals AC, BD is fully black. Case 1: AC is neither horizontal nor vertical. A = (x,a), C = (z,c), x != z, a != c. Put P = (x,c), Q = (z,a) (grid points). T = {A,P,C,Q} is an axis-aligned rectangle. PQ has the midpoint and length of AC, hence of BD. If {P,Q} met {B,D}, the common midpoint would give {P,Q} = {B,D} and R = T would be axis-aligned. So U = {P,B,Q,D} is a rectangle of positive area, A is not in U, T != U, T and U share exactly P, Q, and the symmetric difference is {A,B,C,D}, black. By (K1) T and U have equal presentations: contradiction. Case 2: both diagonals are horizontal or vertical. Then R = {(x-d,y),(x+d,y),(x,y-d),(x,y+d)}, d >= 1 an integer. If d >= 2: A = (x-d,y), u = (1,-1), v = (d,d), R = {A, A+du, A+v, A+du+v}; T = {A, A+u, A+v, A+u+v} and U = {A+u, A+du, A+u+v, A+du+v} are rectangles of positive area with corners on sides of R, T != U, symmetric difference R: contradiction. If d = 1: 2 <= x <= m-1, 2 <= y <= h-1; as m, h >= 4 choose sigma, tau in {1,-1} with 2 <= x+sigma <= m-1, 2 <= y+tau <= h-1; u = (sigma,tau), w = (sigma,-tau), A = (x-sigma,y), R = {A, A+u, A+w, A+u+w}; T = R + u is the unit diamond centred (x+sigma,y+tau), in the grid; U = {A, A+2u, A+w, A+2u+w} has its corners in R or T; T = {A+u, A+2u, A+u+w, A+2u+w}; symmetric difference of T and U is {A+u, A+u+w, A, A+w} = R: contradiction.

PROPOSITION 3 = (P1). (a) Lemma 2. (b) If column x were a double, or a singleton whose black row is in the other part than rho, Lemma 1 gives an axis-aligned rectangle with presentation {W}; the tilted rectangle has the same presentation; contradiction. (c) follows.

THEOREM 4 = (P2). Take an equality board of width m = m_h (K4). It has exactly q doubles (K2). Group them into maximal runs of consecutive columns. Each run has at most k-1 columns, so there are at least ceil(q/(k-1)) runs, and two runs are separated by at least one singleton column. So there are at least ceil(q/(k-1)) - 1 = floor((q-1)/(k-1)) singleton columns and m >= q + floor((q-1)/(k-1)).

COROLLARY 5 = (P3). If an equality board has k consecutive double columns, translate them to columns 1..k. Their row pairs are distinct edges of K_{A,B} (K2), and by Proposition 3(c) every tilted rectangle inside has at most two black corners. So they form an N-window and k <= W_N(h). Apply Theorem 4 with k = W_N(h) + 1. Remark: the cyclic staircase {(i,i),(i,i+1): 1 <= i < h} plus (h,h),(h,1) has no tilted rectangle with three black corners (archive: continuation_cyclic_staircase_obstruction.md, Section 2); its pairs {i,i+1} are parity edges and {1,h} is one for even h. So W_N(h) >= h-1, and >= h for even h.

LEMMA 6 (ray rules) = first part of (P6). Let every 45-degree rectangle of the h x k grid have at most two corners in P, Z = (x,y) in P; the span of a ray is the least i >= 1 with Z + i d in P. (a) NE and SE rays meet P with spans s, t => x+s+t > k. (b) NW and SW => x-s-t < 1. (c) NE and NW => y+s+t > h. (d) SE and SW => y-s-t < 1. Proof of (a): Z, Z+s(1,1), Z+t(1,-1) are in P; the fourth corner Z+(s+t, s-t) has a row between y-t and y+s; if x+s+t <= k it is a grid point and a 45-degree rectangle has three corners in P. The other cases use the fourth corners Z+(-s-t,s-t), Z+(s-t,s+t), Z+(s-t,-s-t). In (a), (b): s <= h-y, t <= y-1, so s+t <= h-1 and the conclusion fails for h <= x <= k-h+1. Three occupied rays always contain {NE,SE} or {NW,SW}. LEMMA 7 (row form): in (d), s = y-a, t = y-c give a+c <= y; in (c), s = a-y, t = c-y give a+c >= y+h+1.

PROPOSITION 8 = (P4). The two points of a column have rows of different parity, so coordinate sums of different parity: one point per class per column. The corners V, V+s(1,1), V+t(1,-1), V+s(1,1)+t(1,-1) have coordinate sums c, c+2s, c, c+2s: one class. The saturated statement follows with (K2).

PROPOSITION 9 = (P5). Grid points on a line of direction (c,d) form a chain with step (c,d) since gcd(c,d) = 1. A grid point (x,y) is the first of its chain iff x <= c or y <= d. Count: qh - (q-c)(h-d) = qd + ch - cd. For d >= 2: qd + ch - cd - 2q = q(d-2) + c(h-d) >= 0. For d = 1: q + c(h-1) lines, excess of points q - c(h-1). Perpendicular pair (c,d), (-d,c): (c+d)(q+h) - 2cd lines; minus 2q gives (c+d-2)q + (c+d)h - 2cd; minus (2h-2) this is (c+d-2)(q+h) - 2(cd-1) >= 0 because q+h >= 2 max(c,d) and (c+d-2) max(c,d) >= cd - 1.

PROPOSITION 10 = (P7). For even u let f(u) be the v with the point of L on x+y = u lying on x-y = v; its row is (u-f(u))/2, so u-2h <= f(u) <= u-2, and f is a bijection of the even integers. N(c) = #{u > c: f(u) <= c} satisfies N(c) - N(c-2) = #{u > c: f(u) = c} - #{u = c: f(c) <= c-2} = 1 - 1 = 0. A point is counted in N(c) iff x+y >= c+2 and x-y <= c, i.e. iff y-1 >= |x-c-1|. If L is p-periodic, the sum of rows over one period is the number of pairs (u,c), u in the period, c even, f(u) <= c < u; each translation orbit of such pairs has one pair with c in a fixed set of p/2 consecutive even numbers; so the sum is (p/2) N over p/2 points.

COMPUTATIONS (each script < 60 s, command py, no solver). (C1) explore_windows.py mode N extends windows column by column and tests every tilted rectangle (leftmost corner (x,r), sides (a,-b),(c,d), ac = bd) ending in the new column; profile.py is a second implementation by right angles among point triples; both give identical counts of windows by width for the parity bipartition at h = 6, 7, 8 (h = 8: 1,16,240,2856,10392,11130,3260,164,4 for widths 0..8). Maxima: h=4: 4 for {1,3}, 3 otherwise; h=5: 5 for A={1,3},{3,5}, 3 for {2,3},{3,4}, 4 otherwise; h=6: 6 for parity, 4 for {1,4,5}, 5 otherwise; h=7: 7 for A={1,3,5},{3,5,7}, 6 for the other 33; h=8 (windows_h8.py, 35 bipartitions): 8 for eight bipartitions, 7 for 27; h=9 parity: 8. (C2) class_functions.py enumerates the one-per-column class functions of (P4) with a row cap; crosscheck.py compares with brute force from the definition on 8 instances (identical sets); t2_saturated_any.py pairs the classes: functions per class 6, 8, 58, 678, 7220, 339816; pairs with complementary row use 9, 0, 8, 4, 242, 1880; boards 4, 0, 0, 0, 0, 14 for h = 4..9. check_board.py (separate checker from the definition) confirms for the listed h = 9 board: pairs = all (odd, even) pairs, 0 45-degree rectangles with >= 3 black corners, 98 tilted rectangles of other slopes with >= 3 black corners. h9_boards.py: all 14 boards are invalid already for the family of axis-aligned and 45-degree rectangles. (C3) t2_allparts.py and check_board.py: the two listed non-parity boards have 0 45-degree rectangles with >= 3 black corners (and 6, 17 tilted rectangles of other slopes with >= 3 black corners).

WHY THE RIGIDITY DOES NOT CLOSE. (i) By (P5) the only forced incidences are on lines of slope +-1 (about two points per line, forest identity components + empty lines = 2h-2, which is an identity and cannot be violated) and on lines of slope +-1/c, c < about h/4. Two black points on such a line only force other points to be white, which is the default colour; black is forced only by "two per column" and the row degrees. (ii) By (C2), (C3) the 45-degree corner condition is satisfiable at saturation, so the zigzag structure of Section 7 of quadratic_threshold_reattack.md, and anything derived from 45-degree corner triples alone, cannot prove m_h > q_h for all h and all bipartitions. For the parity bipartition it does exclude saturation at h = 5..8; this is a small-height effect of the rigidity of the class functions (their number on a window of width w is 112 for h = 6, w = 12..30, and about 14106 for h = 8, w = 32, 40; sampled functions are periodic away from the ends; at h = 10 the enumeration did not finish and sampled functions change pattern in the middle). (iii) With all slopes the widest N-window has width exactly h for h <= 8 and the staircase shows that no window bound below h-1 is possible; with 45-degree rectangles only, windows reach width 8 of 9 at h = 6 and at least 14 of 16 at h = 8; with only the rectangles having a side (1,e) the window 14 78 67 16 58 34 38 12 18 has width 9 at h = 8 (check_adj.py). (iv) Heuristic: a random-like saturated board has about 2.4 log^2 h tilted corner triples per column against entropy 2 log h per column, so the obstruction is real but only structured windows have to be bounded.

## External results used

- Paper (in repository) papers/extremal/sections/sec3_rowbound.tex, Theorem 'equality structure' and Theorem 'row bound' (via Mantel's theorem, Neuwirth 2001): used as (K2), (K3).
- Paper papers/extremal/sections/sec2_prelim.tex, Lemma 'diff' (equal presentations iff the symmetric difference of corner sets is black): used as (K1).
- Archive research_archive/2026-11-09/full_problem_push/hidden_rectangles_and_exact_hypergraph.md (ledger C1, no fully black rectangle when h, m >= 4): the proof for tilted rectangles is repeated in full, not cited.
- Archive research_archive/2026-11-09/full_problem_push/equality_window_capacity.md (window-capacity theorem): Theorem (P2) is its special case d = k-1, reproved here.
- Archive research_archive/2026-11-11/continuation_cyclic_staircase_obstruction.md, Section 2 (the cyclic staircase has no tilted rectangle with three black corners): cited only for the remark W_N(h) >= h-1.
- No published external theorem beyond those already used by the paper is needed.

## Checks

All scripts are in scripts_lower_bound/ and run with py in under 60 seconds each. (1) explore_windows.py (mode N), windows_h8.py, profile.py: largest all-double window without a tilted corner triple, all balanced bipartitions for h = 4..8 and the parity bipartition for h = 9. Result: maximum width h for h = 4..8; parity: 4, 4, 6, 6, 8, 8. Two implementations give identical window counts by width for parity at h = 6, 7, 8. (2) class_functions.py, crosscheck.py, t2_saturated_any.py, h9_boards.py: saturated parity boards with no 45-degree corner triple: 4, 0, 0, 0, 0, 14 for h = 4..9; enumerator equals brute force on 8 instances; none of the 14 boards at h = 9 is valid. (3) check_board.py: definition-level check of the explicit boards at h = 9 (parity), h = 6 (A = {1,3,6}), h = 5 (A = {1,2}): zero 45-degree rectangles with three or more black corners, but 98, 17, 6 tilted rectangles of other slopes with three or more black corners; the cyclic staircase at h = 8 has zero tilted rectangles with three black corners and one presentation collision. (4) t2_allparts.py: saturated boards with no 45-degree corner triple exist for 7 of 10 bipartitions at h = 5 and 2 of 10 at h = 6, never for parity at h = 5, 6. (5) profile3.py, check_adj.py: with 45-degree rectangles only, windows reach width 8 of 9 (h = 6) and at least 14 of 16 (h = 8); with only rectangles having a side of horizontal extent 1, a window of width 9 exists at h = 8. (6) long_class.py: the number of one-per-column 45-degree corner-free functions of one bishop class is 112 for h = 6 at widths 12, 18, 24, 30 and 14108, 14106 for h = 8 at widths 32, 40. (7) Side tests not used in the statements: K_{2,3} is a corner-free window at h = 7 but not at h = 6 (k23.py); two-per-column sets on four lines of slope 1/2 fail after about c/2 columns (lines_test.py).

## Gaps

- The target is not proved: m_h >= q_h + 1 for all h >= 4, or for all large h, remains open. No lower bound above q_h is proved for any h >= 9.
- The window conjecture W_N(h) <= h (or any bound W_N(h) < q_h) is open for h >= 9. Without it Corollary (P3) gives nothing new.
- The computed statements (C1)-(C3) are exhaustive searches by Python scripts. They have no proof log or independent certificate. Cross-checks: two implementations agree on the window counts for the parity bipartition at h = 6, 7, 8; the class-function enumerator agrees with a definition-level brute force on 8 instances; explicit boards were rechecked by a separate definition-level checker.
- The remark W_N(h) >= h-1 (>= h for even h) cites the archive's cyclic staircase proof. I did not re-audit that proof line by line; I confirmed it by computer for h <= 8.
- The rigidity of class functions (bounded count, periodic bulk) is an observation at h = 6 and h = 8 only. It is not proved, and at h = 10 the data suggest it changes.
- This note does not decide whether the simplified 45-degree variant has threshold above q_h for all h: the searches forbid fully black 45-degree rectangles, which is necessary in the full problem but not in that variant.

## Missing estimate

Window conjecture: for every h >= 5 and every balanced bipartition (A,B) of {1..h}, there is no set P of 2(h+1) points of the h x (h+1) grid with exactly two points in every column, whose h+1 row pairs are distinct edges of K_{A,B}, such that every tilted lattice rectangle of the grid has at most two corners in P. Equivalently W_N(h) <= h. By (P3) it gives m_h >= q_h + floor((q_h - 1)/h) for all h >= 5, which is about q_h + h/4. The weaker statement with width q_h in place of h+1 (no saturated board satisfies the corner condition, W_N(h) < q_h) gives m_h >= q_h + 1. Both hold for h <= 8 by exhaustive search.

## Next steps

- Classify the N-windows of width h and h-1. In all computed cases they are staircase runs with at most two extra columns; a classification would prove the window conjecture by showing that none extends.
- Produce a solver proof log for 'no N-window of width h+1' at h = 9 and h = 10, so that m_h >= q_h + 1 is citable for h <= 10 (the archive has solver runs without logs).
- For the parity bipartition, use the decoupling (P4) to enumerate saturated boards under the 45-degree corner triples plus the mixed 45-degree collisions (types T4, T5) at h = 10, 11, 12. This decides whether the 45-degree family keeps excluding saturation beyond h = 9.
- Study the rigidity of the one-per-column class functions (flow lemma (P7), periodic bulk at h = 6, 8). If such a function is periodic away from two ends of length O(h), long all-double windows of a parity board repeat a row pair, which bounds the window width; the data at h = 10 show that this needs a new idea.
- For non-parity bipartitions add the square conditions (two black points in one row at distance 2k are forbidden when rows y-k and y+k lie in different parts); they cut the saturated boards from 362880 to a few hundred at h = 6 and may give a short proof for those bipartitions.

# Audit

## Verdict

correct

## Summary

I re-read the proofs of (P1) to (P7) line by line against the paper's Lemma diff (sec2_prelim.tex, line 21) and Theorem equality structure (sec3_rowbound.tex, line 82). I found no mathematical error. Three wording points need fixing, all minor. Separately, I wrote my own program from the definitions only and confirmed (C1): W_N(h) = h for h = 4, 5, 6, 7, 8, checked over every balanced bipartition (3, 10, 10, 35 and 35 edge sets) with no symmetry reduction. No bipartition at h <= 8 has an N-window of width h + 1. I also confirmed that the parity bipartition at h = 9 gives 8. The consequence m_8 >= 17 = q_8 + 1 therefore holds. It is computer-assisted: the proof chain is complete, and the only computational input is "no N-window of width 9 at h = 8". The weaker statement "no N-window of width 16" is enough, and it follows by prefix closure. The by-width counts match the earlier own counts exactly (parity bipartition, h = 8: 1, 16, 240, 2856, 10392, 11130, 3260, 164, 4). The bipartitions that reach the maximum width also match the earlier list for every h. I did not audit (C2), (C3), or the archive proof of the cyclic staircase, which is used only in the remark W_N(h) >= h - 1. Those stay undecided from my side, except that my program confirms the staircase windows for h <= 8. The bounds m_5 >= 7, m_6 >= 10 and m_7 >= 13 are weaker than the known m_5 = 8 and m_6 = 15 (paper, Table 1) and m_7 >= 17 (archive, equality_window_capacity.md). This agrees with the claim that only m_8 >= 17 is new. I did not search the whole archive for an older h = 8 bound. The only h = 8 threshold figure I came across, m_8 = 30 in the 2026-11-07 research log, is a pre-registered prediction, not a proof.

## Issues

- location: Lemma 2, case split; severity: minor; description: Case 1 assumes that AC is neither horizontal nor vertical, and Case 2 is written as 'both diagonals are horizontal or vertical'. The proof never says what happens when AC is axis-parallel but BD is not.; fix: Add one sentence: if some diagonal is not axis-parallel, rename the corners so that it is AC and apply Case 1. Otherwise both diagonals are axis-parallel, and since they are perpendicular with a common midpoint and equal length, R is the diamond of Case 2 with integer d.
- location: (P5), first consequence; severity: minor; description: 'A set of 2q points is forced to have two points on a common line only for d = 1 and c < q/(h-1)' is true only in the pigeonhole sense: it counts lines against points. When the number of lines is at least 2q, it does not show that a configuration with no two points on a common line exists.; fix: Write 'is forced by pigeonhole'.
- location: (P6), statement; severity: minor; description: The row rules (a + c <= y, a + c >= y + h + 1) come from parts (c) and (d), which hold for every x. The statement restricts them to h <= x <= k - h + 1, which is needlessly narrow. 'Lower' and 'upper' refer to decreasing and increasing y, whereas the paper puts row 1 at the top. The 'first meeting' qualifier is also unnecessary.; fix: State the row rules for every Z in P, and say that 'lower' means smaller y.
- location: (C1) and the consequence m_8 >= 17; severity: minor; description: The consequence is computer-assisted (exhaustive Python search), with no proof log or certificate. Two independent implementations now agree: the earlier and mine.; fix: Label m_8 >= 17 as computer-assisted, and cite both implementations and the matching by-width counts.
- location: Remark W_N(h) >= h - 1 (h >= 4), W_N(h) >= h (even h); severity: minor; description: This rests on the archive's cyclic-staircase proof (continuation_cyclic_staircase_obstruction.md, Section 2), which neither the note three_term_relations.md nor I audited. It is not used for m_8 >= 17.; fix: Keep it marked as cited. My program confirms it for h <= 8.

## Corrected statement

Proved by hand: (P1) to (P7), with the three minor wording fixes. Computer-assisted, by two independent implementations: W_N(h) = h for 4 <= h <= 8 and W_N(9) restricted to the parity bipartition = 8. Hence m_8 >= 17 = q_8 + 1. Not audited here: (C2), (C3), and the general remark W_N(h) >= h - 1, which is cited to the archive's staircase proof.

## Independent derivation

LEMMA 1. W = (x, rho) is white and (x, s) is black, with s in the part that does not contain rho. By (K2), {rho, s} is a double pair, owned by a column z. z != x, because (x, rho) is white. Then {x, z} x {rho, s} is an axis-aligned rectangle with presentation {W}. In a double column {a, b} with a in A and b in B, exactly one of the two black rows lies in the part that does not contain rho. Correct.

LEMMA 2, CASE 1. A = (x, a), C = (z, c), x != z, a != c. Put P = (x, c), Q = (z, a), and T = APCQ, which is axis-aligned with positive area. PQ, AC and BD share their midpoint and length. If {P, Q} met {B, D}, reflection through the midpoint would give {P, Q} = {B, D}, so R = T, which is not tilted. So U = PBQD is a rectangle. A and C are not in U: A differs from P because a != c and from Q because x != z, and C likewise. Hence T ∩ U = {P, Q}, the symmetric difference is {A, B, C, D}, which is black, and Lemma diff gives the same presentation. Contradiction.

LEMMA 2, CASE 2, d >= 2. Take u = (1, -1), v = (d, d), T = {A, A+u, A+v, A+u+v} and U = {A+u, A+du, A+u+v, A+du+v}. U has sides (d-1)u and v, so positive area. The common corners are A+u and A+u+v, which lie on sides of R and so inside the grid. The symmetric difference is R. Contradiction.

LEMMA 2, CASE 2, d = 1. Here 2 <= x <= m-1 and 2 <= y <= h-1. Since m, h >= 4, one of x ± 1 lies in [2, m-1], and one of y ± 1 lies in [2, h-1]. With u = (σ, τ), w = (σ, -τ) and A = (x-σ, y), I checked that A+u = (x, y+τ), A+w = (x, y-τ) and A+u+w = (x+σ, y). T = R + u is a diamond centred inside [2, m-1] x [2, h-1]. U = {A, A+2u, A+w, A+2u+w} has sides 2u and w. T ∩ U = {A+2u, A+2u+w}, and T Δ U = R. Contradiction. Correct.

PROPOSITION 3. If a tilted rectangle has three black corners and a white corner W in column x, and column x is a double or a singleton whose black row is in the other part, Lemma 1 gives an axis-aligned rival with presentation {W}. Columns are never empty, by (K2)(a). So (b) and (c) hold.

THEOREM 4. In a board of width m_h, the q doubles form maximal runs of at most k-1 columns, so there are at least ceil(q/(k-1)) runs and at least that many minus 1 separating singletons. This gives m >= q + floor((q-1)/(k-1)). It agrees with formula (3) of equality_window_capacity.md at d = k-1: write q-1 = (k-1)a + r; then (3) gives ka + 1 + r = q + a. The run argument does not need that note's range condition m >= k.

COROLLARY 5. k consecutive doubles in an equality board, translated to columns 1..k, have distinct K_{A,B} pairs and no tilted rectangle with 3 or more black corners (Proposition 3). Theorem 4 then applies with k = W_N + 1. Note that W_N(h) < q_h is enough for m_h >= q_h + 1.

(P4). The two points of a column have rows of opposite parity, so one point per column falls in each class of x + y. The corners of a 45-degree rectangle, V + s(1,1) + t(1,-1), have coordinate sums c, c+2s, c, c+2s, so all four lie in one class.

(P5). The chain starts are the points with x <= c or y <= d, which number qh - (q-c)(h-d) = qd + ch - cd. For a perpendicular pair, the excess over 2q, minus (2h - 2), equals (c+d-2)(q+h) - 2(cd-1). This is >= 0 because q + h >= 2M and (c+d-2)M - (cd-1) = (M-1)^2 >= 0, where M = max(c, d).

(P6). The fourth corners are Z+(s+t, s-t), Z+(-s-t, s-t), Z+(s-t, s+t) and Z+(s-t, -s-t). Each has its other coordinate between coordinates of points already in P, so it lies in the grid whenever the stated inequality fails. Since s + t <= h - 1, two east rays cannot both meet P when x <= k-h+1, and two west rays cannot when x >= h. Any three of the four rays include an east pair or a west pair. The row forms follow by substituting s = y - a, t = y - c, and s = a - y, t = c - y.

(P7). N(c) - N(c-2) = #{u > c : f(u) = c} - [f(c) <= c-2] = 1 - 1, because u - 2h <= f(u) <= u - 2. The cone condition is x + y >= c + 2 and x - y <= c, which is equivalent to y - 1 >= |x - c - 1|. For the periodic case, the row of a point equals #{even c : f(u) <= c < u}. Orbits under (u, c) -> (u+p, c+p) give a row sum of (p/2)N over p/2 points.

COMPUTATION. wn.py generates all tilted rectangles as Z, Z+u, Z+v, Z+u+v with u.v = 0 and u not axis-parallel, and checks the result against brute.py's diagonal-pair generator: 278 = 278 on the 7 x 8 grid and 542 = 542 on the 8 x 9 grid, identical sets. The search is a column DFS over unused K_{A,B} edges, up to width min(q, h+1). It asserts that each rectangle has a unique corner in its largest column. Before choosing column x, it counts the old corners of every rectangle whose largest column is x: a count of 3 kills the node, and a count of 2 forbids the row of the rightmost corner. This pruning is exact. brute.py, which tries every permutation of edges with a full recheck, gives identical by-width counts for every bipartition at h = 4 and 5 (all widths) and at h = 6 (widths up to 5).

## Checks

Script folder: scripts_audit_lower_bound_windows/. Scripts: wn.py (DFS), brute.py (permutation brute force), checkwit.py (witness check). I wrote them from the definitions and did not read the wf1/lower_bound scripts. Every run took under 3 s.

Results, maximum width per bipartition (A is the part of size floor(h/2)):
- h = 4: 4 for A = {1,3}, and 3 otherwise.
- h = 5: 5 for {1,3} and {3,5}; 3 for {2,3} and {3,4}; 4 otherwise.
- h = 6: 6 for parity; 4 for {1,4,5}; 5 otherwise.
- h = 7: 7 for {1,3,5} and {3,5,7}; 6 for the other 33.
- h = 8: 8 for 8 bipartitions ({1,3,4,7}, {1,3,4,8}, {1,3,5,7}, {1,3,5,8}, {1,3,6,7}, {1,4,5,7}, {1,4,6,8}, {1,5,6,8}); 7 for the other 27; zero windows of width 9 for all 35.
- h = 9, parity bipartition: 8.

All of these match the claims. Mirror-image bipartitions give identical counts. The parity counts at h = 8 match the earlier numbers exactly. Width-h witnesses, rechecked with the second rectangle generator, all have zero tilted rectangles with 3 or more corners and distinct pairs: at h = 8 these are 12 78 27 35 57 38 23 18 and the cyclic staircase 12 23 34 45 56 67 78 18; at h = 7, 16 56 45 34 23 12 17. Arithmetic: q_8 = 16, floor(15/8) = 1, so m_8 >= 17.

