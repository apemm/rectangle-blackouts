# Three choices solve every two-gap system (Beatty rule)

14 November 2026. Problem 001. Continues continuation_gap_mixing_audit.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: Theorem A. For every a >= 2, b >= 0 and s in {1, 2}, the pattern xi(r) = floor(eps theta r + c) mod 3, with eps = +1 for s = 2 and -1 for s = 1 and theta = 1/a, -2/b, -3/(b+1) or 3 ceil(b/(3a))/b on the four ranges 0 <= b <= a-1, a <= b <= 2a, 2a+1 <= b <= 3a-1 and b >= 3a, satisfies all three constraints of the gaps 3a and 3b + s at every rank, for every phase c; a = 1 is Theorem 2 of the gap-mixing audit. So every full candidate component with at most two gaps is solvable at M = 3, and the uncovered class has no counterexample. Lemma C gives the Beatty criterion for any M and any gap set. Proposition B: in the formerly uncovered class every solution on Z uses all three values. Proposition D: three gaps can fail at M = 3 on four ranks. Audited in audit_gap_mixing_two_gap.md (correct with fixable gaps); Remark E holds only when a Beatty solution means a mod-3 certified one, since for odd a the pattern floor(3r/2 + c) mod 3 with c = 0 or 1/2 is the rule t(r mod 2).

# Result

## Status

proved

## Summary

The uncovered three-choice two-gap class is always solvable. An explicit Beatty pattern xi(r) = floor(eps*theta*r) mod 3, with four cases for theta, solves every a >= 2 and b >= 0. So at M = 3, every full candidate component with at most two distinct gaps is solvable. The result is sharp: exact four-rank systems with three gaps fail.

## Statements

Setting. This is the abstract M = 3 system of continuation_gap_mixing_audit.md, Section 4. The gaps are q0 = 3a and q1 = 3b + s, with a >= 1, b >= 0 and s in {1, 2}. The constraints on xi: Z -> {0, 1, 2} hold for all r:
 (A) xi(r+a) != xi(r);
 (B) xi(r+b) - xi(r) != s (vacuous when b = 0);
 (C) xi(r+b+1) - xi(r) != s - 3.
These are all the candidate constraints the two gaps allow at M = 3. Gap 3d + delta = 3a with |delta| <= 2 forces delta = 0 and d = a. Gap 3b + s allows only d = b with delta = s, and d = b + 1 with delta = s - 3.

THEOREM A (three choices suffice for every two-gap system; proved). For every a >= 1, b >= 0 and s in {1, 2}, there is a periodic xi: Z -> {0, 1, 2} that satisfies (A), (B) and (C) at every r. Thus it satisfies them on every finite rank set and for any subset of the constraints. For a >= 2, set eps = +1 if s = 2 and eps = -1 if s = 1. Put xi(r) = floor(eps * theta * r) mod 3, where
 (i) theta = 1/a if 0 <= b <= a - 1;
 (ii) theta = -2/b if a <= b <= 2a;
 (iii) theta = -3/(b+1) if 2a + 1 <= b <= 3a - 1;
 (iv) theta = 3m/b with m = ceil(b/(3a)) if b >= 3a.
For a = 1, Theorem 2 of the audit applies, because a is odd. More generally, any phase works: floor(eps*theta*r + c) mod 3 is a solution for every real c. If theta = p/q in lowest terms, xi has period dividing 3q.

COROLLARY A1 (proved, given audited Theorem 1). At M = 3, every component of the full candidate graph with at most two distinct gaps has a solution in {0, 1, 2}. If both gaps are divisible by 3, use Theorem 1, greedy, with k0 = 2. If neither is, use constant zero. If exactly one is, Theorem A applies: write the gaps as 3a and 3b + s. Full components share no constraints, so these solutions combine. The whole uncovered class (a even, b not congruent to 0 or -1 mod 2^(alpha+1)) is therefore settled, and no counterexample exists.

PROPOSITION B (three values are needed exactly in the uncovered class; proved). Take b >= 1. A solution on all of Z with values in some two-element subset of {0, 1, 2} exists if and only if v2(b) > v2(a) or v2(b+1) > v2(a). By compactness, "on all of Z" is the same as "on every finite rank set". So in the uncovered class every solution on Z uses all three values, and the binary method of Theorem 2 cannot be pushed further.

LEMMA C (Beatty criterion, any M, any gap set; proved). Fix M >= 2, real tau and c, and put xi(r) = floor(M tau r + c) mod M. Take a gap q and a rank difference d >= 1 in {floor(q/M), ceil(q/M)}. If ||tau d - q/M|| >= 1/M (distance to the nearest integer), then xi avoids the constraint (r, r+d, q - M d) at every r. At M = 3, this gives Theorem A with tau = eps*theta/3.

PROPOSITION D (three gaps can fail at M = 3; proved, exact finite certificates). Each of the following systems on the ranks {0, 1, 2, 3} has no solution in {0, 1, 2}:
 - gaps {3, 4, 5}, all at d = 1 with delta = 0, 1, 2, which force xi(r+1) < xi(r);
 - gaps {1, 2, 3}, with delta = -2, -1, 0 at d = 1, which force xi(r+1) > xi(r);
 - gaps {3, 6, 9}, which force xi to be injective on four ranks (K4).
So Corollary A1 is sharp in the number of gaps. Counting gaps alone cannot extend it to three gaps at M = 3.

REMARK E (a = 1; proved). For a = 1, a Beatty solution exists if and only if b is not congruent to 1 mod 3. So the case split is needed: Theorem 2 covers a = 1.

## Proofs

STEP 0. Floor increments. For real x and y, floor(x+y) - floor(x) is floor(y) or floor(y) + 1. If y is an integer, it equals y. Put phi(r) = floor(theta r + c) and D_k(r) = phi(r+k) - phi(r). Then D_k(r) is in {floor(theta k), ceil(theta k)} for every integer r, including negative r. Also xi(r+k) - xi(r) is congruent to D_k(r) mod M when xi = phi mod M.

PROOF OF LEMMA C. Suppose xi(r+d) - xi(r) = delta = q - M d. Then D_d(r) is congruent to q mod M. So some y in q + MZ lies in [floor(M tau d), ceil(M tau d)]. Then either y = M tau d, or |M tau d - y| < 1. Either way, the distance from M tau d to q + MZ is less than 1. Dividing by M gives ||tau d - q/M|| < 1/M, a contradiction. QED. The proof uses only congruence mod M, so it holds for every phase c.

PROOF OF THEOREM A, s = 2 (eps = +1, xi = floor(theta r) mod 3). Three residue conditions suffice.
 (A') floor(theta a) and ceil(theta a) are both nonzero mod 3. Then D_a is nonzero mod 3, so xi(r+a) != xi(r).
 (B') floor(theta b) and ceil(theta b) are both in {0, 1} mod 3. A difference of +2 would need D_b to be 2 mod 3.
 (C') floor(theta(b+1)) and ceil(theta(b+1)) are both in {0, 1} mod 3. A difference of -1 would need residue 2.
The four cases, with a >= 2:
 (i) theta = 1/a, b <= a - 1. Here theta a = 1, so (A') holds. theta b = b/a is in [0, 1), and theta(b+1) = (b+1)/a is in (0, 1]. Both have floor and ceil in {0, 1}.
 (ii) theta = -2/b, a <= b <= 2a, so b >= 2. theta a = -2a/b is in [-2, -1], and its floor and ceil are in {-2, -1}, residues {1, 2}. theta b = -2, residue 1. theta(b+1) = -2 - 2/b is in [-3, -2), and its floor and ceil are in {-3, -2}, residues {0, 1}.
 (iii) theta = -3/(b+1), 2a + 1 <= b <= 3a - 1. Since 2a < b + 1 <= 3a, theta a = -3a/(b+1) is in (-3/2, -1]. Its floor and ceil are in {-2, -1}, residues {1, 2}. theta b = -3 + 3/(b+1) is in (-3, -2] because b >= 2, residues {0, 1}. theta(b+1) = -3, residue 0.
 (iv) theta = 3m/b, m = ceil(b/(3a)), b >= 3a >= 6. Here m >= b/(3a) and m < b/(3a) + 1 <= b/6 + 1 <= b/3, so m <= b/3. Then theta a = 3ma/b is in [1, 3(1/3 + a/b)), which lies in [1, 2] because a/b <= 1/3. Its floor and ceil are in {1, 2}. theta b = 3m, residue 0. theta(b+1) = 3m + 3m/b with 3m/b <= 1, residues {0, 1}.
Every b >= 0 falls into one of (i) to (iv), because the ranges [0, a-1], [a, 2a], [2a+1, 3a-1] and [3a, infinity) cover all b >= 0. The case b = 0 is in (i), where (B) is vacuous.

PROOF OF THEOREM A, s = 1 (xi = floor(-theta r) mod 3). By Step 0 with -theta, the increments at k lie in {-ceil(theta k), -floor(theta k)}. Their residue sets are the negatives of the s = 2 sets. At a, the residues stay in {1, 2}, which is nonzero. At b and b + 1, the residues lie in -{0, 1} = {0, 2}. Constraint (B) for s = 1 forbids a difference of +1, residue 1. Constraint (C) forbids -2, also residue 1. Neither residue occurs. Phases: Step 0 holds for floor(theta r + c), so every c works. Periodicity: floor(p(r+q)/q) = floor(pr/q) + p, so xi(r + 3q) = xi(r). QED.

PROOF OF COROLLARY A1. A two-gap full component at M = 3 has k0 in {0, 1, 2} gaps divisible by 3. For k0 = 0, use constant zero (Theorem 1). For k0 = 2, greedy works, since 3 > 2*2 - 2 (Theorem 1). For k0 = 1, the gaps are 3a and 3b + s with a >= 1 and b >= 0. The candidate constraints of the component are a subset of (A), (B) and (C), at the component's own ranks. The restriction of the global solution from Theorem A avoids all of them. A one-gap component is covered by Theorem 1. Different full components share no constraint, so their solutions combine (audit, Theorem 1 and Section 5). QED.

PROOF OF PROPOSITION B. One value fails (A). The two-element palettes are {0, 1} and {1, 2}, with differences 0 and +-1, and {0, 2}, with differences 0 and +-2. Write xi = base + w*f with f in {0, 1} and w in {1, 2}. Then (A) says f(r+a) = 1 - f(r), so f has period 2a.
 Case s = 1, w = 1. (C) forbids -2, which never occurs. (B) forbids +1 at shift b, so f(r+b) <= f(r) for all r. Then f(r) >= f(r+b) >= ... >= f(r + 2ab) = f(r), so all are equal, and f is b-periodic.
 Case s = 1, w = 2. (B) forbids +1, which never occurs. (C) forbids -2 at shift b + 1, so f(r+b+1) >= f(r). By the same chain argument, f is (b+1)-periodic.
 Case s = 2, w = 2. (C) forbids -1, which never occurs. (B) forbids +2, so f(r+b) <= f(r), and f is b-periodic.
 Case s = 2, w = 1. (B) forbids +2, which never occurs. (C) forbids -1 at b + 1, and f is (b+1)-periodic.
So a binary solution exists if and only if some f: Z -> {0, 1} is antiperiodic under a and periodic under p, where p = b or b + 1 and p >= 1. Such an f exists if and only if the map k a + l p -> k mod 2 is well defined on aZ + pZ. That holds if and only if every relation k a = -l p has k even. The minimal k is p/gcd(a, p), so the condition is v2(p) > v2(gcd(a, p)), which is equivalent to v2(p) > v2(a). The construction is Theorem 2 of the audit. Compactness over a finite alphabet makes "every finite rank set" equivalent to "all of Z". QED.

PROOF OF PROPOSITION D. Gaps {3, 4, 5} at d = 1 give delta = 0, 1 and 2 for the pairs (0,1), (1,2) and (2,3). So xi(r+1) - xi(r) is not in {0, 1, 2}, which forces xi(r+1) < xi(r) for r = 0, 1, 2. That needs four distinct values in {0, 1, 2}, a contradiction. For gaps {1, 2, 3}, the d = 1 deltas are -2, -1 and 0, so xi strictly increases on four ranks, the same contradiction. For gaps {3, 6, 9}, the delta = 0 constraints at d = 1, 2 and 3 make xi injective on {0, 1, 2, 3}. QED.

PROOF OF REMARK E. For a = 1, Lemma C at M = 3 asks for {tau} in [1/3, 2/3] and for x = {tau b} and {tau(b+1)} = {x + tau} both in [0, 1/3]. With x in [0, 1/3], {x + tau} lies in [0, 1/3] only if tau mod 1 is in [-1/3, 1/3]. So tau is congruent to 1/3 or 2/3. For tau = 1/3, x + 1/3 <= 1/3 forces x = 0, so b is congruent to 0 mod 3. For tau = 2/3, x + 2/3 = 1 forces x = 1/3, so 2b is congruent to 1 and b is congruent to 2 mod 3. This shows that the conditions of Lemma C, with s = 2, are satisfiable if and only if b is not congruent to 1 mod 3. The s = 1 case is the mirror image (tau -> -tau). QED.

HOW THE CONSTRUCTION WAS FOUND. Lemma C turns the system into three window conditions on one real tau: {tau a} in [1/3, 2/3], and {tau b}, {tau(b+1)} in [0, 1/3] for s = 2, or in [2/3, 1] for s = 1. Mirroring tau to -tau swaps s = 1 and s = 2. An exact description of the set G where both b-conditions hold gives
 G = union over m in [0, b/3] of [m/b, (m + 1/3)/(b+1)], together with the union over j in [1, (b+1)/3] of [-j/(b+1), -(j - 1/3)/b].
The four thetas are points of G that meet the a-window: the m = 0 interval, the endpoint -(j - 1/3)/b with j = 1, the endpoint -j/(b+1) with j = 1, and the anchors m/b.

## External results used

- None. The proof uses only floor(x+y) - floor(x) in {floor(y), floor(y)+1}, compactness over a finite alphabet (used only to restate Proposition B), and the audited Theorems 1 and 2 of continuation_gap_mixing_audit.md.

## Checks

I ran three scripts with py -B, one at a time, each well under 60 s and under 1 GB. All are in scripts_gm1_two_gap_proof/. The repository was only read.
- verify_formulas.py checks the explicit formulas of Theorem A directly, with exact integer floors. It covers 2 <= a <= 60, 0 <= b <= 200 and s in {1, 2}, and tests (A), (B) and (C) at every r in one full period 3q. Result: 23,718 systems, 0 failures. Since the solution is 3q-periodic, one period covers all of Z.
- beatty.py decides, with exact rationals, whether the window conditions of Lemma C can be met. It tests all breakpoints and the midpoints between them. On the uncovered class (a even, b not congruent to 0 or -1 mod 2^(alpha+1)), it found a solution in all 2,794 cases with a <= 64 and b <= 130. beatty_all.py (all a <= 50, b <= 80) found that only a = 1 with b congruent to 1 mod 3 has no Beatty solution, matching Remark E.
- sft_check.py is an exact decision on Z. It prunes the window graph of words of length D = max d and reports whether a cycle survives. It covers every gap pair and triple with gaps <= 14 at M = 3, with all candidate constraints present. Every gap pair is solvable, consistent with Corollary A1 and independent of the formulas. 85 triples are unsolvable: 2 with all gaps divisible by 3 ({3,6,9} and {3,9,12}), 83 mixed (for example {1,2,3}, {3,4,5} and {2,4,6}), and none with no gap divisible by 3. That last case is the constant-zero case.
- Hand checks: every case inequality in the proof of Theorem A. Also a = 4, b = 4, the boundary case of (ii), where tau = -1/6 gives {tau a} = 1/3, {tau b} = 1/3 and {tau(b+1)} = 1/6.

## Gaps

- Scope: this result covers the P family only, and only components with at most two distinct gaps at M = 3. It says nothing about Lambda3, Lambda4, R2s, FW or 6PT, and it does not prove a quadratic-width board.
- Corollary A1 depends on the audited framework: the full candidate graph formed at M = 3, Theorem 1 of continuation_gap_mixing_audit.md, and the slot-gap reduction q = 3d + delta. I checked those inputs only by reading them, not by re-deriving the Hilbert geometry.
- Components with three or more gaps at M = 3 stay open. Proposition D shows that gap counting cannot handle them: an actual component's constraint subset and rank set must be used. I have no data on how many Hilbert components have three or more gaps, or which three-gap patterns they contain.
- Priority 2, combining repairs with boundary lists, is not solved here. The only new tools are the phase freedom (any c works, so a single boundary rank with a nonempty list can always be met) and the Beatty criterion (Lemma C), which certifies a whole gap set with one formula. Neither one controls several boundary ranks at once.
- Priority 3, R2s multiplicity on one label pair, was not attempted on this route.
- Remark E is proved only in the Beatty sense. A Beatty solution for a = 1 may fail, but Theorem 2 still solves a = 1.

## Missing estimate

The two-gap target is closed: no estimate is missing for it. For priority 2, the next estimate needed is structural. For the mixed components that actually occur at M = 3, with three or more gaps, does a single tau satisfy Lemma C for the component's own (d, delta) list, or are the failing patterns of Proposition D excluded by the geometry? In particular, can a real component contain four consecutive ranks joined by constraints whose d = 1 deltas cover {0, 1, 2} or {-2, -1, 0}?

## Next steps

- Have someone audit Theorem A: the four case inequalities, the s = 1 mirror, and the Step 0 increment lemma. All are short.
- Record in the ledger: at M = 3, every full candidate component with at most two gaps is solvable, using Theorem 1 plus Theorem A. Also record Proposition D as the sharpness boundary.
- For mixed components with three or more gaps at h = 2048 and 4096 (S = 32, M = 3), run the Lemma C test per component. It reduces to finitely many windows on one real tau, and it gives a certificate for the whole component regardless of its size. Use exact search only where the test fails. This is a per-component check on existing candidate data, not a new census.
- Classify which d = 1 and d = 2 delta patterns the Hilbert geometry allows at consecutive ranks, to see whether the Proposition D obstructions can occur in real components.
- For boundary-compatible repairs, use the free phase c and the reflection xi(r) -> 2 - xi(-r), which preserves every constraint set, to meet boundary lists. As a first target, try to prove that a two-gap repair set with boundary lists on at most two ranks can always be extended.

