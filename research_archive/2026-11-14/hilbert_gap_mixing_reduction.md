# A diagonal-scaled rule and the gap-mixing components

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (partial): no bounded-M rule for every factor and no impossibility proof. For every M and every two-value choice set {0, t}, a short explicit rule removes every P constraint of every factor outside the gap-mixing components, the components of the binding constraint graph that carry two or more slot gaps. So a rule that reads the rank at a diagonal-dependent scale can fail only where two resonance windows overlap; the factor-one rule, the five-label obstruction and every recorded test failure are instances. At M = 3, S = 32 the mixed components grow from 7.0% to 12.3% of binding components between h = 2048 and h = 4096, which suggests mixing becomes generic at large heights. Not audited yet.

# Result

## Status

partial

## Summary

I found no bounded-M rule for every factor, and no impossibility proof. I did prove that, for every M and every two-value choice set {0, t}, a short explicit rule removes every P constraint of every factor outside the "gap-mixing" components. These are the components of the binding constraint graph that carry two or more slot gaps. So any rule that reads the rank at a scale tied to the diagonal T can fail only where two resonance windows overlap. The factor-one rule, the five-label obstruction and every test failure are instances of this reduction. At M = 3, S = 32 the mixed components grow from 7.0% to 12.3% of binding components between h = 2048 and h = 4096. That suggests mixing becomes generic at large heights.

## Statements

Setting (archive): the full-grid Hilbert placement with every label kept, x_e = S(M r_e + xi_e), S even, M >= 2, xi_e in {0..M-1}. A candidate constraint is a triple (e, f, delta) with r_e < r_f, d = r_f - r_e and q = M d + delta >= 1. It means: if xi_f - xi_e = delta, some cross-parity black pair of e and f has X = Sq and X^2 + Y^2 = L^2 with an in-strip completion. Call q its gap. The gap set Q(e) of a label is the set of gaps of the candidate constraints at e (over every factor, role and side). T = j - i.

LEMMA 1 (odd-divisor form of a P vector; proved). Let S be even, q >= 1, N = Sq/2, and Y >= 1 odd. Then (Sq)^2 + Y^2 is a square exactly when Y = |N^2/c - c| for some odd divisor c of N^2. In that case L = c + N^2/c, the half-factors are {c, N^2/c}, and the smaller half-factor is a = min(c, N^2/c). For S = 2^s, the odd divisors of N^2 are the divisors of odd(q)^2, so the set of rows Y carried by a gap q depends only on the odd part of q and on the power of 2 in q.

LEMMA 2 (one gap per factor and diagonal; proved). Assume a <= S^2/32, so A_a = S^2/(8a) >= 4. For each diagonal T there is at most one gap q =: q_a(T) such that some label on the line {j - i = T} has a factor-a candidate constraint with gap q. It is the unique q >= 1 with |T + (eps a + 1)/2 - eps A_a q^2| < 4 sqrt(q) for some eps in {+1, -1}. So for small factors the candidate gap is a function of (a, T). For a general factor, uniqueness holds per label, role and side (archive, Section 7).

THEOREM 3 (binding-gap rule; proved). Fix M >= 2 and t in {1, ..., M-1}, and use only the choices xi in {0, t}. Call a candidate constraint binding when delta is in {0, t, -t}; for M = 2 every constraint is binding. Let B_t be the graph of binding constraints, and let C(e) be the component of e in B_t. Suppose a component C has one gap q_C. Define xi_e = t * [M | q_C] * (floor(M r_e / q_C) mod 2) for e in such a C, and xi_e = 0 for labels with no binding constraint. Then every candidate constraint of every factor that is non-binding, or that lies in a single-gap component, is avoided, whatever values are used on the other components. In particular, if every component of B_t has a single gap, this rule removes the whole P family with two values, at any height and for any retained subset. On a label whose binding constraints all come from factors a <= S^2/32, Q(e) is a subset of {q_a(T_e)}, so the rule reads the rank at the scales q_a(T)/M fixed by the diagonal.

COROLLARY 3a (proved). With M = 2, every factor-one component has a single gap, and Theorem 3 gives back the archive's factor-one theorem. The five-label two-choice obstruction (h = 2048, S = 32, M = 2) is a mixed component of B_1 with gaps 2 (factor 1) and 35 (factor 245): label D = (138,649), on T = 511, carries both gaps. No two-value rule of any kind can repair a mixed component in general.

THEOREM 4 (2-adic sufficient condition; proved). Let M = 2^m and S = 2^s. For a candidate constraint with gap q, put v = v2(q). Then delta is congruent to q mod M. So delta = 0 exactly when v >= m, and such gaps require L >= 4^m S^2/4 + 1 (archive T1). When v < m, v2(delta) = v. So any assignment satisfying both conditions below avoids every P constraint:
(a) xi_e = xi_f mod 2^(v+1) on every constraint with v < m;
(b) xi_e != xi_f on every constraint with v >= m.
Equivalently, write xi = sum over b < m of 2^b beta_b. Then bit beta_b must be constant on each component of H_b, the union of the constraints with b <= v < m, and the delta = 0 constraints must be split by some bit. Using only the top bit is Theorem 3 with t = M/2. That has two binding residues, 0 and M/2, against three for t = 1.

PROPOSITION 5 (rules that read T and a bounded statistic; proved, elementary). Every rule is a function F(r, T), since r alone determines the label. So an impossibility result for all F(r, T) is the open bounded-M question itself. For the restricted class xi = Phi(T, sigma(r)), with sigma taking at most P values on each line, the following hold:
(i) a delta = 0 candidate constraint between two labels on the same line with equal sigma is always violated;
(ii) no single constraint between different lines is forced.
So an obstruction to this class must come from delta = 0 pairs on one line with incompatible rank gaps, or from an unsatisfiable system of constraints between lines.

NOT PROVED: a bounded-M rule for all factors, or for any infinite set of factors with a > S^2/32; any bound on gap mixing; any impossibility result for single-scale rules Phi(T, floor(r/w(T)) mod P).

## Proofs

PROOF OF LEMMA 1. X = Sq is even and Y is odd, so L is odd. Then L - Y = 2a and L + Y = 2b are even, with ab = X^2/4 = N^2. Also b - a = Y is odd, so exactly one of a and b is odd; call it c. The other one is N^2/c, so Y = |N^2/c - c| and L = a + b = c + N^2/c. Conversely, if c is an odd divisor of N^2 with Y = |N^2/c - c| > 0, put L = c + N^2/c. Then L^2 - Y^2 = 4 c (N^2/c) = 4N^2 = X^2. For S = 2^s, N = 2^(s-1) q, so an odd c divides N^2 exactly when it divides odd(q)^2. This agrees with T1 of hilbert_p_family_counts.md: there c = kO^2 when a is odd, and c = b when a is a multiple of S^2/4.

PROOF OF LEMMA 2. Let f be a candidate partner of a label e on line T, with factor a and gap q. By (6) and (7) of continuation_hilbert_factor_one_choices.md, the signed row difference is y = 2T + 2z + 1. Here z = Delta j or -Delta i, and |z| < 4 sqrt(d) <= 4 sqrt(q). The bound d <= q is (5), which holds for every candidate local assignment. The factor-a equation |y| = S^2 q^2/(4a) - a then gives (17):
  T = eps A_a q^2 - (eps a + 1)/2 - z.
Take two such candidates, at labels e1 and e2 on the same line T (e1 = e2 is allowed), with gaps q1 != q2. The contradiction in the fixed-factor lemma (Section 6 of that note) uses only the two copies of (17) with the same T and the bounds |z_i| < 4 sqrt(q_i). It does not use that the focal labels coincide.
- Equal signs: A_a |q1^2 - q2^2| = |z1 - z2| < 4(sqrt q1 + sqrt q2) <= 4(q1 + q2) <= 4|q1^2 - q2^2|. This contradicts A_a >= 4.
- Opposite signs, q1 > q2: A_a(q1^2 + q2^2) - a = z_+ - z_-. The smaller-factor condition gives 2 A_a q2^2 > a, so the left side is more than A_a(q1^2 - q2^2) >= 4(sqrt q1 + sqrt q2), while the right side is smaller in absolute value. Contradiction.
So q is unique, and (17) is the stated window condition.

PROOF OF THEOREM 3. Every value lies in {0, t}, so every actual difference xi_f - xi_e lies in {0, t, -t}.
(1) A non-binding constraint has delta outside {0, t, -t}, so it is never active.
(2) A binding constraint (e, f, delta) is an edge of B_t, so e and f lie in one component C. Suppose C has a single gap q_C. Then q = M d + delta = q_C.
 (2a) If M does not divide q_C, the rule gives xi = 0 on all of C, so the difference is 0. But delta = q_C - M d is not divisible by M, so delta != 0, and the constraint is inactive.
 (2b) If M divides q_C, then delta = q_C - M d is divisible by M with |delta| <= M - 1, so delta = 0 and d = q_C/M. Hence floor(M r_f/q_C) = floor(r_e/d) + 1, the parities differ, and xi_f - xi_e = +t or -t, which is not 0. Inactive.
Every candidate edge is of type (1) or (2), and the values chosen on mixed components affect only edges inside those components. Every pair that could be a P conflict for the final choices is a candidate constraint (archive, Section 1), so no single-gap component and no non-binding pair carries a conflict.
For the last claim: if all binding constraints at e have factors a <= S^2/32, then by Lemma 2 each gap is q_a(T_e), so Q(e) is a subset of {q_a(T_e) : a <= S^2/32 odd}. The rule therefore depends only on r_e, on T_e and on which small factors occur at e.

PROOF OF COROLLARY 3a. By Lemma 2 with a = 1 (A_1 = S^2/8 >= 8 for S >= 8), all factor-one constraints in a component share one gap. With M = 2, t = 1 the rule is the archive rule: 0 on odd q, and floor(r/d0) mod 2 with d0 = q/2 on even q. Table of continuation_hilbert_two_choice_obstruction.md: the short edges C-D and D-E have X = 64, so q = 2 (factor (1025 - 1023)/2 = 1). The long edges A-C, A-D, D-H and E-H have X = 1120, so q = 35 (factor (1525 - 1035)/2 = 245). The five labels are connected, so their component carries two gaps. D = (138, 649) has T = 511 and both gaps.

PROOF OF THEOREM 4. With M = 2^m, delta = q - M d is congruent to q mod 2^m.
- If v = v2(q) >= m, then delta is divisible by M and |delta| < M, so delta = 0 and condition (b) is exactly the requirement. By T1, v2(q) = v2(e') and L >= k(S^2 e'^2/4 + 1) >= 4^m S^2/4 + 1.
- If v < m, then v2(delta) = v and delta != 0. Under (a), xi_f - xi_e is 0 or has 2-adic valuation at least v + 1, so it is not delta.
Bit form: (a) for a constraint of valuation v says beta_0, ..., beta_v agree at its two ends. So beta_b must agree across every constraint with b <= v < m, which means beta_b is constant on each component of H_b. Condition (b) asks that some bit differ. If the bits below m - 1 are fixed at 0, the values are {0, M/2}, the binding residues are exactly 0 and M/2, and the rule of Theorem 3 with t = M/2 satisfies (a) and (b) on every component with a single gap.

PROOF OF PROPOSITION 5. Each rank is one label, so F(r, T) = F(r) is any rule. For (i): equal sigma and equal T give equal xi, and a delta = 0 constraint is active when the two values are equal. For (ii): one constraint between lines T1 != T2 is satisfied by any choice with Phi(T2, .) - Phi(T1, .) != delta at the two statistic values, and such a choice exists for M >= 2.

TESTS AGAINST THE RECORDED OBSTRUCTIONS (as the target asked).
- Two-choice obstruction: it is a mixed component (Corollary 3a). This is where Theorem 3 cannot help, and no M = 2 rule works.
- P triangle at h = 4096: this is M = 1 and imposes nothing on M >= 2.
- Lemma A and Lemma B atoms (hilbert_choice_rule_obstruction.md): each atom is a factor-one candidate with q = MD and delta = 0. When its component in B_t has one gap, Theorem 3 separates it, because floor(r/D) flips. The rule is not in the class of Theorems A and B: it reads floor(M r/q), not an additive digit statistic. I have not shown that the atoms' components are free of mixing at the huge heights where those atoms live.
- Dyadic-residue and orientation obstructions: these are M = 1 class rules for right angles and do not apply to P choice rules.
- Height-independent cores G_B^o: not tested against this rule. The full-system tests below contain the B <= 256 blocks.

## External results used

- Euclid's parametrization of Pythagorean triples (standard); used only through the archive's audited T1 and the elementary factorization in Lemma 1.
- No published theorem beyond that. The archive inputs, all audited, are: the fixed-factor lemma and its relations (5)-(7) and (17) (continuation_hilbert_factor_one_choices.md, Sections 1, 2 and 6; continuation_hilbert_factor_choices_audit.md); T1 of hilbert_p_family_counts.md; and the five-label table of continuation_hilbert_two_choice_obstruction.md.

## Checks

All scripts are in scripts_hb4_t_rule/: build.py, analyze.py, gapsets.py, rules.py, binding_rule.py and binding_rule_t.py. Each was run with py -B, one at a time, each under 35 s and well under 1 GB. The repository was only read.

- build.py is my own rebuild of the archive's in-strip candidate definition, with factor and role data added. It reproduces the archive counts exactly: 145141 rows and 139237 distinct triples at (2048, 32, 3), 163060 at (2048, 32, 2), 173065 at (2048, 32, 4), 717584 rows and 695871 triples at (4096, 32, 3).
- Lemma 2 check at (2048, 32, 3): 89 (small factor, line) keys and 929 (large factor, line) keys, each with exactly one gap. Lines with constraints: 862. Gaps per line: 1 on 647 lines, 2 on 185, 3 on 30. The number of distinct factors per line matches the number of gaps exactly.
- Gap sets per label: 159699 labels with one gap, 12067 with two, 85 with three. Same-line constraints: 11038 of 145141 rows. Only 4 lines carry same-line constraints with two rank gaps: T = -290, 289, 293, 294, with gaps 10 (delta -1, factor 256) and 14 (delta 0, factor 441).
- Rules at (2048, 32, 3), violated constraints out of 139237:
  - random choice in {0,1,2}: 21.8%
  - random choice in {0,1}: 23.9%
  - parity at the factor-one T-scale alone: 13.3%
  - binding-gap rule of Theorem 3 with t = 1: 1.54%, all on mixed-gap edges
  - the sum-mod-M variant: 1.40%, all on mixed-gap edges
- Binding-gap rule, all runs:

| Run (h, S, M) | t | Violated | Binding components | Mixed |
|---|---:|---:|---:|---:|
| (2048, 32, 2) | 1 | 1383 | 38793 | 3073 |
| (2048, 32, 3) | 1 | 2149 | 53102 | 3700 |
| (2048, 32, 6) | 1 | 323 | 21918 | 282 |
| (4096, 32, 3) | 1 | 20224 | 283062 | 34730 |
| (2048, 8, 4) | 1 | 49145 | not recorded | 33659 |
| (2048, 8, 4) | 2 | 35677 | not recorded | 12567 |

  Every violation was on a mixed-gap edge, as Theorem 3 predicts. The t = 2 run violates fewer constraints than t = 1, as Theorem 4 predicts. The (2048, 32, 4) and (2048, 32, 8) runs had zero violations, but trivially (see gaps).
- Hand checks: Lemma 1, Lemma 2, Theorems 3 and 4, and Corollary 3a against the five-label table: X = 64 gives q = 2, X = 1120 gives q = 35, and D = (138, 649) is on T = 511 with both gaps.

## Gaps

- The route's target is not reached. I have no bounded-M rule for all factors, and no rule for any infinite set of factors with a > S^2/32. I also have no impossibility result for rules that read the rank at a T-dependent scale: Proposition 5 shows the full class F(r, T) is every rule, so impossibility for it is the open question itself.
- Theorem 3 removes everything except the components of the binding graph that carry two or more gaps. I prove nothing about those mixed components: their number, their size, their cycle structure, or a rule for them.
- Lemma 2 (one gap per factor and line) holds only for a <= S^2/32. For larger factors, uniqueness is proved only per label, role and side. At h = 2048, S = 32, M = 3, every (factor, line) pair had a single gap, including large factors. That is data, not a theorem.
- Theorem 4 is a sufficient condition, not a characterization. Its useful range depends on the component sizes of H_b, which I did not bound. I expect H_b to have giant components when the density mu/2^b is of order 1, which leaves about m - log2(mu) usable bits.
- Whether Lemma A and Lemma B atoms sit in components with a single gap, at the heights where they exist, is not checked.
- The tests cover only h = 2048 and 4096 (S = 32), plus one S = 8 run, which only emulates higher density. The zero violations at S = 32 with M = 4 and M = 8 are trivial: there SM >= 2 sqrt(h), so by T1 no gap is divisible by M and xi = 0 already works. Those runs are not evidence for bounded M.
- Like the archive's own checks, the candidate system uses the in-strip test but not the owner-column genuineness test. That only adds constraints, so it is conservative for a positive rule.
- Mixed supports, right angles, the sea, collars, and the H7 blocks (row step 28) are untouched.

## Missing estimate

I need a theorem about gap mixing. Call (a, q) a resonance and its window W_a(q) = {T : |T + (eps a + 1)/2 - eps A_a q^2| < 4 sqrt q}. A label is mixed when its partners' windows from two binding resonances overlap at its line. Theorem 3 reduces the P family at bounded M to one of the following two statements.
(A) For each k, a rule with M independent of k that handles components carrying k gaps.
(B) A proof that the mixed components of B_t are sparse and tree-like enough for a local repair, for example: no cycle in B_t passes through two mixed labels within rank distance O(max gap/M).
Two windows W_a(q) and W_a'(q') overlap only if |a' q^2 - a q'^2| is at most about a a'(sqrt q + a)/S^2. These are small values of an indefinite binary quadratic form, which is a Pell-type condition. So (B) is a counting problem for small values of a' x^2 - a y^2 along Hilbert partner windows. With the archive's mean degree mu ~ (16/(pi S)) log(4h/S^2), a typical label at large h lies in about mu windows. Then mixing is generic and (B) should fail at fixed S, which matches the growth from 7.0% to 12.3% of components between h = 2048 and h = 4096. For a fixed-S, bounded-M result, (A) is therefore what is needed. In 2-adic form (Theorem 4, M = 2^m), (A) asks for the bits beta_b, which are constant on the components of H_b, to split every constraint with v2(q) >= m. That needs H_b to break into small components for every b >= log2(mu) + O(1).

## Next steps

- Have someone audit Lemma 2's extension from one label to a whole line, and Theorem 3. Both are short and are the only new load-bearing steps.
- Study mixed components at M = 3, S = 32, h = 4096: their size distribution, cyclomatic number, and how many are satisfiable with three values (exact search per component, which is small). If every mixed component is solvable within {0,1,2} while single-gap components keep {0,1}, then the P certificate needs only local repairs. Then test whether the repair stays local as h doubles.
- Try a two-level rule for mixed components with two gaps q1 < q2: xi = t1 psi_q1 + t2 psi_q2 with t1 != +-t2 and t1 + t2 <= M - 1. This handles delta = 0 edges of both gaps by signed-binary uniqueness. Characterize which delta != 0 edges it can hit, and whether M = 4 or M = 6 suffices for every two-gap component.
- Refuting single-scale rules Phi(T, floor(r/w(T)) mod P) needs lines carrying delta = 0 same-line pairs at P or more incompatible rank gaps, with offsets spread mod w. The diagonal-block lemma gives recurring offsets rho_I in 2B^2 {sum over U of 4^l}. Search the lines of G_B^o for such gap sets, starting with the line family T = 289..294, which has rank gaps 10 and 14.
- In 2-adic form, measure the component sizes of H_b against b at S = 32 (h = 4096 and translated patches) to check the prediction that about m - log2(mu) bits are usable.
- Port Theorem 3 to the H7 blocks (row step 28, S = 6272 sigma). The proof uses only the slot structure q = Md + delta and the candidate-graph definition, so it should transfer verbatim; Lemma 2 needs the condition a <= S^2/(16d) of Section 8.

