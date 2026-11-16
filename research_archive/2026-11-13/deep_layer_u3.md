# The U3 filler rule: S2 removed at every distance

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: one filler rule for zones and gaps (U3) removes S2 in every form, with no zone/gap junction. S5 is untouched by U3, and its 2-adic removal costs Theta(h^3). Not audited yet.

# Result

## Status

partial

## Summary

One filler rule for zones and gaps alike, called U3, removes S2 in every form at every distance, with no zone/gap junction and no width cost. U3 puts holes in one row ρ ≡ r1+8 (mod 16) and base columns in rows R± ≡ r1 (mod 16) chosen by n mod 4, with R+ − R− ≡ 16 (mod 32) and ρ not the midpoint of R±. Earlier, BH16m4 failed only because its hole row was that midpoint (proved). S5 is not touched: its witnesses are always holes. Its 2-adic removal costs Θ(h^3) (proved). Options (a), (c) and (d) of the route each fail for a precise reason.

## Statements

SETTING. Region type (ι8, μ) as in BH16 and sea_row3_split Corollary B. ν = ι8+μ mod 2. Labels sit in columns 4n with n ≡ ν (mod 2), and their odd rows are ≡ r1 = 2ι8+1 (mod 16). The sea row is r0 ∈ {1,3} with r1 ≡ r0+2 (mod 4). The rigid layout is that of rigid_layout_cross_block Theorem 5. Deep point: (4n, y). Same-parity deep pair: D − C = (4δ, 2ε). DH means a deep M2a with a horizontal side and deep witnesses, as in Lemma A2.

DEFINITION U3(ρ, R+, R−). Every deep column 4n without a double gets one filler, by the same rule in block zones and in gaps:
- row ρ if n ≡ ν (mod 2) ("holes");
- row R+ if n ≡ ν+1 (mod 4), row R− if n ≡ ν+3 (mod 4) ("base").
Conditions:
- (U1) ρ ≡ r1+8 and R± ≡ r1 (mod 16), with R+ − R− ≡ 16 (mod 32).
- (U2) All three rows are > (h+r0)/2 and ≥ h − H0 for a constant H0.
- (U3) ρ ≠ (R+ + R−)/2.
The recommended instance is U3top: ρ = T1, the largest row ≡ r1+8 (mod 16), with R+ = ρ−8 and R− = ρ−24, so H0 = 39 and h ≥ 82. "Top labels" means labels with odd row ≥ ρ−40. That is at most 3 odd-row values per region type, so O(Bh) labels, and they are relocated by Prop. partial. BH16 is the degenerate case R+ = R−. BH16m4 is R± = {R, R−16} with ρ = R−8, which violates (U3).

LEMMA W (witness normal form; proved). Let C and D be odd deep points with y_D − y_C = 8e, e ≠ 0, and δ = n_D − n_C. They form the diagonal of a DH iff |δ| = v − u for positive integers u ≠ v with uv = e^2. The witness columns are then n_C ∓ u and n_C ± v, at distance L = u+v. Any common black row r ≠ (y_C+y_D)/2 of the two witness columns gives a black mixed quadruple.
- (W1) If e is odd, then u and v are odd, L ≡ 2 (mod 4) and δ is even.
- (W2) If e ≡ 2 (mod 4), then δ ≡ 2 (mod 4) is impossible.
- (W3) If δ is odd, then L is odd.

THEOREM 1 (U3 removes S2 and all horizontal M2a with a filler; proved). In a U3 region whose labels avoid odd rows R±:
- no shallow M2a, X1, X2 or M1C contains a filler;
- no DH has a filler among C and D, or has C and D in one block.
This covers BH16's S2 (label–hole, in the zone and far in the gap), the K5 one-row family, and every filler–filler DH, at every distance. The only DH left are label–label pairs in different blocks (S5).

THEOREM 2 (the pure U3 gap is valid; proved, given block_sea Theorems 1 and 2, sea_row3 Theorem A for r0 = 3, and an exact finite check). The sea plus U3 fillers, with no labels, has no obstruction (V1)–(V5). In fact it has no corner triple with 3 or more black corners at all, so it has no V3 collisions. Since zones and gaps use one rule, a region has no zone/gap junction.

THEOREM 3 (why BH16m4 failed; proved). Take base rows R± at residues ν±1 (mod 4) with R+ − R− = 16d, d odd, and hole row ρ ≡ r1+8 (mod 16). Consider a mixed quadruple whose side is two base fillers of different residues and whose diagonal is a hole C and a label odd point D. Put ω = (y_D − ρ)/8 (odd) and μ' = (2ρ − R+ − R−)/8. Then a = 2a' and c = 2c', with a' odd, a' | d(ω+μ') and a'^2 − c'^2 = ω^2 − 4d^2.
- (a) If μ' = 0 (BH16m4), then a' = ω, c' = 2d solves both equations for every label. This is the census's 2 per label.
- (b) For U3top (d = 1, μ' = 4), solutions need |ω| ≤ 3, that is, label rows in {ρ±8, ρ±24}, which are top labels.

THEOREM 4 (Lemma P and the Q4 obstruction; proved).
- (P) Suppose every two fillers with distinct rows satisfy v2(Δy) ≤ v2(Δn) + 3. Then no right angle has a filler vertex, one leg to another filler, and the other leg to an even point.
- If (P) fails for a pair, the perpendicular through the filler meets deep columns at rows of both parities. Every even point on that line whose fourth corner lies in the strip then gives a fatal triple.
- Corollary (type dichotomy). Assume all odd deep rows are ≡ r1 (mod 8) (K1) and (P). A gap layer whose fillers all lie in one class mod 16 has a single row, so it carries the K5 one-label family. In particular, the layer Q4 (four rows ≡ r1+8 mod 16, indexed by n mod 4) fails (P). Q4 provably has no horizontal M2a with a filler and no all-filler mixed quadruple, but in the census it has 50 to 65 fatal triples (F;F,Le) per block of 6 to 8 labels.

PROPOSITION R (rival pairs; proved). Under (U2), the number of rival pairs that contain a filler is O(H0^{3/2} B h^{3/2}). So the RELOCATION RULE handles them in o(h^2) width.

THEOREM 5 (S5; proved).
- (a) Take two labels of one region in different blocks. For an odd–odd Pythagorean pair, u and v are even. For an even–even Pythagorean pair, j_D − j_C ≡ n_D − n_C ≡ 0 (mod 2^ν). In both cases both witness columns have label parity. Under U3 or BH16, every such pair whose two witnesses are holes is therefore fatal. U3 does not help S5.
- (b) If ΔM ≡ 0 (mod 2^t) with 2^t ≥ 2A for all block pairs within reach, then no odd–odd label pair across blocks is Pythagorean.
- (c) Any layout that uses (b) has width ≥ (1 − o(1)) h^3/16. A fixed t kills only the pairs with v2(e) ≤ t−3.

PROPOSITION 6 (route options a, c, d; proved, except the computed shares).
- (a) and (c) change only hole contents inside blocks. They leave every BH16 S2 instance whose hole lies outside the block: 73% at h = 10^3, 78% at h = 10^4 and 81% at h = 10^5, by the exact formula.
- (c) Hole fillers in the sea row r0 are fatal for every label C whose column n_C + k(k+1), k = (|y_C − r0|/2 − 1)/2, is a hole. This is Prop 5 of block_sea.
- (a) Interleaving classes in one block keeps (E;O,E) dead. The single-class proofs no longer exclude in-block and steep cross-block (E;E,E) right angles.
- (d) For stride 2, the same A1/A2 dichotomy holds with "ε mod 4" replaced by "ε mod 2". The rigid modulus becomes 2^ν ≥ K/2 instead of K/8.

LEMMA M (margins; proved). Suppose the gap has one row r_g and each zone uses rows ≠ r_g on its block plus m ≥ h/32 slots on each side. Then no DH with C a zone label has both witnesses in gap columns.

WIDTH. U3 changes only filler rows. The width stays BH16's 320 h^2 B + O(h^2), plus relocation of the top labels (O(Bh) labels) and of the labels in rival pairs (O(B h^{3/2}) labels), both o(h^2) by Prop. partial.

NOT PROVED: m_h = O(h^2); S5 removed; a bound on S3, on S4 (V4 Fo/Fo and M2c with a label and a filler), or on V3 in U3 regions. These families are already present in BH16.

## Proofs

Notation: deep point (4n, y). For two deep points, U = B − A = (4a, α), V = D − C = (4c, γ), σ = n_C + n_D − n_A − n_B, β = y_C + y_D − y_A − y_B, and 2N = C + D − A − B, so N = (2σ, β/2). Lemma mixedeq then gives: (i) N·U = 0 ⟺ 16σa = −αβ; (ii) |U| = |V| ⟺ 16(a^2 − c^2) = γ^2 − α^2; also a ≠ 0, N ≠ 0 and V ≠ ±U.

1. LEMMA W. This is A2 of deep_layer_bh16 with ε = 4e.
- Pythagorean means L^2 = δ^2 + 4e^2 with L = L'/2. Then L ≡ δ (mod 2), so u = (L−δ)/2 and v = (L+δ)/2 are integers, uv = (L^2 − δ^2)/4 = e^2, and the witness offsets (δ ∓ L)/2 are −u and v.
- Conversely, uv = e^2 gives (v−u)^2 + 4e^2 = (u+v)^2.
- (W1) uv is an odd square, so u ≡ v (mod 4), L ≡ 2 (mod 4) and δ = v − u is even.
- (W2) δ even with uv even forces u and v even. Then u = 2u', v = 2v', u'v' = (e/2)^2 is odd, and δ = 2(v'−u') ≡ 0 (mod 4).
- (W3) v − u odd implies v + u odd.

2. THEOREM 1. Point types:
- λ: label odd point, parity ν, row ≡ r1 (mod 16);
- η: hole, parity ν, row ρ ≡ r1+8;
- β±: base, parity ν+1, rows ≡ r1.
Every odd deep row is ≡ r1 (mod 8). So every odd–odd pair has y_D − y_C ≡ 0 (mod 8), and A1 excludes shallow M2a. Even deep points are labels only, and A3 covers them. X1, X2 and M1C need odd deep rows ≡ r0 (mod 4) or ≡ r0+4 (mod 8) (sea_row3 Theorem A), and none exists. For r0 = 3, (H1)–(H3) hold because the fillers are high and r1 ≡ 1 (mod 4), and (H4) holds because the even points are labels, as in Corollary B. Witness columns of parity ν+1 are always base fillers, because no label has that parity.
Cases for DH:
- (λ,η): e is odd. By (W1), u and v are odd, so both witnesses have parity ν+1, and their residues mod 4 differ by L ≡ 2. One is β+ and one is β−, so their rows differ.
- (λ,β): e is even and δ is odd. By (W3) the witnesses have opposite parity. One is base (row R±). The other is a hole (ρ ≢ R± mod 16) or a label column (odd row ≠ R± by the exclusion, even row of the wrong parity). There is no common row.
- (η,β): e is odd, so δ must be even by (W1), but δ is odd. Not Pythagorean.
- (β+,β−): e ≡ 2 (mod 4) and δ ≡ 2 (mod 4), so (W2) applies. Not Pythagorean.
- (η,η) and (β,β) in one row: e = 0.
- (λ,λ) in one block: the displacement is (4δ, 2δ) and 20δ^2 is not a square.
- Even–even pairs in one class: the same 20δ^2 argument.
What is left is label–label pairs across blocks (S5).

3. THEOREM 2 (pure U3 gap, r0 = 1; for r0 = 3 use the shift invariance and the boundary items 2(ii)–(iv) of sea_row3).
- Leg valuations. Tilted filler legs are η–β with (v2 Δn, v2 Δy) = (0, 3), or β+–β− with (1, 4). So v2 Δy − v2 Δn = 3 for every tilted leg, and (P) holds.
- No all-deep right angle. It would need 16 Δn1 Δn2 = −Δy1 Δy2. The left side has valuation 4 + Σ v2 Δn = Σ v2 Δy − 2, a contradiction. A horizontal leg forces a vertical leg, which singleton columns rule out.
- Triples with a shallow corner (block_sea Theorem 1).
  - Pa needs even rows.
  - Pb puts W in row y_F + y_G − r0 > h, by (U2).
  - X1 and X2 need the residues excluded above.
  - Pc needs 4aγ = fg. Here v2 f = 1, v2 a ≤ 1, and (v2 γ, v2 g) ∈ {(0,3), (1,4)}. The left side has valuation ≤ 3 + v2 γ and the right side has 4 + v2 γ, a contradiction.
- Mixed quadruples with a shallow point.
  - Shallow M2a and M1C: excluded above.
  - One or three shallow points: excluded by block_sea Theorem 2.
  - M2c with B and D both fillers. Let b = v2 e, β' = v2 u2 = 1 and c = v2 n1. Since z = −e u2/n1 ≢ 0 (mod 4), c ≥ b.
    - (η,β) pair: b = 2 and v2 Δ = 2. If c = 2, then v2(Δ−n1) ≥ 3, so the left side has valuation 6 and the right side 5. If c ≥ 3, then v2(Δ−n1) = 2 = b, so the left side is ≥ 8 and the right side is 5.
    - (β+,β−) pair: b = 3 and v2 Δ = 3. If c = 3, the valuations are 9 and 7. If c ≥ 4, they are ≥ 11 and 7.
    Both pairs are impossible. A direct search (t10) confirms 0 solutions.
- All-filler quadruples.
  - α = 0 gives a DH, excluded by Theorem 1.
  - If α ≠ 0, then (i) makes a | αβ/16 a finite set, and (ii) fixes c. The residue condition n_C − n_A = (σ + a − c)/2 ≡ r_C − r_A (mod 4) must hold, and positions in a gap are otherwise free. The rows enter only as offsets from ρ, so this is a finite, h-independent enumeration. t7 finds 0 solutions for (0,−8,−24) and for six other offset patterns.
- Rival pairs need opposite parities, but every filler is odd.
- With no parked triples, there is no V3.

4. THEOREM 3. Here α = ±16d, γ = 8ω and β = 8(ω + μ').
- From (i): σ = ∓4d(ω + μ')/a'.
- From (ii): a'^2 − c'^2 = ω^2 − 4d^2. The value c is even because C and D have parity ν.
- (a) μ' = 0 makes a' = ω admissible for every ω, which gives the census's 2 per label.
- (b) d = 1 and μ' = 4. Since c'^2 ≥ 0, |a'| ≥ (ω^2 − 4)^{1/2}, so |a'| ≥ |ω| when |ω| ≥ 3. Also a' must divide ω + 4.
  - For ω ≥ 5, the only such divisor is ω + 4. It gives c'^2 = 8ω + 20, that is (c'/2)^2 = 2ω + 5 ≡ 3 (mod 4), which is impossible.
  - For ω ≤ −5, |ω+4| < |ω| − 1, so there is no divisor.
  - That leaves |ω| ≤ 3, the label rows ρ ± 8 and ρ ± 24.

5. THEOREM 4.
- Write Δy = 2^a·y' and Δn = 2^b·n'. The direction perpendicular to (4Δn, Δy) is (Δy, −4Δn)/G with v2 G = min(a, b+2).
- A deep column needs x-step valuation v2 k + a − min(a, b+2) ≥ 2. The y-step valuation is v2 k + b + 2 − min(a, b+2).
- If a ≤ b+2, then v2 k ≥ 2 and the y-step is even. If a = b+3, then v2 k ≥ 1 and the y-step is even. If a ≥ b+4, an odd k is allowed and the y-step is odd.
- So under (P), every deep point on the line is at an odd row and no even point lies on it. Otherwise even points can lie on it, and W = F' + E − F has even row in a column with an odd black point, which is fatal.
- Corollary. If F and F' have distinct rows of one class mod 16, then (P) forces Δn even. A filler G of the other parity must then have row = y_F and row = y_F', a contradiction.

6. PROPOSITION R.
- Lemma rival: 4j(d+j) = t^2 with t = 4Δn, and j ≤ h − max row ≤ H0.
- For a fixed filler row and j: c' − c + j = 4m^2/j, so at most (j(h+j))^{1/2}/2 + 1 even rows c qualify.
- Each even row belongs to at most one label per class, there are ≤ B(h−1) classes in all, and each label has ≤ 2 partners (Δn = ±m).
- Summing over j ≤ H0 and the 3 filler rows gives the bound.

7. THEOREM 5.
- (a) Both points have parity ν, so δ is even. e is even because both rows are ≡ r1 (mod 16). Then u ≡ v (mod 2) and uv is even, so u and v are even.
  - Even–even: the lattice A3 gives ε ≡ δ (mod 2^ν). If v2 δ = v2 ε = w < ν, then 4δ^2 + ε^2 = 2^{2w}(4δ'^2 + ε'^2) with δ', ε' odd, which is ≡ 5 (mod 8), not a square. So v2 δ, v2 ε ≥ ν.
  - Then L' ≡ 0 (mod 2^ν) and (δ − L'/2)/2 ≡ 0 (mod 2^{ν−2}), which is even.
- (b) δ = 4e + 2^t k and w = v2 e ≤ log2(A/4). Then δ^2 + 4e^2 = 20e^2 + 2^{t+3}ek + 2^{2t}k^2. If t ≥ w + 3, this is 2^{2w+2}·(5e'^2 + 8m), and 5e'^2 + 8m ≡ 5 (mod 8) is not a square.
- (c) The S5 reach is |δ| ≤ e^2 < h^2/64. But ΔM ∈ pZ ∩ 2^t Z gives |ΔM| ≥ p·2^t > 20h^2. So no two blocks can lie within reach, and width ≥ 4·(#blocks)·h^2/64 ≥ (h−1)h^2/16.

8. PROPOSITION 6.
- (a)/(c): an S2 instance is (C, f1 f2 = e'^2) with the hole at slot offset ±(f2 − f1). t9 counts every instance for all labels at h = 10^3, 10^4 and 10^5. The per-label counts are 5.55, 9.92 and 15.41, and the in-block shares are 0.27, 0.22 and 0.19.
- (c): ε = (r0 − y_C)/2 is odd. The offset D − C = (4k(k+1), −(4k+2)) is block_sea Prop 5 with its witnesses in the sea.
- (a): with several classes at one M, Theorem 1 of the rigid note with ΔM = 0 gives c2(10t − T0) = 8tΔs, and the rigid rule gives Δs ≡ 0 (mod 2^ν), so (E;O,E) dies. (E;E,E) reduces to 4d1d2 + a1a2 = 0 with a_k ≡ d_k (mod 2^ν), which is solvable 2-adically with a1 = ±2^{ν+2} and v2 d1 = ν.
- (d): the witnesses (x_C + x_D ∓ 2L)/2 have parity δ − L. With L^2 = δ^2 + ε^2, they are shallow iff ε is odd.

9. LEMMA M. Both witnesses in the gap need u ≥ a_L and v ≥ a_R, so uv ≥ a_L a_R ≥ (m+1)(A+m) > h^2/64 ≥ e^2, which contradicts uv = e^2.

## External results used

- research_archive/2026-11-13/block_sea_classification.md: criterion (V1)-(V5), Theorem 1 (Pa, Pb, Pc, X1, X2), Theorem 2 (M2a, M2c equation, M1C, excluded shallow sets), Prop 4 (one-row family), Prop 5 (forbidden offsets). Audited.
- research_archive/2026-11-13/deep_layer_bh16.md: A1, A2 (re-derived here as Lemma W), A3 (even-label lattice), BH16 rule, S1 to S5. Not audited.
- research_archive/2026-11-13/sea_row3_split.md: Theorem A, Corollary B (i mod 8 split, row-3 sea), hypotheses (H1)-(H4), boundary items 2(ii)-(iv). Not audited.
- research_archive/2026-11-13/rigid_layout_cross_block.md: Theorem 1 (exact (E;O,E) form), Theorem 4(a,e), Theorem 5 / Theorem C (rigid layout, width 320 h^2 B, at most B(h-1) classes). Audited.
- Paper sec2_prelim.tex and sec5_threshold.tex: Lemma mixedeq, Lemma rival, Lemma diff, Prop. partial (placing n labels in width c0 n tau*(h)^2), as quoted in the notes.

## Checks

Scripts are in the script folders of this directory. All ran with py, one at a time, each under 60 s and far under 1 GB. The repository was not touched.
- chk.py: my brute-force checker from the definitions (numba). It finds tilted rectangles with 3 or more black corners (V1, fatal, parked by the parity rule), V3 collisions, mixed quadruples via the Lemma mixedeq sum/length index, and rival pairs.
- t0_validate.py: Sea(1,r) is clean for h = 12 and 17 and every r > (h+1)/2. The block_sea X2 example E=(21,1), V=(16,9), G=(24,14), W=(29,6) is found exactly. BH16 at h=57 shows S2 (Mh:FF/FLo) 3, 3 and 2 for three offsets, which matches the note.
- t1_fillerquads.py: Q4 has no all-filler tilted quadruple for any of the 24 permutations. A first version omitted the residue condition on n_C; t2 caught the error and the version reported here is corrected.
- t2_puregap.py: the pure Q4 gap at h=131 is clean.
- t3_block.py: Q4 with one block at h=131 has 50 to 65 F;F,Le per block of 6 to 8 labels, plus rival pairs and top-label families. No horizontal M2a.
- t4_bh16m4.py: BH16m4 shows FF/FLo 2 per label at h = 57 and 131, which reproduces the reported failure.
- t5_variants.py and t8_top.py: U3 variants at h = 99, 115, 131, 139, 147, 155 and 163, for ι8 = 0, 1, 2 and 3. No horizontal M2a (S2) appears in any U3 run. BH16 shows S2 at about 1.6 to 1.8 per label. U3top at h=139 with ρ = h shows only rival pairs 6 and FLe/FLe 1 (17 labels). The ι8=2 FF/FLo hits all involve the label at row ρ+8, as Theorem 3(b) predicts.
- t7_fillerquads_gen.py: 0 all-filler tilted quadruples for U3 offsets (8,24,0), (24,8,0) and six others.
- t9_s2zone.py: exact S2 count and share of instances with the hole inside the block, at h = 10^3 to 10^5.
- t10_m2c_filler.py: direct search of the M2c equation with two U3 fillers, h ∈ {131,139,155,163}, |Δn| ≤ 400, 1.7·10^8 cases. 0 hits.

## Gaps

- Nothing here is independently audited. Theorem 1, Theorem 3, the valuation parts of Theorem 2, Theorem 4 and Theorem 5 were each checked once by me and sanity-checked by brute force at h <= 163.
- For r0 = 3, Theorem 2 relies on sea_row3 Theorem A and its shift-invariance claim. Neither is audited.
- Tilted-side mixed quadruples that contain labels are classified only for the role assignment (base, base | hole, label) (Theorem 3). Other assignments are known only from the census (single-block windows, h = 99 to 163).
- Families left in U3 regions are not bounded. The h=155 census with top labels removed, four region types (19 to 27 labels each) found: S3 (Lo;F,Le) 0 to 3, V4 Fo/Fo (FLo/FLo) 0 to 4, M2c label-filler (LoS/FS) 0 to 8, FLe/FLe 1, F;Le,Lo 1 to 2, rival pairs 12 to 22. BH16 at the same h has S2 (36 to 41) plus FLo/FLo 8 to 9 and LoS/FS up to 6. So U3 is not worse on the shared families, but none of them is bounded. Parked triples and V3 in label zones are not analysed.
- The rival-pair bound O(B h^{3/2}) is rigorous, but its constant is large: at h <= 163 rival pairs are the most numerous family, about 0.6 to 1.1 per label.
- S5 is not removed. Theorem 5 shows U3 cannot remove it and the full 2-adic kill is cubic. Its load stays the heuristic of deep_layer_bh16. The census windows have one block, so S5 is not measured.
- Not analysed: junctions of U3 regions with the Sea(1,g) and Sea(3,g) buffers, region boundaries, and placement of the top labels and rival-pair labels by Prop. partial.
- The all-filler finite check (t7) assumes free positions in a long gap. It is exact for the conditions derived from Lemma mixedeq, but the derivation itself was checked only by me and by the zero-hit brute force on pure gaps.
- Proposition 6 interleaving (option a): (E;E,E) right angles in multi-class blocks are shown admissible 2-adically, but I neither found nor excluded actual instances.

## Missing estimate

S2 is gone. What blocks a full deep layer now is S5 together with the shared families (S3, S4 and V3). Under U3, every S5 pair has both witnesses in label-parity non-label columns ("holes") near the two labels. One structural lever is proved: hole rows may be chosen freely, column by column, from {ρ, ρ−16} without breaking Theorem 1 or (P).
- Label–hole pairs keep e odd for both rows.
- Hole–hole pairs have e = ±2, and uv = 4 with u ≠ v forces δ = ±3, which is odd, but holes are at even distance.
- Hole–base pairs have e odd and δ odd, so they are not Pythagorean.
- The (λ,β) witness classes stay distinct mod 16.
So S5 becomes a 2-colouring problem. Its constraint graph has hole columns as vertices and one edge per S5 witness pair. Its average degree is heuristically about 10^-4 log^2 h per label. What is missing:
- (i) A bound showing that the components with odd cycles involve O(h^{2-δ}) labels, which the RELOCATION RULE then absorbs.
- (ii) A classification of the local filler triples that free hole rows create. Examples: V a hole with two holes of the other row at offsets Δn1·Δn2 = −16, fourth corner in row ρ−32; or legs (hole–hole, hole–base) with Δn1 ≡ 0 (mod 8). These are parked triples, or fatal when the fourth corner falls in a label column, and they must be kept away from V3 collisions.
- (iii) Bounds for S3 and S4 in U3 regions.
With (i)-(iii) and chi(Gamma) < infinity, the width would be 320 h^2 B + O(h^2), which gives m_h = O(h^2) conditionally.

## Next steps

- Audit Lemma W, Theorem 1 (seven cases), Theorem 3 and the valuation parts of Theorem 2. Each is short. If they pass, add a ledger row: uniform U3 filler rule removes every horizontal M2a with a filler, i.e. S2 in all forms and at every distance, with no zone/gap junction.
- Correct deep_layer_bh16.md and sea_row3_split.md: BH16m4 fails only through the midpoint coincidence rho = (R+ + R-)/2 (Theorem 3). It is not a dead end. Record that hole-only repairs, options (a) and (c), miss 73 to 81 percent of S2.
- Implement free hole rows {rho, rho-16} with a greedy 2-colouring against S5 witness pairs. Test on a two-block window with a reduced prime p (h about 150), scored by chk.py, and count the new local filler triples.
- Classify S3 and S4 (V4 Fo/Fo, M2c label-filler) under U3top with exact equations. Rerun the census at h about 200 to 260 with top labels removed to see whether their per-label rates fall.
- Test U3 regions next to the Sea(1,g) and Sea(3,g) buffers, and place top labels and rival-pair labels by Prop. partial.
- Record Theorem 5(c) as a no-go: killing S5 through block congruences mod 2^t, 2^t >= 2A, costs Theta(h^3). A bounded t only rescales the load.

