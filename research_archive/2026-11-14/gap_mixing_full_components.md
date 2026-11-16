# Distinct gaps in full candidate components

14 November 2026. Problem 001. Continues continuation_gap_mixing_audit.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: full candidate components do not have a bounded number of gaps. In the near-diagonal band they form a giant component carrying almost every available gap; exact block certificates at S = 32, M = 3 give at least 9, 32, 84, 203 and 480 distinct gaps in one full component at every h >= 8705, 33793, 133121, 528385 and 2105345 (conditional on the unaudited Corollary A1 of hilbert_p_height_independent_cores.md), and the H7 zero block gives 4, 7 and 12. Proved: an exact edge-diagonal identity, a multiplicative drift bound, a per-factor gap budget, that window arithmetic cannot bound gap counts, a dyadic two-value rule for any number of gaps, and a 3-adic version of Theorem 2. Consequence: the right repair unit is a component of the weighted M-core, which needs no boundary lists. Audited in audit_gap_mixing_full_components.md (correct with fixable gaps; the counts are for the id orientation, and Corollary A1 is confirmed by brute force at h0(32) = 2305).

# Result

## Status

partial

## Summary

Full candidate components do not have a bounded number of gaps. In the near-diagonal band they form a giant component that carries almost every available gap. Exact block certificates at S=32, M=3 give at least 9, 32, 84, 203 and 480 distinct gaps in one full component at every h >= 8705, 33793, 133121, 528385 and 2105345. The H7 zero block gives 4, 7 and 12. On the proof side, I proved an exact edge-diagonal identity, a multiplicative drift bound, a per-factor gap budget, and a theorem that window arithmetic cannot bound gap counts. I also proved a dyadic two-value rule for any number of gaps and a 3-adic version of Theorem 2. Consequence: Theorem 1 cannot be the global mechanism. The correct repair unit is a component of the weighted M-core, which needs no boundary lists. A side result, computer-assisted: the M=3 two-gap case is solvable whenever a is odd or v3(a) <= 4, so it stays open only for 486 | a.

## Statements

Setting. Profile with row step D (even), odd rows a0 + D i, even rows b0 + D j, c = b0 - a0 (odd). The full grid has D = 2, c = 1. H7 has D = 28, c = BRES - 17. Placement x_e = S(M r_e + xi_e), Hilbert ranks, locality max(Di^2, Dj^2) < 16|Dr|, T = j - i. A candidate constraint (e, f, delta) has r_e < r_f, d = r_f - r_e, q = Md + delta >= 1, |delta| <= M-1, and a cross pair (odd point of o, even point of eps, {o, eps} = {e, f}) with X = Sq, Y = |b_eps - a_o|, X^2 + Y^2 = L^2. The smaller half-factor is a = (L-Y)/2. A "full component" is a component of the full candidate graph at the given M. "Normalized design" means S = 8 D^2 sigma (S = 32 sigma in the full grid, S = 6272 sigma in H7). Put rho = 1/sqrt(sigma M).

PROVED

L1 (exact edge diagonal). Put U := j_eps - i_o and eta := sign(b_eps - a_o). Then c + D U = eta Y = eta (S^2 q^2/(4a) - a). So U = U_{a,eta}(q) is determined exactly by (a, q, eta), with no error term. Both endpoints v satisfy |T_v - U| < 4 sqrt(d) <= 4 sqrt(q). In the full grid this reads 2U + 1 = eta Y. Lemma 2 of the reduction note is the special case where a <= S^2/32.

L2 (drift). (i) Two constraints sharing a label have |U1 - U2| < 4(sqrt d1 + sqrt d2). (ii) Each constraint has |T_e - T_f| < 8 sqrt d. (iii) For a full component C, let J(C) be the hull of its edge diagonals, l(C) its length, tau(C) its T-range and d* its largest rank distance. Then l(C) < tau(C) + 8 sqrt(d*) and tau(C) < l(C) + 8 sqrt(d*). (iv) Multiplicative drift in a normalized design: for every constraint and both endpoints, |T_v - U| < rho(|U| + |c|/D) + 4. So one constraint changes |T| by at most a factor (1+rho)/(1-rho), up to O(1). At S = 32, M = 3 this factor is about 3.73. The near-isosceles vectors (L = X + 1) attain the bound up to rounding.

T3 (budget for one factor and sign). Fix a full component C, a factor a and a sign eta. The n distinct gaps that C carries with that (a, eta) satisfy (n-1)^2 <= 4aD l(C)/S^2. In the full grid this is n <= 1 + sqrt(8a l(C))/S. If two of them are q1 < q2, then every path in C from an endpoint of a q1-constraint to an endpoint of a q2-constraint, with rank distances d'_i, satisfies S^2(q2^2 - q1^2)/(4aD) < 4 sqrt(d1) + 4 sqrt(d2) + 8 sum sqrt(d'_i). Hence #gaps(C) <= sum over (a, eta) present of (1 + floor(sqrt(4aD l(C))/S)). Also every gap of C is at most (Y^2 - 1)/(2S), with Y <= |c| + D max|U|.

T4 (window arithmetic cannot bound gap counts; full grid, S = 2^s >= 8, M >= 2). The near-isosceles vectors are v_{n,sg}: Y = Sn + sg, q = n(Sn/2 + sg), L = (Y^2 + 1)/2, a = (Y-1)^2/4, U = (Y-1)/2, with sg = +-1. Consider the necessary windows {T : |T - U| < 4 sqrt(d), d in {floor(q/M), ceil(q/M)}}. Consecutive windows in the order (n,-1), (n,+1), (n+1,-1), ... share an integer whenever floor(q/M) > S^2/256 for both vectors. At (S, M) = (32, 3) they share one for every n >= 1 (exact check through n = 400). So, for h > S^2 n0^2/2, window arithmetic alone links at least 2 floor((sqrt(2h-3) - 1)/S) - 2 n0 distinct gaps into one chain. Here n0 is the least n from which consecutive windows always overlap, and n0 = 1 at (32, 3). Any upper bound on gaps per full component that uses only the L1 and L2 conditions is therefore at least of order sqrt(h)/S. A uniform bound would have to use the exact Hilbert coincidences.

L5 (interleaved intermediate values). Let F_d(r) = j_{r+d} - i_r, and let q be a gap with M not dividing q and d0 = floor(q/M) >= 1. The interleaved sequence F_{d0}(r), F_{d0+1}(r), F_{d0}(r+1), F_{d0+1}(r+1), ... has steps in {-1, 0, 1}. Hence, on any rank interval where F_{d0} takes values both <= U and >= U, some r has F_d(r) = U with d in {d0, d0+1}. That pair is a role-1 cross pair with exact row difference c + DU, and slot delta = q - Md lies in [-(M-1), M-1]. So every P vector whose gap is not divisible by M, and whose diagonal is crossed in this way, has an actual candidate edge, given the in-strip completion.

T6 (dyadic two-value rule for any number of gaps). Fix M and t in {1..M-1}. Let Q be the gap set of a full component, D_Q = {q in Q : M | q} with rank differences q/M, and E_t the set of binding slot rank differences. That set contains d0 = floor(q/M) when q mod M = t and d0 >= 1, and d0 + 1 when q mod M = M - t, for q not in D_Q. Suppose every q/M with q in D_Q has the same 2-adic valuation alpha, and every e in E_t has v2(e) > alpha. Then xi_r = t (floor(r/2^alpha) mod 2) solves every finite rank set; if D_Q is empty, use constant zero. Conversely, if the system contains all constraints of these gaps at all ranks, a rule t (floor(r/g) mod 2) works if and only if this dyadic condition holds. Theorem 2 of the gap-mixing audit is the case M = 3 with two gaps.

T7 (3-adic version of Theorem 2, M = 3, q0 = 3a, q1 = 3b + s). If v3(b) > v3(a), put g = gcd(a, b) and xi_r = pi(floor(r/g) mod 3), with pi = (0,1,2) for s = 2 and pi = (0,2,1) for s = 1. If v3(b+1) > v3(a), put g = gcd(a, b+1), with pi = (0,2,1) for s = 2 and (0,1,2) for s = 1. Either rule solves every finite rank set.

L8 (local form of Theorem 1). For each label f, b^-(f) <= sum over q in Q^-(f) of sigma_M(q) <= 2|Q^-(f)| - k0^-(f) <= 2s - k0. So increasing-rank greedy, with the per-label count of earlier gaps, implies the k0 >= 1 clause of Theorem 1. Only the k0 = 0 clause (constant zero) needs the component-level gap set.

L9 (core reduction, the boundary-free combination). Let K be the weighted M-core of the full candidate multigraph. Each vertex of K has at least M distinct incident triples inside K. If every component of K has an assignment satisfying its internal constraints, then any such assignments combine. Peeled labels are then assigned in reverse order of deletion with the full palette, so no boundary lists are needed. Conversely, every global solution restricts to K. The correct unit for applying Theorems 1, 6, 7 and C2 is a component of K, with its internal gap set, not a full component.

COMPUTER-ASSISTED (exact, P family only)

C1 (gap counts grow; S = 32, M = 3). By Corollary A1 of hilbert_p_height_independent_cores.md, the block system G_B^o embeds in the genuine-rival candidate graph at every h >= h0(B) = 2B^2 + 8B + 1. I re-checked its proof for both the genuine and the candidate (no owner test) versions. The maximum number of distinct gaps in one full component of G_B^o is 2, 9, 32, 84, 203 and 480 for B = 32, 64, 128, 256, 512 and 1024. In the candidate version it is 2, 9, 32, 85, 210 and 489. So for every h >= 8705, 33793, 133121, 528385 and 2105345, the full candidate graph has a full component with at least 9, 32, 84, 203 and 480 distinct gaps. At B = 1024 that component has 251007 labels, and it carries 480 of the 491 gap values present in the candidate block system. Its backbone is the near-isosceles family of T4: 60 of the 63 such gaps with Y < 1024 lie in the B = 512 giant. The weighted 3-core of G_512^o has 2 components with 73 and 59 gaps. The 3-core of G_1024^o has 5 components with 318, 234, 81, 59 and 43 gaps. G_256^o has an empty 3-core, so there the giant is solved by peeling, although it carries 84 gaps.

C1-H7 (zero block BRES = 24, M = 3, all local candidates of a main-diagonal index block). The maximum gaps per full component is 4, 7 and 12 at B = 512, 1024 and 2048. The largest L is 1.29e7, 4.8e7 and 2.35e8. Mean weighted incidence is 0.083, 0.130 and 0.182. The class-9 block at B = 512 has only single-gap components. Embedding these blocks into the real H7 board at large h uses the Corollary A1 argument, which I did not write out separately for H7.

C2 (M = 3, two gaps). Every system q0 = 3a, q1 = 3b + s is solvable on every finite rank set if a is odd (Theorem 2) or v3(a) <= 4. Put k = v3(a) + 1. A (2 * 3^k)-periodic solution exists for every residue of b and both s. This was checked exhaustively for k <= 5. For k = 1 the check is plain brute force over all 3^6 sequences; for k >= 2 it uses SAT, and every returned solution was re-verified. The two-gap three-choice class is open only for a even with 486 | a, that is 1458 | q0. The dominant uncovered pair in the block data, (252, 260), is the near-isosceles pair with n = 4 and has 8- and 18-periodic solutions.

## Proofs

L1. Here b_eps - a_o = b0 + D j_eps - a0 - D i_o = c + D U. From ab = (Sq/2)^2 we get b = S^2 q^2/(4a), so Y = b - a = S^2 q^2/(4a) - a. Also T_o = U - (j_eps - j_o) and T_eps = U - (i_eps - i_o), and |r_eps - r_o| = d, so locality gives |T_v - U| < 4 sqrt(d). Finally d <= q, because q >= M(d-1) + 1 >= d. QED.

L2. (i) A shared label v gives |U1 - T_v| < 4 sqrt(d1) and |T_v - U2| < 4 sqrt(d2). (ii) Both endpoints lie within 4 sqrt(d) of U. (iii) Every edge diagonal lies within 4 sqrt(d*) of a label of C, and every label of C lies within 4 sqrt(d*) of an edge diagonal. (iv) Y^2 = L^2 - X^2 >= 2X + 1, so q <= (Y^2 - 1)/(2S), and d <= ceil(q/M) <= (q + M - 1)/M. Then 16d < 8Y^2/(SM) + 16, so 4 sqrt(d) < Y sqrt(8/(SM)) + 4 = Y/(D sqrt(sigma M)) + 4 when S = 8 D^2 sigma. Use Y <= |c| + D|U|. For a vector with L = X + 1, Y^2 = 2X + 1 and d is about q/M, so the bound is attained up to rounding. QED.

T3. By L1, constraints with the same (a, eta) and gaps q1 < q2 have edge diagonals differing by exactly S^2(q2^2 - q1^2)/(4aD). All of them lie in J(C), so S^2(q_n^2 - q_1^2)/(4aD) <= l(C). Since q_n >= q_1 + n - 1, q_n^2 - q_1^2 >= (n-1)^2. For the path bound, combine this exact difference with L2 (i) and (ii) along the path. Summing over (a, eta) gives the total bound. The gap ceiling follows from q <= (Y^2 - 1)/(2S). QED.

T4. (Sq)^2 + Y^2 = L^2 with L = X + 1 holds exactly when X = (Y^2 - 1)/2. With Y = Sn + sg we get Y^2 - 1 = S^2 n^2 + 2 sg S n, so q = X/S = n(Sn/2 + sg) is an integer, and a = (L - Y)/2 = (Y-1)^2/4. In T1 normal form these are k = 1, e' = n, E = Sn/2 and O = E + sg. Consecutive diagonals differ by Delta in {1, S/2 - 1}. The integer T = U1 + ceil(Delta/2) is within S/4 of both diagonals. So both windows contain it once each half-width 4 sqrt(floor(q/M)) exceeds S/4, that is, once floor(q/M) > S^2/256. At (32, 3), n = 1 gives d in {5, 6} > 4, and n >= 2 gives floor(q/M) >= 20. An integer check confirmed overlap for every n <= 400. The condition L <= h - 1 is Y <= sqrt(2h - 3). The gaps are strictly increasing in (n, sg), so they are distinct. The windows are exactly what L1 and L2 constrain, so this chain satisfies every arithmetic necessary condition. QED.

L5. Consecutive Hilbert cells differ by a unit vector. So F_{d0+1}(r) - F_{d0}(r) = j_{r+d0+1} - j_{r+d0} lies in {-1, 0, 1}, and F_{d0}(r+1) - F_{d0+1}(r) = -(i_{r+1} - i_r) lies in {-1, 0, 1}. The discrete intermediate value theorem gives a hit. When M does not divide q, both d0 and d0 + 1 are admissible slots, with delta = q - Md0 in [1, M-1] and delta = q - M(d0+1) in [1-M, -1]. QED.

T6. Put P(r) = floor(r/2^alpha) mod 2. Then P(r + n 2^alpha) = P(r) + n mod 2 for all integers r, n. Take xi = tP, so every difference lies in {0, t, -t}.
- A constraint from D_Q has delta = 0 and rank difference d' = 2^alpha times an odd number, so the two values differ.
- A constraint with delta outside {0, t, -t} is never active.
- If delta = t, the slot is (d0, t), so the rank difference d0 is in E_t. It is a multiple of 2^(alpha+1), so P is unchanged and the difference is 0.
- If delta = -t, the slot is (d0 + 1, (M - t) - M), and the same argument applies.
For the converse, suppose g does not divide a required shift n. Then floor((r+n)/g) - floor(r/g) takes the two values floor(n/g) and floor(n/g) + 1 at r = 0 and r = g - 1. One of them violates the requirement: for D_Q the index shift must be odd, and for E_t it must be even. Antiperiodicity P(r + g) = 1 - P(r) turns any r with P(r+e) != P(r) into one with the forbidden sign. If g divides every shift, the condition on n/g is exactly the dyadic condition. QED.

T7. M = 3, so the constraints are: shift a forbids 0; shift b forbids s (when b >= 1); shift b + 1 forbids s - 3. Also floor((r + ng)/g) = floor(r/g) + n.
Case v3(b) > v3(a), g = gcd(a, b). Then 3 does not divide a/g, and 3 divides b/g.
- Shift a changes the index by a nonzero amount mod 3. Since pi is a bijection, the values differ.
- Shift b leaves the index unchanged mod 3, so the difference is 0, which is not s.
- Shift b + 1 changes the index by 0 or 1 mod 3. The differences pi(k+1) - pi(k) are {1, 1, -2} for (0,1,2) and {2, -1, -1} for (0,2,1). These avoid -1 (forbidden when s = 2) and -2 (forbidden when s = 1) respectively.
Case v3(b+1) > v3(a), g = gcd(a, b+1).
- Shift b + 1 leaves the index unchanged mod 3, so the difference is 0.
- Shift b changes the index by 0 or -1 mod 3. The differences pi(k-1) - pi(k) are {-1, -1, 2} for (0,1,2), which avoids 1 (s = 1), and {-2, 1, 1} for (0,2,1), which avoids 2 (s = 2).
- Shift a is handled as in the first case. QED. A script checked 3688 triples with a, b <= 60 on ranks -400..400 and found no failure.

L8. An earlier label at rank r_f - d with a constraint of gap q needs d in D_M(q), and delta = q - Md is then determined. So the distinct earlier triples at f number at most sum over q in Q^-(f) of sigma_M(q). Each forbids at most one value. Q^-(f) is contained in Q(C). QED.

L9. Induced subgraphs on distinct components of K have no edges between them. A label deleted in peeling round k has fewer than M triples to labels still alive at that time. Those are exactly the labels assigned before it in reverse order. So at least one value is free whatever was chosen on K, and no list restriction ever reaches K (this is T5 of the P census and L6 of the H7 census). QED.

C1 and C1-H7. These were built by my own implementations.
- Constraint counts match the archive exactly: 229 and 216 (B = 32, id and swap), 1726, 48419, 250953 and 1205405 for G_B^o. The 3-core sizes match too: 3134 labels and 6197 constraints at B = 512, and 40136 labels at B = 1024.
- Components were computed with scipy connected_components on distinct triples.
- Monotonicity in B holds for the candidate version. The Q3 child of an id or swap diagonal 2B-block is a pure translation with the same orientation, so the candidate version of G_{2B}^o contains a copy of the candidate version of G_B^o.
- The owner filter breaks this nesting. That is why the genuine numbers are certified separately per B.

C2. A P-periodic sequence is a solution on Z exactly when it satisfies the reduced shifts (a mod P, b mod P, (b+1) mod P) for every residue. If v2(a) >= 1 and v3(a) = k - 1, then a mod 2*3^k is 2*3^(k-1) or 4*3^(k-1). So for each k, 4 P_k instances cover every such a and every b.
- k = 1 (P = 6): exhaustive over all 729 sequences. Every pair (a mod 6, b mod 6, s) with a mod 6 != 0 is solvable.
- k = 2..5 (P = 18, 54, 162, 486): SAT (CaDiCaL 1.5.3 through pysat). Every returned sequence was re-verified against all P residues.
- 63 random instances, including (84, 86, 2), (344, 338, 2) and (1360, 1370, 2), were re-verified directly on integer ranks -3000..3000.
QED for C2, with no claim for k >= 6.

## External results used

- Hilbert locality max(Di^2, Dj^2) < 16|Dr| (Theorem 1 of continuation_hilbert_placement.md, audited). Used in L1, L2, T3 and T4.
- Euclid and 2-adic normal form T1 of hilbert_p_family_counts.md (audited). Used only to identify the near-isosceles vectors as k = 1, e' = n, O = E +- 1.
- Theorem A and Corollary A1 of hilbert_p_height_independent_cores.md: main-diagonal Hilbert blocks are id or swap, occupy contiguous rank intervals, and embed into the candidate graph at every h >= 2B^2 + 8B + 1. The note itself is unaudited; I re-checked the proof. Used for C1.
- Theorems 1 and 2 and Section 5 of continuation_gap_mixing_audit.md (audited). T6 and T7 generalize Theorem 2.
- pysat with the CaDiCaL 1.5.3 backend, used only to find periodic sequences. Every claimed solution was re-verified independently; no UNSAT result is used in any claim.

## Checks

All scripts are in scripts_gm1_full_comp/ (55 KB). Each ran with py -B, one at a time, under 60 s and well under 1 GB. The repository was only read, and no git command was run.

- gb_components.py (B, S, M, orient): builds G_B with and without the owner filter, then reports full components, distinct gaps, and Theorem 1 and T6 coverage at M. It reproduces the archive counts exactly: 229/216 (B = 32 id/swap), 1726, 10130, 48419, 250953 and 1205405. Maximum distinct gaps per full component (genuine/candidate): B32 2/2, B64 9/9, B128 32/32, B256 84/85, B512 203/210, B1024 480/489. At B = 1024 the genuine giant has 251007 labels. Coverage at M = 3 for G_1024^o: 18409 components by Theorem 1, 2750 more by T6, and 2710 uncovered.
- core_components.py: weighted M-core and its components. B256: empty 3-core. B512: 3134 labels, 6197 constraints (matches the archive), 2 components with 73 and 59 gaps. B1024: 40136 labels (matches), 5 components with 318, 234, 81, 59 and 43 gaps.
- iso_check.py:
  - Window overlap of the near-isosceles chain holds for all n <= 400 at (32, 3).
  - All 31 (B = 256) and 63 (B = 512) near-isosceles gaps are present. 28 and 60 of them lie in the giant.
  - Two-gap full components with k0 = 1 split as follows: 436 covered by Theorem 2 and 87 not (B = 256); 892 and 299 (B = 512).
  - The dominant uncovered pair is (252, 260), with 71 and 233 components; then (1032, 1016).
- h7_block.py: H7 zero block, maximum gaps 4, 7 and 12 at B = 512, 1024 and 2048. The class-9 block at B = 512 has 1661 constraints and single-gap components only.
- two_gap_m3.py: T7 checked on 3688 triples on ranks -400..400 with no failure; periodic solutions for sample pairs.
- dyadic_period.py and family.py: reduction mod 2^(alpha+1) for alpha <= 6, and analysis of the explicit block families.
- modp.py: exhaustive check for P = 3..7; P = 6 solves every a mod 6 != 0.
- modP_sat.py and lift.py: P = 2*3^k for k <= 5, no failures; k = 6 timed out and is not claimed.
- leftover.py: all leftover cases with a <= 40 and b <= 80 have periods <= 15.
- cert_check.py: 63 instances re-verified on integer ranks -3000..3000, 0 failures.
- Proofs checked by hand: L1, L2 (including the constant in (iv)), T3, T4 (including the n = 1 case at (32, 3)), L5, T6 with its converse, T7 (all four sign cases), L8 and L9.

## Gaps

- No analytic proof that the maximum number of distinct gaps per full component tends to infinity. Growth is certified only by exact block computations (B <= 1024 at S=32; B <= 2048 for the H7 zero block). T4 proves only that window arithmetic cannot give a uniform bound. L5 proves that edges exist for each non-divisible vector, not that components connect.
- C1 depends on Corollary A1 of hilbert_p_height_independent_cores.md, which is marked not audited there. I re-read and re-checked its proof, and my independent builder reproduces all of its archived constraint counts. A separate audit is still owed.
- The H7 embedding of C1-H7 (diagonal index blocks with bulk rows, in-strip completion at large h) uses the Corollary A1 argument transferred to row step 28. I did not write it out or audit it. I used only the zero block and one class-9 block, with no owner filter.
- C2 covers v3(a) <= 4 only. The pattern that 2*3^k-periodic solutions exist for every residue is verified for k <= 5 and is conjectured for all k. No lifting lemma is proved. The case with a even and 486 | a stays open. A separate computation solves the reduced systems mod 2^(alpha+1) for alpha <= 6, except the residues (s=1, v2(b)=alpha) and (s=2, v2(b+1)=alpha). Small leftover cases have odd periods 5..15. This is evidence only.
- The heuristic law that the giant's gap count is about C B (log B)^2 / S (ratio about 2.4 per doubling, matching 2(1 + log2/log B)^2) is not proved. Neither is the H7 onset estimate of h about 1e9 to 1e10 for a giant.
- SAT solvability of M-core components (archive Theorem B: cores of G_512 and G_1024 are 3-SAT) does not certify the global system, because G_B omits owner-in-block constraints and other components may attach. I did not attempt to solve core components by a structured rule.
- P family only. R2s, FW, 6PT, Lambda3 and Lambda4, the sea and the collars are untouched. Nothing here proves a quadratic-width board.
- I did not rebuild the full-grid census at h = 2048 or 4096. Full-grid statements at those heights use the archive's per-label tables: 85 labels with 3 gaps at h = 2048, and max F of 2, 3, 4, 5 at h = 1024..8192.

## Missing estimate

For a bounded-M P certificate on this placement, the needed statement is not a bound on gaps per full component. That bound is false in the near-diagonal band (C1) and unobtainable from window arithmetic (T4). What is needed is a structural solution of each component of the weighted M-core (L9). At S = 32, M = 3 those components already carry 43 to 318 distinct gaps at B = 1024. So componentwise rules that read only the gap set (Theorem 1, T6, T7, C2) cannot handle them. Concretely, one needs either:
(a) a rule for M-core components that uses rank structure beyond the gap set, for example periodic rules whose period is tied to the 2- and 3-adic structure of the D-gaps, as C2 does for two gaps; or
(b) a design change that keeps the near-diagonal band subcritical. By L2(iv) the window ratio there is rho = 1/sqrt(sigma M). The density there scales like (log h)^2/S, which is the band excess C4' already pays for with its level-K stride.
For priority 1, the missing piece is a lifting lemma from 2*3^(k-1)-periodic to 2*3^k-periodic solutions, or any uniform construction for 486 | a.

## Next steps

- Priority 1: push C2 to k = 6, 7 in split runs under 60 s each, at about 1458 and 4374 instances per run. In parallel, look for a lifting lemma by studying the structure of the 2*3^k-periodic solutions (for example, whether one can be chosen constant on residue classes mod 3^(k-1) composed with a fixed Z/6 pattern). A proof for all k settles the three-choice two-gap case completely.
- Priority 2: adopt L9 as the combination principle. Classify the components of the weighted 3-core of G_512^o and G_1024^o: cycle structure, which gaps are D-gaps, and whether each admits a periodic rule as in C2 restricted to the component. This replaces boundary lists for everything outside the core.
- Audit L1 to L5, T6, T7 and the C1 embedding (Corollary A1). They are short, and C1 is the load-bearing claim that full components carry unboundedly many gaps in practice.
- Try to turn L5 into an analytic connectivity statement for the near-isosceles backbone. Show that consecutive vectors v_{n,-1} and v_{n,+1} (U differing by 1, rank distances differing by about 2n/M) share a label in every diagonal block of side >= C n. That would give an analytic proof that gap counts per component are unbounded.
- For H7 and C4': estimate the near-diagonal giant onset in normalized designs (S = 8 D^2 sigma), using the exact ratio rho = 1/sqrt(sigma M) of L2(iv) and the near-isosceles density mod 2S. Then check whether the level-K stride of C4' keeps the band subcritical with bounded M.
- Record in the ledger: T6 (dyadic rule for any number of gaps, with its converse), T7 (3-adic rule), C2 (two-gap M = 3 solved unless 486 | a), and C1 (full-component gap counts 9 / 32 / 84 / 203 / 480 at the stated heights, S = 32, M = 3).

