# The multilevel diagonal tiling as a construction

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: the multilevel tiling holds up as a construction, conditional on the H7 inputs and a per-tile hypothesis, and no interaction between tiles or windows escapes the per-tile analysis. Four bookkeeping errors in the earlier description are fixed, one of them real (the final level overlapped level K-1). The exponent stays b = 1 (width h^2 log h). The claim that no tiling can beat b = 1 with degree-counting certificates is a heuristic resting on the random-row model (audit_hilbert_tiling_and_residuals.md). The constant improves if all tiles of a block share one window, and further with one core per block and graded choice counts. Audited in audit_hilbert_tiling_and_residuals.md (correct with fixable gaps).

# Result

## Status

proved

## Summary

The C4 multilevel tiling holds up as a construction, conditional on the unaudited H7 inputs (A) and a per-tile hypothesis. I found no interaction between tiles or windows that the per-tile analysis misses. I proved a conditional assembly theorem. C4 as written has four bookkeeping errors, all now fixed. One is real: the final level overlaps level K-1, which would place some labels twice. The exponent stays b = 1, and no tiling can beat b = 1 with degree-counting certificates. The constant improves a lot if all tiles of a block share one window, and improves further with a single core per block that uses graded choice counts.

## Statements

Notation. H = ln h. D = 2W_h + 1 <= (h-1)^2/2 + 3. Block b is one of the 196 residue blocks of H7. It has rows a = a0 + 28i and b = b0 + 28j, profile pi_b (AP4) and padded side Q = Q_b, a power of two with Q^2 <= (h+28)^2/196. r is the Hilbert rank of H_Q (recursion (2) of continuation_hilbert_placement.md). A TILE of block b is a set c of non-exceptional labels of b inside one aligned dyadic square sq_c of side l_c = 2^m. The rank block of that square is [beta_c l_c^2, (beta_c + 1) l_c^2). The tile has a stride S_c = 6272 sigma_c (sigma_c a power of 2), a choice count M_c >= 1, and private choices 0 <= xi_e < M_c. Label e in c gets the column x_e = x_c + S_c(M_c(r_e - beta_c l_c^2) + xi_e), with 7 | x_c. C_c is the infinite periodic sea s_{pi_b} with the doubles of c substituted. "xi avoids the six families on c" means C_c has no support of type (P), (Lambda3), (Lambda4), (R2s), (FW) or (6PT) with at least 2 labels of c (H7 definitions).

HYPOTHESIS (A), unchanged from C1 and C4: Lemma AP4; N1 Claims (a)-(e) and Lemmas C and TR, with Hilbert cores; Theorem H7 with Lemmas S1-S6 (completeness, read per core); the positional lemma for exceptional labels. These are all unaudited. Also used, and audited: T1 one-label substitution, J5 (A9), the paper's 2W_h+1 locality, and criterion (V1)-(V5).

THEOREM T (tiled assembly; conditional on (A); proved below; not audited). Let h >= h0. For each block b, partition its non-exceptional labels into tiles c (any partition into subsets of aligned dyadic squares). Suppose every tile has a choice vector xi^c that avoids the six families on c. Build block b's single window as: row h | BL4 left collar | the nonempty tile cores in any order, with consecutive cores separated by D_c in [D, D+6] columns of s_{pi_b}, where D_c is chosen so that 7 | x_c | BL4 right collar | row h. Keep everything else as in H7: the exceptional-label windows, the switch z, BL6 separations of at least D, and J5 gluing. Then for every m >= M* the board truncated to columns 1..m is a valid blackout with m + q_h points, where
 M* <= sum_c S_c M_c l_c^2 + (D+6) sum_b (t_b - 1) + C1 h^2,
t_b is the number of nonempty tiles of block b, and C1 h^2 is the H7 overhead (196 pairs of collars, about 1.54e5 h^2, the exceptional labels and the BL6 gaps). VARIANT: if each tile instead gets its own window with its own BL4 collars, the board is also valid, and each extra window costs at most 1571 D, about 786 h^2.

COROLLARY C4' (C4 corrected). Put K = ceil(log2 H), so H <= 2^K < 2H, and l_k = Q 2^(-k).
- Levels k < K hold the labels with l_k/2 <= |j-i| < l_k. Level K holds the labels with |j-i| < l_K. Note: not |j-i| < Q/log h, which overlaps level K-1.
- The tiles of level k are the 3*2^k - 2 aligned squares of side l_k with |p - q| <= 1. Each tile holds the labels of its level that lie in its square.
- Strides: S_k = 6272 * 2^ceil(log2(k+1)) * sigma0, and S_K = 6272 * 2^K * sigma0.
Assume (A) and the following.
(G) A level-k tile admits an avoiding choice vector whenever M > c0 + c1 (k+1) H / S_k for k < K, and whenever M > c0 + c1 H^2 / S_K at level K.
Take sigma0 = 2^ceil(log2 max(1, c1 H/6272)) and M = floor(c0) + 2. Then
 m_h <= 13 * 6272 * sigma0 * M * (h+28)^2 + 1176 h^2 H + O(h^2) <= 26 c1 (c0+2) h^2 H (1 + o(1)) + 1176 h^2 H + O(h^2).
So m_h = O(h^2 log h), exponent b = 1. The number of tiles per block is 3*2^(K+1) - 2K - 5 < 12 H, and there are fewer than 2352 H tiles in all. With one window per tile the extra collars cost about 2352 H * 786 h^2, about 1.85e6 h^2 H.

THEOREM G (graded single core; conditional; same proof). Keep one Hilbert core per block, as in H7, at a fixed stride S = 6272 sigma. Give rank r a choice count M_r >= 1 and the column x_r = x_0 + S(R_r + xi_r), where R_r = sum over r' < r of M_r' and 0 <= xi_r < M_r. Then every H7 per-core tool still holds: (Hil) x_f - x_e >= S(r_f - r_e), S | X, (Al) and (Bulk). Assume (A) and the following.
(G_gr) The core admits an avoiding choice vector when M_e = floor(c0) + 1 + ceil(c1 (k_e+1) H / S) for labels of level k_e < K, M_e = floor(c0) + 1 + ceil(c1 H^2 / S) at level K, and M_r = 1 on unused ranks.
Then m_h <= (6272 sigma (floor(c0)+2) + 6 c1 H)(h+28)^2 + C1 h^2. No windows are added beyond H7's. The leading coefficient is 6 c1 against about 13 c1 (c0+2), or 26 c1 (c0+2) after rounding sigma0 to a power of two, for C4'.

PROPOSITION F (heuristic floor; not a theorem). Every certificate of degeneracy type, whether greedy with M_e > (forbidden count) or criterion (8) M > 8 max_U avg F_U, applied to any tiling or grading of this kind, gives width at least c h^2 log h. So b = 1 is the floor of this route. The premise is the unaudited P count T2 (mean P degree about (16/(pi S)) log(4h/S^2) for bulk labels).

## Proofs

1. TILES ARE HILBERT SQUARES WITH ORIGINAL RANKS. Recursion (2) maps H_q onto the four aligned quadrants of the 2q-square. By induction, every aligned dyadic square of side 2^m is visited by exactly one aligned rank block [beta 4^m, (beta+1) 4^m): the aligned rank blocks visit aligned squares, and the two families are equinumerous. Inside a tile, r' = r - beta l^2 differs from the original rank by a constant. So every rank difference is the original one, and locality (1), max(Δi^2, Δj^2) < 16|Δr|, holds verbatim. For r_f > r_e in c, x_f - x_e = S_c(M_c Δr + xi_f - xi_e) >= S_c(M_c(Δr - 1) + 1) >= S_c Δr. This is (Hil) with sigma = sigma_c: y^2 < 16 * 28^2 Δr = 2 S_c Δr / sigma_c <= 2|X| / sigma_c.
Every label column is x_c plus a multiple of S_c. Since 6272 = 2^7 * 7^2, v2(X) >= v2(S_c) and 49 | X. Since 7 | x_c, every label and slot column has period zero, so T1 and AP4 one-label substitution applies. Every unused slot is a 7 | x column and holds F. The rows of c are those of block b, so they are fixed mod 28, hence mod 4 per parity, and (Al) holds. Exceptional labels are removed before tiling, so (Bulk) holds.
I read the H7 proofs, S1 to S6 and the completeness step. They use only (Hil), S | X, 49 | X, (Al), (Bulk) and mod-7 residues. They never use the base rank, the full square or a uniform M. The one exception is the threshold remarks: angles_mixed Theorem 1 uses M through lambda|a| >= M(t-1) + 1, which with graded M holds with M_min. Those thresholds are not used in the board statement. So H7's per-core reduction applies to each tile, and also to the graded core of Theorem G, where R_f - R_e >= M_e + (Δr - 1) gives x_f - x_e >= S Δr.
Self-checked by script check_tiling.py: aligned squares are aligned rank blocks, and (1) holds, for q <= 64.

2. PARTITION. Fix the level k from |j-i|. The levels are disjoint and cover [0, Q). Then (p, q) = (floor(i/l_k), floor(j/l_k)) is unique. If |p - q| >= 2, then |j-i| > (|p-q| - 1) l_k >= l_k. So every label at level k lies in a square with |p - q| <= 1, and there are 2^k + 2(2^k - 1) = 3*2^k - 2 such squares.
So every non-exceptional label lies in exactly one tile, and by N1 Claims (a) and (b) each parity edge is exactly one double. Script check: exact partition for Q up to 512.
The literal C4 rule is wrong here. Its final level is |j-i| < n/log h, while 2^(-K) <= 1/log h. So labels with Q 2^(-K) <= |j-i| < Q/log h belong to both level K-1 and level K. Their parity edge would be placed twice, which creates a 4-cycle in G_S and breaks the reduction lemma. The fix is the final level |j-i| < Q 2^(-K).

3. EACH CORE IS CLEAN. Take a violation of C_c (V1 to V5; points include W and the black points of W's column).
- 0 labels: the sea s_pi is clean (T1 and AP4).
- 1 label: one-label substitution (T1 and AP4).
- At least 2 labels: by H7 completeness, applied to this core through Step 1, it lies in one of (P), (Lambda3), (Lambda4), (R2s), (FW) and (6PT), which xi^c avoids.
So C_c is clean.

4. NO CROSS-TILE OR CROSS-WINDOW INTERACTION. Every obstruction (paper sec5 lines 29-36), every V2 configuration (a rectangle and W's column) and every V3 pair (two tilted rectangles through one W, each of span at most W_h) lies in D = 2W_h + 1 consecutive columns, so its span is at most D - 1.
Suppose a violation Q has a point in core K_c. Then Q lies in K_c^+ = K_c widened by D - 1 on each side. Separations of at least D columns, and the first collar stage P of length D, keep K_c^+ free of other label columns and of collar stages. On K_c^+ the block equals C_c, because the separation columns carry the same global periodic s_pi (core starts satisfy 7 | x_c). So Step 3 excludes Q.
If Q meets no core, the block agrees with the label-free block B0 on Q's columns, and Lemma C excludes it. The collars are unchanged from H7, and they also cover Lemma TR's stages.
This settles the question of supports with label points in two tiles. Any such support would span more than D - 1 columns, so it cannot be a violation. The same holds for W in another tile's column, since W is a corner of the rectangle. The per-tile analysis is complete.
The non-monotone families (FW, 6PT, R2s with F at emptied slots) are not an assembly issue. Each tile has one fixed occupancy state, and the hypothesis is stated for that state. Cross-block and cross-window interactions are excluded by J5, as in H7: windows are more than 2W_h apart, and outside the windows rows 1 and h form a chain with no rival pair. The 196 blocks keep their own profiles and collars, unchanged.

5. GLUING. N1(c) gives row-h tails. Steps 3 and 4 make every block window clean. BL6 separations and the switch z are as in H7. J5 then gives validity of the union and of every truncation. The variant with one window per tile is the same argument with one core per block.

6. WIDTH OF THEOREM T. The core of c spans S_c M_c l_c^2 columns. Separations cost at most D + 6 each, and there are t_b - 1 of them in block b. The rest is H7's overhead.

7. WIDTH OF C4'.
- Level k has (3*2^k - 2) l_k^2 = Q^2 (3*2^(-k) - 2*4^(-k)) ranks.
- Sum over k < K of (3*2^(-k) - 2*4^(-k)) * 2^ceil(log2(k+1)) = 9.9803 < 10 (computed exactly). The 24 in the synthesis is a loose bound, because level 0 is one tile, not three.
- The final level has (3 - 2^(1-K)) Q^2 2^(-K) ranks at stride 6272 * 2^K * sigma0, which is less than 3 * 6272 sigma0 Q^2.
- So the cores of one block span less than 13 * 6272 sigma0 M Q^2, and summing over blocks (sum of Q^2 <= (h+28)^2) gives less than 13 * 6272 sigma0 M (h+28)^2.
(G) applies:
- For k < K, S_k >= 6272 (k+1) sigma0, so c0 + c1 (k+1) H / S_k <= c0 + c1 H / (6272 sigma0) <= c0 + 1 < M.
- At level K, S_K >= 6272 H sigma0, which gives the same bound.
Since sigma0 < 2 c1 H / 6272 once c1 H > 6272, the cores span at most 26 c1 (c0+2) H (h+28)^2.
Tiles: the count per block is the sum over k <= K of (3*2^k - 2) = 3*2^(K+1) - 2K - 5 < 6*2^K < 12H. The synthesis's 6 log h per block assumed 2^(K+1) <= 2 log h, which fails when 2^K > log h. The correct bound is fewer than 2352 H tiles in all. Separations cost at most 2352 H (h^2/2 + 9), about 1176 h^2 H.
Collars per window are 2(2 + h - H_row) D <= 1570 D, with h - H_row <= 783 from AP4, plus a BL6 gap D. So C4 as literally written, with one window per tile, costs about 1.85e6 h^2 H in collars. That is O(h^2 log h), but it is larger than the 1176 h^2 H of separations, and the synthesis left it uncounted ("O(h^2) per window").

8. WIDTH OF THEOREM G. Write L_k for the labels of level k.
- For k < K: |L_k| = 2 * sum over d in [a, 2a) of (Q - d) <= 2aQ = Q^2 2^(-k), with a = Q 2^(-k-1).
- At level K: |L_K| < 2Q^2 2^(-K) <= 2Q^2 / H.
- So the sum of M_r is at most (floor(c0) + 2) Q^2 + (c1 H / S)(Q^2 * sum over k of (k+1) 2^(-k) + H * |L_K|) <= (floor(c0) + 2) Q^2 + 6 c1 H Q^2 / S.
- Multiplying by S and summing over blocks gives the bound.
The reason G does better: C4' multiplies the c0 term by a stride of order H and wastes ranks, since a tile spans about 3 times as many ranks as it has labels (4 times at level 0; script rank/used ratios 3.9, 3.2, 3.1, 3.0). G pays order H only per label actually present.
A finer tiling helps C4' a little. Level-k labels lie in the squares of side l_k/2 with |p - q| in {1, 2}, which cuts the waste from 3 to 2, at the cost of about 8*2^k tiles per level.

9. PROPOSITION F (heuristic). Each label's cost is at least S_e M_e. A greedy certificate needs M_e larger than e's forbidden count, and criterion (8) at U = everything needs M > 8 avg F. By T2 of hilbert_p_family_counts (unaudited), the average forbidden count over bulk labels is of order (1/S) log(4h/S^2), and it is roughly independent of M. Bulk labels (|b-a| >= h/2) are a positive fraction of all labels. So the average of S_e M_e is at least c H for any strides, choice counts, levels or tiling.
Tiles cannot cut enough partners to change this. Each window or separation costs at least D, about h^2/2, so width h^2 (log h)^b allows at most O((log h)^b) tiles per block, each of side at least Q (log h)^(-b/2). P partners lie within O(sqrt(h/(S M))) of each other in coordinates. So the labels near a tile boundary are an o(1) fraction, and the average degree drops by o(1).
Getting below b = 1 needs a structural bounded-M theorem (synthesis step 7), not a better tiling.

## External results used

- Paper sec5_threshold.tex, lines 29-36: every obstruction lies in 2W_h+1 consecutive columns, because a tilted rectangle spans at most W_h columns. V2 and V3 configurations follow, since each consists of rectangles through one W.
- full_layout_junctions.md J5 (audited A9): windows more than 2W_h apart, each violation-free with constant tails, together carrying each parity edge once, glue to a valid board and every truncation.
- block_layout_n1.md (unaudited): BL3 separations of at least D, the BL4 collars, Claim (d) confinement and Lemma C.
- continuation_hilbert_placement.md (audited): recursion (2), locality (1), and validity for subsets with original ranks under x_f - x_e >= 8d^2 Δr.
- hilbert_sea_design_h7.md (unaudited): the tools (Hil), (Al) and (Bulk), Lemmas S1-S6, and completeness.

## Checks

I checked these by hand:
- aligned dyadic squares are aligned rank blocks, so original ranks are kept up to a shift;
- (Hil) for tile-relative ranks and for graded choice counts;
- that the H7 tools need nothing global;
- the partition, and the overlap bug in C4's final level;
- confinement through 2W_h+1 locality (V2 and V3 included);
- the BL3 separation length and the period-zero alignment of core starts;
- the J5 hypotheses;
- every width sum: tile counts, the collar cost per window, the C4' and G constants, and the level-size bounds.

One script, check_tiling.py in the script folder, ran with py in under 10 s. It confirms that aligned squares are aligned rank blocks and that locality (1) holds, for q <= 64. It confirms the exact partition into tiles and the tile count 3*2^(K+1) - 2K - 5, for Q up to 512 (37, 83, 177). It gives rank-to-label waste ratios of 3.9, 3.2, 3.1 and 3.0 by level. A short py one-liner gave the exact stride sum, 9.9803.

## Gaps

- Every board statement still rests on (A): Lemma AP4, N1 with Hilbert cores (Claims (a)-(e), Lemmas C and TR), and Theorem H7 with S1-S6. None of these is audited. Step 1 rests on my reading of the H7 proofs: that they use only (Hil), S | X, 49 | X, (Al), (Bulk) and residues mod 7. A second reader should confirm this, especially for S4-S6 and for completeness.
- Hypothesis (G) (for C4') and hypothesis (G_gr) (for Theorem G) are unproved for all six families. For R2s, FW and 6PT there is not even a heuristic band profile. G_gr also assumes that the forbidden counts do not depend on the profile of choice counts, and that cross-level partners inside one core do not raise them. In the tiling, different levels never interact, so this is an extra assumption.
- The factor-one and finite-factor theorems, inputs to any future proof of (G) for P, are written for a uniform M. They transfer to tiles unchanged (they use only rank differences). For the graded core of Theorem G they need to be re-derived.
- Proposition F is a heuristic. It rests on the unaudited P count T2 and on the equidistribution of Hilbert partner offsets. It does not rule out structural, non-counting certificates.
- No explicit h0. I did not check the exceptional-label windows or the switch-z junction beyond citing H7 and N1(e). The constant C1 (about 1.6e5 plus the exceptional-label constant) is inherited.
- The sanity script checks only the Hilbert block structure and the tile partition, at small Q. No board was built and no per-tile family was censused.

## Missing estimate

C4' needs (G), and Theorem G needs (G_gr): the per-tile (or per-label) forbidden-choice count for P, R2s, FW, 6PT, Lambda3 and Lambda4 must be at most c0 + c1 (k+1) log h / S at level k, and at most c0 + c1 (log h)^2 / S at the final level. For FW, 6PT and R2s this count must be taken in the tile's actual occupancy state. The assembly itself adds no estimate. Below b = 1, a structural bounded-M theorem is needed.

## Next steps

- Replace C4 in the synthesis with C4'. Use the final level |j-i| < Q 2^(-K), at most 12 log h tiles per block, one window per block with BL3 separations, and the constant 13 (26 after rounding sigma0).
- Prefer Theorem G (graded single core). It adds no windows, and its leading coefficient is 6 c1 rather than about 13-26 c1 (c0+2). First re-derive the factor-one and finite-factor theorems for graded M.
- Have a second reader audit Step 1: that the H7 per-core proofs use only (Hil), S | X, (Al) and (Bulk), with no uniform M and no full square.
- Census P and R2s forbidden counts by level in a real H7 block (S = 6272) under both the tiled and the graded layouts. This tests whether cross-level partners in the graded core change c1.

