# Counting the P family of the Hilbert placement

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: an exact Euclid and 2-adic normal form for P vectors at stride S = 2^s (T1), a vector count V(S, h) of order (h/(pi S)) log(4h/S^2) (T2), an averaged mean-degree bound under a random diagonal shift (T3), and monotonicity of the candidate graph along doubling heights (T4). A random-row model that matches every census to within 6% gives mean P degree about (16/(pi S)) log(4h/S^2), so S and M cannot both stay bounded for degeneracy arguments. A conditional theorem gives width h^2 log h under Hypothesis H, which the synthesis note finds inconsistent with the behaviour of near-diagonal labels. Audited in audit_hilbert_p_family_counts.md (correct with fixable gaps).

# Result

## Status

partial

## Summary

The P family does not get cheaper as M grows. Its mean candidate degree is mu ~ (16/(pi S)) log(4h/S^2), so in a model that matches every census to within 6%, S and M can't both stay bounded. The P family alone points to width about h^2 log h (exponent b = 1, below 1.3108), not O(h^2).

## Statements

PROVED (elementary, complete proofs in the proof field):
(T1) Euclid and 2-adic normal form. Let S = 2^s with s >= 2. Positive integers q, odd Y and L satisfy (Sq)^2 + Y^2 = L^2 exactly when there is a unique triple (k, e', O) with k odd, e' >= 1, O odd, gcd(e', O) = 1, and E = S e'/2, such that q = k e' O, Y = k|E^2 - O^2|, L = k(E^2 + O^2). The smaller half-factor is a = k min(E,O)^2 and the larger is b = k max(E,O)^2. Corollaries: L >= k(S^2 e'^2/4 + 1). Since v_2(q) = v_2(e'), a gap q carries a P vector only if 4^{v_2(q)} S^2/4 + 1 <= L < h. Also k < 4h/S^2, and a is odd (O < E) or a multiple of S^2/4 (E < O).
(T2) Vector count. Let V(S,h) be the number of pairs (q, Y) with Y odd, (Sq)^2 + Y^2 = L^2 and L <= h-1. Then V = sum over odd k of P_S((h-1)/k), with P_S(R) <= pi R/(4S) + sqrt(R)/S and P_S(R) = 0 for R < S^2/4 + 1. Hence V(S,h) <= (pi h/(8S))(log(4h/S^2) + 2) + 3h/S^2 for 4 <= S <= sqrt(h), and V = 0 when S^2/4 + 1 > h - 1. The standard asymptotic V = (h/(pi S))(log(4h/S^2) + c_V + o(1)) is confirmed numerically (c_V about 0.71), not re-proved here.
(T3) Averaged degree under a random diagonal shift. Take h a power of two, and place label (i,j) in Hilbert cell (i, j+J) of the side-h square, with J uniform on {0, ..., h/2 - 1}. All archive theorems still hold for every J: the same-parity exclusion, the factor-one theorem, the finite-factor theorem and criteria (4) to (8). The width grows by a factor of 4. The candidate P multigraph C_J (all |delta| <= M-1, L <= h-1) has E_J[mean degree] <= 64 V(S,h)/h <= (8 pi/S)(log(4h/S^2) + 2) + 192/S^2. So some shift has at most that mean degree.
(T4) Monotonicity. For powers of two h, the candidate multigraph at height h embeds as a subgraph of the one at height 2h (identity-oriented third quadrant). Its weighted degeneracy D_{S,M}(h) and B(M) are therefore nondecreasing along doubling.
(T5) Relations between criteria. F^-_U >= b^-_U/4 (uniqueness lemma), and B(M) >= D/8. Greedy reverse peeling succeeds when M > D. Criterion (8), M > 8B, is never weaker than needing M > D/1.
CONDITIONAL THEOREM (answer to target (c)). Assume Hypothesis H(c0,c1): D_{S,M}(h) <= c0 + c1 mu_hat(S,h) for all h, where mu_hat = (16/(pi S))(log(4h/S^2) + 1). Then either of the following excludes every P constraint, with width O(h^2 log h):
(i) S = 32 and M = floor(c0 + c1 mu_hat(32,h)) + 1, which is O(log h).
(ii) S0(h) = the least power of two >= max(32, (16 c1/pi)(log(4h) + 1)) and M0 = floor(c0) + 2.
The data fit c0 about 2 and c1 about 1.2 (15 data points with mu from 0.17 to 2.86). H is unproved.
MODEL-LEVEL CONCLUSIONS (heuristic, not proved): the random-row model gives mu_model = (16/h^2) sum over vectors of sigma_M(q)(h - L), which is about (8 sigma_bar/(pi S))(log(4h/S^2) + O(1)), with sigma_bar in [1,2] and sigma_M(q) = 2 unless M | q. It matches all 10 archived or new counts to within 1% to 6%. Bounded S and M give mu -> infinity. Bounded M needs S growing like (log h)^1. A smaller power of log fails. The cheapest greedy choice is S = 32 with M about 3 + 0.19 log(h/256).

## Proofs

Notation follows the archive: x_e = S(M r_e + xi_e), q = Md + delta, X = Sq, Y = |cross-parity row difference|, a = (L-Y)/2, b = (L+Y)/2, ab = X^2/4. "Slot" means a pair (d, delta) with |Md - q| <= M-1. Each q has sigma_M(q) <= 2 slots: d = floor(q/M) and d = ceil(q/M), and only one slot when M | q.

1. PROOF OF T1 (normal form).
Let k = gcd(X, Y, L) = gcd(X, Y). Because k | Y and Y is odd, k is odd. The triple (X/k, Y/k, L/k) is primitive with Y/k odd. By the standard parametrization there are coprime m > n of opposite parity with X/k = 2mn, Y/k = m^2 - n^2 and L/k = m^2 + n^2.
Because k is odd and 2^s | X, we get 2^{s-1} | mn. Exactly one of m, n is even. Call it E, and call the odd one O. Then 2^{s-1} | E, so E = (S/2)e'. Also gcd(m,n) = 1 implies gcd(e', O) = 1.
So q = X/S = 2kEO/S = k e' O, Y = k|E^2 - O^2| and L = k(E^2 + O^2). The converse is direct algebra. Uniqueness follows from the uniqueness of k = gcd(X,Y) and of the primitive parametrization.
Next, L - Y = k(E^2 + O^2 - |E^2 - O^2|) = 2k min(E,O)^2, which gives a, and b follows the same way. With O >= 1 and E >= S e'/2, L >= k(S^2 e'^2/4 + 1). Also v_2(q) = v_2(e'), because k and O are odd. So L >= 4^{v_2(q)} S^2/4 + 1, and k < 4h/S^2 when L < h. QED.
Consequence for the census: at S = 32 and h <= 4096, a gap q divisible by 4 needs L >= 4097, so it carries nothing. For M = 4, every contributing q therefore has two slots. For M = 3, the single-slot multiples of 3 do contribute. This explains why the archived M = 4 graph at h = 2048 has 24% more constraints than the M = 3 graph, and why the expected count doesn't fall as M grows.

2. PROOF OF T2 (vector count).
By T1 the vectors correspond one to one to triples (k, e', O) with k * l <= h-1, where l = S^2 e'^2/4 + O^2. So V = sum over odd k of P_S((h-1)/k).
Fix e' with S^2 e'^2/4 <= R. The number of odd O <= sqrt(R - S^2 e'^2/4) is at most (sqrt(R - S^2 e'^2/4) + 1)/2. Here 1 <= e' <= 2 sqrt(R)/S, and the square root decreases in e'. So the sum is at most (1/2) times the integral from 0 to 2 sqrt(R)/S, which equals pi R/(4S), plus sqrt(R)/S. So P_S(R) <= pi R/(4S) + sqrt(R)/S, and P_S(R) = 0 if R < S^2/4 + 1.
The k with a nonzero term satisfy k < K := 4h/S^2. Use sum over odd k <= K of 1/k <= 1 + (1/2) log K and sum over odd k <= K of k^{-1/2} <= 1 + sqrt(K). This gives V <= (pi h/(8S))(log K + 2) + sqrt(h)/S + 2h/S^2. The last two terms are at most 3h/S^2 when S <= sqrt(h). QED.
Numerical check (script `model_large_h.py`): V S/h = 0.875, 1.780, 2.656, 3.538, 4.420, 4.861 at S = 32 and h = 2^11, 2^15, 2^19, 2^23, 2^27, 2^29. That fits (1/pi)(log K + 0.71) for large K. The upper bound exceeds the true value by about 1.3 times.

3. THE RANDOM-ROW MODEL, AND THE ANSWER TO TARGET (a)
3a. Model. For each slot and role, replace the cross-parity row pair with the (odd, even) rows of one uniformly random label. Fix a vector (q, Y, L) with Y > 0. The labels with b - a = +Y and a completion inside the strip are those with odd a in [(L-Y+2)/2, (2h-L-Y)/2]. There are about (h-L)/2 of them, and the same number for b - a = -Y. Labels number AK, about h^2/4.
So each slot and role hits with probability about 4(h-L)/h^2. Multiply by 2 roles, 2 sides and sigma_M(q) slots. The expected number of candidate constraints at a label is
 mu_model = (16/h^2) * (sum over vectors of sigma_M(q)(h - L)).
3b. Asymptotics. By T1, the sum over odd k with k*l < h of (h - k l) is about h^2/(4l). The primitive pairs (e', O) with l <= R have density 2R/(pi S): the ellipse area is pi R/(2S), odd O contribute 1/2, and coprimality contributes 8/pi^2. Summing 1/l from S^2/4 to h gives (2/(pi S)) log(4h/S^2). So mu_model is about (8 sigma_bar/(pi S)) log(4h/S^2). With sigma = 2, the exact Euclid sums give mu = (16/(pi S)) log K + 1.10/S. The constant 1.10 is the same at S = 32, 64 and 128, with K = 4h/S^2. This formula is a model prediction, not a theorem.
3c. Validation. Census numbers come from the archive or from my exact recount. The model is computed exactly.
- Unjittered, no strip test (mean incidence): h = 512, 1024, 2048 at S = 32 give a model of 0.1665, 0.2030, 0.2982. The census gives 0.1698, 0.2022, 0.2966. At S = 64, h = 2048, the model gives 0.0833 and the census 0.0816.
- In-strip candidate multigraph, model edges vs counted edges, written as (h, S, M):
 - (2048, 32, 3): 144946 vs 139237
 - (2048, 32, 4): 183172 vs 173065
 - (4096, 32, 3): 720028 vs 695871
 - (1024, 8, 3): 259110 vs 250365
 - (2048, 8, 3): 1198460 vs 1174117
 - (2048, 16, 4): 576326 vs 553118
 Every ratio lies between 0.95 and 1.02.
3d. Answer to (a).
- The expected count per label is about (8 sigma_bar/(pi S))(log(4h/S^2) + O(1)), with sigma_bar in [1,2]. To first order it doesn't depend on M, because the q-range [1, (h-1)/S] is fixed and M only redistributes q among two slots. It decreases like log(h/S^2)/S, and it is 0 for S^2/4 + 1 > h - 1.
- F matches the count closely. In the measured 3-cores, the average F^- is 0.83 and 0.77 of the average b^- (section 6). Repeated factors at one label exist but are not the main source of density.
- Maximum count: the only rigorous bound is the archive's (13), (16 sqrt(W) + 2) D_h with W about h/(SM). Remark (Shiu): Shiu's Brun-Titchmarsh theorem for multiplicative functions (Crelle 313, 1980) applies to nonnegative multiplicative f with f(p^l) <= A^l and f(n) << n^eps. On intervals of length y >= x^beta, it gives sum of f(n) << (y/log x) exp(sum over p <= x of f(p)/p). With f(n) = tau(n^2), it replaces D_h by (log h)^2, which gives M = C (h/S)^{1/3} (log h)^{4/3} unconditionally. I cite this theorem from memory and did not re-read it this session.
- Observed maximum weighted degree: 8 at S = 32 (h = 2048 and 4096), and 15 to 22 at S = 8. The tails are heavier than Poisson. At h = 1024 there are 199 labels of degree 4 against 14.9 expected under Poisson. One clumping mechanism: if the curve moves by the same horizontal vector (Delta i, 0) over the d steps before and after rank r, both partners of r at distance d give the same (q, Y) in the role "odd row of r, even row of the partner". So they hit together, and paths form.

4. PROOF OF T3 (shift average).
The cells (i, j+J) satisfy i < h/2 and j + J <= h - 2, so one Hilbert square of side Q = h serves every J. The ranks of all cells don't depend on J. Label coordinates differ from cell coordinates by the constant (0, J). So locality (1), T = j - i, and every archive argument hold unchanged. The rank span is below h^2 instead of h^2/4.
Fix the earlier rank r with its cell in column u < A (A*Q such ranks), a slot (d, delta) and a role. The signed cross-parity difference equals c - 2J, with c independent of J. It equals +Y or -Y for at most 2 values of J per Y in Y(q). So the number of J for which this triple is a candidate constraint is at most 2 * 2|Y(q)| over the two roles. Summing over slots, with each q in at most 2 slots, gives sum over J of |E_J| <= A Q * 8V.
Divide by N_J = h/2 and convert to mean degree 2|E_J|/(AK) with A = K = h/2 and Q = h. The result is E_J[mu_J] <= 16 Q V/(N_J K) = 64 V/h. Then insert T2. QED.
This bound is about 4 times the model value. It makes the scaling mu = O(log(4h/S^2)/S) rigorous for the shifted placement. A global average alone does not control (8) (archive K_t example).

5. PROOF OF T4 (monotonicity).
Let h be a power of two, so A = K = Q = h/2. At height 2h, the padded side is h, and H_h maps the third quadrant by (x,y) -> (x + Q, y + Q) with rank 2Q^2 + r, in identity orientation. Labels (i + Q, j + Q) exist at height 2h. Their rows shift by 2Q = h.
For any two translated labels, X, Y and L are unchanged, and completion rows shift from [1, h] into [h+1, 2h]. So every candidate constraint at h, together with its witness factor, appears at 2h. Extra constraints can only appear, for example with L in [h, 2h-1]. Weighted degeneracy and max over U of the average of F_U are monotone under subgraphs. QED.

6. EVIDENCE FOR TARGET (b), AND WHY A PROOF FAILS
6a. Lower side, rigorous. B(M) >= D/8, and B(M) >= the global average of F^-, which is about mu/2 times 0.8. In the model this is about (6.4/(pi S)) log(4h/S^2) times sigma_bar/2. A bound of the form C (log h)^beta/S^gamma + const therefore needs beta >= 1 and gamma <= 1. The exponents beta = gamma = 1 are the best possible. B can't be uniformly bounded at fixed S.
6b. Measured weighted degeneracy D. The script `degeneracy_vs_mu.py` repeats the archive's in-strip constraint definition. Strides 8 and 16 only serve to raise mu. The same-parity exclusion is not claimed there. Entries are (h, S): mu, maximum degree, D.
- M = 3:
 - (1024, 32): 0.174, 5, 2
 - (2048, 32), archive: 0.266, 8, 2
 - (4096, 32), archive: 0.332, 8, 2
 - (512, 16): 0.510, 7, 3
 - (1024, 16): 0.647, 9, 3
 - (2048, 16): 0.810, 11, 3
 - (512, 8): 1.581, 12, 4
 - (1024, 8): 1.910, 15, 4
 - (2048, 8): 2.239, 16, 5
- M = 4:
 - (1024, 32): 0.203, 6, 3
 - (2048, 32), archive: 0.330, 8, 3
 - (1024, 16): 0.841, 10, 3
 - (2048, 16): 1.055, 13, 4
 - (1024, 8): 2.467, 18, 5
 - (2048, 8): 2.863, 22, 6
- M = 6: (1024, 8): 2.281, 18, 7
D grows roughly linearly, by about 1.2 per unit of mu.
6c. Giant cores. At (1024, 8, 3), the 3-core has 33462 vertices, 12.8% of all labels, and 76228 edges. At (2048, 8, 3) it has 183845 vertices, 17.5% of all labels. The graph forms a giant 3-core at mu about 1.9. An Erdos-Renyi graph needs mu about 3.35 for that, so the P graph is more clustered than random.
6d. Factor budgets in the cores (script `factor_vs_degree.py`). At (1024, 8, 3), the average b^- is 2.278 and the average F^- is 1.901, with maxima 10 and 6. At (1024, 16, 3), they are 1.818 and 1.394. In these cores (8) needs M > 8B, which is about 15, while greedy needs only M > D = 4. Criterion (8) loses about a factor of 6 against plain degeneracy. I recommend using weighted degeneracy directly.
6e. Why no proof of an upper bound. A bound on all induced subgraphs needs two things that deterministic counting can't supply:
1. Pseudo-randomness of the Hilbert offsets z_d along the arithmetic slot sets.
2. Control of the clumping in 3d.
Window counting at one label only gives sqrt(h/(SM)) polylog. Hilbert offsets are not anti-concentrated. For d = 4^k, a positive fraction of ranks has the exact displacement (-2^k, 0), and transposed block pairs make j_{r+d} - i_r constant on whole blocks. A per-diagonal fiber of the map r -> j_{r+d} - i_r can have size about N sqrt(d), not O(N). The random shift in T3 fixes the average but gives no tail bounds, because it is a single random variable with h/2 values.

7. TARGET (c) AND THE TRADE-OFF
7a. Unconditional results.
- If S is a power of two with S^2/4 + 1 > h - 1, there are no P constraints and M = 1 works (T1). The width is O(h^{5/2}).
- The archive gives M = h^{1/3+o(1)}. With Shiu, this improves to M = O((h/S)^{1/3} (log h)^{4/3}) and width O(h^{7/3} (log h)^{4/3}) at S = 32.
- No bounded-M theorem with polylogarithmic S is proved.
7b. Conditional theorem, proof. Reverse peeling gives each label at most D earlier-assigned constraints. Each one forbids at most one choice, so M > D suffices.
- In (i), M > c0 + c1 mu_hat(32, h) >= D.
- In (ii), S0 >= (16 c1/pi)(log 4h + 1) gives c1 mu_hat(S0, h) <= 1, because log(4h/S0^2) + 1 <= log(4h) + 1. So D <= c0 + 1 < floor(c0) + 2 = M0. S0 is a power of two and at least 32, which preserves the same-parity exclusion.
The width is below S M Q^2 = O(h^2 log h) in both cases. QED, given H.
7c. Trade-off (model and data, heuristic). D is about 2 + 1.2 mu, with mu about (16/(pi S)) log(4h/S^2) times sigma_bar/2. Greedy needs about M >= 3 + 1.2 mu. The width is proportional to S M, which is about 3S + 6 log h. That is minimal at S = 32 with M = Theta(log h). Bounded S and M fail because mu -> infinity like log h. S = (log h)^c with c < 1 also fails, because mu is about (log h)^{1-c}.
Optimal assignment, not only greedy, has a random-CSP threshold of about mu = Theta(M log M). Under that threshold the best case is S M about log h/log log h. In every version the P family alone predicts width h^2 (log h)^{1-o(1)} to h^2 log h. That beats 1.3108 if mixed supports and the sea also succeed, but it is not O(h^2).
Extrapolated failure heights (S = 32): in the M = 3 data, D reached 3 at mu about 0.5. The model reaches mu = 0.5 at h about 2^14. M = 4 reaches D = 4 at mu about 1.06, which corresponds to h about 2^20. These are extrapolations from S = 8 and S = 16 data.
7d. Failed shortcut. With the two extreme choices xi in {0, M-1}, only delta in {0, +-(M-1)} can bind, and the problem becomes exact 2-SAT (script `twosat_extremes.py`, solver checked on toy cases). It is UNSAT at (1024, 8, 3), (1024, 8, 4) and (2048, 32, 3), where 3-choice greedy succeeds. Min-conflicts search on the (1024, 8, 3) core left 12 of 76228 constraints violated after 45 s. That run is inconclusive about 3-choice satisfiability.

Scripts are in `scripts_hb1_p_count/`: `model_vs_census.py`, `model_large_h.py`, `degeneracy_vs_mu.py`, `core_probe.py`, `factor_vs_degree.py` and `twosat_extremes.py`. Each ran in under 60 s. The repository was not touched.

## External results used

- Euclid parametrization of primitive Pythagorean triples (standard).
- Shiu, A Brun-Titchmarsh theorem for multiplicative functions, J. reine angew. Math. 313 (1980), Theorem 1, cited from memory. Hypotheses: f >= 0 multiplicative, f(p^l) <= A^l, f(n) <= B_eps n^eps, and intervals of length y >= x^beta. Conclusion: the interval sum is << (y/log x) exp(sum over p <= x of f(p)/p). Used only in one remark.
- Erdos-Renyi 3-core threshold of about 3.35 and the random 2-SAT threshold of density 1 (standard), used only for comparison.

## Checks

I checked the model against 10 independent counts, with ratios from 0.95 to 1.02 (sections 3c and 4). I verified the 2-SAT solver on toy instances. I ran the degeneracy peeling against the archive's definitions and reproduced its values at S = 32. I proved T1 through T5 and the conditional theorem by hand. Every computation was a sanity check under 60 s.

## Gaps

- No unconditional theorem with bounded M at polylogarithmic S. Hypothesis H (D <= c0 + c1 mu_hat) is unproved, and its constants come from data with mu <= 2.86.
- The mean-degree formula mu ~ (8 sigma_bar/(pi S)) log(4h/S^2) is a model. It is rigorous only as an upper bound for the shifted placement (T3). For the unshifted placement it is validated, not proved, because Hilbert offsets are not anti-concentrated.
- The claim that bounded S and M fail is heuristic. A growing mean degree doesn't imply unsatisfiability for shift constraints. No dense infeasible core is exhibited at S = 32.
- The degeneracy data with mu >= 0.5 use strides 8 and 16 to emulate stride 32 at larger heights. The emulation is not exact.
- The asymptotic constant of V(S,h) (c_V about 0.71) and the lower-order term of mu (1.10/S) are numerical. Only the upper bound in T2 is proved.
- The Shiu-based improvement relies on a theorem I cited from memory without re-reading it. Its implicit constant is not explicit.
- Mixed supports, cross-parity right angles, the sea and the collars are untouched.

## Missing estimate

To get bounded M with S of order log h, which gives width h^2 log h (b = 1), you need a uniform bound D_{S,M}(h) <= c0 + c1 * log(4h/S^2)/S on the weighted degeneracy of the in-strip candidate P multigraph. Proving it needs pseudo-randomness of the Hilbert offsets on arithmetic slot sets, plus control of the path clumping. For m_h = O(h^2), you need more than that: a structural theorem showing that the P system is solvable with bounded M even though its mean degree grows like log h. The archive's factor-one theorem shows this kind of mechanism for one factor. The data (F about 0.8 b in the cores) show that repeated factors are not where the density comes from.

## Next steps

- Test the extrapolated failure points at S = 32: greedy weighted degeneracy 3 for M = 3 near h = 2^14, and 4 for M = 4 near h = 2^20. Use translated patches or a streaming census to stay under 1 GB.
- Retarget this route to width h^2 log h, exponent b = 1, which still beats 1.3108. Fix S = 32, let M = Theta(log h), and try to prove Hypothesis H, starting with the shifted placement of T3.
- Replace criterion (8) with plain weighted degeneracy. In the measured cores, (8) is about 6 times weaker.
- Try an exact or stronger CSP solver on the S = 8 cores to measure the true 3-choice threshold against the greedy threshold.
- Look for a structural choice rule that extends the factor-one path mechanism across factors. The random model says the needed growth in M is only avoidable this way.

