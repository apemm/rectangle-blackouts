# A two-row deep layer for the block sea

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Not audited yet.

# Result

## Status

partial

## Summary

I give an explicit two-row deep layer, BH16. Its 2-adic row rule provably removes these families: shallow M2a (for labels and fillers, in every block), X1, X2 and M1C for fillers, rival pairs and every triple with two or more fillers, and the deep one-label family at every level. A new dichotomy lemma shows that every Pythagorean deep pair is an obstruction, either with row 1 or with any row that passes through two witness columns. As a result the main survivor, deep M2a, has load tau(e'^2)-1 per label, so this route does not reach O(1).

## Statements

NOTATION. A deep point is a black point (4n, y). For two deep points C and D, write D - C = (4delta, 2eps). Labels (i,j) sit in the rigid layout of rigid_layout_cross_block.md: column 4n with n = i + M_c, odd row 2i+1, even row 2(i+s_c)+2, M_c in pZ, and n(c) = s_c - M_c = kappa mod 2^nu with 2^nu >= 4. The shallow sea is Sh = {(x,1) : x != 0 mod 4}. Labels with i = 0 go to the T25 star region.

PART A. STRUCTURE LEMMAS (proved).
A1 (shallow M2a, simplified). Let C and D be deep points with y_C = y_D mod 2 and delta, eps != 0. Then C and D lie in a shallow M2a quadruple iff 4delta^2 + eps^2 = L'^2 and eps != 0 mod 4. In that case delta is even, delta = 0 mod 4 when eps = 2 mod 4, and the witnesses (2(n_C+n_D) -/+ L', 1) are always shallow.
A2 (dichotomy, new). Suppose 4delta^2 + eps^2 = L'^2 and eps = 0 mod 4. Put L = L'/2 and n_{A,B} = (n_C + n_D -/+ L)/2; both are integers. For every row r != (y_C+y_D)/2, the set {(4n_A, r), (4n_B, r), C, D} is a mixed quadruple with a horizontal side. A pair with eps = 2 mod 4 and delta odd is never Pythagorean. Consequence (W), a necessary condition on any deep layer: every black same-parity Pythagorean deep pair has eps = 0 mod 4, and its two witness columns 4n_A, 4n_B have no common black row other than (y_C+y_D)/2. Prop 5 of block_sea_classification.md is the eps != 0 mod 4 half of this lemma, and Prop 4 is the case where C lies in the witness row.
A3 (label lattice). Every even label point satisfies y = 2n + 2 + 2kappa mod 8. So no shallow M2a joins two even label points, in any blocks. If the classes are split by i mod 4, all odd label rows of a region are congruent mod 8, and no shallow M2a joins two odd label points of that region. This removes the cross-class M2a load on labels.
A4 (M1C refined). If the two even points A and B of an M1C configuration satisfy y = 2n + c mod 8 (true for even labels), then y_D = 5 mod 8. So an odd deep point in a row = 1 mod 8 lies in no X1 and no M1C configuration.
A5. No rival pair has a point in row h, and a tilted rectangle has at most one corner in row h. If a filler F lies in a row >= h - H0, then every rival pair {F, E} has j <= H0 and |x_F - x_E| <= 2 sqrt(H0(h+H0)).

PART B. RULE BH16. A region type is a pair (iota8, mu). It holds the labels with i = iota8 mod 8, i >= 1, in blocks with M_c = mu mod 2. Put nu = iota8 + mu mod 2 and r1 = 2iota8 + 1 mod 16, so every odd label row is = r1 mod 16. Put R = max{y <= h : y = r1 mod 16} and rho = R - 8. In every column 4n without a double, put a base filler (4n, R) if n != nu mod 2 and a hole filler (4n, rho) if n = nu mod 2. This rule covers the empty slots inside blocks, the long gaps and the gap-block transition, with no special case. Assume rho > (h+1)/2, which holds for h >= 48.
COST. There are 16 region types. Each is a copy of Theorem 5's layout for the split classes, with B positions per residue. The width is at most 16(20h^2 B + 2h) plus 15 buffers of 2W_h+1 columns, so 320 h^2 B + O(h^2).
KILLS (proved, for any number of blocks within reach):
K1. No shallow M2a.
K2. No X1, X2 or M1C contains a filler when iota8 is odd. When iota8 is in {0,4}, no X1 or M1C contains a filler, and an X2 needs G to be an even label in a row > rho, with |4gamma| <= 23h.
K3. If R = h, no rival pair contains a base filler. In every case a rival pair with a filler has j <= h - rho <= 23 and is local.
K4. No corner triple of type FFS, FFF or FFe (that is, (O;O,E) with two fillers) exists.
K5. The deep one-label family (three fillers in one row plus a deep D) is absent in row R and in row rho, at every 2-adic level.
SURVIVORS (exact):
S1 (proved fatal). Let a label have odd row in {R, R-16}. Then the tilted square {(4(n-2),rho), (4n, rho-8), (4(n+2),rho), (4n, rho+8)} has 3 black corners, and its white corner lies in the double column. That is O(h) labels per region type, which must be relocated.
S2 (proved). Deep M2a with C an odd label, D a hole and the witnesses on base fillers in row R. It needs e' = (rho - y_C)/8, which is always odd, and delta = 0 mod 4 with delta^2 + 4e'^2 a square. The witnesses lie at n_C + (delta -/+ L)/2 with L = 2 mod 4, always in base columns. Each label has exactly tau(e'^2) - 1 such configurations, minus those whose column 4(n_C+delta) is a label column. This load is unbounded: the mean of tau(m^2) grows like log^2. It is the main obstruction for BH16.
S3. (O;O,E) with V a base filler, P an odd label and Q an even label: 16(n_P - n_V)(n_Q - n_V) = -(y_P - R)(y_Q - R), with n_V != nu mod 2. This is always fatal when R is in the grid, it never occurs with a hole, and each (P,Q) pair has at most 2 positions.
S4. M2c with one filler and one label (the note's equation), V4 Fo/Fo, and V3 collisions of two parked triples with one filler each: census only.
S5. Cross-block label-label deep M2a (A2 with both C and D labels) can occur only when two blocks lie within h^2/4 columns.
PART C. Rule BH-alt (proved part). Put labels at n = nu mod 4, the class-0 row = r1+8 mod 16, and the class-1, class-2 and class-3 rows X, X-8, X-16 with X = r1+4 mod 8. Then (W) holds for every label-filler and filler-filler pair, so every M2a-type family with a filler is gone, S2 included. But the gap alone then carries filler-only V3 collisions and fully black rectangles (census), so it is not valid.
NOT PROVED: m_h = O(h^2); a deep layer with load O(1) per label; validity of any full board.

## Proofs

A1. By Theorem 2 of block_sea_classification.md, M2a holds iff L = |D-C| is an integer with L = 2 mod 4, or L = 4 mod 8 and delta is even. Write L = 2L' with L'^2 = 4delta^2 + eps^2.
- L = 2 mod 4 iff L' is odd iff eps is odd. Then 4delta^2 = L'^2 - eps^2 = 0 mod 8, so delta is even.
- L = 4 mod 8 iff L' = 2L'' with L'' odd. Then eps = 2eps' and L''^2 = delta^2 + eps'^2 with exactly one of delta, eps' odd. With delta even, eps' is odd, so eps = 2 mod 4.
- Conversely, if eps = 2 mod 4 and the pair is Pythagorean, then delta is even. Otherwise delta^2 + eps'^2 = 2 mod 4. So L'' is odd and both conditions hold.
- If eps = 0 mod 4, then either delta is odd, L'' is odd and delta is odd (excluded), or delta is even and L = 0 mod 8. Either way there is no M2a.
- The witness columns are 2(2n_C + delta) -/+ L'. For eps odd, L' is odd. For eps = 2 mod 4, 2(...) - 2L'' = 2delta - 2 = 2 mod 4. Both cases are shallow.

A2. Let eps = 0 mod 4. Then L'^2 = 0 mod 4, so L' is even. Put L = L'/2, so L^2 = delta^2 + (eps/2)^2. Since eps/2 is even, L = delta mod 2, and n_A = n_C + (delta - L)/2 is an integer. With A = (4n_A, r) and B = (4n_A + 4L, r):
- C + D - A - B = (0, y_C + y_D - 2r) = 2n with n = (0, (y_C+y_D)/2 - r). This is nonzero iff r != (y_C+y_D)/2.
- n is perpendicular to B - A = (4L, 0), and |D-C|^2 = 16delta^2 + 4eps^2 = 4L'^2 = |B-A|^2.
- D - C != +-(B-A) because eps != 0.
- p and q lie in row (y_C+y_D)/2, inside the grid.
By Lemma mixedeq this is a mixed quadruple. For eps = 2eps' with eps' and delta odd, 4(delta^2 + eps'^2) = 8 mod 16 is not a square. Computation (dichotomy.py): every Pythagorean pair with delta < 400, |eps| < 30 and h = 60 gave a valid shallow M2a (1522 cases) or valid deep witnesses (23364 cases), with 0 failures.

A3. An even label point has y - 2n = 2(s_c - M_c) + 2 = 2n(c) + 2. For two even labels, eps - delta = n(c') - n(c) = 0 mod 4, so eps = delta mod 4. A1 needs eps odd with delta even, or eps = 2 with delta = 0 mod 4, and both are impossible. Odd labels with i = iota mod 4 have rows = 2iota+1 mod 8, so eps = 0 mod 4.

A4. As in the note's M1C case, n1 is odd and y_B - y_A = 2 mod 4. The lattice gives y_B - y_A = 2(n_B - n_A) mod 8, so Delta = n_B - n_A is odd. Write D - C = (2z, y_D - 1) with z = 2(2n_D - n_A - n_B) - n1. Then z is odd, since n_A + n_B is odd. The length equation reads 4z^2 + (y_D - 1)^2 = 16Delta^2 + 4Y'^2, with Y' = (y_B - y_A)/2 odd. Modulo 32, 4 + (y_D-1)^2 = 16 + 4, so y_D - 1 = 4m with m odd, that is, y_D = 5 mod 8. Computation: m1c_check2.py (lattice-respecting random boards, h = 23) found 45 M1C supports, all with y_D = 5 mod 8. Without the lattice, m1c_check.py also finds y_D = 1 mod 8, so the hypothesis is needed.

A5. This follows from Lemma rival (c' + j <= h and c - j >= 1, so 4j(d+j) = t^2) and from (F1).

B, cost. Splitting a class by i mod 8 keeps it independent in G_T, and Theorem 5 applies to any classes. In region (iota8, mu), M_c = s_c - kappa mod 2^nu and M_c = mu mod 2 are compatible because s_c = kappa + mu mod 2. Each residue needs at most B positions spaced p2^nu, so each region has the length of the whole Theorem 5 layout.

K1. Every odd deep point of a region (labels, holes and bases) has a row = r1 mod 8. Holes and bases have rows rho, R = r1 mod 8 because rho = r1 + 8 mod 16. So eps = 0 mod 4 for every odd-odd pair, and A1 excludes M2a. Even deep points are even labels only, and A3 covers them.

K2. Corollary D of the note covers fillers in rows = 3 mod 4 (iota8 odd gives r1 = 3 mod 4). For iota8 in {0,4}, both rows are = 1 mod 8.
- X1 needs y_G = 5 mod 8, and fillers are never F, which is even.
- M1C needs y_D = 5 mod 8 by A4.
- X2 needs an even G with y_G > y_V >= rho. From a = (y_V - 1)g/(4gamma) != 0 we get |4gamma| <= (y_V - 1)(h - rho).

K3. If R = h, A5 applies. Otherwise min(c-1, h-c') <= h - rho.

K4. Theorem 1 of the note sorts the triples with a shallow corner.
- Pa needs F and G in even rows.
- Pb with two fillers has W in row y_F + y_G - 1 >= 2rho - 1 > h.
- X1 and X2 need an even deep point.
- Pc needs y_G > y_V with V and G odd. No odd point lies below R (no label row = r1 mod 16 exceeds R), so V is a hole and G a base. Then 4a gamma = (rho-1)·8, with gamma = n_G - n_V odd and a != 0 mod 4, so v2(a gamma) <= 1. But v2(2(rho-1)) >= 2: a contradiction.
FFF: all corners lie in rows {R, rho}. Two corners in one row y0 are opposite, the third is in the other row, and the fourth is in row 2y0 - y1. Put |w| = 2delta_s with w = (w_x, +-8), so (2delta_s - w_x)(2delta_s + w_x) = 64. Two co-row fillers of one type have delta_s even, so 4delta_s = 0 mod 8, which leaves only (8,8): delta_s = 4 and w_x = 0. Then the third corner lies in the column of slot n_A + 2, which has the same type as the two co-row corners, not the other type. So no FFF exists.
(O;O,E) with fillers V and P: the leg VP has Delta y in {0, +-8}. Delta y = 0 gives a horizontal leg, so the angle is axis-aligned. Delta y = +-8 gives Delta y2 = -/+2ac, which is even. But V is odd and Q even, so Delta y2 must be odd.

K5. The family is a deep mixed quadruple with A, B and C in one row r, so (u-v)^2 + 4k^2 = (u+v)^2 and uv = k^2. Its members sit in slots n_D - u', n_D + v' - u' and n_D + v', with u = 4u' and v = 4v'.
- Row R: all three members are = nu+1 mod 2. So u' and v' are even, and n_D = nu+1 mod 2. Then D is a base filler, which lies in row R, a contradiction.
- Row rho: u' and v' are even and n_D = nu mod 2, so D is a label. Also k^2 = 16u'v' with 4 | u'v', so 8 | k and y_D = rho mod 16. But label rows are = r1 = rho + 8 mod 16, a contradiction.

S1. Slots i +- 2 are empty in an i mod 8 class, and n +- 2 = nu mod 2, so both are hole columns in row rho. The diagonals (4(n-2),rho)-(4(n+2),rho) and (4n, rho-8)-(4n, rho+8) have the same midpoint and length 16. The point at rho+8 = R (or rho-8 = R-16) is the label's odd point. The other point lies in the label column, in an odd row, while the column also has an even black point. So it is not parked, and the axis-owner lemma makes the triple fatal. rho + 8 <= h always holds.

S2. A2 with C a label and D a hole requires eps = (rho - y_C)/2 = 4e' with e' odd, and delta even. Write delta = 2delta' and L = 2L'' with L''^2 = delta'^2 + e'^2. Since e' is odd, delta' is even and L'' is odd, so delta = 0 mod 4 and L = 2 mod 4. Then (delta -/+ L)/2 is odd, so the witnesses lie in base columns, never in label columns. The factor pairs f1 f2 = e'^2 with f1 < f2 give delta' = (f2 - f1)/2. Here f1 = f2 mod 4 always, so all (tau(e'^2) - 1)/2 positive solutions qualify. With signs, that is tau(e'^2) - 1 positions. Census check at h = 41: the formula predicts 3 V4 FF/Fo for iota8 = 1 (one blocked by a label slot) and 3 for iota8 = 3, and the brute force found 3 and 3.

S3. The dot-product equation of the legs gives the equation in S2's statement. The fourth corner has an even row in a column that has an odd black point, so it is fatal. A hole gives v2(y_P - rho) = 3 < 4, and v2(Delta y1) = 4 + v2(ac) is needed. Census example: V = (960,35), P = (932,19), Q = (964,28) gives 16(-7)(1) + (-16)(-7) = 0.

BH-alt (C). Pairs by class, with the label at class 0:
- D of class 0: e = 2 mod 4, so L = 2 mod 4. The witnesses then sit at odd offsets differing by 2 mod 4, in classes 1 and 3, which have different rows.
- D of class 2: e = (rho2 - y_C)/4 is odd while delta is even, so L is odd and != delta mod 2. No deep M2a, and A1 kills the shallow one.
- D of class 1 or 3: delta odd and e odd, so the pair is not Pythagorean.
- Filler-filler pairs: (0,2) and (0,odd) are non-Pythagorean by parity. (1,2) has witnesses of different parity class. (1,3) has L = 2 mod 4, so the witnesses lie in classes {1,3} or {0,2}, which have distinct rows.
Shallow M2a dies by A1 in every pair.

## External results used

- Paper sec2_prelim.tex: Lemma diff, Lemma mixedeq, facts (F1), (F3); sec5_threshold.tex: Lemma rival, Lemma sea (two sea rows 1 and g even, 2g-1>h), Lemma reduction.
- research_archive/2026-11-13/block_sea_classification.md: criterion V1-V5, Theorem 1 (X1, X2, Pa, Pb, Pc), Theorem 2 (M2a, M2c, M1C), Corollary D, Props 3 to 5 (not audited; the M2a and M1C parts I used were rederived).
- research_archive/2026-11-13/rigid_layout_cross_block.md Theorem 5 / Theorem C: rigid 2-adic layout and its width (not audited).
- research_archive/2026-11-13/lower_bound_windows.md: axis owner lemma (audited), used for fatality of S1 and S3.
- Ledger T25 (quadratic boundary star, audited) for the i = 0 labels.

## Checks

Scripts are in the script folders of this directory. Each run used py, took under 60 s and stayed far under 1 GB. The repository was not touched.
- board.py and driver.py: brute force from the definitions (numba). They find tilted rectangles with >= 3 black corners (V1, V2 by the parked rule, V3), all mixed quadruples with a non-vertical side (R2 axis-aligned or tilted) and rival pairs. Validated on the note's X2 example (E=(21,1), V=(16,9), G=(24,14), W=(29,6)), on an M2a pair (delta=2, eps=3) and on a rival pair (j=1).
- test_pure.py: Sea(1,r) has no obstruction (h=12, every r).
- test_rule.py, h=20: random rows = 3 mod 8 against random rows = 3 mod 4. The mod-8 rule gives 0 V4 SS/FF (M2a) and 0 V4 FS/FS. The mod-4 rule gives 19-21 and 17-21.
- test_bottom.py and test_hole.py (h = 17 to 25): a single bottom row leaves the Prop 4 family (V4 FF/Fo). Holes kill it. A hole row below (h+1)/2 makes V3 explode (thousands).
- t_final.py (BH16), h=41, 4 diagonals per type. Obstructions with a filler / labels:
  - iota8 = 1: 21 / 6 (FFo 4, Feo 2, FF/Fo 3, FS/So 4, Fo/Fo 1, Fe 6, FSo|FSo 1);
  - iota8 = 3: 18 / 6;
  - iota8 = 5: 20 / 6;
  - iota8 = 7: 16 / 6;
  - iota8 = 0: 18 / 4 (FSe 8);
  - iota8 = 2: 16 / 6;
  - iota8 = 4: 30 / 8;
  - iota8 = 6: 46 / 6.
  There were no FFS, FFF, FFe or SS/FF anywhere. FF/Fo counts match S2's formula exactly (3 and 3).
- t_alt.py (BH-alt), h=41: M2a-type survivors fall to FF/Fo 7 (tilted-side quadruples), but filler-only V3 explodes.
- dichotomy.py: A2 verified, 0 failures. m1c_check.py and m1c_check2.py: A4. m2c_search.py: M2c algebraic solutions with rows <= 40 total 40; with odd rows congruent mod 8, only (27,35, Delta=+-24).
- t_trans.py and t_trans2.py: sea junctions.

## Gaps

- No independent audit. A1 to A5, K1 to K5, S1 to S3 and the BH-alt kill were each checked once by me and by brute force at h <= 41 only.
- No O(h^2) deep layer. BH16 leaves S2 (deep M2a, tau(e'^2)-1 per label, unbounded on average). BH-alt removes S2 but creates filler-only V3 collisions and fully black filler rectangles: in 4 test windows at h = 41, FFF|FFF 444, FFS|FFS 820 and V1 FFFo 4.
- The census used one block per window (h <= 41, so the reach is smaller than the block spacing), and classes were plain i mod 8 slices of a diagonal, not G_T-colour classes. The multi-block regime (h > about 320·2^k), where S5 lives, was not tested.
- BH16 needs rho > (h+1)/2, which means h >= 48. The census at h = 39 and 41 satisfied it only for the region types tested. Smaller h needs another hole row.
- Other one-filler triples (V2 FFo besides S1, V2 Feo besides S3), V4 Fo/Fo, M2c with a filler (V4 FS/So) and V3 FSo|FSo collisions are counted only, not classified or bounded.
- For iota8 in {2,6} (rows = 5 mod 8), X1, M1C and X2 with fillers are not proved local. For {0,4}, only X2 survives, and it is local.
- Boundary labels go to T25. The junction from row 1 everywhere to Sea(1,g) with g even > (h+1)/2 is clean by the paper's Lemma sea (seas only, without T25's doubles at the junction). Sea(1,g) next to Sea(1,R) was clean for R in {h, h-2} and every tested g (h = 17 to 29, computation only). The BH16 two-row gap next to a one-row buffer was not tested.
- The S1 labels (odd row R or R-16, O(h) per region) need relocation, and none is constructed. Labels with odd row R recur in every region type with the same iota8.
- The cost constant 320 h^2 B assumes that Theorem 5 of rigid_layout_cross_block.md (not audited) holds with classes split by i mod 8. B itself is bounded only if chi(Gamma) is finite, which is open.

## Missing estimate

Lemma A2 turns the deep layer into a witness-colouring problem. Let y(n) be the row of the filler in deep column 4n. Two conditions are needed:
(i) For every black same-parity deep pair (C,D) with 4delta^2 + eps^2 a square: eps = 0 mod 4, and y differs at the two witness columns n_C + (delta -/+ L)/2.
(ii) The filler-only parked triples (Pc, Pb and FFF) have pairwise distinct white corners.
BH16 satisfies (ii) and every part of (i) except S2: label-hole pairs with base witnesses, tau(e'^2)-1 per label. BH-alt satisfies (i) for every pair containing a filler, but fails (ii).

The estimate needed is a filler pattern on n mod 2^t whose rows meet the congruences of K1 and K2 (class 0 = r1+8 mod 16, class 2 and the odd classes = r1+4 mod 8, all rows > (h+1)/2) and that has no collision among the parked triples Pc(V,G), Pb(F,G) and FFF. Equivalently, the sets {a + 4gamma : a gamma = (y_V-1)(y_G-y_V)/4, the residue conditions hold} must have no coincidences modulo the pattern period.

Label-label pairs across blocks (S5) need the same witness condition with C and D both labels. Its first-moment load is about log^2 h / (80B) per label (heuristic). It would vanish if the witness rows were injective on n mod 2^t with 2^t of order h/32. That costs about h/16 distinct filler rows, which reopens (ii).

## Next steps

- Audit A1, A2 and A4 (short, elementary) and add A2 to the ledger as a necessary condition on every deep layer. It also explains Props 4 and 5 of block_sea_classification.md.
- Search periodic patterns y(n mod 8) or y(n mod 16) that satisfy (W) for label-filler and filler-filler pairs (as BH-alt does) and have zero filler-only V3. Score each pattern with board.py on a pure gap window (h about 49), then on the census.
- Classify the remaining one-filler families (V2 FFo besides S1, V2 Feo = S3, V4 Fo/Fo, V4 FS/So, V3 FSo|FSo) with exact equations, as was done for S2 and S3.
- Design the relocation region for the S1 labels (odd rows R and R-16) and the X2-exposed bottom labels for iota8 in {0,4}. A T25-like star with O(h^2) width should suffice, since there are O(h) such labels.
- Test the BH16 gap next to the Sea(1,g) buffer junction, and T25 doubles next to the Sea(1,g) buffer, by brute force.
- Run the census in the multi-block regime (two blocks at distance < h^2/4, with a reduced p) to measure S5.

