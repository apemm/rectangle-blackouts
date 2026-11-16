# The consolidated board, version 3

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: the board L***U as (B0) to (B10) with every fix of rounds 11 to 13, and Theorem N at exponent theta* = 1.4967429, which beats T1. N-3 is discharged by Theorem U (audited). N-1 is discharged by Theorem N1 with the two fixes of its audit applied here, and those fixes have no second reader yet. The other open items are hypothesis (H1), that the lists K2 and K4 are complete, and the short steps V3-1 to V3-5, which are not audited. NOT PROVED: m_h = O(h^2).

# Result

## Status

partial

## Summary

consolidated_board_v3: the near-goal board L***U as (B0)-(B10), with every fix from rounds 11 and 12 applied, and Theorem N (v3) at exponent theta* = 1.4967429. Theorem N now rests on one open hypothesis: the K2/K4 lists are complete. It also uses a handful of short steps that have had no second reader: the V3 steps written here, and the auditor's patches to N1, which nobody has re-read. N-1 and N-3 are discharged by Theorems N1 and U, both audited this round. NOT PROVED: m_h = O(h^2).

## Statements

THEOREM N (v3; CONDITIONAL). consolidated_board_v3, 14 November 2026. Problem 001.

Notation. Lambda = log h, ell = loglog h, E(a) = (1+3^a)/2, theta* = min over a > 0 of (E(a)+1)/(1+a) = 1.4967429, attained at a* = 0.9124154. B = ceil(Lambda^theta*). L***U is the board (B0)-(B10) in the proof field. It is L*** of consolidated_board_v2 with: the colouring law of heavy_diagonals_sharp Proposition 3 ((B1'), (B4'), (B8')); the reordered destination rule (B7); the T2 block map for the Theorem D and E blocks (block_layout_n1 as patched by its audit); and the order of choices K6-v3.

Statement. Let h >= h0 := max(10^10, h_PNT, h_D). Here 10^10 is the profile range of T1/T3 (filled_mod7 Section 3, inherited by T2), h_PNT is the non-explicit height from the prime number theorem in progressions mod 5 and mod 20 used in (B2), and h_D is the non-explicit height of Theorem D, steps (D1)-(D3). Then for every m >= M, L***U truncated to columns 1..m is a valid blackout of the h x m grid with m + q_h points, and
 M <= C h^2 (B + Lambda^(E(a)+1) B^(-a) + Lambda^2/B) ell^C1 + C h^2 ell + c0 n_rel tau*(h)^2,
 n_rel = O(h^(2-eps_D) + h^(11/6) log h + h^(9/5+2eps)),
where eps_D > 0 is the exponent of Theorem D and eps > 0 is arbitrary. At a = a* and B = ceil(Lambda^theta*) this gives
 m_h <= C h^2 (log h)^theta* (loglog h)^C1, theta* = 1.4967429 < 1.49675,
which is the near goal h^2 (log h)^(2-c) with c = 2 - theta* = 0.5032571 > 0.50325. This beats T1 (C h^2 log^2 h (loglog h)^C). The bound sum over light T of c_T = O(h) is no longer needed.

HYPOTHESES AND DEPENDENCIES (each item's source and status is in proof section 2).
(H1) OPEN HYPOTHESIS: the K2 and K4 constant lists are complete. Every step that uses an old constant (near band, H0, the prime range, the cutoff, the minimum h) has been checked against the v2/v3 constants. Two text searches found no failing step beyond the repaired D-1L3F side cell: audit_constant_lists.md, and the re-run over 25 notes in audit_consolidated_board_v2.md. A text search cannot certify completeness.
(H2) STEPS WITH NO SECOND READER, used as proved:
 - (H2a) the auditor's patches to Theorem N1: the T2 Section 1 block map, the V2/V3 argument for Claim (d) and Lemma RL via T2 Sections 2, 6 and 7, and Lemma TR' (audit of block_layout_n1, this round);
 - (H2b) the steps V3-1 to V3-5 written in proof section 1b: the reordered (B7), the K6-v3 order with Theorem U in pointwise form, Proposition 3 combined with Theorem N1 as a single instance, n_rel, and the width line with K_max = B.
 Each is short. Each applies a fix that an audit proposed or recombines audited statements.
(H3) THE AUDITED INPUTS of proof section 2 hold as audited (with their fixable gaps closed as stated there):
 - P1-P3 (paper);
 - A-1 to A-26 (rounds 9-11);
 - A-27 (V2-1 to V2-9 and Lemma S1L, audit_consolidated_board_v2.md);
 - A-28 (heavy_diagonals_sharp Lemma 1, Theorem 2 and Proposition 3, audit_heavy_diagonals_sharp.md);
 - A-30 (Theorem U in pointwise form, Lemmas U1 and U2, and Lemma U3 for in-subclass objects; audited this round);
 - A-31 (Theorem N1; audited this round);
 - the T1 chain of 2026-11-09 (T1, T2, T3, T4, each with an audit on file; no single audit reads the chain end to end).
(H4) EXTERNAL:
 - Henriot, corrected Theorem 5 (MPCPS 157 (2014) 375-377), through A-18;
 - the PNT in progressions mod 5 and mod 20;
 - quadratic reciprocity;
 - tau(n) << n^eps.
No longer hypotheses:
 - N-1 (now Theorem N1);
 - N-3 (now Theorem U);
 - N-4 (the V2 steps, now audited);
 - (AP) and Q1 to Q5. (AP) = Q5: A-18/A-19. Q1 and Q2: A-20. Q3: A-23. Q4: A-24.
NOT PROVED: m_h = O(h^2). Neither is any exponent below theta*.

## Proofs

consolidated_board_v3. It replaces consolidated_board_v2.md. All notes are in research_archive/2026-11-13 unless a path says otherwise.

STATUS KEY:
- P: paper.
- A9, A10, A11: audited with fixable gaps in round 9 or earlier, round 10, or round 11 (audit file named).
- A12: audited in round 12 (audit file named).
- R12+A: proved in round 12 and audited this round. The verdicts are quoted in section 2.
- N: proved, not audited.
- V3: a step written in this note (section 1b), not audited.
- CIT: citation only.
Fixes carried from v2 keep their tags [F1]-[F26]. New fixes are tagged [G1]-[G20].

==================================================
0. CHOICE OF COLOURING LAW (why Proposition 3, not the truncated split)
==================================================
Two audited routes give theta* = 1.4967429:
- (P3) the uniform random proper B-colouring of heavy_diagonals_sharp Proposition 3;
- (TS) the truncated additive split (B4')/(B8') of truncated_additive_split.md.
I adopt (P3). It needs fewer extra hypotheses and changes.
- (P3) keeps v2's Bad_split definition, its cutoff h^(1/2)/32 and its (AP) range unchanged. It changes only the class law and the heavy threshold (B/4). It uses one Theorem D group (rho = 2/B), so the Theorem D cost does not use Theorem S. It holds at every h >= h0. Its audit (audit_heavy_diagonals_sharp.md) found only minor gaps. The only restatement it needed, N-3 over the law of chi, is covered by Theorem U, which holds for every class datum.
- (TS) needs the following:
 - its Theorem N' restated on the v2 hypotheses (a serious gap in its audit);
 - its residual cutoff realigned from h^(1/2) to h^(1/2)/32;
 - c_T redefined as the max over tau;
 - B' = B + N0 in every count;
 - O(log B') Theorem D groups through Theorem S;
 - the additive_class_split audit fix (even rows at or above the lowest filler row go to the exceptional set).
 Its gain is asymptotic only, since N0 > B at practical h (N_FF(191) = 46 against B = 51 at h = 10^6).
Both give the same exponent. (TS) stays on file as an alternative, with its audit's corrected statement. Its Proposition O is used only in the remark of section 5.

==================================================
1. SPECIFICATION OF L***U
==================================================

(B0) PARAMETERS
- h >= h0 = max(10^10, h_PNT, h_D) [G1, from the N1 audit]. This implies h >= 424 (SAW Theorem 1, Pb, low_rows) and h >= 280 (two_filler Proposition 4).
- Lambda = log h, ell = loglog h, a = a*, B = ceil(Lambda^theta*). Stride 4 only.
- A = ceil(h/2), K = floor(h/2), W_h = floor((h-1)^2/4) + 1.
- A label is (i, j) with 0 <= i < A and 0 <= j < K. Its odd point is in row 2i+1 and its even point is in row 2j+2, in one column (a double). Put s = j - i and T = 2s + 1. There are q_h = AK labels.
- Locality (P3): every violation lies in 2W_h + 1 consecutive columns.
- S is the set of labels that are not T1-exceptional. The T1-exceptional set contains:
 - every label with a row outside [5000, h - 5000];
 - T1's O(h^(3/2)) exceptional labels (T3/T4);
 - [G2] T2's enlarged exceptional rows (2), r = s + t - u with s, t, u in the profile sea rows. There are O(1) such rows per profile, so O(h) labels.

(B1) HEAVY DIAGONALS [G3 = Proposition 3 (B1')]
- kappa_T = |D_T|, with D_T as in stride_menu.
- T is heavy if kappa_T >= B/4, and light otherwise.
- The labels of S on heavy diagonals go to the one Theorem E instance (rule 1).
- The other labels on heavy diagonals go to Proposition partial (R-d).

(B2) PRIMES, fixed first [G4]
- l is prime in (1.04h, 2.08h] with l = +-2 (mod 5).
- p is prime in (40h, 80h] with p = 3 or 7 (mod 20).
- Adm is the set of such pairs. #L >= (1/2 - o(1)) 1.04h/log h and #P >= (10 - o(1)) h/log h. gcd(p, 16l) = 1 (K3, A10).
- K6-v3, step 1: (l, p) is chosen in Adm to minimise Y(l, p) := sum over tau of sum over F in {A4-I.2, A4-II, B7, D8, D17, D18} of Y_F^tau(l, p). Here Y_F^tau is the pointwise bound of Theorem U (section 1b, V3-2).
- kappa (global) and b_tau (per type) are arbitrary fixed integers, for example 0.

(B3) REGION TYPES (unchanged)
- tau = (iota, sigma) = (i mod 32, s mod 16), giving 512 types.
- r0 = 1 if iota is odd, and r0 = 3 if iota is even.
- y_P := 2 iota + 1 (mod 64).
- [F2] tau_T := 2 sigma + 1 (mod 32).
- c_tau = 1 if T = 3 (mod 4), and c_tau = 3 if T = 1 (mod 4).

(B4) CLASSES [G5 = Proposition 3 (B4')]
- For each light T and type tau, chi_{T,tau} is a uniformly random proper B-colouring of G_T[tau]. G_T[tau] is the graph G_T of stride_menu Proposition 1' (A-4) restricted to the slots i = iota (mod 32) of diagonal T.
- The colourings are independent over (T, tau).
- The classes, which are also the final subclasses (there is no further split), are the colour classes, and colour k gets index k in {0, ..., B-1}.
- The law is well defined: the degree in G_T[tau] is at most 2|D_T ∩ 32Z| <= 2 kappa_T < B/2, so proper B-colourings exist.
- Properties (heavy Proposition 3 (a), (b); A-28):
 - every class lies in one (T, tau) and is independent in G_T;
 - each (T, tau) has at most B classes, so K_max = B;
 - for distinct slots u, v of one (T, tau), P(chi(u) = chi(v)) <= 1/(B - 2 kappa_T) < 2/B.
- The class data satisfy (Xi1)-(Xi4) of uniformity_first_moments: (Xi1) every light label is in one class; (Xi2) every class is in one diagonal; (Xi3) the indices are distinct; (Xi4) every class is G_T-independent.
- Compatibility: no downstream step uses the greedy order or K_T. The only use of c_T was Theorem IV's dyadic group cost, which is replaced by the single group of (B8). This was checked by the text searches of heavy_diagonals_sharp and of its audit (J6, threshold_families, polylog Theorem IV/D).

(B5) PLACEMENT (rule L*_l, unchanged)
- Class k of diagonal s in type tau sits at t = rho_s + 16 l k, with rho_s = p^(-1)(s - kappa) (mod 16l) and 0 <= rho_s < 16l.
- Label (i, j) of that class sits at slot n = i + p t + b_tau, in column 4n.
- [F1] rho_tau := iota + sigma - kappa + b_tau (mod 16), rho0 := rho_tau mod 4, and kappa_tau := kappa - b_tau. Every label slot of R_tau has n = rho_tau (mod 16), and n(c) = kappa_tau (mod 16l) for every class.
- Since k <= B - 1, t < 16 l B [G6, from the audit of uniformity_first_moments: K_max = B under (B4)].

(B6) FILLER LAYER (SAW*-shift, unchanged)
- T0_tau is the largest y <= h with y = y_P + 32 (if T = 3 mod 4) or y = y_P + 48 (if T = 1 mod 4), mod 64.
- D0 = h - T0_tau, in [0, 63]. T*_tau = T0_tau - 64 k_tau, with k_tau from Table J1*.
- Every deep column 4n of R_tau, margins included, that holds no label gets exactly one point, in row T*_tau - 24 + 8((n - rho0) mod 4). Such a column is an unused slot, a hole or a margin slot.
- Shallow columns x != 0 (mod 4) hold (x, r0).
- Consequences:
 - T*_tau >= h - 186, and every filler lies in [h - 210, h];
 - a filler at offset w lies in row y_P + 8(w + c_tau) (mod 64);
 - a hole has offset 0 and sits in row T* - 24.
- End phases do not re-phase the sawtooth. (Phi) adds at most 3 slots of the same sawtooth, more than 2W_h + 1 columns from every label.
TABLE J1* (unchanged, A10 via audit_consolidated_board.md). Entries are (o, kappa, j):
- h even, and row-1 types with h = 1 (mod 4): k = 0, no bad pair.
- h = 1 (mod 4), row-3 types: k = 0 bad pairs (1,2,1) at D0 = 0, (3,1,1) at 4, (2,2,1) at 8, (0,3,1) at 12, (3,2,1) at 16, (1,3,1) at 20, (2,3,1) at 28 and (3,3,1) at 36. k = 1 at D0 = 40 and 48; k = 2 at D0 = 56.
- h = 3 (mod 4), row-1 types: (2,3,3) at D0 = 4 and (3,3,3) at D0 = 12; k = 1 at D0 = 24, 32, 40 and 48.
- h = 3 (mod 4), row-3 types: the first list shifted by 2 (D0 = 2, 6, ..., 38); k = 1 at D0 = 42 and 50; k = 2 at D0 = 58.
- Every k = 0 row has a clean phase under (Phi), and every shifted row is clean at every phase.
- [F17] The shift is needed in 10 of the 64 odd-h cases: 3 + 4 + 3.

(B7) DESTINATIONS AND PRIORITY RULE [G7, V3-1]
Each label goes to exactly one destination: the first rule that fits.
1. The label is on a heavy diagonal and lies in S: it goes to Theorem E (WE).
2. The label meets R-a, R-b, R-c or R-d, all deterministic and free of chi and of (l, p): it goes to Proposition partial (WP).
3. The label is in Bad_split (B8) and not in E_D: it goes to Theorem D (WD). By rule 2 every such label lies in S, is not in R-a or R-b, and has 2i + 1 > 300. A label of Bad_split in E_D goes to WP (R-g).
4. The label meets R-e or R-f: it goes to WP.
5. Otherwise the label stays in its light region R_tau.
This is the reordering proposed by audit_consolidated_board_v2 issue 1. It contains the amendment of block_layout_n1 (rule 2' = Bad_split ∩ S minus E_D), and it also settles the R-a/R-b/R-c question that audit left undecided (closed in the N1 audit).
The criteria:
- R-a: i = 0. In row-3 types also i = 2, and j in {0, 1}.
- R-b: an endpoint row >= T*_tau - 320. In types with k_tau = 2 also an odd row >= T*_tau - 444 [F8]. [G8] The extension removes O(h) labels: at most 2 odd label rows per type in the 124-row window, and at most 16 types (row-3 types with D0 in {56, 58}).
- R-c: R2', that is 2i + 1 <= 300.
- R-d: every T1-exceptional label (heavy ones included) and every SAW Theorem 1(6) label (D4).
- R-e: the labels touched by an in-class R_IV edge with max(p_lambda, q_lambda) > h^(1/2)/32, or by an in-class R_FF^oo or R_FF^ee edge with |U'| > h^(1/2)/32.
- R-f: the labels of the counted families:
 - A4 (I.2, and II(1,-1) with Sigma != 0);
 - B7 (cross-class M2c, oo and ee);
 - D8 (V3 family (d));
 - D10 ((e,F) rival pairs);
 - D11 (label-filler M2c);
 - D17 (cross-class F3, n_y <= -1, odd-odd, df = 0);
 - D18 (the even-even analogue).
- R-g: E_D, the exceptional set of the Theorem D instance, with |E_D| <= 4 h^(2-eps_D).
Why any such rule is safe: J3 in hitting-set form (V2-1, A-27), Lemma M1 monotonicity (A-16), Proposition partial accepting any edge set (P2), and Theorem D's hypotheses (i) and (ii) surviving the removal of a deterministic set (audit_consolidated_board_v2 issue 1).

(B8) BAD_SPLIT AND THEOREM D [G9 = Proposition 3 (B8')]
- In each class of (B4), Bad_split is the shallow end of every monochromatic in-class edge of these graphs:
 - R_IV with max(p_lambda, q_lambda) <= h^(1/2)/32 (the q-end);
 - R_FF^oo and R_FF^ee with |U'| <= h^(1/2)/32 (the end at depth |U'|), in each of the 4 filler rows;
 - R_FF^+, all pairs with 0 < |Delta i| <= 210 [G10: written as Delta i, not t]. Within a class Delta i = 0 (mod 32), so there are at most 6 neighbours on each side.
- The Theorem D instance is one weighted Theorem D group, D = {all light T} with |D| <= h and rho = 2/B >= Lambda^(-C'). It receives Y := Bad_split minus (R-a ∪ R-b ∪ R-c ∪ R-d) and places Y minus E_D.
- Hypothesis (i) of Theorem D, weighted: P(f in Bad_split) <= (2/B) times the sum over q in Q_T of c_q 1[q | u_f or q | delta'(f)]. This is heavy Proposition 3 (b) and (c) with a union bound over the designated-end edges, indexed as in Theorem IV and Lemma FF'.
- [F14] c_q is counted with multiplicity over lambda.
- [G11, audit_consolidated_board_v2 issue 2] For R_IV, q is odd, because u = (2i + 1 - r0)/2 is odd. For R_FF the per-diagonal density is gcd(32, m)/m <= 32/|U'| with m = |U'|/gcd(2, |U'|). So kappa_IV and kappa_FF are finite, the latter larger by a factor of at most 32.
- Hypothesis (ii): Bad_split ∩ T is a function of (chi_{T,tau}) over tau, so it is independent across T. Removing the deterministic set of rule 2 keeps (i) and (ii).
- [F3, V2-3] Modulus: each event 'f has an edge at height q' is a union of O(1) residue classes of i modulo lcm(32, q) <= 32q <= h^(1/2). That is inside ap Lemma 4 and Theorem D-weighted (A-18).
- The blocks follow Theorem N1 as patched (BL, below), right of z with row-h tails.

(B9) BUFFERS AND ENDS (unchanged)
- Buffer row g(h) = h for h even, h - 1 for h = 1 (mod 4), and h - 3 for h = 3 (mod 4) (V2-2).
- Pieces Sea(r0, g) and all-g, each 2W_h + 1 wide, in the order of (P8): row-1 tail | Sea(1,g) | the 256 row-1 types | Sea(1,g) | all-g | Sea(3,g) | the 256 row-3 types | Sea(3,g) | all-g | Sea(1,g) | row-1 tail.
- [F12] Margins: R_tau has 2W_h + 1 columns of pure SAW*-shift before its first and after its last label column, plus at most 3 slots for (Phi).
- End phases follow Table J1* and (P9).

(B10) GLUING
- There is one switch z: row 1 left of z, row h right of z, outside the windows.
- Every WD and WE window lies right of z, at least 2W_h + 1 columns from z and from every other window (N1 BL6).
- The WP instances are case (a) for even h, inside the row-1 tail, and case (c) for odd h, with switch z.
- Gluing is by J5 (A-13). The board is truncated to columns 1..m.

BLOCK LAYOUT OF THE WD AND WE INSTANCES (Theorem N1, patched) [G12-G16]
- Profiles are pi = (L, F, H, g) as in filled_mod7 (1)-(3), (7)-(9), with sea s_pi(x) = F if 7 | x, L if chi_7(x) = -1, and H if chi_7(x) = 1.
- [G12, serious fix of the N1 audit] The profile map is T2 Section 1's:
 - L is the unique odd L in [1, 14] with L = a_e (mod 7);
 - for a mixed-residue label (a != b mod 7), g = (b - a)/5 (mod 7);
 - a zero-residue label (a = b mod 7) gets any nonzero g and goes to a separate zero-residue block;
 - no block mixes the two kinds.
- Blocks are B_{I, pi, type}, indexed by instance I in {E, D}, profile and block type in {mixed, zero}. There are O(1) blocks per instance, each with its own collars.
- [G13] Classes inside a block are the dyadic classes (2^(k-1), min(2^k, Lambda^3)] of T1's weight v_pi, then the coarse groups (W_k, W_{k+1}] with W_0 = Lambda^3 and W_{k+1} = W_k^(4/3). Their endpoints are consecutive.
- BL1: each class c has a slot count N_c >= |c| and an injective centre map X_c avoiding T2's events, with T2's slot counts (T1 (8), Theorem E (E4)-(E5), Theorem D (D4)).
- BL2: core K_c = [x_c, x_c + 7N_c - 1] with 7 | x_c. Column x_c + 7X_c(e) holds exactly the two points of e. Every other column x holds s_pi(x), so unchosen slots keep F.
- BL3: consecutive cores are separated by at least 2W_h + 1 columns of s_pi.
- BL4: right collar, in order away from the core: P (2W_h + 1 columns of s_pi); Phi (2W_h + 1 columns of s_pi with H at the multiples of 7); C_H, ..., C_{h-1} (2W_h + 1 columns each of constant rows H, ..., h-1); then row h. The left collar is the mirror image.
- BL5: the block is: row h | left collar | cores and separations | right collar | row h. Its window is U = [a, b].
- BL6: as in (B10).

ORDER OF RANDOM CHOICES (K6-v3) [G4, V3-2]
1. (l, p) is the deterministic minimiser of Y(l, p) over Adm (B2).
2. chi is drawn from the product law of (B4), conditioned on the Theorem D event of the single group. That event has positive probability, by the weighted Theorem D (A-16, A-18) under hypotheses (i) and (ii) of (B8). Neither hypothesis involves (l, p).
3. The WE and WD centre maps are chosen by T2's local lemma. They use only the received label sets and the profiles, never (l, p).
Since Theorem U holds pointwise, X_F <= Y_F^tau(l, p) for every outcome of chi. This order needs neither Markov's inequality nor the D-block part of Lemma U3.

THE K-ITEMS IN v3
- K1: [F1].
- K2: complete as far as the grep reached (A-26). This is hypothesis (H1).
- K3: the admissible-pair count (A10).
- K4: the corrected list of v2. Re-run over 25 notes with the v2 constants in audit_consolidated_board_v2 (A12), with no failure beyond the repaired D-1L3F side cell. Completeness is (H1). Its items:
 - fillers in [h - 210, h], and T* >= h - 186;
 - Theorem 1(6) cutoff y_D - 156 >= T* - 180;
 - FFo with a label vertex needs X >= 234 (320 used);
 - Pb with one label needs 2i + 1 <= 205;
 - Pc with a filler vertex: g < -296;
 - saw (i) and BH16 A5: H0 = 210;
 - the R_FF^+ range 210;
 - v3 (F1) |delta| >= 39h; (F2) |n_x| < h/158; A(ii) |a| < h/158; (F3) with n_y >= 1 empty, because |Dx| <= 106h + 2 < 158h; Foo with a label vertex |alpha| < h/600;
 - Proposition D: one prime factor in (40h, 80h];
 - Proposition E: W row >= 309;
 - two_filler Proposition 4: h >= 280;
 - D-1L3F side: y_L < T* - 72 - 2(h - T*), under R-b with the k = 2 extension.
- K5: buffer rows by J1* and J2.
- K6: K6-v3 above.
- K7: Theorem IV weights:
 - R_IV by Lemma IV, with the large-lambda count p < 21 be^3 [F15];
 - R_FF by Lemma FF', with [G11];
 - R_FF^+ with q = 1;
 - cutoff h^(1/2)/32 throughout.
- K8': Theorem N1(f), as patched.
- K9: LAD not adopted. K10: additive Theorem 5 not adopted.

==================================================
1b. STEPS AND CITED THEOREMS
==================================================

V3-1 (reordered (B7); V3). Partition: each label takes the first rule that fits, and rule 5 is the default. The heavy and light diagonals are disjoint. Rule 1 and rule 3 receive only labels of S: rule 1 by definition, and rule 3 because R-d, which contains every T1-exceptional label, comes first in rule 2. Rule 3's set Y \ E_D equals the N1 instance set R_D = (Bad_split ∩ S) \ E_D minus the deterministic set R-a ∪ R-b ∪ R-c. Theorem D's hypotheses (i) and (ii) are monotone under deleting a deterministic set, so Theorem D applies to Y. Rule 2 moves only labels already counted in n_rel (O(h^(3/2))). J3 (V2-1) needs only that the labels leaving R_tau hit every violating Lambda. Bad_split, R-e and R-f do so whichever destination receives them. So region validity does not depend on the order.

V3-2 (Theorem U pointwise; K6-v3; V3, from R12+A).
- Source: uniformity_first_moments.md, Theorem U, Lemmas U1 to U3. In the pointwise form proposed by its audit, for each family F in R_tau:
 X_F(Xi, kappa, b; l, p) <= Y_F^tau(l, p) := lam_F Phi_F #{sigma in Sigma_F^tau realisable at (l, p)},
 for every class datum Xi with (Xi1)-(Xi3) and every kappa, b.
- The averages over Adm (per type) are:
 - A4 I.2: h^(1+o(1)) (type both; the factor B drops out);
 - A4 II(1,-1) with Sigma != 0: h^(1+o(1));
 - B7: C h N_h^int/min(#L, #P) = O(h^(9/5+eps) log h) (odd-odd p-type, even-even l-type);
 - D8: 2h h^(1+o(1))/#P = h^(1+o(1)) (p-type);
 - D17: 2h |Sigma_tau|/#P with |Sigma_tau| <= 4 · 4 · h^(o(1)) · sum over Q < 3h of |E0(Q)| (4 filler rows per type, at most 4-to-1) [G17], so O(h^(9/5+eps) log h) (p-type);
 - D18: 4h |Sigma_tau|/#L = O(h^(9/5+eps) log h) (l-type).
- Then min over Adm of Y <= average <= 512 · C h^(9/5+2eps). The factor 512 enters only here [G17].
- Fixes applied from the U audit:
 - U1 size facts: |DM| <= |Dx|/4 + |Di| and |Dn| <= |DM| + |Ds|. Both are below h^2/8 + 3h/2, which is below (1.04h)^2 and (40h)^2. A nonzero integer below (1.04h)^2 has at most one prime factor in (1.04h, 2.08h], and one below (40h)^2 has at most one in (40h, 80h] (checked: h^2/8 + 3h/2 < (1.04h)^2 for all h >= 10).
 - D18: |Dn| <= h^2/8 + h/2 + 1, not h^2/16 + ....
 - B7: r0 is fixed by the type, so the factor 2 goes.
 - [G18] Transfer of the shape counts from p in (20h, 40h] to (40h, 80h]: each audited count is an upper bound over a superset of the v3 shapes. The shape sets are cut out by lower bounds such as |Delta| >= 4(p - A + 1) or |Dx| >= 158h, or by the upper bounds they imply (|a| < h/632, |Sigma| < h/312). Those sets only shrink as p grows, and no count uses an upper bound on p. #P grows from about 5h/log h to about 10h/log h. The D8 count h tau^2 does not involve p.
- D11 is deterministic. The filler at slot offset w lies in row T* - 24 + 8(w mod 4), and label slots are rho_tau (mod 16) by [F1]. So the D11 hit set depends only on rows and on the type, with at most (h/2) sum |E0(Q)| = O(h^(9/5+eps)) labels. D11 is not part of Y.
- V2-7's step 'Ds = Dn (mod p), so L2 is unique' is replaced by U1(b): L2's point determines L2 [G19].
- Lemma U3 holds for the in-subclass objects: R_IV, R_FF, Bad_split and R-e are translates of (l, p)-free pictures. Its claim about the D-block event is not used, because of the pointwise order.
- Law coverage: Theorem U covers every (l, p)-free law with (Xi1)-(Xi3), including the uniform proper B-colouring of (B4) (U audit). (Xi4) is used only by the deterministic exclusions (for example b != 0 in I.2), and (B4) gives it.

V3-3 (Proposition 3 with Theorem N1 as a single instance; V3).
- Theorem N1's instances become one Theorem E instance (R_E = heavy labels in S) and one Theorem D instance (R_D = Y \ E_D).
- Its claims (a)-(f) do not use the number of Theorem D groups. Claim (b) uses only that the classes partition each R_{I,pi,type}, which [G13] gives.
- The R_j-independence check of N1 section 8 becomes: Y depends only on chi and on deterministic sets, so it is fixed after step 2 of K6-v3.

V3-4 (n_rel; V3). n_rel is the sum of:
- O(h): R-a; R-b including the k = 2 extension [G8]; R-c; D1 (inside R-b); D9 (inside R-c); the labels with a row outside [5000, h - 5000]; T2's rows (2);
- O(h^(3/2)): D4; D10 (constant about 5.4e4); T1's exceptional labels;
- h^(1+o(1)): A4 and D8 (no factor B; Theorem U);
- O(h^(9/5+2eps)): B7, D17 and D18 (K6-v3 step 1), and D11 (deterministic);
- O(h^(11/6) log h): R-e (V2-3; the bound is over all label pairs of a (T, tau), so it holds for every chi);
- <= 4 h^(2-eps_D): E_D (one group, so no log B factor).
So n_rel = O(h^(2-eps_D) + h^(11/6) log h + h^(9/5+2eps)), and c0 n_rel tau*(h)^2 = h^(2 - min(eps_D, 1/6) + o(1)) = o(h^2).

V3-5 (width; V3). See section 4.

CITED THEOREMS USED AS PROVED (statements as audited):
- Theorem N1 (block_layout_n1.md; R12+A, correct_with_fixable_gaps; serious gaps closed by [G12] and [G14]). Under (B7) as above, every WD and WE block satisfies:
 - (a) every column is a singleton or a double, and the doubles are exactly the label columns, carrying the parity edges;
 - (b) the label-to-column map is injective;
 - (c) the block is constant row h outside its window (E4);
 - (d) with infinite row-h tails, the block has no (V1)-(V5) violation;
 - (e) J5 glues it;
 - (f) K8' holds for the whole board.
 [G14] Claim (d) and Lemma RL use T2's argument, not 'T1 excludes every three-black tilted rectangle':
 - the only three-black tilted rectangles are T2's allowed triangles (a high-sea root and two mixed-residue labels);
 - by T2 (4), W lies in a nonzero-residue column, which holds s_pi = L inside K_c^+, and W has the parity of L, so the triangle is parked (V2);
 - no two allowed triangles on the same two labels share W (T2 Section 2);
 - every other V3 pair is a six-cell event on 3 or 4 labels, avoided by the placement (T2 (15)-(17));
 - a mixed pair with a common black corner is a four-cell support, already among the events;
 - I2 is T2's events with T2's slot counts, and compatible (5) is kept only for higher-arity sums.
 [G15, Lemma RL restated] E_J depends only on X_c restricted to J and on s_pi with F at every other period-zero column. The W of an allowed triangle never lies in a period-zero column, so deleting labels never unparks a triangle.
 [G16, Lemma TR' for adjacent rows] Adjacent rows (y, y+1) on contiguous column intervals form a monotone chain. Lemma chain applies, with x -> -x for the left collar. A rival pair would need j(j+1) to be a square, but j^2 < j(j+1) < (j+1)^2.
 Lemma TR (opposite-parity rows with 2y0 - y1 < 1 and 2y1 - y0 > h) covers Phi | C_H. Lemma C (the label-free block is clean) is unchanged.
- Theorem U (uniformity_first_moments.md; R12+A, correct_with_fixable_gaps): as in V3-2.
- heavy_diagonals_sharp Proposition 3 (A12, audit_heavy_diagonals_sharp.md): (a)-(d) as used in (B1), (B4) and (B8), and in section 4.
- heavy_light Theorem 1(b) (A9): H_d(B/4) <= C_a 4^a h Lambda^(E(a)-1) B^(-a) for every fixed a > 0.
- Theorem E (t1_cost_decomposition, A9): cost C(Delta h Lambda^2 ell^C1 + h^2 ell) for Delta heavy diagonals, with row-h ends.
- Weighted Theorem D (polylog_relocation_diluted A9; ap_hypothesis_henriot A10): cost C(rho kappa |D| h Lambda^2 ell^C1 + h^2 ell), with exceptional set |E_D| <= 4 h^(2-eps_D).
- V2-1 to V2-9 and Lemma S1L (A-27): all re-derived correct in audit_consolidated_board_v2.

==================================================
2. HYPOTHESIS AND DEPENDENCY LIST
(input | source | statement used | status | audit file)
==================================================
PAPER
- P1 | sec2_prelim.tex, sec5_threshold.tex | Lemma mixedeq, the reduction lemma, Lemma rival, Lemma sea, Lemma chain, Lemma diff, criterion and girth lemmas | P.
- P2 | sec5_threshold.tex | Proposition partial, cases (a) and (c): any n edges in width c0 n tau*(h)^2 | P.
- P3 | sec5_threshold.tex | locality 2W_h + 1 | P.

T1 CHAIN (research_archive/2026-11-09; CLAIM_LEDGER rows T1-T4)
- T-1 | two_moment_threshold_refinement.md | slot counts (8) | THM-EXT, audit two_moment_threshold_independent_audit.md.
- T-2 | full_problem_push/safe_triangle_pair_first_moment.md | Section 1 profile map, Section 2 allowed triangles, (2), (4), (15)-(17), Section 7 local lemma | THM-EXT, audits safe_triangle_first_moment_independent_audit.md and safe_triangle_pair_third_audit.md.
- T-3 | filled_mod7_profile_cover.md | profiles, one-label substitution, hole-choice collars, h >= 10^10 | THM, audit filled_mod7_independent_audit.md.
- T-4 | compatible_profile_threshold.md | exceptional roles, the O(h^(3/2)) exceptional set, (5) for higher arity | THM-EXT, audit compatible_profile_threshold_independent_audit.md.
- Caveat: no single audit reads the chain end to end (ledger, section A).

AUDITED BEFORE ROUND 10 (A9)
- A-1 | block_sea_classification | criterion (V1)-(V5) under K8'; Theorems 1 and 2 | audits_rigid_mixed_sea.md.
- A-2 | rigid_layout_cross_block | Theorem C, Proposition R | audits_rigid_mixed_sea.md.
- A-3 | mixed_quadruples_blocks | Theorems 1-4 | audits_rigid_mixed_sea.md.
- A-4 | stride_menu | Proposition 1' (G_T) | audits_stride_menu_and_gamma.md.
- A-5 | heavy_light_split | Theorem 1(b) (Rankin bound for H_d) and Theorem S. Theorem S is no longer used in the cost | audit_heavy_light_split.md.
- A-6 | t1_cost_decomposition | Theorem E (E1)-(E5) | audit_t1_cost_decomposition.md.
- A-7 | sea_row3_split | Theorem A ((H1)-(H4)), Corollary B | audit_sea_row3_split.md. The g issue is met by V2-2.
- A-8 | sea_census_rigid | B1-B4 (R_IV, B3(C1)) | audit_sea_census_rigid.md.
- A-9 | deep_layer_sawtooth | SAW Theorem 1 (1)-(6), Lemmas 2-4, Proposition 5 | audit_deep_layer_sawtooth.md.
- A-10 | ratio_graph_r_iv | Lemma 2, Corollary 3, Theorem 4 | audit_ratio_graph_r_iv.md.
- A-11 | threshold_families_random_prime | L*_l; Proposition 1(b)-(d); Theorems 2 and 3; Proposition 5 | audit_threshold_families_random_prime.md.
- A-12 | saw_residual_families | SAW*; Feo kill (iii-a); (i); (ii-a,b); (iii-b) | audit_saw_residual_families.md.
- A-13 | full_layout_junctions | J1-J5, (P7)-(P9) | audit_full_layout_junctions.md.
- A-14 | point_counts_power_saving | Theorem A, Corollaries B and C | audit_point_counts_power_saving.md.
- A-15 | v3_and_cross_block | Theorems A-C, Propositions D-F | audit_v3_and_cross_block.md. Carried to (40h, 80h] by K4 and [G18].
- A-16 | polylog_relocation_diluted | Lemma M1; Theorem D; Lemma IV; Theorem IV's bookkeeping | audit_polylog_relocation_diluted.md.
- A-17 | additive_class_split | Lemmas 1, 2 and 4 | audit_additive_class_split.md.

ROUND 10 (A10)
- A-18 | ap_hypothesis_henriot | Lemmas 1-4, Corollary (AP), Theorem D-weighted | audit_ap_hypothesis_henriot.md.
- A-19 | the same | (AP) = Q5 | the same.
- A-20 | two_filler_row_lemma | Lemma 1; Corollary 2; Theorem 3(a); the 3(b) shapes; Proposition 4 | audit_two_filler_row_lemma.md.
- A-21 | consolidated_board | Lemma J1* and Table J1*; Lemma L-adic; Lemma FF'; Lemma 3L1F-a; K1-K4 arithmetic | audit_consolidated_board.md.
- A-22 | deep_layer_bh16 | A1, A2, A3 (constant kappa_tau) | audit_deep_layer_bh16.md.

ROUND 11 (A11)
- A-23 | three_label_one_filler | Lemma N; Theorem Q3 | audit_three_label_one_filler.md.
- A-24 | low_rows_row3_types | Lemmas LR, S and N; Q4 (a), (c), (d); (b) restricted to row-3 types; (e) | audit_low_rows_row3_types.md.
- A-25 | obstruction_table_completeness | Theorem K; Lemma Q3; sections 0-6. Lemma Q4 is not used | audit_obstruction_table_completeness.md.
- A-26 | constant lists | K2 (grep); K4 corrected; R2' sufficiency | audit_constant_lists.md. [G20] Lemma S1L, the Theorem 3(b) label step, R2' sufficiency and the Pb parity step were derived inside that audit. They count as 'A11-derivation; re-derived in audit_consolidated_board_v2'. E4 is now Theorem N1(c).

ROUND 12 (A12, R12+A)
- A-27 | consolidated_board_v2 | V2-1 to V2-9, Lemma S1L, width, exponent | A12, audit_consolidated_board_v2.md (correct_with_fixable_gaps; its serious issue is fixed by (B7)).
- A-28 | heavy_diagonals_sharp | Lemma 1, Theorem 2 (kappa-heaviness), Proposition 3 (a)-(d), Proposition 4 (a), (b) | A12, audit_heavy_diagonals_sharp.md (all gaps minor). Propositions 5 and 6 and Route L are not audited and are not used.
- A-29 | truncated_additive_split | Lemmas A-D, Proposition O | A12, audit_truncated_additive_split.md. NOT USED in the board; only Proposition O, with its qualifier, appears in a remark.
- A-30 | uniformity_first_moments | Lemmas U1 and U2, Theorem U (pointwise form), Lemma U3 for in-subclass objects | R12+A. Verdict this round: correct_with_fixable_gaps, all issues minor. The fixes are applied in V3-2.
- A-31 | block_layout_n1 | Theorem N1, Lemmas TR, C and RL | R12+A. Verdict this round: correct_with_fixable_gaps; two serious gaps (the framework mismatch and the profile map), both fixable. The fixes are applied as [G12]-[G16]. The patched text is the auditor's, and nobody has re-read it (H2a).
- gamma_two_split_primes_w | Theorem W | A12, audit_gamma_two_split_primes_w.md. Not used by the board (far goal only).

WRITTEN HERE (V3; not audited) = (H2b)
- V3-1 to V3-5.

NOT AUDITED, NOT LOAD-BEARING
- census_large_heights (P1)-(P3) and (R1)-(R6); census_consolidated_board (O1), (O2); relocation_price_floor Theorem R and Corollaries R1 and R2.

OPEN HYPOTHESIS
- (H1) completeness of K2/K4.

EXTERNAL
- Henriot, New Theorem 5 (MPCPS 157 (2014) 375-377), through A-18;
- PNT in progressions mod 5 and mod 20;
- quadratic reciprocity;
- tau(n) << n^eps.
- For the sharpness remark only: the fundamental lemma of sieve theory in dimension 1/2 (theorem number not checked) and Mertens' theorem for primes = +-1 (mod 5).

==================================================
3. MERGED OBSTRUCTION TABLE
(cell | verdict E/C/W | source | status | labels hit, destination)
E = impossible; C = counted and relocated; W = internal to a certified window. Table T names are in brackets.
==================================================
WINDOWS AND CHAIN
- W1 [WP] Proposition partial | W | P2 | P.
- W2 [WD] Theorem D blocks | W | N1 (a)-(e) with [G12]-[G16]; T2's allowed triangles are parked (T2 (4)); V3 by T2 (15)-(17) | R12+A (patched), A10, A9.
- W3 [WE] Theorem E blocks | W | the same, with the T2 map | R12+A (patched), A9.
- W4 [X] a violation meeting two windows | E | J5, BL6, (B10) | A9, R12+A.
- W5 [SW] the switch | E | Lemma chain, Lemma rival | P.
- L1 two regions, or a label point with a buffer point | E | table section 1(c), margins [F12] | A11.
- C2/L2 pure SAW*-shift gap with sea | E | SAW Theorem 1 (3), (4'); SAW* carry-over; T* mod 64 invariance; census (C2), (R6) | A9, A10. Needs h >= 424. It also covers Table T's T4 (FFF) and M8 (M2c with FF) [audit_v2 issue 3].
- E1/L3 SAW*-shift with a Sea(r0, g) seam | E | J1*; census (C3) | A10.
- C1/L4 buffers, chains, all-g, tails | E | J2, Lemma sea, V2-2 | A9, A12.

LABEL ONLY
- A1 [T1] LLL and LLLL right angles | E | rigid Theorem C, Proposition 1(b) | A9 | 0.
- A2 [R2] (o,e) label rival pairs | E | in one class: G_T independence (Xi4) and Theorem C; across classes: |t| < 2h < 158h | A9, A11 | 0.
- A3 [D-4L] I.1, II(1,1), II(-1,-1), II(1,-1) with Sigma = 0, and 3- or 4-class quadruples | E | mixed_quadruples Theorems 1, 2 and 4; Proposition 1(c); A-24 (d) | A9 | 0.
- A4 [D-4L] I.2, and II(1,-1) with Sigma != 0 | C | threshold Theorems 2 and 3; Theorem U (type both) | A9, R12+A | h^(1+o(1)) at the chosen (l, p); to WP (R-f).
- A5 S5, cross-block A2 pairs | E | Lemma 4(a), Proposition 1(d) | A9 | 0.

LABEL AND SEA
- S0 two shallow corners | E | (F1), sea_row3 Theorem A | A9 | 0.
- B1 [S2, S9] X1, X2 | E | block_sea Theorem 1; sea_row3 A and Corollary B; v3 A(i) | A9 | 0.
- B2 [S1, S2] Pa, and Pb with two labels | E | v3 A(i) | A9 | 0.
- [S6, S7, S8] E as an end: V, G odd in one class (parked); odd across classes (E mod p); even (E, L-adic (i)) | v3 A(ii), A-21 | A9, A10.
- [S10] SLF-Pc parked (v3 Theorem B). With G a base: E, since a = 0 (mod 4) | A9 [added per audit_v2 issue 3]. The V3 cross-class part is D8.
- B3 [V3 SLL/SLL] | E | v3 A(iii) | A9 | 0.
- B4 [M0-M3] | E | block_sea Theorem 2; sea_row3 A(iii); Corollary B; odd deep rows congruent mod 8 | A9 | 0.
- B5 [M6] in-class ee M2c | E | B3 (C1) | A9 | 0.
- B6 [M4] in-class oo M2c (R_IV) | C | B4, Theorem IV, Lemma IV, (AP); the (B4) law | A9, A10, A12 | Bad_split to WD (rule 3); heights > h^(1/2)/32 to WP (R-e), O(h^(11/6) log h).
- B7 [M5] cross-class M2c, oo and ee | C | Proposition 5, Corollary B, Theorem U | A9, R12+A | O(h^(9/5+2eps)); to WP.
- M7' [M7] M2c with the filler shallower than the label | E | rows | A11.
- M9 low M2c in row-3 types | E | (L2), (L3) | A11.
- B8 [R1] rival pair with a shallow point | E | Lemma rival, J1(e) | P, A11 | 0.
- [S13] row-3 types, W in rows 1-2 | E | sea_row3 A(ii) | A9.

LABEL AND FILLER
- D1 S2 near band | C | Theorem 1(2b) | A9 | O(h); in R-b.
- D2 T1 and CE | E/C | Theorem 1(5), Lemma 2 | A9 | exceptional labels to WP (R-d).
- D3 T2 | E | Proposition 5, i mod 32 | A9 | 0.
- D4 [D-1L3F, diagonal] | C | Theorem 1(6), cutoff inside T* - 320 | A9 | O(h^(3/2)); to WP (R-d).
- D4' [D-1L3F, side] | E | V2-4 (grid, with the R-b extension) and Lemma S1L | A11-derivation, re-derived in audit_consolidated_board_v2 (A12) [audit_v2 issue 3]; census (R5) | 0. {e,F,F,F} is excluded by parity.
- D5 [T2, T5] Feo, SAW-S3 and SAW-S3-low (SAW triple names, renamed so they do not collide with Table T's S3) | E | SAW* kill (A-12), v3 Proposition E, Q4(a) | A9, A11 | 0.
- D6 [T2: Fee, Foo; T3: FFe] FFe, Fee and Foo with a label vertex; Foo with a filler vertex (R1) | E | v3 Theorem B with Lemma L-adic (ii) | A9, A10 | 0.
- D7 [T3] FFo with a hole vertex: parked, its V3 empty (v3 Theorem C). FFo with a label vertex: E (X = 320 >= 234) | A9, A10 | 0.
- D8 [V3 cross-class] family (d) | C | Proposition D; Theorem U (p-type) | A9, R12+A | h^(1+o(1)); to WP. Empty for h <= 5117 (O1).
- D9 [S3] Pb with an odd label and a base filler | E after R2' | V2-6 | A12 | inside R-c (2i + 1 <= 205).
- [S4, S5, S11, S12] E as vertex with eF or a hole (rows mod 8); E as vertex with FF (W row > h); E as an end with a filler vertex and a label end (W below row 1); E as an end with FF | E | A9, A10.
- D10 [R3] (e,F) rival pairs | C | saw (i), H0 = 210 | A9, A11 | O(h^(3/2)); to WP. Census: 10% to 49% of FAITHFUL labels per type.
- D11 [M7] M2c with one label and a filler | C, deterministic | saw (ii-a,b), point_counts Theorem A and Corollary C(2); V3-2 | A9, R12+A | O(h^(9/5+eps)); to WP.
- D12 homogeneous Fo/Fo, Fe/Fe with d > 0 | C | finitely many shapes; R_FF^+ with |Delta i| <= 210 | A9, A11 | to WD (q = 1). Census (R3), (R4): every instance found is an R_FF^+ edge.
- D13 homogeneous Fo/Fo, Fe/Fe with d < 0 | C | saw (iii-b), Theorem IV, Lemma FF', (AP), [G11] | A9, A10, A12 | to WD; |U'| > h^(1/2)/32 to WP.
- D14 [D-2L2F] {o,e,F,F}; ll/FF and FF/ll in one class | E | parity; saw (iii-b); across classes: two_filler Proposition 4 (h >= 280), v3 F1 and S5 | A9, A10 | 0.
- D15 in-class inhomogeneous 2L2F (df != 0) | E | two_filler Corollary 2 | A10 | 0.
- D16 cross-block F1, F2; F3 with n_y >= 0; mixed sides with df != 0 | E | v3 Proposition F; K4; two_filler Lemma 1 | A9, A10 | 0.
- D17 cross-class F3, n_y <= -1, odd-odd, df = 0 | C | two_filler Theorem 3(a); point_counts Theorem A; Theorem U (p-type) | A10, R12+A | O(h^(9/5+2eps)); to WP.
- D18 the even-even analogue | C / E | Theorem 3(b) shapes, V2-7 with U1(b) [G19], Proposition 4; Theorem U (l-type) | A10, A12, R12+A | O(h^(9/5+2eps)); to WP.
- D19 {F,o,o,o} | E | Lemma 3L1F-a; Lemma N | A10, A11 | 0.
- D20 [D-3L1F] every 3L1F | E | Theorem Q3; Lemma N; table Lemma Q3 | A11 | 0. Needs [F1].
- D21 row-3 deep-only obstructions with p, q or W in rows 1-2 | E, or inside A3/A4/D10 | Q4 (a), (c)-(e) | A11 | none new.
- D22 V3 completeness | E except D8 | v3 Theorem C; table section 4 | A9, A11. Table T's 'h < 2560' should read 'h <= 5117' [audit_v2 issue 5].
- [V1] fully black tilted rectangle | E | table section 4; sea_row3 A(i), (ii) | A11.
- [V2] fatal triples | E | the S and T cells above.
- [V3 cross-type] | E | the columns differ | A11.
- [R4] (o,F), (o,o), (e,e), (F,F) rival pairs | E | parity | A11.
- [D-4F] | E | SAW Theorem 1(4') | A9.

JUNCTIONS AND EXCEPTIONAL SETS
- E2: J2-J5 | A9.
- E3: Theorem E ends | N1(c), (e) | R12+A, A9.
- E4: Theorem D ends | N1(c), (e) | R12+A (was CIT).
- E5: Corollary B exceptions, near band, low rows, T1-exceptional (with T2's rows (2)) | O(h^(3/2)); to WP.

OPEN CELLS: none (Theorem K for the amended (B7), A11). Changing the class law does not open a cell. Every in-class E cell uses only G_T-independence (Xi4), at most B classes per (T, tau), and the mod-16l position rule (audit_heavy_diagonals_sharp, compatibility check).

==================================================
4. WIDTH AND EXPONENT (V3-5)
==================================================
- Light regions. Each type has t < 16lB, so its width is at most 4p · 16lB + 4A + 2(2W_h + 1) + 12. Over 512 types this is at most 512 · 4 · 80h · 16 · 2.08h · B (1 + o(1)) = 5.453e6 B h^2 (script: 5452595.2).
- Buffers, margins and sea pieces: about 3 · 512 pieces of width O(h^2), so O(h^2).
- Theorem E. There are Delta = H_d(B/4) <= C_a 4^a h Lambda^(E(a)-1) B^(-a) heavy diagonals (heavy_light Theorem 1(b)), and 4^(a*) = 3.54. The cost is C h^2 Lambda^(E(a)+1) B^(-a) ell^C1 + C h^2 ell.
- Theorem D (one group, rho = 2/B, |D| <= h, kappa finite): C h^2 Lambda^2 ell^C1/B + C h^2 ell.
- Collars and separations of the N1 blocks: O(1) blocks per instance. Each block has O(1) collar stages (h - H = O(1)) and O(ell) class separations, each of width O(h^2). Total O(h^2 ell).
- Switch and tails: O(h^2).
- Proposition partial: c0 n_rel tau*(h)^2 = o(h^2) (V3-4).
Total: M <= C h^2 (B + Lambda^(E(a)+1) B^(-a) + Lambda^2/B) ell^C1 + C h^2 ell + o(h^2).
Exponent. Put B = Lambda^x. The exponent is max(x, E(a) + 1 - a x, 2 - x).
- At a = a* = 0.9124154 and x = theta* = (E(a*)+1)/(1+a*) = 1.4967429, the middle term is theta*(1 + a*) - a* theta* = theta*.
- The last term, 2 - theta* = 0.503, is below x.
- Legendre duality (audit_heavy_diagonals_sharp): min over a of (E(a) + 1 - a x) = 2 - phi(x), and min over x of max(x, 2 - phi(x)) = theta*. So theta* is optimal for this three-term trade-off.
- A grid check gave 1.49675 at x = 1.49674.
Hence M <= C h^2 (log h)^theta* (loglog h)^C1.
Since a truncation with m >= M columns has m + q_h points (one per column plus q_h doubles, every double in a column <= M), f(h, m) >= m + q_h for m >= M. With the paper's upper bound f(h, m) <= m + q_h, this gives m_h <= M.
Comparison: v2 had max(x, 2.8588 - 0.91x, 3 - x) = 1.5 at x = 1.5. The Lambda^3/B term of the greedy split with psi becomes Lambda^2/B under (B4).
Rounding [audit_heavy_diagonals_sharp issue 1]: theta* = 1.4967429 < 1.49675 and c = 0.5032571 > 0.50325. The value 1.4967 understates theta* and must not be used.

==================================================
5. REMARKS
==================================================
(R-P1) CENSUS REMARK (census_large_heights (P1); N, not load-bearing).
- Statement: under (B7) and (B8), a class keeps at most floor((h - 623)/448) + 1 labels in its light region.
- Proof: R-c gives i >= 150. R-b gives 2i + 1 <= T* - 322, since T* is odd. So survivors have i in an interval of length at most (h - 623)/2. Two labels of one class have Delta i a nonzero multiple of 32. If |Delta i| <= 210 they form a monochromatic R_FF^+ edge, whose shallow end is in Bad_split and leaves the region, by rule 3 or by R-g.
- The proof uses only that a class lies in one (T, tau), so it carries over to the (B4) law unchanged.
- Consequences: a surviving class with k labels needs h >= 623 + 448(k - 1), which is 1071, 1519 and 1967 for k = 2, 3, 4. So the in-class multi-label cells (D-4L, 3L1F) meet true survivors only for h of about 1500 to 2000 and up.
(R-P2) census_large_heights (P2) and (P3), N:
- for h < 1.2 · 10^7 every R_IV edge goes to R-e (min q = 109 at (1, 3));
- for h < 4096 the Theorem D part of R_FF^oo and R_FF^ee is empty, so Theorem D receives only R_FF^+ shallow ends;
- for h <= 5117 no two classes of a type are within 2W_h + 1 columns ((O1); the script recomputes the threshold as 5118 with p >= 40h + 1).
(R-C) CENSUS EVIDENCE (computational; v2 board with greedy classes and psi, not the (B4) law).
- Coverage: h = 1501, 2003 and 2501; 10 types (row-1 and row-3; k = 0, 1, 2); least admissible (l, p); kappa = b_tau = 0.
- No flags. True survivors show only D10 and D11, and the closure runs have 0 violations.
- Two-label violations occurred only in superset runs, and each is an R_FF edge removed by (B8) or R-e.
- Untested: even h; Table J1* seams; WD/WE blocks at T1 constants; WP junctions; the (B4) law; cross-class families (vacuous for h <= 5117).
- The definition-level N1 blocks of block_layout_n1 section 10 (h = 111, 112 and 129) are a sanity check far below T1's constants, and they did not separate zero-residue from mixed-residue labels.
(R-F) METHOD FLOOR (relocation_price_floor.md Theorem R; N, not audited).
- Statement: every relocation block of class P costs at least c Lambda^2 per label. Class P means independent uniform slots, one fixed sea row s0 on empty slots, and certificates that use only event probabilities and the shared-label dependency graph (every local lemma, Shearer, first-moment alteration). The forcing family is Lemma F: same-parity label points at integral distance with the matching sea pair on empty slots.
- Corollary R1: Theorems D and E are sharp in class P up to (loglog h)^C.
- Corollary R2: with kappa-heaviness, the heavy term of L***U is at least h Lambda^2 H_d(B/4) = h^2 Lambda^(2 - phi(x) + o(1)) (sieve lower bound, heavy Theorem 2, A12). So no class-P relocation lowers this construction below theta*. This bounds a method, not m_h.
- Loopholes: empty-slot seas with many slot rows (period P_s loses only a factor P_s; heuristic best beta about 1.92); the mod-p column rule (the odd-odd half of Lemma F dies, the even-even half is unproved); heaviness measured by chi(G_T[tau]) or |D_T ∩ 32Z|, for which heavy Theorem 2 gives an upper bound only.
(R-X) WHERE THE EXPONENT CAN STILL MOVE (heavy_diagonals_sharp exponent table; with Bad_split / without; all conditional, none audited unless stated):
- L***U (Proposition 3, A12): theta* / theta*.
- Better counts or moments for kappa-heaviness: no gain (Theorem 2, A12; sharp for kappa-heaviness only).
- Route L, layers by i mod Q: 1.2493 / 1, under (Pc), (Eq) and (Bal).
- Proposition 5 under (F): 1 / powers of ell only.
- Proposition 6 under (NR): 1 / 1.
- A relocation price Lambda^beta with beta < 2: theta(beta) (relocation table), excluded in class P by Theorem R.
- Removing Bad_split needs a split with O(1) parts and few bad labels. By truncated_additive_split Proposition O (A12, with its 2-adic qualifier), that would bound chi(R_IV^(5)) on [1, h^(delta/2)] for some type, which is open.
(R-T) ALTERNATIVE (TS). With the fixes of its audit (v2/v3 hypotheses, cutoff h^(1/2)/32, c_T = max over tau, B' = B + N0 throughout, A4 at h^(1+o(1)) by Theorem U), the truncated split also gives theta*, but only asymptotically.

==================================================
6. FIX LEDGER (round 11 and round 12 fixes applied here)
==================================================
From audit_consolidated_board_v2:
- issue 1 (serious): (B7) reordered [G7];
- issue 2: the R_FF density [G11];
- issue 3: D4' status, D5 and D6 names, S10 base cell, C2/L2 covering T4 and M8;
- issue 4: Table T 5117;
- issue 5: the status sentence (Q-mapping in the theorem);
- issue 6: A-26 statuses [G20];
- issue 7: the V2-4 count [G8];
- issue 8: Delta i in (B8) [G10].
From the audit of block_layout_n1:
- the T2 map and block types [G12];
- Claim (d) and Lemma RL via T2 [G14], with I2 restated;
- the E_J restatement [G15];
- Lemma TR' [G16];
- dyadic classes cut at Lambda^3 [G13];
- h0 = max(10^10, h_PNT, h_D) [G1];
- T2's rows (2) in the exceptional set [G2].
From the audit of uniformity_first_moments:
- the D18 constant;
- the U1 bounds stated directly;
- per-type filler rows and r0, with 512 only in min <= average [G17];
- K_max in the width [G6];
- the shape-count transfer sentence [G18];
- the pointwise form and the K6 order [G4].
From audit_heavy_diagonals_sharp:
- rounding to theta* = 1.4967429;
- sharpness stated for kappa-heaviness only;
- Proposition 4(a): gap at least 64lp - 4(A-1) > 2600h^2 with n(c) = kappa_tau;
- Proposition 4(b): restricted to rule L*_l with one region per (T, tau);
- Proposition 4(c): c_T >= 2B;
- N-3 restated over the law of chi (done by Theorem U).
From audit_truncated_additive_split: recorded in (R-T); (TS) is not adopted.
From the target: Theorem U replaces N-3. K6 uses min <= average. D11 is dropped from the sum. A4 and D8 are at h^(1+o(1)). V2-7 uses U1(b). Theorem N1 replaces N-1, with h0 >= 10^10. The census remark is (R-P1), and the method floor is (R-F).

## External results used

- Henriot, corrected Theorem 5, Math. Proc. Camb. Phil. Soc. 157 (2014) 375-377, through ap_hypothesis_henriot Lemma 1 (its audit read the erratum; I did not re-read it).
- Prime number theorem in arithmetic progressions mod 5 and mod 20 (non-explicit), for the admissible (l, p).
- Quadratic reciprocity: (5/p) = (p/5), (5/l) = (l/5).
- tau(n) << n^eps.
- For the sharpness remark only: the fundamental lemma of sieve theory in dimension 1/2 and Mertens' theorem for primes = +-1 mod 5 (theorem number not checked).

## Checks

I worked analytically and checked by hand:
- the reordered (B7) partition, and that rule 3 receives only labels in S;
- that Theorem D's hypotheses (i) and (ii) survive deleting the deterministic set R-a to R-d;
- that Theorem U's pointwise form makes the order '(l, p) first, then chi' legitimate, without Markov's inequality and without the D-block part of Lemma U3;
- n_rel, term by term: one Theorem D group, so no log B factor; A4 and D8 without B; D11 deterministic;
- t < 16lB with K_max = B;
- the exponent at a*, x = theta*, and the census (P1) proof under the new class law.
One script, expo_v3.py, in scripts_v3/, ran with py -I in under 1 s. It found:
- a* = 0.9124153, theta* = 1.4967429, c = 0.5032571, 4^a* = 3.5427;
- grid minimum of max(x, E(a*)+1-a* x, 2-x) = 1.49675 at x = 1.49674; the v2 exponent at x = 1.5 is 1.5;
- the light-width constant 5452595.2;
- (P1) bounds 2, 4, 5 and 8 at h = 1501, 2003, 2501 and 4000;
- h^2/8 + 3h/2 < (1.04h)^2 for all 10 <= h < 10^5;
- the class-separation threshold (64 · 40h - 4(A-1) > 2W_h + 1) holds up to h = 5118.
I read in full: consolidated_board_v2, audit_consolidated_board_v2, uniformity_first_moments, block_layout_n1, heavy_diagonals_sharp and its audit, truncated_additive_split and its audit, relocation_price_floor and census_large_heights. I read the opening of audit_gamma_two_split_primes_w, Section 1 and the start of Section 2 of safe_triangle_pair_first_moment (2026-11-09), and the ledger rows T1 to T4. The repository was only read, no git command was run, and no report file was written.

## Gaps

- (H1) is open: K2/K4 completeness rests on two text searches (audit_constant_lists.md, and the re-run over 25 notes in audit_consolidated_board_v2.md). A missed use of an old constant could hide a failure, as the D-1L3F side cell did in round 11.
- (H2a): the patches to Theorem N1 (the T2 Section 1 block map with separate zero-residue blocks; Claim (d) and Lemma RL via T2 Sections 2, 6 and 7; the E_J restatement; Lemma TR') were written by the auditor of block_layout_n1 and have not been re-read by anyone. They cite T2 (audited twice) and reuse T2's own argument.
- (H2b): V3-1 to V3-5 are new and not audited: the reordered (B7), the K6-v3 order with Theorem U in pointwise form ((l, p) fixed first, then chi on the Theorem D event), Proposition 3 combined with N1 as one Theorem D instance, n_rel, and the width line with t < 16lB.
- The T1 chain (T1 to T4, 2026-11-09) is audited link by link, but no single audit reads it end to end (ledger, section A). Theorem N1 and the slot counts of Theorems D and E rest on it.
- h0 = max(10^10, h_PNT, h_D) is not explicit.
- The census (R-C) tested the v2 board (greedy classes plus psi), not the (B4) colouring law: 10 of 512 types at three odd heights. No WD/WE block was built at T1 constants, and no Proposition partial junction was built at definition level. Cross-class families cannot be tested for h <= 5117.
- Theorem 2 (the heavy count is sharp) holds for kappa-heaviness only. The heavy counts for chi- and 32Z-restricted heaviness are open. Its sieve citation (fundamental lemma, dimension 1/2) has no checked theorem number. This affects only the sharpness remark and Corollary R2, not Theorem N.
- Theorem R (the method floor) and the census propositions (P1)-(P3) are not audited. They appear only in remarks.
- m_h = O(h^2) is not addressed. Nothing below theta* is proved. Route L, (F) and (NR) remain open hypotheses.

## Missing estimate

None for the near goal beyond (H1). Every obstruction cell is impossible, counted at O(h^(2-delta)) labels and relocated, or internal to a certified window. What remains is certification work, not a missing estimate: (H1), K2/K4 completeness, and second readings of the N1 patches and of V3-1 to V3-5. Below theta* = 1.4967429 the binding term is the heavy-light trade-off, B against Lambda^(E(a)+1) B^(-a). By Theorem R (unaudited), it cannot be improved by class-P relocation. The arithmetic targets are (Eq), a 2-adic moment bound for |D_T ∩ QZ|, together with (Pc) and (Bal) for Route L. The other targets are (F), a periodic independent set of density at least 1/K0 in Cay(Z, D_T), or a relocation block outside class P.

## Next steps

- Have a second reader audit V3-1 to V3-5 and the auditor's patches to N1 ([G12]-[G16]), about two pages. Check in particular that T2 (4) and (15)-(17) apply verbatim to the separated zero-residue and mixed-residue blocks.
- Re-run the K4 search over every note cited in section 2 with the v3 changes (heavy threshold B/4, K_max = B, one Theorem D group, h0 >= 10^10), and record one line per use. This is the only way to narrow (H1).
- Re-run the census at h = 1501 to 2501 with the (B4) colouring law (uniform proper B-colourings by Glauber or exact sampling), and at one even height, to test the in-class E cells under the new law.
- Build one definition-level WD block with separate zero-residue and mixed-residue blocks, and record any V2 with W in a low column (N1 audit, Section 10 issue).
- Audit relocation_price_floor Theorem R and Corollary R1, then mark Theorems D and E as optimal in class P.
- For the exponent below theta*: attack (Eq) (the 2-adic distribution of Tr beta over generators of norm -T^2), or test (F) numerically on the richest diagonals.

