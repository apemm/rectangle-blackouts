# Census of the Hilbert P candidate graph

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (computational): for h up to 16384, S from 32 to 256 and M from 1 to 3, the weighted degeneracy of the in-strip P candidate graph is exactly 2 in every nonempty case, so three choices exclude in-strip P everywhere tested, and the new h = 8192 certificates pass an independent check. Increasing-rank greedy fails at S = 32 for h >= 2048. Mean incidence fits (1/S)(a_M + b_M ln(h/S^2)) with b_1 = 2.573, close to the heuristic 8/pi. P only, not full boards.

# Result

## Status

partial

## Summary

Measured the P candidate graph for all requested (h, S, M) plus four h = 16384 cases. Weighted degeneracy is exactly 2 in every nonempty case, so three choices exclude in-strip P everywhere tested; the new h = 8192 certificates also pass an independent check. Increasing-rank greedy fails at S = 32 for h >= 2048, and at every ratio rho = h/S^2 >= 2. Mean incidence follows (1/S)(a_M + b_M ln rho), with b_1 = 2.573 against a heuristic 8/pi = 2.546. Every rho <= 1 case is trivial by a short parity lemma, so only five (h, S) points bear on constant S. Nothing toward m_h = O(h^2) is proved.

## Statements

Proved short claims (the proofs are in the proof field):

(T1) Band completeness. In the placement x_e = S(M r_e + xi_e), take any candidate pair (r, r+d) and either cross-parity role. Its earlier label satisfies |T_r - (+-Y - 1)/2| <= zmax(d), where T = j - i, Y is the absolute row gap, and zmax(d) = isqrt(16d - 1). So restricting the search to these diagonal bands loses no constraint.

(T2) Curve identity. The low-bit rotation algorithm used in the archive verifier gives exactly the recursive Hilbert order (2) of the placement note, for every power of two q.

(T3) Parity reduction. Let S = 2^e, M >= 2, and h <= S^2 + 1. Choose xi_e in {0, 1} with xi_e = M r_e (mod 2). Then no opposite-parity pair of label points has integral distance L <= h - 1, so the whole P family is empty. This holds for any retained subset of labels, in or out of the strip. With xi = 0 it is the archive's 2-adic zero lemma: the graph is empty for every M when h <= S^2/4 + 1.

(T4) Edge decomposition. The candidate system for M is the disjoint union, over slot gaps q' <= (h-1)/S and over d in D_M(q') = {floor(q'/M), ceil(q'/M)} \ {0}, of the pairs (r, r+d) with a P witness at X = S q'. Each such pair carries delta = q' - M d. So E_M <= 2 sum_{q'} max_d H(q', d).

(T5) Round peeling. Each round deletes every vertex of current weighted degree < M. If this empties the multigraph, assigning vertices in reverse round order, one at a time within a round, never runs out of choices.

Finite results, exact integer arithmetic, P family only, in-strip vertical completion only:

(C1) For (h, S) in {(4096, 32), (8192, 32), (8192, 64), (8192, 128), (16384, 64), (16384, 128)}, three choices exclude every in-strip opposite-parity P constraint. The certificates for h = 8192 also pass an independent full-scan verifier based on Euclid's parametrization. The h = 16384 certificates are checked only against the generated constraint list.

(C2) For every nonempty case measured (M = 1, 2, 3; S = 32, 64, 128; h = 1024 to 16384), the weighted degeneracy is exactly 2 and the 3-core is empty. For M = 1 this holds only once the graph contains a cycle; otherwise the degeneracy is 1.

These say nothing about mixed supports, cross-parity right angles, or the sea and collars.

## Proofs

SETUP. These are the conventions of hilbert_finite_choice_search.py. Ranks r < s, d = s - r, slot gap q' = M d + delta with |delta| <= M - 1, and X = S q' < h. A constraint (r, s, delta) forbids xi_s - xi_r = delta. A pair is included when one of its two cross-parity pairs, odd(r) with even(s) or even(r) with odd(s), has X^2 + Y^2 = L^2 with L <= h - 1. Its completion rows (y1 + y2 -+ L)/2 must also lie in [1, h]. Triples are enumerated from ab = (X/2)^2 with a, b of opposite parity, so a = (L - Y)/2 is the smaller half-factor. For h a power of two, A = K = q = h/2, so there is no padding and all q^2 labels are present.

T1. Write T_r = j_r - i_r. In role 1, the row difference is even(s) - odd(r) = 2 j_s - 2 i_r + 1 = 2 T_r + 1 + 2z, with z = j_s - j_r. In role 2, odd(s) - even(r) = -(2 T_r + 1) + 2z', with z' = i_s - i_r. By (1) of the placement note, z^2, z'^2 < 16 d, so |z|, |z'| <= isqrt(16d - 1) = zmax. If |row difference| = Y, then in role 1, T_r = (+-Y - 1)/2 - z. In role 2, T_r = (-+Y - 1)/2 + z'. Either way T_r lies in [c - zmax, c + zmax] for c = (Y - 1)/2 or (-Y - 1)/2, both integers because Y is odd. QED.

T2. At each level s = 1, 2, 4, ..., the algorithm reads the base-4 digit t of the rank. Digit 0 gives quadrant (0, 0) and swaps x and y, which transposes the subsquare. Digit 1 gives (0, s) with no rotation. Digit 2 gives (s, s) with no rotation. Digit 3 maps (x, y) to (s - 1 - y, s - 1 - x) and then adds (s, 0), giving (2s - 1 - y, s - 1 - x). These are the four maps of recursion (2), applied to the sub-curve of the lower digits. Induction on the number of digits gives identity for all q. As a check, both curves agree, and xy2d inverts d2xy, exhaustively for q <= 1024 (test_pgraph.py).

T3. Every slot position p_e = M r_e + xi_e is even, so X = S|p_e - p_f| is divisible by 2S = 2^{e+1}. For an opposite-parity pair, Y is odd, so L is odd. Then a + b = L is odd, so exactly one of a, b is odd. The odd one has no factor of 2, so the even one is divisible by 2^{v2(X^2/4)}, and v2(X^2/4) = 2 v2(X) - 2 >= 2e. So the even half-factor is at least S^2, and L >= S^2 + 1 > h - 1. With xi = 0 the same argument for 2^e | X gives L >= S^2/4 + 1. QED. Consequence: every census point with rho = h/S^2 <= 1 says nothing about the constant-S question. This explains every M = 2 greedy success. When all deltas are odd (q' is odd, as here), the smallest-value greedy always picks 0.

T4. This is immediate from |M d - q'| <= M - 1 with d >= 1. Distinct (q', d) give distinct (d, delta), so there is no double counting.

T5. Let x be removed in round k. Every vertex assigned before x was alive at the start of round k: it is either from a later round or earlier in round k. So the constraints from x to assigned vertices are among x's at most deg_k(x) < M constraints in the multigraph alive at that time. Each forbids at most one value, so one of the M values remains free. QED. certify.py asserts this, and then asserts zero violations.

CROSS-CHECKS OF THE COMPUTATION.
- Band method against the archive's brute full scan, comparing exact witness sets: identical at 9 settings up to (h, S, M) = (2048, 32, 3), including non-powers of two such as h = 777 and 1500.
- Archive values reproduced:
  - h = 2048, M = 3: 139237 constraints, 171851 incident labels, maximum incidence 8, degeneracy 2.
  - h = 4096, M = 3: 695871 constraints, 877697 incident labels, maximum incidence 8, degeneracy 2.
  - M = 1: 94222 and 481323 edges, equal to the archive's unjittered P graph.
  - The archive triangle 1331100, 1331133, 1331166 at h = 4096 is present, with factors 99, 363, 99. These match (2915 - 2717)/2 and (3435 - 2709)/2.
- Splitting the rank-gap range and merging was checked equal to a single run.
- The independent verifier rejects an all-zero assignment at h = 4096 (negative control). It passes the h = 4096 certificate and all three h = 8192, M = 3 certificates:
  - S = 128: 7.0e8 pair checks.
  - S = 64: 1.4e9 pair checks.
  - S = 32: 2.78e9 pair checks, run in three gap ranges because of the 60-second limit.
- No constraint has more than one witness.
- The lemma b^- <= 4 F^- holds at every vertex in every case. The observed maximum of b^-/F^- is 2 for M >= 2 and 1 for M = 1, so the factor 4 is never reached.

MEASUREMENTS. Mean incidence is 2|E|/(number of labels), with constraints counted with multiplicity. Max inc is the maximum weighted degree. F (F^-) is the number of distinct smaller half-factors over all (earlier) constraints at a label. The 2-core column gives the weighted 2-core's vertex count and fraction of all labels. Deg is the weighted degeneracy. Greedy is increasing rank with the smallest admissible value: either OK or the number of stuck labels.

M = 3 (h/S: constraints; incident labels; mean inc; max inc; max F; max F^-; 2-core; deg; greedy):
- 1024/32: 22754; 26929; 0.1736; 5; 2; 2; 4826 (1.84%); 2; OK
- 2048/32: 139237; 171851; 0.2656; 8; 3; 3; 26265 (2.50%); 2; 3 stuck
- 4096/32: 695871; 877697; 0.3318; 8; 4; 3; 116675 (2.78%); 2; 182 stuck
- 8192/32: 3462457; 4352929; 0.4128; 9; 5; 4; 537211 (3.20%); 2; 2421 stuck
- 2048/64: 32798; 40314; 0.0626; 4; 1; 1; 4984 (0.48%); 2; OK
- 4096/64: 189145; 236351; 0.0902; 6; 2; 2; 28635 (0.68%); 2; 8 stuck
- 8192/64: 1142883; 1511799; 0.1362; 6; 3; 3; 140595 (0.84%); 2; 24 stuck
- 16384/64: 5688274; 7733140; 0.1695; 8; 4; 4; 617630 (0.92%); 2; 1182 stuck
- 8192/128: 272625; 350936; 0.0325; 4; 1; 1; 33340 (0.20%); 2; OK
- 16384/128: 1543788; 2078297; 0.0460; 7; 2; 2; 162287 (0.24%); 2; OK

M = 2 (same columns):
- 1024/32: 28173; 30900; 0.2149; 6; 2; 2; 6899; 2; OK
- 2048/32: 163060; 191675; 0.3110; 7; 3; 3; 33295; 2; 1116 stuck
- 4096/32: 827141; 982080; 0.3944; 9; 4; 4; 159552; 2; 9948 stuck
- 8192/32: 4004243; 4743368; 0.4773; 11; 6; 5; 772524; 2; 78729 stuck
- 2048/64: 39305; 45577; 0.0750; 4; 1; 1; 7119; 2; OK
- 4096/64: 234818; 269219; 0.1120; 8; 2; 2; 45377; 2; OK
- 8192/64: 1309083; 1634260; 0.1561; 8; 3; 3; 200030; 2; 4695 stuck
- 8192/128: 326242; 400491; 0.0389; 4; 1; 1; 40726; 2; OK
- 16384/128: 1903304; 2389813; 0.0567; 6; 2; 2; 226055; 2; OK

Every M = 2 success has rho <= 1, where T3 already gives a trivial assignment. At S = 32 and h = 2048, M = 2 is provably unsatisfiable by the archive's five-label obstruction.

M = 1 (this is the actual unjittered graph; greedy fails whenever the graph is nonempty):
- 1024/32: 15851; 0.1209; max inc 4; F 2; 2-core 292; deg 2
- 2048/32: 94222; 0.1797; 5; 4; 1016; 2
- 4096/32: 481323; 0.2295; 6; 4; 3181; 2
- 8192/32: 2417055; 0.2881; 6; 6; 13576; 2
- 2048/64: 21939; 0.0418; 2; 1; 0; 1
- 4096/64: 124720; 0.0595; 4; 2; 0; 1
- 8192/64: 762232; 0.0909; 5; 4; 738; 2
- 8192/128: 172674; 0.0206; 2; 1; 0; 1
- 16384/128: 1007428; 0.0300; 4; 2; 4688; 2

Empty in every M, as forced by T3: S = 64 at h = 1024; S = 128 at h <= 4096; S = 256 at h <= 8192 (and through h = 16385).

More detail for M = 3 at S = 32 (h = 1024, 2048, 4096, 8192):
- Maximum earlier constraints b^-: 3, 4, 6, 6.
- Mean F on incident labels: 1.048, 1.071, 1.114, 1.171.
- Number of distinct factors in the whole graph: 14, 35, 62, 132.
- Largest component: 29, 76, 161, 399.
- Average degree inside the 2-core: 2.32, 2.32, 2.35, 2.40.
- At h = 8192, the label count with F = k for k = 1 to 5 is 3681193, 606623, 59663, 5335, 115.

Induced-average criterion (4) of the report, using U = the 2-core: the average of F^-_U is 0.93 at h = 8192, S = 32, and 0.82 at h = 16384, S = 128. So B(3) >= 0.93, and (4) would need M > 7.4. The criterion cannot certify the three choices that actually work.

FITS. These are least squares over rho >= 1 and are descriptive only.
- S * mean incidence = a_M + b_M ln(h/S^2):
  - M = 1: 3.881 + 2.573 ln rho (7 points, maximum residual 0.15).
  - M = 2: 7.144 + 3.943 ln rho (7 points, maximum residual 0.27).
  - M = 3: 5.846 + 3.581 ln rho (8 points, maximum residual 0.39).
  - At fixed rho the value is S-independent within about 5% (for example 3.87, 3.81, 3.84 at rho = 1 for S = 32, 64, 128). In ln h at S = 32 and M = 3, mean incidence is 0.183 + 0.112 ln(h/1024).
- Heuristic, not proved. Each opposite-parity triple with S | X contributes about 4 nd(q')(h - L)/2 hits, from two roles, two signs, and about (h - L)/2 labels on the matching diagonal after the in-strip trim. Summing over the exactly enumerated triples matches the measured mean within 0.94 to 1.005 in all 28 nonempty cases. With N(l) ~ (l/(pi S)) ln(4l/S^2), from primitive triples l/(2 pi), the 2-adic density 4/S, and odd multiples, the ln rho slope is (8/pi)(2 - P(M | q')). That predicts 2.546 for M = 1, about 3.82 for M = 2, and about 3.40 for M = 3; the observed slopes are 2.573, 3.943, 3.581.
- 2-core fraction: about e^{1.32} S^{-1.52} rho^{0.24} for M = 3 (8 points, maximum log residual 0.08), and e^{1.48} S^{-1.47} rho^{0.25} for M = 2. At fixed h that is about S^{-2.0}; at fixed S, about h^{0.24}. The M = 1 fit is poor (log residual 1.3).
- Maximum F^- depends mainly on rho: 1 at rho = 0.5; 2 at rho = 1; 3 at rho = 2; 3 or 4 at rho = 4; 4 at rho = 8.
- Greedy stuck fraction at S = 32, M = 3: 0, 2.9e-6, 4.3e-5, 1.4e-4.

PREDICTIONS made before the runs (kept in my working notes, not in the archive ledger):
- Mean incidence is proportional to (1/S) ln(h/S^2): the form was confirmed, but my pre-run constant was about twice too large. 8/pi comes from a corrected derivation made after the runs.
- The M-ratio of edge counts is about 2 - 1/M: wrong for M = 3. M = 3 has fewer constraints than M = 2 (ratio 1.45 against 1.72), which T4's nd weighting explains, since multiples of 3 and q' < M get only one d.
- Degeneracy <= 2 at M = 3: confirmed.
- The graph is empty for h <= S^2/4 + 1: confirmed (a theorem).

## Checks

Curve identity: proved for all q, and checked exhaustively for q <= 1024. The band generator matches the archive's brute full scan exactly at 9 settings up to (2048, 32, 3), and reproduces the archive counts at h = 2048 and 4096 (M = 1 and M = 3) and the archive triangle with its factors. The split-gap merge equals a single run. The independent Euclid-parametrization verifier (adapted from the archive one: int32, chunked, skips gaps with no possible triple) passes the h = 4096 and the three h = 8192, M = 3 certificates and rejects an all-zero negative control. certify.py asserts zero violations for all six M = 3 certificates. The fast integer-key version of analyze.py gives the same output as the original on (4096, 32, 3). Every run stayed under 60 seconds and 1 GB; runs that hit the limit were redone in gap-range parts. All Python was run with -B and nothing was imported from the archive, so the rectangle-blackouts repository was not modified.

## Gaps

- No asymptotic statement is proved. Degeneracy 2, and so a three-choice P repair, is verified only for h <= 16384, and only five informative (h, S) points have rho = h/S^2 >= 2: (2048, 32), (4096, 32), (8192, 32), (8192, 64), (16384, 64). All rho <= 1 points are trivial by T3.
- The 2-core grows slowly (about rho^0.24) and its average degree creeps upward (2.32 to 2.40 at S = 32). Nothing excludes a 3-core at larger h. The graph is strongly non-random (a 2-core of about 3% of labels at mean degree 0.41), so random-graph 3-core thresholds cannot be used to extrapolate.
- The fits (slope 8/pi, the M-weights, the 2-core exponents) are heuristic or empirical. The 8/pi derivation assumes a 2-adic density 4/S and per-diagonal hit counts that are not proved.
- The h = 16384 certificates (S = 64, 128) are checked against my generated constraint list, not by the independent full-scan verifier. That verifier would need about 10 runs of 50 seconds each.
- Not run: S = 32 at h = 16384, which needs about 10 split builds and over 17M constraints, beyond the 60-second analysis limit. S = 64 with M = 1, 2 at h = 16384. Any nonempty S = 256 case, which needs h >= 16386 and more than 2.7e8 labels.
- P family only, in-strip completion only. Mixed supports, cross-parity right angles, the sea, collars, and gluing are untouched.
- The observation b^-/F^- <= 2 (the lemma allows 4) is unproved. Even if proved, the vertexwise criterion would need M >= 9 at the observed maximum F^- = 4, so it would not explain why M = 3 works.

## Missing estimate

The P-family question for constant S and M is still open. The census only shows that degeneracy 2 persists through h = 16384, with a slowly growing 2-core. A proof would need a structural reason for an empty 3-core: for example, bounding the cycle structure of the 2-core uniformly in rho, or a direct three-choice rule. The parity lemma T3 shows that the regime h <= S^2 is trivial and costs width at least h^{5/2}, so any useful theorem must handle rho -> infinity at bounded or polylogarithmic S.

## Next steps

- Characterize the weighted 2-core at rho >= 2: classify its cycles (2-cycles from double deltas, triangles like the archive's, longer cycles) by factor pattern, and test whether every 2-core component is a cycle with pendant trees, which would explain degeneracy 2.
- Try to prove b^- <= 2F^- (for a fixed factor at a label, the two cross-parity roles never both occur), which matches every census case.
- Push the S = 32 informative series to h = 16384 (rho = 16) with split builds and a streaming analysis, to test whether the 2-core average degree keeps rising and whether a 3-core appears.
- Run the independent verifier on the h = 16384 certificates in gap-range parts, with odd and even rows cached to disk as int16.

