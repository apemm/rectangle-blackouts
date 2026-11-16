# Combining repairs on the full candidate graph

14 November 2026. Problem 001. Continues continuation_gap_mixing_audit.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: a cyclic block rule for the even-a class, an exact guarded combination theorem for repairs that states what each cut edge costs on the boundary (a crossing edge is cut by exactly M - |delta| deletions), and list versions with sharp exact certificates. For the actual Hilbert P graph, no decomposition with bounded boundary cost and bounded gap count is proved. Audited in audit_gap_mixing_combination_tools.md (T5 to T7 correct; T8 needs a universal quantifier over lists).

# Result

## Status

partial

## Summary

Three choices solve every two-gap full component at M = 3: a new cyclic block rule covers the even-a class that Theorem 2 left open. I also prove an exact guarded combination theorem for repairs, which states what each cut edge costs on the boundary, plus list versions with sharp exact certificates. For the actual Hilbert P graph, no decomposition with bounded beta and s is proved.

## Statements

Abstract setting as in continuation_gap_mixing_audit.md, Section 1. Fix a block size M >= 2. Ranks form a finite set of integers, and xi_r is in {0, ..., M-1}. A constraint (r, u, delta) with r < u forbids xi_u - xi_r = delta, where |delta| <= M-1. Its gap is q = M(u-r) + delta. Write sigma_M(q) = 1 if M | q or q < M, and sigma_M(q) = 2 otherwise.

T1 (cyclic block rule; proved). For integers g >= 1, c, phi and kappa, put xi_r = (c * floor((r+phi)/g) + kappa) mod M. Put n_q = floor(q/(Mg)). Let E_g(q) = {q/(Mg)} if Mg | q, and E_g(q) = {n_q, n_q + 1} otherwise. Every constraint of gap q is satisfied if c*e is not congruent to q mod M for all e in E_g(q). This holds on any rank set and for every phi and kappa.

T2 (two gaps at M = 3; proved). Every full candidate component with at most two distinct gaps has a solution with three choices. The new case is gaps 3a and 3b+s with a even, s in {1, 2} and b >= 0. Put w = v_3(a) and B = floor(b/3^w). Take g = 3^w if B is not congruent to 1 mod 3, and g = 2*3^w otherwise. Then n = floor(b/g) is not congruent to 1 mod 3. Take c = 3-s if n = 0 mod 3, and c = s if n = 2 mod 3. The T1 rule with these values solves the system on every finite rank set, for every phi and kappa. Odd a is Theorem 2 of the audit. Both bounds are sharp: two gaps can fail at M = 2 (gaps {2, 4} on ranks {0, 1, 2}), and three gaps can fail at M = 3 (gaps {3, 6, 9} on ranks {0, 1, 2, 3}). In general, the least M that solves all s-gap full components lies between s+1 and 2s.

T3 (binary palettes on Z; proved). The M = 3 system {3a, 3b+s} has a solution on all of Z using two values iff v_2(b) > v_2(a) or v_2(b+1) > v_2(a). So in the formerly uncovered class, every solution on Z uses all three values. By compactness, so does every solution on all sufficiently long intervals.

T4 (2-adic signature rule; proved; extends Theorem 3 of hilbert_gap_mixing_reduction.md). Fix t in {1, ..., M-1}. Let K be a component of the binding graph B_t (the constraints with delta in {0, t, -t}). Let A(K) be the rank differences of the delta = 0 constraints in K, and Bd(K) the rank differences of the delta = +-t constraints in K. Suppose some v >= 0 satisfies v_2(d) = v for all d in A(K) and v_2(d) > v for all d in Bd(K). Then xi = t*((floor((r+phi)/2^v) + eps) mod 2) satisfies every constraint inside K. If A(K) is empty, a constant works. Corollary: if every B_t-component has this signature, two values remove the whole P family. This contains archive Theorem 3 and both binary halves of audit Theorem 2.

T5 (guarded combination; proved). Partition the ranks into pieces. Every crossing constraint e = (r, u, delta) is made inactive by deleting M - |delta| values in total, split between its two endpoints, and no fewer deletions work. In particular, a crossing edge with |delta| = M-1 is cut by deleting one value at one endpoint of your choice. That value is M-1 at the end that would carry M-1 in an active pair, or 0 at the other end. If every piece is solvable from the resulting lists, the union of the piece solutions is a global solution. Special case (palette separation): take P with P - P inside D, and let the pieces be the components of the graph of constraints with delta in D. If each piece is solved with values in P on its boundary labels, all pieces combine with no lists.

T6 (M = 3 repair of B_1-components; proved). Take the pieces to be the components of B_1. Every crossing edge then has delta = +-2. Guard each crossing edge at its 2-end: the later endpoint when delta = +2, the earlier endpoint when delta = -2. Under these guards, the only deletion anywhere is the value 2 at guarded labels. Hence any assignment that solves each B_1-component inside and avoids 2 at its guarded labels is global. Such assignments exist for components with the T4 signature (t = 1), for components with no 3-divisible binding gap, and for any T1-solvable component whose guarded labels miss one residue class of floor((r+phi)/g) mod 3 for some phi. Any two guarded labels always miss one.

T7 (list versions; proved, with exact certificates). Increasing-rank greedy succeeds from lists L_u whenever |L_u| > sum over q in Q^-(u) of sigma_M(q), where Q^-(u) is the set of gaps of constraints from u to lower ranks. So a component with s gaps, k1 of them single-slot, is solvable from lists of size at least 2s - k1 + 1. With no gap divisible by M, any lists with a common value suffice. The size bound is sharp for one gap. Theorem 2 and T2 have no list-size version at M = 3: lists {1,2} on just two adjacent ranks make the covered system {3, 4} on {0, 1, 2} unsolvable.

T8 (ordered pieces; proved, elementary). Order the pieces R_1, R_2, and so on. Let beta(u) be the number of constraints from u into earlier pieces. If every piece is solvable from lists of size at least M - beta on its labels, a global solution exists. With greedy inner solvers, this condition implies global greedy on the concatenated order. So pieces only help when the inner solvers are structured (T1, T4), and by T7 those are not list-size robust.

## Proofs

Notation: p_e = M r_e + xi_e is the absolute slot of label e. A constraint of gap q says p_u - p_r is not q.

0. Slot facts. For a constraint (r, u, delta) of gap q, delta = q - Md with d = u - r, so delta is congruent to q mod M. Also |q/M - d| < 1, so d is in {floor(q/M), ceil(q/M)}, and d >= 1 removes floor(q/M) when q < M. If M | q, then delta = 0 and d = q/M. For a fixed label u and gap q, each admissible d gives one partner rank u - d (or u + d) and one delta. So u has at most sigma_M(q) constraints of gap q to lower ranks, and as many to higher ranks.

Shift lemma. For integers x, D >= 1 and g >= 1, floor((x+D)/g) - floor(x/g) is in {floor(D/g), ceil(D/g)}. Proof: write D = gm + rho with 0 <= rho < g. Then floor((x+D)/g) = m + floor((x+rho)/g), and floor((x+rho)/g) - floor(x/g) is 0 or 1, and 0 when rho = 0. Also, for an integer m >= 0, ceil((m+1)/g) = floor(m/g) + 1.

PROOF OF T1. Take a constraint (r, r+d, delta) of gap q. The values xi are the representatives in {0, ..., M-1}, so xi_{r+d} - xi_r is congruent to c*e mod M, with e = floor((r+phi+d)/g) - floor((r+phi)/g). By the shift lemma, e is in {floor(d/g), ceil(d/g)}. With d in {floor(q/M), floor(q/M) + 1}, floor(d/g) >= floor(floor(q/M)/g) = n_q (nested floors), and ceil(d/g) <= ceil((floor(q/M)+1)/g) = n_q + 1. If Mg | q, then d = q/M and e = q/(Mg). So e is in E_g(q). Because delta is congruent to q mod M, the hypothesis c*e not congruent to q makes xi_{r+d} - xi_r and delta incongruent mod M, so they differ. The argument uses no property of the rank set and no value of phi or kappa. QED.

PROOF OF T2. Let s' be the number of gaps. One gap is archive Theorem 3, or audit Theorem 1. For two gaps, let k0 be the number divisible by 3. If k0 = 0, constant zero works, since every delta is nonzero mod 3. If k0 = 2, audit Theorem 1 applies, because 3 > 2*2 - 2. If k0 = 1, the gaps are q0 = 3a and q1 = 3b+s. For odd a this is audit Theorem 2. Now let a be even, and apply T1 with M = 3.
- Gap 3a. Both candidates for g divide a: 3^w | a, a is even, and gcd(2, 3) = 1, so 2*3^w | a. Then E_g(3a) = {a/g}, and a/g is a/3^w or a/(2*3^w), neither divisible by 3. For c in {1, 2}, c*a/g is nonzero mod 3, which is the condition for q0 = 0 mod 3.
- Gap 3b+s. Here floor((3b+s)/(3g)) = floor(b/g). To see this, write b = gk + rho with 0 <= rho <= g-1. Then (3b+s)/(3g) = k + (3 rho + s)/(3g), and 3 rho + s <= 3g - 1. So E_g(q1) is contained in {n, n+1} with n = floor(b/g). We need c*{n, n+1} to miss s mod 3.
  - n = 0 mod 3: c*{0,1} = {0, c}, which misses s iff c is not s, so take c = 3-s.
  - n = 2 mod 3: c*{2, 0} = {-c, 0}, which misses s iff c is not -s mod 3, so take c = s.
  - n = 1 mod 3 is the only failure.
- Choice of g. With B = floor(b/3^w), nested floors give floor(b/(2*3^w)) = floor(B/2). If B = 1 mod 3, then B = 6k+1 or 6k+4, so floor(B/2) = 3k or 3k+2, neither 1 mod 3. So one of g = 3^w and g = 2*3^w always gives n not 1 mod 3. Every slot of both gaps is excluded on Z, hence on every rank subset and for any subset of constraints.
Sharpness at M = 2: gaps 2 and 4 give delta = 0 at rank differences 1 and 2, a triangle on {0, 1, 2}. At M = 3: gaps 3, 6 and 9 give delta = 0 at rank differences 1, 2 and 3, so {0, 1, 2, 3} is a K4 of not-equal constraints. In general, the gaps M, 2M, ..., sM on {0, ..., s} form a K_{s+1}, so M >= s+1 is necessary. Audit Theorem 1 gives M >= 2s sufficient. QED.

PROOF OF T3. Sufficiency is audit Theorem 2. For necessity, suppose xi = x0 + t' y with y: Z -> {0,1} and t' in {1, 2}.
1. The delta = 0 slot of 3a at difference a forces y_{r+a} = 1 - y_r. So y has period 2a.
2. The slots of q1 are (b, s) when b >= 1, and (b+1, s-3). Since {|s|, |s-3|} = {1, 2}, exactly one slot has |delta| = t'. Call its rank difference D, with delta = eps t'. The other slot can never be active under this palette.
3. If b = 0, the condition v_2(b) > v_2(a) holds trivially, so assume D >= 1.
4. Sum y_{r+D} - y_r over one period of length 2a. The total is 0, so the counts of +1 and -1 values agree. Forbidding one sign forbids both, and y_{r+D} = y_r for all r.
5. The periods of y form a subgroup containing 2a and D, so G = gcd(2a, D) is a period. If v_2(D) <= v_2(a), then v_2(G) = v_2(D) <= v_2(a), and the odd part of G divides a. So G | a, a is a period, and this contradicts y_{r+a} = 1 - y_r.
6. Hence v_2(D) > v_2(a). The four cases are: t' = 1, s = 1 gives D = b; t' = 1, s = 2 gives D = b+1; t' = 2, s = 1 gives D = b+1; t' = 2, s = 2 gives D = b. So the condition is v_2(b) > v_2(a) or v_2(b+1) > v_2(a).
Compactness: the palette is finite and each constraint involves two ranks. If [-N, N] had a two-valued solution for every N, König's lemma would give one on Z. The palettes {0,1}, {1,2} and {0,2} are finitely many. Finite check: on intervals of length 4a+2b+8, binary solvability matched the criterion for all 144 triples with a <= 8 and b <= 8. QED.

PROOF OF T4. All values lie in {0, t}, so every difference lies in {0, t, -t}. Non-binding constraints inside K therefore never fire. Take a delta = 0 constraint at rank difference d in A(K). Then d/2^v is odd, so floor((r+phi+d)/2^v) = floor((r+phi)/2^v) + d/2^v flips parity, and the difference is +-t, not 0. Take a delta = +-t constraint at d in Bd(K). Then 2^v | d and d/2^v is even, so the parity is unchanged and the difference is 0, not +-t. If A(K) is empty, a constant gives difference 0, which is not +-t. For the corollary: constraints between different B_t-components are non-binding, and every component uses values in {0, t}, so they never fire. Each component may use its own v, phi and eps. Special cases:
- One gap q with M | q: A = {q/M} and Bd is empty.
- One gap q with M not dividing q: A is empty.
- Audit Theorem 2 with t = s (s = 1: D = b; s = 2: D = b) is its first condition.
- Audit Theorem 2 with t = 3-s (D = b+1) is its second condition. QED.

PROOF OF T5. A crossing constraint (r, u, delta) is active exactly on the pairs (x, x+delta) with both x and x+delta in [0, M-1]. These form a matching of M - |delta| disjoint pairs. A set of deleted values at the two ends makes the constraint inactive for every remaining choice iff it is a vertex cover of this matching. That needs at least M - |delta| deletions, and M - |delta| suffice. For |delta| = M-1 the only active pair is (0, M-1) or (M-1, 0), so one deletion at either end works. With the deletions fixed, the inside constraints of each piece are solved within its lists, and every crossing constraint is inactive. So the union satisfies everything.
Palette case: a constraint between different components of G_D has delta outside D. Both endpoints are boundary labels with values in P, so the difference lies in P - P, which is inside D. It is therefore not delta. QED.

PROOF OF T6. Crossing edges between B_1-components are non-binding: delta is +-2 when M = 3. By T5, delta = +2 is active only for (xi_r, xi_u) = (0, 2), and delta = -2 only for (2, 0). Deleting 2 at the 2-end therefore kills the edge, and no other deletion occurs. For the solvable classes:
- The T4 rule with t = 1 uses only {0, 1}, so it never takes the value 2.
- Constant 0 never takes 2.
- In the T1 family with phi fixed, kappa -> xi_r is a bijection onto Z_3. If the guarded labels' block residues c*floor((r+phi)/g) mod 3 miss a class rho, take kappa = 2 - rho. Two guarded labels exclude at most two of the three kappa values.
All three cases satisfy the guard lists, so T5 applies. QED.

PROOF OF T7 AND T8. Greedy in increasing rank: each lower constraint (r, u, delta) forbids one value, xi_r + delta. Their number is at most the sum of sigma_M(q) over Q^-(u) (slot facts), which is at most 2s - k1 for a piece with s gaps. With no gap divisible by M, the common value c gives difference 0, and delta is nonzero mod M. T8 is the audit's Section 5 applied piece by piece, by induction. In the concatenated order, a label u in R_i has at most beta(u) + (2s - k1) earlier constraints. So the hypothesis with greedy inner solvers is exactly a global-greedy hypothesis.
Certificates, checked by hand:
(i) Gap 4 at M = 3 has slots (1, +1) and (2, -2). On ranks 0 to 4, the lists {0,2}, {1,2}, {0,2}, {0,1}, {0,2} admit no solution. If xi0 = 0, the slot (1, +1) forces xi1 = 2. The slot (2, -2) from rank 1 forces xi3 = 1. Then (1, +1) from rank 2 forces xi2 = 2, and (1, +1) from rank 3 forces xi4 = 0, which the slot (2, -2) from rank 2 forbids. If xi0 = 2, the slot (2, -2) forces xi2 = 2, then xi1 = 2 and xi3 = 1, with the same contradiction. So a two-slot single gap needs lists of size 3, the T7 bound.
(ii) Gaps {3, 4} (a = b = s = 1, covered by audit Theorem 2) on ranks 0 to 2, with L0 = L1 = {1, 2} and L2 = {0, 1, 2}. The constraints xi1 not equal to xi0 and xi1 - xi0 not 1 force (xi0, xi1) = (2, 1). Then xi2 is not 1 (delta = 0), not 2 (delta = +1), and not 0 (slot (2, -2) from rank 0).
Exhaustive search on [0, 12) at M = 3 found no failure with up to three restricted labels for any single gap q in {4, 5, 7, 8, 10, 11}. That is data, not a theorem.

HILBERT P GRAPH: WHAT IS PROVED ABOUT beta AND s.
(H1) Rank-ordered pieces (intervals of Hilbert rank). By slot facts and the uniqueness lemma (one gap per factor, role and side; the lower side is fixed), beta(u) <= 2|Q^<(u)| <= 4F^<(u). Here Q^<(u) is the set of gaps to earlier pieces and F^<(u) the number of distinct factors among those constraints. This only recovers b^- <= 4F^-, with the factor-count replaced by a gap count. No uniform bound in h is known.
(H2) Diagonal lines as pieces. By archive Lemma 2, each line T carries at most one gap of each factor a <= S^2/32. By T1 of hilbert_p_family_counts.md, a smaller half-factor below S^2/4 is odd. So the small-factor gaps on a line number at most S^2/64, which is 16 at S = 32. Large factors have no per-line bound, and constraints between lines have |Delta T| < 8 sqrt(q), so beta is uncontrolled. Combined with audit Theorem 1, this needs M >= S^2/32, worse than the finite-factor theorem.
(H3) B_1-pieces at M = 3 with 2-end guards (T6). beta counts only deletions of the value 2. A label has at most two far-slot crossing edges per non-divisible gap in its full gap set, one per side, because the far slot of a gap is unique. Lists are never empty. Every list contains {0, 1}.
(H4) 2-adic range (from T1 of the counts note). A divisible gap q = 3a has v_2(a) = v_2(q) = v_2(e'), and L >= 4^{v_2(q)} S^2/4 + 1. So v_2(a) <= log_4(4(h-2)/S^2). At S = 32 and h <= 4096, v_2(a) is 0 or 1. Nothing bounds v_3(a) or the valuations of the rank differences in Bd(K).

WHAT REMAINS FOR P AT BOUNDED M (exact form, at M = 3). By T5 and T6, the P family at M = 3 is solved once the full candidate graph has a partition with guards in which every piece is solvable from its guard lists. Proved piece types:
- full components with at most two gaps (T2), which need no guards;
- B_1-components with the T4 signature, or with no 3-divisible binding gap, under 2-end guards;
- T1-solvable components whose guarded labels miss a block residue.
Not proved for the actual Hilbert graph:
(R1) any bound on the number of gaps in full or B_1 components;
(R2) any rule for pieces with three or more gaps that fail both the 2-adic and the cyclic criteria. Such pieces can be infeasible in the abstract (the K4 {3, 6, 9}), so Hilbert or arithmetic input is needed to exclude them;
(R3) any control of the guarded sets of components that need the value 2.

## External results used

- None. Everything uses only the archive's audited inputs: the slot structure, Theorems 1 and 2 and Section 5 of continuation_gap_mixing_audit.md, Lemma 2 and Theorem 3 of hilbert_gap_mixing_reduction.md, T1 of hilbert_p_family_counts.md, and the uniqueness lemma in Section 7 of continuation_hilbert_factor_one_choices.md. It also uses the elementary floor identities and König's lemma (compactness for finite palettes), both standard.

## Checks

I proved every theorem by hand and ran four scripts as sanity checks only, each with py -B, under 60 s and well under 1 GB. The repository was only read. Scripts are in scripts_gm1_combine/:
- lists.py: an exact backtracking solver on rank intervals with the full slot constraints. It finds the list certificates of T7: gap 4 at N = 5 with all lists of size 2, and gaps {3, 4} with two restricted labels. Single-slot gaps 1 and 2 never fail with lists of size 2.
- checks2.py, three checks:
  - single two-slot gaps on [0, 12) were never killed by up to three size-2 lists;
  - the binary-palette criterion of T3 matched exact interval solvability for all 144 triples with a, b <= 8 and s in {1, 2};
  - the T4 rule over 4000 random systems with M from 2 to 6 gave 0 violations in 203,650 constraints.
- z3rule.py, two checks:
  - the T1 rule on 2,774 random two-gap systems, random phase and offset, and 150 random ranks gave 0 violations in 285,738 constraints;
  - the criterion (some g | a with 3 not dividing a/g and floor(b/g) not 1 mod 3) covered all 66,642 formerly uncovered pairs with a <= 200 even and b <= 1000.
- even_a_proof_check.py, two checks:
  - the exact rule from the proof of T2 (g in {3^w, 2*3^w}, c as stated), for every even a <= 40, b <= 120, s in {1, 2}, every phi < 2g and every kappa, on ranks -150 to 399, gave 0 violations in 127,774,464 constraints;
  - it confirmed that {3, 6, 9} on {0, 1, 2, 3} has no three-valued solution.
I did not rerun any Hilbert census.

## Gaps

- No decomposition of the actual Hilbert P candidate graph is proved to have bounded beta and bounded s. (H1) only reproduces the local factor budget b^- <= 4F^-, with gaps replacing factors, and no uniform bound in h is known.
- T2 settles the abstract two-gap, three-choice case. It says nothing about how many gaps actual Hilbert components carry. Mixed B_1-components are 7.0% to 12.3% of binding components in the archive data, which is data, not a theorem.
- T2 is new and has not had an independent audit. It needs one, especially the shift-set inclusion E_g(q) in {n, n+1} and the case split on n mod 3.
- Three-gap components at M = 3 are not always solvable (the K4 {3, 6, 9}). Whether the Hilbert M = 3 candidate graph contains such an obstruction is not checked here. Archive certificates show three choices suffice at h = 2048 and 4096.
- The guarded combination (T5, T6) is exact for one fixed guard placement. I have no theorem on choosing guards well, for example placing them at 0-ends inside binary pieces that use phase or complement freedom.
- The finite-interval form of T3 rests on compactness, with no explicit interval length. Only intervals of length 4a+2b+8 for a, b <= 8 were checked.
- The least M that solves all s-gap full components is only bracketed: s+1 <= M_s <= 2s. It is exact only for s = 1 (M = 2) and s = 2 (M = 3).
- Priority 3 (R2s multiplicity on one label pair) and the other five H7 families are not addressed. Nothing here proves a quadratic-width board.

## Missing estimate

At bounded M (take M = 3), the P family is solved once the full candidate graph has a partition with guards (T5) whose pieces are each solvable from their guard lists. The missing Hilbert input is one of the following:
(a) every full candidate component at M = 3 carries at most two distinct gaps, which T2 then solves outright;
(b) every B_1-component that needs the value 2 has at most two guarded labels, or guarded labels that miss a block residue mod 3, and satisfies T1;
(c) a rule for components with three or more gaps that fail both the 2-adic (T4) and the cyclic (T1) criteria.
Option (c) must use the geometry, because abstract three-gap systems can be infeasible at M = 3. Quantitatively, (a) or (b) needs a bound, uniform in h, on the number of distinct gaps per component, or on far-slot crossing edges per bad component. The archive's mean-degree model (mu about (16/(pi S)) log(4h/S^2), a model, not a theorem) predicts that (a) fails at fixed S for large h. That would leave (b) or (c).

## Next steps

- Have someone audit T2 independently (the cyclic block rule for even a): the shift lemma, the nested-floor identity floor((3b+s)/(3g)) = floor(b/g), and the choice g in {3^w, 2*3^w}. Then record the abstract two-gap, three-choice case as settled. Arjun's priority 1 is then done in the abstract.
- Extend T1 to three gaps at M = 3. Characterize which triples of gaps the binary (T4) and cyclic (T1) families jointly cover. Then find the exact infeasible triples beyond delta = 0 cliques, using one small exact search per triple class, not a census.
- Pin down M_3 in [4, 6]: are all three-gap full components solvable at M = 4? Try the cyclic rule mod 4, and layered residue rules mod 2 and mod 3 at M = 6.
- On the existing h = 4096, S = 32, M = 3 certificate data (no new census), classify the B_1-components by T4 signature or no divisible binding gap, by T1-solvability, and by the rest. For the rest, record the gap counts and the 2-end guarded sets. This tests (R1) and (R3) directly.
- Search the M = 3 Hilbert candidate graph at h = 4096 for a delta = 0 K4: four labels pairwise joined by 3-divisible gaps. This is the simplest exact obstruction to three choices for P.
- Study the guard-placement problem: each far-slot crossing edge picks its 2-end or its 0-end. With binary pieces this becomes a 2-SAT over phase and complement bits. Look for a condition under which it is always satisfiable.

