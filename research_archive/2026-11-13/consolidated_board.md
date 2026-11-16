# One consolidated board for the near goal

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: the board L*** (SAW* with a T* shift, modulus 16 l, 512 region types, random subclass split) gives m_h <= C h^2 (log h)^1.5 (loglog h)^C, conditional on the open lemmas and audits listed in its Gaps. New: SAW* breaks the audited seam phase rule, and a T* shift repairs it; hypothesis (FF) holds in the form needed; three labels plus one filler is a family no earlier note listed. Not audited yet.

# Result

## Status

partial

## Summary

I wrote one consolidated board, L***. It combines SAW* (with a new per-type T* shift), the random modulus 16l, 512 region types (i mod 32, s mod 16), and Theorem IV's random split, with hypothesis (FF) now proved. Under (AP), five open counting lemmas and the owed audits, it gives m_h <= C h^2 (log h)^1.5 (loglog h)^C, i.e. c = 1/2. Two new findings: SAW* breaks the audited seam phase rule (kappa = 4 and 6 rival pairs), which a T* shift by 64 or 128 repairs, and the family '3 labels + 1 filler' is in no note's list.

## Statements

BOARD L*** (specification). h >= h0, Lambda = log h, ell = loglog h, B = ceil(Lambda^(3/2)), stride 4 only. A = ceil(h/2), K = floor(h/2), W_h as in the paper. Label (i,j): odd row 2i+1, even row 2j+2, s = j - i, T = 2s+1.
(B1) Heavy diagonals: kappa_T = k_T^(2) >= B. They go to Theorem E blocks (t1_cost_decomposition, audited), right of the switch z, with row-h tails.
(B2) Primes, chosen jointly as the last step: l prime in (1.04h, 2.08h] with l = +-2 (mod 5); p prime in (40h, 80h] with p = 3 or 7 (mod 20). (The range of p is doubled from L**; this is needed in K4.)
(B3) Region types tau = (iota = i mod 32, sigma = s mod 16), 512 of them. r0 = 1 if iota is odd, r0 = 3 if iota is even. Then y_P = 2iota+1 (mod 64) and T = 2sigma+1 (mod 32) are constant per type.
(B4) Classes on a light diagonal T:
 - a greedy G_T colouring, c_T <= kappa_T + 1 <= B classes;
 - each class restricted to the types;
 - each (T,type) class split into K_T = floor(B/c_T) subclasses by iid uniform colours psi_T, independent across T.
 Hence at most B classes per (T, tau).
(B5) Placement (rule of L*_l): class c sits at columns 4(i + p t_c) + 4b_tau, with t_c = p^(-1)(s_c - kappa) (mod 16l). The k-th class of a diagonal is at rho_s + 16lk.
(B6) Filler layer SAW*-shift.
 - T*_tau = T0_tau - 64k_tau, where T0_tau is the largest y <= h with y = y_P + 32 (T = 3 mod 4) or y_P + 48 (T = 1 mod 4) (mod 64).
 - k_tau in {0,1,2} comes from Table J1* (below).
 - The deep column 4n of a non-label slot gets row T*_tau - 24 + 8((n - rho0) mod 4). Shallow columns x != 0 (mod 4) get (x, r0).
(B7) Proposition partial (one instance: case (a) for even h, case (c) for odd h) receives:
 - i = 0;
 - in row-3 types, i = 2 or j in {0,1};
 - every label with an endpoint row >= T*_tau - 320 (near band);
 - every label with 2i+1 <= 300 (R2');
 - T1-exceptional labels, and SAW Theorem 1(6) labels;
 - labels on large-height edges: R_IV with max(p_lambda, q_lambda) > h^(1/2), and R_FF with |U'| > h^(1/2);
 - the labels of the small families (table rows D9, D10, B7, A4, D20);
 - the J3-Bad sets of the open families (hypothesis Q).
(B8) Theorem D blocks (polylog_relocation_diluted, weighted form) receive Bad_split: in each final subclass, the shallow end of every monochromatic small-height edge of R_IV (its q-end), of R_FF^oo and R_FF^ee (its depth-|U'| end, in each of the 4 filler rows), and of the bounded-range graph R_FF^+. The blocks are grouped by c_T in dyadic ranges, right of z, with row-h tails.
(B9) Buffers and ends:
 - L** (P7)-(P8) with g(h) = h (h even), h-1 (h = 1 mod 4), h-3 (h = 3 mod 4);
 - pure SAW*-shift margins of 2W_h + 1 columns plus at most 3 slots;
 - end phases from Table J1*.
(B10) One switch z, J5 gluing, truncation to columns 1..m.
Order of choices: classes, then psi (Theorem D's event, probability >= 1/2), then (l,p) by Markov applied to the sum of all first-moment families.

TABLE J1*. Let D0 = h - T0_tau in [0,63]. Each bad pair below is (o, kappa, j) = (filler offset, slot distance, Lemma rival j).
 - h even, and h = 1 (mod 4) row-1 types: k = 0, no bad pair.
 - h = 1 (mod 4), row-3 types: (1,2,1) at D0 = 0, (3,1,1) at 4, (2,2,1) at 8, (0,3,1) at 12, (3,2,1) at 16, (1,3,1) at 20, (2,3,1) at 28, (3,3,1) at 36. At D0 = 40 and 48, k = 1; at D0 = 56, k = 2.
 - h = 3 (mod 4), row-1 types: (2,3,3) at D0 = 4 and (3,3,3) at D0 = 12; k = 1 at D0 = 24, 32, 40, 48.
 - h = 3 (mod 4), row-3 types: the first list shifted by 2 (D0 = 2, 6, ..., 38); k = 1 at D0 = 42 and 50; k = 2 at D0 = 58.
 - Every k = 0 row has a clean right and left phase. The (Phi) of L** applies, and the D0 <= 14 rows reproduce the audited (P9) exactly. Every shifted row has no bad pair, so any phase is clean.

THEOREM N (near goal; CONDITIONAL). Assume:
 - (AP) of polylog_relocation_diluted (Henriot AP form, q <= h^(1/2));
 - the open counting lemmas Q1 to Q5 (Gaps);
 - the audits U1 to U8 (Gaps) all pass.
Then for every m >= M, L*** truncated to columns 1..m is a valid blackout with m + q_h points, and
 M <= C h^2 (B + Lambda^(E(a)+1) B^(-a) + Lambda^3/B) ell^C1 + c0 n_rel tau*(h)^2 + C h^2,
with E(a) = (1+3^a)/2, a = 0.91, n_rel = O(h^(11/6+o(1))). Hence m_h <= C h^2 (log h)^(3/2) (loglog h)^C1, that is (log h)^(2-c) with c = 1/2. This beats T1.
If, in addition, the sum over light T of c_T is O(h), the exponent returns to 1.4967.
NOT PROVED: any of Q1 to Q5, (AP), or m_h = O(h^2).

## Proofs

The notes are cited by name; all are in research_archive/2026-11-13. "Here" marks a step that is new in this note.

1. NEW LEMMAS

LEMMA J1* (SAW*-shift | Sea(r0,g) seam; proved here, audit owed).
 - Cases (a) to (d) of J1 carry over word for word. They use only four facts: the filler rows are T* - 24 + 8o, which are r1 (mod 8); the deep-pair row differences are 8m with m = slot difference (mod 4) and |m| <= 3; g is even with g > (h+1)/2 and 2g - 3 > h; and T* - 24 > 5. The shift by 64k changes none of these.
 - Case (e), rival pairs, by Lemma rival. Take a filler in row c and a row-g point kappa slots away. A rival pair needs some j >= 1 with j <= h - max(c,g) and j(|g-c| + j) = 4kappa^2. Here h - g is 0, 1 or 3, so j <= 3.
 - With T* >= h - 63 (SAW*), the values h - c run up to 87. This allows h - c = 64 (j = 1, g = h-1), h - c = 66 (j = 1, g = h-3) and h - c = 48 (j = 3, g = h-3), that is kappa = 4 or 6.
 - Four consecutive slots meet every offset, so no end phase avoids a kappa >= 4 pair. So J1 and (P9), proved and audited for SAW (h - T* <= 14), FAIL for SAW* at 10 of the 64 cases (h mod 4, sea row, D0).
 - The condition depends only on (h mod 4, sea row, D = D0 + 64k), because j <= 3. seam_shift.py checked it exhaustively for D0 in [0,63] and k in 0..3, and gives Table J1*.
 - The closed form was asserted equal to a direct geometric search (the rectangle with diagonal CD, its vertical other diagonal with lattice ends of different parity in rows 1..h) in every case.
 - The k = 0, D0 <= 14 rows reproduce the audited (P9) table entry for entry.
 - The shift lowers T* by at most 128, so T*_tau >= h - 186 and every filler row is >= h - 210.

LEMMA L-adic (16l versions of two steps of v3_and_cross_block; proved here). In L*_l, Dn = n(c') - n(c) is in 16lZ, and |Dn| >= |DM| - |Ds| > 39h across classes (p > 40h).
 - (i) Theorem A(ii), both-even Pc. The vertex V and the end G are even label points, and E - V = (a, -f) with f odd. The right angle gives 2(Dj - Dn)a = f Dj.
   - Same class: Dn = 0, so 2a = f, against f odd.
   - Different classes, reduced mod l: 0 < |Dj| < l, so 2a = f (mod l). Also |a| <= hK/(2(39h-K)) < h/70, so |2a - f| < 1.04h < l. Hence 2a = f exactly, against f odd.
 - (ii) Theorem B, Fee with an even-label vertex. 8 alpha delta = -d eta, with d odd and delta = eta - Dn.
   - Same class: 8 alpha = -d, impossible.
   - Different classes: 8 alpha = -d (mod l) with |8 alpha + d| < l, impossible.
 Every other step of v3_and_cross_block uses M_c - M_c' = 0 (mod 16), which the rule mod 16l gives under R1, or mod p only.

LEMMA FF' (hypothesis (FF) of Theorem IV holds, in the form it needs; proved here from additive_class_split Lemmas 1, 2 and the method of 4(b)). For every eps < 1/3, the sum over coprime (a,b) with b > 0 and U != 0 of |U(a,b)|^(-1+eps) is finite.
 - Put k = a - 4b. Then U = k(17(b + 4k/17)^2 + k^2/17).
 - For fixed k, the sum over b is at most 2 max + integral <= C|k|^(-1+2eps), multiplied by |k|^(-1+eps). Summing C|k|^(-2+3eps) over k converges.
 - By Lemma 2, gcd(U,V) divides 40, so |U'| >= |U|/40. With tau(n)^C << n^eps, kappa_FF := the sum over shapes of tau(|U'|)^C/|U'| is finite.
 - Lemma 1 says the shallow label of a homogeneous Fo/Fo or Fe/Fe quadruple has depth mu|U'|, and that this depth fixes the deeper label. So it suffices to relocate the shallow end, and the weight needs only |U'|.
 - The depth delta_o(i) = Y_o - (2i+1) (or minus T for even depths) is affine in i on one diagonal. So '|U'| divides delta' is a union of at most 2 residue classes of i: exactly the form (AP) asks for.
 - Tail: the sum over |U| > Y of 1/|U| << Y^(-1/3), and there are O(X^(2/3)) shapes with |U| <= X. So the labels on shapes with |U'| > h^(1/2) number O(h^2 h^(-1/6) + h^(5/3)) over all diagonals, 512 types and 8 depth maps. They go to Proposition partial.
 - The d > 0 shapes are finite in number (2d <= H0 = 210), so R_FF^+ adds a bounded q = 1 weight.
 Correction to polylog_relocation_diluted: (FF) as stated there (summability over max(u0,v0)) is the wrong quantity. The shallow-end sum is what the weighted Theorem D uses, and it holds unconditionally.

LEMMA 3L1F-a (proved here). In SAW* (any shift), there is no in-class mixed quadruple with three odd label points and one filler.
 - The odd points of a class lie on the line L(x) = (4x, 2x) + base, at slots x = iota (mod 32).
 - Case (alpha): side A, B and diagonal end C on L, with D = F. Then n = (t, -2t) and t^2 = 4(c-a)(b-c) = 4096 u'v'. So row(F) = row(A+B-C) - 4t = y_P (mod 64).
 - Case (beta): A = F, with B, C, D on L. Put P = b - d = 32P' and Q = b - c = 32Q'. Then n = mu(2,1) + nu(1,-2) with mu = -4PQ/(P+Q) and nu^2 = 4PQ(P-Q)^2/(P+Q)^2. Writing P'Q' = (gXY)^2, P' = gX^2 and Q' = gY^2, one gets v2(-2mu + 4nu) >= 6 in both parity cases of X, Y (5mu and 5nu are integers, and 5 is a 2-adic unit). So row(F) = row(P1) - 2mu + 4nu = y_P (mod 64).
 - Every SAW* filler row is y_P + {8,16,24,32} or y_P + {24,...,48} (mod 64), never y_P. Contradiction.
 Check: three_label_check.py found 2448 (alpha) and 340 (beta) geometric solutions from Lemma mixedeq, each asserted from scratch, and all had row(F) = y_P (mod 64).

2. COMPATIBILITY OF THE CHANGES (each proved, or with its source cited)

K1. Splits.
 - i mod 32 refines i mod 16 (SAW, L**, the T2 kill, the ll/FF kill, saw (ii)) and i mod 8 (S2a).
 - s mod 16 (R1) refines s mod 4 (SAW's rho0) and the pair {c, c+4}. So (Hs) holds trivially.
 - The rule mod 16l gives M_c = s_c - kappa (mod 16). So M_c - M_c' = 0 (mod 16) in a region (the effect R1 needs), and every label slot is iota + sigma - kappa (mod 4), the constant rho0.
 - SAW* needs y_P (mod 64) and T (mod 4) fixed per type. Both hold.
 - r0 depends on iota (mod 2), and the parity of y_P matches r1 = 3 or 1 (mod 4), as J1 needs.
 - The random split is hereditary, so Proposition R and Proposition 1(b) apply. J4 gets stronger: two classes of one diagonal are at least 64lp > 2600h^2 columns apart.
 - R_IV for i mod 32 is R_IV^(5), a subgraph of R_IV^(4).
K2. Every result that used 2^nu >= K, under the modulus 16l:
 - SAW Lemma 4(b): Proposition 1(d), using (5/l) = -1 (audited).
 - B1, (-1,-1) with Sigma != 0: the l-adic Proposition 1(c) (audited). With Sigma = 0: mixed_quadruples 4(c), since p = +-2 (mod 5).
 - B3 inside a class: unchanged, because Dn = 0. B3 (C1) across classes is LOST; even-even cross-class M2c moves into N_h (Proposition 5 audited; Corollary B unaudited).
 - Corollary B (sea_row3): needs only nu >= 2. Lattice A3 and the SAW* Feo kill need only mod 8 (audited).
 - J4: stronger.
 - Proposition R's valuation step: Proposition 1(b) (audited).
 - v3 Theorem A(ii) and Theorem B Fee: Lemma L-adic.
 - v3 Foo with a filler vertex, and Proposition D: mod 16 only.
 - Width counts: at most 1 diagonal per residue mod 16l.
 Corollary B of sea_row3 and SAW Theorem 1 never use nu.
K3. Primes.
 - p = 3 (mod 4) for II(1,1).
 - p = +-2 (mod 5): Lemma 4(a), II(-1,-1) with Sigma = 0, and the S2a kill.
 - l = +-2 (mod 5): Lemma 4(b) in its l-adic form.
 - gcd(p, 16l) = 1, since p > 40h > l.
 - Raising p to (40h, 80h] keeps everything. Every use is either a lower bound p > 20h, or 'an integer below (20h)^2 has at most one prime factor in the range' (true a fortiori), or a width (a constant factor).
 - There are at least c h^2/log^2 h admissible pairs (prime number theorem in arithmetic progressions, non-explicit).
K4. Filler window against the exclusions. The fillers lie in [h - 210, h], and T*_tau >= h - 186.
 - SAW Theorem 1 needs T* - 24 > (h+3)/2, so h >= 424.
 - Theorem 1(6) needs labels more than 156 rows below the lowest filler. Covered by the cutoff T* - 320.
 - v3 FFo with a label vertex needs y_L < T* - X with T* >= h + 48 - X, that is X >= 234. Taken X = 320.
 - Pb with one label: y_L <= h + r0 - y_F <= 213, removed by R2'.
 - Pc with a filler vertex: g < -296, so W is below row 1.
 - saw (i): H0 = 210, which gives O(H0^(5/2) h^(3/2)).
 - (iii-b), d > 0: still finite.
 - v3 (F3), branch n_y >= 1: n_y <= 210 gives |Dx| <= 106h + 2. Cross-block needs |Dx| >= 4(p - A) > 158h, so the branch is EMPTY again, because p > 40h. With p in (20h, 40h] it would not follow.
 - The SAW* congruences and the Feo kill depend on T* mod 64 only, so the shift keeps them.
K5. Buffer rows: by J1*. J2 is unchanged.
K6. Order of the random choices.
 - The in-class families (R_IV, R_FF) do not depend on positions, so Bad_split depends on psi alone. Fix psi on Theorem D's event (probability >= 1/2).
 - Every first-moment bound (I.2, II, cross-class M2c, family (d), and N_e if proved) holds uniformly over class structures. Their sum then has a good (l,p) by Markov, inside the admissible set. This settles the audit's 'choose (l,p) jointly'.
K7. Theorem IV weights:
 - R_IV: Lemma IV (sum of 1/q_lambda finite, g | 5);
 - R_FF^oo and R_FF^ee, 4 rows each: Lemma FF';
 - R_FF^+: q = 1.
 Each is an AP condition in i on one diagonal, and the psi_T are independent across T. So kappa < infinity, and Theorem IV's cost h^2 Lambda^3 ell^C/B holds, using sum over light T of c_T <= C h Lambda (Theorem S, audited).
K8. Partition of the labels: heavy (Theorem E), Bad_split (Theorem D), Proposition partial, and the light regions. Every parity edge appears once, so J5 applies. Removing labels leaves SAW holes. J3 closure needs counts in the F(Lambda) sense. Label-shallow families do not see fillers, and SAW-family counts treat every non-label slot as a filler, so both are already in that sense.
K9. LAD is NOT adopted. Its pure gap, Theorem 1(6) and V3 are unproved, and its filler window of about 1880 rows would break J1* and (F3). SAW* already leaves the homogeneous nodal-cubic families to Theorem IV.
K10. The additive split (Theorem 5) is compatible (at most 10B classes) but not adopted. Its removed set E is row-structured, with about 2e6 h^2/B labels. Relocating it needs (Rel_rho), which is open, and Proposition partial costs tau*^2 h^2/B. Theorem IV with FF' replaces it.

3. ASSEMBLY AND WIDTH
 - Light regions: 512 types x (4p 16l B + 4A) <= 5.5e6 B h^2.
 - Buffers and margins: about 3 x 512 pieces of width O(h^2).
 - Proposition partial: n_rel = O(h^(11/6)) [large heights] + O(h^(9/5+eps)) [M2c] + B h^(1+o(1)) [first moments] + O(h^(3/2)) [rival pairs, Theorem 1(6), T1 exceptional] + O(h) + the J3-Bad sets of Q1 to Q5. Cost c0 n_rel tau*^2 = o(h^2).
 - Theorem D: C h^2 Lambda^3 ell^C/B + h^2 ell^2.
 - Theorem E: C h^2 Lambda^(E+1) B^(-a) ell^C.
 - With B = Lambda^x the exponent is max(x, E(a) + 1 - ax, 3 - x). It is minimised at x = 1.5, where 1.8588 + 1 - 1.365 = 1.494 <= 1.5.
 - Validity: J1* (ends), J2 (chain), J3 (closure), J4 (splits), J5 (gluing), and the family table, all under Q, AP and U. Then the reduction lemma and truncation.

4. TABLE OF OBSTRUCTION FAMILIES (status: A = audited, N = proved but not audited, H = here, O = open; then the labels hit in L***)
Label-only:
 A1 LLL, LLLL right angles: Proposition 1(b) and Theorem C. A. 0.
 A2 label rival pairs: G_T-independence and block separation. A. 0.
 A3 I.1, II(1,1), II(-1,-1), II(1,-1) with Sigma = 0: mixed_quadruples 4(a)-(d) and Proposition 1(c). A. 0.
 A4 I.2 and II(1,-1) with Sigma != 0: random-prime Theorems 2 and 3. A. B h^(1+o(1)) in expectation.
 A5 S5 (cross-block A2 pairs): Lemma 4(a) and Proposition 1(d). A. 0.
Label + sea:
 B1 X1, X2: block_sea Theorem 1, Theorem A/Corollary B, and v3 A(i). A (row-1), A (Cor B). 0.
 B2 Pa, Pb with two labels: v3 Theorem A(i). N. 0.
 B3 V3 of SLL triples: v3 A(iii). N. 0.
 B4 M1C, M2a with a label diagonal, the shallow diagonal pair, a sea point on the side: block_sea Theorem 2 and Theorem A. A. 0.
 B5 in-class even-even M2c: B3 (C1). A. 0.
 B6 in-class odd-odd M2c, R_IV: B4 (A), then Theorem IV and Lemma IV (N, needs AP). Bad_split goes to Theorem D. Large heights O(h^(11/6)).
 B7 cross-class M2c, odd-odd and even-even: Proposition 5 (A) and point_counts Corollary B (N). O(h^(9/5+eps)) in expectation.
 B8 label-shallow rival pairs: Lemma rival and J1(e). A. 0.
Pure parts:
 C1 Sea pieces, chains, all-g: Proposition 3, Corollary B, J2. A. -
 C2 pure SAW* gap (FFF, Pythagorean filler pairs, 4F quadruples, M2c with two fillers): SAW Theorem 1 (A); carry-over to SAW* (A, h >= 178); the shift (H). -
Label + filler:
 D1 S2: Theorem 1(2b). A. Near-band O(h).
 D2 T1, CE: Theorem 1(5) and Lemma 2. A. 0.
 D3 T2: Proposition 5 and i mod 32. A. 0.
 D4 one label + 3 fillers: Theorem 1(6). A. O(h^(3/2)).
 D5 Feo/S3, every vertex, any blocks; S3-low: SAW* kill (A) and v3 Proposition E (N). 0.
 D6 FFe, Fee, Foo with a label vertex; Foo with a filler vertex under R1: v3 Theorem B (N), with Lemma L-adic (H). 0.
 D7 FFo with a hole vertex: parked; its V3 empty by v3 Theorem C (N). FFo with a label vertex: empty under X >= 234 (H).
 D8 SLF-Pc: parked. V3 family (d): Proposition D (N). h^(1+o(1)) in expectation over p.
 D9 Pb with one label + filler: R2'. N, with the constants of this note. O(h).
 D10 even label + filler rival pairs: saw (i). A. O(h^(3/2)).
 D11 M2c with one label + filler: saw (ii-a,b) (A) and point_counts Theorem A (N). O(h^(9/5+eps)).
 D12 homogeneous Fo/Fo, Fe/Fe, d > 0: finite shapes (A) and R_FF^+ in Theorem IV. Bounded weight.
 D13 homogeneous Fo/Fo, Fe/Fe, d < 0 (thick): saw (iii-b) (A), then Theorem IV (N) and Lemma FF' (H), needs AP. Theorem D blocks.
 D14 {o,e,F,F}, ll/FF, FF/ll: saw (iii-b). A. 0.
 D15 inhomogeneous in-class two-label two-filler (delta_F != 0): additive Proposition 9 (closed form) and ladder Proposition 5. O (Q2).
 D16 cross-block F1, F2, and F3 with n_y >= 1: v3 Proposition F (N), plus K4 (H). 0.
 D17 cross-block F3 with n_y <= -1, odd-odd: reduces to N_e(h). O (Q1).
 D18 cross-block even-even F3, and even-even quadruples whose side is two labels: O (Q1).
 D19 three labels + one filler, {F,o,o,o} in a class: Lemma 3L1F-a. H. 0.
 D20 three labels + one filler, {F,o,e,e} in a class, and every cross-class 3L1F: IN NO NOTE'S LIST. O (Q3). A 14-slot window search found 0 in-class instances with a matching filler row.
 D21 row-3 types, deep-only quadruples with p or q in rows 1-2: O (Q4).
 D22 V3 completeness in SAW*: v3 Theorem C (N). Census owed (U).
Junctions:
 E1 SAW*-shift | Sea(r0,g): J1* (H). 0.
 E2 J2 to J5: A. 0.
 E3 Theorem E block ends: A (t1 audit). E4 Theorem D block ends: N.
Exceptional sets: E5 Corollary B exceptions, near band, low, T1 exceptional: O(h^(3/2)) in total.

5. CONTRADICTIONS AND INCONSISTENCIES BETWEEN NOTES
 - (i) J1 and (P9) (audited) are proved for SAW, while saw_residual and v3_and_cross_block adopt SAW* without re-checking the seam. They are incompatible at kappa = 4 and 6 (Lemma J1*).
 - (ii) v3_and_cross_block Theorems A and B assume 2^nu >= K, while the audited random-prime layout uses the modulus 16l. The fix is Lemma L-adic.
 - (iii) sea_census B6 lists 'all even-even M2c' as EMPTY. That holds in L* only; in L*_l the cross-class case is N_h-counted.
 - (iv) The constants of v3 (T* >= h-63, n_y <= 87) and the 'Y_o window 63' of additive_class_split are SAW*-specific. The shift changes them (K4).
 - (v) polylog's (FF) is the wrong weight (Lemma FF').
 - (vi) additive_class_split Proposition 7 says 'its chromatic number there is 2', against the audited non-bipartiteness of R_IV. It can only hold for the hypercube subgraph or a finite range.
 - (vii) Already flagged by audits: J6 (O1) 'bipartite'; J6 (O3)(iii) 'thin' against the thick d < 0 family; deep_layer_sawtooth Corollary 6 'vanishing load'; saw_residual's Feo branch.
 - (viii) The (O2)/(O3) lists omitted 3L1F (D20).

## External results used

- Prime number theorem in arithmetic progressions mod 5 and mod 20 (non-explicit), for the admissible (l, p).
- Quadratic reciprocity: (5/p) = (p/5) and (5/l) = (l/5).
- tau(n) << n^eps (standard), used in Lemma FF'.
- Henriot, Nair-Tenenbaum bounds uniform in the discriminant, Corollary 2: used only through the hypothesis (AP), not verified.

## Checks

Scripts are in scripts_consolidated_board/. Each ran with py, one at a time, in under 60 s. The repository was only read.
- seam_shift.py: exhaustive check of the seam rival pairs, by Lemma rival, for every (h mod 4, sea row, D0 in [0,63], k in 0..3).
  - The closed form was asserted equal to a direct geometric search (the rectangle with diagonal CD and a vertical lattice diagonal of mixed parity in rows 1..h).
  - 10 of 64 cases have kappa = 4 or 6 pairs at k = 0. In every one, k = 1 or k = 2 removes all bad pairs. There are 0 failures.
- phase_table.py: the k = 0 rows with D0 <= 14 reproduce the audited (P9) table exactly: (1,2), (3,1), (2,2), (0,3); and (2,3), (3,3) with j = 3.
- three_label_check.py: sympy identity for case (alpha). Brute force from Lemma mixedeq, with every solution asserted from scratch: 2448 (alpha) and 340 (beta) in-class {o,o,o,F} solutions, all with row(F) = y_P (mod 64), so none can be a SAW* filler.
- foee_check.py: exact solver for in-class three-label one-filler quadruples, 14 slots, 12 values of T, both roles. It found 0 solutions with F in a SAW* filler row mod 64, including 18 'eeo' solutions at T = 35. This is a small window, not a proof.
- By hand: Lemma L-adic (i) and (ii); Lemma FF' (the U-sum with exponent -1+eps, gcd | 40 re-derived); the K4 constants (X >= 234, y_L <= 213, |Dx| < 106h + 2); the width and exponent arithmetic (E(0.91) = 1.8588).

## Gaps

- Q1 (open): N_e(h) <= h^(2-delta), the v3 Proposition F branch F3 with n_y <= -1 (odd-odd). Also the even-even versions of F3, and the even-even cross-block quadruples whose side is two labels.
- Q2 (open): inhomogeneous two-label two-filler quadruples inside a class (filler rows differ by 8, 16 or 24) hit O(h^(2-delta)) labels. Closed form: additive Proposition 9 (s | 10(delta_F-2t)^2(delta_F+2t), t | G(s)). Numerics suggest about h^0.5 per class line.
- Q3 (open, newly identified): deep mixed quadruples with three labels and one filler. The in-class case {F,o,e,e} and every cross-class configuration remain. In-class {F,o,o,o} is proved empty here.
- Q4 (open): in row-3 types, deep-only mixed quadruples with a corner p or q in rows 1-2. Check whether the deep-only counts used p, q >= 3 anywhere.
- Q5 (open): (AP), Henriot Corollary 2 restricted to i = i0 (mod q), q <= h^(1/2), for the one-variable moments of T2 (7) and the box second moment of sharper (2), at an extra factor tau(q)^C ell^C/q.
- U1 (audit owed): Lemma J1* is new here. Check that J1(a)-(d) carry over to the shifted rows, and run a definition-level seam check at h of about 430 to 500. The Table J1* closed form agrees with the audited (P9) and with the geometric brute force.
- U2 (audit owed): v3_and_cross_block Theorems A, B and C and Propositions D, E and F (unaudited), with the l-adic replacements of Lemma L-adic and the K4 constants (X = 320, R2' at 2i+1 <= 300, p in (40h, 80h]).
- U3 (audit owed): point_counts_power_saving Theorem A and Corollary B (unaudited): Lemma 1(d), the p-adic Lemma 2, the Pell count and the dyadic step.
- U4 (audit owed): polylog_relocation_diluted Theorem D in weighted form (the Chebyshev step D3), Lemma M1, Lemma IV and Theorem IV, all unaudited.
- U5 (audit owed): additive_class_split Lemmas 1, 2 and 4(b) (unaudited), and Lemma FF' of this note.
- U6 (audit owed): Lemma 3L1F-a of this note; the census in three_label_check.py is consistent with it.
- U7 (audit owed): deep_layer_bh16 A1 and A3 (unaudited, used through SAW). Also no full lcd census of SAW* has been run with fillers; one at h of about 450 to 650 is owed.
- U8 (constants): T*_tau >= h - 186 needs h >= 424 for SAW Theorem 1. The primes need the non-explicit prime number theorem in progressions mod 5 and mod 20. Only the asymptotic statement is claimed.
- The exponent 1.5 (not 1.4967) comes from the proved bound sum over light T of c_T <= C h log h. Data give about 1.1h, but this is not proved.
- Theorem N is a conditional implication. m_h = O(h^2) is not addressed: heavy diagonals keep the T1 cost, and chi(Gamma) is open.

## Missing estimate

With the board fixed, the near goal (exponent 1.5) rests on five estimates.
(Q5) The AP form of Henriot.
(Q1) N_e(h) <= h^(2-delta): the number of (y_L1, Dy, f1, f2, k, w) with k(w^2 + (N'-df)(N'+A')) = w N'(A'+df), k even and |Dx| >= 158h. Also its even-even analogue.
(Q2) Two-filler-row in-class quadruples: an O(h^(1-delta)) count per class line of the (t, s) with s | 10(delta_F-2t)^2(delta_F+2t) and t | (s-2delta_F)((s-2delta_F)^2+delta_F^2).
(Q3) Three-label one-filler quadruples, {F,o,e,e} in a class and all cross-class cases. A first try is the 2-adic and mod-64 row argument of Lemma 3L1F-a, with the even line E(x) = O(x) + (0,T), followed by a mod-p argument across classes.
(Q4) The rows-1-2 check for deep-only quadruples in row-3 types.

## Next steps

- Audit Lemma J1* (the T* shift table and the carry-over of J1(a)-(d)), and run the audit's junction finder on a shifted SAW* seam at h of about 430 to 500.
- Audit v3_and_cross_block Theorems A to C together with Lemma L-adic, then point_counts Theorem A.
- Attack Q3: extend the mod-64 argument of Lemma 3L1F-a to {F,o,e,e} (even rows = y_P + T mod 64) and try a mod-p kill across classes, as in v3 F2.
- Write out (AP) for the one-variable s-moments and the box second moment, then have Theorem D (weighted) and Theorem IV audited.
- Attack Q2 and Q1 through their mutual-divisibility forms. Only one polynomial branch (gamma = 0) is known, and it gives O(sqrt(e h)).
- Run a full definition-level census of L*** at h of about 450 to 650 (one region type with true p > 40h and the shifted T*) to test the family table for completeness.

