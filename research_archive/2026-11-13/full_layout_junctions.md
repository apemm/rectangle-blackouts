# The full layout L** and its junctions

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: one explicit board specification for hypothesis (S), with every junction and boundary settled by proof. (S) reduces to a colouring of R_IV and a list of counting lemmas. The conditional bound is h^2 (log h)^1.4967 (loglog h)^C, because the sea exists only for stride 4. Not audited yet.

# Result

## Status

partial

## Summary

The full layout L** is specified, and all four junction questions (a) to (d) are settled by proofs. (S) is now reduced to an explicit list of counting lemmas plus chi(R_IV) finite. One correction: the sea machinery is stride-4 only, so the conditional bound is h^2 (log h)^1.4967 (loglog h)^C, not 1.369. That still beats T1.

## Statements

NOTATION. A = ceil(h/2), K = floor(h/2), q_h = AK, W_h = floor((h-1)^2/4)+1. Every obstruction, and every V3 pair, lies in 2W_h+1 consecutive columns. Label (i,j): odd row 2i+1, even row 2j+2, s = j-i, T = 2s+1. "Violation" means a failure of (V1)-(V5) of block_sea_classification.md (audited). That criterion is global only through 'every parity edge is one double'. Everything else is local.

BOARD L** (specification). Fix h >= h0 (h0 >= 80 for SAW, and large enough for the prime in (P6)).
(P1) Menu: stride 4 only. Heaviness: kappa_T = k_T^(2). Light threshold B = ceil((log h)^theta) with theta = 1.4967 (a = 0.91). This is heavy_light_split.md Theorem 3 with m = 1, audited.
(P2) Heavy diagonals H = {T : kappa_T >= B}. They go to the T1 side (P11). Every other diagonal is light.
(P3) Classes. Greedily colour G_T on each light diagonal (at most B classes). Then split each class by i mod 16, and by psi(u), where psi is a proper colouring of R_IV^(4) with X colours and u = (2i+1-r0)/2 (odd in every type).
(P4) Region types tau = (iota = i mod 16, an s mod 16 pair {c, c+4} with c mod 16 fixed). That makes 16 x 8 = 128 types. The s-pair fixes s mod 4, so label slots n = i + M_c are constant mod 4 (rho0_tau), as SAW requires. Each pair lies in a half-window, so (Hs) of sea_census_rigid.md holds. The sea row is r0 = 1 if iota is odd and r0 = 3 if iota is even. Put r1 = 2 iota + 1 (mod 16) and T*_tau = max{y <= h : y = r1 mod 16}.
(P5) Exceptional labels go to the relocation region (P10):
- i = 0;
- i = 2, and j in {0,1}, in row-3 types (Corollary B);
- near-band labels, with 2i+1 >= T*_tau - 128 (this includes the SAW Theorem 1(2b) exception and the Theorem 1(6) proviso), O(h) labels;
- the SAW Theorem 1(6) labels, O(sqrt h) per diagonal;
- the set Bad of Lemma J3.
(P6) One global prime p with 20h < p <= 40h and p = 3 or 7 (mod 20). This combines (Hp) p = 3 mod 4 with SAW's p = +-2 mod 5. Note that (5/p) = -1 is also the AR condition ((sigma^2+1)/p) = -1 at sigma = 2. Take 2^nu the least power of 2 that is >= K (Hnu), and a global kappa.
(P7) Region R_tau holds the type-tau classes of light diagonals:
- class c at columns 4(i + p m_c) + 4 b_tau, with distinct m_c, p m_c = s_c - kappa (mod 2^nu), filled residue by residue;
- every column x != 0 mod 4 holds the shallow point (x, r0);
- every deep column 4n without a label holds the SAW filler y(n) = T* - 24 + 8((n - rho0) mod 4). Removed labels leave SAW holes.
- The region extends 2W_h+1 columns of pure SAW past its first and last label columns, plus at most 3 slots, so that the end phases obey (Phi).
(P8) Buffer row: g(h) = h for even h, h-1 for h = 1 (mod 4), h-3 for h = 3 (mod 4). Pieces (each 2W_h+1 wide, deep columns = 0 mod 4):
- Sea(r0,g) = {(x,r0) : x != 0 mod 4} union {(x,g) : x = 0 mod 4};
- all-g = row g in every column.
Left to right:
row-1 tail | Sea(1,g) | R(64 row-1 types, separated by Sea(1,g)) | Sea(1,g) | all-g | Sea(3,g) | R(64 row-3 types, separated by Sea(3,g)) | Sea(3,g) | all-g | Sea(1,g) | row-1 tail.
(P9) Phase rule (Phi), needed only for odd h. Let delta = h - T*_tau (even, 0..14), and let offset o carry row T* - 24 + 8o. The bad pair (o, kappa) of the type is:
- h = 1 (mod 4), g = h-1: row-1 types have none. Row-3 types: delta = 0, 4, 8, 12 gives (o, kappa) = (1,2), (3,1), (2,2), (0,3).
- h = 3 (mod 4), g = h-3: row-1 types: delta = 4 gives (2,3) and delta = 12 gives (3,3), with j = 3; delta = 0, 8 have none. Row-3 types: delta = 2, 6, 10, 14 gives (1,2), (3,1), (2,2), (0,3), with j = 1.
Rule: at a region's right end, the first buffer slot n0 has n0 - rho0 = o + kappa + 1 (mod 4). At a left end, the first SAW slot n0' has n0' - rho0 = o + 1 (mod 4).
(P10) Relocation: one instance of the paper's Proposition partial, applied to all exceptional labels (P5) and to T1's exceptional labels:
- case (a) for even h, as a window inside the row-1 tail;
- case (c) for odd h, its switch column taken as the global switch z.
The T25 star is not used. If kept, it is one more row-1-tailed window and is glued by J5 with no further analysis.
(P11) Switch z: row 1 for x < z and row h for x >= z outside all windows. Right of z come the Theorem E blocks (t1_cost_decomposition.md, audited) for the labels of H, which have row-h collars and tails.
(P12) Truncate to columns 1..m for every m >= M.

LEMMA J1 (SAW | Sea(r0,g) seam; PROVED here). Let r0 be in {1,3}, with SAW rows = r1 (mod 8), r1 = 3 mod 4 when r0 = 1 and r1 = 1 mod 4 when r0 = 3. Let g be even with g > (h+1)/2 and 2g-3 > h, and T* - 24 > 5. In the seam configuration (shallow row r0 everywhere, deep columns SAW left of z0 and row g right of z0, or the mirror), every violation that contains both a SAW filler and a row-g point is a rival pair {filler in row c, row-g point}. For g = h there is none. For the odd-h g of (P8) there is none exactly when the end phases obey (Phi). The bad pairs listed in (P9) are the only ones.
LEMMA J2 (buffer chain; PROVED, extending audit_sea_row3_split.md). For h >= 10 and g = g(h), the following carry no obstruction:
- each piece: Sea(1,g), all-g, Sea(3,g);
- each seam: row-1 tail | Sea(1,g), Sea(1,g) | all-g, all-g | Sea(3,g), in both orientations.
For h = 3 (mod 4) the choice g = h-1 fails whenever h-3 is the square of an even number (h = 39 confirmed), which is why g = h-3 is used.
LEMMA J3 (relocation closure; PROVED). For a region with label set Y0 and Lambda a subset of Y0, let F(Lambda) be the region in which the columns of Lambda hold their labels and every other deep column holds its SAW filler. Let Bad be the set of labels lambda that lie in some Lambda with |Lambda| <= 7, such that F(Lambda) has a violation whose label columns (black corners or W) are exactly the columns of Lambda. If F(empty set), the pure SAW gap, has no violation, then F(Y0 \ Bad) has none.
LEMMA J4 (classes of one diagonal never meet; PROVED). In any L(k) layout, two classes of one diagonal are more than 40h^2 - 44h > 2W_h + 1 columns apart. So no obstruction or V3 pair contains points, fillers or shallow points near both of them. Hence the i mod 16 split and the psi split create no new interaction.
LEMMA J5 (gluing with one switch; PROVED, the audit's Corollary F fix written out). Take windows separated from each other, and from z, by more than 2W_h columns, and blocks that are violation-free with constant tails (row 1 left of z, row h right of z). The doubles of all blocks together carry each parity edge exactly once. Then the union is valid, and so is its truncation to columns 1..m.

THEOREM J6 (assembly; CONDITIONAL). Assume:
- (O1) chi(R_IV^(4) restricted to odd u <= h/2) <= X;
- (O2) and (O3): the open counting lemmas (list in Proof, section 7) give |Bad| = O(h^(2-delta)) in the F(Lambda) sense of J3;
- the unaudited inputs (U1) to (U3).
Then L** is a valid blackout with m + q_h points for every m >= M, and
 M <= C X h^2 (log h)^1.4967 (loglog h)^C1 + C h^2.
So m_h is at most this, which beats T1 whenever X <= (log h)^c with c < 1.056 (after re-balancing B). If chi(Gamma) < infinity, then H is empty and m_h = O(X h^2).
NOT PROVED: (S) itself, (O1) to (O3), and m_h = O(h^2).

## Proofs

0. WHY STRIDE 4 ONLY. Corollary B, SAW, the L* census and B3 all use the stride-4 geometry: shallow columns != 0 mod 4, deep columns = 0 mod 4, and the 2-adic laws at sigma = 2. None of them exists for strides 2, 8, 12 or 20. So (S) can be specified only for stride-4 rigid regions. The menu {4} has theta = 1.4967 (audited table), which is still below 2. Recovering 1.369 needs a sea for the other strides, which is open and not needed for the near goal.

1. LEMMA J1. Points: shallow points S = (x, r0) for x != 0 mod 4 (both sides); SAW fillers (4n, c) with c in {T*-24, T*-16, T*-8, T*}, all = r1 mod 8; and row-g points in deep columns. Two SAW fillers at slot distance d have row difference 8m, where m is the offset difference in {-3..3} and m = d (mod 4). A violation without a row-g point lies in the pure SAW gap, the input (U1). A violation without a SAW point lies in the pure Sea(r0,g), which is clean by block_sea Proposition 3 and audited Corollary B. So only "mixed" supports matter.

(a) Corner triples with a shallow corner, r0 = 1. block_sea Theorem 1 (audited) gives exactly one shallow corner E, with F and G deep.
- Pa needs F and G in two distinct even rows. The only even deep row is g. Impossible.
- Pb needs rows = 3 mod 4, so F and G are both SAW: pure.
- X1 needs y_G = 5 (mod 8), but SAW rows are 3 or 7 mod 8. Impossible.
- Pc needs y_G - y_V even, so both are SAW (pure) or both are row g. Both row g makes VG horizontal, and then the rectangle is not tilted.
- X2 needs y_V = 1 (mod 4). SAW rows are 3 mod 4 and g is even. Impossible.
r0 = 3: the seam configuration satisfies (H1) to (H3) of the audited Theorem A: all rows are >= 3, no deep point is in row 4 or 5, and odd deep rows are 1 mod 4. The shifted list applies with the same five checks: Pa needs two distinct even rows; Pb needs rows 1 mod 4 (pure SAW); X1 needs 7 mod 8 while SAW rows are 1 or 5 mod 8; Pc is as above; X2 needs y_V = 3 mod 4. Theorem A also excludes low-W triples with a shallow corner. Two shallow corners in row 3 are opposite, and they put the fourth corner in row 6 - y < 1.

(b) All-deep corner triples (any r0). Write V and the two ends with leg vectors (4a1, e1) and (4a2, e2), so that 16 a1 a2 = -e1 e2.
- Ends F and G both in row g, with V SAW: e1 = e2 = g - y_V is odd. Impossible.
- V in row g, F and G SAW: e1 e2 is odd. Impossible.
- V and one end SAW, the other end in row g: e1 is odd, and e2 is a nonzero SAW difference with v2 in {3, 4}. Then v2(e2) = 4, which forces e2 = +-16 and a1, a2 odd. But a row difference of 16 means an offset difference of 2 (mod 4), so a2 is even. Contradiction.
- Two row-g corners that are adjacent make a horizontal side, so the rectangle is not tilted.
So there is no seam triple, no fully black rectangle and no parked seam triple. The pure parts have no parked triples either (U1, Proposition 3), so there is no V3 pair.

(c) Mixed quadruples with a shallow point. block_sea Theorem 2 lists the possible shallow sets; row 3 is covered by its shift together with item (iii) of the row-3 proof as audited.
- M1C needs A and B in even rows with difference 2 mod 4, but only g is even.
- M2a needs a same-parity deep pair whose rows are not congruent mod 8. SAW pairs are congruent mod 8, and two row-g points are in the same row.
- M2c needs a deep pair B, D of the same parity in distinct rows. So both are SAW, and the support is pure.
- The low items for r0 = 3 need a deep pair with row difference 2 or 4. No such pair exists.

(d) All-deep mixed quadruples. Use C + D = A + B + 2n with n.u = 0 and |D - C| = |u|. All columns are 0 mod 4, so n1 is even. Let alpha and gamma be the numbers of row-g points in {A,B} and in {C,D}. Row parity forces alpha = gamma (mod 2).
- alpha = gamma = 2: n2 = 0, so n = 0. Impossible.
- alpha = 2, gamma = 0, or the reverse: one pair is horizontal and the other is a SAW pair at integral distance. By SAW (2a), which I re-derived (m = +-1: no solution; m = +-2: delta = 3, against delta = 2 mod 4; m = +-3: delta = 8, against delta odd), that SAW pair is horizontal too. Then D - C = +-u. Impossible.
- alpha = gamma = 1: say the side is {G1, S1} and the diagonal is {G2, S2}, with sigma = g - s1 odd and s2 - s1 = 8m. Then n2 = 4m, and m != 0 (otherwise n = 0). Perpendicularity gives a n1 = m sigma, with 4a the column difference of the side. n1 is even and |m| <= 3, so v2(m) = 1, v2(n1) = 1 and a is odd. The norms give a^2 - c^2 = -m G'' with G'' = (2g - s1 - s2)/2, which is odd because s1 + s2 = 2 (mod 4). So a^2 - c^2 = 2 (mod 4) with a odd. Impossible.

(e) Rival pairs.
- Shallow points: row 1 is never in a rival pair. For row 3, t != 0 mod 4 against the even row g: j = 1 needs g - 2 odd, and j = 2 needs 8(g-1) to be a square. Impossible.
- SAW-SAW and g-g pairs have rows of equal parity. Impossible.
- SAW filler (row c, odd) with a row-g point: 4j(|g - c| + j) = t^2, where j <= min(lower - 1, h - upper) and t = 4 kappa (both columns are deep).
  - g = h: none, because j <= 0.
  - g = h-1: only j = 1, which needs h - c = 4 kappa^2. With h - c = delta + 8a, the bad cases are delta = 0 mod 4 (delta + 8a in {4, 16, 36}).
  - g = h-3: j = 1 needs delta + 8a - 2 = 4 kappa^2. j = 2 gives 2 x odd, never a square. j = 3 needs 3(h - c) = 4 kappa^2, so h - c = 12 and kappa = 3.
  - SAW rows above g: only c = h-2 for g = h-3, with 4j(1+j) in {8, 24}, never a square.
  Hence the table in (P9). Each type has at most one bad pair, with kappa <= 3. The pair needs the bad filler within kappa slots of the buffer, so (Phi) leaves exactly the offsets o+1..o+kappa in those slots. [] This also explains the h = 67 (row-1 type) and h = 85 (row-3 type) pairs reported in deep_layer_sawtooth.md: both runs used g = h-1, and delta = 0 (mod 4) in both cases.

2. LEMMA J2.
- Sea(1,g): Proposition 3.
- Sea(3,g): audited Corollary B (2g - 3 > h, g even).
- all-g: a single row is a chain (Lemma chain), and a rival pair needs two parities.
- row-1 | Sea(1,g) and Sea(1,g) | all-g: all points lie in rows 1 and g, so the paper's Lemma sea applies (g even, 2g - 1 > h).
- all-g | Sea(3,g): rows 3 and g.
  - Two corners in one row are opposite, and the fourth corner is in row 6 - g < 1 or 2g - 3 > h.
  - Mixed quadruples: the parity argument of Lemma sea with 3 + g odd.
  - Rival pairs: j <= 2. j = 1 needs g - 2 to be the square of an even number, which fails for g = h (j <= 0 there) and for g = 0 mod 4 (then g - 2 = 2 mod 4). j = 2 needs 8(g-1) to be a square, impossible.
For h = 1 (mod 4), g = h-1 = 0 (mod 4). For h = 3 (mod 4), g = h-3 = 0 (mod 4), and 2g - 3 > h needs h >= 10. []

3. LEMMA J3. A violation is fixed by its black points, its white corner W and the content of W's column, which is at most 7 columns for a V3 pair. So whether it occurs in F(Y) depends only on Y intersected with the labels of those columns. Suppose F(Y0 \ Bad) has a violation.
- If it involves no label column, it is a violation of F(empty set). That is excluded.
- Otherwise let Lambda be the labels of Y0 \ Bad whose columns it involves. It is then a violation of F(Lambda) whose label columns are exactly those of Lambda, so Lambda is contained in Bad. Contradiction. []
Consequences:
- Relocation is self-consistent: removing labels only creates SAW holes, and the families have to be counted in the F(Lambda) sense, with every other deep column a filler. The SAW kills are stated for arbitrary fillers, so they are already in this sense.
- Relocated labels cost c0 |Bad| tau*(h)^2 = O(h^(2-delta+o(1))).

4. LEMMA J4. Classes c and c' of one diagonal have M_c = M_c' (mod 2^nu) and M = p m, so m_c = m_c' (mod 2^nu) and |m_c - m_c'| >= 2^nu >= K/8. Their points are at least 4(p 2^nu - A) >= 10hK - 4h >= 5h^2 - 9h columns apart (40h^2 - 44h under (Hnu)). That exceeds 2W_h + 1 <= (h-1)^2/2 + 3 for h >= 4. So no local object contains points from both classes, or from their neighbourhoods of width W_h. []
Compatibility (d):
- Independence in G_T is hereditary, so every subclass is a valid class for Proposition R.
- The i mod 16 split sends subclasses to different regions, and the psi split keeps them on one diagonal. By J4, neither creates any cross interaction.
- R_IV edges join slots in one residue class, so psi is needed inside each (i mod 16) subclass; it is applied per type, through u = (2i+1-r0)/2.
- Light and heavy are a partition of the diagonals, relocation is a partition of the light labels, and Theorem E takes whole heavy diagonals. So each parity edge occurs exactly once.
- Per type and per diagonal there are at most B X classes. Each residue mod 2^nu serves at most 2 diagonals, so m_c < 4K B X and the region width is < 320 h^2 B X + 4A. Over 128 types this is < 40960 h^2 B X + O(h).
- Translating a whole region by a multiple of 4 shifts every M_c and every n(c) by the same amount, so every region proof, which uses only differences and residues mod 4, is unchanged.

5. LEMMA J5. Take a violation, or V3 pair, Q. It spans at most 2W_h + 1 columns.
- If Q meets a window U_k, then Q lies in U_k extended by 2W_h, where the union equals block k with its constant tail. Block k is violation-free there.
- Otherwise every point of Q is in row 1 at x < z or in row h at x >= z. That set is a chain (no corner triple, no mixed quadruple), and Lemma rival forbids rows 1 and h.
Every parity edge is a double exactly once, so the criterion (V1)-(V5) gives validity. Truncation removes whole columns, so it creates no violation. []
The heavy blocks of Theorem E have row-h collars at both ends. The rigid chain and the case-(a) relocation window have row-1 tails. Case (c) supplies its own z, which is the global z.

6. THEOREM J6.
- Inside each R_tau the label part and the label-sea part hold by (U1) to (U3) and (O1) to (O3), and the R_IV family is removed by psi.
- The ends of each R_tau hold by J1, using margins of 2W_h + 1 of pure SAW so that no label can see a seam.
- The chains hold by J2, closure by J3, splits by J4, and global gluing by J5.
- Width: 40960 B X h^2 for the regions, about 134 (2W_h + 1) for buffers, 256 (2W_h + 1) for margins, c0 n tau*^2 for relocation, and C(Delta h Lambda^2 ell^C1 + h^2 ell) for the heavy blocks, with Delta = H_d(B) <= C h (log h)^(E-1) B^(-a) and E = (1 + 3^a)/2.
With B = (log h)^1.4967 this gives the bound. If X grows, the light term becomes B X h^2, and re-balancing gives an exponent of about 1.4967 + 0.476 log_(log h) X. []

7. LEMMAS STILL NEEDED FOR (S). Status and owning note for each.
(O1) chi(R_IV^(4)) < infinity. Enough for the near goal: X <= (log h)^1.05 on u <= h. OPEN. Owner: sea_census_rigid.md B4. Numerics: bipartite, degeneracy 2 up to 2*10^6.
(O2) O(h^(2-delta)) hit counts in the F(Lambda) sense, label plus shallow (owner sea_census_rigid.md B1, B2, B3(C3), B6). All OPEN; empty only below the stated thresholds.
- (a) I.2 (empty for h <= 81632);
- (b) II(1,-1) (empty for h <= 39900);
- (c) odd-odd M2c across classes. By J4 only pairs on different diagonals matter (empty for h <= 2550);
- (d) V3 between parked SLL triples (no threshold; 0 among 6.2*10^5).
(O3) SAW residual families in the F(Lambda) sense. All OPEN; owner deep_layer_sawtooth.md, Gaps and Missing estimate, unless noted.
- (i) rival pairs of an even label with a filler (K3), heuristically about h^1.5;
- (ii) M2c with one label and one filler;
- (iii) two-label Fe/Fe and Feo (S3 type);
- (iv) cross-block families with fillers other than S5;
- (v) V3 among parked one-label triples;
- (vi) in row-3 types, deep-only violations with W, p or q in row 1 or 2, the S3-low analogue under SAW (owner audit_sea_row3_split.md issue 2, re-posed for SAW);
- (vii) V3 between a filler triple and an SLL triple (sea_census_rigid.md B5).
(U1) SAW Theorem 1 (1)-(6), Lemma 2, Lemma 4, Proposition 5 and Corollary 6. UNAUDITED; owner deep_layer_sawtooth.md. J1 needs only the definition of SAW and (2a), which I re-derived. J3 needs (4') and (3), that the pure gap is clean.
(U2) sea_census_rigid.md B1 to B4 and B6. UNAUDITED.
(U3) deep_layer_bh16.md A1 and A3. UNAUDITED; A2 is re-derived in SAW.
(P) A prime p = 3 or 7 (mod 20) in (20h, 40h]: true for large h by the prime number theorem in progressions. No explicit h0 checked. Small h are irrelevant for the asymptotic bound.
PROVED HERE, audit owed: J1, J2 (odd-h rule), J3, J4, J5, and the table (P9).
AUDITED INPUTS USED: Proposition R, Lemma G, Theorem 3 (heavy_light); Theorem A and Corollary B with the g fix (sea_row3); Theorem E and the Corollary F switch (t1 decomposition); block_sea Theorems 1-2 and the criterion; rigid Theorem C; the paper's Lemmas sea, rival, chain, block, Proposition partial and locality.

## External results used

- Paper sec5_threshold.tex: Lemmas reduction, rival, sea, chain, counting, block; Proposition partial cases (a) and (c) with the switch column z; locality 2W_h+1.
- block_sea_classification.md (audited): criterion (V1)-(V5), Theorems 1 and 2, Proposition 3.
- sea_row3_split.md Theorem A and Corollary B, with the corrections of audit_sea_row3_split.md (H4 dropped, g condition).
- heavy_light_split.md Proposition R, Lemma G, Theorems 1 and 3 (audited); t1_cost_decomposition.md Theorem E and the Corollary F switch fix (audited).
- deep_layer_sawtooth.md (unaudited): SAW definition, Theorem 1, Lemma 4, Corollary 6; sea_census_rigid.md (unaudited): L*, B1-B6, R_IV.
- Quadratic reciprocity ((5/p) = (p/5)); prime number theorem in arithmetic progressions mod 20 (asymptotic existence only).

## Checks

Scripts are in the script folders of this directory. Each ran with py in under 60 s. The repository was only read.
- seam.py: a definition-level finder for one-point-per-column boards (numba). It finds tilted rectangles with >= 3 black corners (classified fully black, fatal or parked by W's column parity), V3 pairs, mixed quadruples (diagonal pair CD, then pq with the same midpoint and length, then AB = pq - n, AB not vertical) and rival pairs. It reports violations that contain both a SAW filler and a row-g point. The logic follows the audited chk.py, rewritten for single-point columns.
- Positive controls. At h = 49 with g = 48, all 4 phases on both sides for every row-3 residue: rival pairs appear exactly at the phases (Phi) forbids, and vanish exactly at the allowed ones, for (o, kappa) = (1,2), (0,3), (2,2), (3,1). The h = 67 pair (filler row 51 = h - 16, gap 8, g = h-1) and the h = 85 pair (row 69, row-3 type) are reproduced. The h = 83 j = 3 pair (row 71 = h - 12, gap 12) is reproduced at a wrong phase. In chain.py, h = 21 with g = 18 and h = 39 with g = 38 give rival pairs at the all-g | Sea(3,g) seam (g - 2 an even square).
- Clean runs with g = g(h) and the phase rule: h = 48 and 50 (all 8 row residues, both sides), 49 and 51 (all residues, both sides), 67 (g = 64, all phases), 81 and 83 (all 8 residues), 82 (4 cases) and 85 (allowed phase). In every case 0 fatal or fully black triples, 0 V3, 0 mixed quadruples and 0 rival pairs at the seam.
- chain.py at h = 51 with g = 48, and h = 49 with g = 48: row1|Sea(1,g), Sea(1,g)|all-g, all-g|Sea(3,g), Sea(3,g)|all-g, all-g|row-h and row1|row-h are all clean.
These are sanity checks at small h. The statements rest on the proofs.

## Gaps

- (S) is not proved. It reduces to (O1) to (O3) and the unaudited inputs (U1) to (U3). None of (O1) to (O3) has a proof: they are counting or colouring statements, backed only by censuses and by thresholds in h.
- J1 to J5 and the phase table were checked once, by me. They need a second-reader audit. J1 depends on the SAW definition and on (2a), which I re-derived. It assumes that the pure SAW gap and the pure Sea pieces are clean; for SAW that is the unaudited Theorem 1(3),(4'), which needs h >= 80.
- The specification is stride-4 only, so the conditional exponent is 1.4967, not 1.369. A sea for strides 2, 8, 12 and 20 does not exist yet.
- The relocation counts must be proved in the F(Lambda) sense of J3, with every other deep column a filler. The censuses in the notes used actual boards with all slots occupied, which is not the same quantity.
- Theorem E blocks are glued as 'violation-free with row-h tails' on the authority of audit_t1_cost_decomposition.md (Corollary F fix). I did not re-check T1's safe-triangle notion against (V1)-(V5) at the block ends.
- No explicit h0 for the prime p = 3 or 7 mod 20 in (20h, 40h], and none for h >= 80 in SAW. The theorem is asymptotic.
- (Hs) needs the s mod 16 pair split, which doubles SAW's 64 types to 128. I did not re-check sea_census B3 (C1) and (C3) with the pair split rather than a full half-window, though the pair lies in a half-window, which is all that (Hs) asks.
- The constants are astronomical: c0 = 48*2^31 in Proposition partial, and 40960 B X in the regions. Only the asymptotics are claimed.

## Missing estimate

Every junction is now closed by proof. (S), and with it the near goal, a full valid board in width C X h^2 (log h)^1.4967 (loglog h)^C1, follows from three groups of estimates.
(O1) A proper colouring of the ratio graph R_IV^(4) on odd u <= h with X <= (log h)^1.05 colours. Finite chi is the clean target; numerically R_IV is bipartite with degeneracy 2.
(O2) For the label-shallow families I.2, II(1,-1), odd-odd M2c across classes of different diagonals, and V3 between parked SLL triples: at most O(h^(2-delta)) labels hit. Each family needs two independent coincidences of size about 1/h, while averaging over p supplies only one.
(O3) For the SAW residual families (rival pairs even label + filler, M2c label-filler, Fe/Fe and Feo, cross-block filler families, V3 among one-label parked triples, low deep-only violations in row-3 types, and filler-triple/SLL V3): at most O(h^(2-delta)) labels hit, counted in the F(Lambda) sense of J3.
Any family with load of order 1 per label would instead need a colouring split, as R_IV does. The cost is a factor X in B, which is affordable up to (log h)^1.05.

## Next steps

- Audit J1 (seam case analysis (a)-(e)), J2 (the odd-h rule g = h-1 or h-3), J3, J4 and J5. All are short and elementary. Then add ledger rows: 'SAW | Sea(r0,g) seam clean under g(h) and (Phi)' and 'relocation closure in the F(Lambda) sense'.
- Re-pose the census targets of (O2) and (O3) in the F(Lambda) sense: every non-Lambda deep column is a SAW filler. Rerun the existing censuses that way.
- Attack (O1). Finite chi is the clean target, but a degeneracy bound on [1,h] of order (log h)^1.05 is already enough for the near goal.
- Audit deep_layer_sawtooth.md Theorem 1, especially (3) and (4'), since J1 and J3 use the pure-gap cleanness.
- Optional: drop the T25 star and route the i = 0 labels through Proposition partial, as in (P10), which removes one region type from the board.
- Optional: build a Corollary B and SAW analogue for stride 8 or 12, to recover the menu exponent 1.369.

