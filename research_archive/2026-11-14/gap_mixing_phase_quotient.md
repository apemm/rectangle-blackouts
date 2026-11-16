# A phase quotient for Beatty pieces

15 November 2026. Problem 001. Continues continuation_gap_mixing_audit.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (partial): a phase-quotient theorem for pieces carrying Beatty assignments with their own tau and real phases. One tau never covers a real 3-core component at M = 3, and phases beat Z/3 shifts on G_512 only with tiny pieces. Not audited yet.

# Result

## Status

partial

## Summary

I proved a phase-quotient theorem for Beatty pieces. One tau never covers a real 3-core component at M = 3. Phases beat Z/3 shifts on G_512, but only with tiny pieces.

## Statements

Problem 001, P family only. Nothing below is audited. The proofs are in the proof field. Labels: PROVED means a complete proof is given here. COMPUTED means an exact finite computation on a fixed system, with UNSAT verdicts reported by CaDiCaL without proof logging.

NOTATION. T = R/Z, ||x|| = distance to Z, M >= 2. I_k = [k/M, (k+1)/M) in [0,1). The digit of y in T is D(y) = floor(M{y}). A constraint e = (r, u, delta), r < u, forbids xi_u - xi_r = delta. Its rank difference is d = u - r, its gap is q = Md + delta, and its slot is (d, delta). K_delta = {k : 0 <= k and k + delta <= M-1}, so |K_delta| = M - |delta|. "Certified" means mod-M certified: xi_u - xi_r is not congruent to delta (equivalently to q) mod M.

LEMMA 0 (Beatty rules are rotation codings; PROVED). floor(M tau r + c) mod M = D(tau r + c/M). So a Beatty piece is a pair (tau, theta) in T x T with theta = c/M mod 1. Only tau mod 1 matters, and "every real phase c" means "every theta in T".

LEMMA 1 (two digits; PROVED). D(z) - D(y) = delta exactly when (y, z) lies in W_delta, the disjoint union over k in K_delta of I_k x I_{k+delta}. If D(z) - D(y) is congruent to delta mod M, then ||z - y - delta/M|| < 1/M.

PROPOSITION 2 (exact single-constraint set, and the converse of Lemma C; PROVED). Let a Beatty piece (tau, theta) carry the constraint (r, r+d, delta). Write tau d = delta/M + eps mod 1 with eps in (-1/2, 1/2].
(a) The constraint is violated exactly when theta + tau r lies in V = union over k in K_delta of I_k ∩ (I_k - eps). Its measure is (M - |delta|)(1/M - ||tau d - q/M||)_+.
(b) So the constraint holds for every phase if and only if ||tau d - q/M|| >= 1/M. Lemma C is exactly "certified for every phase", and its condition is also necessary.
(c) Suppose ||tau d - q/M|| < 1/M, tau is irrational, and the piece carries the slot (d, delta) at every rank r of an interval of length at least L0(tau, eps). Then every phase violates the constraint at some rank. If tau = a/N in lowest terms and the ranks cover all residues mod N, then a phase works if and only if theta + (1/N)Z misses V.

LEMMA 3 (forbidden phase set of a crossing constraint; PROVED). Pieces P and Q carry Beatty rules (tau_P, theta_P) and (tau_Q, theta_Q). A crossing constraint e = (r, u, delta) with r in P and u in Q is violated exactly when (theta_P, theta_Q) lies in F_e = W_delta - (tau_P r, tau_Q u), a subset of T^2.
(i) F_e is a disjoint union of M - |delta| half-open squares of side 1/M, so mu(F_e) = (M - |delta|)/M^2. In phase coordinates c = M theta in R/MZ, F_e is the union over k in K_delta of the unit lattice squares [k, k+1) x [k+delta, k+delta+1), translated by (-M tau_P r, -M tau_Q u) mod M.
(ii) Fix theta_P. The slice of F_e is empty or is exactly one half-open arc of length 1/M. That arc is I_{D(theta_P + tau_P r) + delta} - tau_Q u when that digit index lies in [0, M-1]. The same holds with the roles of P and Q swapped and -delta in place of delta.
(iii) F_e lies inside the strip Sigma_e = {||theta_Q - theta_P - beta_e|| < 1/M}, where beta_e = delta/M + tau_P r - tau_Q u. If tau_P = tau_Q = tau, then beta_e = delta/M - tau d depends only on the slot, not on the ranks.

THEOREM 4 (phase quotient; PROVED). Partition a finite rank set into pieces P. Give each piece a tau_P such that every internal constraint satisfies ||tau_P d - q/M|| >= 1/M. Choose phases theta_P in T and set xi_r = D(tau_{P(r)} r + theta_{P(r)}).
(a) Internal constraints hold for every choice of phases. The assignment is a solution if and only if the phase vector avoids every cylinder set F_e of a crossing constraint.
(b) Exact sequential criterion. Order the pieces P_1, ..., P_n and fix the phases of P_1, ..., P_{j-1}. Take each crossing constraint e that joins a rank p_e in P_j to an assigned rank w_e. Set f_e = xi_{w_e} + delta if w_e < p_e, and f_e = xi_{w_e} - delta if w_e > p_e. When 0 <= f_e <= M-1, the constraint forbids exactly the arc [lambda_e, lambda_e + 1/M) with lambda_e = f_e/M - tau_{P_j} p_e; otherwise it forbids nothing. Let Lambda_j be the set of the points lambda_e. A valid theta_{P_j} exists if and only if Lambda_j is empty or some circular gap between consecutive points of Lambda_j exceeds 1/M. The free measure is the sum over the gaps g of (g - 1/M)_+. In particular, a valid phase exists whenever there are at most M-1 distinct forbidden arcs.
(c) Phase-independent sufficient condition (a cost-weighted quotient degeneracy). For P_j and an earlier piece Q, let N_e(P_j, Q) be the number of crossing constraints between them. Let N_sigma(P_j, Q) be the number of distinct (slot, orientation) pairs among them; use N_sigma only when tau_Q = tau_{P_j}. Put cost(P_j, Q) = min(N_e, 2 N_sigma), or cost = N_e when the taus differ. If the sum over earlier Q of cost(P_j, Q) is less than M for every j, then phases exist for all pieces at once, chosen greedily.
(d) Linear pieces (tau_P in (1/M)Z, that is xi = i_P r + const mod M): continuous phases reduce to Z/M shifts. All constraints with the same (slot, orientation) between pieces with the same i forbid the same single arc, so in (c) the term 2 N_sigma improves to N_sigma.
(e) No ordering (Lovasz Local Lemma). If every piece P satisfies sum over crossing constraints e at P of (M - |delta_e|)/M^2 <= 1/8, then a valid phase vector exists. At M = 3 this allows only one crossing constraint with |delta| = 2 per piece, which is weaker than (b). It helps only for large M.
(f) The shift quotient II.1 with Beatty bases is the restriction theta_P in theta_P^0 + (1/M)Z, because D(y + kappa/M) = (D(y) + kappa) mod M.

PROPOSITION 5 (certified solutions are circular solutions; PROVED). An assignment xi is certified if and only if phi = (xi + 1/2)/M satisfies ||phi_u - phi_r - q_e/M|| >= 1/M for every constraint e. Conversely, if some phi: ranks -> T satisfies these inequalities, then D(phi + theta) is a certified solution for every theta. So the following are all special cases of one problem, the existence of a circular solution phi:
- Beatty rules that satisfy Lemma C (phi affine in r);
- block and linear rules;
- II.1 with certified pieces;
- phase quotients certified through the strips Sigma_e of Lemma 3(iii).
That problem is equivalent to certified solvability. Only the exact form of Theorem 4(a) and (b) can produce non-certified solutions.

PROPOSITION 6 (how much freedom phases add; PROVED). On a piece with p ranks and irrational tau, the phase theta realizes exactly M p distinct assignments: one for each cell between the M p distinct breakpoints k/M - tau r. Z/M shifts realize M. If tau is rational, phases realize at most M p.

THEOREM 7 (the admissible set of tau for a slot set Gamma; PROVED). Let A(Gamma) be the set of tau in T with ||tau d - delta/M|| >= 1/M for every slot (d, delta) in Gamma. For each d, let R_d be the set of residues delta mod M that occur at d.
(a) Let G(R) be the union of the closed cells [j/M, (j+1)/M] with j and j+1 both outside R, together with the isolated grid points j/M with j outside R. Then A(Gamma) is the intersection over d of {tau : d tau in G(R_d)}. It is a finite union of closed arcs and points, with endpoints in the union over d of (1/(Md))Z. The set {tau : d tau in G(R)} has measure g(R) = 1 - |R ∪ (R - 1)|/M.
(b) Union bound: mu(A) >= 1 - sum over d of (1 - g(R_d)) >= 1 - 2|Gamma|/M.
(c) Pairs: with g = gcd(d1, d2), mu equals the sum over k in Z of f1^(k d2/g) f2^(-k d1/g), where f_i is the indicator of G(R_i). Also |mu - g(R1) g(R2)| <= J1 J2 g^2/(3 d1 d2), where J_i <= M is the number of cells of G(R_i). The Fourier coefficient f^(n) vanishes for every nonzero multiple n of M. So the two conditions are exactly independent when M divides d1/g or d2/g.
(d) Lacunary existence. Let d_1 < ... < d_n be the distinct rank differences, and suppose each G(R_{d_i}) has at least one closed cell. If d_{i+1} >= 2M d_i for every i, then A(Gamma) contains a closed arc of length at least 1/(M d_n).
(e) Forcing. If R_d ∪ (R_d - 1) = Z/M, then every admissible tau has d tau = j/M for some j outside R_d. At M = 3 this happens for every d that carries two residues. If R_d = Z/M, then A(Gamma) is empty. If two forcing rank differences d and d' occur, then M gcd(d, d') tau is an integer. When gcd(d, d') = 1, tau lies in (1/M)Z, so only the linear rules xi = i r + c remain, and they work if and only if i d is not congruent to q mod M for every slot.
(f) Odd-gap lemma. Let M be odd and d odd. If Gamma contains the d-slots of all odd gaps in [M(d-1)+1, M(d+1)-1], then A(Gamma) is empty. For example, at M = 3 the d = 1 slots of gaps 1, 3 and 5 suffice. By T1 with k = e' = 1, every odd q is a P gap, with Y = |S^2/4 - q^2|.

COMPUTED (exact; S = 32, M = 3, identity orientation, owner outside the block, as in gap_mixing_full_components.md). My own builder reproduces the archive counts. G_512 has 250953 constraints and a 3-core with 3134 labels and 6197 constraints. G_1024 has 1205405 constraints and a 3-core with 40136 labels in 5 components, carrying 318, 234, 81, 59 and 43 gaps.
(C1) A(Gamma_C) is empty for every 3-core component of G_512 (2 components) and G_1024 (5 components). One Beatty rule cannot be phase-free on any core component.
(C2) Each of these 7 components has a plain solution and a certified solution (SAT). So no certified obstruction exists on these fixed systems.
(C3) The minimal killing slot sets in G_512 are {(9,0), (9,2), (10,-1), (11,0)} (gaps 27, 29, 29, 33) and {(9,0), (9,2), (10,-1), (10,1)} (gaps 27, 29, 29, 31). I proved both by hand with Theorem 7(e). The forcing rank differences are rare: 4 of 78 and 6 of 96. No R_d = Z/3 occurs. 3124 of the 3134 closed neighbourhoods are tau-admissible.
(C4) Phases against shifts on G_512. I grew connected tau-admissible pieces by BFS with a size cap, and took tau_P as the midpoint of the longest arc of A(P). The theta-circle was then cut at its breakpoints and decided exactly by SAT. With the same pieces and taus, Z/3 shifts (II.1) are UNSAT at caps 3, 5 and 7, but continuous phases are SAT; each phase model was re-checked against all 6197 constraints with 0 violations. Both are SAT at cap 2, and both are UNSAT at cap 10, 50 and uncapped (306 pieces).

## Proofs

LEMMA 0. Put A = M tau r + c. Then floor(A) mod M = floor(A) - M floor(floor(A)/M) = floor(A) - M floor(A/M), because floor(floor(A)/M) = floor(A/M) for integer M >= 1. This equals floor(A - M floor(A/M)) = floor(M{A/M}) = D(tau r + c/M). Replacing tau by tau + 1 adds M r to floor(A), which does not change the residue. QED.

LEMMA 1. The first claim is the definition of D. For the second, take representatives y and z in [0,1) with D(y) = k and D(z) = k'. Then z - y lies in ((k'-k)/M - 1/M, (k'-k)/M + 1/M). If k' - k is congruent to delta mod M, then (k'-k)/M is congruent to delta/M mod 1. QED.

PROPOSITION 2. (a) D(y + tau d) - D(y) = delta requires y in I_k for some k in K_delta, and D(y + tau d) = k + delta. As sets of reals, I_{k+delta} = I_k + delta/M. So the condition reads y + delta/M + eps in I_k + delta/M + Z, that is, y + eps in I_k + Z. Since y is in I_k and |eps| <= 1/2, the translate I_k + m with m = 1 would need k/M + 1 < (k+1)/M + 1/2, that is, 1/M > 1/2, which is false for M >= 2. The case m = -1 is symmetric. So m = 0, and y lies in I_k ∩ (I_k - eps), which has length (1/M - |eps|)_+. Also |eps| = ||tau d - delta/M|| = ||tau d - q/M||. Summing over the M - |delta| values of k gives the measure.
(b) V is empty if and only if |eps| >= 1/M. Lemma 1 gives the certified form.
(c) If |eps| < 1/M, V contains an arc of length l = 1/M - |eps| > 0, because K_delta is nonempty. Since tau is irrational, pigeonhole on the N + 1 points {j tau}, j <= N, with N = ceil(1/l) + 1, gives n <= N with 0 < ||n tau|| < l. Starting from r0, the ranks r0 + jn for 0 <= j <= ceil(1/||n tau||) move theta + tau r around the whole circle in steps shorter than l, so they meet every arc of length l. Take L0 = N ceil(1/||n tau||). If tau = a/N in lowest terms and the ranks cover all residues mod N, then the points theta + tau r run over the coset theta + (1/N)Z. QED.

LEMMA 3. (i) Apply Lemma 1 to y = theta_P + tau_P r and z = theta_Q + tau_Q u. The phase change c = M theta scales cells of side 1/M to unit squares. (ii) Given theta_P, the digit k = D(theta_P + tau_P r) is fixed. Then z must lie in I_{k+delta}, one arc of length 1/M, or in no arc when k + delta is outside [0, M-1]. (iii) Lemma 1 gives ||z - y - delta/M|| < 1/M, and z - y = theta_Q - theta_P + tau_Q u - tau_P r. QED.

THEOREM 4. (a) Proposition 2(b) applied to each internal constraint, and Lemma 3 applied to each crossing one.
(b) A constraint to an assigned rank w is violated exactly when xi_p = f_e. That means tau p + theta lies in I_{f_e}, so theta lies in I_{f_e} - tau p = [lambda_e, lambda_e + 1/M). Each crossing constraint is checked once, at the later of its two pieces.
Covering criterion. If some gap g > 1/M runs from lambda_i to the next point, then theta = lambda_i + 1/M is free. It is not in [lambda_i, lambda_i + 1/M), and an arc from lambda_j covers it only if lambda_j lies in (lambda_i, lambda_i + 1/M], but that interval contains no point. Conversely, if every gap is at most 1/M, the arc from each point reaches the next point, so the arcs cover T. The free measure is the sum of the uncovered parts of the gaps. Points of Lambda_j at most M - 1 force some gap >= 1/(M-1) > 1/M.
(c) The arcs coming from Q have total length at most N_e/M. If tau_Q = tau_{P_j}, Lemma 3(iii) puts every forbidden theta_{P_j} for a constraint of a given (slot, orientation) inside one open arc of length 2/M centered at theta_Q -/+ beta, where beta = delta/M - tau d depends only on the slot. That bounds the forbidden measure by 2 N_sigma/M. When the costs sum to less than M, the forbidden set has measure below 1, so the complement is nonempty.
(d) If tau = i/M, then tau w is in (1/M)Z, and D(tau w + theta_Q) = (i w + D(theta_Q)) mod M. Take a constraint with p = w + d in P_j and f = xi_w + delta in range. Then lambda = f/M - i p/M is congruent to (D(theta_Q) + delta - i d)/M mod 1, which depends only on the slot. With w > p and f = xi_w - delta, the same computation works with the sign changed.
(e) Give the phases independent uniform laws. The event F_e has probability p_e = (M - |delta_e|)/M^2 and depends only on the coordinates of its two pieces. So it is mutually independent of all events that share neither piece. For each e, the sum of p_f over the neighbours f of e is at most the sum over constraints at P plus the sum over constraints at Q, which is at most 1/4. Take x_f = 2 p_f <= 1/4. Then the product over the neighbours of (1 - x_f) is at least 1 - 2 sum p_f >= 1/2, so x_e times that product is at least p_e. The asymmetric local lemma gives probability at least the product of (1 - x_e) > 0 of avoiding every event, for a finite system. At M = 3, M^2/8 = 9/8.
(f) If y is in I_k, then y + kappa/M lies in I_{(k + kappa) mod M}. QED.

PROPOSITION 5. phi_u - phi_r - q/M = (xi_u - xi_r - q)/M, and ||n/M|| >= 1/M holds exactly when M does not divide n. For the converse, if D(phi_u + theta) - D(phi_r + theta) were congruent to delta, which is congruent to q, mod M, then Lemma 1 would give ||phi_u - phi_r - q/M|| < 1/M. QED.

PROPOSITION 6. As theta increases, the digit of rank r changes exactly when theta crosses a point k/M - tau r. For irrational tau these M p points are distinct, so the digits are constant on the M p cells between them. Two adjacent cells differ in exactly one digit. Every cell gives a different assignment, because each digit runs once through 0, ..., M-1 as theta goes around the circle. For rational tau, some breakpoints coincide. QED.

THEOREM 7. (a) Take x in the closed cell [j/M, (j+1)/M]. If x is interior, ||x - rho/M|| < 1/M exactly when rho is j or j + 1. At x = j/M, it holds exactly when rho = j. The map tau -> d tau is a d-to-1 covering of T, so it preserves Haar measure.
(b) Subadditivity, plus |R ∪ (R - 1)| <= 2|R|.
(c) Write F_i(tau) = f_i(d_i tau). Then F_i^(n) = f_i^(n/d_i) when d_i divides n, and 0 otherwise. Parseval sums over n = k lcm(d1, d2), and the terms are f1^(k d2/g) conj(f2^(k d1/g)), which equals f2^(-k d1/g) because f2 is real. For n != 0, f^(n) = (1 - e(-n/M))/(2 pi i n) times the sum over cells j of e(-n j/M). This vanishes when M divides n, and in general |f^(n)| <= J/(pi |n|). The error is at most the sum over k != 0 of J1 J2 g^2/(pi^2 k^2 d1 d2), which equals J1 J2 g^2/(3 d1 d2).
(d) Induction. Inside the closed arc J_i of length >= 1/(M d_i), the allowed set of d_{i+1} repeats with period 1/d_{i+1} and contains closed arcs of length >= 1/(M d_{i+1}). Since |J_i| >= 2/d_{i+1} >= (1 + 1/M)/d_{i+1}, J_i contains one of these arcs entirely.
(e) G(R) has no cell, so only grid points j/M with j outside R remain. If M d tau and M d' tau are both integers, Bezout makes M gcd(d, d') tau an integer. For tau = i/M, ||(i d - delta)/M|| >= 1/M holds exactly when i d is not congruent to delta mod M.
(f) The interval [Md - M + 1, Md + M - 1] has 2M - 1 integers. It starts at M(d-1) + 1, which is odd, so it contains exactly M odd numbers in arithmetic progression with step 2. Since 2 is invertible mod M, they cover Z/M. So R_d = Z/M, and A(Gamma) is empty by (e). QED.

C3 BY HAND. Killing set 1. R_9 = {0, 2}, so 9 tau is congruent to 1/3, and tau = m/27 with m congruent to 1 mod 3. Slot (10,-1) needs (10m + 9) mod 27 in [9, 18]. Slot (11,0) needs 11m mod 27 in [9, 18]. For m = 1, 4, ..., 25, the first value is 19, 22, 25, 1, 4, 7, 10, 13, 16, so only m = 19, 22, 25 pass. For those, 11m mod 27 is 20, 26, 5, which all fail. So A is empty.
Killing set 2. R_10 = {2, 1}, so 10 tau is an integer. Together with 27 tau an integer, this gives tau = 0, but then 9 tau is not congruent to 1/3. QED.

## External results used

- Asymmetric Lovasz Local Lemma (Erdos and Lovasz 1975; asymmetric form as in Spencer 1977 and in Alon and Spencer, The Probabilistic Method). Hypotheses in my own words: finitely many events in one probability space; each event is mutually independent of all events outside its neighbour set; and there are numbers x_e in [0,1) with P(E_e) <= x_e times the product over its neighbours f of (1 - x_f). Conclusion: with probability at least the product of (1 - x_e) > 0, no event occurs. I cite it from memory and use it only in Theorem 4(e).
- Parseval's identity on T, and the elementary bound |f^(n)| <= J/(pi |n|) for the indicator of J arcs. Used in Theorem 7(c).
- Normal form T1 of hilbert_p_family_counts.md (audited). Used only in Theorem 7(f), to note that every odd q is a P gap with k = e' = 1.
- Corollary A1 of hilbert_p_height_independent_cores.md (unaudited). Used only to relate C1 to C4 to all large h.

## Checks

All scripts are in scripts_gm2_phase_quotient/ (2.2 MB). Each ran with py -B, one at a time, under 60 s and under 1 GB. The repository was only read, and I ran no git command.
- core_cert.py rebuilds G_B^o and reproduces the archive counts exactly. G_512 has 250953 constraints and a 3-core with 3134 labels and 6197 constraints. G_1024 has 1205405 constraints and a 3-core with 40136 labels in 5 components with 318, 234, 81, 59 and 43 gaps. For every core component, the script computes A(Gamma) exactly with Fractions (always empty) and runs plain and certified SAT (always SAT).
- kill_sets.py finds minimal killing slot sets and runs the closed-neighbourhood test on G_512 (C3). I proved both killing sets by hand (proof field). The G_1024 run hit the 60 s limit, and I did not use it.
- phase_greedy.py gives the residue statistics and a naive greedy phase run: 0 internal violations, as Theorem 4(a) predicts, and 403 crossing violations, because the greedy order fails.
- phase_sat.py decides phases against shifts exactly by SAT (C4). It re-checks every model against all core constraints and finds 0 violations each time. dump_core.py caches the G_1024 core (81898 constraints), but phase_sat.py on that cache still hit the 60 s limit, so I report no G_1024 result.
- sanity_formulas.py checks three formulas exactly with Fractions. The Proposition 2 measure formula passes 3000 random (M, delta, t). The pair independence and error bound of Theorem 7(c) pass 1454 random cases. The count of M p phase assignments in Proposition 6 holds at M = 3, p = 40.
These are sanity checks, not proofs. The proofs are by hand.

## Gaps

- Nothing here is audited. Theorem 4, Propositions 2, 5 and 6, Theorem 7, and the hand checks of C3 all still need an independent second reader.
- No bounded-M theorem for P follows. Theorem 4 gives the same worst-case count as II.1: fewer than M distinct forbidden arcs, or a quotient cost below M. Phase freedom helps only through clustering of arcs (the circular-gap criterion), and I have no structural theorem that shows clustering in the Hilbert P graph.
- The measure condition asked for (bounded crossing measure per piece) is proved only as the Lovasz Local Lemma statement of Theorem 4(e). At M = 3 it is weaker than plain greedy. I found no measure-type condition that beats degeneracy at bounded M.
- C1 to C4 concern the fixed block systems G_512^o and G_1024^o (S = 32, M = 3, identity orientation, owner outside the block). Their relevance to every large h rests on the unaudited Corollary A1 of hilbert_p_height_independent_cores.md. The real graph also has constraints that G_B^o omits, so the SAT results in C2 and C4 are consistency checks for the real graph, not solutions of it.
- The UNSAT verdicts in C4 (shift quotient at caps 3, 5, 7; both quotients at cap 10 and above) are CaDiCaL results without DRAT proofs. They apply only to my BFS partition and my choice of tau_P (midpoint of the longest arc of A(P)). They do not rule out other partitions or other taus. C4 was run on G_512 only: the G_1024 runs of phase_sat.py and kill_sets.py hit the 60 s limit, so I have no minimal killing sets or phase-against-shift comparison for G_1024.
- Theorem 7 gives an exact description of A(Gamma), an exact formula and an error bound for pairs, a union bound, a lacunary sufficient condition and forcing lemmas. It gives no closed formula for mu(A(Gamma)) with three or more rank differences, and no proof that A is empty for real components in general. Emptiness for real components is computed only for the 7 core components.
- Proposition 2(c) needs the slot at every rank of a long interval. Real pieces are not shift-invariant, so a Beatty rule that fails Lemma C can still work for special phases on a real piece. I did not search over (tau, theta) jointly for that case.
- R2s multiplicity on one pair, and the other H7 families, were not attempted on this route.

## Missing estimate

To get bounded M for P from Theorem 4, one structural statement is missing. One needs a partition of each weighted M-core component into tau-admissible pieces such that, in some order, every piece sees fewer than M distinct forbidden arcs, or arcs that cluster with a circular gap above 1/M. Theorem 7(e) and C1 show that the pieces cannot be whole components. C4 shows that on G_512 the pieces I tried must have at most 7 labels. So the quotient is almost the original problem, and the mechanism is still local. Proposition 5 places every certified method inside one question: does the M-core have a circular solution phi with ||phi_u - phi_r - q/M|| >= 1/M? For a uniform-in-h result, one would need to build such a phi structurally, for example piecewise affine along Hilbert sub-blocks with slopes tied to the forcing rank differences. Alternatively, one needs a reason why the exact non-certified crossings of Theorem 4(b) cluster.

## Next steps

- Audit Theorem 4, Proposition 5 and Theorem 7. Each proof is a few lines. Record C1 in the ledger as exact and P-only: no single tau is phase-free on any 3-core component of G_512 or G_1024 at M = 3.
- Test whether the cap threshold in C4 comes from tau or from the partition. Re-run phase_sat.py on G_512 at cap 10 with tau_P taken as a grid point or as the longest-arc endpoint, and with pieces taken as Hilbert sub-blocks (contiguous rank intervals) instead of BFS balls. Only Hilbert-block pieces could give a statement that is uniform in h.
- Look for a circular solution phi of the G_512 core that is piecewise affine on Hilbert sub-blocks of one fixed size. Fit slopes to the forcing rank differences (d = 9, 10 in C3) and solve for the block phases. This is the certified route of Proposition 5 with structure.
- Classify forcing pairs in the real P graph. Theorem 7(e) at M = 3 says that gaps q and q' with |q - q'| <= 4, different residues mod 3, and a common rank difference force the slope tau. Use T1 and the drift bound L2 to estimate how often such pairs share a component: the odd family q = O (k = e' = 1) supplies them at every scale.
- Split the G_1024 checks into smaller runs: kill sets per component without the neighbourhood test, and phase_sat.py per component. Each run must stay under 60 s.

