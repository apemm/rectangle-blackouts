# Counts for the families that the sawtooth layer leaves

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: rival pairs with a filler hit O(h^1.5) labels (proved). Label-filler M2c reduces to one cubic surface, with no count yet. Feo is thick in SAW and empty in the variant SAW*. The two-label quadruples Fo/Fo and Fe/Fe are thick, through a rational nodal cubic, so (S) needs a further colour split. Not audited yet.

# Result

## Status

partial

## Summary

Rival pairs (i) are proved harmless at O(h^{3/2}) labels. Label-filler M2c (ii) is reduced to holes only and to one explicit surface equation, but no count is proved. Feo is thick in SAW and empty in a constant-cost variant SAW* (proved). The two-label quadruples Fo/Fo and Fe/Fe (iii) are thick in SAW and SAW*: they come from a rational nodal cubic, and T2 is one point of it. So Corollary 6's residual list is not thin, and hypothesis (S) fails for SAW unless the classes are split further by colouring.

## Statements

Setting: the layout of deep_layer_sawtooth.md, Corollary 6 (SAW rows T*-24, T*-16, T*-8, T* by slot offset 0..3 mod 4; label columns at offset 0; classes split by i mod 16; rigid lattice n(c) = kappa mod 2^nu). Coordinates: deep point (4n, y). "All slots occupied" means a class that holds every slot of its residue (the census convention).

DEFINITION (SAW*): SAW with two changes, each costing a constant factor. Classes are split by i mod 32, so y_P = 2i+1 is fixed mod 64 per region type. T* is the largest y <= h with y = y_P + 32 (mod 64) when T = 3 (mod 4), or y = y_P + 48 (mod 64) when T = 1 (mod 4). T mod 4 is already fixed per region type, because M_c mod 4 is set by s_c mod 4. T* = r1 (mod 16) still holds, so every proof in deep_layer_sawtooth.md carries over, with T* >= h - 63 and H0 <= 87.

LIST OF RESULTS (proved unless marked otherwise):

(i) RIVAL PAIRS (even label point and filler). PROVED: harmless. Suppose every filler lies in a row >= h - H0. Then the even label rows that occur in some rival pair with a filler number at most H0/2 + (1/6)(H0+2)(H0+1)^{3/2} sqrt(h+H0). At most ceil(h/2) labels have a given even row. So the labels hit number O(H0^{5/2} h^{3/2}): at most about 865 h^{3/2} for SAW (H0 = 39) and about 6100 h^{3/2} for SAW* (H0 = 87). The relocation rule moves them in width O(h^{3/2} tau*(h)^2).

(ii) M2c WITH ONE LABEL AND ONE FILLER (B odd label, D filler, A and C shallow).
 (ii-a) PROVED (2-adic lemma), in SAW and SAW*, for row-1 and row-3 types. D is never a base filler. D is a hole, with e = (y_D - y_B)/2 = 4 (mod 8), in exactly one of two patterns:
  (alpha) D at slot offset 2 (delta = 2 mod 4), with k := e u2/n1 = 2 (mod 4) and v2(Delta - 2n1) = 4;
  (beta) delta = 0 (mod 8), with k odd.
 (ii-b) PROVED (exact reduction). Put Q = y_D - 1. A label with odd row y_B is hit iff, for some filler row, e = (Q - u2)/2 lies in E(Q). Here E(Q) is the set of e for which there are integers n1, X, Y >= 1 with
   XY = e^2 + n1^2 and n1 (X + Y + 2 n1) = e (Q - 2e),
 together with the congruences of (ii-a) and the slot condition delta = +-(X + 2n1)/4 or +-(Y + 2n1)/4. Equivalently, with t = X + n1, E(Q) is the projection to e of the integer points of the affine cubic surface S_Q : (t+X) e^2 - XQ e + t^2 (t - X) = 0. The labels hit number at most (h/2) * sum over the filler rows of |E(Q)|.
 (ii-c) PROVED (partial counts), for every eps > 0:
  - the e in E(Q) that have a solution with min(X, Y) <= Z number at most C_eps Z Q^eps (sum-of-two-squares fibration);
  - those with a solution with n1 <= N0 number at most C_eps N0 Q^{1/3+eps} (Bombieri-Pila on an absolutely irreducible cubic curve);
  - S_Q contains no rational line other than the degenerate e = 0 lines, so no thick (linear) subfamily exists.
 NOT PROVED: |E(Q)| = O(Q^{1-delta}). The missing range has e, n1, X, Y and u2 all of order Q. Census: at most 3 bad odd rows per residue for h <= 4001.

(iii) TWO-LABEL FAMILIES INSIDE A CLASS.
 (iii-a) Feo = corner triple {filler V, odd label point P, even label point Q}; its fourth corner is always fatal when it lies in the grid. PROVED:
  - Q-vertex: impossible, by parity.
  - P-vertex: requires V to be a base filler with v2(y_V - y_P) >= 6 (cross-block) or >= 8 (same class).
  - V-vertex: requires V to be a base filler with y_V - y_P = 16 f', f' odd. Then g = D - 2f' and t = D + N/D - 4f' for a signed divisor D of N = f'(4f' + kappa'), with kappa' = y_V - y_e(n_P). Inside a class, N = f'(20 f' - T).
  - In SAW, CE (Lemma 2) together with the S2 kill (Theorem 1(2b)) forces the two base rows to differ by 16 (mod 32). So for every label one base row has v2 = 4, and V-vertex Feo cannot be removed 2-adically in SAW.
  - In SAW, Feo is THICK. With all slots occupied, there are at least c h^2 fatal Feo triples: the linear branch D = f' gives g = -f' and t = 17 f' - T whenever f' = T (mod 16) and f' = -a (mod 4). Numerically the rate is about 0.127 V-vertex triples per label at h = 20481 and still growing, mostly from divisor branches of unbounded degree.
  - THEOREM: in SAW*, there is no Feo at all: no vertex type, no hole or base, in any pair of blocks of a region.
 (iii-b) Two-label mixed quadruples with two fillers. PROVED:
  - Only {o, o, F, F} and {e, e, F, F} occur; {o, e, F, F} is impossible by parity.
  - Side = two labels with diagonal = two fillers, and the reverse, is impossible under the i mod 16 split.
  - The remaining shape (side {L1, F1}, diagonal {L2, F2}) is equivalent to the cubic P^3 - 8t P^2 + ((Y1 - Y2)^2 - 8t Y1) P - 8t (Y2^2 - Y1^2) = 0 in P = X1 - X2, in original units.
  - When both fillers lie in one row, the solutions form the cone over the plane cubic F(p,u,v) = p^3 - 4dp^2 + (d^2 - 4du)p + 4d^2(u+v) = 0, with d = u - v, (u, v) the label depths below the filler row in units of 4 rows, and p in slot units. This cubic has a node at (0:1:1), so it is rational:
   (x1, u, x2, v, d) = kappa (b(a^2+b^2), (a-4b)(a^2+b^2), b(-3a^2+8ab+b^2), a^3-4a^2b-3ab^2+4b^3, 4b^2(a-2b)), with m = a/b = p/d. T2 is m = 3.
  - The vertical component of the vector N is N_y = 2d rows. If d > 0 (the diagonal label is shallower), each class has only finitely many shapes, so O(1) quadruples per class and O(#classes) labels in total: harmless.
  - If d < 0, each admissible shape scales by lambda = 1 (mod 2^K), with about h/(2^K D_shape) instances per class. That is THICK: Theta(h^2) with all slots occupied.
  - Admissible d < 0 shapes exist and were verified (lists in Checks): Fo/Fo with i mod 16 (for example depth ratio 53:101 at depths 318, 742, 1166, ...), with i mod 32 and 64, and in SAW*. Fe/Fe also occurs in SAW and SAW*.
  - Odd-odd families do not depend on T: they are edges of a ratio graph on depths below each filler row, of the same nature as R_IV.
(iv) CROSS-BLOCK. Rival pairs and M2c involve only one label, so (i) and (ii) cover every block. Feo across blocks is empty in SAW* (proved in (iii-a)). Two-label cross-block quadruples obey the same cubic with (4t, 2t) replaced by the inter-block vector (Dx, Dy): P^3 - 2Dx P^2 + ((Y1-Y2)^2 - 4Dy Y1) P - 2Dx (Y2^2 - Y1^2) = 0. They are not homogeneous, and NOT COUNTED.
(v) V3 among parked one-label triples: NOT PROVED, no progress.
CONSEQUENCE: hypothesis (S) of heavy_light_split.md fails for SAW, and also for SAW* through (iii-b), unless every class is additionally independent in the graphs above. These graphs are the Feo graph F_T (not needed in SAW*) and the d < 0 nodal-cubic ratio graphs for oo and ee. Whether they have bounded chromatic number is OPEN. Numerically F_T has degeneracy 2 at h <= 2561.

## Proofs

Notation: deep point (4n, y). An odd label point P has y_P = 2i+1, which is r1 mod 16 (mod 32 in SAW, mod 64 in SAW*). Its even point is y_eP = y_P + T, with T = 2s+1. Every even label point of a region satisfies y = 2n + 2 + 2n(c) with n(c) = kappa (mod 2^nu) and 2^nu >= 4 (lattice A3). Hole rows (offsets 0, 2) are T*+8 (mod 16). Base rows (offsets 1, 3) are T* (mod 16) and differ by 16. All label slots have offset 0 (mod 4).

(i) RIVAL PAIRS. Take an even label point E and a filler F. By Lemma rival (sec5_threshold.tex), with rows lo < hi there is j >= 1 with lo - j >= 1, hi + j <= h and 4j(d+j) = (x_E - x_F)^2, where d = hi - lo is odd. Since hi >= y_F >= h - H0, we get j <= H0.
- If y_E > y_F, then y_E > h - H0, which allows at most H0/2 even rows.
- If y_E < y_F, write x_E - x_F = 4delta. Then j(d+j) = 4delta^2 with d + j <= h + H0. For fixed (y_F, j) there are at most sqrt(j(h+H0))/2 values of delta >= 1. Each fixes d, hence y_E.
Summing over the at most (H0+2)/2 odd rows in [h - H0, h] (this covers every region type at once) and over j <= H0, with sum_{j<=H0} sqrt(j) <= (2/3)(H0+1)^{3/2}, gives the row bound. A label is the parity edge {2i+1, 2j+2}, so a given even row carries at most ceil(h/2) labels. This upper bound counts every non-label slot as a filler, so it survives any relocation, which only turns label slots into fillers.

(ii-a) The identities of sea_census_rigid.md B3 follow from the audited block_sea M2c equations n1 z = -e u2 and tau^2 + tau z + e(u2 + e) = 0 with tau = Delta - n1. Put w := -Delta - z. Then e u2 = n1(Delta + w) (I1) and (Delta - 2n1) w = e^2 + n1^2 (I2), which I re-derived. Put X = Delta - 2n1, Y = w and k = -z = X + Y + 2n1. Shallowness gives v2(k) <= 1 and 2n1 + k != 0 (mod 4). The value n1 = 0 would force u2 = 0, which is impossible.
- v2(u2) = 1 in both sea types (u2 = y_B - r0 with y_B = r0 + 2 mod 4).
- b := v2(e) = 2 for holes and b >= 3 for bases. c := v2(Delta) = 2 + v2(delta), so c = 2 for bases, c = 3 at offset 2 and c >= 4 at offset 0.
- (I1) gives v2(n1) = b + 1 - v2(k).
- k odd: Y is odd, so v2(X) = v2(e^2 + n1^2) = 2b, while v2(2n1) = b + 2. Then c < b+2 forces c = 2b < b+2, which is impossible. c > b+2 forces b = 2 and c >= 5. c = b+2 forces b >= 3 and c >= 5, which is offset 0, a hole with b = 2: a contradiction. So the only case is pattern (beta).
- k = 2 (mod 4): v2(n1) = b and v2(Y) = 1, because c >= 2. Then v2(e^2 + n1^2) = 2b + 1, so v2(X) = 2b. With v2(2n1) = b + 1, only c = b + 1 works (c < b+1 or c > b+1 give 2b in {c, b+1}, which is impossible for b >= 2). Bases (c = 2) would need b = 1, so this is a hole with c = 3: pattern (alpha).
- The shallowness of C holds in both cases.

(ii-b) Fix the filler row, so Q = u2 + 2e. (I1) and (I2) give the stated system. The converse is the audited M2c converse. Mirror symmetry (n1, Delta) -> (-n1, -Delta) lets us take n1 > 0, and then X, Y > 0. Eliminating Y through n1((X+n1)^2 + e^2) = eX(Q - 2e) and putting t = X + n1 gives (t+X)e^2 - XQe + t^2(t-X) = 0.

(ii-c)
- Fixed X. The discriminant in e must be a square W^2 = X^2 Q^2 - 4t^2(t^2 - X^2), that is (2t^2 - X^2)^2 + W^2 = X^2(X^2 + Q^2). So 2t^2 - X^2 is one of at most r2(X^2(X^2+Q^2)) << Q^eps values; each gives at most one t > 0 and then at most 2 values of e. The same works for Y, since the root tau = Y + n1 obeys the same identity. Also min(X, Y) <= sqrt(e^2 + n1^2) <= Q.
- Fixed n1. The curve n1 t^2 - n1 e^2 + 2e^2 t - Qet + Q n1 e = 0 has degree 3. As a quadratic in t it is primitive, and its discriminant e[e(2e-Q)^2 - 4n1^2(Q-e)] is divisible by e exactly once, so it is not a square. Hence the curve is absolutely irreducible. Points with t the smaller root lie in [0, Q]^2, and Bombieri-Pila gives << Q^{1/3+eps} of them.
- Lines. The system is homogeneous in (e, n1, X, Y, Q): it is the intersection of two quadrics in P^4. A non-degenerate rational line would project from the vertex (0:0:0:0:1) to a rational line on XY = e^2 + n1^2. That quadric has discriminant -1/4, so its rulings are defined over Q(i) only. Lines through the vertex need e = 0.

(iii-a) FEO. Put g = n_V - n_P, t = n_Q - n_P and f = y_V - y_P.
- Q-vertex: 16(n_V - n_Q)(n_P - n_Q) + (y_V - y_Q)(y_P - y_Q) = 0. The second product is odd times odd, so the left side is odd and cannot vanish.
- P-vertex: 16 g t = -f (y_Q - y_P), and y_Q - y_P is odd.
  - Holes: v2(f) = 3 and g is even. The left side has valuation >= 5, the right side 3: impossible.
  - Bases: g is odd, so v2(t) = v2(f) - 4. A label slot needs v2(t) >= 2 (offset 0), and the same class needs v2(t) >= 4 under i mod 16.
- V-vertex: write y_Q = y_e(n_P) + 2t, where y_e is the even-row line of Q's block, and put kappa' = y_V - y_e(n_P), which is odd. Then t(16g + 2f) = 16g^2 + f kappa'.
  - Holes: v2(16g + 2f) = 4 and v2(16g^2 + f kappa') = 3: no integer t.
  - Bases with v2(f) >= 5: both sides have valuation 4 exactly, so t is odd and Q would sit at an odd offset, which is not a label slot.
  - Bases with v2(f) = 4: f = 16f' with f' odd and D = g + 2f' odd. Then t = (g^2 + f' kappa')/D. Since g = -2f' (mod D), D divides f'(4f' + kappa'), and t = D + N/D - 4f'. Inside a class, kappa' = f - T, so N = f'(20f' - T).
  - The closed form matches the brute force over |g| <= h^2/8 exactly (feo_closed.py check), and lcd.py (the note's checker) finds exactly the same two V2:Feo triples at h = 241, s = -20.
- SAW is forced: CE (Lemma 2) requires v2(dy) <= 3 + v2(g) for every filler pair. Two bases at slot distance 2 (mod 4) have v2(g) = 1, so v2(dy) <= 4. Theorem 1(2b) needs H(1) != H(3), with both base rows r1 mod 16. So the base rows differ by 16 (mod 32), and for every label exactly one base row has v2(f) = 4.
- Thickness in SAW. D = f' always divides N. It gives g = -f' and t = 17f' - T. This t is always an integer, it is 0 mod 16 iff f' = T (mod 16), and the offset condition is f' = -a (mod 4). Explicit instance at h = 241 (iota = 1, s = 33): P = (324,163), V = (312,211), Q = (260,198), with dot product 12·(-52) + (-48)(-13) = 0. The fourth corner W = (272,150) has an even row, and its column holds the odd filler at row 227, so the triple is fatal. For a fixed region type with T = -a (mod 4), a positive proportion of (label, T) pairs satisfies the congruences and the range conditions (18 f' <~ T, W in the grid), so there are >= c h^2 triples with all slots occupied. This branch has bounded degree (D in {+-f', +-(20f' - T)}), but the divisor branches dominate: 63151 of 834161 hits at h = 20481 are linear.
- SAW* kills everything.
  - P-vertex: the v2 >= 5 base row has v2(f) = 5 exactly, because y_V = y_P + 32 (mod 64). So v2(t) = 1, offset 2, and no label slot in any block.
  - V-vertex: kappa' = y_V - y_eP = f - T_P (mod 8), because the A3 lattice gives c_Q = c_P (mod 2^{nu+1}). So f' kappa' = -f' T_P (mod 4). The rule for T* gives f' T_P = 3 (mod 4): case T = 3 has T* - 16 = y_P + 16 (mod 64), so f' = 1 (mod 4); case T = 1 has T* = y_P + 48, so f' = 3. Hence g^2 + f' kappa' = 2 (mod 4), v2(t) = 1, and Q would sit at offset 2.
  - Holes are excluded as above, and the Q-vertex by parity.
  - The one-label Feo (Q the even point of P's own label) needs g^2 = f'(T - 16f'), so f'T = 1 (mod 8). That fails in SAW*. In SAW it gives at most r2(T^2) labels per diagonal, which is harmless.

(iii-b)
- Parity: C + D - A - B needs an even row sum. With fillers odd, a support with exactly one even point is impossible.
- ll/FF and FF/ll: |L2 - L1|^2 = 5d^2 in (n, Y) units, with d = 0 (mod 8) under i mod 16. Then Dmu^2 = 5d^2 - DH^2 with DH in {+-2, +-4, +-6}. After dividing out powers of 2 this needs x'^2 = -1 (mod 16), x''^2 = -1 (mod 4) or x'^2 = 7 (mod 16), all impossible. DH = 0 needs 5d^2 to be a square. Even-even pairs differ by the same vector (4Di, 2Di), so the argument is the same.
- Cubic: with Sigma = 2(L2 - L1) + V - U, the condition Sigma·U = 0 together with |U| = |V| gives |U - V|^2 = 4(L2 - L1)·U. Put P = X1 - X2 and Qs = X1 + X2, with P·Qs = Y2^2 - Y1^2, and eliminate Qs.
- Same filler row: the cubic is homogeneous and equals F(p,u,v). The partial derivatives vanish at (0:1:1) (sympy), so the curve is a nodal, hence rational, cubic. Lines through the node, p = m d, give d[d(m^3 - 4m^2 - 3m + 4) - 4v(m-2)] = 0, which yields the parametrization; T2 is (p, u, v) = (-6, 5, 7) with m = 3.
- Sigma_Y = 2d + v - u = d, so N_y = 2d rows. The corner q = F1 + N then has row y_F + 2d.
  - d > 0: we need 2d <= h - y_F <= H0, so d is at most 19 (SAW) or 43 (SAW*), and d is a multiple of 8. Integrality of x1 = d(a^2+b^2)/(4b(a-2b)) with gcd(b, a^2+b^2) = 1 forces b | d. Since a^2 + b^2 = 5b^2 (mod a - 2b), also (a - 2b) | 5db^2. So only finitely many (a, b) remain, giving O(1) quadruples per class and filler row. Example: m = 12 (ratio 29:28, d = 8), which appears once per class at every h tested.
  - d < 0: N points down. Scaling about the centre O' (the intersection of the class line and the filler row) by lambda = 1 (mod 2^K) preserves every slot and row congruence, and integrality. The lowest of the six points stays >= 1 for lambda <= h/D_shape. So each admissible shape gives about h/(2^K D_shape) instances per class.
- Instance check (h = 1281, by hand): A = (644,323), B = (760,1251), C = (708,355), D = (440,1251). Then |AB|^2 = |CD|^2 = 874640, N = (-128,16), N·(B - A) = 0, p = (516,339) and q = (632,1267) lie in the grid.
- Scaling check: the 53:101 shape recurs at depths 6, 14, 22, 30, 38, 46 times 53, which is an arithmetic progression in lambda (fofo_shapes.py).

(iv) The cross-block cubic is the same elimination with L2 - L1 = (Dx, Dy).

## External results used

- Bombieri and Pila, Duke Math. J. 59 (1989), Theorem 5: an absolutely irreducible plane curve of degree d has <<_{d,eps} N^{1/d+eps} integer points in [0,N]^2. Cited from memory; I did not re-open the paper.
- r2(n) <= 4 tau(n) and tau(n) << n^eps (standard).
- Repository inputs: Lemma rival and Lemma mixedeq (paper). block_sea_classification.md Theorem 2 M2c equations and converse (audited). sea_census_rigid.md B3 identities (I1)-(I2), re-derived here. deep_layer_sawtooth.md SAW, Theorem 1(2b) and Lemma 2 (CE). Lattice A3 of deep_layer_bh16.md. deep_layer_u3.md Proposition R, the template for (i).

## Checks

All scripts are in the matching scripts_ folder of this directory. Each ran one at a time with py, under 60 s and under 1 GB. The repository was not touched.
- feo_formula.py (brute force) and feo_closed.py (closed form) match on 12 diagonals at h = 241. lcd.py and lc.py (copies of the note's checker) find the same two V2:Feo triples at h = 241, s = -20.
- feo_verify.py rebuilt the SAW board with lcd.build and checked 38 deep Feo hits at h = 641 from the definitions: right angle, colours, and W white in a column with an odd point. 38 passed, 0 failed.
- feo_fast.py, V-vertex Feo per label (all slots, near-band labels excluded): 0.0138 (h = 401), 0.027 (641), 0.054 (1281), 0.078 (2561), 0.097 (5121), 0.113 (10241), 0.127 (20481).
- feo_lin.py: linear-branch hits 870/7972 (h = 2561), 15515/185562 (10241), 63151/834161 (20481).
- feo_pvertex.py, P-vertex per label: 0.031 (401), 0.091 (1281), 0.133 (2561); every hit has v2(y_V - y_P) >= 8.
- feo_graph.py, F_T: degeneracy 2 and max degree 5 at h = 1281, max degree 8 at h = 2561; 27 and 79 diagonals are not bipartite.
- sawstar_feo.py (brute force over g and over Q, all three vertex types):
  - SAW at h = 641: V-vertex 55, P-vertex 162, Q-vertex 0;
  - SAW with i mod 32 but the old T*: V-vertex 16 or 13, P-vertex 0 or 16;
  - SAW*: 0/0/0 at h = 641 (iota = 1, 5) and at h = 961 (iota = 3, 9, 30).
- cubic_curve.py: node at (0:1:1); rational points listed, including T2 = (-6, 5, 7).
- fofo_cubic.py (exact cubic solver, both orientations), oo hits on the s = 0 diagonal:
  - i mod 8, h = 241: 90 (T2);
  - i mod 16: 0 (h = 241, 641), 2/37 (1281), 4/77 (2561), 7/157 (5121);
  - i mod 32: 1/79 (5121), 9/319 (20481);
  - i mod 64: 3/160 (20481);
  - i mod 128: 0/80 (20481);
  - SAW* is the same as SAW for these.
  - ee (Fe/Fe): 9/1479 (h = 641), 21/1953 (1281), 21/2293 (2561); SAW*: 14/1525 (1281).
  - Every hit has both fillers in one row.
- fofo_shapes.py: hits per class grow linearly in h (2, 4, 7, 14, 28 for h = 1281 to 20481). Every hit except the 29:28 shape (d = +8) has d < 0, and shapes such as 53:101 recur in arithmetic progressions.
- One Fe/Fe instance (h = 1281, s = -277) was checked directly against Lemma mixedeq.
- m2c_types.py: only types (offset 2, v2 k = 1, v2 Delta = 3) and (offset 0, k odd, v2 Delta >= 5) occur at h = 1001, 2001 and 4001, with 0 base fillers. Bad odd rows per residue: at most 3.
- m2c_count.py: |E(Q)| without congruences is 19 (Q = 1000), 6 (1002) and 39 (2002). The count tracks the divisors of Q, through scaling.

## Gaps

- (ii) is not proved: |E(Q)| = O(Q^{1-delta}) is missing when e, n1, X, Y and u2 are all of order Q. This is a dimension-growth problem for integral points on S_Q, beyond known general bounds. The census gives only 0 to 3 bad odd rows per residue for h <= 4001.
- (iii-b) is thick in SAW and SAW*. Its removal needs every class to be independent in the d < 0 nodal-cubic ratio graphs (oo: T-independent; ee: T-dependent), whose chromatic number is unknown. I did not prove that admissible d < 0 shapes exist for every class modulus 2^k: they were found for k = 4, 5 and 6, but not at k = 7 (h = 20481, 80 labels, too small a sample).
- Thickness is shown with all residue slots occupied. For real G_T classes, (iii-a) in SAW and (iii-b) are fatal only when both labels share a class, so the true load depends on the class colouring. I prove the edge sets are Theta(h^2) (iii-a: an explicit linear branch; iii-b: scaling families), but not a lower bound against every colouring.
- Inhomogeneous two-label quadruples (fillers in two different rows) are not counted. None appeared in any census up to h = 20481.
- (iv) Cross-block two-label quadruples, and cross-block Foo/Fee triples with W in a label column, are not counted. Only the cross-block Feo kill in SAW* is proved.
- (v) V3 among parked one-label triples: no progress.
- SAW* is checked for Feo only. I argued that Theorem 1, Lemma 4 and Proposition 5 of the note carry over, because T* = r1 mod 16 is kept and the split is finer, but I did not rerun the full lcd census on SAW*. Junction behaviour with the lower T* (>= h - 63) is unchecked.
- Nothing here is audited. The 2-adic lemmas (ii-a) and (iii-a) and the cubic reduction (iii-b) were each derived once by me and checked by exact computation.

## Missing estimate

Three estimates are missing.
(1) For (ii): #{e in (0, Q/2) : there are n1, X, Y >= 1 with XY = e^2 + n1^2 and n1(X + Y + 2n1) = e(Q - 2e), plus the congruences of (ii-a)} = O(Q^{1-delta}). Proved only for solutions with min(X, Y) <= Q^{1-delta} or n1 <= Q^{2/3-delta}. A possible route: average over T* in [h - h^theta, h] (theta < 1/3, so the rival-pair cost stays below h^2) and prove a mean-value bound. That needs two independent divisibilities, X | e^2 + n1^2 and e | n1(X+n1)^2, to be equidistributed.
(2) For (iii-b): chi of the ratio graph R_FF on depths below each filler row, with edges (u, (v0/u0) u) for the admissible d < 0 points of the nodal cubic F(p,u,v) = p^3 - 4dp^2 + (d^2 - 4du)p + 4d^2(u+v), and of its even-even analogue. The alternative is a deep layer under which no d < 0 point of this rational curve satisfies the congruences.
(3) For SAW only: chi(F_T), with edges i_P -- i_P + D + N/D - 4f', D | f'(20 f' - T). SAW* removes this need.

## Next steps

- Audit the 2-adic lemmas (ii-a) and (iii-a), including the SAW* Feo kill, and the reduction of (iii-b) to the nodal cubic with the d > 0 finiteness argument. Correct deep_layer_sawtooth.md: Feo is thick asymptotically (the census at h <= 401 hid it), and Corollary 6's claim that only vanishing-load families remain is false because of the d < 0 nodal-cubic families.
- Decide the (iii-b) route. One option is a 2-adic search for filler heights or label residues under which no d < 0 point of the parametrized curve satisfies the congruences: it is a finite check per height pattern in (a, b, kappa) mod 2^K. The other is to compute chi or the degeneracy of R_FF, as was done for R_IV.
- For (ii), try the average over T* in [h - h^theta, h]: write the mean of |E(Q)| as a lattice-point count with the two divisibilities X | e^2+n1^2 and e | n1(X+n1)^2, and look for a large-sieve bound.
- Run the full lcd census on SAW* at h of about 400 to 650 to confirm that nothing new appears with the lower T*. Extend fofo_cubic.py to two blocks for (iv), and to inhomogeneous filler pairs at h of about 10^4.
- Classify the parked one-label triples (FFo, FFe, label plus shallow) in SAW* by exact equations before attacking (v).

