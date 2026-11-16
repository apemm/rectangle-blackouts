# A sawtooth filler layer

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: a 4-row sawtooth filler layer (SAW) removes S2 and the BH16m4 family for every label. With classes split by i mod 16, p = +-2 (mod 5) and 2^nu >= K, it also removes S5 and a thick 45-degree family T2. The remaining families are bounded only by computation. Not audited yet.

# Result

## Status

partial

## Summary

A 4-row sawtooth filler layer (SAW) meets conditions (1)-(3) with proofs, and (4) by computation. It removes S2 and the BH16m4 tilted family for every label. With three constant-cost layout changes (classes split by i mod 16, p = ±2 mod 5, 2^nu >= K), S5 and a new thick 45-degree family T2 are also removed. In a census up to h = 401, only families with a vanishing per-label load (rival pairs, M2c) remain.

## Statements

Setting: the rigid stride-4 layout of item (2), with the region types of sea_row3_split.md Corollary B. Euclidean coordinates for odd deep points: (4n, y) with y = r1 (mod 8) maps to (n, Y), where Y = (y - r1)/4. This is a similarity with factor 4, so every rectangle, right-angle or mixed-quadruple condition among odd deep points becomes the same Euclidean condition on (n, Y), up to grid bounds. Odd label points lie on lines Y = (n - n0)/2, at n = n0 (mod 8).

DEFINITION (SAW). Fix a region type. All its label columns have n = rho0 (mod 4), and T* = max{y <= h : y = r1 (mod 16)}. The filler in deep column 4n gets row
 y(n) = T* - 24, T* - 16, T* - 8, T* for n - rho0 = 0, 1, 2, 3 (mod 4).
In Y units relative to the band this is H = (-2, 0, 2, 4). Holes (even offsets) have Y = 2 (mod 4) and bases (odd offsets) Y = 0 (mod 4). The same rule fills block zones and gaps, so a zone needs no join to a gap. For row-3 types the rule is the same with r1 = 1 (mod 4), as in Corollary B. That gives 4 filler rows per region type.

THEOREM 1 (SAW; proved). Assume T* - 24 > (h+1)/2 (true for h >= 80). Then:
(1) every odd deep row is = r1 (mod 8), and label odd rows are = r1 (mod 16);
(2a) no two fillers form a Pythagorean same-parity pair. So no deep M2a has two filler ends, and no witness condition among fillers is needed;
(2b) for every odd label point C and filler D with D - C Pythagorean (Lemma A2), the two witness columns have different filler rows. The only exception is a witness column that is a label column whose odd row is a filler row; those labels lie in the band and are relocated. This removes S2;
(3) three fillers never form a tilted right angle. There is no Pc, Pb, Pa, X1 or X2 triple with two fillers, so there are no parked filler triples at all, and (3) holds vacuously;
(4') the pure SAW gap with its row-1 (or row-3) sea satisfies (V1)-(V5). There is no filler-only mixed quadruple, no M2c with two fillers, no shallow M2a, no M1C and no filler rival pair;
(5) the BH16m4 failure family T1 and the even-label short-side family CE (Lemma 2) do not occur;
(6) at fixed row choices, every other one-label quadruple with filler side AB and diagonal (label, filler) satisfies a nondegenerate square condition. Such quadruples hit O(sqrt h) labels per diagonal. This holds for labels more than about 80 rows below the band; nearer labels, O(1) per diagonal, are relocated.

LEMMA 2 (CE, the even-label short-side family; proved). Let fillers P and Q differ by (4g, dy) with dy != 0. If v2(dy) >= 4 + v2(g), then for a positive fraction of even label points E there is a fatal tilted rectangle P, Q, Q + w, E with w perpendicular to PQ. If v2(dy) <= 3 + v2(g) for every filler pair, no tilted rectangle has black corners {E, F, F'} with E an even label point below the band. This kills the two-row design with rows 16 apart (Q4): adjacent slots have dy = 16.

LEMMA 3 (structure; proved). Call a layer hole-generic when every non-label deep slot holds one filler. Suppose such a layer, with rows = r1 (mod 8), satisfies CE and robust Pc-freeness (v2(dy) not in {v2(g)+1, v2(g)+2}). Then consecutive slot steps are either all 0 or all odd multiples of 8. If all steps are +-8, the layer is 4-periodic and is BH16 (two rows) or the triangle wave L, L+8, L+16, L+8. BH16 fails S2 (deep_layer_bh16.md) and the triangle wave fails T1, both thickly. So under these conditions a working layer needs at least 3 rows and a step of 24. SAW is such a layer.

LEMMA 4 (S5 removed by the layout; proved). In the rigid layout:
(a) if p = +-2 (mod 5), no two odd label points in different blocks form an A2 pair;
(b) if n(c) = kappa (mod 2^nu) with 2^nu >= K, no two even label points in different blocks form an A2 pair.

PROPOSITION 5 (T2; proved). Labels A and C = A + (-8t, -4t) (Euclidean, same class) and fillers B = A + (-10t, 10t), D = A + (-6t, 10t) in one row form a black mixed quadruple. In SAW this happens for t odd and Y_A = 2 - 10t (relative), which is 1/5 of the labels times the probability that the partner is in the class: thick. Splitting classes by i mod 16 removes T2. In a period-4 layer with the forced parity classes, T2 is present whenever classes contain slot differences of 8 times an odd number. Raising the period to 8 forces a filler pair of vector (4, -8) (Lemma 3 rules), and such a pair creates the label-line family LL, which kills every pair of consecutive labels on a class line through its midpoint.

COROLLARY 6 (conditional cost). Use SAW, classes split by i mod 16, M_c mod 4 fixed per type, p prime in (20h, 40h] with p = +-2 (mod 5) (exists for h >= h0 by the prime number theorem in arithmetic progressions), and 2^nu >= K. Relocate the O(h) labels within about 104 rows of the band. Then S1, S2, S5, T1, T2, X1, X2, M1C and every filler-only obstruction are absent. The width is at most 64(160 h^2 B' + 2h) + O(h^2), with B' <= 2 max_T chi_T. This is O(h^2) if chi(Gamma) < infinity. The construction is still not a full valid board, because the residual families are not bounded by proof (see Gaps).

## Proofs

0. NOTATION. A deep pair C, D with D - C = (4delta, 2eps) and eps = 0 (mod 4) has, by Lemma A2 of deep_layer_bh16.md (re-derived here), Euclidean form D - C = (delta, dY) with eps = 2 dY. Write m = dY/2. The pair is Pythagorean iff delta^2 + 4m^2 = L^2. Then (L - delta)/2 = g1 and (L + delta)/2 = g2 with g1 g2 = m^2, and the witnesses sit at slots n_C - g1 and n_C + g2. For m odd, g1 = g2 (mod 8), because x^(-1) = x (mod 8) for odd x. If m = +-1 there is no solution with delta != 0. SAW heights by offset are -2, 0, 2, 4. Their differences: offset difference 1 or 3 (mod 4) gives dY in {+-2, +-6}; difference 2 gives dY = +-4; difference 0 gives 0.

1. THEOREM 1(1). The rows T* - 24k are = r1 (mod 8), and labels have 2i + 1 = r1 (mod 16).

2. (2a) A filler pair has dY = +-2 (m = +-1: never Pythagorean), dY = +-4 at odd offset distance, or dY = +-6.
 - dY = +-4: m = 2, g1 g2 = 4 gives delta = 3, which is odd. But dY = +-4 occurs only at offset distance 2 (mod 4). Contradiction.
 - dY = +-6: g1 g2 = 9 gives delta = 8 = 0 (mod 4), so the heights are equal. Contradiction.

3. (2b), the proof that kills S2. C is a label point (offset 0, Y_C = 0 mod 4) and D a filler at offset delta.
 - D at an even offset: Y_D = 2 (mod 4), so m is odd, so g1 and g2 are odd with g1 = g2 (mod 8). The witnesses lie at offsets -g1 and g2 = g1 (mod 4), which are {1, 3}. Their heights are 0 and 4, which differ. Odd offsets are never label columns.
 - D at an odd offset: m is even and delta is odd, so exactly one of g1, g2 is odd and the other is = 0 (mod 4). One witness is a base (Y = 0 mod 4). The other sits at offset 0 (mod 4): a hole (Y = 2 mod 4, so the rows differ) or a label column. A label column can share a row with the base only if its odd row is a filler row; that label lies in the band and is relocated.
 - Pythagorean with D at an even offset and m even is impossible, because holes are = 2 (mod 4).
 The proof uses only the parity classes and H(1) != H(3).
 Check: vpat.py found 0 failures among 4339 Pythagorean label-filler pairs for SAW, against 738 for BH16.

4. THEOREM 1(3).
 Right angles. For three fillers we need a1 a2 = -e1 e2 with ai, ei != 0.
 - Both legs odd: e1 e2 is a sum of products in {4, 12, 36}, which is even, but a1 a2 is odd.
 - One leg odd and one = 2 (mod 4): v2(a1 a2) = 1, but v2(e1 e2) = 3.
 - Both = 2 (mod 4): v2(a1 a2) = 2, but e1 e2 = +-16 has v2 = 4.
 So no filler right angle exists: no FFF and no fully black filler rectangle.
 Shallow corners (Theorem 1 of block_sea_classification.md, audited):
 - Pc: 4 a gamma = f g with v2(f) = 1. The pairs (g, v2(gamma)) are (8, 0), (24, 0) and (16, 1), and each gives v2(a) = 2, so a = 0 (mod 4): no Pc.
 - X2 needs y_V = 1 (mod 4), X1 needs y_G = 5 (mod 8), and Pa needs even rows; none of these occurs.
 - Pb has W in row y_F + y_G - 1 > h.

5. (4') Pure gap.
 Mixed quadruples with four fillers: |AB| = |CD|, and modulo 32 the norm classes are 5 (mod 8) for an odd leg, 20 for a leg = 2 (mod 4), and 0 (mod 16) for a horizontal leg. So the two sides have the same type.
 - Horizontal type: Sigma n = 0 and |U| = |delta| force {c, d} = {a, b}.
 - Type 2 (mod 4): if Sigma Y = 0 the same holds. Otherwise U = +-2 and Sigma n = +-8, which puts C and D at the residues of A and B, so Sigma Y = 0: a contradiction.
 - Odd type: if Sigma Y != 0 then |U| <= |Sigma Y e| <= 72. If Sigma Y = 0 then U^2 - delta^2 is 0 or +-32, and (|U|, |delta|) is (9, 7) or (7, 9). The bounded cases were checked by exact enumeration (vpat.py and verify_saw.py): 0 solutions.
 M2c with two fillers (Theorem 2 of block_sea_classification.md). Here e is in {4, 8, 12}, v2(u2) = 1 and v2(n1) is in {v2(e), v2(e) + 1}. In each of the 6 cases, v2 of n1((Delta - n1)^2 + e^2) is 8, 6, 11, 9, 8 or 6, while v2 of e u2 (Delta - 2n1) is 5, 5, 7, 7, 5 or 5. They never match.
 Other families: shallow M2a needs eps != 0 (mod 4) (A1); M1C needs y_D = 1 (mod 4); rival pairs need an odd row difference.
 Computation: board.py found the pure gap clean at h = 57 and 121.

6. (5) and (6). Take C a label, D a filler, and A, B fillers with e = Y_B - Y_A != 0. Perpendicularity gives U = Sigma Y e / k with Sigma n = -k, and Sigma Y = -dY + s0, where s0 = 2Y_D - Y_A - Y_B. Since U^2 >= dY^2 - e^2, we get |k| <= |e| for dY >> e.
 - k = +-e: then delta^2 = e^2 + s0^2 - 2 s0 dY.
   - s0 = 0 gives the thick family T1: delta = +-e, U = +-dY, and A, D, B heights in arithmetic progression. SAW has no AP whose midpoint is the height at offset 0 (the only APs are (0,2,4) with midpoint 2 at offset 2, and (-2,0,2) with midpoint 0 at a base), and T1 needs D at C +- 4, which is offset 0. So T1 is empty (vpat.py e_T1 = 0).
   - s0 != 0: a linear expression in dY must be a square, which gives O(sqrt h) labels per diagonal.
 - |k| < |e|: X^2 = ((e/k)^2 - 1) dY^2 + ... For e <= 6, (e/k)^2 - 1 is never a rational square, so this is a Pell equation with nonzero right side and O(h^o(1)) solutions.
 - Label in {A, B} with C, D fillers: q = B + n lies above the grid once the label is more than 80 rows below the band.
 BH16m4 (heights Y_h - 2, Y_h, Y_h + 2) is exactly T1: the census gave 32 FF/Fo for 16 labels at h = 321.
 CE (Lemma 2): w = t(dy, -4g)/G. E is even iff 4gt/G is odd, and E is deep iff v2(t dy/G) >= 2. Together these need v2(dy) >= 4 + v2(g). Then W = E + (Q - P) is an even point in a filler column, fatal by the axis owner lemma. SAW has v2(dy) = 3 + v2(g) for all pairs.

7. LEMMA 3. With every non-label slot a filler, CE at g = 1 gives steps in {0} union 8*odd. If one step in a 3-chain is 0 and the other is 8*odd, the pair at distance 2 has v2 = 3, which is forbidden (it needs 0 or 4); so the steps are all 0 or all nonzero. With +-8 steps, 4-windows must sum to 0 or +-4, which forces sigma5 = sigma1. Bounded height forces period sum 0, which leaves +-+- (BH16) or ++-- (triangle wave). The triangle wave with labels at M: T1 with D at C +- 4 of height M; at L or T: S2-type failures at high 2-adic valuation. Two rows 8*odd apart: robust Pc forces parity-constant heights, so BH16-type, so S2.

8. LEMMA 4.
 (a) 4(Di + DM)^2 + Di^2 = 5 Di^2 (mod p) must be a square. If 5 is a non-residue (quadratic reciprocity: p = +-2 mod 5), then p | Di, so Di = 0, so eps = 0.
 (b) eps - delta = n(c') - n(c) = 0 (mod 2^nu). Write f1(f1 + 4delta) = eps^2 with a = v2(delta) < nu, so v2(eps) = a. The case b = a gives phi^2 + 4phi delta' = 5 (mod 8) against eps'^2 = 1. The cases b > a + 2 and b = a + 2 give valuation contradictions. So v2(delta) >= nu, so eps is in 2^nu Z with |eps| < K <= 2^nu, so eps = 0.
 Check (s5check.py): blocks at p ~ h and 2^nu = K/8 gave 598 odd-odd pairs for p = 4 (mod 5) and 0 for p = 3 (mod 5).

9. PROPOSITION 5. Direct check: |AB|^2 = 200t^2 = |CD|^2, Sigma = (-4t, -4t), which is perpendicular to (-10t, 10t), and p, q lie in the grid. The slots -10t and -6t have the same residue mod 4, offset 2, height 2. So Y_A = 2 - 10t, which is = 0 (mod 4) iff t is odd. With i mod 16 classes, t is even, the offset is 0 and the height is -2, while Y_A would be = 2 (mod 4): impossible. Census Fo/Fo counts (all residue slots occupied): 3 to 8 per 3 diagonals with mod 8 classes, 0 with mod 16 classes (h = 241, 281, 321, 401). A period-8 search (search8.py) gave 512 local candidates. The best one, [-2,0,2,4,-2,0,-6,4], kills T2 but creates FF/oo and oo/FF (33 at h = 241): the LL family.

10. COST. Region types: iota16 (16 values) times M_c mod 4 (4 values) = 64; M_c mod 4 is set by s_c mod 4. Each type is a rigid layout with 2^nu < 2K, so its width is at most 4p 2^nu B' <= 160 h^2 B', where each residue mod 2^nu holds at most 2 diagonals. Buffers add O(h^2), and relocations add O(h^{1.5+o(1)}).

## External results used

- block_sea_classification.md (audited): criterion V1-V5, Theorem 1 (Pa, Pb, Pc, X1, X2), Theorem 2 (M2a, M2c equation, M1C).
- deep_layer_bh16.md (not audited): A1, Lemma A2 (re-derived as g1 g2 = m^2), A3, the BH16 rule and S2.
- sea_row3_split.md (not audited): Theorem A, Corollary B region types, the BH16m4 and even-lattice failures.
- rigid_layout_cross_block.md (audited): n(c) = s_c - M_c = kappa (mod 2^nu), M_c in pZ, Theorem C/5.
- lower_bound_windows.md (audited): axis owner lemma, used for fatality in Lemma 2.
- Paper sec2_prelim.tex and sec5_threshold.tex: Lemma mixedeq, Lemma rival, Lemma sea, Prop. partial.
- Quadratic reciprocity: (5/p) = (p/5). Prime number theorem in arithmetic progressions mod 5 (no explicit bound checked).

## Checks

All scripts are in scripts_deep_rows. Each ran one at a time with py, under 60 s.
- lc.py and lcd.py: a new label-centric numba checker for V1-V5 (all obstructions containing a label point or with W in a label column, plus V3 at their W). It matched board.py exactly on BH16 (3 FF/Fo), BH16m4 (4 FF/Fo, 1 Fe) and Q4 (48 in 6 categories) at h = 57.
- vpat.py, verify_saw.py and search8.py: exact local checks.
- s5check.py: Lemma 4.
- onelabel.py: bad-row sets for M2c and rival pairs up to h = 4001.
- junc.py, pat.py and tp.py: junction and gap tests (board.py, obs.py copies).
Main census (filler-involving and label obstructions per label, near-band labels excluded):
- BH16: 73 per 16 labels at h = 321.
- BH16m4: 45 per 16.
- SAW with mod 8 classes: 37 per 29 (h = 241) and 18 per 19 (h = 361).
- SAW with mod 16 classes: 5 per 11 (h = 241), 13 per 16 (h = 321), 9 per 10 and 2 per 8 (h = 401), only rival pairs plus at most 1 M2c or Feo per diagonal; all 16 residue types at h = 281 look alike.

## Gaps

- The residual families are bounded only by computation or heuristics; none are proved small:
  - Rival pairs (even label + filler): the exact fraction of bad even rows is 30%, 20%, 22% and 17% at h = 281, 1001, 2001 and 4001, against a heuristic of 2 sqrt(J/h) with J ~ 24-40. So the relocated count is about h^{1.5}, small only asymptotically, and large at practical h.
  - M2c (So/FS): 0 to 3 bad odd rows per residue for h <= 4001 (onelabel.py), so O(h) labels if that persists. Not proved.
  - Two-label families (Fe/Fe, Feo/S3): at most 1 per diagonal in the census.
- V3 collisions among parked one-label triples (FFo of Lemma 2 with odd E, Pb/Pc with a label) are unbounded by proof; the census found 0 for h >= 161 after the near-band exclusion.
- The census covers one block with all residue slots occupied (plus sparse random subsets at h = 281), with fillers to h^2/4 columns. Cross-block families with fillers other than S5 were never tested, because that needs h > 320.
- Junction (4): SAW is global, so no zone/gap join exists. The SAW | Sea(1,g) region boundary was clean at h = 53, 57, 60, 85 and 88 (board.py). At h = 67 (row-1 type) and h = 85 (row-3 type) a junction rival pair appears (filler row h - 4k^2, j = 1); phase 0 removed it at h = 67 and the phase choice was not checked at h = 85. Junctions with the T25 star and the relocation regions were not checked.
- Theorem 1(6) assumes labels more than about 80 rows below the band. Those nearer, O(1) per diagonal, are relocated by the paper's Prop. partial without a construction. Small h (< 80) breaks Pb.
- Unaudited inputs: Lemma A2 and K-results of deep_layer_bh16.md (I re-derived A2's parametrization), Theorem A and Corollary B of sea_row3_split.md, and Theorem 5 of rigid_layout_cross_block.md with 2^nu >= K and 64 types. A prime p in (20h, 40h] with p = +-2 (mod 5) exists for large h by the prime number theorem in arithmetic progressions; I did not check an explicit h0.
- Everything here was checked once by me, with no independent audit. Thick vs thin for the residual families is classified only in part.
- B' bounded still needs chi(Gamma) < infinity, which is open.

## Missing estimate

With SAW and the three layout changes, the block-zone deep layer no longer has any family I could find with per-label load of order 1. What is missing is a proof that the residual label families hit only O(h^{2-delta}) labels:
(i) rival pairs (even label + filler), heuristic 2 sqrt(J/h) of even rows, so about h^{1.5};
(ii) M2c with one label and one filler, which needs a bound on #{i : e(e u2^2 - 4 n1^2 (u2 + e)) is a square for some n1 | e u2 with the v2 conditions};
(iii) the two-label families Fe/Fe and Feo (S3-type) inside a block;
(iv) cross-block families with fillers;
(v) V3 among parked one-label triples.
Each is a single explicit equation. If all are O(h^{2-delta}), Corollary 6 gives m_h = O(h^2) conditional on chi(Gamma) < infinity, and every step in it beyond the label scaffold is constant-cost.

## Next steps

- Audit Theorem 1(2b), Lemma 4(a) and Lemma 4(b), and Proposition 5. They are short 2-adic and quadratic-residue arguments, and they replace S2, S5 and T2 in the ledger.
- Prove the M2c bound: for fixed (e, n1, k) the curve k(u2(Q - u2) - k) = n1^2 (Q^2 - u2^2) has at most 2 points, so count the admissible (n1, k).
- Prove the two-label count: use the cubic in U of Section 9 and find all its rational linear branches. T2 was the only one found (U = -e1, e1 = -10k').
- Run a two-block census at h around 337 with p just above 20h, p = +-2 (mod 5), using lcd.py extended to two blocks.
- Shrink the rival-pair constant: choose T* = h or h - 1 by a per-type r1 shift, and test whether an even-row lattice choice (kappa) can exclude j in {1, 3} for the top two rows.
- Settle the junction phase rule for h = 1 or 3 (mod 4) (rival pair with filler row h - 4k^2), and test junctions with the T25 star region.

