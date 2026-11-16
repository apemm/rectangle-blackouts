# Synthesis: gap mixing after the two-gap theorem

14 November 2026. Problem 001. Continues continuation_gap_mixing_audit.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: (i) the three-choice two-gap case is settled by proof, by three independent constructions (Beatty, block and 3-adic rules); every full component with at most two gaps is solvable at M = 3, and with M choices some M gaps fail, so the least M for s gaps lies between s + 1 and 2s and is exact for s = 1, 2. (ii) Proved combination tools: the boundary-free M-core reduction and a new shift-quotient theorem for mod-M certified pieces; neither is yet proved for the actual Hilbert P graph. (iii) Real full components carry many gaps (480 at large h, conditional on an unaudited corollary), so gap counting cannot give bounded M, and a bounded-M result for P must be structural. (iv) R2s single-pair multiplicity is open in the middle zone. Two corrections from the audits: the shift-quotient theorem II.1 is false as literally stated and holds once the count uses the directed forbidden shift difference (audit_gap_mixing_combination_tools.md), and the sentence after Proposition I.6 that only the rigid binary solution remains is false, since for gaps {3, 13} the word 0121 solves the system (audit_gap_mixing_two_gap.md).

# Result

## Status

partial

## Summary

(i) The three-choice, two-gap case is settled by proof. Every full candidate component with at most two gaps is solvable at M = 3. Three independent constructions agree, and I re-proved the block rule by hand and checked all three formulas exactly. (ii) The proved combination tools are the boundary-free M-core reduction and a new shift-quotient theorem. Both are abstract, and neither is yet proved for the actual Hilbert P graph. (iii) Real full components carry many gaps: 480 at large h, conditional on an unaudited corollary. So gap counting cannot give bounded M, and any bounded-M result for P must be structural. (iv) R2s multiplicity on one label pair is still open in the middle zone.

## Statements

Abstract setting as in continuation_gap_mixing_audit.md, Section 1. Ranks are integers. Each rank r gets xi_r in {0,...,M-1}. A constraint (r,u,delta) with r<u forbids xi_u - xi_r = delta, where |delta| <= M-1, and its gap is q = M(u-r)+delta. Call an assignment y "mod-M certified" on a constraint set if y_u - y_r is not congruent to delta mod M for every constraint in the set. This is stronger than satisfying the set.

(i) TWO GAPS AT M = 3. These results are proved, and each was re-checked by a second derivation.
THEOREM I.1 (block rule; two_gap_search Theorem 3 = combine T2). Take gaps 3a and 3b+s with a even, b >= 0 and s in {1,2}. Put h = 3^{v_3(a)}. Choose g in {h, 2h} with n = floor(b/g) not congruent to 1 mod 3. Two valid selection rules are: g = h unless floor(b/h) is congruent to 1, then g = 2h; or g = 2h unless floor(b/2h) is congruent to 1, then g = h. Take c = 3-s if n is congruent to 0 mod 3, and c = s if n is congruent to 2. Then xi_r = c*floor((r+phi)/g) + kappa mod 3 satisfies every constraint of both gaps at every r, for every phi and kappa. It is mod-3 certified.
THEOREM I.2 (Beatty rule; two_gap_proof Theorem A). For every a >= 2, b >= 0 and s, the four-case rule floor(eps*theta*r + c) mod 3 is a mod-3-certified solution on Z.
PROPOSITION I.3 (odd a). xi_r = t(r mod 2), with t = s for b even and t = 3-s for b odd, solves the system. This is a one-line form of audited Theorem 2.
COROLLARY I.4. At M = 3, every component of the full candidate graph with at most two distinct gaps is solvable. This settles priority 1. There is no counterexample.
PROPOSITION I.5 (binary palettes; combine T3 = two_gap_proof Prop. B). A {0,t}-valued solution on Z exists iff v_2(b) > v_2(a) or v_2(b+1) > v_2(a). So, on Z, every solution in the formerly uncovered class uses three values.
SHARPNESS (proved). With M choices, M gaps can fail: Q = {Mk+1,...,Mk+M} is unsolvable on M+k+1 consecutive ranks (two_gap_search Prop. 5; for example {10,11,12} on ranks 0..6). The gaps {2,4} fail at M = 2. The least M that solves every s-gap full component, M_s, satisfies s+1 <= M_s <= 2s. It is exact for s = 1 and s = 2.
NEW, PROPOSITION I.6 (when shift-invariant solutions exist; proved here). An M = 3 two-gap system {3a, 3b+s} has a mod-3-certified solution on Z unless a = 1 and b is congruent to 1 mod 3, that is, gap pairs {3, 9k+4} and {3, 9k+5}. In those cases no mod-3-certified solution exists on Z. Only the rigid binary solution of Theorem 2 remains. For a = 1 and b not congruent to 1, the certified solutions are exactly y_r = z r + const with z = s(b-1)^{-1} mod 3.

(ii) COMBINATION THEOREMS (abstract, proved).
L9 (M-core, from full_comp; proof checked). Peel any label with fewer than M distinct incident triples in the remaining graph. Then every assignment of the weighted M-core K that satisfies the constraints inside each component of K extends to a global solution with no boundary lists. The extension assigns peeled labels in reverse deletion order with the full palette.
NEW, THEOREM II.1 (shift quotient). Partition the ranks, or the ranks of K, into pieces. Suppose each piece P has an assignment y^P that is mod-M certified on all constraints induced on P. For any shifts kappa_P in Z/M, set xi_r = (y^P_r + kappa_P) mod M. Then every internal constraint holds. A crossing constraint e = (r in P, u in Q, delta) is violated only if kappa_Q - kappa_P is congruent to c_e := y^P_r - y^Q_u + delta mod M. Fixing one side's shift forbids at most one shift on the other side. Order the pieces, and for each piece count the distinct pairs (Q, c_e) over crossing constraints into earlier pieces Q. If that count is at most M-1 for every piece, greedy shifts give a global solution. More generally, only the weighted M-core of this quotient has to be solved.
Inputs that are proved mod-M certified: the constant zero rule and Theorem 1 greedy, run on residues, under the same bound 2s - k0 < M; the block rule T1; the Beatty rule (Lemma C); the 3-adic rule (full_comp T7); and every two-gap system at M = 3 except the I.6 exceptions. Binary rules (audit Theorem 2, T4, T6) are generally not certified. They enter only as rigid pieces with one option.
List and guard versions (combine T5 to T8) are proved and consistent with these results. T5 says a crossing edge is cut by exactly M-|delta| deletions. T6 is the M = 3 repair of B_1-components with guards at 2-ends. Its inside condition includes the delta = +-2 edges internal to a component.

(iii) GAP COUNTS (full_comp). Proved: window arithmetic alone cannot bound gaps per full component (T4); any such bound is at least of order sqrt(h)/S. Computer-assisted, conditional on Corollary A1 of hilbert_p_height_independent_cores.md, which is unaudited: at S = 32 and M = 3, for every h >= 8705, 33793, 133121, 528385 and 2105345, some full component carries at least 9, 32, 84, 203 and 480 gaps. Consequence: Theorem 1 and Corollary I.4 apply to almost none of the mass of the giant component. Sharpness shows that no gap-count rule gives bounded M. Bounded M for P is not excluded, because the obstruction is structural. G_256 has an empty 3-core despite 84 gaps, and the archive's SAT certificates exist. But the 3-core components of G_1024 carry 318 and 234 gaps.

(iv) R2s (r2s_mult, unaudited). For M <= 40, distinct R2s constraints of one curve in one window have distinct |U|. Away from the window centre, at most one constraint lies on each arc, so at most 3 per live curve. At most 8 live curves exist per pair. The middle zone, where most H7 pairs lie, has no bound and no construction.

## Proofs

1. CHECK OF THE BLOCK RULE (I.1), BY HAND.
Write e = floor((r+phi+d)/g) - floor((r+phi)/g). Then e is in {floor(d/g), ceil(d/g)}, and xi_{r+d} - xi_r is congruent to c*e mod 3. A violated constraint means the integer difference equals delta, and delta is congruent to q mod 3. So the constraint holds whenever c*e is not congruent to q mod 3. This proves combine T1, including the inclusion of E_g(q) in {n_q, n_q+1}. For d in {floor(q/M), ceil(q/M)}, we have floor(d/g) >= floor(floor(q/M)/g) = floor(q/(Mg)) and ceil(d/g) <= ceil(q/(Mg)). If Mg divides q, then d = q/M and e = q/(Mg) exactly.
Gap 3a: d = a and delta = 0. Here g divides a, because a is even and 3^w divides a. Also a/g is in {a/h, a/(2h)}, which has 3-adic valuation 0. So e = a/g is not congruent to 0 mod 3, and c*e is not congruent to 0 for c in {1,2}.
Gap 3b+s: (3b+s)/(3g) = b/g + s/(3g), and the remainder of b mod g is at most g-1, so n = floor(b/g). Both e = n and e = n+1 are possible. The requirement is that c*n and c*(n+1) avoid s mod 3.
 - If n is congruent to 0, then c must differ from s, so c = 3-s.
 - If n is congruent to 2, then 2c must avoid s, which forces c = s. Then c*(n+1) is congruent to 0, which avoids s.
 - If n is congruent to 1, both c = 1 and c = 2 fail.
Selection rule A: if B = floor(b/h) is congruent to 1, write B = 3k+1. Then floor(b/2h) = floor(B/2) is 3j for k = 2j and 3j+2 for k = 2j+1, never 1.
Selection rule B: if C = floor(b/2h) is congruent to 1, then floor(b/h) is in {2C, 2C+1}, which are congruent to 2 and 0. The search route's c, congruent to s(B+2), equals 3-s at n = 0 and s at n = 2. It agrees with the rule above. The variant h = a/2 also works, since a/g is in {1,2}.

2. CHECK OF THE ODD-a RULE (I.3).
 - C0: the shift a is odd, so the values 0 and t alternate.
 - b even: the C1 difference is 0, not s. The C2 distance b+1 is odd, the difference is +-s, and s-3 is not +-s.
 - b odd: the C1 difference is +-(3-s), which is never s. The C2 difference is 0, not s-3.

3. CHECK OF I.5 (binary palettes), BY HAND.
With palette {p, p+t}, differences lie in {0, +-t}, and C0 makes z_r = (xi_r - p)/t antiperiodic with antiperiod a.
If t = s, C2 is vacuous, and C1 forces z_{r+b} >= z_r. Since z is 2a-periodic, summing over one period gives equality, so z is b-periodic. Antiperiod a together with period gcd(2a, b) is consistent iff gcd(2a, b) does not divide a, that is, iff v_2(b) > v_2(a).
If t = 3-s, C1 is vacuous, and the same argument with b+1 gives v_2(b+1) > v_2(a).
Sufficiency is audit Theorem 2.

4. CHECK OF THE BEATTY CRITERION (Lemma C).
The difference floor(x + M tau d) - floor(x) lies in (M tau d - 1, M tau d + 1). A violation means it equals q + Mk, so |tau d - q/M - k| < 1/M. I checked case (i) of Theorem A by hand for both s, at d = a, b and b+1. Cases (ii) to (iv) were checked only by exact computation, below.

5. EXACT COMPUTATION (sanity check, not a proof).
Script: scripts_gm1_synthesis/check_twogap.py. Each rule is periodic, so checking r over one period covers all of Z. All 12,080 triples with 1 <= a <= 40, 0 <= b <= 150 and s in {1,2} pass, with 0 failures:
 - both block selections for even a, including the mod-3-certified check;
 - the odd-a rule;
 - the Beatty rule for a >= 2, including the mod-3-certified check.
Script: scripts_gm1_synthesis/check_extra.py. All 2,304 block-rule checks with a in {486, 972, 1458, 2916} pass. This is the case that full_comp's C2 left open.

6. PROOF OF I.6 (NEW).
Suppose y is mod-3 certified for a = 1. Then z_r = y_{r+1} - y_r is nonzero mod 3. Put sigma_k(r) = z_r + ... + z_{r+k-1}. The certified conditions say that sigma_b(r) and sigma_{b+1}(r) both avoid s.
From sigma_{b+1}(r) = sigma_b(r) + z_{r+b}, sigma_b(r) avoids s and s - z_{r+b}. Hence sigma_b(r) is congruent to s + z_{r+b}.
From sigma_{b+1}(r) = z_r + sigma_b(r+1), sigma_b(r+1) is congruent to s + z_r. Comparing with the first relation at r+1 gives z_{r+b+1} congruent to z_r.
The difference sigma_b(r+1) - sigma_b(r) equals z_{r+b} - z_r. By the first relation it is also congruent to z_{r+b+1} - z_{r+b}, which equals z_r - z_{r+b}. So 2(z_r - z_{r+b}) is congruent to 0, and z_{r+b} is congruent to z_r.
Together with period b+1, this makes z constant. Then sigma_b = bz is congruent to s + z, so (b-1)z is congruent to s. This is impossible iff b is congruent to 1 mod 3. Conversely, a constant z = s(b-1)^{-1} works.
Finite check: a DFS finds that the longest certified interval is exactly 2b ranks for every b congruent to 1 mod 3 with b <= 19, and length 60 or more otherwise. That is consistent with Remark E of two_gap_proof.

7. PROOF OF II.1 (NEW).
Internal constraints: ((y_u + kappa) mod M) - ((y_r + kappa) mod M) is congruent to y_u - y_r, which is not congruent to delta. So the integer difference is not delta.
A crossing constraint is violated iff there is an x in [0, M-1] with x + delta in [0, M-1], kappa_P congruent to x - y_r, and kappa_Q congruent to x + delta - y_u. On this set, kappa_Q - kappa_P is congruent to c_e. Given kappa_Q, the value x + delta is fixed, so x and hence kappa_P are fixed: at most one value. Two crossing edges to the same Q with equal c_e forbid the same kappa_P.
Greedy over the order: a piece has M shifts and at most M-1 forbidden ones, so a shift remains. The weighted-core form follows by the same peeling argument as L9.
Theorem 1 greedy run on residues: at each rank, each earlier constraint forbids the one residue y_r + delta. The forbidden count is still at most 2s - k0 by the audited counting, so a certified value exists when M > 2s - k0.
Binary rules are not certified. Example: s = 1, b odd, rule 2(r mod 2). The C1 difference -2 is congruent to 1 = delta mod 3. Shifting the values by 1 produces the forbidden integer difference +1.

8. CHECK OF L9.
At its deletion time, a peeled vertex v has at most M-1 distinct triples to vertices that are still present, and those vertices are assigned before v in reverse order. Each triple, given the other endpoint's value, forbids exactly one value of xi_v. Distinct components of K share no constraints.

9. CHECK OF THE SHARPNESS RESULTS.
Prop. 5: at distance k, the forbidden deltas are 1..M-1, which gives xi_{r+k} <= xi_r. At distance k+1, the forbidden deltas are -(M-1)..0, which gives xi_{r+k+1} > xi_r. Hence xi_{r+1} >= xi_{r+k+1} > xi_r for r = 0..M-1. That makes M+1 strictly increasing values, a contradiction.
{2,4} at M = 2 is a triangle that needs three values.
The lists {1,2} on ranks 0 and 1 make {3,4} on {0,1,2} unsolvable. With the lists on ranks 1 and 2 instead, the system is solvable. So combine T7's example is correct only for that placement.

10. CHECKS ON THE OTHER ROUTES.
full_comp T7 (3-adic rule): checked by hand. The shift a moves floor(r/g) by a/g, which is nonzero mod 3. The shift b moves it by 0 mod 3. The shift b+1 moves it by 0 or 1, and the permutation's step differences avoid s-3.
r2s algebra: g = V - U gives U = (N/g - g)/2, V = (N/g + g)/2, T = -m delta/U = Kg/(g^2 - N), and X = (T - g)/2. Then F'(g) = -(1 + K(g^2+N)/(g^2-N)^2)/2. For N < 0, this is negative iff |K| < 8|N|. That holds because 0 < K/N < 1. This confirms the one-arc monotonicity. The Diophantine and sea-type parts were not re-derived.

CONFLICTS AND RESOLUTIONS.
(a) full_comp's C2 says the two-gap case stays open for 486 | a. The other three routes, my hand proof of I.1 and the exact checks at a = 486..2916 all settle it. The class is closed, so C2 is superseded.
(b) There is no conflict between "every two-gap full component is solvable" (I.4) and "full components carry 480 gaps" (iii). I.4 is true but nearly vacuous for the giant component.
(c) combine's bracket s+1 <= M_s <= 2s, two_gap_search's Conjecture 6 (M_s = s+1) and Prop. 5 are mutually consistent.
(d) two_gap_proof's Remark E (Beatty fails for a = 1, b congruent to 1) is strengthened by I.6: every certified rule fails there, not only Beatty rules.
(e) combine T6's phrase "solves each B_1-component inside" must include the delta = +-2 constraints induced inside the component. This is the same scope point as the audit's Section 2 correction. Binary {0,1} rules meet it automatically, and three-valued T1 rules must be checked against the induced gaps.

## External results used

- None. No published theorem was used. All arguments are elementary or come from the archive notes and the five route results.

## Checks

I re-proved these by hand: the block rule I.1, with both g-selection rules and the c choice; the odd-a rule; the binary-palette characterization I.5; Lemma C; case (i) of Beatty Theorem A; full_comp T7 (3-adic); the L9 core peeling; combine T5 and T6, with a scope caveat; Prop. 5 and Prop. D sharpness; and the r2s curve parametrization and monotonicity. I also proved two new results: Prop. I.6 (a = 1 exception for shift-invariant solutions) and Theorem II.1 (shift quotient). Exact computation found 0 failures across 12,080 triples for all three rules, plus 2,304 block checks at 486 | a, and a DFS for the a = 1 exception. Each script ran in under 35 seconds. No repository file was touched.

## Gaps

- The Hilbert P graph supplies neither hypothesis of the combination theorems. No partition of the M-core of the actual candidate graph is proved to have pieces with mod-M-certified solutions, or a quotient with at most M-1 distinct (Q, c_e) classes per piece. So no bounded-M theorem for P follows.
- The gap growth in (iii) rests on Corollary A1 of hilbert_p_height_independent_cores.md, which is unaudited. The H7 transfer of the block embedding (C1-H7) is not written out. No analytic proof shows that gaps per component tend to infinity; T4 only rules out window arithmetic as a bounding method.
- Three or more gaps at M = 3 are genuinely unsolvable in some systems. Whether the actual 3-core of the Hilbert graph contains such a pattern (for example a K4 on gaps 3, 6, 9, or Q = {3k+1, 3k+2, 3k+3}) is unchecked.
- The new results have had no independent audit, which the pre-registration protocol requires. That includes the block rule I.1 as a new statement, Prop. I.6 and Theorem II.1. Cases (ii) to (iv) of the Beatty Theorem A were checked only computationally, for a <= 40 and b <= 150.
- Conjecture 6 (M-1 gaps solvable with M choices) has only bounded-search support. The least M for s gaps is known only for s <= 2.
- R2s middle zone: neither a multiplicity bound nor a construction exists. Theorem 1(c) of r2s_mult covers M <= 40 only, and Theorem 3 needs v_2(delta) <= e-2. The whole r2s_mult note is unaudited, and I re-derived only its curve algebra.
- The other H7 families (Lambda3, Lambda4, FW, 6PT, and R2s beyond one pair) are untouched. No valid board, and no quadratic-width board, is claimed.

## Missing estimate

Priority 1 is closed. For P with bounded M, the missing piece is one structural theorem about the M-core of the actual candidate graph, an essentially new idea. For the board, five further families remain.

## Next steps

- 1. Send the closed two-gap result to an independent audit. Its parts are I.1, I.3, I.4, I.5, I.6 and Theorem II.1. The audit is short, because the proofs are a few lines each. Record Corollary I.4 in the ledger as P-only.
- 2. Run one exact certificate, not a census, on the H7 zero block at B = 2048. Find the weighted 3-core. Then test the hypotheses of Theorem II.1: pieces equal to the components of the induced graph with at most 2 gaps (excluding {3, 9k+4} and {3, 9k+5}), and quotient degeneracy below 3. This shows whether the shift-quotient route has room before any proof attempt.
- 3. Prove a structural degeneracy statement for the M-core. A candidate route is an ordering by rank within a diagonal band, using the drift bounds L2 and the per-factor gap budget T3. The target is a bound on crossing constraints to earlier pieces.
- 4. Audit Corollary A1 of hilbert_p_height_independent_cores.md. Every gap-growth statement in (iii) depends on it.
- 5. R2s middle zone: try the curvature (determinant) argument with a certified constant c2. Alternatively, search for a two-solution coincidence family with S | X automatic for both solutions.
- 6. Conjecture 6 at M = 4 (three gaps), as a lower-priority abstract target.

