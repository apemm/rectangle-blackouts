# One limit graph for all diagonal graphs

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Not audited yet.

# Result

## Status

partial

## Summary

Questions (a) and (b) reduce to one countable graph Γ: the rationals with odd denominator, x ~ y iff 20(x−y)² ± 4(x−y) + 1 is a rational square. sup over all h and T of chi(G_T(h)) equals chi(Γ). Each chi_∞(T) := chi(Cay(Z, D_T^∞)) is finite and is reached by G_T(h) for large h. If chi(Γ) = C < ∞, the linear total holds: sum_T chi(G_T(h)) ≤ C(h−1). If chi(Γ) = ∞, the answer to (a) is yes. Bounds on chi(Γ): at least 5 by hand, at least 7 by computer. Whether chi(Γ) is finite is open. No lower bound beyond 2h/3 is proved for general h.

## Statements

NOTATION. As in the setting. For odd T: Q(T,d) = 20d² + 4Td + T². S_T^∞ = { d ≠ 0 : Q(T,d) is a square }. L(d) = sqrt Q(T,d). D_T^∞ = { |d| : d ∈ S_T^∞ }. chi_∞(T) = chi(Cay(Z, D_T^∞)). G_T(h) is the graph of the target: vertices I_T(h), edges at distances in D_T(h) = { |d| : d ∈ S_T^∞, L(d) < h, |d| < n_T }. Z_odd = rationals with odd denominator. N(p,q) = p² − pq − q². R_odd = { pq/(2N(p,q)) : p, q coprime integers, pq even }. Γ = graph on Z_odd with x ~ y iff x − y ∈ R_odd ∪ (−R_odd).

PROVED (complete proofs below, each re-read line by line; no independent audit).

(L1) Parametrization. Let r ∈ Q, r ≠ 0. Then 20r² + 4r + 1 is a rational square iff r = pq/(2N) for coprime p, q with pq ≠ 0, N = N(p,q). In that case sqrt(20r² + 4r + 1) = (p² + q²)/|N|. N is odd and coprime to pq. r has odd denominator iff pq is even, and then its reduced denominator is |N|.
Consequence for odd T: d ∈ S_T^∞ iff d = (T/N)·(pq/2) for coprime p, q with pq even and N | T. Then L(d) = |T|(p² + q²)/|N|. Each d comes from exactly the four pairs ±(p,q), ±(−q,p). So Γ is the graph of the conditions 20r² ± 4r + 1 ∈ Q² on Z_odd.

(L2) Inert primes and 5 are inert for the graph. A primitive value N(p,q) (gcd(p,q) = 1) has no prime factor ℓ ≡ ±2 mod 5, and 25 does not divide it. Put T* = sign(T)·5^{min(1, v_5(T))}·∏_{ℓ ≡ ±1 (5)} ℓ^{v_ℓ(T)}. Then S_T^∞ = (T/T*)·S_{T*}^∞, with L scaled by the factor T/T*, and chi_∞(T) = chi_∞(T*) = chi_∞(−T). Also chi_∞(cT) ≥ chi_∞(T) for every odd c.

(L3) Lacunary structure and finiteness. For each odd T, D_T^∞ is the union of a finite set and finitely many sets, each the set of terms of an increasing sequence of positive integers with ratio at least 2 between consecutive terms. Hence chi_∞(T) < ∞. An explicit crude bound is chi_∞(T) ≤ P·27^{2|F_T|}, with F_T the finite set of orbit representatives in the proof and P a prime above the finite exceptional set.

(T1) Limits per diagonal. For fixed odd T, chi(G_T(h)) is nondecreasing in h. It equals chi_∞(T) for all h ≥ h_1(T).

(T2) One graph for all diagonals. sup_T chi_∞(T) = chi(Γ), in N ∪ {∞}. The function M(h) = max over the diagonals T at height h of chi(G_T(h)) is nondecreasing, and lim_{h→∞} M(h) = chi(Γ). Consequences:
 (i) If chi(Γ) = C < ∞, then for every h, sum_T chi(G_T(h)) ≤ C(h−1). The labels then split into at most C(h−1) constant-offset classes, each monotone of slope 1, P-free and without right angles (Proposition 1 of the 12 November note). The missing estimate (E) then holds in its strongest form, chi(G_T) ≤ C.
 (ii) If chi(Γ) = ∞, then sup_T chi(G_T(h)) → ∞, which answers (a) yes. This alone does not decide (b).
 So question (a) is equivalent to chi(Γ) = ∞.

(T3) Lower bounds.
 (a) Γ contains K_5: {0, 35, 209, 260, 434}/1045 (hand-checkable, square roots listed below). So chi(Γ) ≥ 5, and chi(G_1045(h)) ≥ 5 for h ≥ 1746 (all ten L-values are at most 1745, and n_T ≥ 435 at those heights).
 (b) sum_T chi(G_T(h)) ≥ (h − 1) + #{odd T : |T| < h/5} + #{odd T ≡ 0 mod 5 : |T| < h/5} = 1.24h − O(1). This holds because d = T gives L = 5|T|, and for T = 5t the distances |t|, 5|t|, 6|t| form a triangle with L ≤ 5|T|.

COMPUTED (SAT, two solvers agree, no proof log).
 (C1) chi(Cay([0,54), D_55^∞)) ≥ 6, so chi_∞(55) ≥ 6 and chi(G_55(h)) ≥ 6 for h ≥ 206.
 (C2) chi(Cay([0,700), D_1045^∞)) ≥ 7, so chi(Γ) ≥ 7, chi(G_1045(h)) ≥ 7 for h ≥ 3356, and M(3356) ≥ 7. By L2, chi(G_T(h)) ≥ 7 for every multiple T of 1045 with |T| < about 0.31h.
 (C3) The 25-vertex set listed below is a clique of the monotone-or-P constraint graph at h = 32, checked from the definition by a separate script. So at least 25 > 2h/3 classes are needed at h = 32. This is a finite-h fact only.

NOT PROVED: whether chi(Γ) is finite; whether sum_T chi(G_T)/h is bounded; any lower bound c·h with c > 2/3 for monotone P-free partitions for all large h; any lower bound of order k_T/log h for chi(G_T).

## Proofs

[1] PROOF OF L1. Let r ≠ 0 and put u = (1 + 2r)/(4r). Then 20r² + 4r + 1 = (1 + 2r)² + (4r)² = (4r)²(1 + u²), so the left side is a rational square iff 1 + u² is.
If 1 + u² = v² with v ∈ Q, then (v + u)(v − u) = 1. Put m = v + u ≠ 0; then v − u = 1/m and u = (m − 1/m)/2. Conversely, 1 + ((m − 1/m)/2)² = ((m + 1/m)/2)².
From 4ru = 1 + 2r we get r(4u − 2) = 1, so r = 1/(4u − 2) = 1/(2m − 2/m − 2) = m/(2(m² − m − 1)). Conversely, for m ∈ Q*, m² − m − 1 ≠ 0 because sqrt 5 is irrational. Then r := m/(2(m² − m − 1)) is nonzero, 1/r + 2 = 2(m² − 1)/m, and u = (1/r + 2)/4 = (m − 1/m)/2.
With m = p/q in lowest terms (p, q ≠ 0) this is r = pq/(2N). Also sqrt = 4|r|·|m + 1/m|/2 = 2|r|·(p² + q²)/|pq| = (p² + q²)/|N|.
N is odd: if p and q are both odd, N ≡ 1 − 1 − 1 (mod 2); if exactly one is even, N ≡ 1. A prime dividing p and N divides q², which is impossible; the same holds for q. So gcd(pq, N) = 1.
If pq is odd, then gcd(pq, 2N) = 1 and the reduced denominator 2|N| is even. If pq is even, then r = (pq/2)/N with gcd(pq/2, N) = 1, and the denominator is |N|, which is odd.
For odd T and d ≠ 0 put r = d/T. Then Q(T,d) = T²(20r² + 4r + 1), and an integer that is a rational square is an integer square. So d ∈ S_T^∞ iff r = pq/(2N) as above. Since the reduced denominator of d/T divides the odd number T, pq is even and |N| divides T. Conversely, if N | T and pq is even, then d = (T/N)(pq/2) is a nonzero integer and Q(T,d) = T²(p² + q²)²/N².
The map m ↦ u is 2-to-1 (m and −1/m), so each r comes from ±(p,q) and ±(−q,p).
In Γ, x − y ∈ −R_odd means the condition with −r, that is, 20r² − 4r + 1 ∈ Q². []

[2] PROOF OF L2. We have 4N = (2p − q)² − 5q².
Let ℓ ≠ 5 be an odd prime dividing N. If ℓ | q, then ℓ | (2p − q)², so ℓ | p, which contradicts coprimality. So 5 ≡ ((2p − q)/q)² mod ℓ, and by reciprocity (5/ℓ) = (ℓ/5) = 1, that is, ℓ ≡ ±1 mod 5.
Let 5 | N. Then 5 | 2p − q, say 2p − q = 5a, and 4N = 5(5a² − q²). Here 5 does not divide q, since otherwise 5 | 2p and 5 | p. So v_5(N) = 1.
Hence N | T iff N | T*. Write c = T/T* (a positive odd integer, since T* has the sign of T). Then d = (T/N)(pq/2) = c·(T*/N)(pq/2), so S_T^∞ = c·S_{T*}^∞ and L_T(cd') = c·L_{T*}(d').
Cay(Z, cD) is the disjoint union of c copies of Cay(Z, D), one on each coset of cZ, so it has the same chromatic number. S_{−T}^∞ = −S_T^∞ because Q(−T,−d) = Q(T,d). Finally, S_{cT}^∞ ⊇ c·S_T^∞ because Q(cT, cd) = c²Q(T,d). []

[3] PROOF OF L3.
(3.1) The ring. Z[φ] = { (a + b·sqrt5)/2 : a ≡ b mod 2 }, with norm N(β) = ββ'.
For d ∈ S_T^∞ put X = 10d + T and L = L(d) > 0. Then X² − 5L² = (10d + T)² − 5(20d² + 4Td + T²) = −4T². X is odd because T is, and L is odd because L² ≡ T² mod 2. So β_d := (X + L·sqrt5)/2 ∈ Z[φ], N(β_d) = −T², and d = (Tr β_d − T)/10. The map d ↦ β_d is injective.
(3.2) Finitely many orbits. Let ββ' = −T². Choose k with |βφ^(−2k)| ∈ [|T|, |T|φ²), and put γ = βφ^(−2k). Since N(φ²) = 1 and φ' = −1/φ, we get γγ' = −T² and |γ'| ∈ (|T|/φ², |T|]. The image of Z[φ] under β ↦ (β, β') is a lattice in R², so only finitely many γ lie in this bounded box. Call this finite set F_T (it includes both signs). Every β of norm −T² is γφ^(2k) with γ ∈ F_T and k ∈ Z.
(3.3) Ratios. For γ ∈ F_T put a_k = |γφ^(2k) + γ'φ^(−2k) − T|/10. Then a_k = |γ|φ^(2k)/10 + O(1) as k → +∞, and a_k = |γ'|φ^(−2k)/10 + O(1) as k → −∞. Since φ² > 2.6, there is k_γ with a_{k+1} ≥ 2a_k > 0 for k ≥ k_γ, and likewise at −∞.
So D_T^∞ ⊆ F ∪ ∪_γ (E_γ^+ ∪ E_γ^−), where F is finite and each E is the set of terms a_k (over the k in a tail for which d is an integer in S_T^∞). A subsequence of a sequence with ratio at least 2 still has ratio at least 2.
(3.4) Colouring lemma. Let e_1 < e_2 < ... be positive integers with e_{n+1} ≥ 6e_n.
Put J_1 = [1/(3e_1), 2/(3e_1)]. Given J_n = [x, x + 1/(3e_n)], let b = ⌈x·e_{n+1} − 1/3⌉. Then J_{n+1} := [(b + 1/3)/e_{n+1}, (b + 2/3)/e_{n+1}] starts in [x, x + 1/e_{n+1}) and ends before x + 4/(3e_{n+1}) ≤ x + 1/(3e_n). So J_{n+1} ⊆ J_n.
Take θ in the intersection of the J_n. Then ||θe_n|| ≥ 1/3 for every n. The colouring x ↦ ⌊3·frac(θx)⌋ is proper: if two integers get the same colour, their difference δ has ||θδ|| < 1/3.
A sequence with ratio at least 2 splits into three subsequences e_{3n+r}, each with ratio at least 8, so its Cayley graph has chi ≤ 27. For the finite set F, colour x by x mod P for a prime P > max F; this gives at most P colours.
The product colouring is proper for a union of distance sets, so chi_∞(T) ≤ P·27^(2|F_T|). []

[4] PROOF OF T1. I_T(h) = [max(0, −s), min(A, K − s)). The left end does not depend on h, and the right end is nondecreasing because A and K are. D_T(h) ⊆ D_T(h+1). So G_T(h) is a spanning subgraph of an induced subgraph of G_T(h+1), which gives monotonicity. It also gives G_T(h) ⊆ Cay(Z, D_T^∞), so chi(G_T(h)) ≤ chi_∞(T) < ∞ by L3.
By the de Bruijn–Erdős theorem (for countable graphs this is a König's-lemma compactness argument), some finite subgraph W of Cay(Z, D_T^∞) has chi(W) = chi_∞(T). After translation W lies in an interval of length ℓ and uses distances with L-values below some H. Since n_T(h) → ∞ as h → ∞, for all h with h > H and n_T(h) > ℓ the graph G_T(h) contains a translate of W. []

[5] PROOF OF T2. For odd T define ι_T(i) = i/T, from Z to (1/T)Z. Then |i − i'| ∈ D_T^∞ iff ±(i − i') ∈ S_T^∞, iff 20r² ± 4r + 1 ∈ Q² with r = (i − i')/T (by L1), iff ι_T(i) ~ ι_T(i') in Γ. So Cay(Z, D_T^∞) ≅ Γ[(1/T)Z], and chi_∞(T) ≤ chi(Γ).
Every finite subgraph of Γ lies in (1/T)Z for T the lcm of its denominators, which is odd. So every finite subgraph has chi ≤ sup_T chi_∞(T). By de Bruijn–Erdős, chi(Γ) ≤ sup_T chi_∞(T).
M(h) is nondecreasing: every diagonal at height h is a diagonal at height h + 1, and T1 applies. Its limit is sup_T chi_∞(T) by T1.
Part (i): there are h − 1 diagonals, each with chi ≤ chi(Γ). Part (ii) is immediate. []

[6] PROOF OF T3.
(a) With T = 1045, the ten differences and their L-values are: d = −35 (L = 985), −209 (1045), −260 (1165), −434 (1745), −174 (985), +225 (1745), −399 (1615), +51 (1165). Here 225 occurs twice and 174 occurs twice. Example check: Q(1045, −35) = 24500 − 146300 + 1092025 = 970225 = 985². So the five points are pairwise adjacent.
(b) For T odd with 0 < |T| < h/5: Q(T,T) = 25T², so L = 5|T| < h. Also n_T > |T|: for T > 0, n_T = K − (T−1)/2 ≥ 0.4h − 1/2; for T < 0, n_T = A − (|T|+1)/2 ≥ 0.4h − 1/2. So G_T(h) has an edge.
For T = 5t: Q(T,−t) = 25t², Q(T,5t) = 625t² and Q(T,−6t) = 625t², so all three L-values are at most 5|T| < h. Also 6|t| < n_T. The triangle 0, |t|, 6|t| has differences |t|, 6|t|, 5|t|, so chi ≥ 3.
There are h − 1 diagonals, about h/5 odd T with |T| < h/5, and about h/25 of those are divisible by 5. []

[7] STRUCTURE THAT MATTERS FOR (E) (proved by L1, L2). At height h, D_T(h) = { |T||pq|/(2|N|) : N | T*, pq even, gcd(p,q) = 1, (p² + q²)/|N| < h/|T|, |T||pq|/(2|N|) < n_T }.
The ratio (p² + q²)/|N| is at least 2/sqrt5, because N has eigenvalues ±sqrt5/2. For |T| ≍ h, only pairs (p:q) in a bounded window count, about one element per ideal of norm T*². So k_T ≍ number of such ideals, about 3^(number of split primes of T). For |T| = o(h), each orbit contributes about log(h/|T|)/(2 log φ) elements. That is where lacunarity (L3) helps, but it does not help in the regime |T| ≍ h, which carries most of sum k_T. So L3 does not give (E). It gives only boundedness for each fixed T.

[8] ON (c), WHY 2h/3 IS WHERE THE PIVOT CLIQUE STOPS (heuristic, not a theorem). Let X be the full column i_0 (K labels) and Y the labels whose even point sees the odd point of slot i_0. Every vertex of Y is adjacent to every vertex of X. So chi(H) ≥ K + chi(H[Y]) (proved: no colour class meets both).
In coordinates Δ = i − i_0, y = 2(j − i_0) + 1, Y is the set of points (±g(s² − t²)/8, ±gst) on rays through the origin, with g, s, t odd. An antichain uses distinct j-levels and must follow a monotone path. Points on one ray of negative slope form an antichain, but a monotone path cannot interleave two rays at one scale. So the densest choice is the ray s/t = 3 (density 1/3 of the j-levels), which gives K + K/3 = 2h/3.
The clique of size 25 at h = 32: slot 0: j = 12, 15; slot 2: 7, 9; slot 4: 6; slot 5: 7..15; slot 7: 4, 5, 6; slot 8: 2, 5; slot 10: 4; slot 11: 3; slot 13: 2, 3; slot 15: 0, 1. It uses small Pythagorean triples that thin out as h grows, so I do not expect it to give a constant above 2/3.
Fractional bounds |S|/α(S) also failed to beat K in rough estimates: diagonals with D_T empty already give monotone P-free classes of size about 0.4h.

[9] HEURISTIC FOR WHERE THE ANSWERS LIE (not a theorem). For |T| ≍ h with w split primes, D_T(h) has about 3^w elements with no evident additive structure. A random Cayley graph on an interval of length n with k generators has chi ≍ k/log n once k ≫ log n. Diagonals with 3^w ≫ log h exist (T < h with w ≍ log h/log log h), so I expect chi(Γ) = ∞, that is, (a) yes. They are rare, so I also expect (b) no, which is the linear total, consistent with (E).
The ratio (Hoffman-type) bound computed by the earlier run grows by about 1 per prime factor (T = 5: 3.64, 55: 4.88, 1045: 5.74). These limit sets are unions of lacunary orbits, so that growth says nothing about the regime |T| ≍ h.

## External results used

- N. G. de Bruijn and P. Erdős, A colour problem for infinite graphs and a problem in the theory of relations, Indag. Math. 13 (1951), 369–373: a graph is k-colourable if every finite subgraph is. Used in T1 and T2. For countable graphs this is a König's-lemma argument.
- Quadratic reciprocity, (5/ℓ) = (ℓ/5) for odd primes ℓ ≠ 5. Used in L2.
- Repository: Proposition 1 of research_archive/2026-11-12/arc_classes_monotone_partition.md (subsets of a diagonal are monotone with slope 1 and have no right angle; P-free iff independent in G_T). Used only to read T2(i) as a statement about classes.
- Repository, for comparison only: ledger T22 (crt_chain_cayley_equivalence.md, the analogous Cayley graph on 2Z_odd with 25w² ± 6w + 1, open) and T31 (odd Pythagorean graph unbounded, via Frantzikinakis, Klurman and Moreira). T31 does not transfer to Γ: its graph varies T with the vertex, and its condition is homogeneous.

## Checks

All scripts are in scripts_graph_limits/. Each runs with py in under 60 s. None failed.
(1) v1_param.py checks the parametrization L1 (d = (T/N)pq/2 with N | T, L = |T|(p² + q²)/|N|) against brute force for 21 values of T, including negative T and T = 605, 1045, 2255, for |d| ≤ 600. There were 0 mismatches, and the L-values agree.
(2) v2_chi.py: T = 55, 54 vertices, 9 distances: not 5-colourable (CaDiCaL and Glucose). T = 1045, 700 vertices, 24 distances: not 6-colourable (both solvers, 10 to 15 s), with the K5 colours fixed.
(3) v4_witness.py lists the K5 L-values (all squares) and the least heights where the witnesses fit: h = 206 for T = 55 and h = 3356 for T = 1045.
(4) v5_clique32.py checks from the definition that the 25 listed labels at h = 32 are pairwise in conflict (0 non-adjacent pairs).
(5) v3_typical.py gives chi(G_T(h)) at h = 2|T|: T = 11: 3; 55: 4; 209: 5; 6061: at least 5; 1045: at least 6. At h = 3|T| for 209: 5; at h = 4|T| for 55: 6. (The run labelled 121771 is not a product of split primes. It used a mistyped T and has no bearing on the questions.)
From an earlier log (not rerun): clique numbers of the constraint graph 6, 8, 13, 16, 18, 22, 25 at h = 8, 12, ..., 32; M(256) = 6; the sum-chi data quoted in gaps.

## Gaps

- The main question stays open: whether the chromatic number of the graph Γ on the odd-denominator rationals is finite. T2 shows that (a) is equivalent to chi(Γ) = ∞, and that a finite chi(Γ) gives the linear total, but neither side is proved.
- (b) is not settled. The only proved lower bound is sum_T chi(G_T(h)) ≥ 1.24h − O(1), and the only proved upper bound is the earlier O(h log h / log log h) (the local sparsity bound, itself under audit).
- (c) is not settled. No lower bound c·h with c > 2/3 is proved for large h. The 25-clique at h = 32 is a finite computation, and section [8] of the proof (why pivot cliques stop at 2h/3) is a heuristic.
- No lower bound of order k_T/log h is proved for chi(G_T) on rich diagonals, so the sharpness of (E) is open.
- chi(Γ) ≥ 7 and chi_∞(55) ≥ 6 rest on SAT runs (CaDiCaL 1.5.3 and Glucose 4 via pysat agree, with valid clique-colour symmetry breaking) without a DRAT proof log. Only chi(Γ) ≥ 5 is hand-checkable.
- The values M(256) = 6 and sum_T chi(G_T(h))/h = 1.59, 1.66, 1.84, 1.88 at h = 32, 64, 128, 256 come from an earlier script s10_sumchi.py and were not rerun here.
- Cited without re-proof: the de Bruijn–Erdős compactness theorem (Indag. Math. 13 (1951) 369–373; for countable graphs, König's lemma) and quadratic reciprocity for (5/ℓ). Everything else in L1 to L3, T1 to T3 is proved in full above, re-read once by me, with no independent audit.
- The bound in L3 (chi_∞(T) ≤ P·27^(2|F_T|)) is very crude. A Peres–Schlag bound would give O(J log J) for J orbits, which is still useless in the regime |T| ≍ h.

## Missing estimate

Decide whether chi(Γ) < ∞, where Γ is the graph on Z_odd with x ~ y iff x − y = ±pq/(2(p² − pq − q²)) for coprime p, q with pq even. A finite colouring would give sum_T chi(G_T(h)) ≤ chi(Γ)(h−1) for every h, which is the linear total and more than (E). An infinite chromatic number answers (a) yes. In that case (b) needs the finer estimate (E), restricted to the height window (p² + q²)/|N| < h/|T|.

## Next steps

- Have L1, L2, L3 and T1, T2 audited by hand. They are short and elementary, and they change how question (a) is posed.
- Attack chi(Γ) directly. To refute any Bohr-type (arc-product) colouring, try to show that R_odd meets every Bohr neighbourhood of 0 in Z_odd. Watch the adversarial adelic characters built from sqrt5 at split primes: the family (p,q) = (1,q) is near 0 for them, so the two-parameter family must be used.
- Compare Γ with the T22 graph (25w² ± 6w + 1 on 2Z_odd). Both are of the form Cay(Z_odd, {1/(4u − c) : 1 + u² ∈ Q²}), with c = 2 here and c = 3 there, scaled differently. A method for one likely transfers. They are not related by a scaling (u ↦ affine maps do not preserve {1 + u² square}).
- In the regime |T| ≍ h, test whether chi(G_T(h)) grows with the number w of split primes. Use T = 11, 209, 6061, 187891 with h = 2T (for 6061, chi ≥ 5 is known; 5 colours timed out in a 6 s solver run). If chi grows linearly in w, then (b) is false (sum about h log log h), which would redirect the project.
- Produce DRAT certificates for chi_∞(55) ≥ 6 (54 vertices) and chi_∞(1045) ≥ 7 (700 vertices) so that chi(Γ) ≥ 7 can be cited.
- For (c), replace cliques by a weighted (fractional) argument that uses P-conflicts inside Y = common neighbourhood of a column. The join bound chi ≥ K + chi(H[Y]) is proved, but width(Y) alone stops at h/6.

