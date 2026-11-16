# The two-block systems across scales

15 November 2026. Problem 001. Continues the gap-mixing notes of 2026-11-14 (continuation_gap_mixing_audit.md, p_excursion_decomposition.md, p_cross_scale_chains.md). Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (partial): no proof that the two-block systems are solvable at every scale, and no obstruction. Proved: an exact self-similar description of the geometry of the two-block systems and two scale-uniform arithmetic facts; exact data show that the constraints are new at each scale, so solvability at one scale does not transfer by translation. Not audited yet.

# Result

## Status

partial

## Summary

I did not prove that Pi_j is solvable for every j, and I found no obstruction. I did prove an exact self-similar description of Pi_j's geometry and two scale-uniform arithmetic facts, and exact data shows the constraints are new at each scale.

## Statements

Setting: S = 32 and the cand version (no owner test, no row-range test). A label is a Hilbert cell (x, y) with odd row 2x+1, even row 2y+2 and diagonal T = y - x. A pair v, w with ranks r_v < r_w and d = r_w - r_v has two cross diagonals, U1 = y_w - x_v and U2 = y_v - x_w, with Y_i = |2U_i + 1|. The pair carries the triple (v, w, delta) when (32q)^2 + Y_i^2 is a square for some i, where q = Md + delta and |delta| <= M - 1. "Certified" means y_w - y_v is not congruent to q mod M. H_n is the recursion-(2) curve. tau(x,y) = (y,x). alpha_n(x,y) = (n-1-y, n-1-x). rho = tau alpha.

THEOREM 1 (exact type recursion; proved).
(a) Classes. Let B be an aligned block: side s = 2^i and corner (x0, y0) with s | x0 and s | y0. Its local curve is one of H_s, alpha H_s, tau H_s, rho H_s. Call {H, alpha H} class id and {tau H, rho H} class swap. The centre offset of B is c = y0 - x0 = k s, with k an integer.
(b) alpha-invariance. Let beta(x,y) = (x0+y0+s-1-y, x0+y0+s-1-x). This map sends B to itself, preserves T and swaps U1 with U2. Together with diagonal translation, it shows that the cand triple set of B (in local ranks) depends only on its type (s, k, class), at every M. Class id and class swap give different systems.
(c) Children rule. The four children of a type (2s, k, o) block, in rank order, have side s and these types:
- o = id: (2k, swap), (2k+1, id), (2k, id), (2k-1, id).
- o = swap: (2k, id), (2k-1, swap), (2k, swap), (2k+1, swap).
For a main-diagonal block (k = 0) this gives Theorem A: C1 has the other class and C3 keeps the class. For an id block, O2 = (1, id) and O4 = (-1, id). For a swap block, O2 = (-1, swap) and O4 = (1, swap).
(d) Chain blocks and the four Pi_j. If the P_i are id, every W_i = O4(P_{i+1}) has type (2^i, -1, id). If they are swap, W_i has type (2^i, +1, swap). The four two-block systems are therefore:
- Pi_j^1 = (2^{j-1}, -1, id) + (2^j, -1, id)
- Pi_j^2 = (2^{j-1}, -1, id) + (2^j, -1, swap)
- Pi_j^3 = (2^{j-1}, +1, swap) + (2^j, +1, swap)
- Pi_j^4 = (2^{j-1}, +1, swap) + (2^j, +1, id)
In archive labels these are (id,O4), (id,O2), (swap,O4) and (swap,O2).
(e) Corner copy. In Pi^1 and Pi^3, the second child of the new block W_j is a diagonal translate, with ranks shifted, of the old block W_{j-1}, so its cand system is exactly that of W_{j-1}. In Pi^2 and Pi^4, the fourth child of the new block is a translate of the previous block of the same O2 type.
(f) Junction anatomy, the same at every scale. The junction J_j sits on the line |T| = 2^j.
- Old side: the last-descendant chain of W_{j-1} has types (2^{j-1-i}, -/+(2^{i+1}-1), same class), i >= 0. Its offsets are -/+(2^j - 2^{j-1-i}), so it approaches |T| = 2^j from below.
- New side: the first-descendant chain of the new block has types (2^{j-i}, -/+2^i, alternating class). Every one of these blocks is centred exactly on |T| = 2^j.
(g) Refinement (the exact self-similar description). Coarsening by 2 x 2, that is cells (x//2, y//2) and ranks r//4, maps a type (2s, k, o) curve onto a type (s, k, o) curve. So Pi_{j+1}^a = R(Pi_j^a) as rank-ordered cell sequences, up to diagonal translation. Here R replaces each cell by its four children in the Hilbert order of its class. The scale-transition operations of T4 commute with R.

REMARK 1.7 (the constraints do not refine; exact data, plus a short reason). If v' and w' refine v and w, then U' is in 2U + {-1, 0, 1} and d' is in 4d + [-3, 3]. Whether a pair is constrained depends on the arithmetic set Gamma = {(U, d) : 2U+1 has a leg 32q with |q - Md| <= M - 1}, and R does not preserve Gamma. Exact counts (M = 3):
| W_j to W_{j+1} | constrained parent pairs | with a constrained refined pair | refined-constrained parent pairs | of those, parent unconstrained |
|---|---:|---:|---:|---:|
| j = 6 | 3286 | 913 | 9083 | 8170 |
| j = 7 | 15677 | 1249 | 48133 | 46884 |
| j = 8 | 83256 | 1580 | 233515 | 231935 |
So any self-similar induction must carry arithmetic information about Gamma at every scale. A combinatorial invariant of Pi_j cannot propagate by itself. P6 is one instance of this.

THEOREM 2 (mod-3 support; proved, every scale). At M = 3, with any S not divisible by 3, every triple with q not divisible by 3 has a cross pair with 3 | Y, that is, U congruent to 1 mod 3. So the certified M = 3 system is a proper-colouring graph G0 on the triples with 3 | q (y_w != y_v), plus twisted edges (y_w - y_v != q mod 3, q nonzero mod 3) that come only from cross diagonals with U congruent to 1 mod 3. Exact check: 0 violations on 147762 such triples of cand G_512 id and 200000 of cand G_1024 id.

THEOREM 3 (leg spacing; proved).
(a) The legs of an odd Y are X_a = (Y^2/a - a)/2, one for each divisor a < Y of Y^2. For a1 < a2: X_{a1} - X_{a2} = (a2 - a1)(Y^2 + a1 a2)/(2 a1 a2).
(b) If Y has three legs in an interval of length H, then Y < H^6/8.
(c) For each H, the number of odd Y <= N with two legs within H of each other is O_H(log N). Each such Y comes from one of finitely many generalized Pell equations, depending on H.
(d) Corollary. The q-window of a rank distance d spans X-length H = 64(M-1). If min(|U1|, |U2|) >= H^6/16 + 1, a pair carries at most 4 gaps. Then no pair forbids all 2M - 1 integer differences when M >= 3, and no pair forbids all M certified residues when M >= 5. Two-label obstructions therefore disappear at large scale for these M.

PROPOSITION 4 (exact, computer-assisted).
(a) Among odd Y <= 2*10^6, only Y = 8463 (q = 712 and 713, d in {237, 238}) and Y = 260865 (q = 510 and 511, d = 170) have two legs with distinct residues mod 3 in one window [3d-2, 3d+2]. No Y in that range has three legs in one window.
(b) Neither has a second cross diagonal within 16 sqrt(d) that supplies the missing residue. Those would be q = 711 or 714 for 8463, and q = 509 or 512 for 260865.
(c) So at M = 3, no pair with max(|U1|, |U2|) < 10^6 is certified-blocked or integer-blocked. Inside every Sigma_j and Tail_j with j <= 17, where |U| < 2.37|T| + 11 < 10^6, every certified (or integer) 3-unsolvable subsystem has at least three labels.

STATUS OF THE TARGET.
- Not proved: certified 3-solvability of Pi_j for all j, a propagating invariant, or a colouring rule.
- No obstruction was found or proved.
- The question for fixed larger M is not decided.
- Heuristic only, not proved: on the blocks W_j, triples per label grow (0.804, 0.957, 1.271, 1.503, 1.776 for j = 6 to 10). The certified 3-core grows from 0 to 3.4%, 16.4% and 44.3% of labels, and its mean certified degree from 3.88 to 3.96 and 4.37 (j = 8 to 10). If the structure behaved like a random Z_3-gain graph, certified M = 3 would fail at a moderate scale, roughly j = 12 to 14, and each fixed M would fail later. This is a prediction, not a result.

## Proofs

PROOF OF THEOREM 1.
(a) Induct on depth. H_{2n} is tau(H_n) on [0,n)^2, then H_n + (0,n), then H_n + (n,n), then alpha_n(H_n) + (n,0). Q4 = (2n-1-y, n-1-x) is alpha_n followed by translation by (n, 0).

The set V = {1, tau, alpha, rho} is the Klein group. Each g in V sends aligned children to aligned children and restricts to the same-named symmetry at half size. For example, alpha_{2n}(x+a, y+b) = alpha_n(x, y) + (n-b, n-a). So if B's local curve is g(H_{2n}), each child's local curve is g_n composed with tau, 1, 1 or alpha, which is again in V. Ranks of aligned blocks are contiguous by the same induction.

(b) In local coordinates, beta(x,y) = (s-1-y, s-1-x) about the centre of B. The new diagonal is T' = (c' - x) - (c' - y) = T. The new cross diagonals are
- U1' = (c' - x_w) - (c' - y_v) = y_v - x_w = U2,
- U2' = U1,
where c' = x0+y0+s-1.

The kernel tests both roles, so the triple set at (r, r+d) depends on d and the unordered pair {Y1, Y2}. Hence it is unchanged under beta, and beta maps placed H to placed alpha H, and tau H to rho H. A diagonal translation (x, y) -> (x+t, y+t) fixes U1, U2 and d. The only data left are s, c and the class.

Check (type_check.py): the cand systems of H and alpha H at offsets 256, 512, -256 and -768 (s = 256) are identical: 83515, 100463, 83265 and 102087 triples. tau H differs in every case.

(c) Inside the parent, the children at local positions (0,0), (0,n), (n,n) and (n,0) have centre offsets c, c+n, c and c-n. With c = 2n k, these are 2k, 2k+1, 2k and 2k-1 in units of n.
- For the curve H, the rank order is (0,0) with tau (swap), (0,n) with 1, (n,n) with 1, and (n,0) with alpha (id).
- For tau H, transpose the positions and multiply the classes by tau: (0,0) id, (n,0) swap, (n,n) swap, (0,n) swap.
- The representatives alpha H and rho H give the same type sequence. alpha maps positions (0,0), (0,n), (n,n), (n,0) to (n,n), (0,n), (0,0), (n,0), with classes alpha tau (swap), alpha, 1 and 1. By (b) the systems agree in any case.
Check: all 5456 aligned blocks of sides 4 to 64 in the 256-curve follow the rule, with 0 mismatches.

(d) Apply (c) with k = 0 to the id and swap diagonal blocks. In Tail chains all P_i share one class (T4). O4 is the fourth child and O2 the second.

(e) Apply (c) to (2^j, -1, id): the children are (-2, swap), (-1, id), (-2, id), (-3, id). The second child has type (2^{j-1}, -1, id), the type of W_{j-1}. By (b) the systems coincide.
- The swap case is similar: (2, id), (1, swap), (2, swap), (3, swap).
- For O2 types: (2^j, 1, id) has children (2, swap), (3, id), (2, id), (1, id), whose fourth child is (1, id). (2^j, -1, swap) has fourth child (-1, swap).
Check: for j = 7 and 8, the second child of W_j equals W_{j-1} translated by (64, 64) and (128, 128), with identical cand systems (3295 and 15686 triples).

(f) The last child of type (k, id) is (2k-1, id). Starting from k = -1, this gives k_i = -(2^{i+1}-1) at side 2^{j-1-i}, so the offset is k_i 2^{j-1-i} = -2^j + 2^{j-1-i}.

The first child of (k, id) is (2k, swap), and the first child of (k, swap) is (2k, id). So from (2^j, -1, o) the offset k s stays at -2^j while the class alternates. The swap-side cases are mirror images, using the last-child rule (2k+1, swap).

(g) Coarsening commutes with the recursion. coarse(H_{2n}) = H_n by induction (base coarse(H_2) = H_1), and coarse(g H_{2n}) = g_n coarse(H_{2n}) for g in V, because each g maps aligned 2 x 2 blocks to aligned 2 x 2 blocks with block index map g_n. Offsets halve together with the side, so k is preserved.
Check: for j = 6, 7 and 8, coarsened W_{j+1} equals W_j exactly, and the 4-rank groups are 2 x 2 blocks.

REMARK 1.7. y_{w'} is in 2y_w + {0,1} and x_{v'} is in 2x_v + {0,1}, which gives U' and d' as stated. The table comes from refine_check.py. It is exact data, not a theorem about all j.

PROOF OF THEOREM 2. In any Pythagorean triple, 3 | XY: if neither leg were divisible by 3, then X^2 + Y^2 would be 2 mod 3, which is not a square. If 3 does not divide q, then 3 does not divide X = 32q, so 3 | Y = |2U+1|, which means U is 1 mod 3. A triple with q divisible by 3 has delta = 0, since |delta| <= 2, and its certified form is y_w != y_v.

PROOF OF THEOREM 3.
(a) Y^2 = (L - X)(L + X) with both factors odd. Put a = L - X < Y. Then X = (Y^2/a - a)/2, and subtracting two such expressions gives the formula.

(b) Let a1 < a2 < a3 < Y be odd, so each difference a_l - a_i is at least 2.
- X1 - X2 > (a2 - a1)Y^2/(2a1a2) >= Y^2/(a1a2). Since this is at most H, a1a2 > Y^2/H, and so a1 > Y/H.
- X1 - X3 > (a3 - a1)(Y^2/(a1a3) + 1)/2 > a3 - a1, so a3 - a1 < H.
- gcd(a_i, a_l) is odd and divides a_l - a_i, which is even, so it is at most (a_l - a_i)/2 < H/2.
- lcm(a1, a2, a3) divides Y^2 and is at least a1a2a3/(g12 g13 g23) > 8a1^3/H^3.
Hence Y^2 > 8Y^3/H^6, that is, Y < H^6/8.

(c) Two legs with D = X1 - X2 <= H give a2 = a1 + 2 delta with 2 delta < D, and 2a1a2 D = 2 delta (Y^2 + a1a2). So Y^2 = a1a2(D - delta)/delta.
- Let g = gcd(a1, a2). It divides 2 delta and is odd, so g | delta. Write a1 = g alpha and a2 = g beta with gcd(alpha, beta) = 1. Then alpha beta delta(D - delta) = (Y delta/g)^2 is a square.
- Write alpha = A u^2 and beta = B v^2 with A and B squarefree and coprime. Then AB = sqf(delta(D - delta)), so there are finitely many pairs (A, B) for each (delta, D, g). Also B v^2 - A u^2 = 2 delta/g, with u, v < sqrt(N).
- If AB = 1, the equation v^2 - u^2 = c has finitely many solutions. Otherwise multiply by B: (Bv)^2 - AB u^2 = Bc with AB not a square. Its solutions form finitely many classes, each an orbit of the unit group, so O(log N) of them have height at most sqrt(N).
- Y is determined by the data. Summing over D <= H, delta < D/2 and g | delta gives O_H(log N).
Both examples fit. For Y = 8463: a = 1519, 1521, g = 1, A = 31, u = 7, B = 1, v = 39, and v^2 - 31u^2 = 2. For Y = 260865: a = 245025, 245055, g = 15, A = 15, u = 33, B = 17, v = 31, and 17v^2 - 15u^2 = 2.

(d) The window q in [Md-(M-1), Md+(M-1)] spans X-length 32(2M-2) = 64(M-1). If Y >= H^6/8, each cross pair contributes at most 2 gaps by (b), so a pair carries at most 4. That is fewer than 2M - 1 integer differences when M >= 3, and fewer than M residues when M >= 5.

PROOF OF PROPOSITION 4.
- nt_double_legs.py enumerates, for every odd Y <= 2*10^6, the divisors of Y^2 by sieve factorisation and keeps the legs with 32 | X. It finds three pairs with |q1 - q2| in {1, 2, 4}. One of them, Y = 390609 with q = 13205 and 13209, lies in no common window, because 13205 is not 1 mod 3. It finds no Y with three distinct residues in one window.
- Sanity checks: the legs of 255 are {1, 1016}, of 247 {3}, of 1025 {16416} and of 1005 {350}, matching the archive and the P6 witness.
- A certified-blocked pair needs all 3 residues from the gap sets of Y1 and Y2, so one Y needs two distinct residues in the window: a double. If max Y <= 2*10^6, that Y is 8463 or 260865 and d is forced.
- By T1 both cross diagonals have the sign of T, so |Y1 - Y2| = 2|U1 - U2| <= 2(|dx| + |dy|) < 16 sqrt(d). That is below 247 for d <= 238.
- y_for_leg.py lists every Y with a given leg. q = 711: nearest values 11811, 13825, ... . q = 714: 4945, 9911, ... . q = 509 and q = 512: no value within 210 of 260865.
- The case Y1 = Y2 gives only two residues.
- Integer-blocked means all 5 values q = 3d-2, ..., 3d+2, which cover all 3 residues, so it implies certified-blocked.
- The chain bound uses |U - T_z| < 4 sqrt(d) and d < 0.116627(t+4.5)^2 + 1 (section 0 of p_cross_scale_chains.md). Together these give |U| < 2.366t + 10.2, which is less than 620300 for t <= 2^18 - 1.
Supporting data: cand G_1024 id has 1212 pairs with 2 residues and 0 with 3, and every one of them has Y <= 4095, so it comes from two different cross pairs, as (c) predicts.

## External results used

- Classical structure of x^2 - n y^2 = m with n > 0 not a square: the solutions form finitely many classes, each an orbit of the unit group of Z[sqrt n], so O(log V) of them have height at most V (for example Nagell, Introduction to Number Theory, chapter on Pell equations). Cited from memory and not re-fetched. Used only in Theorem 3(c).
- 3 | XY for every Pythagorean triple (elementary, proved inline).
- Archive inputs, used as stated: T1 sign separation, the Hilbert locality max(dx^2, dy^2) < 16d (audited Theorem 1 of continuation_hilbert_placement.md), the crude depth bound and the definitions of T4 from p_cross_scale_chains.md (unaudited), and the kernel in blk.py (copied, read-only).

## Checks

I wrote every proof by hand first and then ran small exact checks. Each script ran one at a time, in under 15 s and well under 1 GB. The scripts are in scripts_gm4_pi_induction/ (126 KB). blk.py there is a byte copy of the archive's builder.
- type_check.py: children rule on 5456 aligned blocks with 0 mismatches. alpha-invariance on 4 offsets: identical triple sets, and tau gives a different set. Corner copy for j = 7 and 8: identical cell sequences after diagonal translation and identical cand systems.
- refine_check.py: coarsened W_{j+1} equals W_j exactly for j = 6, 7, 8, plus the non-refinement counts in Remark 1.7.
- double_edges.py: cand G_512 id gave 273707 triples, matching the archive, with 588 two-residue pairs. cand G_1024 id gave 1344642 triples, matching, with 1212 two-residue pairs and 0 three-residue pairs. The mod-3 lemma had 0 violations.
- wj_density.py: triples, triples per label, certified 3-core size and core mean degree for W_6 to W_10.
- nt_double_legs.py and y_for_leg.py: Proposition 4 (2*10^6 in 12.6 s).
- sanity_legs.py: leg lists against archive values.
Hand checks: Lemma 1.1 (beta swaps U1 and U2 and preserves T), the children rule for all four representatives, junction offsets, the coarsening induction, Theorem 2, Theorem 3(a) to (c) including both Pell examples, and the chain bound |U| < 2.366t + 10.2.

## Gaps

- The target is not met. Nothing proves that Pi_j is certified-3-solvable for all j, and no obstruction is proved. Theorem 1(g) gives an exact self-similar description of the geometry only, and the exact data in Remark 1.7 shows the constraints do not refine (for example, at j = 8 only 1580 of 83256 constrained parent pairs have a constrained refined pair). Any working induction must control the arithmetic set Gamma at every scale.
- No invariant of the certified solution sets was found that propagates across scales. Together with P6, Remark 1.7 suggests that no purely combinatorial invariant can work, but I did not prove an impossibility theorem.
- Structural colouring rule: Theorem 2 is the only scale-uniform residue structure I found. It does not give a rule. The proper-colouring part G0 behaves like an arithmetic, pseudo-random graph.
- The question for fixed larger M is not decided. Theorem 3(d) only removes two-label obstructions at large |U|: for M >= 3 integer and M >= 5 certified, and for M = 3 at every scale j <= 17 (Proposition 4). Larger obstructions are not addressed. The growth of mean degree and core size is exact data for j <= 10 together with a random-CSP heuristic. It is not a theorem, and the archive's model gives log h growth for the strip system, not for cand.
- Theorem 3(c) relies on the classical finite-class structure of generalized Pell equations. I cited it from memory and did not re-read a source. Its constant is not explicit.
- Proposition 4 is computer-assisted: one enumeration up to 2*10^6, plus a short divisor list for four values of q. No second program was run.
- Everything here is for cand. An obstruction in cand would not obstruct the genuine system, and solvability statements need the subsystem relation already used in C11. DEC at J_11 was not tested, because the junction window (Dmax(2047) is about 4.9*10^5 ranks) is far beyond 60 s with the archive kernel.
- Process note: my first two runs imported scripts_gm3_hier/blk.py in place. Python and numba (cache=True) then created scripts_gm3_hier/__pycache__ in the read-only repository (blk.cpython-314.pyc, blk.kernel-40.py314.1.nbc and .nbi, at 01:50 and 02:10). I deleted exactly those files and the empty directory I had created. Only the folder's modification time changed. All scripts now import a local copy of blk.py in the script folder. I ran no git command that changes state, and I did not touch Kagey-Problems.
- Nothing here is audited.

## Missing estimate

To get every j, two things are needed, and both are now sharply located.

First, a statement about the arithmetic set Gamma = {(U, d) : 2U+1 has a leg 32q with |q - 3d| <= 2} restricted to the refinement tower R^n(Pi_j). Theorem 1 fixes the geometry exactly at all scales: each junction is the meeting of an end corner approaching |T| = 2^j with a first-descendant chain centred on |T| = 2^j. The exact data shows that Gamma is essentially uncorrelated across one refinement step (at j = 8, 1.9% of constrained parent pairs have a constrained refined pair).

Second, a DP-3-colouring theorem for the Z_3-gain graphs this produces. The graph is the proper-colouring part G0 plus twisted edges supported on U congruent to 1 mod 3 (Theorem 2), with multi-residue pairs logarithmically rare (Theorem 3).

The data rules out a cheap version of this. Core mean certified degree is 3.88, 3.96 and 4.37 for j = 8 to 10. For an obstruction, the missing piece is an explicit certified-unsatisfiable subsystem. By Proposition 4 it must have at least three labels up to j = 17, and by Theorem 3(d) it must grow with M at large scale.

## Next steps

- Audit Theorem 1, parts (b), (c), (f) and (g), and Theorem 3(b) and (c). Each fits on half a page. Theorem 1(g) gives T4's chains an exact refinement structure, and 1(b) explains the archive's id/swap dichotomy.
- Record in the ledger: the types (s, k, class), the children rule, the junction on |T| = 2^j, Pi_{j+1} = R(Pi_j) with constraints not refining, the mod-3 support lemma, and 'no certified or integer blocked pair at M = 3 for j <= 17'.
- Pre-registered prediction to test on one fixed system: the certified 3-core mean degree of W_11 exceeds 4.6, and the core fraction exceeds 60%. A chunked build of the single block W_11 (4.2M labels) gives this without SAT. If the prediction holds, test certified 3-solvability of the densest type at the next scale, (2^11, -2, swap) (the first child of W_12, 4.2M labels), in chunks or with an UNSAT core.
- If an UNSAT type appears, it obstructs every Pi_j containing that type, by Theorem 1(b) and (e). Prove the reachability claim I only observed: from (-1, id), every k in [-(2^{l+1}-1), -1] occurs at depth l. That would make a single UNSAT type a persistent obstruction for M = 3 in cand.
- For fixed larger M, use Theorem 3(d): every obstruction at large |U| needs more than M/4 labels, so search only for dense subsystems (cores), not local patterns. M = 4 needs the same pipeline at scales beyond j = 10, where the 4-core first appears.

