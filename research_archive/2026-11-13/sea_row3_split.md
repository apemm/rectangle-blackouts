# Removing X1, X2 and M1C by a row-3 sea on half the classes

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: splitting classes by i mod 8 and moving the shallow sea to row 3 for even i removes X1, X2, M1C and label-label shallow M2a. The deep layer in the block zones is what remains. Not audited yet.

# Result

## Status

partial

## Summary

X1 and X2, the named bottleneck, are removed outright, cross-class and intra-class, with no congruence condition on blocks. Split every class by i mod 8, as BH16 already does. The odd-i types keep the row-1 sea. The even-i types get their shallow sea moved to row 3. Then no deep point is an X1 or X2 vertex, so the load log(h/160)/(20 chi) becomes 0, at a constant factor in width. M1C and label-label shallow M2a also vanish, without needing p = ±2 mod 5. What remains is the deep layer: BH16's S2 (tau(e'^2)-1 per label, now the main survivor) and S5, plus V3 collisions and M2c. Two natural deep-layer fixes I tested both fail.

## Statements

SETTING. Stride 4 and the rigid layout of item (2). Shallow points: one black point in every column x != 0 mod 4 of a window, all in one sea row r0. Deep points: black points in columns = 0 mod 4 (labels and fillers). Families and criterion (V1)-(V5) are those of block_sea_classification.md (audited).

THEOREM A (vertex sources; proved). Let r0 be the sea row of a window. Inside that window, every tilted rectangle with at least 3 black corners and at least one shallow corner is either fatal of type X1 or X2, or parked (Pa, Pb, Pc). Moreover:
(a) X2 needs a deep vertex V of the same parity as r0 with y_V = r0 (mod 4).
(b) X1 needs a deep end G of the same parity as r0 with y_G = r0 + 4 (mod 8).
(c) M1C needs a deep point D with y_D = r0 (mod 4) (D odd when r0 is odd).
This holds for r0 = 1 with no further hypothesis. It holds for r0 = 3 under these hypotheses:
(H1) every black point of the window lies in a row >= 3;
(H2) no deep point lies in row 4 or row 5;
(H3) every odd deep row is = 1 (mod 4);
(H4) no two even deep points with row difference 2 lie within 2h columns of each other.
For r0 = 3 under (H1)-(H4), no corner triple whose white corner lies in row 1 or 2 has a shallow corner.

COROLLARY B (source-free layout; proved, given the cited results). Split each class by i mod 8, as in the 16 BH16 region types (iota8, mu).
- Types with iota8 odd: row-1 sea. Every odd deep row is = 3 (mod 4).
- Types with iota8 even: row-3 sea. The BH16 rule is shifted up by 2 rows, so R = max{y <= h : y = 2iota8+1 (mod 16)} and rho = R - 8.
Take out these O(h) exceptional labels: i = 0 (T25 star), i = 2, j in {0, 1} in the row-3 types, and the BH16 S1 labels. Place the exceptional labels by the paper's Prop. partial (width c0 n tau_max(h)^2 = O(h^{1+o(1)})), behind buffers of 2W_h+1 columns.
Then in every region:
- no X1, no X2 and no M1C exists among labels, fillers and the sea, cross-class or intra-class, at any block distance;
- no shallow M2a joins two label points (only the rigid rule with nu >= 2 is used, not p = ±2 mod 5);
- in the row-3 types, no mixed quadruple or corner triple made of label points and shallow points has a corner in row 1 or 2.
The width is the BH16 width 320 h^2 B + O(h^2), plus O(h^2) for junction buffers. B is unchanged, because i and i-2 never share a class after the i mod 8 split.

PROPOSITION C (extreme-row obstruction; proved, and it explains why row 3 is used). Suppose every region's shallow sea lies in row 1 or in row h. Then every label of
 Q = {i even, j = K+1 (mod 2)} (h even), Q = {i even} (h = 1 mod 4), Q = empty (h = 3 mod 4)
satisfies the X2 vertex congruence of Theorem A in both orientations, row 1 and row h (reflected). So for h != 3 (mod 4), using only the extreme rows leaves a quarter (h even) or a half (h = 1 mod 4) of the labels as X2 vertices. For h = 3 (mod 4), two regions suffice: row 1 for i odd, and its mirror image (row h) for i even. That variant needs no boundary analysis.

NOT PROVED: m_h = O(h^2); a deep layer that removes BH16's S2 and S5; any bound for V3 collisions or M2c.

## Proofs

1. THEOREM A FOR r0 = 1. This is a direct reading of block_sea Theorem 1 (audited).
- X1: the vertex E is in row 1 with x_E = 2 mod 4, F is in an even row, and y_G = 5 (mod 8).
- X2: E is an end, and the vertex V has y_V = 1 (mod 4) and y_V >= 5.
- Every other triple with a shallow corner is Pa, Pb or Pc (parked).
- M1C forces y_D = 1 (mod 4) (Theorem 2, audited).
These are conditions on deep points only. In particular they hold for fillers, for labels of any class, and at any distance between blocks.

2. THEOREM A FOR r0 = 3.

(i) Shift invariance. The proofs of Theorems 1 and 2 use only three things:
- row differences relative to the sea row;
- columns mod 4 and lengths mod 16;
- (F1)/(F3) for the sea row.
They use the strip boundary in exactly two places:
(alpha) in the end case, "W is not in row 1, so g >= 1";
(beta) in Theorem 2(i), "if pq is not horizontal, one of p and q is below the sea row".
Lemma rival also uses the boundary. Everything else carries over with y replaced by y - 2. So under (H1), any obstruction whose non-black corners (W, or p and q) all lie in rows >= 3 obeys the shifted Theorems 1 and 2: X2 needs y_V = 3 (mod 4), X1 needs y_G = 7 (mod 8), and M1C needs y_D = 3 (mod 4). It remains to treat the configurations that use rows 1 and 2.

(ii) Corner triples with the white corner W in row 1 or 2. All black corners lie in rows >= 3, so W is the unique lowest corner. Let P1 = W + v and P3 = W + w be its neighbours (v.w = 0, v_y, w_y > 0) and P2 = W + v + w the top corner. P1 and P3 are opposite.
- P1 and P3 both shallow (row 3), with e = 3 - y_W.
  - e = 1: v_x w_x = -1, so P2 = (x_W, 4) is directly above W.
  - e = 2: v_x w_x = -4. The splits (1,-4) and (4,-1) put P1 or P3 in a column = 0 mod 4, which contradicts shallowness. So only (2,-2) remains, and P2 = (x_W, 5).
  - Both cases need a deep point in row 4 or 5, which (H2) excludes. These squares are fatal: W lies in the double column of a label with j = 1 or i = 2. That is why those labels are excluded.
- Exactly one of P1, P3 shallow, say P1, with v_y = e. P2 is the top corner, so it is not in row 3 and is deep. P3 and P2 are deep, so v_x = 0 (mod 4) and w_x != 0 (mod 4). Also e w_y = -v_x w_x.
  - e = 1: w_y = 0 (mod 4). Then y_P3 = 2 (mod 4) and y_P2 = y_P3 + 1 = 3 (mod 4) is odd, which (H3) excludes.
  - e = 2: P2 - P3 = (v_x, 2). The two points have the same parity and |v_x| = 2w_y/|w_x| <= 2h. Odd-odd pairs have Delta y = 0 (mod 4) by (H3), and even-even pairs are excluded by (H4).
- P1 and P3 both deep. Then P2 is deep, so x_W = 0 (mod 4) and all three black corners are deep. Such triples are covered by the label-only results (Theorem C of the rigid note: no tilted right angle among label points, whatever the fourth corner) or by the deep-layer analysis.

(iii) Mixed quadruples with p or q in row 1 or 2. Use Lemma mixedeq: C + D = A + B + 2n, p = A + n, q = B + n. Sort by the shallow set (the mod-4 and mod-16 eliminations of Theorem 2(ii),(iii) and M1C are shift invariant).
- {A, B} shallow: n is vertical and y_C + y_D = 6 + 2n2. A low p needs n2 <= -1, so y_C + y_D <= 4, which (H1)/(H2) exclude.
- {C, D} shallow: CD is horizontal in row 3, pq has the same midpoint and the same length L, and p is in row 3 - e.
  - L^2 - 4e^2 must be a square, so e = 1 gives L = 2, and e = 2 gives L = 4 or L = 5.
  - L = 2 or L = 4 makes pq vertical, so AB is vertical, which is excluded.
  - L = 5 gives B - A = q - p = (±3, 4), but A and B are deep, so their column difference is = 0 mod 4, a contradiction.
- One of A, B and one of C, D shallow. Only the shallow one's partner can be low: if q = B + n is low with B deep, then p is below row 1. Name the points so that A is shallow, p = A + n with n = (n1, -e) and e in {1, 2}, and the deep pair is B, D with B - D = (beta, 2e). Put z = x_B - x_A (z != 0 mod 4) and u2 = y_B - 3. Perpendicularity and equal lengths give
  n1 z = e u2 and (beta + n1)(beta + n1 - z) = e(u2 - e), equivalently (w - z)^2 = z^2 - beta z - e^2 with w = beta + n1.
  - Locality: |n1|, |z| <= 2h. If w(w - z) != 0 then |w| <= |z| + 2h. So |beta| <= 6h < 76h, and the deep pair lies in one block zone.
  - Same class: B - D = (4t, 2t) with t = e. Under (H3), or the i mod 8 split, t = 2 is the only option for odd-odd pairs. With beta = 8 and e = 2, (z - 4)^2 - 20 must be a square, so z is in {10, -2}. Then 2(y_B - 3) = n1 z is in {60, 12, 28}, which gives y_B in {33, 9, 17}, an odd point at slot i in {16, 4, 8} paired with slot i - 2. The even-even case would need y_B odd, so it is impossible.
  - After the i mod 8 split, i and i - 2 are never in one class. So no label-label instance exists.
  - Check: the random census at h = 24 found exactly this shape (B = (8,17), D = (16,13), A = (6,3), p = (20,1)).
- Exactly one shallow point, or three: impossible by Theorem 2(ii),(iii). M1C needs y_D = 3 (mod 4), which (H3) excludes.

(iv) Rival pairs with a row-3 shallow point C. Here j <= 2, because c - j >= 1. Let D be deep and t = x_C - x_D, which is != 0 (mod 4).
- j = 1 gives 4(c' - 2) = t^2, so t = 2 (mod 4), so c' - 2 is odd and c' is odd. But c' - 3 must be odd, a contradiction.
- j = 2 gives t^2 = 8(c' - 1), which forces 4 | t, a contradiction.
- A row-3 partner has the same parity, and row h is excluded by Lemma rival.

3. COROLLARY B.
- Types with iota8 odd: every odd label row is 2i+1 = 3 (mod 4), and BH16 fillers lie in rows = r1 = 3 (mod 4). So nothing satisfies (a), (b) or (c) of Theorem A for r0 = 1.
- Types with iota8 even and r0 = 3: odd label rows and the shifted BH16 rows R, rho are all = 2iota8 + 1 = 1 (mod 4). So nothing satisfies (a) (needs 3 mod 4), (b) (needs 7 mod 8) or (c).
  - (H1): rows 1 and 2 hold no black point, since i = 0 and j = 0 are excluded.
  - (H2): j = 1 and i = 2 are excluded, and the fillers are high.
  - (H3): holds by the residues above.
  - (H4): within one class, even points with Delta y = 2 would need consecutive slots, which the i mod 8 split excludes. Two even points in different blocks have |Delta x| > 76h > 2h. Fillers are odd.
- The X1/X2 relations hold at any block distance, so the cross-class loads (B2, B3, B5 of cross_class_sea.md) vanish. So does the intra-class X2 relation (block_sea D2), so the v2(i) mod 3 split is no longer needed. Intra-class X1 needs y_G = 5 (mod 8), so it vanishes too, and the X1 factor in A3 (2tau*(h^2)) disappears.
- Shallow M2a among labels.
  - Even-even: by deep_layer A3, the rigid rule with nu >= 2 gives eps = delta (mod 4), and A1 then excludes M2a.
  - Odd-odd: a type has i fixed mod 8, so its odd rows are congruent mod 16, eps = 0 (mod 4), and A1 excludes M2a.
- BH16's K2 was proved only for iota8 odd. In shifted coordinates every type is now the iota8-odd case, so K2 holds for all 16 types.
- Width:
  - the label split is BH16's own, so B is unchanged;
  - the 16 types cost 320 h^2 B + O(h^2);
  - each change of sea row (1 to 3) uses the chain Sea(1,g) | all-row-g | Sea(3,g), each piece 2W_h+1 columns wide, with g even and 2g - 3 > h;
  - Sea(3,g) is valid: two corners in row 3 put the fourth corner in row 6 - g < 1, and two corners in row g put it in row 2g - 3 > h; the parity argument of Lemma sea needs 3 + g odd; and the rival-pair and boundary cases are as in (ii) and (iv);
  - the exceptional labels: n = O(h) parity edges in width c0 n tau_max^2 (paper Prop. partial, every edge good for g = h when h is even, case (c) when h is odd).

4. PROPOSITION C. Reflection y -> h+1-y maps a row-1 sea onto a row-h sea, and maps label (i,j) to (K-1-j, K-1-i) for h even and to (A-1-i, K-1-j) for h odd. X2 at row 1 needs i even. X2 at row h therefore needs the reflected i to be even: j = K+1 (mod 2) for h even, and i = A-1 (mod 2) for h odd. Intersecting the two conditions gives Q. Q is invariant under the reflection, so no pair of extreme-row regions covers it. For h = 3 (mod 4), A is even, Q is empty, and two regions suffice: i odd with the row-1 sea, and i even with the row-h sea.

5. OPTIONS (i)-(iii) OF THE ROUTE, evaluated. These are heuristic and are now moot for X1/X2.
(i) Slot or order choice among O(1) options per class. A neighbouring pair of blocks carries about 2 log h/chi^2 X2 offsets in expectation, and a block has about h/80 neighbours. So O(1) options cannot avoid them once log h >> chi^2. This is the same first-moment obstruction as the rigid note's "Repairs".
(iii) Spreading blocks. The load scales like 1/lambda, which needs lambda of order log h, that is width about h^2 log h.
(ii)/(iv) The source-free sea-row choice above has zero X1/X2 load. That is the route taken.

## External results used

- research_archive/2026-11-13/block_sea_classification.md: Theorem 1 (X1, X2, Pa-Pc), Theorem 2 (M2a, M2c, M1C), Proposition 3, criterion (V1)-(V5). Audited in audits_rigid_mixed_sea.md.
- research_archive/2026-11-13/rigid_layout_cross_block.md: Theorem C/5, no tilted right angle and no rival pair among label points in the rigid layout. Audited.
- research_archive/2026-11-13/deep_layer_bh16.md: A1, A3 (lattice of even labels), BH16 rule, K1-K5, S1-S5. Not audited.
- Paper sec5_threshold.tex: Lemma sea, Lemma rival, Lemma reduction, Lemma block, Prop. partial (placement of n edges in width c0 n tau_max^2).
- Ledger T25 (quadratic boundary star, audited) for the i = 0 labels.

## Checks

Scripts are in the script folders of this directory. All were run with py, one at a time, each under 45 s.
- obs.py: my own obstruction finder from the definitions. It finds every tilted rectangle with at least 3 black corners and classifies it as V1, fatal or parked by the (V2) parity rule. It also lists V3 collisions, mixed quadruples via Lemma mixedeq (p and q in the strip, AB not vertical, D - C != ±u) and rival pairs via Lemma rival.
- t1_regionA.py (row-1 sea, i odd labels, fillers = 3 mod 4): 0 fatal triples with a shallow corner at (h, width) = (24,160), (40,400) and (31,600). The controls that allow even i give 91, 363 and 452 fatal X1/X2.
- t2_regionC.py: random census comparing region A and region C (row-3 sea). Region C has no fatal triple with a shallow corner. Its extra boundary families are filler-involved, or the predicted M2c-low shape with deep rows (17, 13) and p in row 1.
- t4_blocks.py, t5_pqlow.py, t6_v3.py: structured blocks (G_T-independent constant-offset classes, one i parity) at h = 24, with T computed from 20d^2 + 4Td + T^2 = L^2. Both regions: 0 fatal triples with a shallow corner. Every region-C boundary quadruple involves a filler. Every V3 collision involves a filler. Region A shows 3 label-label M2c (LSSL).
- t7_gap.py: the pure BH16 gap and the pure BH16m4 gap are obstruction-free at h = 57 and h = 60.
- t8_block.py, t9_detail.py: one BH16 block (iota8 = 1) at h = 57. BH16 gives 3 S2 quadruples. BH16m4 gives 4 new tilted-side quadruples and 1 rival pair.
- t10_lattice.py, t11_latblock.py: the even-lattice deep layer at h = 40, as reported under Gaps.
These are sanity checks at small h. Cross-class configurations need h >= about 150 with p > 20h, so they are covered only by the proofs, which hold at every distance.

## Gaps

- Nothing here is independently audited. Theorem A for r0 = 1 is only a reading of the audited Theorem 1. The r0 = 3 boundary analysis (proof items 2(ii)-(iv)) and the shift-invariance claim (item 2(i)) are new and were checked once by me. The brute-force censuses at h <= 40 agree with them.
- Corollary B inherits BH16's survivors unchanged, and they are now the main sea obstruction. S2 (deep M2a: label C, hole D, base witnesses in row R) has tau(e'^2)-1 instances per label. The mean of tau(e'^2) over odd e' <= h/8 grows like log^2 h, so most labels are hit, and BH16 is not a usable deep layer. S5 (cross-block label-label deep M2a) remains, with heuristic load about log^2 h/(c chi). I proved that its witness columns lie within (L - |delta|)/2 < h/1200 slot positions of C and D, so S5 is zone-local; it lives in the block zones, not in the gaps. S3 and S1 also remain, and S1 needs O(h) relocated labels.
- Two deep-layer fixes I tested fail. (1) BH16m4, with base rows R or R-16 by n mod 4: the horizontal S2 quadruples disappear, but tilted-side quadruples with witnesses in rows R-16 and R appear in equal number (h = 57: 4 against BH16's 3), plus a local rival pair. The pure gap stays clean. (2) Even-lattice fillers, every non-label deep column in an even row y = 2(n+kappa+1) mod 2^(nu+1) with 2^nu >= K/2. They provably have no right angle and no deep or shallow M2a among even points, and no three-filler one-label family. But the gap then carries filler-filler M2c (40) and V3 (20) at h = 40. Using the lattice only inside blocks creates shallow M2a at the gap transition (43 and 55).
- V3 collisions among parked triples (Pa, Pb, Pc, and the X1/X2 shapes that are now absent) are not bounded. A heuristic count of cross-block collisions is O(h log^2 h) in total, which relocation would absorb in O(h^{1+o(1)}) width, but nothing is proved. Intra-block collisions are not estimated. In the structured censuses, every V3 collision involved a filler.
- M2c is not bounded. Intra-class degeneracy is at most 2 numerically, and family (IV) survives every i mod 2^k split. The cross-class count is heuristic.
- The junction of a BH16 gap with a Sea(1,g) or Sea(3,g) buffer is untested. This gap is inherited from deep_layer_bh16.md. The chain Sea(1,g) | all-g | Sea(3,g) is proved clean only for pure seas.
- The exceptional labels (i = 0, i = 2, j in {0,1} in row-3 types, S1 labels) go to T25 and to a paper-style region. The combination with buffers is argued from Lemma block of the paper and not checked by computation.
- The payoff computation for the orbit bound on chi(G_T) belongs to the chi route and was not checked here.

## Missing estimate

With X1, X2 and M1C gone, the sea next to the blocks reduces to a deep-layer problem inside the block zones, and only there. S5's witnesses lie within h/1200 slot positions of their labels, and S2 is local by construction. In each block zone, a filler row function y(n) is needed with four properties:
(1) Odd deep rows are congruent mod 8 within a region. This keeps K1, Theorem A's congruences and (H3) when r0 = 3.
(2) Lemma A2's witness condition holds for label-filler, filler-filler and cross-block label-label pairs: the two witness columns n_C + (delta ∓ L)/2 share no black row other than the midpoint row.
(3) Parked filler triples have distinct white corners.
(4) The zone joins a constant-row gap with no new family.
BH16 meets everything except (2) for label-hole pairs (S2) and cross-block pairs (S5). The natural repairs, mod-4 base rows and even-lattice fillers, break (2) with tilted sides, or break (3) and (4). Any layer meeting (1)-(4) with O(1) distinct rows per zone would give the full sea at width 320 h^2 B + O(h^2), conditional on M2c and V3 adding at most O(h^2/tau_max^2) relocations, and on chi(Gamma) < infinity for B.

## Next steps

- Audit Theorem A for r0 = 3: the shift-invariance claim (item 2(i)) and the boundary items 2(ii)-(iv). They are short and elementary. Then add a ledger row: 'i mod 8 split with sea row 1 for odd iota8 and row 3 for even iota8: no X1, X2 or M1C, and no label-label shallow M2a, in any rigid layout'.
- Correct cross_class_sea.md B2, B3 and B5 ('no rule removes X2'). The removal comes from the sea row, not from congruences on blocks. Also drop the v2(i) mod 3 split and the X1 factor from A3.
- Attack the zone deep layer as a finite design problem on n mod 2^t inside block zones, using a pattern search scored by obs.py. Require (1)-(4) of the missing estimate, and include tilted-side M2a (the BH16m4 failure) in the score.
- Bound V3 among parked label triples. Count the Pc-Pc and Pa-Pb coincidences at one W exactly, by the method of Theorem 1, then decide whether O(h^{1+o(1)}) relocations suffice.
- Test the BH16 gap next to the Sea(1,g) and Sea(3,g) buffers at h of about 57 (inherited gap).

