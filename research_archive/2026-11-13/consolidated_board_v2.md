# The consolidated board, version 2

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: L*** restated as (B0) to (B10) with every round-10 and round-11 fix and one destination rule, the merged obstruction table, and Theorem N with an explicit hypothesis list. No obstruction cell is open. The bound m_h <= C h^2 (log h)^1.5 (loglog h)^C is conditional on the block-layout fact for Theorem D and E blocks (N-1), uniformity of the first-moment bounds (N-3), and audits of the new steps V2-1 to V2-9. Not audited yet.

# Result

## Status

partial

## Summary

consolidated_board_v2 applies every round-10 and round-11 fix. L*** is restated as (B0)-(B10) with one destination rule. No obstruction cell is open, and (AP), Q1 to Q4 are closed by audited notes. Theorem N (exponent 3/2, c = 1/2) is still conditional on four unaudited items: K8'(b) together with E4 (how the Theorem D and Theorem E blocks lay out their edges and ends), completeness of the K2/K4 lists (only as far as a grep reached), K6 uniformity, and the short new steps written here.

## Statements

THEOREM N (v2; CONDITIONAL). Let h >= h0, where h0 >= 424 is not explicit because it comes from the prime number theorem in progressions mod 5 and mod 20. Let L*** be the board (B0)-(B10) below. Assume these four things.
(i) The paper results P1-P3.
(ii) The audited inputs A-1 to A-26 of the hypothesis list, as corrected in this note.
(iii) N-1 = K8'(b): every Theorem D block and every Theorem E block places each parity edge it receives exactly once, as a double. Every other column of the block is a singleton, and each block has constant row-h tails (E4).
(iv) N-3 = K6 uniformity: every first-moment bound used in (B7) R-f holds uniformly over the class structure and over psi.
Then, for every m >= M, L*** truncated to columns 1..m is a valid blackout with m + q_h points, and
 M <= C h^2 (B + Lambda^(E(a)+1) B^(-a) + Lambda^3/B) ell^C1 + c0 n_rel tau*(h)^2 + C h^2,
with Lambda = log h, ell = loglog h, B = ceil(Lambda^(3/2)), a = 0.91, E(a) = (1+3^a)/2 = 1.8588, and
 n_rel = O(h^(2-eps_D) log B + h^(11/6) log h + h^(9/5+eps) + B h^(1+o(1)) + h^(3/2) + h).
Here eps_D > 0 is the exponent of Theorem D. Hence
 m_h <= C h^2 (log h)^(3/2) (loglog h)^C1, that is (log h)^(2-c) with c = 1/2.
This beats T1 (C h^2 log^2 h (loglog h)^C).
If the sum over light T of c_T is O(h) (not proved), the exponent becomes 2.8588/1.91 = 1.4967.
Status: (AP), Q1, Q2, Q3, Q4 and Q5 are no longer hypotheses. Each is now an audited result: A-19, A-20, A-23 and A-24, A-24. The implication still rests on N-1 and N-3, on the new steps V2-1 to V2-9 (none separately audited), and on the K2/K4 lists, whose completeness is confirmed only as far as a text search reached. NOT PROVED: m_h = O(h^2).

## Proofs

consolidated_board_v2 (14 November 2026). It replaces consolidated_board.md. All notes cited are in research_archive/2026-11-13.

STATUS KEY:
- P: paper.
- A9: audited with fixable gaps in round 9 or earlier.
- A10, A11: audited with fixable gaps in round 10 or round 11.
- N: proved, not audited.
- V2: a short step written here. Each V2 proof is given in full in section 1b. None has a separate audit.
- CIT: holds by citation only.
Every fix applied below is marked [Fk] and carries its re-check.

==================================================
1. SPECIFICATION OF L*** (v2)
==================================================

(B0) PARAMETERS
- h >= h0 with h0 >= 424, non-explicit.
- Lambda = log h, ell = loglog h, B = ceil(Lambda^(3/2)). Stride 4 only.
- A = ceil(h/2), K = floor(h/2), W_h = floor((h-1)^2/4) + 1 (paper).
- A label is (i,j) with 0 <= i < A and 0 <= j < K. Its odd point is in row 2i+1 and its even point in row 2j+2, in one column (a double). Write s = j - i and T = 2s+1. There are q_h = AK = floor(h^2/4) labels.
- Locality (P3): every violation lies in 2W_h+1 consecutive columns.

(B1) HEAVY DIAGONALS
- A diagonal is heavy when kappa_T := k_T^(2) >= B.
- Its non-exceptional labels go to Theorem E blocks (t1_cost_decomposition, A9). These sit right of z, with row-h collars and tails.
- Its T1-exceptional labels go to Proposition partial (B7, R-d).

(B2) PRIMES, chosen jointly and last
- l is prime in (1.04h, 2.08h] with l = +-2 (mod 5).
- p is prime in (40h, 80h] with p = 3 or 7 (mod 20).
- Then gcd(p, 16l) = 1, and there are at least c h^2/log^2 h admissible pairs (K3, A10).

(B3) REGION TYPES
- tau = (iota, sigma) = (i mod 32, s mod 16), so there are 512 types.
- r0 = 1 if iota is odd, r0 = 3 if iota is even.
- y_P := 2 iota + 1 (mod 64).
- [F2] tau_T := 2 sigma + 1 (mod 32). three_label_one_filler.md calls this residue T0. It is renamed here so that T0_tau keeps its (B6) meaning, the filler top row.
- T mod 4 is fixed by sigma. Put c_tau = 1 if T = 3 (mod 4) and c_tau = 3 if T = 1 (mod 4).

(B4) CLASSES
- On each light diagonal T, a greedy G_T colouring gives c_T <= kappa_T + 1 <= B classes. G_T is as in stride_menu Proposition 1' (A9).
- Each class is restricted to the types.
- Each (T, tau) class is split into K_T = floor(B/c_T) subclasses by iid uniform colours psi_T, independent across T.
- So there are at most B subclasses per (T, tau).

(B5) PLACEMENT (rule L*_l)
- kappa is one global integer, and b_tau is a per-type offset.
- Subclass k of diagonal s in type tau sits at t = rho_s + 16lk, with rho_s = p^(-1)(s - kappa) (mod 16l).
- Label (i,j) of that subclass sits at slot n = i + p t + b_tau, in column 4n.
- [F1] DERIVED CONSTANTS. Put rho_tau := iota + sigma - kappa + b_tau (mod 16), rho0 := rho_tau mod 4, and kappa_tau := kappa - b_tau.
- Re-check: n - i = pt + b_tau = s - kappa + b_tau (mod 16l), with i = iota (mod 32) and s = sigma (mod 16). So n = rho_tau (mod 16) for every label slot of R_tau, and n(c) := s_c - (n - i) = kappa_tau (mod 16l) for every class.
- This corrects K1 of consolidated_board.md, which dropped b_tau (flagged by audit_deep_layer_bh16 and the q3 audit). It also fixes the A3 lattice constant (kappa_tau, not kappa) and (K-d) of three_label_one_filler.md.
- low_rows (F1) should cite (B5) directly.

(B6) FILLER LAYER (SAW*-shift)
- T0_tau is the largest y <= h with y = y_P + 32 (if T = 3 mod 4) or y_P + 48 (if T = 1 mod 4), mod 64.
- D0 := h - T0_tau, in [0,63]. T*_tau = T0_tau - 64 k_tau, with k_tau taken from Table J1*.
- Every deep column 4n of R_tau, margins included, that holds no label gets exactly one point, in row T*_tau - 24 + 8((n - rho0) mod 4), with rho0 from [F1]. Such a column is an unused slot, a hole left by a relocated label, or a margin slot.
- Shallow columns x != 0 (mod 4) hold (x, r0).
- Consequences:
  - T*_tau >= h - 186, and every filler lies in [h-210, h];
  - a filler at offset w lies in row f = y_P + 8(w + c_tau) (mod 64), because the shift by 64k leaves T* mod 64 unchanged;
  - a hole has offset 0 and lies in row T* - 24.
- End phases do not re-phase the sawtooth (q3 audit, part C). (Phi) only fixes where a region ends, by up to 3 extra slots of the same sawtooth. Those slots lie more than 2W_h+1 columns from every label.

TABLE J1* (unchanged; A10)
Notation: entries are (o, kappa, j) = (filler offset, slot distance, j of Lemma rival).
- h even, and row-1 types with h = 1 (mod 4): k = 0, no bad pair.
- h = 1 (mod 4), row-3 types:
  - k = 0 bad pairs: (1,2,1) at D0 = 0, (3,1,1) at 4, (2,2,1) at 8, (0,3,1) at 12, (3,2,1) at 16, (1,3,1) at 20, (2,3,1) at 28, (3,3,1) at 36;
  - k = 1 at D0 = 40 and 48; k = 2 at D0 = 56.
- h = 3 (mod 4), row-1 types: (2,3,3) at D0 = 4, (3,3,3) at D0 = 12; k = 1 at D0 = 24, 32, 40, 48.
- h = 3 (mod 4), row-3 types: the first list shifted by 2 (D0 = 2, 6, ..., 38); k = 1 at D0 = 42 and 50; k = 2 at D0 = 58.
- Every k = 0 row has a clean phase under (Phi). Every shifted row is clean at every phase.
- [F17] The failure of the unshifted SAW* layer occurs in 10 of the 64 odd-h cases (2 residues of h mod 4, times 2 sea rows, times 16 values of D0).
- Evidence: the definition-level seam check at h = 432 to 500 (audit_consolidated_board) and census (C3) at h = 429, 451 and 701.

(B7) DESTINATIONS AND THE PRIORITY RULE [F5, F6, F8]
Each label goes to exactly one destination. Apply the first rule that fits:
1. The label is on a heavy diagonal and is not T1-exceptional: it goes to Theorem E (B1).
2. The label is in Bad_split (B8) and not in the exceptional set E_D of its Theorem D group: it goes to Theorem D. A label of E_D goes to Proposition partial.
3. The label meets some criterion R below: it goes to Proposition partial. This is one instance: case (a) for even h, inside the row-1 tail; case (c) for odd h, with switch z.
4. Otherwise the label stays in its light region R_tau.

The criteria R:
- R-a: i = 0. In row-3 types also i = 2, and j in {0, 1}.
- R-b: near band. An endpoint row >= T*_tau - 320. In types with k_tau = 2, also an odd row >= T*_tau - 444 [F8, NEW, V2-4].
- R-c: R2', that is 2i+1 <= 300.
- R-d: every T1-exceptional label (heavy ones included) and every SAW Theorem 1(6) label (D4). The near-band S2 labels (D1) are already inside R-b.
- R-e: large heights [F3]. Labels touched by an R_IV edge with max(p_lambda, q_lambda) > h^(1/2)/32, or by an R_FF^oo or R_FF^ee edge with |U'| > h^(1/2)/32.
- R-f: the labels of the counted families:
  - A4 (I.2, and II(1,-1) with Sigma != 0);
  - B7 (cross-class M2c, oo and ee);
  - D8 (V3 family (d), Proposition D) [F5, ADDED];
  - D10 (even label plus filler rival pairs);
  - D11 (one label plus filler M2c) [F5, ADDED; found by the census, which saw 176 such labels at h = 701];
  - D17 (cross-class F3 with n_y <= -1, odd-odd, df = 0) [F5, ADDED explicitly];
  - D18 (the even-even analogue of D17) [F5, ADDED explicitly].
- R-g: the set E_D of each Theorem D group, with |E_D| <= 4h^(2-eps_D).

Removed from v1:
- the bullet 'J3-Bad sets of the open families (hypothesis Q)', because no family is open;
- D20, which is empty;
- D9 as a separate item, because D9 is contained in R2' (V2-6).

Why any such rule is safe: J3 in hitting-set form (V2-1), Lemma M1 monotonicity (A9), and Proposition partial accepting any edge set (P).

(B8) BAD_SPLIT AND THEOREM D
In each final subclass, Bad_split is the shallow end of every monochromatic edge of these graphs:
- R_IV with max(p_lambda, q_lambda) <= h^(1/2)/32 (its q-end);
- R_FF^oo and R_FF^ee with |U'| <= h^(1/2)/32 (the end at depth |U'|), in each of the 4 filler rows;
- R_FF^+, with range |t| <= 210 [F9]. This was 86 in additive Lemma 1; the new bound comes from 2d <= h - y_F <= 210, and t = 0 (mod 32) inside a class, so at most 6 neighbours lie on each side.

Bad_split goes to Theorem D-weighted (A10), with [F14]:
- the hypothesis rho >= (log h)^(-C') kept (rho_j >= 1/B = Lambda^(-3/2));
- c_q counted with multiplicity over lambda, so kappa_IV = sum over lambda of (tau(q_lambda)^C/q_lambda + tau(p_lambda)^C/p_lambda), which is finite by Lemma IV.

The blocks are grouped by c_T in dyadic ranges and placed right of z, with row-h tails.

Modulus [F3, V2-3]: for every label f, the event 'f has an edge at height lambda' is a union of O(1) residue classes of i modulo q' = lcm(32, q). With the cutoff above, q' <= h^(1/2), the range of ap Lemma 4 and of Theorem D-weighted.

(B9) BUFFERS AND ENDS
- Buffer row g(h) = h (h even), h-1 (h = 1 mod 4), h-3 (h = 3 mod 4).
- Pieces Sea(r0,g) and all-g, each 2W_h+1 wide, in the order of (P8): row-1 tail | Sea(1,g) | the 256 row-1 types | Sea(1,g) | all-g | Sea(3,g) | the 256 row-3 types | Sea(3,g) | all-g | Sea(1,g) | row-1 tail.
- [F12] Margins: R_tau has 2W_h+1 columns of pure SAW*-shift BEFORE its first and AFTER its last label column, plus at most 3 slots to realise (Phi).
- End phases follow Table J1* and (P9).
- The g(h) choice settles the serious issue of audit_sea_row3_split (V2-2).

(B10) GLUING
One switch z: row 1 left of z and row h right of z, outside the windows. All windows are separated from each other and from z by more than 2W_h columns. Gluing is by J5. The board is truncated to columns 1..m.

ORDER OF RANDOM CHOICES (K6)
1. The classes (deterministic).
2. psi, taken on the intersection of the Theorem D events of all O(log B) dyadic groups. Those events are independent across T, so the intersection has positive probability (polylog audit). Bad_split depends on psi only.
3. (l, p), by Markov applied to the sum of the first moments of A4, B7, D8, D17, D18 (and of D11 if it is counted in expectation). This needs N-3.

REMARKS (census_consolidated_board; N, not load-bearing)
- (O1): for h <= 5117, no two subclasses lie within 2W_h+1 columns of each other (64p - 4(A-1) > 2558h). So every cross-class family is empty at those heights.
- (O2): no light label survives (B7) for h <= 652. The extension R-b only removes more labels.

THE K-ITEMS IN v2
- K1: as before, with [F1].
- K2: unchanged. It is complete as far as the klists audit's grep reached (A11).
- K3: unchanged (A10).
- K4: the corrected list. Fillers lie in [h-210, h] and T* >= h - 186.
  - SAW Theorem 1 needs h >= 424.
  - Theorem 1(6) cutoff: y_D - 156 >= T* - 180 > T* - 320.
  - FFo with a label vertex: X >= 234 (we use 320).
  - Pb with one label: needs an odd label point and a base filler, so 2i+1 <= 205 (V2-6). [F9] This corrects 'y_L <= 213'.
  - Pc with a filler vertex: g < -296.
  - saw (i) and BH16 A5: H0 = 210.
  - (iii-b) with d > 0: finite, and R_FF^+ range 210.
  - v3 constants:
    - (F1): |delta| >= 39h;
    - (F2): |n_x| < h/158;
    - A(ii) both odd: |a| < h/158 and |2a - f| < 3h < p;
    - (F3) with n_y >= 1: |Dx| <= 106h + 2 < 158h, so the branch is empty;
    - Foo with a label vertex: |alpha| < h/600;
    - Proposition D: one prime factor in (40h, 80h];
    - Proposition E: W row >= 309.
  - two_filler Proposition 4 needs h >= 280.
  - D-1L3F with the label on the side: the grid argument needs y_L < T* - 72 - 2(h - T*). That holds under R-b, including the k = 2 extension (V2-4). Lemma S1L gives a second proof (V2-5).
- K5: buffer rows by J1* and J2.
- K6: see 'Order of random choices' above.
- K7: Theorem IV weights:
  - R_IV: Lemma IV, with the large-lambda count corrected through p < 21 be^3 [F15];
  - R_FF^oo and R_FF^ee: Lemma FF';
  - R_FF^+: q = 1;
  - all with the cutoff h^(1/2)/32.
- K8': see V2-8.
- K9: LAD is not adopted.
- K10: additive Theorem 5 is not adopted.

OTHER WORDING FIXES CARRIED INTO v2
- [F16] Q5 is (AP); list it once.
- [F18] Section 5 of v1, items (v) and (vi), weakened as the round-10 audit asked:
  - polylog's (FF) with the max weight matches a deep-end rule; the shallow-end rule of (B8) needs the 1/|U'| sum of FF';
  - additive Proposition 7's 'chromatic number 2' refers to the hypercube subgraph only.
- [F19] Lemma L-adic: add the degenerate cases. Dj = 0 gives a = 0 or a degenerate leg. eta = 0 gives a vertical leg.
- [F20] two_filler: write 2n = 2Dv + V - U and 2n_x = 2Dx + (x_F2 - x_L2) - (x_F1 - x_L1).
- [F21] point_counts Corollary B bounds N_h^int (n1 | e u2). That is exactly the count that M2c and Proposition 5 need.
- [F24] three_label_one_filler step 4 should read: 'Fee and Foo by v3 Theorem B (A9) with Lemma L-adic, Feo by the audited SAW* kill. Q3 concerns V4 and V1 only. The parked triples are SLL-Pc, SLF-Pc and FFo with a hole vertex. Their V3 pairs reduce to family (d) (v3 Theorem C).'
- [F24] low_rows Theorem Q4(b) is restricted to row-3 types. For row-1 types it covers only the V3 pairs of deep-only triples, which does not matter: row-1 types use unshifted rows.
- [F24] Q4(e) is derived from (a), (c) and (d): every deep-only obstruction with a non-black corner in rows 1-2 is an empty triple, a rival pair (inside saw (i), or excluded by G_T), or a four-label quadruple (A3/A4 over [1,h]).
- [F24] The (e) sentence on sea_row3 is reworded as the q4 audit asks.
- [F26] v3 Proposition D under R1: the minimal separation is 64p, not 32p. The expectation bound is unchanged.

==================================================
1b. SHORT PROOFS WRITTEN HERE (V2)
==================================================

V2-1. J3 IN HITTING-SET FORM.
Claim: let R be any set of labels of a region that meets every Lambda (|Lambda| <= 7) for which F(Lambda) has a violation whose label columns are exactly Lambda. Then F(Y0 \ R) has no violation, provided F(empty set) has none.
Proof:
- A violation is fixed by its black points, its white corner and the content of W's column, so by at most 7 columns (J3 proof, A9).
- Suppose F(Y0 \ R) has a violation, and let Lambda be the set of labels whose columns it uses. Then Lambda is contained in Y0 \ R.
- In F(Lambda) those same columns have the same content: the labels of Lambda, and fillers or holes elsewhere. So F(Lambda) has the same violation.
- If Lambda is empty, this contradicts the clean pure gap. Otherwise R meets Lambda, which contradicts Lambda being contained in Y0 \ R. QED.
Consequence: relocating one end of each R_IV or R_FF edge (B8) is enough, and so is relocating every label of each counted family (B7). This needs the family counts in the F(Lambda) sense, every non-label slot being a filler. K8 of v1 states that they are; the J3 note itself flags this point.

V2-2. BUFFER ROW g.
- The audit of sea_row3 found a rival pair at the all-g | Sea(3,g) seam: C = (x, 3) and D in row g.
- Lemma rival needs 4j(g - 3 + j) = t^2 with 1 <= j <= 2 (since 3 - j >= 1) and g + j <= h.
- Even h: g = h, so g + j > h. No pair.
- h = 1 or 3 (mod 4): g = h-1 or h-3 is 0 (mod 4).
  - j = 1 needs g - 2 = (t/2)^2, but g - 2 = 2 (mod 4) is not a square.
  - j = 2 needs t = 4u and g - 1 = 2u^2, but g - 1 is odd.
- So there is no pair. Script: 0 cases for 424 <= h <= 20000. This agrees with J2 (A9) and census j2.py.

V2-3. CUTOFF h^(1/2)/32 AND THE AP MODULUS.
- On one diagonal, labels of type tau satisfy i = iota (mod 32), and the depth delta(i) depends on the type through Y_o.
- So the event that an edge of height q is present is a union over iota of at most O(1) classes of i mod lcm(32, q) <= 32q.
- With q <= h^(1/2)/32, every modulus is <= h^(1/2), inside ap Lemma 4 and Theorem D-weighted as stated.
- kappa stays finite: the sum over the 32 residues gives 32 · (h/(32q)) · tau(32q)^C <= C (h/q) tau(q)^C.
- Cost:
  - R_IV: be > ((h^(1/2)/32)/21)^(1/3) = c h^(1/6), and the tail is O(h^(11/6) log h).
  - R_FF: the tail sum over |U'| > Y of 1/|U'| is O(Y^(-1/3)), giving O(h^2 (h^(1/2)/32)^(-1/3)) = O(h^(11/6)).
- Constant factors only.
- An alternative is to extend (AP) to q <= 32 h^(1/2): ap Lemmas 1-3 allow h^(1-eta), but Lemma 4 is stated only for q <= h^(1/2). The cutoff route avoids that extension.

V2-4. D-1L3F WITH THE LABEL ON THE SIDE.
- Let A = L be the label, and B, C, D fillers in rows >= T* - 24.
- If L is even, the row-parity count already excludes the configuration.
- If L is odd: 2n = C + D - A - B, and one of p, q has row (y_B + y_C + y_D - y_L)/2 >= (3T* - 72 - y_L)/2. This exceeds h iff y_L < T* - 72 - 2D, with D := h - T*_tau.
- k = 0 and k = 1 types have D <= 114 <= 124. There T* - 320 suffices, and kept labels have y_L <= T* - 321.
- k = 2 types have D in {184, 186}. There we need y_L < T* - 444, which the R-b extension guarantees.
- The extension removes O(h) labels: about 62 values of i times h/2 values of j per type, over at most 64 types.
- So the cell is E with no new lemma. The klists audit found that the v1 grid argument fails here.

V2-5. LEMMA S1L (second derivation; first given in the klists audit). In one region, under any 64k shift, no mixed quadruple consists of one odd label point on the side and three fillers.
Proof:
- Put L at the origin. Divide coordinates by 4: a filler P becomes (a_P, 2b_P) with a_P = n_P - n_L.
- Its offset is a_P mod 4, which uses [F1] (n_L = rho0 mod 4). So b_P = b0 + (a_P mod 4), where 8b0 = T* - 24 - y_L = 8 (mod 16). So b0 is odd.
- Lemma mixedeq gives |B|^2 = |D - C|^2: a_B^2 + 4b_B^2 = d^2 + 4e^2, with d = a_D - a_C, e = (a_D mod 4) - (a_C mod 4) = d (mod 4), and |e| <= 3.
- Right side: 5 (mod 8) if d is odd; 20 (mod 32) if d = 2 (mod 4); 0 (mod 16) if 4 | d.
- Left side:
  - a_B odd: b_B is even, so the left side is 1 (mod 8). No match.
  - a_B = 2 (mod 4): b_B is odd, so the left side is 8 (mod 16). No match.
  - 4 | a_B: b_B = b0, so the left side is a_B^2 + 4 (mod 32). This forces d = 2 (mod 4), e = +-2 and a_B = 4 (mod 8).
- Perpendicularity n.B = 0 reads (a_C + a_D - a_B) a_B + 4(b0 + (a_C mod 4) + (a_D mod 4)) b0 = 0.
  - The two residues mod 4 differ by 2, so they sum to 2 or 4, and the second term is 4 times an odd number: v2 = 2.
  - a_C + a_D - a_B = 2a_C + 2 - a_B (mod 4) is 2 (mod 4) when a_C is even and 0 (mod 4) when a_C is odd. With v2(a_B) = 2, the first term is 0 or has v2 >= 3.
  - So the sum has v2 = 2 and is not 0. Contradiction.
- The swap A <-> B is symmetric. QED.
Script: 0 residue solutions mod 32 over every odd b0. The control with b0 even has 10240 residue solutions.

V2-6. Pb WITH ONE LABEL AND ONE FILLER (re-derivation of the klists item).
- Right angle at the shallow corner E: a c + f g = 0, with a = x_L - x_E, c = x_F - x_E, f = y_L - r0 and g = y_F - r0. Since y_F = y_P (mod 8) and y_P - r0 = 2 (mod 4), g = 2 (mod 4).
- Even label point: f is odd, so v2(fg) = 1. But ac is odd (x_E odd) or has v2 = 2 (x_E = 2 mod 4). Impossible.
- Odd label point: x_E = 2u with u odd, and a = 2a', c = 2c'. Then a'c' = 1 + 2(n_L + n_F) (mod 4), and -f'g' = 3 (mod 4) because g' - f' = 4(o + c) = 0 (mod 4). So n_F - n_L is odd, and F is a base with y_F >= T* - 16 >= h - 202.
- The W row y_L + y_F - r0 <= h then gives y_L <= 205. So R-c (300) covers it.

V2-7. TWO_FILLER THEOREM 3(b), FROM SHAPES TO LABELS (re-derivation of the klists text).
- An even-even shape with df = 0 fixes (Dx, Dy). Put Dn := Dy/2 - Dx/4 = Ds - p Dt = n(c2) - n(c1). This lies in 16lZ, and it is nonzero across classes: Dn = 0 would force Dt = Ds = 0.
- |Dn| <= h/2 + (2W_h+1)/4 < (1.04h)^2, so at most one admissible l divides Dn.
- Given the shape and s1, the label L1 is unique (each parity edge occurs once), and its class does not depend on (l, p).
- Given p, Ds = Dn (mod p) with |Ds| < p/2, so L2 is unique.
- So E[labels hit] <= 2 N^ee · 2h / #L = O(N^ee log h) = O(h^(9/5+eps)), with N^ee << h^(9/5+eps) by Theorem 3(b) (A10).
- Theorem 3(b) uses the (e,n1,Q) witness map with no parity, and the region-wide congruences Dx = 0 (mod 64) and Dy = 0 (mod 32).

V2-8. K8' AND ITS PROOF FOR L***.
Statement K8': every column is a singleton or a double, the doubles carry pairwise distinct parity edges, and every parity edge occurs.
Proof for the light part and Proposition partial (assembled from the table audit, part F):
- In R_tau, a label column is the double {2i+1, 2j+2}. Every other deep slot holds one filler (holes included). Shallow columns, buffers, tails and the switch are singletons.
- Label columns are distinct: inside a class i differs, and across classes |p Dt| >= p > |Di|.
- Each label lies in exactly one destination, by the priority rule (B7).
- Proposition partial places exactly the edges it receives (P).
- K8'(b) is NOT proved here: that the Theorem D and Theorem E blocks place each received edge exactly once as a double, with singletons elsewhere (N-1). Truncation keeps every double, because all doubles lie in columns <= M <= m.

V2-9. n_rel.
n_rel is the sum of:
- O(h): R-a, R-b (k = 2 extension included), R-c, D1, D9;
- O(h^(3/2)): D4, D10, the T1-exceptional labels;
- B h^(1+o(1)): A4, D8 (Markov);
- O(h^(9/5+eps)): B7, D11, D17, D18;
- O(h^(11/6) log h): R-e;
- 4h^(2-eps_D) per group, over O(log B) groups: R-g. v1 omitted this term.
The cost c0 n_rel tau*(h)^2 = h^(2 - min(eps_D, 1/6) + o(1)) = o(h^2).

==================================================
2. THEOREM N: HYPOTHESIS LIST
(input | note | statement used | status | audit)
==================================================

PAPER
- P1 | sec2_prelim.tex, sec5_threshold.tex | Lemma mixedeq, reduction lemma, Lemma rival, Lemma sea, criterion and girth lemmas, chain lemma | P | paper.
- P2 | sec5_threshold.tex | Proposition partial (cases (a) and (c)): any n edges in width c0 n tau*(h)^2 | P.
- P3 | sec5 | locality 2W_h + 1 | P.

AUDITED BEFORE ROUND 10 (A9)
- A-1 | block_sea_classification | criterion (V1)-(V5) under K8'; Theorems 1 and 2 (the shallow sets) | A9 | audits_rigid_mixed_sea.md.
- A-2 | rigid_layout_cross_block | rigid Theorem C (LLL, in-class o-e rival pairs), Proposition R | A9 | audits_rigid_mixed_sea.md.
- A-3 | mixed_quadruples_blocks | Theorems 1-4 (four-label quadruples) | A9 | audits_rigid_mixed_sea.md.
- A-4 | stride_menu | Proposition 1' (G_T through Lemma rival, L <= h-1) | A9 | audits_stride_menu_and_gamma.md.
- A-5 | heavy_light_split | the heavy/light threshold; Theorem S: sum over light T of c_T <= C h Lambda | A9 | audit_heavy_light_split.md.
- A-6 | t1_cost_decomposition | Theorem E (heavy blocks, cost C h^2 Lambda^(E+1) B^(-a) ell^C, row-h ends); the T1/T2 inputs | A9 | audit_t1_cost_decomposition.md.
- A-7 | sea_row3_split | Theorem A ((H1)-(H4)); Corollary B | A9 | audit_sea_row3_split.md. The g issue is met by (B9) (V2-2). (H4) follows from (L3).
- A-8 | sea_census_rigid | B1-B4 (definition of R_IV, B3(C1)) | A9 | audit_sea_census_rigid.md.
- A-9 | deep_layer_sawtooth | SAW Theorem 1 (1)-(6), Lemmas 2-4, Proposition 5 | A9 | audit_deep_layer_sawtooth.md.
- A-10 | ratio_graph_r_iv | Lemma 2, Corollary 3, Theorem 4 (R_IV is not bipartite, hence the random split) | A9 | audit_ratio_graph_r_iv.md. Corollary 5(iii) is not used.
- A-11 | threshold_families_random_prime | L*_l rule; Proposition 1(b), (c), (d); Theorems 2 and 3; Proposition 5 | A9 | audit_threshold_families_random_prime.md.
- A-12 | saw_residual_families | SAW* definition; Feo kill (iii-a); (i); (ii-a,b); (iii-b) | A9 | audit_saw_residual_families.md.
- A-13 | full_layout_junctions | J1-J5; (P7)-(P9) | A9 | audit_full_layout_junctions.md. J6 is not used.
- A-14 | point_counts_power_saving | Theorem A, |E0(Q)| << Q^(4/5+eps); Corollary B for N_h^int | A9 | audit_point_counts_power_saving.md.
- A-15 | v3_and_cross_block | Theorems A, B, C; Propositions D, E, F | A9 | audit_v3_and_cross_block.md. Proved under 2^nu >= K and p in (20h, 40h]; carried to L*** by Lemma L-adic (A-21) and K4 (A-26).
- A-16 | polylog_relocation_diluted | Lemma M1; Theorem D; Lemma IV (large-lambda count corrected, p < 21 be^3); the mechanism and bookkeeping of Theorem IV, with its hypothesis list replaced by the table | A9 | audit_polylog_relocation_diluted.md.
- A-17 | additive_class_split | Lemmas 1, 2, 4 (U = k(a^2 + b^2), gcd(U,V) divides 40, the depth mu|U'|) | A9 | audit_additive_class_split.md.

ROUND 10 (A10)
- A-18 | ap_hypothesis_henriot | Lemma 1 (q <= h^(1-eta), with I contained in [-A0h, A0h], plus the short-interval trivial case); Lemmas 2 and 3 (3(b) with saving min(h^(-1/2), h^(-eta))); Lemma 4 (q <= h^(1/2), coincidence diagonals by w < 2v(f)); Corollary = (AP); Theorem D-weighted | A10 | audit_ap_hypothesis_henriot.md. The auditor read Henriot's 2014 erratum (New Theorem 5).
- A-19 | the same | (AP) closes Q5 | A10.
- A-20 | two_filler_row_lemma | Lemma 1; Corollary 2 (D15 empty); Theorem 3(a); the shape count of 3(b); Proposition 4 (h >= 280 in L***) | A10 | audit_two_filler_row_lemma.md. The 3(b) label step is V2-7.
- A-21 | consolidated_board | Lemma J1* and Table J1*; Lemma L-adic; Lemma FF'; Lemma 3L1F-a; K1-K4 arithmetic; width | A10 | audit_consolidated_board.md.
- A-22 | deep_layer_bh16 | A1 (any r0), A2, A3 (with constant kappa_tau) | A10 | audit_deep_layer_bh16.md.

ROUND 11 (A11)
- A-23 | three_label_one_filler | Lemma N (N1)-(N4); Theorem Q3 (a), (b), with rho0 from [F1] | A11 | q3 audit. Cross-class Q3 rests on the proof alone: it is vacuous for h <= 5117 by (O1).
- A-24 | low_rows_row3_types | Lemmas LR, S and N; Theorem Q4 (a), (c), (d); (b) restricted; (e) from (a), (c), (d) | A11 | q4 audit.
- A-25 | obstruction_table_completeness | Theorem K for the amended (B7); Lemma Q3; sections 0-6 | A11 | table audit. Lemma Q4 is spot-checked only and is NOT used: A-24 replaces it.
- A-26 | klists audit | K2 complete as far as the grep reached; K4 corrected; Lemma S1L; the R2' sufficiency; E4 by citation (Lemma M1, Theorem E, J5) | A11 (the search, and the new items in the audit's own derivation).

NOT AUDITED (hypotheses of Theorem N)
- N-1 | K8'(b) and E4 | the Theorem D and Theorem E blocks: each received edge placed once as a double, singletons elsewhere, constant row-h tails | CIT | no definition-level D block has been built.
- N-3 | K6 | the first-moment bounds of R-f hold uniformly over the class structure and psi | N | not checked by any audit (audit_consolidated_board, section 8).
- N-4 | this note | V2-1 to V2-9 | V2.

EXTERNAL
- Henriot, New Theorem 5 (MPCPS 157 (2014) 375-377), through A-18.
- The prime number theorem in progressions mod 5 and mod 20 (non-explicit).
- Quadratic reciprocity ((5/p) = (p/5)).
- tau(n) << n^eps.

==================================================
3. MERGED OBSTRUCTION TABLE
(cell | verdict E/C/W | source | status | labels hit, destination)
==================================================
Cell kinds:
- E: impossible.
- C: counted, with its labels relocated.
- W: internal to a certified window.
Table T cell names are in brackets.

WINDOWS AND CHAIN
- W1 [WP] Proposition partial | W | P2 | P.
- W2 [WD] Theorem D blocks | W | A-18, A-16 | A10, A9. Block structure N-1; ends E4 CIT.
- W3 [WE] Theorem E blocks | W | A-6 | A9. Block structure N-1.
- W4 [X] a violation meeting two windows | E | J5 and (B10) | A9.
- W5 [SW] the switch | E | chain lemma and Lemma rival | P.
- L1 two regions, or a label point with a buffer point | E | table section 1(c), margins on both sides [F12] | A11.
- C2/L2 pure SAW*-shift gap, with sea | E | SAW Theorem 1 (3), (4') (A-9); SAW* carry-over (A-12); T* mod 64 invariance (A-21); census (C2) | A. Requires h >= 424. A label-free triple has no tilted rectangle with 3 or more black corners, whatever the column of W [F12].
- E1/L3 SAW*-shift | Sea(r0,g) seam | E | J1* (A-21); census (C3) | A10.
- C1/L4 buffers, chains, all-g, tails | E | J2 (A-13), Lemma sea (P), V2-2 | A, V2.

LABEL ONLY
- A1 [T1] LLL and LLLL right angles, including the two points of one label | E | rigid Theorem C, Proposition 1(b) | A9 | 0.
- A2 [R2] (o,e) label rival pairs | E | in one class: G_T independence (A-4) and Theorem C; across classes: |t| < 2h < 158h | A9, A11 | 0.
- A3 [D-4L] I.1, II(1,1), II(-1,-1), II(1,-1) with Sigma = 0, and quadruples on 3 or 4 classes | E | mixed_quadruples Theorems 1, 2 and 4, Proposition 1(c) | A9 | 0. This includes quadruples with p or q in rows 1-2 (A-24 (d)).
- A4 [D-4L] I.2, and II(1,-1) with Sigma != 0 | C | random-prime Theorems 2 and 3 | A9 | B h^(1+o(1)) in expectation; to WP (R-f).
- A5 S5, cross-block A2 pairs | E | Lemma 4(a), Proposition 1(d) | A9 | 0.

LABEL AND SEA
- S0 two shallow corners | E | (F1), sea_row3 Theorem A | A9 | 0.
- B1 [S2, S9] X1, X2 | E | block_sea Theorem 1, sea_row3 A and Corollary B, v3 A(i) | A9 | 0.
- B2 [S1, S2] Pa, and Pb with two labels | E | v3 A(i) | A9 | 0.
- [S6, S7, S8] E as an end: V, G odd in one class (parked); odd across classes (E, mod p); even (E, L-adic(i)) | v3 A(ii), A-21 | A9, A10.
- B3 [V3 SLL/SLL] | E | v3 A(iii) | A9 | 0.
- B4 [M0-M3] M1C; M2a with a label diagonal; the shallow diagonal pair; a sea point on the side | E | block_sea Theorem 2; sea_row3 A(iii) (low corners); Corollary B for an ee diagonal; odd deep rows congruent mod 8 for oo, oF, FF | A9 | 0.
- B5 [M6] in-class ee M2c | E | B3 (C1) | A9 | 0.
- B6 [M4] in-class oo M2c (R_IV) | C | B4, then Theorem IV with Lemma IV and (AP) | A9, A10 | Bad_split to WD; heights > h^(1/2)/32 to WP, O(h^(11/6) log h).
- B7 [M5] cross-class M2c, oo and ee | C | Proposition 5, Corollary B (N_h^int) | A9 | O(h^(9/5+eps)) in expectation; to WP.
- M7' [M7] M2c with the filler shallower than the label | E | rows | A11.
- M9 low M2c in row-3 types | E | (L2), (L3): same-parity row differences are multiples of 8, never 2 or 4 | A11.
- B8 [R1] rival pair with a shallow point | E | Lemma rival, J1(e), table section 3 | P, A11 | 0.
- [S13] row-3 types, W in rows 1-2 | E | sea_row3 A(ii) | A9.

LABEL AND FILLER
- D1 S2 near band | C | Theorem 1(2b) | A9 | O(h); in R-b.
- D2 T1 and CE | E/C | Theorem 1(5), Lemma 2 | A9 | exceptional labels to WP (R-d).
- D3 T2 | E | Proposition 5, i mod 32 | A9 | 0.
- D4 [D-1L3F, diagonal] one label and 3 fillers, label on the diagonal | C | Theorem 1(6), cutoff 156 rows inside T* - 320 | A9 | O(h^(3/2)); to WP.
- D4' [D-1L3F, side] label on the side | E | grid argument with R-b (V2-4); Lemma S1L (A-26, V2-5) | A9 plus V2 | 0. An {e,F,F,F} side is excluded by parity.
- D5 [T2, T5] Feo, S3, S3-low (every vertex, any blocks) | E | SAW* kill (A-12), v3 Proposition E (A-15), Q4(a) (A-24) | A | 0.
- D6 [T2] FFe, Fee, Foo with a label vertex; Foo with a filler vertex (R1) | E | v3 Theorem B with Lemma L-adic (ii) | A9, A10 | 0.
- D7 [T3] FFo with a hole vertex: parked; its V3 empty by v3 Theorem C. FFo with a label vertex: E (X = 320 >= 234) | A9, A10 | 0.
- D8 [S10, V3 cross-class] SLF-Pc is parked (Theorem B). V3 family (d) | C | Proposition D | A9 | h^(1+o(1)) in expectation; to WP (ADDED). Empty for h <= 5117 by (O1).
- D9 [S3] Pb with an odd label and a base filler | E after R2' | V2-6, A-26 | A11 | contained in R-c.
- [S4, S5, S11, S12] E as vertex with eF or a hole (rows mod 8); E as vertex with FF (W row > h, h >= 424); E as an end with a filler vertex and a label end (W below row 1); E as an end with FF (SAW Theorem 1(3)) | E | A9, A10.
- D10 [R3] (e,F) rival pairs | C | saw (i) with H0 = 210 | A9, A11 | O(h^(3/2)), constant about 5.4e4; to WP.
- D11 [M7] M2c with one label and a filler | C | saw (ii-a,b), point_counts Theorem A | A9 | O(h^(9/5+eps)); to WP (ADDED).
- D12 homogeneous Fo/Fo, Fe/Fe with d > 0 | C | finitely many shapes; R_FF^+ range 210 | A9, A11 | to WD (weight q = 1).
- D13 homogeneous Fo/Fo, Fe/Fe with d < 0 (thick) | C | saw (iii-b), Theorem IV, Lemma FF', (AP) | A9, A10 | to WD; |U'| > h^(1/2)/32 to WP.
- D14 [D-2L2F] {o,e,F,F}, and ll/FF and FF/ll in one class | E | parity; saw (iii-b) | A9 | 0. Across classes: ll/FF by two_filler Proposition 4 (A10, h >= 280); FF/ll by v3 F1 and S5 (A9).
- D15 in-class inhomogeneous 2L2F (df != 0) | E | two_filler Corollary 2 | A10 | 0 (was open as Q2).
- D16 cross-block F1, F2; F3 with n_y >= 1 or n_y = 0; mixed sides with df != 0 | E | v3 Proposition F; K4 (|Dx| <= 106h + 2 < 158h); two_filler Lemma 1 | A9, A10 | 0.
- D17 cross-class F3, n_y <= -1, odd-odd, df = 0 | C | two_filler Theorem 3(a), point_counts Theorem A, v3 reduction | A10, A9 | O(h^(9/5+eps)); to WP (was open as Q1).
- D18 the even-even analogue; even-even sides of two labels | C / E | Theorem 3(b) shapes (A10) with V2-7 for labels; Proposition 4 (A10) | O(h^(9/5+eps)); to WP.
- D19 {F,o,o,o} | E | Lemma 3L1F-a (A10); Lemma N (A11) | 0.
- D20 [D-3L1F] {F,o,e,e} and every 3L1F, in every role, class and block | E | Theorem Q3; low_rows Lemma N; table Lemma Q3 (three proofs) | A11 | 0. Needs [F1]. {F,o,o,e} and {F,e,e,e} are excluded by parity.
- D21 row-3 deep-only obstructions with p, q or W in rows 1-2 | E, or inside A3/A4/D10 | Theorem Q4 (a), (c), (d), (e) | A11 | none new.
- D22 V3 completeness | E except D8 | v3 Theorem C; table section 4 | A9, A11. Census (C4) found no V3.
- [V1] fully black tilted rectangle | E | table section 4: the triple list, plus sea_row3 A(i), (ii) for row-3 types | A11.
- [V2] fatal triples | E | the S and T cells above.
- [V3 cross-type] a shallow-W triple with a deep-W triple | E | the columns differ | A11.
- [R4] (o,F), (o,o), (e,e), (F,F) rival pairs | E | parity | A11.
- [D-4F] | E | SAW Theorem 1(4') | A9.

JUNCTIONS AND EXCEPTIONAL SETS
- E2: J2-J5 | A9.
- E3: Theorem E ends | A9.
- E4: Theorem D ends | CIT (A-26), definition-level check owed.
- E5: Corollary B exceptions, near band, low rows, T1-exceptional | O(h^(3/2)) in total; to WP.

OPEN CELLS: none (Theorem K for the amended (B7), A11).

==================================================
4. WIDTH AND EXPONENT
==================================================
- Light regions: each type has t < 16l(B+1), so its width is at most 4p · 16l(B+1) + 4A + 2(2W_h+1) + 12. Over 512 types this is 512 · 4 · 80h · 16 · 2.08h · B (1 + o(1)) = 5.45e6 B h^2 (script: 5.453e6).
- Buffers and margins: about 3 · 512 pieces of width O(h^2), so O(h^2).
- Theorem D (Theorem IV group sum): C h^2 Lambda^3 ell^C / B + h^2 ell^2. This uses kappa < infinity (K7) and the sum over light T of c_T <= C h Lambda (A-5).
- Theorem E: C h^2 Lambda^(E(a)+1) B^(-a) ell^C, with E(0.91) = 1.8588.
- Proposition partial: c0 n_rel tau*(h)^2 = h^(2 - min(eps_D, 1/6) + o(1)) = o(h^2) (V2-9).
- With B = Lambda^x the exponent is max(x, 2.8588 - 0.91x, 3 - x). Since max(x, 3 - x) >= 1.5 for every x, the minimum is 1.5, reached at x = 1.5, where the middle term is 1.4938. So M <= C h^2 Lambda^(3/2) ell^C1, and c = 1/2.
- If the sum of c_T is O(h), the third term becomes 2 - x and the optimum is x = 2.8588/1.91 = 1.4967 (not proved).

==================================================
5. STILL UNAUDITED OR UNPROVED, IN ORDER OF IMPORTANCE
==================================================
1. N-1: K8'(b) and E4. Theorem D and Theorem E blocks must place each received parity edge exactly once as a double, with singletons elsewhere and constant row-h tails. Both the criterion (A-1) and J5 need this. It is cited only, and no D block has been built at definition level.
2. Completeness of K2 and K4. The search was text-based (A-26), and a missed use of an old constant could hide a failure. The D-1L3F side cell shows the danger: it failed for k = 2 and was found only in round 11.
3. N-3: K6. The first-moment bounds must hold uniformly over class structures and psi, for the joint Markov choice of (l, p). No audit has checked this.
4. The V2 steps (V2-1 to V2-9) and the new items of the round-11 audits (the K8' assembly, the priority rule, the Theorem 3(b) label step, Lemma S1L). Each is short, but none has an independent audit. V2-4 makes S1L unnecessary.
5. The completeness of the parked-triple list (v3 Theorem C) was audited before round 10, but the round-11 Q3 audit did not re-derive it.
6. Evidence limits. Cross-class families cannot be tested for h <= 5117 (O1), and no light label survives for h <= 652 (O2). (O1) and (O2) are unaudited, but they are not load-bearing.
7. h0 is not explicit (prime number theorem in progressions).
8. Not needed: table Lemma Q4 item by item; the Heath-Brown cross-checks (undecided).
9. The exponent 1.4967 needs the sum of c_T to be O(h) (unproved).
10. m_h = O(h^2) is not addressed: heavy diagonals keep the T1 cost, and chi(Gamma) is open.

## External results used

- Henriot, corrected Theorem 5 (Math. Proc. Camb. Phil. Soc. 157 (2014) 375-377). It enters through ap_hypothesis_henriot Lemma 1, whose audit read the erratum. I did not re-read it.
- Prime number theorem in arithmetic progressions mod 5 and mod 20 (non-explicit), for the admissible (l, p).
- Quadratic reciprocity: (5/p) = (p/5) and (5/l) = (l/5).
- tau(n) << n^eps.

## Checks

By hand, I re-checked each fix as I applied it:
- [F1]: slot = rho_tau (mod 16) and n(c) = kappa - b_tau (mod 16l), from (B5).
- Table J1* and the bounds T* >= h - 186 and fillers >= h - 210.
- The grid bound y_L < T* - 72 - 2(h - T*) for D-1L3F with the label on the side. It gives 320 at D <= 124 and 444 at D = 186.
- Lemma S1L, with every valuation case.
- The Pb parity argument (even label impossible, odd label needs a base filler, 2i+1 <= 205).
- The Theorem 3(b) l-adic step.
- The g-row rival analysis.
- The AP modulus bookkeeping for the cutoff h^(1/2)/32.
- J3 in hitting-set form.
- The n_rel terms, including the omitted E_D.
- The width constant and the exponent.

Read: consolidated_board.md, audit_consolidated_board.md, obstruction_table_completeness.md, census_consolidated_board.md, audit_ap_hypothesis_henriot.md, audit_two_filler_row_lemma.md and audit_deep_layer_bh16.md in full. I read the statements of three_label_one_filler.md, low_rows_row3_types.md, two_filler_row_lemma.md and ap_hypothesis_henriot.md. I read the summaries of the polylog, v3, point_counts and additive audits, the verdict line and every serious issue of every audit, full_layout_junctions (P1)-(P12) and J1-J5, and polylog Theorem D and Lemma IV. I used the four round-11 audits given in the setting.

One script, sanity_v2.py, ran with py -I in under 60 s, in scripts_board_v2/sanity_v2.py:
- S1L residue check mod 32: 0 solutions; the b0-even control has 10240.
- g-row rival pairs for 424 <= h <= 20000: 0.
- E(0.91) = 1.8588, minimum exponent 1.5 at x = 1.5, and the light-width constant 5.453e6.
The repository was only read, and no git command was run.

## Gaps

- N-1 (most important): K8'(b) and E4. The Theorem D and Theorem E blocks must place each received parity edge exactly once as a double, with singletons elsewhere and constant row-h tails. This rests on citation only (Lemma M1, Theorem E, J5), and no definition-level D block has been built.
- Completeness of the K2 and K4 lists. The klists audit found no further failing step, but its search was a grep, so completeness cannot be certified. The D-1L3F side cell failed for k = 2 types and was found only in round 11.
- N-3: K6 uniformity. The first-moment bounds of A4, B7, D8, D17 and D18 must hold uniformly over class structures and psi, for the joint Markov choice of (l, p). No audit has checked this.
- The V2 steps written here (J3 in hitting-set form, the g-row check, the cutoff h^(1/2)/32 with moduli lcm(32, q), the near-band extension for k = 2 types, the Pb parity step, the Theorem 3(b) label step, the K8' assembly, n_rel with E_D) are not separately audited. The same holds for the new items in the round-11 audits' own derivations (Lemma S1L, the priority rule).
- v3 Theorem C (completeness of the parked-triple list, family (d)) was not re-derived in round 11. It rests on its earlier audit.
- Cross-class families are proof-only: they are vacuous for h <= 5117 (O1), and no light label survives for h <= 652 (O2). (O1) and (O2) are unaudited, though not load-bearing.
- h0 is not explicit (prime number theorem in progressions mod 5 and mod 20).
- Theorem N remains a conditional implication. m_h = O(h^2) is not addressed, and the exponent 1.4967 needs the sum of c_T over light T to be O(h), which is unproved.

## Missing estimate

No counting estimate is missing: every cell of the merged table is impossible, counted at O(h^(2-delta)) labels and relocated, or internal to a window. Three things remain: the structural fact K8'(b) and E4 about the Theorem D and Theorem E blocks, K6 uniformity, and audits of the V2 steps and of the completeness of the K2 and K4 lists.

## Next steps

- Build one Theorem D block and one Theorem E block at definition level, with their received edges, collars and row-h tails, and check K8'(b) and E4 with the census checker (core.py and checker.py in scripts_census).
- Audit K6: check that each first-moment proof (random-prime Theorems 2 and 3, Proposition 5, Proposition D, two_filler Theorem 3 with V2-7) bounds per-configuration probabilities over (l, p) for a fixed but arbitrary class structure and psi.
- Have a second reader audit V2-1 to V2-9 and the priority rule (about two pages).
- Re-run the K4 grep with the v2 constants (near band 320/444, H0 = 210, p in (40h, 80h], cutoff h^(1/2)/32) over every note cited in the hypothesis list, and record a line for each use.
- Run an exact census at h of about 1500 to 3000, where subclasses hold several labels, to test the in-class two- and three-label cells against true survivors.
- Then fold the fixes into the paper-ready write-up of Theorem N, keeping it labelled conditional until N-1 and N-3 are done.

