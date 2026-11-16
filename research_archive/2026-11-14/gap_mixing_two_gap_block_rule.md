# Three choices solve every two-gap system (block rule)

14 November 2026. Problem 001. Continues continuation_gap_mixing_audit.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: an independent second construction for the same class. For even a, xi_r = c floor(r/g) mod 3 with g = 3^(v_3(a)) or 2 * 3^(v_3(a)) solves the system on every finite rank set, so every full candidate component with at most two gaps is solvable at M = 3. Exact certificates show that three gaps can fail at M = 3 at every scale, and that with M choices some M gaps fail. Audited in audit_gap_mixing_two_gap.md (correct with fixable gaps).

# Result

## Status

proved

## Summary

The remaining three-choice, two-gap case is solvable for every even a, by xi_r = c*floor(r/g) mod 3 with g equal to 3^{v_3(a)} or 2*3^{v_3(a)}. So at M = 3 every full candidate component with at most two gaps is solvable. Three gaps can fail at M = 3 at every scale; exact certificates are below.

## Statements

Setting (from continuation_gap_mixing_audit.md, Section 4). M = 3. The choices are xi_r in {0,1,2}. The gaps are q0 = 3a and q1 = 3b+s, with a >= 1, b >= 0 and s in {1,2}. The constraints are: (C0) xi_{r+a} != xi_r; (C1) xi_{r+b} - xi_r != s (only when b >= 1); (C2) xi_{r+b+1} - xi_r != s-3.

THEOREM 3 (even a; covers the whole uncovered class). Let a >= 2 be even, b >= 0, s in {1,2}, and h = 3^{v_3(a)}. Set g = 2h if floor(b/(2h)) is not congruent to 1 mod 3. Otherwise set g = h. Put B = floor(b/g) and choose c in {1,2} with c ≡ s(B+2) (mod 3). Then
    xi_r = (c * floor(r/g)) mod 3
satisfies C0, C1 and C2 for every integer r. Its period is 3g, which divides 2*3^{v_3(a)+1}. The same statement and proof hold with h = a/2, so g is a or a/2 and the period is 3a or 3a/2.

PROPOSITION (odd a; a one-line form of audited Theorem 2). If a is odd, xi_r = t*(r mod 2) works. Take t = s if b is even and t = 3-s if b is odd. The period is 2.

COROLLARY 4 (priority 1 settled). At M = 3, every full candidate component with at most two distinct gaps is solvable. The cases are:
- One gap: Theorem 1.
- Two gaps, both divisible by 3: Theorem 1 with k0 = 2.
- Two gaps, neither divisible by 3: constant zero.
- Mixed gaps: the Proposition (a odd) or Theorem 3 (a even).
Each formula satisfies every constraint with those gaps on all of Z. It therefore solves any rank subset and any subset of those constraints, and it needs no boundary lists inside a full component. Every system 3a, 3b+s has an explicit solution whose period divides 2*3^{v_3(a)+1}.

PROPOSITION 5 (sharpness at M gaps, at every scale). For every M >= 2 and k >= 0, the gap set Q = {Mk+1, Mk+2, ..., Mk+M} has no solution on M+k+1 consecutive ranks when all its constraints are present. At M = 3, three gaps can therefore fail with arbitrarily large gaps. Example: {10, 11, 12} fails on ranks 0..6.

CONJECTURE 6 (not proved). For every M >= 2, a full component with at most M-1 distinct gaps is solvable with M choices. This holds for M = 2 (Theorem 1) and M = 3 (Corollary 4). Proposition 5 shows M-1 cannot be raised to M. Theorem 1 gives only M >= 2s, so this conjecture is a strict strengthening of it.

## Proofs

STEP 0. B is not congruent to 1 mod 3, so c is well defined.
- If g = 2h, this is the selection rule.
- If g = h, then m = floor(b/2h) ≡ 1 mod 3. Write b = 2hm + rho with 0 <= rho < 2h. Then B = floor(b/h) = 2m + floor(rho/h), which is 2m or 2m+1, so B ≡ 2 or 0 mod 3.
In both cases B+2 is not divisible by 3. Since s is a unit mod 3, s(B+2) is not 0 mod 3, so c is 1 or 2. Note that c^2 ≡ 1 and s^2 ≡ 1 mod 3.

STEP 1. Floor increments. Write r = gn + p0 with 0 <= p0 < g (any integer r, negative ones included), and k = gK + kappa with 0 <= kappa < g. Then floor((r+k)/g) = n + K + [p0 + kappa >= g], because 0 <= p0 + kappa <= 2g-2. So the increment e_k(r) = floor((r+k)/g) - floor(r/g) is K or K+1, and it equals K whenever g divides k. Consequently xi_{r+k} - xi_r ≡ c e_k(r) (mod 3).

STEP 2. Constraint C0. g divides a, and a/g is a/h or a/(2h). Since h = 3^{v_3(a)} and h is odd, both are integers that 3 does not divide. So e_a = a/g is not 0 mod 3, hence c e_a is not 0 mod 3. Two values in {0,1,2} that differ mod 3 are distinct, so xi_{r+a} != xi_r.

STEP 3. Constraint C1 (b >= 1). Suppose xi_{r+b} - xi_r = s. Then c e_b ≡ s. Multiplying by c gives e_b ≡ cs ≡ s^2(B+2) ≡ B+2. But e_b is B or B+1, and neither is congruent to B+2 mod 3. This is a contradiction.

STEP 4. Constraint C2. Suppose xi_{r+b+1} - xi_r = s-3, which is ≡ s mod 3. As in Step 3, e_{b+1} ≡ B+2.
- If g does not divide b+1, then floor((b+1)/g) = B, so e_{b+1} is B or B+1.
- If g divides b+1, then e_{b+1} = (b+1)/g = B+1.
Either way this is a contradiction. QED for Theorem 3.

The variant with h = a/2 uses the same proof. It needs only g1 | a and 2g1 | a, with 3 dividing neither a/g1 nor a/(2g1). The doubling step, floor(b/g1) in {2 floor(b/2g1), 2 floor(b/2g1) + 1}, then forces one of the two scales to have B not congruent to 1.

ODD-a PROPOSITION. The two values are 0 and t, so every difference is 0, t or -t. Shift a is odd, so the difference at shift a is ±t, which is not 0.
- If b is even, the difference at shift b is 0, which is not s. The difference at shift b+1 is ±t, and t = s avoids s-3: for s = 1, t = 1 and ±1 != -2; for s = 2, t = 2 and ±2 != -1.
- If b is odd, t = 3-s. Then ±t != s, and the difference at shift b+1 is 0, which is not s-3.

COROLLARY 4. The mixed case is split by parity of a. Within one full component, the constraints present are a subset of all constraints with those two gaps. A formula valid on all of Z satisfies every such subset. Full components share no constraints, so their solutions combine.

PROPOSITION 5. A gap Mk+delta with 1 <= delta <= M-1 gives two relations. At shift k (when k >= 1) it forbids difference delta. At shift k+1 it forbids difference delta-M. The gap M(k+1) forbids difference 0 at shift k+1. So shift k allows only differences <= 0, and shift k+1 allows only differences >= 1.
- If k >= 1: for every r with r+k+1 inside the interval, xi_{r+1} >= xi_{r+1+k} > xi_r.
- If k = 0: xi_{r+1} > xi_r directly.
So xi is strictly increasing on the first L-k ranks. On L = M+k+1 ranks that gives M+1 strictly increasing values, but only M values exist.
Check at M = 3, k = 3, Q = {10, 11, 12}: xi_0 < xi_4 <= xi_1 < xi_5 <= xi_2 < xi_6 forces four distinct values on ranks 0..6. A smaller example is Q = {3,4,5}. Shift 1 forbids differences 0, 1 and 2, so xi strictly decreases. Shift 2 forbids differences -2 and -1, which a double decrease must produce. So it fails on 3 ranks.

## External results used

- None. All arguments are self-contained. The only inputs are the audited Theorem 1, the gap-to-(rank difference, delta) uniqueness from its proof, and the system definitions in continuation_gap_mixing_audit.md.

## Checks

I wrote the proofs first, then checked them by computation. Every script ran in well under 60 s. Scripts are in scripts_gm1_two_gap_search/ (321 KB).

(1) Theorem 3, scale-a variant: verify_block.py does not import the solver code. It checked all even a <= 160, 0 <= b <= 600 and both s on r in [-3g, 3g): 96,160 cases, 0 failures. Two negative controls failed as they should. Swapping c for 3-c failed all 820 cases. Forcing g = a hit the c = 0 assertion.

(2) Both variants (h = 3^{v_3(a)} and h = a/2) against the raw slot rule, which forbids 3(u-r) + xi_u - xi_r in {3a, 3b+s}: raw_block.py checked even a <= 90, b <= 270: 48,780 cases, 0 failures.

(3) Exact minimal periods with a SAT solver (pysat Glucose4, run1.py, r2.json): all 2,732 uncovered triples (a, b, s) with a even <= 64 and b <= 64. Every solution was re-checked. Minimal periods: 3 (1250), 4 (281), 5 (581), 6 (270), 7 (205), 8 (58), 9 (64), 10 (16), 11 (5), 12 (1), 15 (1, at (36,36,1): 220122012001200). The bounded search up to 24 is now superseded by the proof.

(4) Residue tables (gp.py, p54.py). For periods p <= 19 I tabulated the residue pairs (a mod p, b mod p) with no p-periodic solution. Exactly p = 2, 6 and 18 have none. p = 54 has none over all 5,724 instances, and p = 162 has none at a ≡ 54 or 108. Theorem 3 and the odd-a Proposition explain this for every p = 2*3^k. Solutions of period 2*3^k also show the symmetry (s, b) to (3-s, -b-1) mod p, which comes from reflection plus complement.

(5) Three gaps at M = 3 (three_gap.py, three30.json): 2,920 gap triples <= 30 with a gap divisible by 3. 2,457 have periodic solutions and 463 have exact unsatisfiable intervals. 141 of the failing triples have all gaps >= 10. I proved the certificates for {1,2,3} (L = 4), {3,4,5} (L = 3) and {10,11,12} (L = 7) by hand, as above. The other unsatisfiable verdicts are SAT-only.

(6) Conjecture 6 evidence (gapM.py, plus gapM_check.py for the raw slot rule). Periodic solutions were re-verified against the raw slot rule, checking every rank distance: 990 two-gap sets at M = 3 (gaps <= 60), 5,820 three-gap sets at M = 4 (gaps <= 40) and 5,781 four-gap sets at M = 5 (gaps <= 24), with 0 failures. At M = 4 with four gaps, 312 of 7,566 sets <= 24 are unsatisfiable, consistent with Proposition 5.

The repository rectangle-blackouts was read only. No git commands were run, and Kagey-Problems was not touched.

## Gaps

- Conjecture 6 (M-1 gaps with M choices) is supported only by bounded search. At M = 4, all 20,030 three-gap sets with gaps <= 60 and a gap divisible by 4 have a periodic solution. At M = 5, all 25,901 four-gap sets with gaps <= 34 do. Neither greedy (2s - k0 forbidden values) nor the block-linear family obviously proves it. The block-linear form needs one g with floor(d_q/g) avoiding two residues mod M for every gap, which is a lonely-runner-type covering problem.
- None of this measures how many distinct gaps actual Hilbert full candidate components have at M = 3 or M = 4. The archive's 7.0% and 12.3% mixed shares are for binding components. Corollary 4 solves the P family only for full components with at most two gaps. Components with three or more gaps at M = 3 can be genuinely unsolvable (Proposition 5).
- I did not touch priority 2 for partial (binding) components. The new formulas remove boundary issues only inside full components.
- I did not touch priority 3 (R2s multiplicity) or the other five families (Lambda3, Lambda4, R2s, FW, 6PT).
- Minimal periods are not described by a formula. Only the upper bound, period dividing 2*3^{v_3(a)+1}, is proved.

## Missing estimate

Priority 1 is closed: three choices solve every two-gap full component. The next open point on this line is whether actual Hilbert full components at M = 3 have at most two gaps. If not, it is whether Conjecture 6 at M = 4 (three gaps) holds, or whether components with four or more gaps occur.

## Next steps

- Record Theorem 3 and Corollary 4 in the ledger and send them for independent audit. The proof takes a dozen lines.
- Measure the number of distinct gaps per FULL candidate component (not binding) at M = 3 and M = 4 on the existing h = 2048 and 4096 data. Do not run a new census. If full components have at most two gaps at M = 3, the P family needs only three choices and formulas at the scale 3^{v_3(a)}.
- Attack Conjecture 6 at M = 4 with three gaps. The cases Theorem 1 misses are k0 = 1 and k0 = 2. Try a two-scale block-linear rule xi = c*floor(r/g) mod 4, using a doubling argument like the one in Theorem 3.
- For components with three gaps at M = 3, use Proposition 5's structure, a monotone-chain obstruction: Q contains Mk+1, ..., Mk+M. Test whether it is the only kind of obstruction for three gaps by checking the 463 failing triples for a short chain certificate.
- Priority 3 (R2s on one label pair) remains independent of this result.

