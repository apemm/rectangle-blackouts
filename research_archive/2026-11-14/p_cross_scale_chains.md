# Chains of off-diagonal blocks and the cross-scale combination

15 November 2026. Problem 001. Continues continuation_gap_mixing_audit.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: the P candidate graph at S = 32, M >= 3 splits exactly into chains of first-off-diagonal blocks W_0 -> W_1 -> ..., with constraints only inside a block or between consecutive blocks, and diagonal children never interact (sign separation T1, backward isolation T2, diagonal starts are cuts T3, exact decomposition T4). The naive invariant fails: a certified child solution need not extend under any shift (P6, with a witness). Core stability holds from 512 to 1024 and fails from 1024 to 2048. What survives is a two-block decoupling (DEC) at every junction up to 2048; with four new exact two-block certificates (saved in scripts_gm3_hier/certificates_pi10_M3.npz) the candidate P system is certified-3-solvable at every h <= 4096 (C11). For all h, solvability is equivalent to solvability of two system types per scale, and, under DEC at every junction, of four two-block systems per scale (C12). No bounded-M theorem for all h is proved. Audited in ../2026-11-15/audit_p_excursion_decomposition.md (correct with fixable gaps); DEC is proved at every scale in ../2026-11-15/p_dec_all_scales.md (not audited yet).

# Result

## Status

partial

## Summary

Combining across scales: the candidate P graph at S = 32, M >= 3 splits exactly into chains of first-off-diagonal blocks, and diagonal children never interact. The naive invariant fails: a certified child solution need not extend under any shift. Core stability holds from 512 to 1024 and fails from 1024 to 2048. The invariant that survives is a two-block decoupling at every junction up to 2048. With four new exact certificates, it shows the candidate P system is certified-3-solvable at every h <= 4096.

## Statements

Setting. S = 32, M >= 3 unless stated otherwise. Labels are the cells (x, y) of the padded q-square (q = 2^k), with odd row 2x+1, even row 2y+2, Hilbert rank r and diagonal T = y - x. "cand" means the archive's candidate constraints with no owner test and no row-range test. The global candidate system at height h is a subsystem of cand on the q-square (q = least power of 2 >= ceil(h/2)), so certified solvability of cand implies solvability at h. "Certified" means y_u - y_r is not congruent to delta mod M. W_i denotes a block of side 2^i.

T1 (sign separation; proved). Every cand constraint joins two labels whose T have the same sign and |T| >= 6. Computed exactly: |T| >= 7 at M = 3 and |T| >= 8 at M = 4.

T2 (backward isolation; proved). Let D be any main-diagonal Hilbert block, of any side, position or orientation, and v a label of D at local rank rho. Then every cand constraint of v has rank distance d <= rho. Hence no constraint joins v to a label that precedes D.

T3 (diagonal starts are cuts; proved). For every main-diagonal block D, no cand constraint joins a label of rank < start(D) to a label of rank >= start(D). In particular every main-diagonal cell is a cut.

T4 (exact decomposition; proved). The cand system on the q-square is the disjoint union of independent systems, one per rank interval between consecutive main-diagonal cells. Each interval system is, by translation along the diagonal, one of the following:
- Sigma_j^g = W_0 -> W_1 -> ... -> W_{j-1} -> W_j'. Here W_i = O4(P_{i+1}) has side 2^i, W_j' = O2(P_{j+1}) has side 2^j, P_1 is in P_2 is in ... is in P_{j+1} are main-diagonal blocks, P_i = C3(P_{i+1}) for i < j, P_j = C1(P_{j+1}), and g is the orientation of P_{j+1}.
- The terminal tail Tail_k^id = W_0 -> ... -> W_{k-1} of the top block.
Every block of a chain is a first-off-diagonal block (offset equal to its side), and all of them lie in one half (T > 0 or T < 0). Constraints occur only inside a block or between rank-consecutive blocks of a chain. Write Tail_j^g = W_0..W_{j-1}. Then Tail_{j+1}^g = Tail_j^g + O4 (side 2^j), and Sigma_j^{g o swap} = Tail_j^g + O2 (side 2^j). These are the only two scale-transition operations.

C4' (the question for a diagonal 2B-block P; proved). The two diagonal children C1 and C3 share no constraint. C3 shares none with O2(P), and C1 shares none with O4(P). The only crossing constraints are C1 to O2(P) and C3 to O4(P). Each joins the last off-diagonal grandchild O4(C) of the diagonal child (side B/2) to the first ranks of the off-diagonal child, within rank depth Dmax(B-1) of the junction on both sides. Dmax(511) = 30477 and Dmax(1023) = 122160 at M = 3. Diagonal grandchildren are never touched. Hence the certified solution set of P is a product over independent segments, and only the four tail-to-block junctions couple anything. Exact counts:
- B = 512 to 1024: 2402, 1783, 1590 and 1889 crossing triples for (id,O4), (swap,O2), (id,O2), (swap,O4). They carry 38 to 47 gaps in [2, 24375], with depth <= 5467 on the old side and <= 7294 on the new side. The old endpoints have |T| in [381, 511].
- B = 1024 to 2048: 10988, 8062, 10404 and 8309 triples, with 81 to 102 gaps in [165, 99777] and depth <= 22102 (old) and <= 29977 (new).

L5 (shifts are vacuous; proved). When only one side of a junction is fixed, a certified y extends iff y + kappa extends. So "extends after some shift" is the same as "extends".

P6 (the naive invariant fails; exact, with a hand-checkable witness). Take y_B, the cand B1024 swap certificate restricted to its first child. It is a certified solution of cand G_512^id (0 violations). Placed as the third child of the id parent of side 1024, no shift of it extends to a certified solution of the parent: 33 labels of O4 are blocked outright. The other three cross-placements also fail.

P7 (core stability; exact). Let K_A be the certified 3-core of the old tail A.
- At 512 to 1024, K(Tail_9^g) is a union of components of the joint core for all four junction types.
- At 1024 to 2048, this is false for all four types: a component of K(Tail_10^g) merges with labels of the attached block.

T8 (combining junction repairs; proved, abstract). Take a chain W_0, ..., W_m in which constraints occur only inside blocks or between consecutive blocks. Assume DEC: every component of the certified M-core lies in W_{i-1} union W_i for some i. Then the chain is certified-M-solvable iff every two-block system Pi_i = W_{i-1} union W_i (induced) is. Moreover, independently chosen certified solutions of the Pi_i always combine.

L9 (local DEC test; proved). Let A = W_0..W_{i-1} satisfy DEC, and let Z = the labels of A with a constraint into W_i. Suppose no component of the graph induced on the Z-anchored certified core of A contains both a label before J_{i-1} (the start of W_{i-1}) and a label of Z. Then A + W_i satisfies DEC.

C10 (DEC holds through 2048; exact). DEC holds at J_8, J_9 and J_10 for all junction types: (id,O4), (id,O2), (swap,O4), (swap,O2).

C11 (finite consequence; computer-assisted). At S = 32 and M = 3, the cand P system on the q-square is certified-3-solvable for every q <= 2048. So the archive's global P candidate system is 3-solvable at every h <= 4096. This uses the archive's B1024 certificates and four new two-block certificates Pi_10 (W_9 union W_10, 1310720 labels each), each verified with 0 certified violations.

C12 (all large h). Certified-M-solvability of cand at every height is equivalent to certified-M-solvability of the family {Sigma_j^g, Tail_j^g : j >= 0}. Two types are added per scale, and failure of one type persists at every larger h.
- M = 3: solved for j <= 10 (Sigma) and j <= 11 (Tail).
- Conditional on DEC at every junction: solvability for all h is equivalent to solvability of the two-block systems Pi_j^{a,g}, four per scale.
- M = 4: every type with j <= 9 (Sigma) or j <= 10 (Tail) has an empty certified 4-core.
- No bounded-M theorem for all h is proved.

## Proofs

0. Notation and the basic bound. A constraint between labels v and w at rank distance d >= 1 has gap q = Md + delta with |delta| <= M-1, X = Sq, and a cross pair: the odd row 2x_o+1 of one label and the even row 2y_e+2 of the other. So Y = |2U+1| with U = y_e - x_o.
- From X^2 + Y^2 = L^2 with X even and Y odd, Y^2 >= 2X + 1. So q <= (Y^2-1)/(2S) = 2U(U+1)/S, and Md <= q + M - 1. Hence d <= F(U) := floor(2U(U+1)/(SM) + (M-1)/M).
- Locality (audited Theorem 1 of continuation_hilbert_placement.md): max(Dx^2, Dy^2) < 16d. If v is the odd endpoint, T_v - U = y_v - y_w. If v is the even endpoint, T_v - U = x_w - x_v. Either way |T_v - U| < 4 sqrt(d), and likewise for w.
- Minimal leg. A triple with 32 | X and Y odd has the form X = 2mn g, Y = |m^2 - n^2| g with g odd, gcd(m, n) = 1 and opposite parity. Then 16 divides the even one of m, n, so Y >= |e - o|(e + o) >= 31, attained at (16, 15). Hence |U| >= 15 (U >= 15 or U <= -16).
- Crude bound (SM >= 96, so any M >= 3 at S = 32). Put A = |U| + 1/2. Then 2U(U+1) <= 2A^2 - 1/2, so d < A^2/48 + 1 and 4 sqrt(d) < sqrt(A^2/3 + 16) <= A/sqrt3 + 4. If |T_v| <= t, then A - 1/2 - t < A/sqrt3 + 4. This gives A < 2.36603(t + 4.5) and d < 0.116627(t + 4.5)^2 + 1 =: crude(t). Write Dmax(t) for the exact maximum of F(U) over admissible U (|2U+1| >= 31 and (|U| - t)_+^2 < 16F(U)).
- Exact values (lemma_check.py): no constraint exists for |T| <= 6 (M = 3) or <= 7 (M = 4). By hand: for U >= 15, (U-5)^2 >= U(U+1)/3 + 32/3, so |T| <= 5 is excluded for every M >= 3. Dmax(7) = 7 (M = 3) and 0 (M = 4), Dmax(2^k - 1) <= 4^(k-1) for k <= 12, and in particular Dmax(1023) = 122160.

1. T1. Suppose T_v <= 0 <= T_w. Then |U| <= max(|U - T_v|, |U - T_w|) < 4 sqrt(d), so U^2 < 16F(U) <= U(U+1)/3 + 16. That forces 2U^2 - U - 48 < 0, so |U| <= 5, which contradicts |U| >= 15. The bound |T| >= 6 follows from the exact remark in 0. QED.

2. T2. Let D have side 2^b and v local rank rho.
- If rho = 0, then T_v = 0 and v has no constraints.
- Otherwise let k be minimal with rho < 4^k, so k <= b and 4^(k-1) <= rho. The first 4^k ranks of a diagonal block (either orientation) are its lower-left sub-block of side 2^k, which is diagonal: the first child C1 is lower-left, and so on recursively. So |T_v| <= 2^k - 1.
- For k <= 2, v has no constraints (|T| <= 3).
- For k = 3, d <= Dmax(7) <= 16 <= rho. By hand for any M >= 3: admissible U satisfy U <= 18, and F(18) <= 8.
- For k >= 4, put x = 2^k >= 16. Then crude(x - 1) <= x^2/4 = 4^(k-1) <= rho, since x^2/4 - 0.116627(x + 3.5)^2 - 1 is positive at x = 16 (64 - 45.35) and increasing for x >= 16.
So d <= rho. QED.

3. T3. This is strong induction on the number of ancestors of D (the claim for larger blocks first). Let F be the maximal main-diagonal block with start(F) = start(D), of side m. If F is the top block, the claim is vacuous. Otherwise F is not a first child (else its parent starts at the same rank), so F = C3(P) with P of side 2m. Take a constraint (w, v) with rank(w) < start(F) <= rank(v).
- If v is in F, T2 gives rank(w) = rank(v) - d >= start(F). Contradiction.
- If v is not in F, then d >= m^2 + 1. Every label of P has |T| <= 2m - 1, and Dmax(2m - 1) <= m^2 by step 2 with k = log2(2m). So neither w nor v lies in P. Then the constraint crosses start(P) with v after P, which contradicts the claim for P.
QED.

4. T4. By T3, the cand graph has no edge across the rank of any diagonal cell, so it is the disjoint union of the interval systems. Follow the Hilbert recursion after a diagonal cell c.
- If c = C1 of its 2-block P_1, the next cell is O2(P_1) and then C3(P_1), which begins with a diagonal cell.
- If c = C3(P_1), then O4(P_1) follows. If P_1 = C3(P_2), then O4(P_2) follows, and so on, until P_j = C1(P_{j+1}). Then O2(P_{j+1}) follows, and C3(P_{j+1}) begins with a diagonal cell.
So the interval is c (which has no constraints) followed by O4(P_1), ..., O4(P_j), O2(P_{j+1}), with sides 1, ..., 2^(j-1), 2^j.

These blocks are first-off-diagonal, for example O4 of a diagonal block of side 2m is [m, 2m) x [0, m). P_1, ..., P_j share the orientation g o swap (C3 keeps orientation, C1 swaps it). O4 of an id block is lower and O2 is upper, and the reverse holds for swap, so all blocks lie in one half. A cand system is invariant under the translation (x, y) -> (x + c, y + c) with the matching rank shift, because X, Y and d depend only on differences. So the interval system depends only on (j, g).

Non-consecutive blocks W_i and W_{i+2} would need d > 4^(i+1). But W_i has |T| <= 2^(i+1) - 1, and Dmax(2^(i+1) - 1) <= 4^i. So constraints are only between consecutive blocks.

C4' follows by reading off a diagonal 2B-block: its segments are Sigma(C1) restricted to C1, closed; Tail(C1) + O2(P); the segments of C3; and Tail(C3) + O4(P). The junction depth bound is Dmax(B - 1), applied to the old endpoint, which has |T| <= B - 1. The counts come from interface.py and next_junction.py.

Checks of T1 to T4 (check_decomp.py): cand G_512 (id and swap) and cand G_1024^id, with 273707 / 272870 / 1344642 distinct triples, matching the archive. In all of them there are 0 opposite-sign constraints, 0 constraints across a diagonal-cell cut, and max d/(t + 4.5)^2 = 0.044 (the proved bound is 0.117). The B1024 id core lies in exactly three segments: 2313 labels in Sigma_8, 43508 in Sigma_9^id and 48205 in Tail_10^id.

5. L5. The certified system is invariant under adding kappa to every label. If (y, z) solves, so does (y + kappa, z + kappa). QED.

6. P6. With y_B fixed on Tail_512^id (ranks [699050, 786432) of the id-1024 parent) and O4 free, the relative core of O4 has a 15103-label component that is UNSAT from its lists, plus 17 singleton list components, of which 7 are UNSAT. By L5 and T4 (the parent's constraints touching C3 are exactly these), no shift helps. The witness is checkable by hand.
- Label u = rank 786444, cell (1020, 510), sees (old rank, value, delta, q):
  - (780972, 0, 0, 16416), the near-isosceles vector n = 32 with Y = 1025 and L = X + 1;
  - (780993, 0, -1, 16352);
  - (786328, 2, 2, 350), with X = 11200, Y = 1005, L = 11245.
- These forbid the residues 0, 2 and 1, so u is blocked.

The other placements: y_A (the id certificate) on Sigma_9^swap; the id certificate's first-child tail on Tail_1024^swap; and the swap certificate's third-child tail on Sigma_9^id. All three are UNSAT on a relative-core component (fe_test.py). child_check.py confirms that the four restrictions are certified solutions of cand G_512^id and cand G_512^swap.

7. P7.
- 512 to 1024 (interface.py, exact). The two K_A components (1719 and 1415 labels) remain unchanged components of the joint core, and no core crossing triple touches K_A. Tail_512^swap has an empty core.
- 1024 to 2048 (stab10.py). Build the cand system induced on Tail_10 plus the first 120000 ranks of W_10. Its core lies inside the full segment core, because cores are monotone under induced subsystems. In all four types, a K_A component merges with W labels: in (id,O4), 23081 K_A labels join 9729 other old labels and 61416 W labels. So stability is refuted. K_A recomputed in the 2048 frame matches the 1024 build (48205 and 29122 labels).

8. T8. Each component C of the core K lies in some Pi_i. Every label of C has at least M certified classes inside C, which is a subset of Pi_i, so C lies in K(Pi_i). K(Pi_i) is a subset of K, so the K(Pi_i)-neighbours of C lie in C. Hence C is a component of K(Pi_i), and any certified solution of Pi_i restricts to one of C. Distinct components of K share no constraint, so the choices combine, and Lemma CC (reverse peeling of certified classes) extends them to the chain. The converse holds because Pi_i is an induced subsystem. QED.

9. L9. Let K be the core of A + W_i.
- Containment: K intersected with A lies in K_A^Z. A label of K in A but not in Z has all its constraints in A, so it has at least M classes inside K intersected with A. The Z-anchored core is the largest subset of A in which every non-Z label has at least M classes inside.
- A component C of K that meets W_i: a path inside C from a label before J_{i-1} to W_i leaves A at a label z of Z. Its A-part lies in K_A^Z and connects that label to z. The hypothesis forbids this, so C lies in W_{i-1} union W_i.
- A component that misses W_i lies in K(A) and is closed there, so it is a component of K(A), and DEC for A applies.
QED.

10. C10 and C11.
- J_8 and J_9: full segment cores from dec9.py. Examples of component splits (before J_{i-1} / last old block / new block): (1719: 0/323/1396) and (1415: 0/0/1415) at J_8; (14877: 0/655/14222) and (23081: 0/0/23081) at J_9. No component spans two junctions.
- J_10: next_junction.py, a window of 124000 ranks, which is at least Dmax(1023) = 122160, so every crossing triple is captured. The anchored cores have 69, 38, 42 and 36 components, and none holds both a pre-J_9 label and a Z label.
- Below J_8 the cores are empty (the G_256 cores are empty).
So by T8 and L9: Sigma_10^g and Tail_11^g are certified-3-solvable iff Tail_10^g is (the archive certificate) and the four Pi_10 are.

pi_stage.py solved the four Pi_10 systems:
| Pi_10 | triples | certified core labels | core classes | CaDiCaL |
|---|---:|---:|---:|---|
| (id,O4) | 2267053 | 521431 | 1132634 | SAT in 18 s |
| (swap,O2) | 2300426 | 516262 | — | SAT in 39 s |
| (id,O2) | 2302662 | 545202 | — | SAT in 36 s |
| (swap,O4) | 2261960 | 492178 | — | SAT in 8 s |

Every model was checked on every core class, then extended by reverse peeling, with 0 certified violations on all of Pi. The cores of the (id,O4) system have components 187918 (junction: 32810 labels in W_9, 155108 in W_10), 306406 (interior of W_10), and repeated copies of 1402, 1415 and 4296.

The types with j <= 9 lie inside cand G_1024 of both orientations (archive certificates; nesting re-checked). The q-square uses Sigma_j for j <= 10 and Tail_11^id, so C11 follows.

M = 4: the empty weighted 4-cores of G_1024 pass to its induced subsystems, and the certified core lies inside the integer core.

C12: the h-independence of the types is T4, and monotonicity holds because every type with j <= k - 1 occurs in every q-square with q >= 2^(k+1).

## External results used

- Hilbert locality max(Dx^2, Dy^2) < 16|Dr| (audited Theorem 1, continuation_hilbert_placement.md); used in T1 to T4.
- Lemma CC and L9 (certified and integer M-core reduction, audited in audit_gap_mixing_combination_tools.md); used in T8 and C11.
- Archive certificates certificates_B1024_M3.npz (cand and gen, id and swap; unaudited, two-program checked); used in P6, C10 and C11.
- pysat 1.9.dev15 with the CaDiCaL 1.5.3 backend (already installed), used only to find SAT models; every model was verified and no UNSAT verdict is taken from it. No published theorem was used.

## Checks

Every script ran with py -B, one at a time. All runs were under 60 s and 1 GB except one solve_pi.py attempt, killed at its 300 s limit inside the pure-Python solver; I then used the staged CaDiCaL route. The repository was only read, no git command was run, and nothing was written outside script folder (7.9 MB). Hand proofs: T1 to T4, C4', L5, T8 and L9, plus the P6 witness. Exact computations: the decomposition checks at B = 512 and 1024 (0 violations), exact Dmax tables, the interface counts at both scales, the four cross-extension tests, the core-stability tests at both scales, the DEC tests at J_8, J_9 and J_10, and the four Pi_10 certificates (0 certified violations).

## Gaps

- No bounded-M theorem for all h. DEC was verified only at J_8, J_9 and J_10, and nothing proves it at larger scales. Heuristic warning: the interior core of W_10 is already one giant component of 306406 labels, so at J_11 the junction component may connect through it to the J_10 component, and DEC could fail. Then the reduction would need three-block systems.
- C11 is computer-assisted. The four Pi_10 certificates were checked only against my own builder's triple list (blk.py and stab10_kern.py are reimplementations of the archive builder). That builder reproduces the archive counts (1344642, 273707, 272870) and the K_A sizes in the 2048 frame, but no independent checker in the style of verify_full.py was run at the 2048 scale. Everything also rests on the archive's B1024 certificates, which are unaudited but were checked by two programs.
- All statements are for the cand version: no owner test and no row-range test. That is a superset of the real candidate constraints, so it gives solvability only. An UNSAT segment would not by itself obstruct the real system; that needs the in-strip, genuine-rival argument of Corollary A1. The decomposition T4 does not use Corollary A1.
- The UNSAT verdicts in P6 come from my list solver (forward checking at the root). The explicit singleton witness checks P6 by hand, independently of the solver. Integer (non-certified) extension of y_B was not tested.
- M = 4 is settled only through j <= 9 (Sigma) and j <= 10 (Tail), via empty 4-cores. Pi_10 at M = 4 was not built.
- P family only. R2s multiplicity, FW, 6PT, Lambda3/4, the sea and the collars are untouched. Nothing here is audited.
- The proved depth bound Dmax(2^j - 1) of about 0.117 * 4^j is about 5.6 times the observed depth of about 4^j/48. A sharper discrete L-infinity dilation constant for the Hilbert curve would close this gap; I did not prove or cite one.

## Missing estimate

To get every height at M = 3, two things are missing. The first is a scale-uniform statement about the junction systems: either DEC at every junction J_j, which reduces everything to the two-block systems Pi_j = W_{j-1} union W_j^a (four per scale), or a replacement for it if DEC fails once the interior cores of the blocks percolate. The second is a uniform certified-3-colourability theorem for those systems, or for whatever multi-block systems replace them. The decomposition shows that nothing else is involved: diagonal blocks never interact, and every coupling is a tail-to-block junction of first-off-diagonal blocks. What is missing in the end is a structure theorem for first-off-diagonal blocks of side 2^j at offset 2^j. Exact data: their certified cores grow from 0 (j <= 7) to about 5% of labels (j = 9) and about 40% (j = 10), with giant components at j = 10.

## Next steps

- Audit T1 to T4 and L5, T8 and L9. They are short and elementary, and T4 replaces the unaudited Corollary A1 for every positive (solvability) statement about cand.
- Independently verify the four Pi_10 certificates (pi_<g>_<attach>_sol.npy, int8 per rank of [J - 512^2, J + 1024^2)) with a checker that recomputes the Pythagorean pairs from the placed columns, as verify_full.py does, run in chunks under 60 s.
- Test DEC at J_11 locally, as at J_10: build the cand core of Tail_11 = Tail_10 + W_10 (about 1.4M labels) and the junction window into W_11. Pre-registered prediction: DEC fails, because the J_11 junction component reaches the J_10 component through W_10's giant interior component. If it fails, generalise T8 to k-block windows and find the least k for which the decomposition still holds.
- Study the first-off-diagonal block W_j as the primary object. Its corner sub-block is a translate of a W_{j-1}-type block, and the recurring components 1402, 1415 and 4296 appear in both W_9 and W_10. A recursive theorem for W_j, describing the components that sit at its start, its end and its self-similar corner, is the natural place for a scale invariant.
- Record in the ledger: T4 (exact chain decomposition, which makes the diagonal 2B-block question vacuous because C1 and C3 never interact); P6 (the naive extension invariant is false, with an explicit blocked label); P7 (core stability holds at 1024 and fails at 2048); and C11 (cand P certified-3-solvable at every h <= 4096). Scripts are in scripts_gm3_hier/: blk.py, check_decomp.py, lemma_check.py, interface.py, next_junction.py, stab10.py, stab10_kern.py, dec9.py, fe_test.py, listsolve.py, bw_core.py, witness.py, child_check.py, solve_pi.py and pi_stage.py, plus the certificates pi_*_sol.npy (7.9 MB in total).

