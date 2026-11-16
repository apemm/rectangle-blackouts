# What carries over to the ladder layer

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: most SAW* results carry over to the ladder layer, but it fails at the buffer seams and through thick V3 collisions between FFo triples; repairs are partial. The consolidated board does not use the ladder layer. Not audited yet.

# Result

## Status

partial

## Summary

The ladder layer mostly carries over. I proved most of (a) and (b), and the strip theorem settles all-class-slot four-filler quadruples for every E'. LAD as specified fails in two places, each checked from the definitions: seam mixed quadruples at the Sea(r0,g) buffer, and thick V3 collisions between FFo triples inside one class. A per-type T* shift fixes the seams for E' <= 3, and the class split i mod 1024 removes the FFo collisions whose fillers are non-class.

## Statements

Setting. LAD_6(E') as in ladder_layer.md Thm 4, with a random class phase psi (4 | psi) added. Units: X = slot rel = n - rho0, eta = depth, filler row = T* - 8 eta(X), metric X^2 + 4 eta^2, which is similar to the true metric. Assumption (H-slot): every label of a region sits at X = 0 mod 64, so region types fix s mod 64. This is a constant cost, 4 times R1. Exact form, checked: eta = (X+1) mod 4 for odd X; eta = X - 1 mod 16 for X = 2 mod 4; eta = 3 + (X mod 2^{v2(X)+3}) for X = 0 mod 4 and v2(X) <= 5; class slots (X = 0 mod 64) have eta = 3 + 64((X/64 + psi) mod 2^{E'}). Changing psi is a translation by 64 psi, so pure-gap statements do not depend on psi. Staircase checked exhaustively for E' <= 3.

A. PURE GAP (part a).
A1 (proved). The pure LAD gap with its row-1 or row-3 sea has: no corner triple with 3 or more black corners (no FFF; no Pa, Pb, Pc, X1, X2 with two fillers); hence no parked triple and no V3; no M2a, no M1C, no rival pair; and no M2c with two fillers.
A2 (proved, structure lemma). Every four-filler mixed quadruple (A,B side; C,D diagonal) has the following properties:
- e = eta_B - eta_A != 0;
- with c1 = C - A = (d1, al) and c2 = D - B = (d2, be): al != 0, be != 0, al + be != 0;
- v2 of every coordinate of B-A, C-A, D-B and D-C equals one common r;
- A = D and B = C (mod 2^{r+1});
- |G| <= 4|e||al+be|, and G divides 4e(al+be).
So the class points of a quadruple are all four points, or a nonempty subset of {A,D} or of {B,C}. Several class points can occur only if they all lie in {A,D} or all in {B,C}.
A3 (strip theorem, proved for every n >= 1). The set {(X, X mod 2^n)} has no four-point mixed quadruple. Hence no LAD four-filler quadruple lies entirely in class slots, for any E'.
A4 (exhaustive computation, a finite proof). There are no four-filler quadruples without class points, for every E'. There are no mixed class/non-class quadruples for E' <= 6 (h < about 1.7e9). For larger E' the mixed case is open.

B. ONE-LABEL FAMILIES (part b).
B1 Rival pairs (proved). Non-class filler rows contribute at most C h^{3/2} labels, deterministically. Class rows: the expectation over psi is at most 155 h^{11/6}. Labels whose even row lies within D_max = 512·2^{E'} + 87 = O(h^{1/3}) rows of h number O(h^{4/3}).
B2 Label-filler M2c (proved). Lemma (ii-a) carries over verbatim. Theorem A of point_counts applies to each filler row, which gives O(h^{9/5+eps}) labels from the 22 non-class rows. The class rows give O(h^{9/5+eps}) in expectation over psi. Summed deterministically over the class rows they would give h^{2+2/15}, which is too large.
B3 Feo (proved). The SAW* kill carries over: hole rows have v2(y - y_P) = 3, and the base rows and the T* rule are unchanged.
B4 One label, three fillers.
- Label on the side: labels with depth at most 2H + O(1) are near-band, O(h^{4/3}) labels.
- Label on the diagonal: the family is thick (linear in the label depth) iff k^2 + 4 rho^2 = 4e^2, with k = S and rho = 2eta_D - eta_A - eta_B (proved). T1 is rho = 0.
- Exhaustive computation: no thick family with non-class fillers for any E'; no thick family at all for E' <= 2.
- Non-thick, non-class: O(h^{3/2}) labels (proved).
- Cutoff for |k| > 2|e|: labels with depth up to about 4H^2; this is O(h^{5/3}) labels.
- Class-involving, non-thick: OPEN.

C. SEAMS (part c).
- J1 (a), (b), (c) hold for LAD (proved).
- J1 (d) FAILS: there are seam mixed quadruples with one row-g point on each pair (explicit instance below). For some t0 = T* - g, no end phase avoids them.
- J1 (e): bad rival pairs now reach kap = 27, and four (h - g, h - T*) cases cannot be avoided by any phase.
- REPAIR (computation, E' <= 3): per type, lower T* by 64k with k <= 4, and choose the end phases. This makes (d) and (e) clean at both ends for every case of (h - g, h - T*). The T* shift keeps the SAW* rule mod 64. General E' is open.

D. V3 AND TWO-LABEL FAMILIES (part d).
- These kills carry over (proved): FFe, Fee, Feo, Foo (both vertex types, with R1), LLL, FFF, Pc with a filler vertex, and the FFo label-vertex case. Pb now needs labels with 2i+1 <= D_max + 65 relocated, O(h^{4/3}) labels.
- FFo triples (vertex a hole at X_L - X_V = 4 mod 8) stay parked: W is never in a label column and never fully black (proved).
- BUT V3 between FFo triples of one class FAILS: explicit instance below; 26 colliding W at h = 4001 and 93 at h = 6001 per class.
- REPAIR (proved for non-class F2): split classes by i mod 1024 (cost 16 times). This removes every same-class collision in which both F2 fillers are non-class.
- OPEN: cross-class FFo collisions, collisions with class-row F2, SLF-Pc pairs whose holes differ by 128 rows (census: 0), and inhomogeneous two-label quadruples (N_e-type counts).

## Proofs

0. NOTATION. A filler pair has vector (g, k) in (X, eta). Staircase: k = 0 with v2(g) >= 2, or v2(k) = v2(g). So N(g,k) = g^2 + 4k^2 = 4^t·(1 mod 8) when k = 0, and 4^t·(5 mod 8) when k != 0, with t = v2(g). Hole rows minus odd label rows have v2 = 3. Base rows are T*-16 and T*, unchanged, with v2(base - label) in {4,5}. All filler rows are r1 (mod 8).

A1.
- Filler right angle: 16 g1 g2 + dy1 dy2 = 0. If dy1 dy2 != 0, the valuations are 4 + v2 g1 + v2 g2 against 6 + v2 g1 + v2 g2. If some dy = 0, then g1 g2 = 0.
- Pc: 4 a gamma = f g with v2(f) = 1 and v2(g) = 3 + v2(gamma), so v2(a) = 2. X1 needs a row = 5 (mod 8); X2 needs y_V = 1 (mod 4); Pa needs even rows; Pb puts W above the grid. Row-3 types work the same way under (H1)-(H3).
- M2a never occurs for rows that agree mod 8. M1C needs even rows. Rival pairs need mixed parity.
- M2c with two fillers: staircase gives v2(e) = v2(Delta) = b >= 2, v2(u2) = 1 and c = v2(n1) in {b, b+1}. The left side has order 3b or 3b+2; the right side has order 2b+1. They cannot match.

A2.
- e = 0: then G S = 0, so S = 0. Then N(w) = G^2 forces the D-C pair to be horizontal, and w = +-u or degenerate.
- With u = (G, e) and sigma = c1 + c2 = (S, s): u·sigma = 0 and |u + c2 - c1| = |u|. These are equivalent to u·c1 = Q/4 = -u·c2, with Q = |c1 - c2|^2.
- Cramer's rule gives G = Q s/(4 Delta) and e = -Q S/(16 Delta), with Delta = d1 be - d2 al. Also s = 0 forces c2 = -c1, so n = 0.
- From G S = -4 e s and v2(G) = v2(e): v2(S) = v2(s) + 2. Then the staircase on c1 and c2 forces v2(d1) = v2(d2) = r.
- With u = 2^t u' and w = 2^t w' (odd coordinates), Q/4 = 4^t N(z) where z = (u' - w')/2. Comparing v2(u·c1) = t + r gives r = t + v2(N z) >= t.
- If al = 0: d1 + d2 = 4·odd, so v2(Q) = 2r + 3 and v2(G) = r + 1 > r, which contradicts r >= t. So al, be != 0, and t = r.
- The other pairs, B - C = u - c1 and D - A = u + c2, have both coordinates divisible by 2^{r+1}.
- |G| <= |K| follows from G(d1 + d2) = K := -4e(al + be) with d1 + d2 != 0.
- A class point has v2(X) >= 6. If r <= 5 and A is a class point, then v2(X_B) = v2(X_C) = r < 6 and v2(X_D) >= r+1. If r >= 6, all four points are class points.

A3 (strip; points (X, k) with k = X mod N, N = 2^n). Every difference has dk = dX (mod N) and |dk| < N.
- By A2 (the strip is a staircase layer), s = S (mod N) and v2(S) = v2(s) + 2. So v2(s) >= n, and since 0 < |s| < 2N, s = +-N. Use the point reflection (X,k) -> (N-1-X, N-1-k) to take s = N.
- Then al, be lie in (0, N). Also S = 2^{n+2}·odd, |G| <= |e| < N, and -e/G = S/(4N) is an odd integer. So e = G, or e = G - N (when G > 0, with G | N), or e = G + N (when G < 0).
- Integrality of al = d1 (mod N) gives V - U = N (mod 2N). Here tau = (U, V) = c1 - c2 satisfies |tau - u| = |u|; put U' = U - G and V' = V - e.
- Case e = G. Cauchy-Schwarz gives |V' - U'| <= 2.5|G| < 2.5N, so U' - V' = +-N. Then (5G - X)(5G + X) = 4N^2, so |G| = (4^m + 1)/5 · 2^r with 2^m > |G|/2^r. This forces m = 1 and G = +-N/2. Then tau is (2G, 0) or (0, 2G). The first violates 0 <= k_A < N together with k_B < al. The second gives |V| = N.
- Case e = G -+ N. The vertical bounds k_B >= 0, k_C < N and k_B < al give |V'| < |G| <= N/2. Also V' - U' = 0 (mod 2N), so U' - V' is 0 or +-2N. U' = V' gives 5V'^2 = G^2 + 4e^2 >= 5G^2, a contradiction. U' = V' +- 2N needs N <= |G|, a contradiction.

A4. quad4.py enumerates (eta_A, eta_B, eta_C, eta_D), the divisors G of K, and both roots U of (G - U)^2 = G^2 + 4V(2e - V), then every A residue. It was validated against a definition-level O(W^4) brute force on three random toy layers (44/44, 36/36 and 56/56 placements). Results: 0 for E' = 0..5. quad4mix.py, which searches only the mixed class patterns, gives 0 for E' = 4, 5 and 6. Non-class rows do not depend on E', so the E' = 0 run covers every E'.

B1. Lemma rival with E below F gives j <= D_F, j(d + j) = 4 Delta^2 and j | 4Delta^2, so there are at most sqrt(h + j) + 1 values of d for each (row, j).
- Non-class rows: sum over the 22 rows with D_F <= 1943. This gives C h^{3/2}.
- Class row k: the filler at slot X_E +- Delta must be a class slot in row k. That is one residue of psi mod 2^{E'}. It is the same condition for all the at most h/2 labels with that even row, because the A3 lattice fixes n_E mod 2^nu.
- So E_psi <= 8·2^{-E'}·(h/2)·sqrt(2h)·sum_k D_k, with sum_k D_k ~ 256·4^{E'} and 2^{E'} <= 0.107 h^{1/3}.
- E above F lies in the near-band.

B2.
- (ii-a) uses only b, c and v2(u2) = 1.
- For label B and class row k, e is fixed. There are h^{o(1)} witnesses and at most 4 slots per witness. The class slot needs 64 | delta and the right psi residue.

B4.
- Label on the side: q = B + n has depth eta_B + s/2 < 0 once lambda > 2H + 16.
- Label on the diagonal: put m = 4e^2/k^2. Then w_x^2 = A2 lam^2 + A1 lam + A0, with discriminant A1^2 - 4A2A0 = 64[m(c_s + eta_D)^2 - (m - 1)e^2]. This vanishes, with m - 1 a square, iff k^2 + 4 rho^2 = 4e^2.
- onelabel_thick2.py tests every such family over a full period in lam. Positive control: the triangle wave gives 8 T1 families; SAW gives 0. Result: 0 hits among 1344, 1568 and 1896 candidate families for E' = 0, 1 and 2.
- When m - 1 is not a square, the equation is a Pell-type equation. When it is a square but the form is not a perfect square, the equation factors. Either way there are O(sqrt h) admissible depths per tuple.

C.
- (b) V and one end LAD, the other end in row g: v2(16 a1 a2) = 4 + v2 a1 + v2 a2, against v2(e1 e2) = 3 + v2 a2.
- (d) Write a = Q1 - P1, c = Q2 - P2 and s2 - s1 = 8m, sig1 = s1 - g. The conditions are a^2 - c^2 = m(sig1 + 4m) and a(a - c + 2 Dl) = -m sig1/2. The valuation argument leaves v2 a = v2 c consistent. This is complete enumeration over the divisors of m(sig1 + 4m): seam.py, seam_phase.py and seam_repair.py.
- (e) j(|g - c| + j) = 4 kap^2 with j <= h - max(g, c). The (h - g, h - T*) cases (1,48), (3,32), (3,48) and (3,50) are unavoidable because base rows recur every 4 slots.

D.
- FFo: alpha·beta = -4 e1 e2 with e1 odd forces V to be an offset-0 hole with v2(alpha) = 2. W is in a label column only if 64 | beta, which needs v2(e2) >= 6. Rows at X = 4 (mod 8) differ by 8, 16 or 24, so this is impossible. So the triples stay parked.
- A collision W1 = W2 inside one class forces i2 - i1 = -4(e21 - e22) = 0 (mod 64) and beta1 - beta2 = -4(e21 - e22).
- For non-class F2, e2 lies in [-31, 220], so |i2 - i1| <= 1004 < 1024.
- Theorem B's other items use only the mod-4 offsets of hole rows and the v2 relations to labels, which LAD keeps.

INSTANCES (checked by hand from Lemma mixedeq and by assert).
(i) Seam, t0 = T* - g = -51. LAD points S1 = (0, T*-24) and S2 = (96, T*-216); row-g points G1 = (300, g) and G2 = (252, g), true coordinates. Side {G1, S1}, diagonal {G2, S2}. |u|^2 = |D - C|^2 = 95625, n = (24, -96), n·u = 0, p = (324, g-96), q = (24, T*-120).
(ii) FFo V3, h = 4001, row-1 type, iota = 5, T* = 3963, E' = 0 (T* follows the SAW* rule). Triple 1: L1 = (0, 11), V1 = (-48, 3779), F21 = (10000, 3907). Triple 2: L2 = (512, 267), V2 = (560, 3843), F22 = (10096, 3715). Both right angles are exact (482304 - 482304 and -457728 + 457728). Both rectangles meet at W = (10048, 139). W's column holds a filler in row 3299, so both rectangles are parked at W.

## External results used

- Repository inputs: ladder_layer.md (LAD definition, Theorem 4), deep_layer_sawtooth.md and its audit, saw_residual_families.md (ii-a, ii-b, iii) and its audit, v3_and_cross_block.md (Theorems A, B, C, Proposition D), full_layout_junctions.md (J1, P9) and its audit, block_sea_classification.md (criterion V1-V5, Theorems 1 and 2), point_counts_power_saving.md Theorem A (unaudited), paper Lemmas mixedeq and rival.
- Standard facts only: divisor bound tau(n) = n^{o(1)}; the Pell/factorization dichotomy for X^2 - D Y^2 = N; the Cauchy-Schwarz inequality.

## Checks

Scripts, all in scripts_ladder_carry/. Each ran with py, one at a time, under 60 s and under 1 GB.
- lad.py: the LAD eta(X) definition.
- stair.py: staircase check, 0 violations for E' = 0..3.
- quad4.py: reduced four-filler search. Validated against a definition-level brute force on toy layers (44/44, 36/36, 56/56). LAD gives 0 for E' = 0..5.
- strip.py: 0 for N = 4..64, consistent with A3.
- quad4mix.py: 0 mixed quadruples for E' = 4, 5, 6.
- onelabel_thick2.py with onelabel_thick_core.py and onelabel_thick_toy.py: the triangle-wave control gives 8 T1 families and SAW gives 0. LAD gives 0 hits for E' = 0, 1, 2; E' = 3 timed out.
- seam.py, seam_phase.py, seam_repair.py: seam (d) shapes per t0, the phase sets, and the repair. Every (h - g, h - T*) case is repaired with a T* shift of at most 4 for E' = 0..3. One (d) instance was verified by hand.
- slf_v3.py: 0 same-class SLF-Pc collisions at h = 4001, 8001, 16001 and 20001.
- ffo_v3.py: FFo/FFo collisions, 26 at h = 4001 (iota = 5, T* = 3963) and 93 at h = 6001. The instance was verified by hand.
The repository was only read; no git commands were run.

## Gaps

- Mixed class/non-class four-filler quadruples are excluded only for E' <= 6 (exhaustive). The general E' case is open; for E' >= 7 the search exceeds the memory limit.
- Seam repair (T* shifts by up to 4·64 rows plus end phases) is verified only for E' <= 3. Class rows near the seam (kap up to about 0.9 sqrt(D_max)) are unchecked for larger E'.
- FFo/FFo V3: same-class collisions with class-row F2, cross-class collisions (they need a first-moment count over p, as for family (d)), and same-label double triples are not bounded. Without a fix this family is thick: 26 colliding W at h = 4001 and 93 at h = 6001 per class.
- SLF-Pc V3 between holes whose rows differ by 128 (phi differing by 4, i differing by 64) is new under LAD. The census at h = 4001 to 20001 found 0; there is no proof.
- One label with three fillers, class-involving, non-thick: the psi average does not obviously bound it, because several class points have linked rows. Thick families with class rows are excluded only for E' <= 2.
- Inhomogeneous two-label quadruples (fillers in different rows) and the cross-block two-label families under LAD: not done. They remain the N_e / Proposition 5 counts.
- Class-row bounds for B1 and B2 hold only in expectation over a new random class phase psi. psi must be chosen jointly with p (Markov over all first-moment families). Assumption (H-slot) needs s fixed mod 64 per region type.
- The near-band cutoff for |k| > 2|e| in B4 is about 32 H^2 rows. That is O(h) labels for non-class rows but O(h^{5/3}) labels for class rows, and the constants are huge.
- Nothing here is audited. The four-filler, thick-family and seam conclusions for small E' rest on my own finite computations; quad4.py was validated against a definition-level brute force, and onelabel_thick2.py against a positive control.

## Missing estimate

Three bounds would complete the LAD route with the two repairs (T* shifts, i mod 1024).
(1) A general-E' proof that there is no mixed class/non-class four-filler quadruple (class points in {A,D}, r <= 5). The congruence available for the non-class pairs is only mod 2^{r+3}, so the strip method does not extend directly.
(2) Bounds of O(h^{2-delta}) labels for: FFo/FFo V3 with class-row F2 or across classes; SLF-Pc V3 across hole rows; and the class-involving one-label three-filler family. Each is a W-collision or square condition with two divisor coincidences.
(3) The inhomogeneous count N_e(h) <= h^{2-delta}, as in ladder_layer.md (2) and v3_and_cross_block.md (F3).

## Next steps

- Audit A2 (structure lemma) and A3 (strip theorem) first. They are short valuation and size arguments, they settle every all-class quadruple for every E', and they record that e != 0, al, be != 0 and that the class points must lie in {A,D} or {B,C}.
- Decide the FFo/FFo fix. Option 1: i mod 1024 (proved for non-class F2) plus a first-moment bound over p for cross-class collisions, as in family (d). Option 2: redesign the tau-odd sub-ladder so that e21 - e22 = 0 (mod 16) cannot occur together with row-matching F2. Then rerun ffo_v3.py at h = 4001 and 6001 with the chosen split.
- Prove the seam repair for general E' by placing the last 2^{E'+6} slots before each buffer in phase with psi, so that no class slot lies within reach of the seam. Rerun seam_repair.py for E' = 4 with a lighter divisor routine.
- Attack the mixed four-filler case for general E' by fixing the non-class pair (B, C) mod 2^{r+3} and showing that the class depths of A and D must be bounded by C(H_nc). Then the E' <= 6 computation finishes it.
- Run slf_v3.py and ffo_v3.py across classes, with two classes at spacing p > 20h, to measure the cross-class V3 families under LAD.

