# The junction decoupling holds at every scale

15 November 2026. Problem 001. Continues the gap-mixing notes of 2026-11-14 (continuation_gap_mixing_audit.md, p_excursion_decomposition.md, p_cross_scale_chains.md). Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: for S = 32 and every M >= 3, every cell with |T| <= 1 is an isolated cut of the whole candidate P graph. So every candidate component, not only every core component, lies in a corner segment Gamma_i = post(W_{i-1}) + pre(W_i) or in Omega_j = post(W_{j-1}) + O2, and DEC holds at every junction of every chain at all scales, by hand. The global candidate P problem is exactly M-solvability of four fixed systems per scale (Gamma_j^id, Gamma_j^swap, Omega_j^id, Omega_j^swap), and solutions chosen on different pieces always combine, with no boundary conditions. Not audited yet.

# Result

## Status

proved

## Summary

DEC holds at every junction of every chain, at all scales, for S = 32 and every M >= 3. The proof is by hand, and the result is stronger than DEC. Inside each staircase block W_i = O4(P_{i+1}), the cell with |T| = 1 is an isolated cut of the whole candidate graph. In fact every cell with |T| <= 1 is an isolated cut. So every candidate component, not only every core component, lies in a corner segment Gamma_i = post(W_{i-1}) + pre(W_i), which is inside W_{i-1} + W_i, or in Omega_j = post(W_{j-1}) + O2. C12 no longer needs the DEC hypothesis. The global candidate P problem is now exactly M-solvability of four fixed systems per scale: Gamma_j^id, Gamma_j^swap, Omega_j^id and Omega_j^swap. Solutions chosen on different pieces always combine, with no boundary conditions. This refutes the prediction that DEC fails at J_11.

## Statements

Setting. S = 32 and any M >= 3. Cand constraints live on the q-square, q = 2^k: no owner test and no row-range test. Every statement also holds for any subset of these constraints: gen, the strip-restricted set at any h, or the genuine rivals. Cells are (x, y), with odd row 2x+1, even row 2y+2 and T = y - x. Ranks follow Hilbert recursion (2) and are not compressed. A constraint (v, w, delta) has r_v < r_w, d = r_w - r_v, q = Md + delta >= 1 and |delta| <= M-1. Its cross pair (odd point of o, even point of e, {o,e} = {v,w}) has Y = |2U+1| with U = y_e - x_o, and (Sq)^2 + Y^2 is a square.

Notation.
- W(P) := O4(P) for a main-diagonal block P of side 2m.
- c*(P) := the unique cell of O4(P) with |T| = 1. For an id block P = [a, a+2m)^2 this is (a+m, a+m-1); for a swap block it is the transpose.
- pre(W) := the ranks of W before c*. There are R(m) = (m^2-1)/3 of them.
- post(W) := the ranks of W from c* on. There are (2m^2+1)/3 of them.

THEOREM 1 (corner cut). For every main-diagonal block P of side 2m >= 2:
- (a) no cand constraint is incident to c*(P);
- (b) no cand constraint (v, w) has r_v < rank(c*(P)) < r_w.

COROLLARY 1' (all |T| <= 1 cells are cuts). Every cell with |T| <= 1 is an isolated cut of the cand graph. No constraint touches it, and none joins a lower rank to a higher rank across it. Diagonal cells are covered by Theorem E / T3. The O2 corner is the last cell of its excursion. The O4 corner is Theorem 1. Every |T| = 1 cell is one of the two centre cells of a unique diagonal block.

COROLLARY 2 (DEC at every junction, strong form). Take any chain Sigma_j^g = W_0 -> ... -> W_{j-1} -> W_j' or Tail_j^g, with any orientation, any scale and either attach type. Every connected component of the full cand graph lies inside one of these pieces:
- Gamma_i := post(W_{i-1}) + pre(W_i), contained in W_{i-1} + W_i, for 1 <= i <= j-1;
- Omega_j := post(W_{j-1}) + W_j', for Sigma only;
- post(W_{j-1}), for Tail only;
- the initial diagonal cell, which has no constraints.

A fortiori every component of the certified or integer weighted M-core lies in two consecutive blocks. So DEC holds at every junction J_i, for all four junction types (id,O4), (id,O2), (swap,O4), (swap,O2), at every scale.

THEOREM R (exact reduction, unconditional). Define the following, each up to translation along the diagonal.
- Gamma_i^{g'} (i >= 1, g' in {id, swap}): take P_{i+1} of side 2^{i+1} and orientation g', and P_i = C3(P_{i+1}). Then Gamma_i^{g'} = post(O4(P_i)) + pre(O4(P_{i+1})). It occupies the rank interval [J_i - (2*4^{i-1}+1)/3, J_i + (4^i-1)/3), where J_i = start of O4(P_{i+1}), and has 2*4^{i-1} labels.
- Omega_j^g (j >= 1): take P_{j+1} of orientation g and P_j = C1(P_{j+1}). Then Omega_j^g = post(O4(P_j)) + O2(P_{j+1}), with (4^j+2)/6 + 4^j labels.

Then:
- (i) The cand P system on the q-square, q = 2^k, is a disjoint union of independent systems. No constraint joins two of them. Each is a translate of one of: Gamma_i^{g'} (i <= k-1); Omega_j^g (j <= k-1); post(O4(top)), which is a rank-prefix, hence induced subsystem, of Gamma_k^id; or a constraint-free cell. Plain or certified solutions chosen independently on the pieces always combine, with no boundary lists, no anchoring and no certification needed.
- (ii) The cand system is M-solvable (respectively certified-M-solvable) on every q-square if and only if every Gamma_i^{g'} and every Omega_j^g, for i, j >= 1 and both orientations, is. That is four fixed systems per scale.
- (iii) The conditional clause of C12 (p_cross_scale_chains.md) is now unconditional. The family {Pi_j^{a,g}} of two-block systems is solvable for all j exactly when {Gamma_j^{g'}, Omega_j^g} is. Each Pi_j^{O4,g'} = W_{j-1} + W_j splits at the two corner cuts into pre(W_{j-1}) + Gamma_j^{g'} + post(W_j). The two outer pieces are induced subsystems of the neighbouring Gamma or Omega systems. Each Pi_j^{O2} = pre(W_{j-1}) + Omega_j. So T8 holds at every scale, with Pi_j replaced by smaller systems: Gamma_j has 40% of the labels of Pi_j^{O4}, and Omega_j has about 93% of Pi_j^{O2}.

Status at M = 3 (computer-assisted, from archived certificates). Gamma_i^{g'} and Omega_j^g are certified-3-solvable for i, j <= 10, both orientations. This re-derives C11 (the cand P system is 3-solvable at every h <= 4096). The derivation no longer uses C10, L9 or any DEC computation. The open systems are those with i, j >= 11.

## Proofs

0. INPUTS (all earlier results, none audited; I re-derived each by hand).
- (T1) Every cand endpoint has |T| >= 6. A Pythagorean triple with 32 | X and Y odd has Y >= 31, so |U| >= 15. With |T_z - U| < 4 sqrt(d) (Hilbert locality, audited) and 16d < |U|(|U|+1)/3 + 16 (Lemma 1), |T_z| <= 5 forces 2x^2 - 31x + 27 < 0 for x = |U|, which fails for x >= 15.
- (E) Theorem E of p_excursion_decomposition.md (equivalently T3 of p_cross_scale_chains.md): no constraint crosses the rank of a main-diagonal cell. So every constraint lies in one excursion.
- (L) Corollary L there (equivalently the last paragraph of T4): inside an excursion (x,x), W_0, W_1, ..., W_{j-1}, W_j' (W_i = O4(P_{i+1}), side 2^i; W_j' = O2(P_{j+1})), constraints join only labels of the same link or of two consecutive links. I re-checked Lemma A' (s = 1 and the monotonicity of g), Lemma B (cases d = 1 and 2) and the induction in Theorem E.
- Theorem A: each main-diagonal block is a translate of H_{2m} or of its transpose. Orientation rule: C1 swaps, C3 keeps.

1. LEMMA 1 (rank length from the cross diagonal). Every cand constraint satisfies d < |U|(|U|+1)/48 + 1.
Proof.
- X = Sq > 0 and Y is odd, so L >= X + 1 and Y^2 = (L-X)(L+X) >= 2X + 1 = 64q + 1.
- Y^2 = 4U^2 + 4U + 1, so q <= U(U+1)/16 <= |U|(|U|+1)/16.
- From q >= Md - (M-1), d <= (q + M - 1)/M <= |U|(|U|+1)/(16M) + (M-1)/M < |U|(|U|+1)/48 + 1 when M >= 3.
QED. No locality is used.

Box form. If o lies in a box with x-range I and e in a box with y-range J, then |U| <= max |J - I|. Taking both role assignments makes the bound invariant under transposition. Hence:
- (B0) any two cells of a diagonal block of side L have |U| <= L - 1;
- every bound below holds for swap blocks too.

2. LEMMA 2 (geometry of an O4 block). Let P be an id block of side 2m. Up to diagonal translation, P = [0, 2m)^2 and W = O4(P) = [m, 2m) x [0, m), traversed as phi(H_m) with phi(x,y) = (2m-1-y, m-1-x). (This is the Q4 map of recursion (2).)
Let s = 2n be the side of such a canonical block. Recursion (2) lists H_s as:
- Q1 = transpose on [0,n)^2;
- Q2 = (x, y+n);
- Q3 = (x+n, y+n);
- Q4 = (2n-1-y, n-1-x).
Applying phi, the rank quarters of W are, in order:
- Q1(W) = A = [3s/2, 2s) x [s/2, s);
- Q2(W) = N = [s, 3s/2) x [s/2, s);
- Q3(W) = B = [s, 3s/2) x [0, s/2);
- Q4(W) = F = [3s/2, 2s) x [0, s/2).

The second quarter keeps the traversal type. phi(x, y+n) = (3n-1-y, 2n-1-x) equals (a+2n-1-y, a+n-1-x) with a = n. So N, with its traversal, is the canonical side-n block translated by (n, n).

Put W^(0) = W and W^(k+1) = Q2(W^(k)). Then:
- W^(k) is the canonical block of side s_k = m/2^k, translated to [m, m+s_k) x [m-s_k, m);
- every W^(k) contains (m, m-1), and W^(i) = {c*} with c* = (m, m-1), T = -1 (m = 2^i);
- inside W^(k), c* sits in Q2 at local offset R(s_k/2), so its local rank in W is R(m) = m^2/4 + R(m/2) = (m^2-1)/3.
For a swap block, transpose everything.

3. LEMMA 3 (U bounds inside W^(k), side s). The quarters span these coordinate ranges:
- A: x in [3s/2, 2s), y in [s/2, s);
- N: x in [s, 3s/2), y in [s/2, s);
- B and F together: x in [s, 2s), y in [0, s/2).
Hence:
- (A, N): U = y_e - x_o lies in [-(3s/2-1), -(s/2+1)] or in [-(s-1), -1], so |U| <= 3s/2 - 1.
- (N, B+F): U lies in [-(3s/2-1), -(s/2+1)] or in [-(3s/2-1), -1], so |U| <= 3s/2 - 1.
- (A, B+F): U lies in [-(2s-1), -(s+1)] or in [-(3s/2-1), -1], so |U| <= 2s - 1.

4. PROOF OF THEOREM 1. Let W = O4(P) with side m = 2^i, and p = rank(c*).
- (a) c* has |T| = 1, so by (T1) it has no constraint.
- (b) Suppose r_v < p < r_w. By (E), the constraint lies in the excursion where W = W_i is a staircase link. By (L), the links of v and w are equal or consecutive. Since the links are rank intervals and p lies in W, only three placements remain.

Case (a): v in W_{i-1}, w in W after c*.
- Then d >= R(m) + 2.
- W_{i-1} and W_i both lie in P = P_{i+1}, of side 2m. By B0, |U| <= 2m - 1, so by Lemma 1, d < (4m^2 - 2m)/48 + 1.
- Now (4m^2 - 2m)/48 + 1 <= (m^2-1)/3 + 2, because 4m^2 - 2m <= 16m^2 + 32. Contradiction.

Case (b): v in W before c*, w in the next link L'.
- L' is O4(P_{i+2}) or O2(P_{i+2}), and W lies in P_{i+1}, which lies in P_{i+2}, of side 4m.
- Then d >= m^2 - R(m) + 1 = (2m^2+1)/3 + 1.
- By B0, |U| <= 4m - 1, so d < (16m^2 - 4m)/48 + 1.
- Now 16m^2 - 4m <= 32m^2 + 16. Contradiction.

Case (c): v and w both in W. Let k be maximal with v, w in W^(k), and let s = s_k >= 2. In local ranks, Q1 = [0, s^2/4), Q2 = [s^2/4, s^2/2), Q3+Q4 = [s^2/2, s^2), and p = s^2/4 + R(s/2). Three placements remain:
- (c1) v in Q1, w in Q2 after p. Then d >= R(s/2) + 2 = (s^2-4)/12 + 2. Lemma 3 gives d < (9s^2/4 - 3s/2)/48 + 1. The contradiction needs 9s^2 - 6s <= 16s^2 + 128, which holds.
- (c2) v in Q2 before p, w in Q3+Q4. Then d >= s^2/4 - R(s/2) + 1 = (s^2+2)/6 + 1. Lemma 3 gives d < (9s^2/4 - 3s/2)/48 + 1. The contradiction needs 9s^2 - 6s <= 32s^2 + 64, which holds.
- (c3) v in Q1, w in Q3+Q4. Then d >= s^2/4 + 1. Lemma 3 gives d < (4s^2 - 2s)/48 + 1 <= s^2/4 + 1.

Every inequality holds for all s, m >= 1, so no small cases are needed. For m <= 2 the claim is vacuous in any case, because |T| <= 3 there. Swap blocks follow by transposition. QED.

5. COROLLARY 1'. Every |T| = 1 cell (x+1, x) or (x, x+1) is a centre cell of the least aligned diagonal block P containing (x,x) and (x+1,x+1). It lies in O2(P) or in O4(P).
- If it lies in O4(P), Theorem 1 applies.
- If it lies in O2(P), it is the last cell of O2(P): H_q ends at (q-1, 0), which maps to (q-1, q) or its transpose. So it is the last cell of its excursion and is followed by a diagonal cell. A constraint across it would cross that diagonal cut (E).
- Diagonal cells are handled by (E) and T1.
QED.

6. COROLLARY 2.
- Cut the chain at c*(W_1), ..., c*(W_{j-1}); W_0 is itself a |T| = 1 cell.
- By Theorem 1 the pieces between consecutive cuts share no constraint.
- These pieces are exactly Gamma_1, ..., Gamma_{j-1} and the final piece, which is Omega_j for Sigma or post(W_{j-1}) for Tail.
- Gamma_i lies in W_{i-1} + W_i, and Omega_j in W_{j-1} + W_j'.
QED.

7. THEOREM R.
- (i) Combine (E) with Corollary 2. Cand constraints depend only on relative coordinates and rank differences, so each piece is a diagonal translate of the stated type. Its type depends only on (i, g') or (j, g):
  - W_{i-1} and W_i sit inside P_{i+1} with P_i = C3(P_{i+1}), so Gamma_i depends only on the orientation of P_{i+1}.
  - Omega_j uses P_j = C1(P_{j+1}).
  - The terminal tail has all parents id, and post(O4(top)) is a rank-prefix of Gamma_k^id.
  Disjoint pieces share no constraint, so any per-piece solutions combine. Certification is not needed, because no constraint crosses a piece boundary.
- (ii) "If" follows from (i). For "only if": Sigma_j^g occurs in every q-square that contains a diagonal block of side 2^{j+1} and orientation g. By Theorem A both orientations occur at each scale below the top. So every Gamma_i^{g'} and every Omega_j^g occurs as a whole piece once k is large enough.
- (iii) Pi_j^{O4,g'} = W_{j-1} + W_j contains the cuts c*(W_{j-1}) and c*(W_j), so it splits into pre(W_{j-1}), Gamma_j^{g'} and post(W_j). The first is an induced subsystem (rank suffix) of Gamma_{j-1}^{g'}. The last is a rank prefix of Gamma_{j+1}^{g'} or of Omega_{j+1}. The O2 case is the same with one cut.
QED.

8. REMARKS AND COROLLARIES OF THE PROOF.
- Junction depth. By case (a), every W_{i-1}-to-W_i constraint has d <= F(2m-1) < m^2/12 + 1. This beats the locality bound Dmax(m-1) of C4': at J_10 it gives 87339 against 122160. On the new side, junction constraints touch only A(W_i), the first quarter of W_i.
- The prediction pre-registered in p_cross_scale_chains.md fails. It said DEC would break at J_11 because the junction component would reach the J_10 component through the interior giant of W_10. In fact that giant lies in post(W_10) and the J_10 component lies in pre(W_10); c*(W_10) separates them.
- P6 and P7 are consistent with the theorem. Their conflicts and merges happen inside Gamma_10 = post(W_9) + pre(W_10). So the inductive object is a solution of Gamma_i, not of a block.
- Self-similarity, structural only: pre(W_i) = A(W_i) + (translate of pre(W_{i-1})), and post(W_i) = (translate of post(W_{i-2})) + B + F of W_{i-1}... Precisely, Gamma_i, in rank order, is a copy of post(W_{i-2}), then B and F of W_{i-1}, then J_i, then A(W_i), then a copy of pre(W_{i-1}). The two copies together have |Gamma_{i-1}| labels.
- Scope of the hypotheses. The steps of Section 4 use only Lemma 1 and Lemma 2. The full theorem also needs (E), (L) and T1, so its scope is theirs: S = 32 and M >= 3.

9. EXACT CHECKS (sanity checks only, not part of the proof).
- check_cuts.py: cand G_1024, both orientations. My builder reproduces the archive counts 1344642 (id) and 1341364 (swap). All 1023 O4 corners per orientation have 0 crossing and 0 incident triples, and all 2046 |T| = 1 cells are isolated cuts.
- verify_pi10.py: the four Pi_10 windows on the 2048 curve. Triple counts 2267053, 2302662, 2261960 and 2300426, and core counts 521431, 545202, 492178 and 516262, all match the table. The corners of W_9 and W_10 have 0 crossings. The archived certificates certificates_pi10_M3.npz have 0 certified violations against my independent builder.
- Core sizes inside the cut pieces:
  - Gamma_10^id: 195031 of 524288 labels (components 187918, 4296, 1415, 1402).
  - Gamma_10^swap: 179448.
  - Omega_10^swap: 530919 of 1223339.
  - Omega_10^id: 509446.
- dec11.py window: W_9 + W_10 + 600000 ranks of W_11, (id,O4), 4096 curve, 3590981 triples. The core components are 736687 (0 / 317380 / 419307), 187918 (32810 / 155108 / 0), 12881, and copies of 4296, 1415 and 1402. No component holds both a W_9 label and a W_11 label. Corners c*(W_9) and c*(W_10) have 0 crossings.
- gamma11.py: Gamma_11^id has 2097152 labels, 4149319 triples, 0 crossings at both bounding corners, and a certified 3-core of 1205355 labels. Its components are 1198242, 4296, 1415 and 1402, with |T| in [193, 3071]. Gamma_11^swap has 4170642 triples and a core of 1201783 labels in one component, with |T| in [349, 3071].

## External results used

- No published theorem was used, and no web source was consulted.
- Hilbert locality max(Dx^2, Dy^2) < 16|Dr|: Theorem 1 of continuation_hilbert_placement.md, audited. Used only through T1, Theorem E and Corollary L.
- Theorem E, Lemma A', Lemma B and Corollary L of p_excursion_decomposition.md, equivalently T1 to T4 of p_cross_scale_chains.md. Not audited; re-checked by hand here.
- Theorem A (diagonal blocks are id or swap; C1 swaps, C3 keeps) of hilbert_p_height_independent_cores.md, confirmed in audit_gap_mixing_full_components.md.
- Archived certificates: scripts_gm2_core_exact/certificates_B1024_M3.npz (re-verified in p_excursion_decomposition.md) and scripts_gm3_hier/certificates_pi10_M3.npz (re-verified here with an independent builder: 0 violations, all four types). Used only for the M = 3 status for j <= 10.

## Checks

Scripts are in scripts_gm4_dec_all/ (15 MB). Each ran with py -B, one at a time, under 60 s (the longest was verify_pi10.py at 55.6 s) and under 1 GB.
- common.py is my own builder: recursion (2), legs from a divisor sieve, and a parallel two-pass numba kernel over (d, delta, both roles), deduplicated by a packed key.
- repro_pi10.py reproduces 2267053 and 2300426 triples and 521431 and 516262 core labels.
- check_cuts.py checks every O4 corner and every |T| = 1 cell of cand G_1024 in both orientations, and reproduces 1344642 and 1341364 triples.
- verify_pi10.py checks the four archived Pi_10 certificates (0 certified violations each) and the corner cuts.
- dec11.py checks the J_11 window and lists its core components.
- check_win_cuts.py checks the corners in that window.
- gamma11.py builds Gamma_11^id and Gamma_11^swap, checks the bounding cuts, and computes the cores.

Hand checks: Lemma 1; Lemma 2 (quarter boxes and the translate identity (3n-1-y, 2n-1-x)); Lemma 3 (all six role ranges); the five inequalities of cases a, b, c1, c2, c3 for all s, m; Corollary 1'; and the inputs T1, Lemma A', Lemma B and the Theorem E induction.

I read the repository and did not change it. I ran no git command and did not touch Kagey-Problems.

## Gaps

- Nothing here is audited. Theorem 1 itself (Lemmas 1 to 3 and cases a, b, c1 to c3) is elementary and under a page, and it should go to an independent reader.
- The proof cites Theorem E / T3 (diagonal cells are cuts), Corollary L / T4 (constraints only within a link or between consecutive links) and T1 (|T| >= 6). Two notes derived these independently, and I re-checked them by hand. None of them is audited. They rest on audited Hilbert locality and on Theorem A, which audit_gap_mixing_full_components.md confirmed. Only cases (b) and the confinement to the chain use them. Case (c), both endpoints in one block, uses only Lemma 1 and the geometry.
- Everything is for the cand version on the q-square, and so for every subset of it. That gives the decomposition and positive (solvability) statements at every h. A negative verdict on some Gamma_i or Omega_j, carried to genuine rivals at large h, still needs Corollary A1 and the gen version, as in Corollary R(b).
- The bounded-M P problem is not solved. Theorem R reduces it, with no gluing left, to four fixed systems per scale: Gamma_j^id, Gamma_j^swap, Omega_j^id and Omega_j^swap. M = 3 is certified for j <= 10 only, using the archived certificates. I re-verified the four Pi_10 certificates; I did not re-verify the B1024 certificates, but p_excursion_decomposition.md did with its own builder. Gamma_11 has a single giant certified core of about 1.2M labels, 57% of its labels. Omega_11 has about 4.9M labels. I did not attempt a SAT certificate for either, because it would exceed the 60 s budget and it is census-like.
- P family only, at S = 32, full grid (c = 1, D = 2). Profile boards (H7: D = 28, S = 6272 sigma, offset c) are not done; there Y = |c + D U| changes Lemma 1. R2s, FW, 6PT, Lambda3/4, the sea and the collars are untouched.
- Core sizes and component structure inside the Gamma and Omega pieces are exact data for j <= 11 only. No structural statement about where the core sits inside Gamma_j is proved.

## Missing estimate

Theorem 1 removes all gluing. What remains is a uniform M-solvability theorem for the corner segments Gamma_j^{g'} = post(W_{j-1}) + pre(W_j), with 2*4^{j-1} labels, and Omega_j^g = post(W_{j-1}) + O2, with (4^j+2)/6 + 4^j labels, for all j and both orientations, at some fixed M.

At M = 3 the certified core fraction of Gamma_j grows:
- 0 for j <= 7;
- 37% (id) and 34% (swap) at j = 10;
- 57% at j = 11, as one giant component of about 1.2M labels.

So a solution rule must handle a core that percolates through Gamma_j. The natural structure to exploit is the inflation Gamma_j = [copy of post(W_{j-2})] + B(W_{j-1}) + F(W_{j-1}) | J_j | A(W_j) + [copy of pre(W_{j-1})]. Its outer copies carry exactly |Gamma_{j-1}| labels and reproduce the small recurring components (4296, 1415, 1402). An inductive statement would have to control how the new middle part (B, F and A blocks of sides 2^{j-2} and 2^{j-1}) attaches to the two copies.

## Next steps

- Audit Theorem 1: Lemmas 1 to 3 and cases a, b, c1 to c3. It is under a page and makes C10, L9 and the J_11 test unnecessary. Record in the ledger that every |T| <= 1 cell is an isolated cut of the cand P graph at S = 32, M >= 3, and that the global P problem is exactly the four corner-segment systems per scale.
- Update p_cross_scale_chains.md. C12 becomes unconditional, with Pi_j replaced by Gamma_j and Omega_j. The J_11 DEC prediction is false. C11 now needs only T4, Theorem 1 and the certificates, not C10.
- Transfer Theorem 1 to profile boards (H7: D = 28, S = 6272 sigma, offset c). Case (c) needs only a Lemma 1 analogue d < (c + D|U|)^2/(2SM) + 1 together with the O4 geometry. Check that the five inequalities survive with the H7 constants, and whether Theorem E transfers.
- Check whether the corner-cut argument applies to R2s, FW, 6PT and Lambda3/4. Any family whose rank length is bounded by a quadratic in a cross-pair diagonal tied to the spatial box would split at the same |T| <= 1 cells.
- Structural work on Gamma_j: prove or refute that the core of Gamma_j stays within a fixed set of quarter blocks around J_j, and look for a choice rule that is compatible with the inflation Gamma_j = copy + middle + copy.
- If an exact certificate is wanted later: run SAT on the cores of Gamma_11^id and Gamma_11^swap (about 1.2M labels each). That needs a staged run longer than 60 s. Omega_11 (about 4.9M labels) is out of budget.

